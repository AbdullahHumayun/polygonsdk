import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from cfg import seven_days_from_now_str
import requests
from requests.exceptions import HTTPError
from .option_aggs import OptionAggs
import asyncio
import pandas as pd
import csv
import aiohttp
import aiofiles
import re

from .option_snapshot import OptionSnapshotData
from .universal_snapshot import UniversalOptionSnapshot, UniversalSnapshot, CallsOrPuts
from typing import List, Optional
from datetime import datetime
from urllib.parse import urlencode
from .option_trades import OptionTrade
import requests
from .option_quote import OptionQuote
from requests.exceptions import HTTPError
from urllib.parse import urlencode
from cfg import YOUR_API_KEY, fifteen_days_from_now_str, five_days_from_now_str, today_str

MAX_SIMULTANEOUS_REQUESTS = 50 # adjust based on your needs. Lower = longer time to collect options data.

class PolygonOptionsSDK:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.polygon.io"

        self.conditions_map = None



    async def get_option_data(self, ticker, price):
        async with aiohttp.ClientSession() as session:
            if price is not None:
                lower_strike = round(price * 0.95)
                upper_strike = round(price * 1.05)
                initial_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte={seven_days_from_now_str}&limit=250&apiKey={YOUR_API_KEY}"

                async with session.get(initial_url) as resp:
                    data = await resp.json()

                    results = data['results']
                    if results is not None:
                        option_data = OptionSnapshotData(results)
                        symbols = str(option_data.option_symbol).replace("'","").replace(']','').replace('[','').replace(' ','')


                        if option_data is not None:
                            df = pd.DataFrame(option_data.data_dict).dropna(how="any").sort_values('implied_volatility', ascending=True)
                            if not df.empty:
                                df = df.iloc[[0]]
                                for _, row in df.iterrows():
                                    strike = row['strike_price']
                                    symbol = row['underlying_ticker']
                                    iv = round(float(row['implied_volatility'])*100,5)
                                    underlying_price = row['underlying_price']
                                    expiry = row['expiration_date']
                                    volume = float(row['day_volume'])
                                    gamma = row['gamma']
                                    delta = row['delta']
                                    vega = row['vega']
                                    open_interest = row['open_interest']
                                    ask = row['ask']
                                    bid = row['bid']
                                    bid_size = row['bid_size']
                                    ask_size = row['ask_size']
                                    expiry = expiry[5:]
                                    skew = "🔥" if strike <= underlying_price else "🟢"
                                    skew_metric = strike - underlying_price
                                    if skew_metric < -5 or skew_metric > 5:
                                        return [symbol, f"{strike}", f"{skew}", underlying_price, expiry, iv, volume, skew_metric,gamma,delta,vega,ask,bid,bid_size,ask_size, open_interest]
                        return None
    async def get_universal_snapshot(self, tickers):
        """Fetches the Polygon.io universal snapshot API endpoint"""
        url=f"https://api.polygon.io/v3/snapshot?ticker.any_of={tickers}&limit=250&apiKey={self.api_key}"
        print(url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.json()
                results = data['results'] if data['results'] is not None else None
                if results is not None:
                    return UniversalSnapshot(results)

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




    async def extract_underlying_symbol(self, symb):



        try:
            match = re.search(r'O:(\w{1,5})(\d{2})(\d{2})(\d{2})([CP])(\d+)', symb)
            underlying_symbol, year, month, day, call_put, strike_price = match.groups() 

        except AttributeError:
            return "M/A"
        
        return underlying_symbol

    async def get_option_quote(self, option_symbol, order="desc", limit="10", sort="timestamp", timestamp_lt=None, timestamp_lte=None, timestamp_gt=None, timestamp_gte=None):
        url = f"{self.base_url}/v3/quotes/{option_symbol}?order={order}&limit={limit}&sort={sort}&apiKey={self.api_key}"
        
        if timestamp_lt:
            url += f"&timestamp.lt={timestamp_lt}"
        if timestamp_lte:
            url += f"&timestamp.lte={timestamp_lte}"
        if timestamp_gt:
            url += f"&timestamp.gt={timestamp_gt}"
        if timestamp_gte:
            url += f"&timestamp.gte={timestamp_gte}"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                print(url)
                results = data['results']
                return OptionQuote(results)
    async def _request(self, endpoint, params=None):
        if params is None:
            params = {}
        params["apiKey"] = self.api_key
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f"An HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"An error occurred: {err}")
            return None

        try:
            return response.json()
        except Exception as err:
            print(f"Error decoding JSON response: {err}")
            return None

    async def _request_all_pages(self, initial_url, params=None):
        if params is None:
            params = {}
        params["apiKey"] = self.api_key

        all_results = []
        next_url = initial_url

        while next_url:
            try:
                response = requests.get(next_url, params=params)
                response.raise_for_status()
                data = response.json()

                if "results" in data:
                    all_results.extend(data["results"])

                next_url = data.get("next_url")
                if next_url:
                    next_url += f'&{urlencode({"apiKey": self.api_key})}'
                    params = {}

            except HTTPError as http_err:
                print(f"An HTTP error occurred: {http_err}")
                break
            except Exception as err:
                print(f"An error occurred: {err}")
                break

        return all_results


    async def get_options_contracts(
        self,
        underlying_ticker=None,
        contract_type=None,
        expiration_date=None,
        as_of=None,
        strike_price=None,
        expired=None,
        order=None,
        limit=None,
        sort=None,
    ):
        endpoint = "/v3/reference/options/contracts"
        initial_url = f"{self.base_url}{endpoint}"
        params = {}

        if underlying_ticker is not None:
            params["underlying_ticker"] = underlying_ticker
        if contract_type is not None:
            params["contract_type"] = contract_type
        if expiration_date is not None:
            params["expiration_date"] = expiration_date
        if as_of is not None:
            params["as_of"] = as_of
        if strike_price is not None:
            params["strike_price"] = strike_price
        if expired is not None:
            params["expired"] = expired
        if order is not None:
            params["order"] = order
        if limit is not None:
            params["limit"] = limit
        if sort is not None:
            params["sort"] = sort

        return await self._request_all_pages(initial_url, params=params)
    

 
        
    async def fetch_all_option_contracts(self, expiration_date=None, expiration_date_lt=None, expiration_date_lte=None,
                                        expiration_date_gt=None, expiration_date_gte=None):
        """
            Fetches all option contracts from the Polygon API based on optional filter parameters.

            Args:
                expiration_date (Optional[str]): A string representing the expiration date (e.g. '2023-06-16') to filter by.
                expiration_date_lt (Optional[str]): A string representing the maximum expiration date (exclusive) to filter by.
                expiration_date_lte (Optional[str]): A string representing the maximum expiration date (inclusive) to filter by.
                expiration_date_gt (Optional[str]): A string representing the minimum expiration date (exclusive) to filter by.
                expiration_date_gte (Optional[str]): A string representing the minimum expiration date (inclusive) to filter by.

            Returns:
                List[Dict[str, Any]]: A list of dictionaries representing the option contracts that match the given filters.
                Each dictionary contains the keys "ticker" and "underlying_ticker".
            """

        url = f'https://api.polygon.io/v3/reference/options/contracts?limit=1000&apiKey={YOUR_API_KEY}'
        print(url)
        if expiration_date:
            url += f'&expiration_date={expiration_date}'
        if expiration_date_lt:
            url += f'&expiration_date.lt={expiration_date_lt}'
        if expiration_date_lte:
            url += f'&expiration_date.lte={expiration_date_lte}'
        if expiration_date_gt:
            url += f'&expiration_date.gt={expiration_date_gt}'
        if expiration_date_gte:
            url += f'&expiration_date.gte={expiration_date_gte}'
        
        contracts = []
        
        async with aiohttp.ClientSession() as session:
            while url:
                async with session.get(url) as response:

                    data = await response.json()
                    contracts.extend([{"ticker": contract["ticker"], "underlying_ticker": contract["underlying_ticker"]} for contract in data["results"]])
                    print(data)
                    # Check if there's a next URL and append the API key
                    next_url = data.get("next_url")
                    if next_url:
                        url = f"{next_url}&apiKey={YOUR_API_KEY}"
                    else:
                        url = None
                        
            return contracts
            




    async def get_options_snapshot_async(self, contract, semaphore):
        """
        Fetches the options snapshot data for a given option contract from the Polygon API.

        Args:
            contract (Dict[str, str]): A dictionary containing the keys "ticker" and "underlying_ticker" for the option contract.
            semaphore (asyncio.Semaphore): A semaphore object to control concurrent access to the API.

        Returns:
            Optional[Dict[str, Any]]: A dictionary representing the snapshot data for the given option contract, or None if the request failed.
        """



        url = f'https://api.polygon.io/v3/snapshot/options/{contract["underlying_ticker"]}/{contract["ticker"]}?apiKey={YOUR_API_KEY}'
        async with semaphore:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as response:
                        if response.status == 200:
                            data = await response.json()
                            print(f"Fetched snapshot for {contract['ticker']}: {data}")
                            return data["results"]
                        else:
                            print(f"An error occurred while fetching snapshot for {contract['ticker']}: {response.status}, {response.reason}, url={url}")
                            return None
            except aiohttp.ClientConnectorError:
                print(f"Failed to connect to {url}, retrying...")
                await asyncio.sleep(5)
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as response:
                        if response.status == 200:
                            data = await response.json()
                            print(f"Fetched snapshot for {contract['ticker']}: {data}")
                            return data["results"]
                        else:
                            print(f"An error occurred while fetching snapshot for {contract['ticker']}: {response.status}, {response.reason}, url={url}")
                            return None


    async def write_snapshot_to_csv(self, writer, snapshot):
        """
        Write a snapshot of option data to a CSV file using the provided writer.
        :param writer: A CSV DictWriter object
        :param snapshot: A dictionary containing the snapshot of option data
        """
        if snapshot:
        
            details = snapshot["details"]
            greeks = snapshot["greeks"]
            last_quote = snapshot["last_quote"]
            underlying_asset = snapshot["underlying_asset"]
            print(underlying_asset)
            day = snapshot["day"]
            last_trade = snapshot["last_trade"]

            await writer.writerow({
                "ticker": details["ticker"],
                "break_even_price": snapshot.get("break_even_price", None),
                "contract_type": details.get("contract_type", None),
                "exercise_style": details.get("exercise_style", None),
                "expiration_date": details.get("expiration_date", None),
                "shares_per_contract": details.get("shares_per_contract", None),
                "strike_price": details.get("strike_price", None),
                "delta": greeks.get("delta", None),
                "gamma": greeks.get("gamma", None),
                "theta": greeks.get("theta", None),
                "vega": greeks.get("vega", None),
                "implied_volatility": snapshot.get("implied_volatility", None),
                "open_interest": snapshot.get("open_interest", None),
                "ask": last_quote.get("ask", None),
                "ask_size": last_quote.get("ask_size", None),
                "bid": last_quote.get("bid", None),
                "bid_size": last_quote.get("bid_size", None),
                "last_updated": last_quote.get("last_updated", None),
                "midpoint": last_quote.get("midpoint", None),
                "timeframe_quote": last_quote.get("timeframe", None),
                "last_trade_conditions": last_trade.get("conditions", None),
                "last_trade_exchange": last_trade.get("exchange", None),
                "last_trade_price": last_trade.get("price", None),
                "last_trade_sip_timestamp": last_trade.get("sip_timestamp", None),
                "last_trade_size": last_trade.get("size", None),
                "timeframe_trade": last_trade.get("timeframe", None),
                "day_change": day.get("change", None),
                "day_change_percent": day.get("change_percent", None),
                "day_close": day.get("close", None),
                "day_high": day.get("high", None),
                "day_last_updated": day.get("last_updated", None),
                "day_low": day.get("low", None),
                "day_open": day.get("open", None),
                "day_previous_close": day.get("previous_close", None),
                "day_volume": day.get("volume", None),
                "day_vwap": day.get("vwap", None),
                "change_to_break_even": underlying_asset.get("change_to_break_even", None),
                "price": underlying_asset.get("price", None),
                "underlying_ticker": underlying_asset.get("ticker", None),
            
            })
    async def get_snapshots(self, option_contracts, output_file):

        semaphore = asyncio.Semaphore(MAX_SIMULTANEOUS_REQUESTS)
        async with aiofiles.open(output_file, mode='w', newline='') as csvfile:

            fieldnames = ["ticker", "break_even_price", "contract_type", "exercise_style", "expiration_date",
                        "shares_per_contract", "strike_price", "delta", "gamma", "theta", "vega", "implied_volatility",
                        "open_interest", "ask", "ask_size", "bid", "bid_size", "last_updated", "midpoint", "timeframe_quote",
                        "last_trade_conditions", "last_trade_exchange", "last_trade_price", "last_trade_sip_timestamp",
                        "last_trade_size", "timeframe_trade", "day_change", "day_change_percent", "day_close", "day_high",
                        "day_last_updated", "day_low", "day_open", "day_previous_close", "day_volume", "day_vwap",
                        "change_to_break_even", "price", "underlying_ticker"]

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # Write the headers to the CSV file
            await writer.writeheader()

            tasks = [
                self.get_options_snapshot_async(contract, semaphore) for contract in option_contracts
            ]

            snapshots = await asyncio.gather(*tasks)

            for snapshot in snapshots:
                if snapshot:  # Check if the snapshot is not None
                    await self.write_snapshot_to_csv(writer, snapshot)
                    await csvfile.flush()

            return snapshots
    async def get_option_conditions(self):
        """
        Get stock conditions data from the Polygon.io API.
        
        :return: A dictionary with condition IDs as keys and condition names as values.
        """
        url = f"https://api.polygon.io/v3/reference/conditions?asset_class=options&limit=1000&apiKey={self.api_key}"
        response = requests.get(url)
        stock_conditions = {}

        if response.status_code == 200:
            data = response.json()
            conditions_data = data['results']

            for condition in conditions_data:
                condition_id = condition['id']
                condition_name = condition['name']
                stock_conditions[condition_id] = condition_name
        else:
            print(f"Error: {response.status_code}")

        return stock_conditions

    async def load_option_exchanges(self, **kwargs):
        endpoint = "/v3/reference/exchanges"
        exchanges_data = self._request(endpoint, params=kwargs)

        if exchanges_data.get("results"):
            for exchange in exchanges_data["results"]:
                exchange_id = exchange.get("id")
                if exchange_id is not None:
                    self.exchanges_map[str(exchange_id)] = exchange 

    async def get_option_exchanges(self, asset_class=None, locale=None):
        endpoint = "/v3/reference/exchanges"
        params = {}

        if asset_class:
            params["asset_class"] = asset_class
        if locale:
            params["locale"] = locale

        exchanges_data = await self._request(endpoint, params=params)

        return exchanges_data

    async def generate_option_symbol(self, underlying_symbol, expiration_date, option_type, strike_price):
        """
        Generate an option symbol for a given underlying symbol, expiration date, option type, and strike price.

        :param underlying_symbol: The symbol of the underlying stock or ETF.
        :param expiration_date: The expiration date of the option in the format 'YYYY-MM-DD'.
        :param option_type: The option type, 'C' for call or 'P' for put.
        :param strike_price: The strike price of the option as an integer.
        :return: The generated option symbol as a string.
        """
        # Convert the expiration date to the format 'YYMMDD'
        expiration_date_obj = datetime.strptime(expiration_date, "%Y-%m-%d")
        expiration_date_formatted = expiration_date_obj.strftime("%y%m%d")

        # Pad the strike price with two leading zeroes and additional zeroes to reach 8 digits
        # Calculate the total number of digits for strike price and trailing zeroes
        total_digits = 12 - len(underlying_symbol)

        # Pad the strike price with the correct number of leading zeroes and trailing zeroes
        padded_strike = '00{:05.0f}0'.format(float(strike_price) * 100)


        return f"O:{underlying_symbol}{expiration_date_formatted}{option_type}{padded_strike}"


    async def get_aggregate_bars(self, options_ticker, multiplier, timespan, start_date, end_date, adjusted, sort="asc", limit=120, as_dataframe: Optional[bool] = "false") -> List[OptionAggs]:
        """
        Get aggregate bars for an option contract over a given date range in custom time window sizes.

        :param options_ticker: The ticker symbol of the options contract in 'AAPL200918C00260000' format.
        :param multiplier: The size of the timespan multiplier.
        :param timespan: The size of the time window.
        :param start_date: The start of the aggregate time window. Either a date with the format YYYY-MM-DD or a millisecond timestamp.
        :param end_date: The end of the aggregate time window. Either a date with the format YYYY-MM-DD or a millisecond timestamp.
        :param adjusted: Whether or not the results are adjusted for splits. By default, results are adjusted.
        :param sort: Sort the results by timestamp. "asc" will return results in ascending order (oldest at the top), "desc" will return results in descending order (newest at the top).
        :param limit: Limits the number of base aggregates queried to create the aggregate results. Max 50000 and Default 5000.
        :return: A JSON object containing the results.
        """
        async with aiohttp.ClientSession() as session:
            url=f"https://api.polygon.io/v2/aggs/ticker/{options_ticker}/range/{multiplier}/{timespan}/{start_date}/{end_date}?adjusted={adjusted}&limit={limit}&apiKey={self.api_key}"
            print(url)
            async with session.get(url) as response:
                data = await response.json()
                results = data['results']
                
                return [OptionAggs(i) for i in results if i is not None]
        




    async def get_daily_open_close(self, options_ticker, date, adjusted=True):
        """
        Get the open, close, and after-hours prices of an options contract on a certain date.

        :param options_ticker: The ticker symbol of the options contract.
        :param date: The date of the requested open/close in the format YYYY-MM-DD.
        :param adjusted: Whether or not the results are adjusted for splits. Default is True.
        :return: A dictionary containing the response data.
        """
        endpoint = f"/v1/open-close/{options_ticker}/{date}"
        params = {"adjusted": adjusted}
        return await self._request(endpoint, params)

    async def get_previous_close(self, options_ticker, adjusted=True):
        """
        Get the previous day's open, high, low, and close (OHLC) for the specified options contract.

        :param options_ticker: The ticker symbol of the options contract.
        :param adjusted: Whether or not the results are adjusted for splits. Default is True.
        :return: A dictionary containing the response data.
        """
        endpoint = f"/v2/aggs/ticker/{options_ticker}/prev"
        params = {"adjusted": adjusted}
        return await self._request(endpoint, params)
    


    async def get_option_trades(self, symbol, limit=100) -> List[OptionTrade]: 
        """
        Get trades for an options ticker symbol in a given time range.

        :param options_ticker: The options ticker symbol to get trades for.
        :param timestamp: Query by trade timestamp. Either a date with the format YYYY-MM-DD or a nanosecond timestamp.
        :param order: Order results based on the sort field.
        :param limit: Limit the number of results returned, default is 10 and max is 50000.
        :param sort: Sort field used for ordering.
        :return: A DataFrame containing the response data.
        """
        async with aiohttp.ClientSession() as session:
            url=f"https://api.polygon.io/v3/trades/{symbol}?limit={limit}&apiKey={self.api_key}"
            print(url)
            async with session.get(url) as response:
                data = await response.json()
                results = data['results']
                trades = [OptionTrade(i) for i in results]
                return trades
          
    async def get_last_option_trade(self, options_ticker):
        """
        Get the most recent trade for a given options contract.

        :param options_ticker: The ticker symbol of the options contract.
        :return: A dictionary containing the response data.
        """
        endpoint = f"/v2/last/trade/{options_ticker}"
        return await self._request(endpoint)

    async def get_options_quotes(self, options_ticker, timestamp=None, order=None, limit=None, sort=None):
        """
        Get quotes for an options ticker symbol in a given time range.
        
        :param api_key: str, API key to access Polygon.io API
        :param options_ticker: str, The ticker symbol to get quotes for
        :param timestamp: str, optional, Query by timestamp (date format YYYY-MM-DD or a nanosecond timestamp)
        :param order: str, optional, Order results based on the sort field
        :param limit: int, optional, Limit the number of results returned (default is 10, max is 50000)
        :param sort: str, optional, Sort field used for ordering
        :return: dict, JSON response containing quote data
        """
        endpoint = f"/v3/quotes/{options_ticker}"
        params = {}
        if timestamp:
            params += f"&timestamp={timestamp}"
        if order:
            params += f"&order={order}"
        if limit:
            params += f"&limit={limit}"
        if sort:
            params += f"&sort={sort}"

        return await self._request(endpoint)
    

    async def get_option_contract_snapshot(self, underlying_asset, option_contract):
        """
        Get the snapshot of an option contract for a stock equity.

        :param underlying_asset: The underlying ticker symbol of the option contract.
        :param option_contract: The option contract identifier.
        :return: A JSON object containing the option contract snapshot data.
        """
        endpoint = f"{self.base_url}/v3/snapshot/options/{underlying_asset}/{option_contract}?apiKey={self.api_key}"

        async with aiohttp.ClientSession() as session:
            async with session.get(endpoint) as response:
                data = await response.json()
                if data is not None:
                    results = data['results']
                    
                    snapshot = OptionSnapshotData(results) 

                    return snapshot

    
    

    async def get_option_chain(self, underlying_asset, strike_price=None, expiration_date=None, contract_type=None, order=None, limit=10, sort=None):
        """
        Get the snapshot of all options contracts for an underlying ticker.

        :param underlying_asset: The underlying ticker symbol of the option contract.
        :param strike_price: Query by strike price of a contract.
        :param expiration_date: Query by contract expiration with date format YYYY-MM-DD.
        :param contract_type: Query by the type of contract.
        :param order: Order results based on the sort field.
        :param limit: Limit the number of results returned, default is 10 and max is 250.
        :param sort: Sort field used for ordering.
        :return: A JSON object containing the option chain data.
        """
        endpoint = f"/v3/snapshot/options/{underlying_asset}"
        params = {
            "strike_price": strike_price,
            "expiration_date": expiration_date,
            "contract_type": contract_type,
            "order": order,
            "limit": limit,
            "sort": sort
        }

        # Remove parameters with None values
        params = {k: v for k, v in params.items() if v is not None}
        return await self._request(endpoint)

    async def get_option_chain_all(self, underlying_asset, strike_price=None, expiration_date=None, contract_type=None, order=None, limit=250, sort=None):
        """
        Get all options contracts for an underlying ticker across all pages.

        :param underlying_asset: The underlying ticker symbol of the option contract.
        :param strike_price: Query by strike price of a contract.
        :param expiration_date: Query by contract expiration with date format YYYY-MM-DD.
        :param contract_type: Query by the type of contract.
        :param order: Order results based on the sort field.
        :param limit: Limit the number of results returned, default is 10 and max is 250.
        :param sort: Sort field used for ordering.
        :return: A list containing all option chain data across all pages.
        """
        endpoint = f"{self.base_url}/v3/snapshot/options/{underlying_asset}"
        params = {
            "strike_price": strike_price,
            "expiration_date": expiration_date,
            "contract_type": contract_type,
            "order": order,
            "limit": limit,
            "sort": sort,
            "apiKey": self.api_key
        }
        response_data = await self._request_all_pages(endpoint, params=params)
        option_data = OptionSnapshotData(response_data)
  
        return option_data
    

    async def get_index_price(self, ticker=str):
        """Fetch the price of an index ticker"""
        if ticker == "SPX":
            url = f"https://api.polygon.io/v3/snapshot?ticker.any_of=I:{ticker}&apiKey={self.api_key}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:

                    data = await resp.json()
                    results = data['results'] if data['results'] is not None else None
                    if results is None:
                        print(f"Error - results from price request.")
                    value = results[0]['value']
                    return value
    
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
                except KeyError:
                    pass  # Handle the KeyError and continue with the next ticker

        return None  # Return None if the stock price couldn't be retrieved
    
    async def fetch_option_data(self, session, tickers):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.polygon.io/v3/snapshot?ticker.any_of={tickers}&apiKey={YOUR_API_KEY}") as response:
                try:
                    near_money = await response.json(content_type=None)
                    near_money_results = near_money['results']
                    atm_data = UniversalOptionSnapshot(near_money_results)
                    return atm_data.df.sort_values('IV', ascending=True)
                except Exception as e:
                    print(f"Error processing tickers: {tickers}. Error: {e}")
                    return pd.DataFrame()

    async def get_near_the_money_options(self, ticker: str, lower_threshold: float, upper_threshold: float):
        ticker = ticker.upper()
        if ticker.startswith("SPX"):
            price = await self.get_index_price(ticker)
            lower_strike = round(price) * 0.985
            upper_strike = round(price) * 1.015
        else:
            price = await self.get_stock_price(ticker)
            lower_strike = round(price * (1 - lower_threshold/100), 2)
            upper_strike = round(price * (1 + upper_threshold/100), 2)
        print(f"SPX TICKER: {ticker}: {lower_strike}, {price}, {upper_strike}")

        async with aiohttp.ClientSession() as session:
            initial_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte={fifteen_days_from_now_str}&limit=250&apiKey={YOUR_API_KEY}"

            results = await self._request_all_pages(initial_url)
            if results is not None:
                option_data = UniversalOptionSnapshot(results)
                calls = option_data.df[option_data.df['type'] == 'call']
                puts = option_data.df[option_data.df['type'] == 'put']
                calls_grouped = calls.groupby('exp')
                puts_grouped = puts.groupby('exp')

                async def process_grouped_tickers(grouped_df, session):
                    results = []
                    for _, group in grouped_df:
                        group_tickers = group['ticker'].tolist()
                        if not group_tickers:
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

                # Create a list of tasks to run concurrently
                tasks = [
                    process_grouped_tickers(calls_grouped, session),
                    process_grouped_tickers(puts_grouped, session)
                ]

                # Run the tasks concurrently and gather the results
                calls_results, puts_results = await asyncio.gather(*tasks)

                calls_results_df = pd.concat(calls_results)
                puts_results_df = pd.concat(puts_results)

                return calls_results_df, puts_results_df