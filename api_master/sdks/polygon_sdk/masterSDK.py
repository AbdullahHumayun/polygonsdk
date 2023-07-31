from cfg import YOUR_API_KEY, thirty_days_from_now_str,seven_days_from_now_str, fifteen_days_from_now_str, two_days_from_now_str, today_str, five_days_from_now_str, thirty_days_ago_str
import aiohttp
from typing import Optional,Any,List, Union
from .all_universal import UniversalSnapshotResult,UnderlyingAsset
from .ticker_snapshot import TickerSnapshotResults
from .aggregates import AggregatesData
from .crypto_snapshot import CryptoSnapshotResult
from .universal_snapshot import MultipleUniversalOptionSnapshot
import httpx
from aiohttp.client_exceptions import ContentTypeError
from .universal_option import OptionsSnapshotResult
from .universal_indices import IndicesSnapshotResult
import json
from .list_sets import etfs_list
from .async_options_sdk import PolygonOptionsSDK
from cfg import yesterday, eight_days_from_now_str
from .universal_snapshot import UniversalOptionSnapshot, UniversalSnapshot
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
from .option_aggs import OptionAggs
from .list_sets import indices_list
from .indices_snapshot import IndicesData
import asyncio
from typing import List
from .trades import DataContainer
from tabulate import tabulate
import pandas as pd
import asyncio
from sdks.polygon_sdk.list_sets import subscriptions
sdk = PolygonOptionsSDK(YOUR_API_KEY)
from urllib.parse import urlencode

import logging

logger = logging.getLogger(__name__)
# Set the log level to include all messages
logger.setLevel(logging.DEBUG)

# Create a file handler
handler = logging.FileHandler('bot.log')
# Create a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)

webull = AsyncWebullSDK()
class MasterSDK:
    def __init__(self):
        self.sdk = PolygonOptionsSDK(YOUR_API_KEY)


    async def _request_all_pages_concurrently(self,session, initial_url):

        all_results = []
        next_url = initial_url
        while next_url:
            try:
                async with self.session.get(next_url) as response:
                    response.raise_for_status()
                    data = await response.json()

                    if "results" in data:
                        all_results.extend(data["results"])

                    next_url = data.get("next_url")
                    if next_url:
                        next_url += f'&{urlencode({"apiKey": YOUR_API_KEY})}'

            except aiohttp.ClientResponseError as http_err:
                print(f"An HTTP error occurred: {http_err}")
                break
            except Exception as err:
                print(f"An error occurred: {err}")
                break

        return all_results


    async def find_skew(self, atm_options):
        async with aiohttp.ClientSession() as session:
            url = f"https://api.polygon.io/v3/snapshot?ticker.any_of={atm_options}&limit=250&apiKey={YOUR_API_KEY}"
            print(url)
            async with session.get(url) as response:
                r = await response.json()  # assuming response is JSON
                data = r['results'] if 'results' in r else None
                if data is not None:
                    try:
                        option_data = UniversalSnapshot(data)
                        skew_row = option_data.df.sort_values('IV', ascending=True)
                        return skew_row.iloc[[0]]
                    except KeyError:
                        return None
                    
    async def fetch_option_data(self, session, option):
        url = f"https://api.polygon.io/v3/trades/{option}?limit=100&apiKey={YOUR_API_KEY}"
        print(url)
        async with session.get(url) as response:
            if response.headers.get("content-type") == "application/json":
                r = await response.json()  # assuming response is JSON
                if 'results' in r:
                    data = r['results']
                    if data:  # Check if any results were received for this option
                        return [DataContainer.from_dict(result) for result in data]
                    else:
                        print(f"No results received for option: {option}")
            else:
                print(f"Unexpected content-type: {response.headers.get('content-type')}")
        return []
    async def atm_trades(self, atm_options: str) -> pd.DataFrame:
        atm_options = atm_options.split(',')
        data_containers = []
        symbols = []
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch_option_data(session, option) for option in atm_options]
            results = await asyncio.gather(*tasks)

        # Flatten the list of lists and keep track of symbols
        for sublist, symbol in zip(results, atm_options):
            for item in sublist:
                data_containers.append(item)
                symbols.append(symbol)

        if not data_containers:
            print("No results received for any option.")
            return pd.DataFrame()

        # Convert list of data containers to DataFrame
        df = pd.DataFrame([dc.__dict__ for dc in data_containers])
