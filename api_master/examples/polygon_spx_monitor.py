import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
import asyncio
from tabulate import tabulate
from cfg import YOUR_API_KEY
from sdks.polygon_sdk.universal_snapshot import UniversalOptionSnapshot, UniversalSnapshot
poly = AsyncPolygonSDK(YOUR_API_KEY)
import aiohttp
import csv
from cfg import two_days_from_now_str, today_str
async def main():
    while True:
        ticker="SPX"
        price = await poly.get_index_price(ticker)
        print(price)

        lower_strike = round(price * 0.98)
        upper_strike = round(price * 1.02)
        print(lower_strike)
        print(upper_strike)
        

        async with aiohttp.ClientSession() as session:
            initial_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte={two_days_from_now_str}&limit=250&apiKey={YOUR_API_KEY}"
            async with session.get(initial_url) as resp:
                data = await resp.json()
                results = data['results']
                if results is not None:
                    option_data = UniversalOptionSnapshot(results)
                    symbols = str(option_data.ticker).replace("'","").replace(']','').replace('[','').replace(' ','')
                    
                    async with aiohttp.ClientSession() as session:
                        async with session.get(f"https://api.polygon.io/v3/snapshot?ticker.any_of={symbols}&limit=1&apiKey={YOUR_API_KEY}") as response:
                            near_money = await response.json()
                            near_money_results = near_money['results']
                            if near_money_results is not None:
                                atm_data = UniversalSnapshot(near_money_results)

                                df = atm_data.df.sort_values('IV', ascending=True)
                                call_df = df[df['Type'] == 'call'].sort_values('IV', ascending=True)
                                put_df = df[df['Type'] == 'put'].sort_values('IV', ascending=True)
                                call_df.to_csv('test1.csv')
                                put_df.to_csv('test2.csv')

                                print(call_df.iloc[[0]])
                                print(put_df.iloc[[0]])

                                call_table = call_df[['Price','Strike', 'IV', 'Exp', 'Type', 'Vol', 'Open Interest', 'Close', 'High', 'Open', 'Low', 'Midpoint', 'Bid', 'Bid Size', 'Ask', 'Ask Size', 'Last Trade Conditions', 'Delta', 'Gamma', 'Theta', 'Vega', 'Change Percent']].iloc[[1]]
                                put_table = put_df[['Price','Strike', 'IV', 'Exp', 'Type', 'Vol', 'Open Interest', 'Close', 'High', 'Open', 'Low', 'Midpoint', 'Bid', 'Bid Size', 'Ask', 'Ask Size', 'Last Trade Conditions', 'Delta', 'Gamma', 'Theta', 'Vega', 'Change Percent']].iloc[[1]]
                                # Remove the year portion from the 'Exp' column
                                call_table['Exp'] = call_table['Exp'].str.replace(r'^\d+-', '', regex=True)
                                put_table['Exp'] = put_table['Exp'].str.replace(r'^\d+-', '', regex=True)
                                # Calculate the price based on the strike price and option type

                                # Print the modified tables
                                print(call_table)
                                print(put_table)
                                # Convert the selected rows to a list of lists
                                call_rows = call_table.values.tolist()
                                put_rows = put_table.values.tolist()

                                # Create a table with the selected columns for call_df and put_df
                                table = call_rows + put_rows
                                table_str = tabulate(table, headers=call_table.columns, tablefmt="grid")
                                print(table_str)
                                # Print the table using tabulate
                                print(tabulate(table, headers=call_table.columns, tablefmt="grid"))
                                # Write the tabulate table to a CSV file
                                with open('skew_data.csv', mode='a', newline='') as outfile:
                                    writer = csv.writer(outfile)
                                    writer.writerows(table)  # Write the table rows


asyncio.run(main()) 

