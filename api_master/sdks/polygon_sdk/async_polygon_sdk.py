import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import asyncio

from .option_snapshot import OptionSnapshotData
from tabulate import tabulate
from .company_info import CompanyResults
from requests import session
from .ticker_news import NewsArticle
import httpx
from .tickernews import TickerNews
from typing import List, Union, Tuple, Optional
from .list_sets import indices_list
from urllib.parse import urlencode, unquote
from .list_sets import subscriptions
import pandas as pd
from .indices_snapshot import IndicesData

from .forex_crypto import ForexSnapshot, CryptoSnapshot
from .technicals.rsi import RSI
from .technicals.macd import MACDData
from .universal_snapshot import UniversalSnapshot
from .financials import BalanceSheet,IncomeStatement,ComprehensiveIncome,CashFlow
from .technicals.sma import SimpleMovingAverage
from _discord import emojis
import csv
from cfg import YOUR_API_KEY

from datetime import datetime, timedelta
from .snapshot import StockSnapshot
import numpy as np
from scipy.signal import argrelextrema
from typing import List, Dict, Any
from .models import Dividend, Condition
from .pivot_points import PivotPointData
from cfg import YOUR_NASDAQ_KEY, seven_days_from_now_str
from .aggregates import AggregatesData
from .quote import Quote
import aiohttp
from datetime import datetime, timedelta
from _discord.embeddings import Data


from cfg import today_str
ten_days_ago = datetime.utcnow() - timedelta(days=5)
date_string = ten_days_ago.strftime("%Y-%m-%dT%H:%M:%SZ")

