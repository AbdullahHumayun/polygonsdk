import disnake
from disnake.ext import commands
from autocomp import ticker_autocomp
import numpy as np
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY, today_str
from sdks.polygon_sdk.universal_snapshot import UniversalOptionSnapshot,UniversalSnapshot
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
polygon = AsyncPolygonSDK(YOUR_API_KEY)
poly = PolygonOptionsSDK(YOUR_API_KEY)
from tabulate import tabulate
import aiohttp
import asyncio
import pandas as pd

class Track(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.slash_command()
    async def track(self, inter):
        pass


    @track.sub_command()
    async def support_resistance(self, inter:disnake.AppCmdInter, ticker:str=commands.Param(autocomplete=ticker_autocomp)):
        """Track volume vs OI for calls and puts for resistance monitoring"""
        await inter.response.defer()
        while True:
            MAX_CONCURRENCY = 60

            ticker = ticker.upper()

            async def fetch_data(session, tickers):
                async with session.get(f"https://api.polygon.io/v3/snapshot?ticker.any_of={tickers}&apiKey={YOUR_API_KEY}") as response:
                    try:
                        near_money = await response.json(content_type=None)
                        near_money_results = near_money['results']
                        atm_data = UniversalOptionSnapshot(near_money_results)
                        return atm_data.df.sort_values('IV', ascending=True)
                    except Exception as e:
                        print(f"Error processing tickers: {tickers}. Error: {e}")
                        return pd.DataFrame()

            async def process_option_data(grouped_df, session, sem):
                tasks = []
                for _, group in grouped_df:
                    group_tickers = group['ticker'].tolist()
                    if not group_tickers:
                        continue
                    tickers_string = ','.join(group_tickers)
                    task = asyncio.create_task(fetch_data(session, tickers_string))
                    tasks.append(task)

                results = []
                async with sem:
                    for future in asyncio.as_completed(tasks):
                        result = await future
                        results.append(result)

                return results

            async with aiohttp.ClientSession() as session:
                sem = asyncio.Semaphore(MAX_CONCURRENCY)

                while True:
                    if ticker.startswith("SPX"):
                        price = await polygon.get_index_price(ticker)
                        lower_strike = round(price) * 0.99
                        upper_strike = round(price) * 1.01
                    else:
                        price = await poly.get_stock_price(ticker)
                        lower_strike = round(price) * 0.99
                        upper_strike = round(price) * 1.01
                    print(f"SPX TICKER: {ticker}: {lower_strike}, {price}, {upper_strike}")

                    initial_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte=2023-09-30&limit=250&apiKey={YOUR_API_KEY}"
                    results = await poly._request_all_pages(initial_url)

                    if results is not None:
                        option_data = UniversalOptionSnapshot(results)
                        calls = option_data.df[option_data.df['type'] == 'call']
                        puts = option_data.df[option_data.df['type'] == 'put']


                        nearest_expiry = min(option_data.df['exp'])

                        # Filter by nearest expiry and get relevant columns
                        filtered_calls = calls[calls['exp'] == nearest_expiry][['vol', 'strike', 'price']]
                        filtered_puts = puts[puts['exp'] == nearest_expiry][['vol', 'strike']]

                        # Rename volume column for clarity
                        filtered_calls = filtered_calls.rename(columns={'vol': 'call_volume'})
                        filtered_puts = filtered_puts.rename(columns={'vol': 'put_volume'})

                        # Merge the call and put dataframes based on strike price
                        merged_df = pd.merge(filtered_calls, filtered_puts, on='strike', how='outer')
        
                        # Fill NAs with 0 (if any)
                        merged_df = merged_df.fillna(0)
                        merged_df['comparison'] = np.where(merged_df['put_volume'] > merged_df['call_volume'], '✅ Supt.', '❌ Res.')
                        table = tabulate(merged_df, headers='keys', tablefmt='fancy', showindex=False)
                        embed = disnake.Embed(title=f"Support + Resistance Tracker", description=f"```{table}```", color=disnake.Colour.random())
                        embed.add_field(name=f"Info:", value=f"```py\nViewing calls vs put volume for {ticker} in real time. A Check = support. An X = resistance.```")
                        await inter.edit_original_message(embed=embed)

def setup(bot:commands.Bot):
    bot.add_cog(Track(bot))
    print(f"> Extension {__name__} is ready\n")