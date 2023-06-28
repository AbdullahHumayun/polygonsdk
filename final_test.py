
import aiohttp
from api_master.sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK

from collections import defaultdict
from api_master.sdks.polygon_sdk.universal_snapshot import UniversalOptionSnapshot,UniversalSnapshot
import asyncio
import pandas as pd
from tabulate import tabulate
from api_master.cfg import YOUR_API_KEY, today_str, thirty_days_from_now_str, two_years_from_now_str

poly = AsyncPolygonSDK(YOUR_API_KEY)

async def get_data():
    ticker = "SPY"

    def chunk_list(input_list, chunk_size):
        """Yield successive n-sized chunks from a list."""
        for i in range(0, len(input_list), chunk_size):
            yield input_list[i:i + chunk_size]

    if ticker.startswith("SPX"):
        price = await poly.get_index_price(ticker)
        lower_strike = round(price) * 0.97
        upper_strike = round(price) * 1.03
    else:
        price = await poly.get_stock_price(ticker)
        lower_strike = round(price) * 0.85
        upper_strike = round(price) * 1.15
    print(f"SPX TICKER: {ticker}: {lower_strike}, {price}, {upper_strike}")
    
    async with aiohttp.ClientSession() as session:
        initial_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte={thirty_days_from_now_str}&limit=250&apiKey={YOUR_API_KEY}"
        
        results = await poly._request_all_pages(initial_url)
        if results is not None:
            
            option_data = UniversalOptionSnapshot(results)
            
            #split the data into a calls and puts dataframe

            calls = option_data.df[option_data.df['type'] == 'call']
            puts = option_data.df[option_data.df['type'] == 'put']
            calls_grouped = calls.groupby('exp')
            puts_grouped = puts.groupby('exp')
            async def process_grouped_tickers(grouped_df, session):
                results = []
                for _, group in grouped_df:
                    group_tickers = group['ticker'].tolist()
                    if not group_tickers:  # Handle case where group_tickers is empty
                        continue
                    tickers_string = ','.join(group_tickers)
                    async with session.get(f"https://api.polygon.io/v3/snapshot?ticker.any_of={tickers_string}&apiKey={YOUR_API_KEY}") as response:
                        try:
                            near_money = await response.json(content_type=None)
                            near_money_results = near_money['results']
                            atm_data = UniversalSnapshot(near_money_results)
                            results.append(atm_data.df.sort_values('IV', ascending=True))
                        except Exception as e:
                            print(f"Error processing tickers_string: {tickers_string}. Error: {e}")
                return results

        calls_results = await process_grouped_tickers(calls_grouped, session)
        puts_results = await process_grouped_tickers(puts_grouped, session)
        calls_results_df = pd.concat(calls_results)
        puts_results_df = pd.concat(puts_results)
        # Combine call and put results into one DataFrame
        all_results_df = pd.concat([calls_results_df, puts_results_df])

        # Group the combined DataFrame by 'Exp' column
        grouped = all_results_df.groupby('Exp', as_index=False)
        first_rows = grouped.first()
        selected_columns_df = first_rows[['Exp', 'IV', 'Strike', 'Price', 'Vol']]
        print(selected_columns_df)














                #     # Sort the DataFrames by 'IV'
                #     calls_sorted = calls.sort_values(by='IV', ascending=False)
                #     puts_sorted = puts.sort_values(by='IV', ascending=False)

                #     # Group by 'expiry' and select the first row for each group

                #     calls_grouped = calls_sorted.groupby('expiry', as_index=False)
                #     puts_grouped = puts_sorted.groupby('expiry', as_index=False)

                #     first_calls = calls_grouped.first()
                #     first_puts = puts_grouped.first()   
                #     # Select only the specific columns
                #     first_calls = first_calls[['sym', 'expiry', 'IV', 'strike', 'contract_type']]
                #     first_puts = first_puts[['sym', 'expiry', 'IV', 'strike', 'contract_type']]

                #     # Convert the DataFrames to tabulated strings
                #     calls_table = tabulate(first_calls, headers='keys', tablefmt='psql', showindex=False)
                #     puts_table = tabulate(first_puts, headers='keys', tablefmt='psql', showindex=False)

                #     # Print the tabulated strings
                #     print("Calls Table:\n", calls_table)
                #     print("Puts Table:\n", puts_table)
                #     # Concatenate the tables
                #     combined_table = calls_table + "\n\n" + puts_table

                #     # Print the combined table
                #     print("Combined Table:\n", combined_table)
                #     # Select the desired columns


                #     # Print the DataFrames in a tabulated format
                #     # print(first_calls.to_string(index=False))
                #     # print(first_puts.to_string(index=False))

                # #     return first_calls, first_puts  # These will be DataFrames with the first row of the lowest IV for each group (call and put)


                # # else:
                # #     print("No results were found.")
                # #     return None, None
                

asyncio.run(get_data())