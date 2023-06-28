import disnake
from disnake.ext import commands
from autocomp import ticker_autocomp

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK

from cfg import YOUR_API_KEY


polygon_sdk = AsyncPolygonSDK(YOUR_API_KEY)

class PolygonCMD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.slash_command()
    async def poly(self, inter):
        pass




    @poly.sub_command(name="company_information")
    async def company_info(self, inter:disnake.AppCmdInter, ticker:str=commands.Param(autocomplete=ticker_autocomp)):
        """💠Returns company information for a ticker"""
        await inter.response.defer()

        company_info_data = await polygon_sdk.company_info(ticker)

        cik = company_info_data.cik
        composite_figi = company_info_data.composite_figi
        currency_name = company_info_data.currency_name
        description = company_info_data.description
        homepage_url = company_info_data.homepage_url
        list_date = company_info_data.list_date
        locale = company_info_data.locale
        market = company_info_data.market
        market_cap = company_info_data.market_cap
        name = company_info_data.name
        phone_number = company_info_data.phone_number
        primary_exchange = company_info_data.primary_exchange
        round_lot = company_info_data.round_lot
        share_class_figi = company_info_data.share_class_figi
        share_class_shares_outstanding = float(company_info_data.share_class_shares_outstanding)
        sic_code = company_info_data.sic_code
        sic_description = company_info_data.sic_description
        ticker = company_info_data.ticker

        embed = disnake.Embed(title=f"💠 Company Information  - {ticker} 💠", description=f"```py\n{description}```", url=homepage_url, color=disnake.Colour.dark_magenta())
        embed.add_field(name=f"Codes:", value=f"> CIK#: **{cik}**\n> FIGI: **{composite_figi}**\n> SIC: **{sic_code}**\n> SIC Description: **{sic_description}**", inline=False)
        embed.add_field(name=f"Contact Details:", value=f"> **{name}**\n> **{phone_number}**")
        embed.add_field(name=f"Ticker Info:", value=f"> Primary Exchange: **{primary_exchange}**\n> Listed: **{list_date}**\n> Market: **{market}**")
        embed.add_field(name=f"Trade Info:", value=f"> MarketCap: **${float(market_cap):,}**\n> Shares Outstanding: **{share_class_shares_outstanding:,}**")
        embed.set_thumbnail(await polygon_sdk.get_polygon_logo(ticker))
        embed.add_field(name=f"This command:", value=f"> </poly company_info:1121575902459998329>")
        embed.set_footer(text=f"Data Provided by Polygon.io | Implemented by FUDSTOP")
        await inter.edit_original_message(embed=embed)




    @poly.sub_command()
    async def rsi(self, inter:disnake.AppCmdInter, ticker:str=commands.Param(autocomplete=ticker_autocomp), timespan:str=commands.Param(choices=["minute","hour","day","week","quarter","year"]), window=14):
        """💠Returns the latest RSI value for a ticker with an optional window argument."""
        await inter.response.defer()
        rsi_data = await polygon_sdk.get_rsi(symbol=ticker,timespan=timespan,window=window)
        if rsi_data is not None:
            rsi = rsi_data.rsi_value[0]
            if rsi > 70:
                color = disnake.Colour.dark_red()
            if rsi < 30:
                color = disnake.Colour.dark_green()

            embed=  disnake.Embed(title=f"💠 RSI - {ticker} 💠", description=f"```py\nThe latest RSI value is: {rsi} for the {timespan} timespan.```", color=color)
            embed.add_field(name=f"This command:", value=f"> </poly rsi:1121575902459998329>")
            embed.set_thumbnail(await polygon_sdk.get_polygon_logo(ticker))
            embed.set_footer(text=f"Data Provided by Polygon.io | Implemented by FUDSTOP")
            await inter.edit_original_message(embed=embed)

            
    

def setup(bot:commands.Bot):
    bot.add_cog(PolygonCMD(bot))
    print(f"> Extension {__name__} is ready\n")