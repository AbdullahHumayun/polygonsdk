import disnake
from disnake.ext import commands
from autocomp import ticker_autocomp
import numpy as np
from sdks.polygon_sdk.masterSDK import MasterSDK
from discord_webhook import DiscordEmbed,DiscordWebhook
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
master = MasterSDK()
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

                call_leader = True  # Variable to track the call leadership
                put_leader = False  # Variable to track the put leadership
                leader_strike = None 
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
                        # Previous leadership status
                        previous_call_leader = call_leader
                        previous_put_leader = put_leader

                        # Determine the current leadership based on volume comparison
                        if merged_df['call_volume'].sum() > merged_df['put_volume'].sum():
                            call_leader = True
                            put_leader = False
                        else:
                            call_leader = False
                            put_leader = True
                        # Check if the leadership has changed

                            
                        # Check if the leadership has changed
                        if previous_call_leader and put_leader:
                            # Calls were leading, but now puts have taken the lead
                            print("Puts have overtaken calls as the leader!")
                            leader_strike = merged_df.loc[merged_df['put_volume'].idxmax(), 'strike']
                            webhook = DiscordWebhook('https://discord.com/api/webhooks/1003909050766983189/yj4aP3v7TooemmBJo57pFT9TceNDPedOks0MFMPRCi6Cx_KFAq6K1S0-l0_pv6q3LIIW', content=f"The strike price at which the change occurred: {leader_strike}")
                            await webhook.execute()
                            print(f"The strike price at which the change occurred: {leader_strike}")
                            # Additional actions or notifications can be added here

                        if previous_put_leader and call_leader:
                            # Puts were leading, but now calls have taken the lead
                            print("Calls have overtaken puts as the leader!")
                            leader_strike = merged_df.loc[merged_df['call_volume'].idxmax(), 'strike']
                            webhook = DiscordWebhook('https://discord.com/api/webhooks/1003909050766983189/yj4aP3v7TooemmBJo57pFT9TceNDPedOks0MFMPRCi6Cx_KFAq6K1S0-l0_pv6q3LIIW', content=f"The strike price at which the change occurred: {leader_strike}")
                            await webhook.execute()
                            print(f"The strike price at which the change occurred: {leader_strike}")
                        table = tabulate(merged_df, headers='keys', tablefmt='fancy', showindex=False)
                        embed = disnake.Embed(title=f"Support + Resistance Tracker", description=f"```{table}```", color=disnake.Colour.random())
                        embed.add_field(name=f"Info:", value=f"```py\nViewing calls vs put volume for {ticker} in real time. A Check = support. An X = resistance.```")
                        await inter.edit_original_message(embed=embed)
    @track.sub_command()
    async def rsi(self, inter:disnake.AppCmdInter):
        await inter.response.defer()
        await master.scan_all_rsi()
        await inter.edit_original_message(file=disnake.File('rsi_values.csv'))
        await inter.send(f"> Market finished scanning all RSIs across all timeframes.")
           

    @track.sub_command()
    async def volume_oi(self, inter:disnake.AppCmdInter,tickers:str):
        """Track volume, oi, and IV skew for multiple tickers"""
        tickers = tickers.split(',')
        await inter.response.defer()
        table_data = []

        for ticker in tickers:
            atm_calls, atm_puts = await poly.get_near_the_money_options(ticker)
            if ticker.startswith("SPX"):
                price = await poly.get_index_price(ticker)
            else:
                price = await poly.get_stock_price(ticker)

            first_row_volume_calls = atm_calls.iloc[0]['Vol']
            first_row_volume_puts = atm_puts.iloc[0]['Vol']
            first_row_oi_calls = atm_calls.iloc[0]['OI']
            first_row_oi_puts = atm_puts.iloc[0]['OI']
            first_row_iv_puts = atm_puts.iloc[0]['IV']
            first_row_iv_calls = atm_calls.iloc[0]['IV']
            first_row_iv_puts = atm_puts.iloc[0]['Strike']
            first_row_iv_calls = atm_calls.iloc[0]['Strike']

            first_row_exp_calls = atm_calls.iloc[0]['🗓️']
            first_row_exp_puts = atm_puts.iloc[0]['🗓️']
            first_row_skew_calls = atm_calls.iloc[0]['Skew']
            first_row_skew_puts = atm_puts.iloc[0]['Skew']
            skew_check = ''
            if first_row_skew_calls > price and first_row_skew_puts > price:
                skew_check = '✅'
            
            elif first_row_skew_calls < price and first_row_skew_puts < price:
                skew_check = '✅'
            else:
                skew_check = '❌'
            data_dict = {
                'Sym': ticker,
                'pVol': first_row_volume_puts,
                'pOI': first_row_oi_puts,
                'pSkew': f"{first_row_skew_puts} {skew_check}",
                '💲': price,
                'cSkew': f"{first_row_skew_calls} {skew_check}",
                'cOI': first_row_oi_calls,
                'cVOL': first_row_volume_calls,
            }


            table_data.append(data_dict)

        df = pd.DataFrame(table_data)
        table = tabulate(df, headers='keys', tablefmt='plain', showindex=False)
        embed=disnake.Embed(title=f"Volume & OI Tracker", description=f"```{table}```", color=disnake.Colour.random())
        await inter.send(embed=embed)



    


def setup(bot:commands.Bot):
    bot.add_cog(Track(bot))
    print(f"> Extension {__name__} is ready\n")