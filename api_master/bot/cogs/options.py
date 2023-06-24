import requests
import disnake
from disnake.ext import commands
from time import sleep
from requests.auth import HTTPBasicAuth
import time
import pandas as pd
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK

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
    async def get_near_the_money_options(ctx: disnake.AppCommandInter, tickers:str):
        """Get near the money options for a ticker"""
        prices = await polygon.get_multiple_stock_prices(tickers)
        for price in prices:
            lower_strike = round(price * 0.97)
            upper_strike = round(price * 1.03)


async def setup(bot:commands.Bot):
    await bot.add_cog(Options(bot))
    print(f"> Extension {__name__} is ready\n")