

import aiohttp
from api_master.sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK

from collections import defaultdict
from api_master.sdks.polygon_sdk.universal_snapshot import UniversalOptionSnapshot,UniversalSnapshot
import asyncio
import pandas as pd
   
from api_master.cfg import YOUR_API_KEY, today_str, thirty_days_from_now_str, two_years_from_now_str

poly = AsyncPolygonSDK(YOUR_API_KEY)
async def get_data():
    ticker = "SPX"

    def chunk_list(input_list, chunk_size):
        """Yield successive n-sized chunks from a list."""
        for i in range(0, len(input_list), chunk_size):
            yield input_list[i:i + chunk_size]
    if ticker.startswith("SPX"): #check if the ticker is SPX - must be queried differently
        price = await poly.get_index_price(ticker)
        lower_strike = round(price) * 0.95
        upper_strike = round(price) * 1.00
        print(f"SPX TICKER: {ticker}: {lower_strike}, {price}, {upper_strike}")
        
        async with aiohttp.ClientSession() as session:
            initial_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte={thirty_days_from_now_str}&limit=250&apiKey={YOUR_API_KEY}"
            async with session.get(initial_url) as resp:
                
                results = await poly._request_all_pages(initial_url)
                if results is not None:
                    
                    option_data = UniversalOptionSnapshot(results)


                    
                    # Assuming option_data.ticker gives a list of tickers
      
                    symbols_list = option_data.ticker
      
                    chunks = list(chunk_list(symbols_list, 250))

                    all_dfs = []
                    for chunk in chunks:
                        chunk = str(chunk).replace("'","").replace(']','').replace('[','').replace(' ','')
                        print(chunk)
                        async with session.get(f"https://api.polygon.io/v3/snapshot?ticker.any_of={chunk}&apiKey={YOUR_API_KEY}") as response:
                            near_money = await response.json(content_type=None)
                            near_money_results = near_money['results']
                            atm_data = UniversalSnapshot(near_money_results)
                            first_row = atm_data.df.iloc[0]  # Extract the first row of the DataFrame
                            all_dfs.append(first_row)

                    # Convert the list of Series to DataFrame
                    df = pd.concat(all_dfs, axis=1).transpose().reset_index(drop=True)

                    # If the DataFrame is not empty, save it to a CSV file
                    if not df.empty:
                        df.to_csv('all_dataframes_spy.csv')
                        print(df)
                    else:
                        print("No dataframes were found.")
asyncio.run(get_data())