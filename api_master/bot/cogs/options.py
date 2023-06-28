import requests
import disnake
from disnake.ext import commands
from time import sleep
from requests.auth import HTTPBasicAuth
import time
import pandas as pd
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from menus.embedmenus import AlertMenus
from sdks.polygon_sdk.mapping_dicts import OPTIONS_EXCHANGES, option_condition_dict
from sdks.helpers.helpers import human_readable
from cfg import YOUR_API_KEY
polygon_options = PolygonOptionsSDK(YOUR_API_KEY)
polygon = AsyncPolygonSDK(YOUR_API_KEY)

class Options(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command()
    async def options(self, inter):
        pass

    @options.sub_command()
    async def fetch_entire_chain(ctx: disnake.AppCommandInter, tickers: str):
        """Fetches the latest up-to-date data for every option for any ticker across all expirations."""
        
        tickers = tickers.split(',')
        await ctx.response.defer()

        combined_data = []  # List to store all dataframes

        for ticker in tickers:
            all_options = await polygon_options.get_option_chain_all(ticker)

            df = pd.DataFrame(all_options.data_dict)
            combined_data.append(df)

        if combined_data:
            combined_df = pd.concat(combined_data, ignore_index=True)
            combined_df.to_csv('files/options/ticker_chains/all_tickers_combined.csv', index=False)
            await ctx.send("Data Ready for all tickers", file=disnake.File('files/options/ticker_chains/all_tickers_combined.csv'))
        else:
            await ctx.send("No data available for the given tickers.")


    @options.sub_command()
    async def all_market_options(self, inter:disnake.AppCmdInter, sort_by: str=commands.Param(choices=["ticker","contract_type", "expiration_date","strike_price","delta","gamma","theta","vega","day_volume","open_interest","implied_volatility","day_change_percent","last_trade_conditions","ask_size","bid_size", "underlying_ticker"])):
        """Returns all options market-wide thru 07/30/2023 with custom sorting."""

        df = pd.read_csv('files/options/all_options_data.csv').sort_values(sort_by,ascending=False).dropna(how="any") #you must download this spreadsheet from the "get_latest_options_data.py" file.
        embeds = []
        for i,row in df.iterrows():
            option_symbol = human_readable(row['ticker'])
            break_even_price = row['break_even_price']
            contract_type = row['contract_type']
            exercise_style = row['exercise_style']
            expiry = row['expiration_date']
            strike = row['strike_price']
            delta = round(float(row['delta'])*100,2)
            vega = round(float(row['vega']),2)
            theta = round(float(row['theta']),2)
            gamma = round(float(row['gamma']),2)
            iv = round(float(row['implied_volatility'])*100,2)
            oi = float(row['open_interest'])
            ask = row['ask']
            bid = row['bid']
            bid_size = float(row['bid_size'])
            ask_size = float(row['ask_size'])
            mid = row['midpoint']
            trade_size = float(row['last_trade_size'])
            exchange = OPTIONS_EXCHANGES.get(row['last_trade_exchange'])
            last_price = row['last_trade_price']
            conditions = option_condition_dict.get(row['last_trade_conditions'])
            day_change = row['day_change']
            day_change_percent = row['day_change_percent']
            day_close = row['day_close']
            day_high = row['day_high']
            day_low = row['day_low']
            day_open = row['day_open']
            prev_close = row['day_previous_close']
            day_volume = float(row['day_volume'])
            day_vwap = row['day_vwap']
            change_to_breakeven = row['change_to_break_even']
            price = row['price']
            underlying_ticker = row['underlying_ticker']
            if day_volume > oi:
                unusual = "✅"
            else:
                unusual = "❌"
            embed = disnake.Embed(title=f"All Market Options", color=disnake.Colour.dark_gold())
            embed.add_field(name=f"Option Details:", value=f"> Symbol: **{option_symbol}**\n> Break-Even Price: $**{break_even_price}**\n> Exercise Style: **{exercise_style}**")
            embed.add_field(name=f"Day Performance:", value=f"> Open: **${day_open}**\n> High: **${day_high}**\n> Low: **${day_low}**\n> Close: **${day_close}**\n> Change%: **{day_change_percent}%**\n> Dollar Change: **${day_change}**\n> Previous Close: **${prev_close}**\n> VWAP: **${day_vwap}**", inline=False)
            embed.add_field(name=f"Greeks:",value=f"> Delta: **{delta}%** of closing ITM.\n> Gamma: **{gamma}**\n> Theta: **{theta}**\n> Vega: **{vega}**\n> IV: **{iv}**")
            embed.add_field(name=f"Quote Info:", value=f"> Bid: **${bid}**\n> Mid: **${mid}**\n> Ask: **${ask}**\n> Bid Size: **{bid_size}**\n> Ask Size: **{ask_size}**")
            embed.add_field(name=f"Last Trade:", value=f"> Size: **{trade_size:,}\n> Price: **${last_price}**\n> Exchange: **{exchange}**\n> Conditions: **{conditions}**")
            embed.add_field(name=f"Volume & OI:",value=f"> Volume: **{day_volume:,}**\n> Open Interest: **{oi:,}**\n\n> **Unusual: {unusual}**")
            embed.add_field(name=f"Underlying Asset:", value=f"> Ticker: **{underlying_ticker}**\n> Change to Break-even: **{change_to_breakeven}**\n> Underlying Price: **${price}**")
            embed.add_field(name=f"Sorted By:", value=f"```py\nData is currently being sorted by {sort_by}```", inline=False)
            embeds.append(embed)
        view = AlertMenus(embeds)
        df.to_csv('files/options/all_options_data_group.csv')
        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, label=f"Download")
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File('files/options/all_options_data.csv'))
        view.add_item(button)


        await inter.edit_original_message(view=view, embed=embeds[0])



def setup(bot:commands.Bot):
    bot.add_cog(Options(bot))
    print(f"> Extension {__name__} is ready\n")