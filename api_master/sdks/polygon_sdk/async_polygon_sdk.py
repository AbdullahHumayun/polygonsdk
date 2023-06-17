import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


import httpx
from typing import List, Union, Tuple, Optional
from urllib.parse import urlencode, unquote
import pandas as pd
from .indices_snapshot import Indices,IndicesData
from .company_info import CompanyInfo
from .forex_crypto import ForexSnapshot, CryptoSnapshot
from .technicals.rsi import RSI
from .technicals.macd import MACDData
from .financials import BalanceSheet,IncomeStatement,ComprehensiveIncome,CashFlow
from .technicals.sma import SimpleMovingAverage
from .technicals.ema import ExponentialMovingAverage
import csv
from cfg import YOUR_API_KEY
from .news import News
from datetime import datetime, timedelta
from .snapshot import StockSnapshot
import numpy as np
from scipy.signal import argrelextrema
from typing import List, Dict, Any
from .models import Dividend, Condition
from .pivot_points import PivotPointData
from cfg import YOUR_NASDAQ_KEY
import requests
from .aggregates import AggregatesData
from .quote import Quote
import aiohttp
from datetime import datetime, timedelta
from _discord.embeddings import Data

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
        await self.session.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        print("Closing session")
        await self.session.__aexit__(exc_type, exc, tb)
    async def initialize(self):
        self.conditions_map = await self.get_stock_conditions()


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

    async def get_all_indices(self) -> pd.DataFrame:
        """Returns all up-to-date indices data in the form of a dataframe."""
        url = f"https://api.polygon.io/v3/snapshot/indices?apiKey={self.api_key}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                r = await resp.json()
                results = r['results']
                name = Indices(results)
                session = IndicesData(results)
                data = { 
                    'ticker': name.ticker,
                    'Name': name.name,
                    'Dollar Change':session.change,
                    'Change Percent':session.change_percent,
                    'Close':session.close,
                    'High':session.high,
                    'Open':session.open,
                    'Low':session.low,
                    'Previous Close':session.previous_close
                }
                df = pd.DataFrame(data)
                df.to_csv('files/indices/indices_data.csv')

                return df
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
        snapshot_endpoint = f"/v2/snapshot/locale/us/markets/stocks/tickers/{ticker}"
        snapshot_data = await self._request(snapshot_endpoint)
        results = snapshot_data['ticker']
        if snapshot_data is None:
            return None

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
    async def ticker_news(self, keyword_hooks):
        sent_articles = set()
        while True:
            endpoint = "/v2/reference/news"
            response = await self._request(endpoint)

            if not response or "results" not in response:
                continue

            results = response['results']
            publisher = [i['publisher'] if 'publisher' in i and i['publisher'] else 'N/A' for i in results]
            home_url = [i['homepage_url'] if 'homepage_url' in i and i['homepage_url'] else 'N/A' for i in publisher]
            icon_url = [i['logo_url'] if 'logo_url' in i and i['logo_url'] else 'N/A' for i in publisher]
            name = [i['name'] if 'name' in i and i['name'] else "N/A" for i in results]
            title = [i['title'] if 'title' in i and i['title'] else 'N/A' for i in results]
            author = [i['author'] if 'author' in i and i['author'] else 'N/A' for i in results]
            article_url = [i['article_url'] if 'article_url' in i and i['article_url'] else 'N/A' for i in results]
            tickers = [i['ticker'] if 'ticker' in i and i['ticker'] else 'N/A' for i in results]
            amp_url = [i['amp_url'] if 'amp_url' in i and i['amp_url'] else 'N/A' for i in results]
            image_url = [i['image_url'] if 'image_url' in i and i['image_url'] else 'N/A' for i in results]
            description = [i['description'] if 'description' in i and i['description'] else 'N/A' for i in results]
            keywords = [i['keywords'] if 'keywords' in i and i['keywords'] else 'N/A' for i in results]

            for article_index, article_url in enumerate(article_url):
                if article_url in sent_articles:
                    continue

                article_keywords = keywords[article_index]
                sent_webhook = False

                for keyword, webhook_url in keyword_hooks.items():
                    if keyword in article_keywords:
                        await Data().make_news_embed(webhook_url, image_url[article_index], title[article_index], description[article_index], name[article_index], icon_url[article_index], article_url, tickers[article_index], home_url[article_index], article_keywords, author[article_index])
                        sent_articles.add(article_url)
                        sent_webhook = True
                        print(f"New article processed: {title[article_index]} {keywords}")


                if not sent_webhook:
                    continue


    async def get_stock_conditions(self, conditions) -> Dict[int, str]:
        """
        Get stock conditions data from the Polygon.io API.

        :return: A dictionary with condition IDs as keys and condition names as values.
        """
        url = f"https://api.polygon.io/v3/reference/conditions?asset_class=stocks&limit=1000&apiKey={self.api_key}"
        stock_conditions = {}

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    conditions_data = data['results']

                    for condition in conditions_data:
                        condition_id = condition['id']
                        condition_name = condition['name']
                        stock_conditions[condition_id] = condition_name
                else:
                    print(f"Error: {response.status}")

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
    
    async def get_aggregates(self, ticker, multiplier, timespan, from_date, to_date, order="asc", limit=50):
        """
        Retrieve aggregate data for a given stock ticker.

        :param stock_ticker: The stock ticker symbol as a string.
        :param multiplier: The multiplier for the timespan as an integer.
        :param timespan: The timespan as a string (e.g., "minute", "hour", "day", "week", "month", "quarter", "year").
        :param from_date: The start date for the data as a string in YYYY-MM-DD format.
        :param to_date: The end date for the data as a string in YYYY-MM-DD format.
        :return: An instance of AggregatesData containing the aggregate data.
        """
        url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/{multiplier}/{timespan}/{from_date}/{to_date}?adjusted=true&sort={order}&limit={limit}&apiKey={YOUR_API_KEY}"

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
                results = data['results']
                return(CompanyInfo(results))

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

        except (KeyError, TypeError) as e:
            print(f"KeyError in get_macd: {e}. The requested key is not available in the response.")
            return None

        return macd, signal, histogram

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

    async def get_ticker_narrative(self, ticker, limit=10):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.polygon.io/v2/reference/news?ticker={ticker}&limit={limit}&sort=published_utc&apiKey={self.api_key}") as response:
                data = await response.json()

                results = data['results']
                news_narrative = [News(i) for i in results if i is not None]
                return news_narrative

     
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
        url=f"https://api.polygon.io/v1/indicators/rsi/{symbol}?timespan={timespan}&adjusted={adjusted}&window={window}&series_type=close&order={order}&limit={limit}&apiKey={self.api_key}"
        async with aiohttp.ClientSession() as session:
            print(url)
            async with session.get(url) as response:
                data = await response.json()
                results = data['results']
                values = results['values']
                rsi = RSI(values)
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