class AsyncPolygonSDK:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.polygon.io"
        self.conditions_map = None
        self.exchanges_map = {}  # Add this line to define the exchanges_map attribute
        self.session = httpx.AsyncClient()

    async def __aenter__(self):
        await session.__aenter__()
        return self

    async def process_conditions(self, ticker):
        url = f"https://api.polygon.io/v3/quotes/{ticker}?limit=1&apiKey={YOUR_API_KEY}"
        resp = await self.session.get(url)
        data = resp.json()
        if data is not None:
            results = data['results']
            for i in results:
                indicators = i.get('indicators', None)
                conditions = i.get('conditions', None)
                yield indicators, conditions


    async def get_nbbo_quotes(self, ticker):
        async with aiohttp.ClientSession() as session:
            url=f"https://api.polygon.io/v3/quotes/{ticker}?apiKey={YOUR_API_KEY}"
            async with session.get(url) as resp:
                data = await resp.json()
                if data is not None:
                    results = data['results'] if 'results' in data else None
                    return Quote(results)
                



    async def process_news(self):
        async with aiohttp.ClientSession() as session:
            url=f"https://api.polygon.io/v2/reference/news?limit=1000&apiKey={YOUR_API_KEY}"

            async with session.get(url) as resp:
                data = await resp.json()
                results = data['results'] if 'results' in data else None
                if results is not None:
                    return TickerNews(results)

    @staticmethod
    def create_data_model(data_type, data):
        data_model_factories = {
            'stock_snapshot': lambda: StockSnapshot(data),
            # Add other data model factories here...
        }
        return data_model_factories[data_type]() if data_type in data_model_factories else None

    async def initialize(self):
        self.conditions_map = await self.get_stock_conditions()

    async def _request_all_pages_concurrently(self, session, initial_url):
        all_results = []
        next_url = initial_url
        while next_url:
            try:
                async with session.get(next_url) as response:
                    response.raise_for_status()
                    data = await response.json()

                    if "results" in data:
                        all_results.extend(data["results"])

                    next_url = data.get("next_url")
                    if next_url:
                        next_url += f'&apiKey={self.api_key}'

            except aiohttp.ClientResponseError as http_err:
                print(f"An HTTP error occurred: {http_err}")
                break
            except Exception as err:
                print(f"An error occurred: {err}")
                break

        return all_results

    async def get_cik(self, ticker):

        get_cik = await self.company_info(ticker)
        cik = get_cik.cik
        return cik

    async def _request(self, endpoint, params=None):
        if params is None:
            params = {}
        params["apiKey"] = self.api_key
        url = f"{self.base_url}{endpoint}"
        try:
            response = await self.session.get(url, params=params)
            response.raise_for_status()
        except httpx.HTTPError as http_err:
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
                response = await self.session.get(next_url, params=params)
                response.raise_for_status()
                data = response.json()

                if "results" in data:
                    all_results.extend(data["results"])

                # Check if there is a next_url
                next_url = data.get("next_url")
                if next_url:
                    next_url += f'&{urlencode({"apiKey": self.api_key})}'
                    params = {}
                else:
                    break  # Break the loop if there is no next_url

            except httpx.HTTPError as http_err:
                print(f"An HTTP error occurred: {http_err}")
                break
            except Exception as err:
                print(f"An error occurred: {err}")
                break

        return all_results

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


            

    async def get_all_crypto_snapshots(self) -> List[CryptoSnapshot]:
        """Fetch all Crypto snapshots"""
        url=f"https://api.polygon.io/v2/snapshot/locale/global/markets/crypto/tickers?apiKey={self.api_key}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                tickers = data.get('tickers', None)
                crypto_snapshots = CryptoSnapshot(tickers)
                return crypto_snapshots          
            
    async def get_all_forex_snapshots(self) -> List[ForexSnapshot]:
        """Fetch all Forex snapshots"""
        url=f"https://api.polygon.io/v2/snapshot/locale/global/markets/forex/tickers?apiKey={self.api_key}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                tickers = data.get('tickers', None)
                forex_snapshots = ForexSnapshot(tickers)
                return forex_snapshots

    async def get_all_tickers(self, include_otc=False) -> List[StockSnapshot]:
        """
        Fetches a list of all stock tickers available on Polygon.io.

        Returns:
            A list of StockSnapshot objects, each containing data for a single stock ticker.

        Usage:
            To fetch a list of all stock tickers available on Polygon.io, you can call:
            ```
            tickers = await sdk.get_all_tickers()
            print(f"Number of tickers found: {len(tickers)}")
            ```
        """
        url = f"https://api.polygon.io/v2/snapshot/locale/us/markets/stocks/tickers?include_otc={include_otc}&apiKey={self.api_key}"
        params = {
            "apiKey": self.api_key,
        }
        print(url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                response_data = await response.json()



                tickers = response_data['tickers']
                print(tickers)
                ticker_data = [StockSnapshot(ticker) for ticker in response_data['tickers'] if ticker is not None]
                return ticker_data


    async def fetch_historical_data(self, pair, days, timeframe, multiplier):
        now = datetime.now()
        days_ago = now - timedelta(days=days)
        to_date = now.strftime("%Y-%m-%d")
        from_date = days_ago.strftime("%Y-%m-%d")

        endpoint = f"/v2/aggs/ticker/X:{pair}/range/{multiplier}/{timeframe}/{from_date}/{to_date}?adjusted=true&sort=asc&limit=5000"
        data = await self._request(endpoint)

        if isinstance(data, dict):
            if "results" not in data or not data["results"]:
                print(f"Warning: No historical data found for {pair}. API response: {data}")
                return []
            else:
                return data["results"]
        else:
            print(f"Error fetching historical data for {pair}. API response: {data}")
            raise ValueError("Error fetching historical data")

    async def get_stock_snapshot(self, ticker):
        """
        Get the stock snapshot for the given ticker symbol.
        
        :param ticker: The stock ticker symbol as a string.
        :return: An instance of the StockSnapshot class.
        """
        async with aiohttp.ClientSession() as session:
            url=f"https://api.polygon.io/v2/snapshot/locale/us/markets/stocks/tickers/{ticker}?apiKey={YOUR_API_KEY}"
            print(url)
            async with session.get(url) as resp:
                data = await resp.json()
                if data is None:
                    return
                results = data['ticker'] if 'ticker' in data else None
                if results is not None:
                    return StockSnapshot(results)

    

    async def find_gaps(self, o, h, l, c, t):
        """
        Finds the gap-up and gap-down points in the given stock data.

        Args:
            o (List[float]): The list of opening prices.
            h (List[float]): The list of high prices.
            l (List[float]): The list of low prices.
            c (List[float]): The list of closing prices.
            t (List[datetime]): The list of timestamps corresponding to each data point.

        Returns:
            A pandas DataFrame containing the indices and timestamps of gap-up and gap-down points.

        Usage:
            To find gap-up and gap-down points in the stock data for a given symbol, you can call:
            ```
            o, h, l, c, t = await sdk.get_stock_data("AAPL")
            gap_df = await sdk.find_gaps(o, h, l, c, t)
            print(gap_df)
            ```
        """
        gap_ups = []
        gap_downs = []

        for i in range(1, len(o)):
            if o[i] > h[i-1]:
                gap_ups.append(i)
            elif o[i] < l[i-1]:
                gap_downs.append(i)
        t = [datetime.fromtimestamp(ts / 1000) for ts in t]

        gap_ups_data = []
        for i in gap_ups:
            gap_low, gap_high = await self.find_gap_price_range(o, h, l, c, t, i)
            filled_timestamp = await self.find_gap_price_range(o, h, l, c, t, i, filled=True)
            gap_ups_data.append((t[i].strftime('%Y-%m-%d'), i, gap_low, gap_high, filled_timestamp))

        gap_downs_data = []
        for i in gap_downs:
            gap_low, gap_high = await self.find_gap_price_range(o, h, l, c, t, i)
            filled_timestamp = await self.find_gap_price_range(o, h, l, c, t, i, filled=True)
            gap_downs_data.append((t[i].strftime('%Y-%m-%d'), i, gap_low, gap_high, filled_timestamp))

        gap_up_df = pd.DataFrame(
            gap_ups_data,
            columns=['Dates', 'Indices', 'Gap Low', 'Gap High', 'Filled Timestamp']
        )
        gap_up_df.insert(0, 'Type', 'Gap-up')

        gap_down_df = pd.DataFrame(
            gap_downs_data,
            columns=['Dates', 'Indices', 'Gap Low', 'Gap High', 'Filled Timestamp']
        )
        gap_down_df.insert(0, 'Type', 'Gap-down')

        gap_df = pd.concat([gap_up_df, gap_down_df], ignore_index=True)

        return gap_df




    async def find_gap_price_range(self, o, h, l, c, t, gap_index, filled=None) -> Union[Tuple[Optional[float], Optional[float]], Optional[datetime]]:

        """
        Finds the price range for the gap at the specified index, and optionally finds the timestamp at which the gap was filled.

        Args:
            o (List[float]): The list of opening prices.
            h (List[float]): The list of high prices.
            l (List[float]): The list of low prices.
            c (List[float]): The list of closing prices.
            t (List[datetime]): The list of timestamps corresponding to each data point.
            gap_index (int): The index of the gap for which to find the price range.
            filled (Optional[bool]): If True, finds the timestamp at which the gap was filled. If False or None,
                only returns the low and high prices for the gap.

        Returns:
            If filled is False or None, returns a tuple containing the low and high prices for the gap.
            If filled is True and the gap was filled, returns the timestamp at which the gap was filled.
            If filled is True and the gap was not filled, returns None.

        Usage:
            To find the price range for a gap in the stock data and optionally find the timestamp at which the gap was filled, you can call:
            ```
            o, h, l, c, t = await sdk.get_stock_data("AAPL")
            gap_ups, gap_downs = await sdk.find_gaps(o, h, l, c, t)"""
       
        if o[gap_index] > h[gap_index - 1]:
            direction = "up"
            gap_low = h[gap_index - 1]
            gap_high = l[gap_index]
        elif o[gap_index] < l[gap_index - 1]:
            direction = "down"
            gap_low = h[gap_index]
            gap_high = l[gap_index - 1]
        else:
            direction = "unknown"
            gap_low = None
            gap_high = None

        if filled is None:
            return gap_low, gap_high
        else:
            fill_index = None
            for i in range(gap_index + 1, len(c)):
                if direction == "up":
                    if l[i] <= gap_high and h[i] >= gap_low:
                        fill_index = i
                        break
                elif direction == "down":
                    if h[i] >= gap_high and l[i] <= gap_low:
                        fill_index = i
                        break

            if filled is True:
                if fill_index is not None:
                    return t[fill_index]
                else:
                    return None
            else:
                if fill_index is not None:
                    return t[fill_index]
                else:
                    return None     
    async def get_exchanges(self, asset_class=None, locale=None) -> Dict[str, Any]:
        """
        Get exchanges data from the Polygon.io API.

        :param asset_class: Optional string specifying the asset class to filter exchanges (e.g., 'stocks', 'options', 'crypto', 'fx').
        :param locale: Optional string specifying the locale to filter exchanges (e.g., 'us', 'global').
        :return: A dictionary containing the exchanges data.
        """
        endpoint = "/v3/reference/exchanges"
        params = {}

        if asset_class:
            params["asset_class"] = asset_class
        if locale:
            params["locale"] = locale

        exchanges_data = await self._request(endpoint, params=params)

        return exchanges_data
        
    async def all_options(self, ticker:str, expiration_date: Optional[str] = seven_days_from_now_str):
        """Returns all options contracts for a ticker"""
        async with aiohttp.ClientSession() as session:
            all_option_data = []
            url=f"https://api.polygon.io/v3/snapshot/options/{ticker}?expiration_date.lte={expiration_date}&limit=250&apiKey={YOUR_API_KEY}"
            async with session.get(url) as resp:
                results = await self._request_all_pages_concurrently(session, url)
                if results is not None:
                    option_data = OptionSnapshotData(results)
                    return option_data

    async def get_top_gainers(self):
        async with aiohttp.ClientSession() as session:
            url=f"https://api.polygon.io/v2/snapshot/locale/us/markets/stocks/gainers?include_otc=false&apiKey={YOUR_API_KEY}"
            async with session.get(url) as resp:
                data = await resp.json()
                tickers = [i['ticker'] if 'ticker' is not None and 'ticker' in i else None for i in data]
                return tickers
            

    async def all_snapshots(self, type):
        """Returns all snapshots for a data type.
        
        types:

        >>> indices
        >>> options
        >>> stocks
        >>> crypto
        >>> forex

    
        """
        async with aiohttp.ClientSession() as session:
            url=f"https://api.polygon.io/v3/snapshot?type={type}&limit=250&apiKey={YOUR_API_KEY}"
            async with session.get(url):
                data = await self._request_all_pages_concurrently(session, url)
                print(data)
                if data is not None:
                    results = [i['results'] if 'results' in i else None for i in data]
                    if type == "indices":
                        indices_data = IndicesData(results)
                        return indices_data
                    elif type == "options":
                        option_data = OptionSnapshotData(results)
                        return option_data
                    elif type == "crypto":
                        crypto_data = CryptoSnapshot(results)
                        return crypto_data
                    elif type == "forex":
                        forex_data = ForexSnapshot(results)
                        return forex_data
                    elif type == "stocks":
                        stock_data = StockSnapshot(results)
                        return stock_data
                    else:
                        return None

                
                    



    async def last_trade_condition(self, ticker:str):
        """Returns the last trade and accompanying data for a ticker"""
        async with aiohttp.ClientSession() as session:
            url=f"https://api.polygon.io/v2/last/trade/{ticker}?apiKey={YOUR_API_KEY}"
            async with session.get(url) as resp:
                data = await resp.json()
                if data is None:
                    return
                else:
                    results = data['results'] if 'results' in data else None
                    last_condition = results['c'] if 'c' in results else None
                    return last_condition

    async def last_quote_condition(self, ticker:str):
        """Returns last quote condition for a ticker."""
        async with aiohttp.ClientSession() as session:
            url=f"https://api.polygon.io/v3/quotes/{ticker}?limit=1&apiKey={YOUR_API_KEY}"
            async with session.get(url) as resp:
                data = await resp.json()
                if data is None:
                    return
                else:
                    results = data['results'] if 'results' in data else None
                    condition = [i['conditions'] if 'conditions' in i else None for i in results]
                    indicator = [i['indicators'] if 'indicators' in i else None for i in results]
                    return condition, indicator
  



    async def get_polygon_logo(self, symbol: str) -> Optional[str]:
        """
        Fetches the URL of the logo for the given stock symbol from Polygon.io.

        Args:
            symbol: A string representing the stock symbol to fetch the logo for.

        Returns:
            A string representing the URL of the logo for the given stock symbol, or None if no logo is found.

        Usage:
            To fetch the URL of the logo for a given stock symbol, you can call:
            ```
            symbol = "AAPL"
            logo_url = await sdk.get_polygon_logo(symbol)
            if logo_url is not None:
                print(f"Logo URL: {logo_url}")
            else:
                print(f"No logo found for symbol {symbol}")
            ```
        """
        url = f'https://api.polygon.io/v3/reference/tickers/{symbol}?apiKey={self.api_key}'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                
                if 'results' not in data:
                    # No results found
                    return None
                
                results = data['results']
                branding = results.get('branding')

                if branding and 'icon_url' in branding:
                    encoded_url = branding['icon_url']
                    decoded_url = unquote(encoded_url)
                    url_with_api_key = f"{decoded_url}?apiKey={self.api_key}"
                    return url_with_api_key    
                    




    async def get_stock_conditions(self, type, conditions) -> Dict[int, str]:
        """
        Get stock conditions data from the Polygon.io API.

        :return: A dictionary with condition IDs as keys and condition names as values.
        """
        for c in conditions:
            url = f"https://api.polygon.io/v3/reference/conditions?id={c}&limit=1000&apiKey={self.api_key}"
            stock_conditions = {}

            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        conditions_data = data['results']

                        for condition in conditions_data:
                            condition_id = condition['id']
                            condition_name = condition['name']
                            print(condition_name)
                            stock_conditions[condition_id] = condition_name
                        else:
                            print(f"Error: {response.status}")

            return stock_conditions

    async def fetch_condition_names(self, trade_conditions):

        stock_conditions = {}

        for condition in trade_conditions:
            name = await self.get_stock_conditions(type="stocks", condition=condition)
            stock_conditions[condition] = name

        return stock_conditions

    async def get_quotes(self, ticker, **kwargs):
        """
        Get NBBO quotes for a ticker symbol in a given time range.

        :param ticker: The stock ticker symbol.
        :param kwargs: Optional keyword arguments.
            timestamp: Query by timestamp. Either a date with the format 'YYYY-MM-DD' or a nanosecond timestamp.
            order: Order results based on the sort field.
            limit: Limit the number of results returned, default is 10 and max is 50000.
            sort: Sort field used for ordering.
        :return: A list of Quote objects containing the NBBO quotes for the specified stock ticker.
        """
        endpoint = f"/v3/quotes/{ticker}"

        response_data = await self._request(endpoint, params=kwargs)
        if response_data is None:
            return []

        ticker_data = [Quote.from_dict(ticker) for ticker in response_data.get('results', []) if ticker is not None]
        return ticker_data
    
    async def get_aggregates(self, ticker, multiplier, timespan, from_date, to_date, limit=1000):
        """
        Retrieve aggregate data for a given stock ticker.

        :param stock_ticker: The stock ticker symbol as a string.
        :param multiplier: The multiplier for the timespan as an integer.
        :param timespan: The timespan as a string (e.g., "minute", "hour", "day", "week", "month", "quarter", "year").
        :param from_date: The start date for the data as a string in YYYY-MM-DD format.
        :param to_date: The end date for the data as a string in YYYY-MM-DD format.
        :return: An instance of AggregatesData containing the aggregate data.
        """
        url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/{multiplier}/{timespan}/{from_date}/{to_date}?adjusted=true&limit={limit}&apiKey={YOUR_API_KEY}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                all_results = []
                next_url = url
                data = await response.json()
                while next_url:
                    try:
                        response = await self.session.get(next_url)
                        response.raise_for_status()
                        data = response.json()

                        if "results" in data:
                            all_results.extend(data["results"])

                        next_url = data.get("next_url")
                        if next_url:
                            next_url += f'&{urlencode({"apiKey": self.api_key})}'

                    except httpx.HTTPError as http_err:
                        print(f"An HTTP error occurred: {http_err}")
                        break
                    except Exception as err:
                        print(f"An error occurred: {err}")
                        break

                aggregates_data = AggregatesData({"results": all_results, "ticker": ticker})

                return aggregates_data
            

    async def get_support_resistance_levels(self, stock_ticker, multiplier, timespan, from_date, to_date, window=10):
        """
        Calculate support and resistance levels for a given stock ticker using historic aggregate data.

        :param stock_ticker: The stock ticker symbol as a string.
        :param multiplier: The multiplier for the timespan as an integer.
        :param timespan: The timespan as a string (e.g., "minute", "hour", "day", "week", "month", "quarter", "year").
        :param from_date: The start date for the data as a string in YYYY-MM-DD format.
        :param to_date: The end date for the data as a string in YYYY-MM-DD format.
        :param window: The window size for finding local minima and maxima as an integer (default: 10).
        :return: A tuple containing two lists: support levels and resistance levels.
        """
        # Retrieve historic aggregate data
        try:
            aggregates_data = await self.get_aggregates(stock_ticker, multiplier, timespan, from_date, to_date, limit=50000)
            closing_prices = np.array([agg["c"] for agg in aggregates_data.results])

            # Define comparator functions for local minima and maxima
            local_minima_comparator = np.less
            local_maxima_comparator = np.greater

            # Find local minima and maxima within the specified window
            local_minima_indices = argrelextrema(closing_prices, local_minima_comparator, order=window)
            local_maxima_indices = argrelextrema(closing_prices, local_maxima_comparator, order=window)

            # Extract support and resistance levels from local minima and maxima
            support_levels = closing_prices[local_minima_indices].tolist()
            resistance_levels = closing_prices[local_maxima_indices].tolist()
            return support_levels[0], resistance_levels[0]
        except (TypeError, KeyError):
            print(f"Error")



        
    

    async def get_simple_moving_average(self, symbol, timestamp=None, timespan='day', adjusted=True, window=50,
                                series_type='close', expand_underlying=True, order='desc', limit=10):
        """
        Get the simple moving average (SMA) for a ticker symbol over a given time range for a ticker or options symbol.

        :param ticker: The stock ticker symbol or options symbol. Use 'generate_option_symbol' to create the needed symbol.
        :param timestamp: Optional timestamp. Either a date with the format YYYY-MM-DD or a millisecond timestamp.
        :param timespan: Optional aggregate time window. Default is 'day'.
        :param adjusted: Optional boolean to adjust aggregates for splits. Default is True.
        :param window: Optional window size to calculate the SMA. Default is 50.
        :param series_type: Optional price to use for SMA calculation. Default is 'close'.
        :param expand_underlying: Optional boolean to include aggregates in the response. Default is False.
        :param order: Optional order to return results, ordered by timestamp. Default is 'desc'.
        :param limit: Optional limit for the number of results returned. Default is 10, max is 5000.
        >>> Symbol prefixes:

            >>> crypto = X:

            >>> forex = C:

            >>> options = O:

            >>> indices = I:

            >>> stocks = None

        :return: A list of SMA values.
        """
        url = f"https://api.polygon.io/v1/indicators/sma/{symbol}?timespan={timespan}&adjusted={adjusted}&window={window}&series_type=close&order={order}&limit={limit}&apiKey={self.api_key}"
            # Remove parameters with None values


        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                try:
                    results = data['results']
                    values = results['values']
                    value = [i['value'] if i['value'] is not None else None for i in values]
                    timestamps = [i['timestamp'] if i['timestamp'] is not None else None for i in values]
                    timestamps = await self.format_timestamps_list(timestamps)



                    return value, timestamps
                except (TypeError, KeyError):
                    pass




    async def get_exponential_moving_average(self, symbol, timestamp=None, timespan: str=None, adjusted=True, window: str=None, series_type="close", expand_underlying=None, order="desc", limit: str=None):
        """
        Get the exponential moving average (EMA) for a ticker symbol over a given time range.

        :param ticker: The stock ticker symbol or options symbol. Use 'generate_option_symbol' to create the needed symbol.
        :param timestamp: Query by timestamp. Either a date with the format YYYY-MM-DD or a millisecond timestamp.
        :param timespan: The size of the aggregate time window.
        :param adjusted: Whether or not the aggregates used to calculate the EMA are adjusted for splits.
        :param window: The window size used to calculate the EMA.
        :param series_type: The price in the aggregate which will be used to calculate the EMA.
        :param expand_underlying: Whether or not to include the aggregates used to calculate this indicator in the response.
        :param order: The order in which to return the results, ordered by timestamp.
        :param limit: Limit the number of results returned, default is 10 and max is 5000.

        >>> Symbol prefixes:

            >>> crypto = X:

            >>> forex = C:

            >>> options = O:

            >>> indices = I:

            >>> stocks = None

        :return: A list of SMA values.
        """
        url = f"https://api.polygon.io/v1/indicators/ema/{symbol}?timespan={timespan}&adjusted={adjusted}&window={window}&series_type=close&order={order}&limit={limit}&apiKey={self.api_key}"
            # Remove parameters with None values


        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                try:
                    results = data['results']
                    values = results['values']
                    timestamps = [i['timestamp'] if i['timestamp'] is not None else None for i in values]
                    value = [i['value'] if i['value'] is not None else None for i in values]
                    timestamps = await self.format_timestamps_list(timestamps)




                    return value, timestamps
                except (TypeError, KeyError):
                    pass



    async def company_info(self, ticker):
        url = f"https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={self.api_key}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                return CompanyResults(data)

    async def get_cik(self, ticker):

        get_cik = await self.company_info(ticker)
        cik = get_cik.cik
        return cik          

    async def get_macd(self, symbol, timestamp=None, timespan: str=None, adjusted=True, short_window=12, long_window=26, signal_window=9, series_type="close", expand_underlying=None, order="desc", limit: str=None):
        """
        Get moving average convergence/divergence (MACD) data for a ticker symbol over a given time range.

        :param ticker: The stock ticker symbol or options symbol. Use 'generate_option_symbol' to create the needed symbol.
        :param timestamp: Query by timestamp. Either a date with the format YYYY-MM-DD or a millisecond timestamp.
        :param timespan: The size of the aggregate time window.
        :param adjusted: Whether or not the aggregates used to calculate the MACD are adjusted for splits.
        :param short_window: The short window size used to calculate MACD data.
        :param long_window: The long window size used to calculate MACD data.
        :param signal_window: The window size used to calculate the MACD signal line.
        :param series_type: The price in the aggregate which will be used to calculate the MACD.
        :param expand_underlying: Whether or not to include the aggregates used to calculate this indicator in the response.
        :param order: The order in which to return the results, ordered by timestamp.
        :param limit: Limit the number of results returned, default is 10 and max is 5000.

        >>> Symbol prefixes:



            >>> crypto = X:

            >>> forex = C:

            >>> options = O:

            >>> indices = I:

            >>> stocks = None

        returns: A list of MACD values, histogram values, and signal values.
        """
        endpoint = f"/v1/indicators/macd/{symbol}"
        params = {
            "timestamp": timestamp,
            "timespan": timespan,
            "adjusted": adjusted,
            "short_window": short_window,
            "long_window": long_window,
            "signal_window": signal_window,
            "series_type": series_type,
            "expand_underlying": expand_underlying,
            "order": order,
            "limit": limit
        }

        # Remove parameters with None values
        params = {k: v for k, v in params.items() if v is not None}

        request = await self._request(endpoint, params=params)
        try:
            results = request['results']
            values = results['values']
            macd = [i['value'] for i in values]
            signal = [i['signal'] for i in values]
            histogram = [i['histogram'] for i in values]
            if values is not None:
                return MACDData(values)
        except (KeyError, TypeError) as e:
            print(f"KeyError in get_macd: {e}. The requested key is not available in the response.")
            return None


    async def get_and_check_bullish(self,ticker, timespan:str="hour"):
        hist = await self.get_macd(ticker, timespan=timespan)
        rsi = await self.get_rsi(ticker, timespan=timespan)  # Assume you have a method to get RSI

        macd_bullish = await self.get_and_check_bullish(hist)
        rsi_bullish = await self.get_and_check_bullish(rsi)

        return ticker, macd_bullish, rsi_bullish

    async def get_and_check_bearish(self,ticker, timespan:str="hour"):
        hist = await self.get_macd(ticker, timespan=timespan)
        rsi = await self.get_rsi(ticker, timespan=timespan)  # Assume you have a method to get RSI

        macd_bearish = await self.get_and_check_bearish(hist)
        rsi_bearish = await self.get_and_check_bearish(rsi)

        return ticker, macd_bearish, rsi_bearish
    
    async def get_upside_downside(self, tickers, timespan:str="hour"):
        bearish_tasks = [self.get_and_check_bearish(ticker, timespan) for ticker in tickers]
        bullish_tasks = [self.get_and_check_bullish(ticker, timespan) for ticker in tickers]
        bearish_results = await asyncio.gather(*bearish_tasks)
        bullish_results = await asyncio.gather(*bullish_tasks)

        bearish_df = pd.DataFrame(bearish_results, columns=['ticker', 'macd_bearish', 'rsi_bearish'])
        bullish_df = pd.DataFrame(bullish_results, columns=['ticker', 'macd_bullish', 'rsi_bullish'])

        # Filter the dataframes to only include rows where both conditions are met
        bearish_df = bearish_df[(bearish_df['macd_bearish'] == True) & (bearish_df['rsi_bearish'] == True)]
        bullish_df = bullish_df[(bullish_df['macd_bullish'] == True) & (bullish_df['rsi_bullish'] == True)]

        # Drop duplicates
        bearish_df = bearish_df.drop_duplicates('ticker')
        bullish_df = bullish_df.drop_duplicates('ticker')

        return bearish_df, bullish_df


    async def get_pivot_points(self, stock_ticker, multiplier, timespan, from_date, to_date):
        """
        Calculate pivot points and corresponding support and resistance levels for a given stock ticker using historic aggregate data.

        :param stock_ticker: The stock ticker symbol as a string.
        :param multiplier: The multiplier for the timespan as an integer.
        :param timespan: The timespan as a string (e.g., "minute", "hour", "day", "week", "month", "quarter", "year").
        :param from_date: The start date for the data as a string in YYYY-MM-DD format.
        :param to_date: The end date for the data as a string in YYYY-MM-DD format.
        :return: A list of dictionaries, each containing the pivot point, support levels, and resistance levels for each time period with a formatted timestamp.
        """
        aggregates_data = await self.get_aggregates(stock_ticker, multiplier, timespan, from_date, to_date)
        aggregates = aggregates_data.results

        if aggregates is None or aggregates_data.results is None:
            return []

        pivot_points_data = []

        for i in range(1, len(aggregates)):
            high = aggregates[i - 1]["h"]
            low = aggregates[i - 1]["l"]
            close = aggregates[i - 1]["c"]

            pivot_point = (high + low + close) / 3
            resistance1 = 2 * pivot_point - low
            resistance2 = pivot_point + (high - low)
            support1 = 2 * pivot_point - high
            support2 = pivot_point - (high - low)

            timestamp = datetime.fromtimestamp(aggregates[i]["t"] / 1000)
            formatted_timestamp = await self.format_timestamp(timestamp)

            pivot_data = PivotPointData(
                timestamp=formatted_timestamp,
                pivot_point=pivot_point,
                resistance1=resistance1,
                resistance2=resistance2,
                support1=support1,
                support2=support2
            )

            pivot_points_data.append(pivot_data)

        return pivot_data

    async def get_all_macd(self, symbol:str, timestamp_greater_than:str="2023-01-01", timstamp_less_than:str=today_str,timespan:str="hour", limit:str=1000):
            all_results =[]
            async with aiohttp.ClientSession() as session:
                url=f"https://api.polygon.io/v1/indicators/macd/{symbol}?timespan={timespan}&timestamp.gte={timestamp_greater_than}&timestamp.lte={timstamp_less_than}&adjusted=true&short_window=12&long_window=26&signal_window=9&series_type=close&order=desc&limit={limit}&apiKey={YOUR_API_KEY}"
                while url:
                    print(url)
                    async with session.get(url) as response:
                        data = await response.json()
                        try:
                            all_results.extend(data['results']['values'])
                        except KeyError:
                            continue  # Extracting the 'values' part of the 'results'
                        next_url = data.get('next_url', None)  # Get the next URL or set to None if it doesn't exist
                        if next_url:
                            url = f"{next_url}&apiKey={self.api_key}"  # Append the API key to the next URL
                        else:
                            url = None
            return MACDData(all_results)    

    async def get_all_aggregates(self, ticker, multiplier, timespan, from_date, to_date, limit=1000):
        """
        Retrieve aggregate data for a given stock ticker.

        :param stock_ticker: The stock ticker symbol as a string.
        :param multiplier: The multiplier for the timespan as an integer.
        :param timespan: The timespan as a string (e.g., "minute", "hour", "day", "week", "month", "quarter", "year").
        :param from_date: The start date for the data as a string in YYYY-MM-DD format.
        :param to_date: The end date for the data as a string in YYYY-MM-DD format.
        :return: An instance of AggregatesData containing the aggregate data.
        """
        url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/{multiplier}/{timespan}/{from_date}/{to_date}?adjusted=true&limit={limit}&apiKey={YOUR_API_KEY}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                all_results = []
                next_url = url
                data = await response.json()
                while next_url:
                    try:
                        response = await self.session.get(next_url)
                        response.raise_for_status()
                        data = response.json()

                        if "results" in data:
                            all_results.extend(data["results"])

                        next_url = data.get("next_url")
                        if next_url:
                            next_url += f'&{urlencode({"apiKey": self.api_key})}'

                    except httpx.HTTPError as http_err:
                        print(f"An HTTP error occurred: {http_err}")
                        break
                    except Exception as err:
                        print(f"An error occurred: {err}")
                        break

                aggregates_data = AggregatesData({"results": all_results, "ticker": ticker})

                return aggregates_data
               
    async def get_all_rsi(self, symbol, timespan="hour", window=14, limit=1000, timestamp_greater_than:str="2023-01-01", timestamp_less_than=today_str):
        all_results = []
        url = f"https://api.polygon.io/v1/indicators/rsi/{symbol}?timespan={timespan}&window={window}&limit={limit}&timestamp.gte={timestamp_greater_than}&timestamp.lte={timestamp_less_than}&apiKey={self.api_key}"
        print(url)
        async with aiohttp.ClientSession() as session:
            while url:
                async with session.get(url) as response:
                    data = await response.json()
                    all_results.extend(data['results']['values'])  # Extracting the 'values' part of the 'results'
                    next_url = data.get('next_url', None)  # Get the next URL or set to None if it doesn't exist
                    if next_url:
                        url = f"{next_url}&apiKey={self.api_key}"  # Append the API key to the next URL
                    else:
                        url = None

        return RSI(all_results)
    
    async def rsi_snapshot(self, ticker:str):
        rsi  = await self.get_rsi(symbol=ticker,timespan="hour",window=14)
        rsi_hour_value = rsi[0] if rsi is not None and len(rsi) > 0 else None
        rsi_min = await self.get_rsi(symbol=ticker, timespan="minute",window=14)
        rsi_min_value = rsi_min[0] if rsi_min is not None and len(rsi_min) > 0 else None
        rsi_day = await self.get_rsi(symbol=ticker, timespan="day", window=14)
        rsi_day_value = rsi_day[0] if rsi_day is not None and len(rsi_day) > 0 else None
        rsi_week = await self.get_rsi(symbol=ticker, timespan="week", window=14)
        rsi_week_value = rsi_week[0] if rsi_week is not None and len(rsi_week) > 0 else None
        rsi_month = await self.get_rsi(symbol=ticker, window=14, timespan="month")
        rsi_month_value = rsi_month[0] if rsi_month is not None and len(rsi_month) > 0 else None
        rsi_quarter = await self.get_rsi(symbol=ticker, window=14, timespan="quarter")
        rsi_quarter_value = rsi_quarter[0] if rsi_quarter is not None and len(rsi_quarter) > 0 else None
        rsi_year = await self.get_rsi(symbol=ticker, timespan="year")
        rsi_year_value = rsi_year[0] if rsi_year is not None and len(rsi_year) > 0 else None

        if rsi_min_value is not None and rsi_min_value > 70:
            rsi_min_result = "🐻"
        elif rsi_min_value is not None and rsi_min_value < 30:
            rsi_min_result = "🐂"
        else:
            rsi_min_result = ""

        if rsi_day_value is not None and rsi_day_value > 70:
            rsi_day_result = "🐻"
        elif rsi_day_value is not None and rsi_day_value < 30:
            rsi_day_result = "🐂"
        else:
            rsi_day_result = ""
 

        if rsi_week_value is not None and rsi_week_value > 70:
            rsi_week_result = "🐻"
        elif rsi_week_value is not None and rsi_week_value < 30:
            rsi_week_result = "🐂"
        else:
            rsi_week_result = ""           
  

        if rsi_month_value is not None and rsi_month_value > 70:
            rsi_month_result = "🐻"
        elif rsi_month_value is not None and rsi_month_value < 30:
            rsi_month_result = "🐂"
        else:
            rsi_month_result = "" 

        if rsi_hour_value is not None and rsi_hour_value > 70 :
            rsi_hour_result = "🐻"
        elif rsi_hour_value is not None and rsi_hour_value < 30:
            rsi_hour_result = "🐂"
        else:
            rsi_hour_result = ""

        if rsi_quarter_value is not None and rsi_quarter_value > 70:
            rsi_quarter_result = "🐻"
        elif rsi_quarter_value is not None and rsi_quarter_value < 30:
            rsi_quarter_result = "🐂"
        else:
            rsi_quarter_result = ""


        if rsi_year_value is not None and rsi_year_value > 70:
            rsi_year_result = "🐻"
        elif rsi_year_value is not None and rsi_year_value < 30:
            rsi_year_result = "🐂"
        else:
            rsi_year_result = ""

        self.data_dict = { 

            'Minute': (rsi_min_value, rsi_min_result),
            'Hour': (rsi_hour_value, rsi_hour_result),
            'Day': (rsi_day_value, rsi_day_result),
            'Week': (rsi_week_value, rsi_week_result),
            'Month': (rsi_month_value, rsi_month_result),
            'Quarter': (rsi_quarter_value, rsi_quarter_result),
            'Year': (rsi_year_value, rsi_year_result)
        }

        self.df = pd.DataFrame(self.data_dict).transpose()

        self.table = tabulate(self.df, headers=['Timespan', 'Value', 'Bull/Bear'], tablefmt='fancy', showindex=True)


        return self.table
    async def check_ticker(self, ticker):
        timespans = ['minute', 'hour', 'day', 'week', 'month', 'quarter', 'year']
        results = []
        for timespan in timespans:
            bear_result = await self.check_macd_condition_bearish(ticker, timespan=timespan)
            bull_result = await self.check_macd_condition_bullish(ticker, timespan=timespan)
            rsi = await self.get_rsi(ticker, timespan)
            
            bear_rsi_result = await self.check_rsi_condition_bearish(rsi)
            bull_rsi_result = await self.check_rsi_condition_bearish(rsi)

            results.append((ticker, timespan, bear_result, bull_result, bear_rsi_result, bull_rsi_result))
        return results

    async def check_rsi_condition_bullish(self,rsi):
        if rsi is not None and len(rsi) > 0:
            return rsi[0] <= 32


    async def check_rsi_condition_bearish(self, rsi):
        if rsi is not None and len(rsi) > 0:
            return rsi[0] >= 68
        


    async def check_macd_condition_bullish(self, ticker, timespan):
        data = await self.get_macd(ticker, timespan=timespan)
        if data is not None:
            hist = data.histogram
            if hist is not None:
                if hist is not None and len(hist) >= 3:
                    
                        last_three_values = hist[:3]
                        print(last_three_values)
                        return (
                            abs(last_three_values[0] - (-0.03)) < 0.02
                            and all(last_three_values[i] > last_three_values[i + 1] for i in range(len(last_three_values) - 1))
                        )
                    


    async def check_macd_condition_bearish(self, ticker, timespan):
        data = await self.get_macd(ticker, timespan=timespan)
        if data is not None:
            hist = data.histogram
            if hist is not None and len(hist) >= 3:

            

                last_three_values = hist[:3]
                print(last_three_values)
                return (
                    abs(last_three_values[0] - 0.03) < 0.02
                    and all(last_three_values[i] < last_three_values[i + 1] for i in range(len(last_three_values) - 1))
                )



    async def get_sec_filings(self, ticker):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
            "Accept-Encoding": "gzip, deflate",

        }
        async with aiohttp.ClientSession() as session:
            
            cik = await self.get_cik(ticker)
            url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()

    async def write_snapshots_to_csv(self):
        """Gets all snapshots market-wide and saves
        to CSV for further analysis / testing purposes."""

        tickers = await self.get_all_tickers()


        symbol = [i.ticker for i in tickers]

        last_trade_conditions = [i.last_trade.conditions for i in tickers]
        last_trade_exchange = [i.last_trade.trade_exchange for i in tickers]
        last_trade_price = [i.last_trade.trade_price for i in tickers]
        last_trade_size = [i.last_trade.trade_size for i in tickers]
        last_trade_timestamp = [i.last_trade.trade_timestamp for i in tickers]
        last_trade_id = [i.last_trade.trade_id for i in tickers]

        
        last_quote_bid_price = [i.stock_last_quote.bid_price for i in tickers]
        last_quote_ask_price = [i.stock_last_quote.ask_price for i in tickers]
        last_quote_ask_size = [i.stock_last_quote.ask_size for i in tickers]
        last_quote_bid_size = [i.stock_last_quote.ask_size for i in tickers]
        last_quote_timestamp = [i.stock_last_quote.quote_timestamp for i in tickers]

        min_data_accumulated_volume = [i.stock_minute_bar.accumulated_volume for i in tickers]
        min_data_volume = [i.stock_minute_bar.volume for i in tickers]
        min_data_close = [i.stock_minute_bar.close for i in tickers]
        min_data_open = [i.stock_minute_bar.open for i in tickers]
        min_data_high = [i.stock_minute_bar.high for i in tickers]
        min_data_low = [i.stock_minute_bar.low for i in tickers]
        min_data_vwap = [i.stock_minute_bar.vwap for i in tickers]

        day_open = [i.stock_day.open for i in tickers]
        day_close = [i.stock_day.close for i in tickers]
        day_high = [i.stock_day.high for i in tickers]
        day_low = [i.prev_day.low for i in tickers]
        day_volume = [i.stock_day.volume for i in tickers]
        day_vwap = [i.stock_day.vwap for i in tickers]

        prev_day_open = [i.prev_day.open for i in tickers]
        prev_day_close = [i.prev_day.close for i in tickers]
        prev_day_high = [i.prev_day.high for i in tickers]
        prev_day_low = [i.prev_day.low for i in tickers]
        prev_day_volume = [i.prev_day.volume for i in tickers]
        prev_day_vwap = [i.prev_day.vwap for i in tickers]


        change_percent = [i.today_changep for i in tickers]
        change = [i.today_change for i in tickers]

        rows = zip(
            symbol, change_percent, change, day_open, day_close, day_high, day_low, day_volume, day_vwap, 
            last_trade_conditions, last_trade_exchange, last_trade_price, last_trade_size, last_trade_timestamp, last_trade_id,
            last_quote_bid_price, last_quote_ask_price, last_quote_ask_size, last_quote_bid_size, last_quote_timestamp,
            min_data_accumulated_volume, min_data_volume, min_data_close, min_data_open, min_data_high, min_data_low, min_data_vwap,
            prev_day_open, prev_day_close, prev_day_high, prev_day_low, prev_day_volume, prev_day_vwap
        )

        with open('files/stocks/all_snapshots.csv', 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            # Write the header
            csv_writer.writerow([
                'Symbol', 'Change Percent', 'Change', 'Day Open', 'Day Close', 'Day High', 'Day Low', 'Day Volume', 'Day VWAP', 'Last Trade Conditions', 'Last Trade Exchange', 'Last Trade Price', 'Last Trade Size', 'Last Trade Timestamp', 'Last Trade ID',
                'Last Quote Bid Price', 'Last Quote Ask Price', 'Last Quote Ask Size', 'Last Quote Bid Size', 'Last Quote Timestamp',
                'Minute Data Accumulated Volume', 'Minute Data Volume', 'Minute Data Close', 'Minute Data Open', 'Minute Data High', 'Minute Data Low', 'Minute Data VWAP',
                'Prev Day Open', 'Prev Day Close', 'Prev Day High', 'Prev Day Low', 'Prev Day Volume', 'Prev Day VWAP',
                
            ])
            # Write the rows
            csv_writer.writerows(rows)
    async def get_iv_percentile(self, symbol):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://data.nasdaq.com/api/v3/datasets/QOR/{symbol}/data.json?api_key={YOUR_NASDAQ_KEY}") as response:
                d = await response.json()
                dataset = d['dataset_data']
                data = dataset['data']
                column_names = dataset['column_names']
                Date = column_names[0]
                values = data[0]
                Date = values[0]
                ivper30 = round(values[8] * 100, ndigits=2)
                ivper60 = round(values[11]* 100, ndigits=2)
                ivper90 = round(values[14]* 100, ndigits=2)
                ivper360 = round(values[17]* 100, ndigits=2)
                self.ivperavg = round((ivper30 + ivper60 + ivper90 + ivper360) / 4, ndigits=4)

        return self.ivperavg



     
    async def format_timestamp(self, timestamp: datetime) -> str:
        """
        Formats a timestamp into a string representation.

        Args:
            timestamp (datetime): The timestamp to format.

        Returns:
            str: The formatted timestamp string.
        """
        return timestamp.strftime("%Y/%m/%d %I:%M %p")

    async def format_timestamps_list(self, timestamps: List[int]) -> List[str]:
        """
        Formats a list of timestamps (in milliseconds) into a list of formatted timestamp strings.

        Args:
            timestamps (List[int]): The list of timestamps (in milliseconds) to format.

        Returns:
            List[str]: The list of formatted timestamp strings.
        """
        formatted_timestamps = []
        for timestamp_ms in timestamps:
            timestamp = datetime.fromtimestamp(timestamp_ms / 1000)  # Convert milliseconds to seconds
            formatted_timestamp = await self.format_timestamp(timestamp)
            formatted_timestamps.append(formatted_timestamp)
        return formatted_timestamps         
    

    async def fetch_conditions(self, type: str) -> List[Condition]:
        url = f"https://api.polygon.io/v3/reference/conditions?asset_class=stocks&limit=1000&apiKey={self.api_key}"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    raise Exception(f"Failed to fetch conditions with status code {response.status}")
                json_data = await response.json()
                results = json_data['results']
        
        conditions = [Condition.from_json(result) for result in results]
        return conditions


    async def get_rsi(self, symbol, timestamp=None, timespan: str="hour", adjusted=True, window=14, series_type="close", expand_underlying=None, order="desc", limit:str = 10):
        """
        Get the relative strength index (RSI) for a ticker symbol over a given time range.

        :param ticker: The stock ticker symbol or options symbol. Use 'generate_option_symbol' to create the needed symbol.
        :param timestamp: Query by timestamp. Either a date with the format YYYY-MM-DD or a millisecond timestamp.
        :param timespan: The size of the aggregate time window.
        :param adjusted: Whether or not the aggregates used to calculate the RSI are adjusted for splits.
        :param window: The window size used to calculate the RSI.
        :param series_type: The price in the aggregate which will be used to calculate the RSI.
        :param expand_underlying: Whether or not to include the aggregates used to calculate this indicator in the response.
        :param order: The order in which to return the results, ordered by timestamp.
        :param limit: Limit the number of results returned, default is 10 and max is 5000.
        
        >>> Symbol prefixes:



            >>> crypto = X:

            >>> forex = C:

            >>> options = O:

            >>> indices = I:

            >>> stocks = None

        Returns: A list of RSI values.

        
        """
    async def get_rsi(self, symbol, timespan="hour", window=14, limit=1000):
        async def get_data(session, symbol):
            url = f"https://api.polygon.io/v1/indicators/rsi/{symbol}?timespan={timespan}&window={window}&limit={limit}&apiKey={self.api_key}"
        
            async with session.get(url) as response:
                data = await response.json()
                results = data.get('results')
            
                if results is not None:
                    values = results.get('values')
                    rsi = RSI(values)
                    if rsi is not None:
                        return rsi.rsi_value
                else:
                    return None

        async with aiohttp.ClientSession() as session:
            rsi = await get_data(session, symbol)
            return rsi



    async def financials(self, symbol, return_as_dataframe: bool=False):
        url=f"https://api.polygon.io/vX/reference/financials?ticker={symbol}&limit=100&apiKey={self.api_key}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                r = await resp.json()
                results = r['results']
                print(results)
                financials = [i['financials'] for i in results]
                balance_sheet = BalanceSheet(financials)
                comp_incomes = ComprehensiveIncome(financials)
                cash = CashFlow(financials)
                income = IncomeStatement(financials)

                data_names = [
                    'Assets', 'Current Assets', 'Current Liabilities', 
                    'Equity Attributable to Non-Controlling Interest', 
                    'Equity Attributable to Parent', 'Equity Value', 
                    'Assets Value', 'Liabilities and Equity', 'Liabilities', 
                    'Non-current Assets', 'Non-current Liabilities', 
                    'Other Thn Fixed Non-current Assets', 
                    'Exchange Gains and Losses', 'Net Cash Flow', 
                    'Net Cash Flow Continuing', 
                    'Net Cash Flow From Financing Continuing', 
                    'Net Cash Flow From Financing', 
                    'Net Cash Flow From Investing Continuing', 
                    'Net Cash Flow From Investing', 
                    'Net Cash Flow From Operating Continuing', 
                    'Net Cash Flow From Operating', 
                    'Comprehensive Income Loss Attributable to Non-controlling Interest',
                    'Comprehensive Income Loss Attributable to Parent', 
                    'Comprehensive Income Loss', 'Other Comprehensive Income Loss', 
                    'Basic Earnings Per Share', 'Diluted Earnings Per Share', 
                    'Benefits Costs and Expenses', 'Cost of Revenue', 
                    'Cost and Expenses', 'Gross Profit Value', 
                    'Income Loss From Continuing Operations After Tax',
                    'Income Loss From Continuing Operations Before Tax', 
                    'Income Loss From  Discontinued Operations Net of Tax', 
                    'Income Tax Expense Benefit - Current', 
                    'Income Tax Epense Benefit - Deferred', 
                    'Interest Income Expense After Provision For Losses',
                    'Interest Income Expense Operating - Net', 
                    'Net Income Loss Attributable to Non-controlling Interest', 
                    'Net Income Loss Attributable to Parent', 'Net Income Loss', 
                    'Operating Expenses', 'Operating Income Loss', 
                    'Participating Securities Distributed and Undistributed Earnings Loss - Basic', 
                    'Preferred Stock Dividends and Other Adjustments', 
                    'Provision for Loan Lease and Other Losses', 'Revenues']

                data_values = [
                    balance_sheet.assets_value,
                    balance_sheet.current_assets_value,
                    balance_sheet.current_liabilities_value,
                    balance_sheet.equity_attributable_to_noncontrolling_interest_value,
                    balance_sheet.equity_attributable_to_parent_value,
                    balance_sheet.equity_value,
                    balance_sheet.fixed_assets_value,
                    balance_sheet.liabilities_and_equity_value,
                    balance_sheet.liabilities_value,
                    balance_sheet.noncurrent_assets_value,
                    balance_sheet.noncurrent_liabilities_value,
                    balance_sheet.other_than_fixed_noncurrent_assets_value,
                    cash.exchange_gains_losses_value,
                    cash.net_cash_flow,
                    cash.net_cash_flow_continuing_value,
                    cash.net_cash_flow_from_financing_activities_continuing_value,
                    cash.net_cash_flow_from_financing_activities_value,
                    cash.net_cash_flow_from_investing_activities_continuing_value,
                    cash.net_cash_flow_from_investing_activities_value,
                    cash.net_cash_flow_from_operating_activities_continuing_value,
                    cash.net_cash_flow_from_operating_activities_value,
                    comp_incomes.comprehensive_income_loss_attributable_to_noncontrolling_interest_value,
                    comp_incomes.comprehensive_income_loss_attributable_to_parent_value,
                    comp_incomes.comprehensive_income_loss_value,
                    comp_incomes.other_comprehensive_income_loss_value,
                    income.basic_earnings_per_share_value,
                    income.diluted_earnings_per_share_value,
                    income.benefits_costs_expenses_value,
                    income.cost_of_revenue_value,
                    income.costs_and_expenses_value,
                    income.gross_profit_value,
                    income.income_loss_from_continuing_operations_after_tax_value,
                    income.income_loss_from_continuing_operations_before_tax_value,
                    income.income_loss_from_discontinued_operations_net_of_tax_value,
                    income.income_tax_expense_benefit_current_value,
                    income.income_tax_expense_benefit_deferred_value,
                    income.interest_income_expense_after_provision_for_losses_value,
                    income.interest_income_expense_operating_net_value,
                    income.net_income_loss_attributable_to_noncontrolling_interest_value,
                    income.net_income_loss_attributable_to_parent_value,
                    income.net_income_loss_value,
                    income.operating_expenses_value,
                    income.operating_income_loss_value,
                    income.participating_securities_distributed_and_undistributed_earnings_loss_basic_value,
                    income.preferred_stock_dividends_and_other_adjustments_value,
                    income.provision_for_loan_lease_and_other_losses_value,
                    income.revenues_value
                ]

                # create an empty DataFrame
                df = pd.DataFrame()

                # add columns to the DataFrame one by one
                for name, values in zip(data_names, data_values):
                    df[name] = pd.Series(values)

                df = df.replace({None: np.nan}).dropna()

                if not return_as_dataframe:
                    df = df.to_dict('records')

                return df


    async def get_bollinger_bands(self, symbol, multiplier, timespan, from_date, to_date, window=20, num_std_dev=2):
        aggregates_data = await self.get_aggregates(symbol, multiplier, timespan, from_date, to_date, limit=1000)
        if not aggregates_data:
            return [], [], []

        closing_prices = aggregates_data.close
        upper_band = []
        middle_band = []
        lower_band = []

        if len(closing_prices) < window:
            print(f'Not enough data to calculate Bollinger Bands for window size {window}')
            return [], [], []

        for i in range(window - 1, len(closing_prices)):
            window_prices = closing_prices[i - window + 1: i + 1]

            # Calculate the middle band (SMA)
            avg = np.mean(window_prices)

            # Calculate the standard deviation
            std_dev = np.std(window_prices, ddof=1)  # Use sample standard deviation

            # Calculate the upper and lower bands
            upper = avg + (num_std_dev * std_dev)
            lower = avg - (num_std_dev * std_dev)

            upper_band.append(upper)
            middle_band.append(avg)
            lower_band.append(lower)

        return upper_band, middle_band, lower_band


    def get_polygon_logo_sync(symbol):
        data = session().get(f"https://api.polygon.io/v3/reference/tickers/{symbol}?apiKey={YOUR_API_KEY}")
                
        if 'results' not in data:
            # No results found
            return None
        
        results = data['results']
        branding = results.get('branding')

        if branding and 'icon_url' in branding:
            encoded_url = branding['icon_url']
            decoded_url = unquote(encoded_url)
            url_with_api_key = f"{decoded_url}?apiKey={YOUR_API_KEY}"
            return url_with_api_key



    async def get_rate_of_change_and_rocma(self, symbol, multiplier, timespan, from_date, to_date, window: int=12, rocma_window: int=5):
        aggregates_data = await self.get_aggregates(symbol, multiplier, timespan, from_date, to_date)

        closing_prices = aggregates_data.close
        roc_values = []
        rocma_values = []

        for i in range(window, len(closing_prices)):
            roc = ((closing_prices[i] - closing_prices[i - window]) / closing_prices[i - window]) * 100
            roc_values.append(roc)

        for i in range(rocma_window - 1, len(roc_values)):
            rocma = np.mean(roc_values[i - rocma_window + 1:i + 1])
            rocma_values.append(rocma)

        return roc_values, rocma_values



    async def get_price(self, ticker=str):
        ticker = ticker if ticker not in indices_list else f"I:{ticker}"
        url = f"https://api.polygon.io/v3/snapshot?ticker.any_of={ticker}&apiKey={self.api_key}"
        print(url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                try:
                    data = await resp.json()
                    results = data['results'] if 'results' in data else None
                    if results is not None:
                        value = results[0]['session']['close'] if 'session' in results else results[0]['value']
                        if value is not None:
                            return value
                except KeyError:
                    pass  # Handle the KeyError and continue with the next ticker

        return None  # Return None if the stock price couldn't be retrieved

            


    async def find_lowest_iv(self, output):
        final_dicts_call = []
        final_dicts_put = []

        async with aiohttp.ClientSession() as session:
            for url in output:
                async with session.get(url) as filtered_resp:
                    if filtered_resp.status != 200:
                        print(f"Error")
                        continue
                    else:
                        response = await filtered_resp.json()

                        if response is None:
                            print(f"Bad output: {output}")
                            continue

                        filtered_results = response['results'] if 'results' in response else None
                        if filtered_results is not None:
                            call_data = []
                            put_data = []
                            for result in filtered_results:
                                contract_type = result.get('details').get('contract_type')
                                if contract_type == 'call':
                                    call_data.append(result)
                                elif contract_type == 'put':
                                    put_data.append(result)
                                else:
                                    continue

                            call_symbols = [i.get('ticker', None) for i in call_data]
                            call_ivs = [i.get('implied_volatility', None) for i in call_data]
                            call_strikes = [i.get('details').get('strike_price', None) for i in call_data]
                            call_expiry = [i.get('details').get('expiration_date', None) for i in call_data]
                            call_name = [i.get('name', None) for i in call_data]
                            put_symbols = [i.get('ticker', None) for i in put_data]
                            put_ivs = [i.get('implied_volatility', None) for i in put_data]
                            put_strikes = [i.get('details').get('strike_price', None) for i in put_data]
                            put_expiry = [i.get('details').get('expiration_date', None) for i in put_data]
                            put_name = [i.get('name', None) for i in put_data]


                            call_volume = [i.get('session').get('volume', None) for i in call_data]
                            put_volume = [i.get('session').get('volume', None) for i in put_data]

                            call_dict = {
                                'Symbol': call_symbols,
                                'Name': call_name,
                                'Strike': call_strikes,
                                'Expiry': call_expiry,
                                'IV': call_ivs,
                                'Volume': call_volume,
                            }

                            put_dict = {
                                'Symbol': put_symbols,
                                'Name': put_name,
                                'Strike': put_strikes,
                                'Expiry': put_expiry,
                                'IV': put_ivs,
                                'Volume': put_volume
                            }

                            call_df = pd.DataFrame(call_dict).sort_values('IV').dropna(how="any")
                            put_df = pd.DataFrame(put_dict).sort_values('IV').dropna(how="any")
                            call_df.to_csv('iv_monitor_calls.csv', index=False)
                            put_df.to_csv('iv_monitor_puts.csv', index=False)

                            def get_lowest_iv(group):
                                return group.sort_values('IV').iloc[0]

                            grouped_call_df = call_df.groupby('Expiry').apply(get_lowest_iv)
                            grouped_put_df = put_df.groupby('Expiry').apply(get_lowest_iv)

                            for index, row in grouped_call_df.iterrows():
                                current_dict = {
                                    'symbol': row['Symbol'],
                                    'name': row['Name'],
                                    'strike': row['Strike'],
                                    'expiry': index,  # level 0 index is 'Expiry'
                                    'iv': row['IV'],
                                    'volume': row['Volume']
                                }
                                final_dicts_call.append(current_dict)

                            for index, row in grouped_put_df.iterrows():
                                current_dict = {
                                    'symbol': row['Symbol'],
                                    'name': row['Name'],
                                    'strike': row['Strike'],
                                    'expiry': index,  # level 0 index is 'Expiry'
                                    'iv': row['IV'],
                                    'volume': row['Volume']
                                }
                                final_dicts_put.append(current_dict)

        return final_dicts_call, final_dicts_put
    
    async def __aexit__(self, exc_type, exc, tb):
        print("Closing session")
        await self.session.__aexit__(exc_type, exc, tb)


