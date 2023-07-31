import pandas as pd
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.polygon_sdk.universal_snapshot import UniversalOptionSnapshot,UniversalSnapshot
from cfg import YOUR_API_KEY as poly_options, today_str, seven_days_from_now_str
import asyncio
from sdks.polygon_sdk.masterSDK import MasterSDK
import aiohttp
from tabulate import tabulate
master = MasterSDK()
polygon = AsyncPolygonSDK(poly_options)
async def pc(ticker:str):
    """View skews for the next 60 days. PC Format with more columns."""
    MAX_CONCURRENCY = 60
    ticker = ticker.upper()

    async def fetch_data(session, tickers):
        async with session.get(f"https://api.polygon.io/v3/snapshot?ticker.any_of={tickers}&apiKey={poly_options}") as response:
            try:
                near_money = await response.json(content_type=None)
                near_money_results = near_money['results']
                atm_data = UniversalSnapshot(near_money_results)
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
        counter = 0
        while True:
            counter = counter + 1
            if ticker.startswith("SPX"):
                price = await master.get_index_price(ticker)
                lower_strike = round(price) * 0.97
                upper_strike = round(price) * 1.03
            else:
                price = await master.get_stock_price(ticker)
                if price is None:
                    continue
                lower_strike = round(price) * 0.85
                upper_strike = round(price) * 1.15
            print(f"SPX TICKER: {ticker}: {lower_strike}, {price}, {upper_strike}")

            initial_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte={seven_days_from_now_str}&limit=250&apiKey={poly_options}"
            results = await polygon._request_all_pages(initial_url)

            if results is not None:
                option_data = UniversalOptionSnapshot(results)
                calls = option_data.df[option_data.df['C/P'] == 'call']
                puts = option_data.df[option_data.df['C/P'] == 'put']
                calls_grouped = calls.groupby('Exp')
                puts_grouped = puts.groupby('Exp')

                calls_results = await process_option_data(calls_grouped, session, sem)
                if calls_results is not None and len(calls_results) > 0:
                    calls_results_df = pd.concat(calls_results)
                    calls_grouped = calls_results_df.groupby('Exp', as_index=False)
                else:
                    continue

                puts_results = await process_option_data(puts_grouped, session, sem)
                if puts_results is not None:
                    puts_results_df = pd.concat(puts_results)
                    puts_grouped = puts_results_df.groupby('Exp', as_index=False)
                else:
                    continue

                calls_first_rows = calls_grouped.first()
                puts_first_rows = puts_grouped.first()

                calls_selected_columns_df = calls_first_rows[['Exp', 'IV', 'Skew', 'Price', 'Size', 'Vol', 'OI']]
                puts_selected_columns_df = puts_first_rows[['Exp', 'IV', 'Skew', 'Price', 'Size', 'Vol', 'OI']]
                calls_selected_columns_df['Exp'] = calls_selected_columns_df['Exp'].apply(lambda x: x[5:])
                puts_selected_columns_df['Exp'] = puts_selected_columns_df['Exp'].apply(lambda x: x[5:])
                calls_selected_columns_df['IV'] = (calls_selected_columns_df['IV'] * 100).round(4)
                puts_selected_columns_df['IV'] = (puts_selected_columns_df['IV'] * 100).round(4)
                calls_selected_columns_df = calls_selected_columns_df.reset_index(drop=True)[['Exp', 'IV', 'Skew', 'Price', 'Size', 'Vol', 'OI']]
                puts_selected_columns_df = puts_selected_columns_df.reset_index(drop=True)[['Exp', 'IV', 'Skew', 'Price', 'Size', 'Vol', 'OI']]

                print(calls_selected_columns_df)
                print(puts_selected_columns_df)
                call_table = tabulate(calls_selected_columns_df, headers='keys', tablefmt='fancy', showindex=False)
                put_table = tabulate(puts_selected_columns_df, headers='keys', tablefmt='fancy', showindex=False)
                print(call_table)
                print(put_table)