#        Transform the symbols into a human-readable format
        human_readable_symbols = [(symbol) for symbol in symbols]

        # Add the human-readable symbols to the DataFrame
        df['Symbol'] = human_readable_symbols

        if 'sip_timestamp' in df:
            df['sip_timestamp'] = pd.to_datetime(df['sip_timestamp'])
        else:
            df['sip_timestamp'] = pd.NaT 

        df.set_index('sip_timestamp', inplace=True)
        df = df.drop(columns=['participant_timestamp'])
        df.sort_values('size', ascending=False)
        return df



            
    async def show_the_chain(self, atm_options):
        async with aiohttp.ClientSession() as session:
            url = f"https://api.polygon.io/v3/snapshot?ticker.any_of={atm_options}&limit=250&apiKey={YOUR_API_KEY}"
            async with session.get(url) as response:
                r = await response.json()  # assuming response is JSON
                data = r['results'] if 'results' in r else None
                if data is not None:
                    try:
                        option_data = UniversalSnapshot(data)
                        df = option_data.df
                        df = df.sort_values('Strike', ascending=True)
                        df.sort_values('IV', ascending=True)
                        df['Vol'] = df['IV'].astype(str)  # Convert 'Vol' to string
                        df.iloc[0, 'IV'] = '🔥 ' + df.iloc[0, 'Vol']
                        return df
                    except KeyError:
                        return None
    async def find_multiple_skews(self,atm_options_list):
        all_option_data = []

        for atm_options in atm_options_list:
            options_combined = ''.join(atm_options)[:-1]  # Combine options and remove the trailing comma
            if len(options_combined) >= 250:
                initial_url = f"https://api.polygon.io/v3/snapshot?ticker.any_of={options_combined}&limit=250&apiKey={YOUR_API_KEY}"
                results = await self._request_all_pages_concurrently(initial_url)
                if results is not None:
                    option_data = UniversalOptionSnapshot(results)
                    all_option_data.append(option_data)


        return all_option_data
    
    async def get_all_indices(self):
        """Returns all up-to-date indices data in the form of a dataframe."""
        url = f"https://api.polygon.io/v3/snapshot/indices?apiKey={self.api_key}"
        all_indices_data = []
        async with aiohttp.ClientSession() as session:
            r = await self._request_all_pages_concurrently(session, url)
            print(r)
            if r is not None:
                print(r)

                all_indices_data.extend(r)  # use extend instead of append

        return IndicesData(all_indices_data)
    


    async def get_universal_snapshot(self, ticker): #✅
        """Fetches the Polygon.io universal snapshot API endpoint"""
        url=f"https://api.polygon.io/v3/snapshot?ticker.any_of={ticker}&limit=250&apiKey={YOUR_API_KEY}"
        print(url)
  
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as resp:
                    data = await resp.json()
                    results = data['results'] if 'results' in data else None
                    if results is not None:
                        return UniversalSnapshot(results)
                    else:
                        return None
            except ContentTypeError:
                pass


    async def check_macd_condition_bullish(self, hist):
        if hist is not None and len(hist) > 0:
            last_three_values = hist[:3]
            print(last_three_values)
            return (
                abs(last_three_values[0] - (-0.03)) < 0.02
                and all(last_three_values[i] > last_three_values[i + 1] for i in range(len(last_three_values) - 1))
            )


    async def check_macd_condition_bearish(hist):
        if hist is not None and len(hist) > 0:
        

            last_three_values = hist[:3]
            print(last_three_values)
            return (
                abs(last_three_values[0] - 0.03) > 0.02
                and all(last_three_values[i] < last_three_values[i + 1] for i in range(len(last_three_values) - 1))
            )
        


        
    async def tabulate_options(self, tickers):
        all_rows = []

        async def process_ticker(ticker):
            options_lists = await self.get_near_the_money_single(ticker)
            print(options_lists)
            x = await sdk.get_universal_snapshot(options_lists)

            df = x.df
            calls = df[df['C/P'] == 'call'].sort_values('IV', ascending=True)
            puts = df[df['C/P'] == 'put'].sort_values('IV', ascending=True)
            if not calls.empty and not puts.empty:
                call_skew = calls.iloc[[0]]
                put_skew = puts.iloc[[0]]
                # Rename headers in call_skew DataFrame
                call_skew = call_skew.rename(columns={"Vol": "Call Vol", "OI": "Call OI", "Skew": "Low IV Call Strike", "IV": "Call IV%", "Change %": "Call Change"})

                # Rename headers in put_skew DataFrame
                put_skew = put_skew.rename(columns={"Vol": "Put Vol", "OI": "Put OI", "Skew": "Low IV Put Strike", "IV": "Put IV%", "Change %": "Put Change"})

                # Select specific columns from call_skew DataFrame
                call_skew_selected = call_skew[["Sym","Exp","Call IV%", "Call OI", "Call Change","Low IV Call Strike"]].reset_index(drop=True)

                # Select specific columns from put_skew DataFrame
                put_skew_selected = put_skew[["Price", "Low IV Put Strike", "Put Change", "Put OI", "Put IV%","Exp"]].reset_index(drop=True)

                combined_skew = pd.concat([call_skew_selected, put_skew_selected], axis=1)
                combined_skew = combined_skew.fillna("")  # Replace remaining NaN values with empty string

                # Dropping the duplicated 'Sym' column
                # Modify IV columns
                combined_skew["Call IV%"] = combined_skew["Call IV%"].apply(lambda x: round(float(x) * 100, 6) if x != "" else x)
                combined_skew["Put IV%"] = combined_skew["Put IV%"].apply(lambda x: round(float(x) * 100, 6) if x != "" else x)

                # Dropping the duplicated 'Sym' column
                combined_skew = combined_skew.loc[:, ~combined_skew.columns.duplicated()]
                all_rows.append(combined_skew)

        # Run coroutines concurrently with max concurrency
        max_concurrency = 10  # Adjust this value to control the maximum number of concurrent tasks
        tasks = [process_ticker(ticker) for ticker in tickers]
        chunked_tasks = [tasks[i:i + max_concurrency] for i in range(0, len(tasks), max_concurrency)]
        
        for task_chunk in chunked_tasks:
            await asyncio.gather(*task_chunk)

        # Combine all dataframes in all_rows
        all_data = pd.concat(all_rows)

        # Print DataFrame as a fancy grid
        table = tabulate(all_data, headers='keys', tablefmt='fancy_grid', showindex=False)
        return all_data, table

    async def fetch_polygon_snapshot_async(
                self, snapshot_type: str, tickers: str,
                order: Optional[str] = None, limit: Optional[str] = None, 
                sort: Optional[str] = None, contract_type: Optional[str] = None,
                expiration_date: Optional[str] = None, strike_price: Optional[str] = None, option_contract: Optional[str] = None) -> Union[List[Any], Any]:
            """
            Fetch the snapshot data of a specific type from Polygon API.
            
            :param snapshot_type: Type of the snapshot. Can be 'indices', 'stocks', 'options' or 'crypto'.
            :param tickers: A string representing ticker symbols.
            :param order: (Optional) The order of the results. Can be 'asc' or 'desc'.
            :param limit: (Optional) The number of results to be returned.
            :param sort: (Optional) The field to sort the results by.
            :param contract_type: (Optional) Contract type, used for options snapshot.
            :param expiration_date: (Optional) Expiration date, used for options snapshot.
            :param strike_price: (Optional) Strike price, used for options snapshot.
            
            :return: A list of snapshot results if snapshot_type is 'indices' or 'options'. 
                    An instance of TickerSnapshotResults if snapshot_type is 'stocks'. 
                    An instance of CryptoSnapshotResult if snapshot_type is 'crypto'. 

            :raise ValueError: If the snapshot_type is not one of 'indices', 'stocks', 'options' or 'crypto'.
            """
            params = {}
            if snapshot_type == "indices":
                url = f"https://api.polygon.io/v3/snapshot/{snapshot_type}"
            elif snapshot_type == "stocks":
                url = f"https://api.polygon.io/v2/snapshot/locale/us/markets/stocks/tickers/{tickers}"
            elif snapshot_type == "options":
                url = f"https://api.polygon.io/v3/snapshot/options/{tickers}?apiKey={YOUR_API_KEY}"
                print(url)
            elif snapshot_type == "option_chain":
                url = f"https://api.polygon.io/v3/snapshot/options/{tickers}/{option_contract}"
                print(url)
            elif snapshot_type == "universal":
                url = f"https://api.polygon.io/v3/snapshot?ticker.any_of={tickers}&apiKey={YOUR_API_KEY}"
            elif snapshot_type == "crypto":
                url = f"https://api.polygon.io/v2/snapshot/locale/global/markets/crypto/tickers/{tickers}"
            else:
                raise ValueError(f"Invalid snapshot type: {snapshot_type}")

            # Building the params
            if snapshot_type == "indices":
                params = {
                    "ticker.any_of": tickers,
                    "order": order,
                    "limit": limit,
                    "sort": sort,
                    "apiKey": f"{YOUR_API_KEY}",
                }
            elif snapshot_type in ("stocks"):
                params = {
                    "apiKey": f"{YOUR_API_KEY}",
                }

            elif snapshot_type in ("crypto"):
                params = { 
                    "apiKey": f"{YOUR_API_KEY}"
                    
                }
            elif snapshot_type == "options":
                params = {
                    "contract_type": contract_type,
                    "strike_price": strike_price,
                    "order": order,
                    "limit": limit,
                    "sort": sort,
                    "apiKey": f"{YOUR_API_KEY}",
                }
            elif snapshot_type == "option_chain":
                params = {
                    "contract_type": contract_type,
                    "strike_price": strike_price,
                    "option_contract": option_contract,
                    "order": order,
                    "limit": limit,
                    "sort": sort,
                    "apiKey": f"{YOUR_API_KEY}",
                }

            # Filter out None values
            params = {k: v for k, v in params.items() if v is not None}

            async with aiohttp.ClientSession() as session:
                async with session.get(url, params=params) as response:
                    data = await response.json()
                    if data is not None:
                        results = data['results']
                    #print(f"API response for {tickers}: {data}")  # Add this line fo
                    
                if snapshot_type == "indices":
                    return [IndicesSnapshotResult.from_dict(result) for result in data['results']]
                elif snapshot_type in ("stocks"):
                    return [TickerSnapshotResults.from_dict(data['ticker']) if snapshot_type == "stocks" else CryptoSnapshotResult.from_dict(data['ticker'])]
                elif snapshot_type == "options":
                    return [OptionsSnapshotResult.from_dict(results) for results in data['results']]
                elif snapshot_type == "universal":
                    return [UniversalSnapshotResult.from_dict(result) for result in data['results']]

    async def get_strike_thresholds(self, ticker:str, price):
        if price is not None and ticker in indices_list:
            lower_strike = round(price * 0.99)
            upper_strike = round(price * 1.01)
            return lower_strike, upper_strike
        else:
            lower_strike = round(price * 0.95)
            upper_strike = round(price * 1.05)
            return lower_strike, upper_strike
    async def get_near_the_money_single(self, ticker: str, exp_greater_than:str=today_str, exp_less_than:str=eight_days_from_now_str):
        price = await self.get_price(ticker)
        print(price)
        if price is not None:
            upper_strike, lower_strike = await self.get_strike_thresholds(ticker, price)
            print(upper_strike,lower_strike)
            async with aiohttp.ClientSession() as session:
                url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.lte={lower_strike}&strike_price.gte={upper_strike}&expiration_date.gt={exp_greater_than}&expiration_date.lte={exp_less_than}&limit=250&apiKey={YOUR_API_KEY}"
                print(url)
                async with session.get(url) as resp:
                    r = await resp.json()
                    results = r['results'] if 'results' in r else None
                    if results is None:
                        return
                    else:
                        results = UniversalOptionSnapshot(results)
                        print(results)
                        tickers = results.ticker
                        if ticker is not None:
                            atm_tickers = ','.join(tickers)
                            return atm_tickers
                        else:
                            return None
                        
    async def get_near_the_money_oi(self,ticker):
        shield="<a:_:1047279498468544612>"
        money="<a:_:1043015510549348412>"
        uptrend="<a:_:1045174789150605375>"
        downtrend="<a:_:1045945801756643390>"
        exp="<a:_:1104233012020908042>"
        price = await self.get_price(ticker)
        if price is not None:
            upper_strike, lower_strike = await self.get_strike_thresholds(ticker, price)
            async with aiohttp.ClientSession() as session:
                url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.lte={lower_strike}&strike_price.gte={upper_strike}&expiration_date.lte={seven_days_from_now_str}&expiration_date.gte={today_str}&limit=250&apiKey={YOUR_API_KEY}"
                print(url)
                async with session.get(url) as resp:
                    r = await resp.json()
                    results = r['results'] if 'results' in r else None
                    if results is None:
                        return
                    else:
                        results = UniversalOptionSnapshot(results)
                        print(results.df.columns)
                        calls = pd.DataFrame()
                        puts = pd.DataFrame()
                        if results.contract_type is not None:
                            calls_data = results.df[results.df['C/P'] == 'call']
                            puts_data = results.df[results.df['C/P'] == 'put']
                            calls = pd.concat([calls, calls_data.sort_values('OI', ascending=False).head(5)])
                            puts = pd.concat([puts, puts_data.sort_values('OI', ascending=False).head(5)])
                        columns_to_keep = ['sym', 'exp', 'strike', 'price', 'OI', 'vol']
                        new_column_names = ['Sym', f"🗓️",'Strk', f'💲', f'🛡️OI', '⚔️Vol']
                        calls = calls[columns_to_keep].rename(columns=dict(zip(columns_to_keep, new_column_names)))
                        puts = puts[columns_to_keep].rename(columns=dict(zip(columns_to_keep, new_column_names)))
                        calls = calls[new_column_names]
                        puts = puts[new_column_names]
                        return calls, puts



                        
    async def get_call_or_puts_df(self, ticker: str, exp_greater_than: str=today_str, exp_less_than:str=thirty_days_from_now_str, contract_type:str="call"):
        price = await self.get_price(ticker) if ticker == "SPX" else await self.get_price(ticker)
        if price is not None:
            upper_strike, lower_strike = await self.get_strike_thresholds(ticker, price)



            async with aiohttp.ClientSession() as session:
                url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?contract_type={contract_type}&strike_price.lte={lower_strike}&strike_price.gte={upper_strike}&expiration_date.lte={exp_less_than}&expiration_date.gte={exp_greater_than}&limit=250&apiKey={YOUR_API_KEY}"
                async with session.get(url) as resp:
                    r = await resp.json()
                    results = r['results'] if 'results' in r else None
                    print(type(results), results)
                    if results is None:
                        return None, None
                    else:
                        data = UniversalOptionSnapshot(results)
                        
                        return data.df
                    

    async def get_unusual_options(self, ticker: str, exp_greater_than: str=today_str, exp_less_than:str=thirty_days_from_now_str, contract_type:str="call"):
        price = await self.get_price(ticker) if ticker == "SPX" else await self.get_price(ticker)
        if price is not None:
            upper_strike, lower_strike = await self.get_strike_thresholds(ticker, price)



            async with aiohttp.ClientSession() as session:
                url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.lte={lower_strike}&strike_price.gte={upper_strike}&expiration_date.lte={exp_less_than}&expiration_date.gte={exp_greater_than}&limit=250&apiKey={YOUR_API_KEY}"
                async with session.get(url) as resp:
                    r = await resp.json()
                    results = r['results'] if 'results' in r else None
                    print(type(results), results)
                    if results is None:
                        return None, None
                    else:
                        data = UniversalOptionSnapshot(results)
                        option_activity = list(zip(data.ticker, data.open_interest, data.volume))
                        # Filter the tuples where oi > volume
                        # Filter the tuples where oi > volume and add the 'Unusual' column
                        # Filter the tuples where oi > volume and add the 'Unusual' column
                        filtered_data = [(ticker, oi, volume, volume > oi if volume is not None else "NEW STRIKE") for ticker, oi, volume in option_activity]
            
                        # Filter out None values and concatenate the remaining results into a final tabulated form

                        final_table = tabulate(filtered_data, headers='keys', tablefmt='grid')

                        # Split the final table into smaller chunks
                        chunk_size = 4000  # Adjust this value as needed
                        chunks = [final_table[i:i + chunk_size] for i in range(0, len(final_table), chunk_size)]
                        print(chunks)

                        return chunks


                        
    async def fetch_data(self, session, url):
        async with session.get(url) as resp:
            return await resp.json()



    async def get_price(self, ticker=str):
        ticker = ticker if ticker not in indices_list else f"I:{ticker}"
        url = f"https://api.polygon.io/v3/snapshot?ticker.any_of={ticker}&apiKey={YOUR_API_KEY}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                try:
                    data = await resp.json()
                    results = data['results'] if 'results' in data else None
                    if results is not None:
                        value = results[0].get('session', {}).get('close', None)
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
            more_tickers = await webull.get_top_option_string()

            combined_tickers = list(set(tickers) | set(more_tickers))
            timespans = ['minute', 'hour', 'day', 'week', 'month', 'quarter', 'year']

            tasks = []
            for ticker in combined_tickers:
                for timespan in timespans:
                    url = f"https://api.polygon.io/v1/indicators/rsi/{ticker}?timespan={timespan}&adjusted=true&window=14&series_type=close&order=desc&limit=1000&apiKey={YOUR_API_KEY}"
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