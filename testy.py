

import aiohttp
from api_master.sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from api_master.sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from collections import defaultdict
from api_master.sdks.polygon_sdk.universal_snapshot import UniversalOptionSnapshot
from api_master.sdks.polygon_sdk.universal_snapshot import UniversalSnapshot
import asyncio
import pandas as pd
   
from api_master.cfg import YOUR_API_KEY, today_str, thirty_days_from_now_str, two_years_from_now_str
opts = PolygonOptionsSDK(YOUR_API_KEY)
poly = AsyncPolygonSDK(YOUR_API_KEY)
# async def get_data():
#     ticker = "SPX"

#     def chunk_list(input_list, chunk_size):
#         """Yield successive n-sized chunks from a list."""
#         for i in range(0, len(input_list), chunk_size):
#             yield input_list[i:i + chunk_size]
#     if ticker.startswith("SPX"): #check if the ticker is SPX - must be queried differently
#         price = await poly.get_index_price(ticker)
#         lower_strike = round(price) * 0.95
#         upper_strike = round(price) * 1.00
#         print(f"SPX TICKER: {ticker}: {lower_strike}, {price}, {upper_strike}")
        
#         async with aiohttp.ClientSession() as session:
#             initial_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte={thirty_days_from_now_str}&limit=250&apiKey={YOUR_API_KEY}"
#             async with session.get(initial_url) as resp:
                
#                 results = await poly._request_all_pages(initial_url)
#                 if results is not None:
                    
#                     option_data = UniversalOptionSnapshot(results)


                    
#                     # Assuming option_data.ticker gives a list of tickers
      
#                     symbols_list = option_data.ticker
      
#                     chunks = list(chunk_list(symbols_list, 250))

#                     all_dfs = []
#                     for chunk in chunks:
#                         chunk = str(chunk).replace("'","").replace(']','').replace('[','').replace(' ','')
#                         print(chunk)
#                         async with session.get(f"https://api.polygon.io/v3/snapshot?ticker.any_of={chunk}&apiKey={YOUR_API_KEY}") as response:
#                             near_money = await response.json(content_type=None)
#                             near_money_results = near_money['results']
#                             atm_data = UniversalSnapshot(near_money_results)
#                             first_row = atm_data.df.iloc[0]  # Extract the first row of the DataFrame
#                             all_dfs.append(first_row)

#                     # Convert the list of Series to DataFrame
#                     df = pd.concat(all_dfs, axis=1).transpose().reset_index(drop=True)

#                     # If the DataFrame is not empty, save it to a CSV file
#                     if not df.empty:
#                         df.to_csv('all_dataframes_spy.csv')
#                         print(df)
#                     else:
#                         print("No dataframes were found.")
# asyncio.run(get_data())


async def find_skew(atm_options):
    async with aiohttp.ClientSession() as session:
        url=f"https://api.polygon.io/v3/snapshot?ticker.any_of={atm_options}&limit=250&apiKey={YOUR_API_KEY}"
        async with session.get(url) as resp:
            r = await resp.json()
            data = r['results'] if 'results' in r else None
            if data is not None:
                try:
                    return UniversalSnapshot(data)
                except KeyError:
                    return "N/A"

from tabulate import tabulate
from api_master.sdks.polygon_sdk.masterSDK import MasterSDK
sdk = MasterSDK()
async def main():
    tickers = ['TSLA', 'IWM', 
                'AAPL', 'NVDA', 'AMD', 'MU', 'AMZN', 
                'AMC', 'VIX', 'SPCE', 'HYG', 'SOFI', 
                'MARA', 'RIVN', 'LCID', 'CCL', 'F', 'META', 
                'MSFT', 'BAC', 'EEM', 'CVNA', 'JPM', 'TQQQ', 
                'GLD', 'BABA', 'PLTR', 'UBER', 'COIN', 'TLT', 
                'INTC', 'GOOGL', 'EWZ', 'NFLX', 'DIS', 'SQQQ', 
                'NKE', 'CHPT', 'PYPL', 'XLF', 'SNOW', 'AAL', 
                'GOOG', 'OXY', 'WBD', 'RIOT', 'AI', 
                'BB',  
                'TNA', 'WMT', 'KO']
    call_rows = []  # List to store first call rows for each ticker
    put_rows = []  # List to store first put rows for each ticker
    
    for ticker in tickers:
        atm_contracts = await sdk.get_near_the_money(ticker)

        atm_data = await find_skew(atm_contracts)
        if atm_data is not None and atm_data is not "N/A":
            print(atm_data)
            df = atm_data.df.sort_values(['IV'], ascending=True)

            first_call = df[df['C/P'] == 'call'].iloc[[0]]
            first_put = df[df['C/P'] == 'put'].iloc[[0]]
            # Modify the '🗓️' column to remove the '2023-' prefix
            first_call['🗓️'] = first_call['🗓️'].str[5:]
            first_put['🗓️'] = first_put['🗓️'].str[5:]
            # Add 'Emoji' column to the first call rows and first put rows
            first_call['Emoji'] = first_call.apply(lambda row: '🔥' if row['Price'] > row['Skew'] else '🟢', axis=1)
            first_put['Emoji'] = first_put.apply(lambda row: '🔥' if row['Price'] > row['Skew'] else '🟢', axis=1)

            call_rows.append(first_call[["Sym", "C/P", "Price", "Skew", "🗓️", "IV", "Emoji"]])
            put_rows.append(first_put[["Sym", "C/P", "Price", "Skew", "🗓️", "IV", "Emoji"]])


    # Combine all first call rows and first put rows into single dataframes
    call_df = pd.concat(call_rows)
    put_df = pd.concat(put_rows)

    # Tabulate the first call rows and first put rows
    call_table_str = tabulate(call_df, headers="keys", tablefmt="fancy_grid", showindex=False)
    put_table_str = tabulate(put_df, headers="keys", tablefmt="fancy_grid", showindex=False)

    # Print the tables
    print("First Call Rows:")
    print(call_table_str)
    print("\nFirst Put Rows:")
    print(put_table_str)

asyncio.run(main())