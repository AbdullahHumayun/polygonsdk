import disnake
from disnake.ext import commands
import pandas as pd
from autocomp import ticker_autocomp, multiplier_autocomp
import aiohttp
from views.learnviews import AlertMenus
from tabulate import tabulate
from disnake import ui, ButtonStyle
from cfg import today_str, YOUR_API_KEY
from sdks.polygon_sdk.clients.AggregatesClient import AggregatesData,AggregatesResponse
from sdks.polygon_sdk.clients.TradesClient import TradeData,TradeResponse
class Paginator(ui.View):
    def __init__(self, pages):
        super().__init__()
        self.pages = pages
        self.current_page = 0

    async def on_timeout(self) -> None:
        for button in self.children:
            button.disabled = True
        await self.message.edit(view=self)

    @ui.button(style=disnake.ButtonStyle.green, label="Previous", custom_id="on_prev")
    async def on_prev(self, button: ui.Button, interaction: disnake.AppCmdInter):
        if self.current_page == 0:
            return
        self.current_page -= 1
        await interaction.response.edit_message(embed=self.pages[self.current_page], view=self)

    @ui.button(style=disnake.ButtonStyle.green, label="Next",custom_id="on_next")
    async def on_next(self, button: ui.Button, interaction: disnake.AppCmdInter):
        if self.current_page == len(self.pages) - 1:
            return
        self.current_page += 1
        await interaction.response.edit_message(embed=self.pages[self.current_page], view=self)


class Today(commands.Cog):
    def __init__(self, bot):
        self.bot=bot



    @commands.slash_command()
    async def today(self, inter):
        pass

    @today.sub_command()
    async def price_changes_by_timespan(inter: disnake.AppCmdInter,ticker:str=commands.Param(autocomplete=ticker_autocomp), multiplier:str=commands.Param(autocomplete=multiplier_autocomp), timespan:str=commands.Param(choices=['minute','hour','day'])):

        """View today's price changes by minute, hour, or the whole day."""
        await inter.response.defer()
        max_rows = 50
        async with aiohttp.ClientSession() as session:
            url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/range/{multiplier}/{timespan}/{today_str}/{today_str}?adjusted=true&sort=desc&limit=5000&apiKey={YOUR_API_KEY}'
            print(url)
            async with session.get(url) as resp:
                
                data = await resp.json()
            
                # Create PolygonResponse object
                results = [AggregatesData(**result) for result in data['results']]
                response = AggregatesResponse(
                    adjusted=data['adjusted'],
                    next_url=data['next_url'] if 'next_url' in data else None,
                    queryCount=data['queryCount'],
                    request_id=data['request_id'],
                    results=results,
                    resultsCount=data['resultsCount'],
                    status=data['status'],
                    ticker=data['ticker']
                )
                
                # Call functions
                avg_closing_price = await response.average_closing_price()
                date_range_res = await response.date_range()
                high_low_closing_prices = await response.highest_and_lowest_closing_prices()
                total_vol = await response.total_volume()
                    # Filter out entries with no change
                daily_price_change = await response.daily_price_change(timespan=timespan, return_df=True)
                # Split your data into pages and create an embed for each one
                pages = []
                for i in range(0, len(daily_price_change), max_rows):
                    page = daily_price_change.iloc[i:i+max_rows]
                    table = tabulate(page, headers='keys', tablefmt='fancy', showindex=False)
                    embed = disnake.Embed(title=f"Price Changes - {timespan} | {ticker}", description=f"```{table}```")
                    embed.add_field(name=f"Info:", value=f"> You are viewing the price changes that occurred every **{multiplier} {timespan}** for today, **{today_str}.**")
                    pages.append(embed)

                # Create a Paginator and send the first page
                view = Paginator(pages)
                await inter.edit_original_message(embed=pages[0], view=view)

    @today.sub_command()
    async def average_traded(self,inter:disnake.AppCmdInter, ticker:str=commands.Param(autocomplete=ticker_autocomp), date:str=today_str):
        """Returns the average trade price on the day for a ticker"""
        await inter.response.defer()
        async with aiohttp.ClientSession() as session:
            url=f"https://api.polygon.io/v3/trades/{ticker}?timestamp={today_str}&apiKey={YOUR_API_KEY}"
            async with session.get(url) as resp:
                data = await resp.json()
                # Create TradeResult objects for each result
                results = [TradeData(**result) for result in data['results']]
                # Create a Response object
                response = TradeResponse(
                    next_url=data['next_url'] if 'next_url' in data else None,
                    request_id=data['request_id'],
                    results=results,
                    status=data['status']
                )
                # Call the get_average_trade_price method and send the result
                average_price = await response.get_average_trade_price()
                await inter.edit_original_message(f"The average trade price for {ticker} today is {average_price}")




def setup(bot: commands.Bot):
    bot.add_cog(Today(bot))
    print(f"Plot commands ready!")