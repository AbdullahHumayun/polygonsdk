import requests
import aiohttp
import httpx
import asyncio



from urllib.parse import urlencode
from discord_webhook import AsyncDiscordWebhook

from typing import Optional, List, Any, Union
from models.poly.crypto_snapshot import CryptoSnapshotResult
from models.poly.option_snapshot import OptionsSnapshotResult
from models.poly.indices_snapshot import IndicesSnapshotResult
from models.poly.ema import EMAResponse
from models.poly.sma import SMAResults
from models.poly.aggregates import AggregateResult, AggregateResponse
from models.poly.quotes_NBBO import QuotesNBBO,QuotesNBBOItem
from models.poly.rsi import RSIResults
from models.poly.ticker_snapshot import TickerSnapshotResults
from models.poly.universal_snapshot import UniversalSnapshotResult
from models.weballs.top_tickers import TopTickers
from models.weballs.top_options import WebullTopOptions

from api_master.cfg import YOUR_API_KEY, fifteen_days_from_now_str, today_str, thirty_days_ago_str, thirty_days_from_now_str


class MasterControl:
    def __init__(self):
        self.api_endpoints = {
            'Polygon': 'https://api.polygon.io',
            # Add more APIs as needed
        }
        self.polygon_api_key = YOUR_API_KEY


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
    
    async def nbbo_quotes(self, ticker: str, limit: str = "100", order: str = "desc"):
        async with aiohttp.ClientSession() as session:
            url = f"https://api.polygon.io/v3/quotes/{ticker}?limit={limit}&order={order}&apiKey={YOUR_API_KEY}"
            async with session.get(url) as resp:
                data = await resp.json()
                quotes_nbbo = QuotesNBBO.from_dict(data)
                return quotes_nbbo


    async def get_index_price(self, ticker=str):
        """Fetch the price of an index ticker"""
        url = f"https://api.polygon.io/v3/snapshot?ticker.any_of=I:{ticker}&apiKey={YOUR_API_KEY}"
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
        url = f"https://api.polygon.io/v3/snapshot?ticker.any_of={ticker}&apiKey={YOUR_API_KEY}"
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
    


    async def get_near_the_money_single(self, ticker: str, threshold: float):
        if ticker is not None:
            if ticker.startswith("SPX"):
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
                            results = UniversalSnapshotResult(results)
                            tickers = results.ticker
                            atm_tickers = ','.join(tickers)
                            return atm_tickers
            else:
                return None
        return None


    async def fetch_async(self, api_name, endpoint, params=None):
        """Fetch data from an API asynchronously."""
        if api_name not in self.api_endpoints:
            raise ValueError(f'Unknown API: {api_name}')

        url = self.api_endpoints[api_name] + endpoint

        if api_name == 'Polygon':
            if params is None:
                params = {}
            params['apiKey'] = self.polygon_api_key

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as resp:
                return await resp.json()

    async def fetch_data(ticker: str, multiplier:str=1, timespan:str="day", start_date:str=thirty_days_ago_str, end_date:str=today_str, limit:str=1000):
        async with httpx.AsyncClient() as client:
            url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/{multiplier}/{timespan}/{start_date}/{end_date}?adjusted=true&sort=asc&limit={limit}&otc=true&apiKey={YOUR_API_KEY}"
            resp = await client.get(url)
            resp.raise_for_status()
            data = resp.json()

            # Assuming the `results` field in response data is an array of objects
            results = [AggregateResult(**item) for item in data.get('results', [])]
            
            return AggregateResponse(results)
    
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


    async def fetch_sma_data(self, ticker: str, timespan: str= "day", window:str = 14) -> Optional[SMAResults]:
        async with aiohttp.ClientSession() as session:
            url = f"https://api.polygon.io/v1/indicators/ema/{ticker}?timespan={timespan}&adjusted=true&window={window}&series_type=close&order=desc&apiKey={YOUR_API_KEY}"
            async with session.get(url) as response:
                if response.status == 200:
                    data_dict = await response.json()
                    return SMAResults.from_dict(data_dict)
                else:
                    print(f"Error fetching SMA data. Status code: {response.status}")
        return None



    async def fetch_webull_top_options_async(self, rank_type: str):
        """Fetch the top options from Webull API.
        
        >>> posDecrease
        >>> posIncrease
        >>> impVol
        >>> turnover
        >>> volume
        >>> position
        
        """
        url = f"https://quotes-gw.webullfintech.com/api/wlas/option/rank/list?regionId=6&rankType={rank_type}&pageIndex=1&pageSize=350"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.json()
                if 'data' in data:
                    return [WebullTopOptions.from_dict(item) for item in data['data']]
                else:
                    return None
                
    async def fetch_ema_pair(self, ticker:str, window1:str=9, window2:str=21, timespan:str="hour", order:str="desc", limit:str="1000"):
        """
        Fetches the EMA value for two windows. 
        Timespan options:

        >>> minute
        >>> hour
        >>> day
        >>> week
        >>> month
        >>> quarter
        >>> year

        Order Options:

        >>> asc (ascending)
        >>> desc (descending - default)
    
        """
        urls = [f"https://api.polygon.io/v1/indicators/ema/{ticker}?timespan={timespan}&adjusted=true&window={window1}&series_type=close&order={order}&limit={limit}&apiKey={YOUR_API_KEY}",
                f"https://api.polygon.io/v1/indicators/ema/{ticker}?timespan={timespan}&adjusted=true&window={window2}&series_type=close&order={order}&limit={limit}&apiKey={YOUR_API_KEY}"]
        for url in urls:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    data = await resp.json()
                    return EMAResponse.from_dict(data) 
    async def fetch_rsi(self, ticker: str, window:str=14, limit:str=1000) -> RSIResults:
        url = f"https://api.polygon.io/v1/indicators/rsi/{ticker}?timespan=day&adjusted=true&window={window}&series_type=close&order=desc&limit={limit}&apiKey={YOUR_API_KEY}"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                
                data = await resp.json()
    
                return RSIResults.from_dict(data)               

    async def get_top_traded_contracts(self, rank_type: str):
        """Fetch the top options from Webull API.
        
        >>> totalPosition
        >>> totalVolume
        
        """
        
        url = f"https://quotes-gw.webullfintech.com/api/wlas/option/rank/list?regionId=6&rankType={rank_type}&pageIndex=1&pageSize=350"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.json()
                if 'data' in data:
                    option_data = [TopTickers.from_dict(item) for item in data['data']]
                    return option_data
                else:
                    return None


    async def get_top_traded_options(self):
        rank_types = ["posDecrease", "posIncrease", "volume", "position", "turnover"]
        all_unique_symbols = []  # List to store all unique tickers
        all_unique_undersymbols = []
        for type in rank_types:
            posDecrease = await self.fetch_webull_top_options_async(rank_type=type)
            symbols = [i.derivative.symbol for i in posDecrease]
            underSym = [i.belongTicker.symbol for i in posDecrease]
            
            unique_symbols = list(set(symbols))  # Remove duplicates
            unique_underSym = list(set(underSym))
            all_unique_symbols.extend(unique_symbols)  # Add unique tickers to the list
            all_unique_undersymbols.extend(unique_underSym)
            print(unique_underSym)
            


        return all_unique_undersymbols



    async def get_top_traded_option_symbols(self):
        rank_types = ["posDecrease", "posIncrease", "volume", "position", "turnover"]
        all_unique_symbols = []  # List to store all unique tickers
        all_unique_undersymbols = []
        for type in rank_types:
            posDecrease = await self.fetch_webull_top_options_async(rank_type=type)
            symbols = [i.derivative.symbol for i in posDecrease]
            underSym = [i.belongTicker.symbol for i in posDecrease]
            
            unique_symbols = list(set(symbols))  # Remove duplicates
            unique_underSym = list(set(underSym))
            all_unique_symbols.extend(unique_symbols)  # Add unique tickers to the list
            all_unique_undersymbols.extend(unique_underSym)
            print(unique_underSym)
            


        return all_unique_symbols


    async def get_near_the_money_single(self, ticker: str, threshold: float):
        if ticker is not None:
            if ticker.startswith("SPX"):
                price_data = await self.get_index_price(ticker)
                
            else:
                price_data = await self.get_stock_price(ticker)
                price = price_data
            if price is not None:
                lower_strike = round(price * (1 - threshold/100), 2)
                upper_strike = round(price * (1 + threshold/100), 2)

                async with aiohttp.ClientSession() as session:
                    url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.lte={upper_strike}&strike_price.gte={lower_strike}&expiration_date.lte={fifteen_days_from_now_str}&expiration_date.gt={today_str}&limit=250&apiKey={YOUR_API_KEY}"
                    async with session.get(url) as resp:
                        r = await resp.json()
                        results = r['results']
                        if results is not None:
                            results = UniversalSnapshotResult(results)
                            tickers = results.ticker
                            atm_tickers = ','.join(tickers)
                            return atm_tickers
            else:
                return None
        return None
    




    async def send_to_discord(snapshot_result: UniversalSnapshotResult, discord_webhook_url):
        if discord_webhook_url is not None and snapshot_result is not None:
            # First, convert the snapshot result to a Discord embed
            embed = snapshot_result.to_unusual_embed()

            # Create a Discord webhook with the provided URL
            webhook = AsyncDiscordWebhook(url=discord_webhook_url, embeds=[embed])

            # Execute the webhook to send the embed to Discord
            if embed is not None:
                await webhook.execute()

