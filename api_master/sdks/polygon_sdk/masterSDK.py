from cfg import YOUR_API_KEY, thirty_days_from_now_str, fifteen_days_from_now_str, two_days_from_now_str, today_str
import aiohttp
from .async_options_sdk import PolygonOptionsSDK
from .universal_snapshot import UniversalOptionSnapshot, UniversalSnapshot
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
from typing import List
from tabulate import tabulate
import pandas as pd
import asyncio
sdk = PolygonOptionsSDK(YOUR_API_KEY)
from urllib.parse import urlencode

webull = AsyncWebullSDK()
class MasterSDK(PolygonOptionsSDK):
    def __init__(self):
        self.api_key = YOUR_API_KEY
        self.snapshot_base_url = f"https://api.polygon.io/v3/snapshot/options/"
    

    async def _request_all_pages_concurrently(session, initial_url,api_key=YOUR_API_KEY):

        all_results = []
        next_url = initial_url
        while next_url:
            try:
                async with session.get(next_url, params=params) as response:
                    response.raise_for_status()
                    data = await response.json()

                    if "results" in data:
                        all_results.extend(data["results"])

                    next_url = data.get("next_url")
                    if next_url:
                        next_url += f'&{urlencode({"apiKey": api_key})}'
                        params = {}

            except aiohttp.ClientResponseError as http_err:
                print(f"An HTTP error occurred: {http_err}")
                break
            except Exception as err:
                print(f"An error occurred: {err}")
                break

        return all_results


    async def find_skew(self, atm_options):
        async with aiohttp.ClientSession() as session:
            url=f"https://api.polygon.io/v3/snapshot?ticker.any_of={atm_options}&limit=250&apiKey={YOUR_API_KEY}"
            async with session.get(url):
                r = await self._request_all_pages_concurrently(url)
                data = r['results'] if 'results' in r else None
                if data is not None:
                    try:
                        option_data = UniversalSnapshot(data)
                        skew_row = option_data.df.sort_values('IV', ascending=True)
                        return skew_row.iloc[[0]]
                    except KeyError:
                        return None
    async def find_multiple_skews(self,atm_options_list):
        all_option_data = []

        for atm_options in atm_options_list:
            options_with_commas = [f"{option}," for option in atm_options if option]  # Add comma at the end of each option
            options_combined = ''.join(options_with_commas)[:-1]  # Combine options and remove the trailing comma
            if len(options_combined) >= 250:
                initial_url = f"https://api.polygon.io/v3/snapshot?ticker.any_of={options_combined}&limit=250&apiKey={YOUR_API_KEY}"
                results = await self._request_all_pages_concurrently(initial_url)
                if results is not None:
                    option_data = UniversalOptionSnapshot(results)
                    all_option_data.append(option_data)
            else:
                async with aiohttp.ClientSession() as session:
                    url = f"https://api.polygon.io/v3/snapshot?ticker.any_of={options_combined}&limit=250&apiKey={YOUR_API_KEY}"
                    try:
                        async with session.get(url) as resp:
                            if resp.content_type == 'application/json':
                                r = await resp.json()
                                data = r.get('results')
                                if data is not None:
                                    option_data = UniversalSnapshot(data)
                                    all_option_data.append(option_data)
                            else:
                                print(f"Unexpected content type: {resp.content_type} for URL: {url}")
                    except aiohttp.client_exceptions.ContentTypeError as e:
                        print(f"Error decoding JSON response for URL: {url}")
                        print(e)

        return all_option_data
    
    async def tabulate_options(self):
        tickers = ["AMD", "GME", "NVDA", "TSLA", "UPST", "BIDU", "U", "W", "MSFT"]
        all_rows = []

        for ticker in tickers:
            options_lists = await self.get_near_the_money_single(ticker, 5)
            print(options_lists)
            x = await sdk.get_universal_snapshot(options_lists)

            df = x.df
            calls = df[df['C/P'] == 'call'].sort_values('IV', ascending=True)
            puts = df[df['C/P'] == 'put'].sort_values('IV', ascending=True)

            call_skew = calls.iloc[[0]]
            put_skew = puts.iloc[[0]]
            # Rename headers in call_skew DataFrame
            call_skew = call_skew.rename(columns={"Vol": "Call Vol", "OI": "Call OI", "Skew": "Low IV Call Strike", "IV": "Call IV%", "Change %": "Call Change"})

            # Rename headers in put_skew DataFrame
            put_skew = put_skew.rename(columns={"💲": "💲 Price", "Vol": "Put Vol", "OI": "Put OI", "Skew": "Low IV Put Strike", "IV": "Put IV%", "Change %": "Put Change"})

            # Select specific columns from call_skew DataFrame
            call_skew_selected = call_skew[["Sym","🗓️","Call IV%", "Call OI", "Call Change","Low IV Call Strike"]].reset_index(drop=True)

            # Select specific columns from put_skew DataFrame
            put_skew_selected = put_skew[["💲 Price", "Low IV Put Strike", "Put Change", "Put OI", "Put IV%","🗓️"]].reset_index(drop=True)

            combined_skew = pd.concat([call_skew_selected, put_skew_selected], axis=1)
            combined_skew = combined_skew.fillna("")  # Replace remaining NaN values with empty string

            # Dropping the duplicated 'Sym' column
            # Modify IV columns
            combined_skew["Call IV%"] = combined_skew["Call IV%"].apply(lambda x: round(float(x) * 100, 6) if x != "" else x)
            combined_skew["Put IV%"] = combined_skew["Put IV%"].apply(lambda x: round(float(x) * 100, 6) if x != "" else x)

            # Dropping the duplicated 'Sym' column
            combined_skew = combined_skew.loc[:, ~combined_skew.columns.duplicated()]
            all_rows.append(combined_skew)

        # Combine all dataframes in all_rows
        all_data = pd.concat(all_rows)

        # Print DataFrame as a fancy grid
        print(tabulate(all_data, headers='keys', tablefmt='fancy_grid', showindex=False))
        return all_data

    async def get_near_the_money_single(self, ticker: str, threshold: float):
        if ticker is not None:
            if ticker.startswith("SPX") or ticker.startswith("VIX") or ticker.startswith("NDX"):
                price = await self.get_index_price(ticker)
            else:
                price = await self.get_stock_price(ticker)
            if price is not None:
                lower_strike = round(price * (1 - threshold/100), 2)
                upper_strike = round(price * (1 + threshold/100), 2)

                async with aiohttp.ClientSession() as session:
                    url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.lte={upper_strike}&strike_price.gte={lower_strike}&expiration_date.lte={fifteen_days_from_now_str}&expiration_date.gt={today_str}&limit=250&apiKey={YOUR_API_KEY}"
                    async with session.get(url) as resp:
                        r = await resp.json()
                        results = r['results']
                        if results is not None:
                            results = UniversalOptionSnapshot(results)
                            tickers = results.ticker
                            atm_tickers = ','.join(tickers)
                            return atm_tickers
            else:
                return None
        return None
                
    async def fetch_data(self, session, url):
        async with session.get(url) as resp:
            return await resp.json()

    async def get_near_the_money_multiple(self, tickers: List[str], threshold: float, search_until:str=thirty_days_from_now_str):
        results = []
        tasks = []

        async with aiohttp.ClientSession() as session:
            for ticker in tickers:
                if ticker.startswith("SPX") or ticker.startswith("VIX") or ticker.startswith("NDX"):
                    price = await self.get_index_price(ticker)
                else:
                    price = await self.get_stock_price(ticker)

                lower_strike = round(price * (1 - threshold / 100), 2)
                upper_strike = round(price * (1 + threshold / 100), 2)

                url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.lte={upper_strike}&strike_price.gte={lower_strike}&expiration_date.lte={search_until}&limit=250&apiKey={YOUR_API_KEY}"
                print(url)

                task = asyncio.create_task(self.fetch_data(session, url))
                tasks.append((ticker, task))

            for ticker, task in tasks:
                r = await task
                response_results = r['results']
                if response_results is not None:
                    response_results = UniversalOptionSnapshot(response_results)
                    ticker_list = response_results.ticker
                    atm_tickers = ','.join(ticker_list)
                    results.append(atm_tickers)

            return results

                
    async def get_index_price(self, ticker=str):
        """Fetch the price of an index ticker"""
        url = f"https://api.polygon.io/v3/snapshot?ticker.any_of=I:{ticker}&apiKey={self.api_key}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.json()
                results = data['results'] if data['results'] is not None else None
                if results is None:
                    print(f"Error - results from price request.")

                else:
                    value = results[0]['value'] if results and len(results) > 0 and 'value' in results[0] else None
                    if value is not None:
                        return value
        return None
    
    async def get_stock_price(self, ticker=str):
        url = f"https://api.polygon.io/v3/snapshot?ticker.any_of={ticker}&apiKey={self.api_key}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                try:
                    data = await resp.json()
                    results = data['results'] if 'results' in data else None
                    if results is not None:
                        value = results[0]['session']['close']
                        if value is not None:
                            return value
                        else:
                            return None
                except KeyError:
                    pass  # Handle the KeyError and continue with the next ticker

        return None  # Return None if the stock price couldn't be retrieved
    async def fetch_rsi(self, session, url, ticker, timespan):
        async with session.get(url) as resp:
            r = await resp.json()
            results = r.get('results')

            if results:
                values = results.get('values')
                if values:
                    rsi_value = values[0]['value']  # Get the first RSI value
                    return (ticker, timespan, rsi_value)
        return None

    async def scan_all_rsi(self):
        """Scans top 500 tickers and returns RSI snapshots."""
        async with aiohttp.ClientSession() as session:
            tickers = await webull.get_top_traded_options()
            more_tickers = await webull.get_top_options()

            combined_tickers = list(set(tickers) | set(more_tickers))
            timespans = ['minute', 'hour', 'day', 'week', 'month', 'quarter', 'year']

            tasks = []
            for ticker in combined_tickers:
                for timespan in timespans:
                    url = f"https://api.polygon.io/v1/indicators/rsi/{ticker}?timespan={timespan}&adjusted=true&window=14&series_type=close&order=desc&limit=1000&apiKey={self.api_key}"
                    task = asyncio.create_task(self.fetch_rsi(session, url, ticker, timespan))
                    tasks.append(task)

            results = await asyncio.gather(*tasks)
            results = [result for result in results if result is not None]

            # Initialize a dictionary for storing the results
            rsi_dict = {}

            for result in results:
                ticker, timespan, rsi_value = result
                if rsi_value < 30 or rsi_value > 70:
                    if ticker not in rsi_dict:
                        rsi_dict[ticker] = {}
                    rsi_dict[ticker][timespan] = rsi_value

            # Convert the nested dictionary to a list of dictionaries for tabulate
            table = []
            for ticker, timespan_values in rsi_dict.items():
                row = {"Ticker": ticker}
                row.update(timespan_values)
                table.append(row)
            df = pd.DataFrame(table)
            df.to_csv('rsi_values.csv', index=False)
            print(tabulate(table, headers="keys", tablefmt="pretty"))

            return df