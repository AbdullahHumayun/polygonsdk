import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


import asyncio
from sdks.polygon_sdk.option_snapshot import OptionSnapshotData
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
import json
from cfg import YOUR_API_KEY, today_str,seven_days_from_now_str
from urllib.parse import urlencode
import aiohttp
import pandas as pd
from datetime import datetime, timedelta

poly = AsyncPolygonSDK(YOUR_API_KEY)

class ConcurrentModel:
    def __init__(self):
        self.base_url = "https://api.polygon.io"
        self.api_key = f"{YOUR_API_KEY}"

    async def _request_all_pages_concurrently(self, session, initial_url, params=None, api_key=YOUR_API_KEY):
        if params is None:
            params = {}
        params["apiKey"] = api_key
        print(initial_url)
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

    async def option_chain_generator(self, underlying_asset, strike_price=None, expiration_date=None, contract_type=None, order=None, limit=250, sort=None):
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

        async for response_data in self._request_all_pages_generator(endpoint, params=params):
            for item in response_data:
                print(item)
                yield OptionSnapshotData(item)

   

    async def _request_all_pages_generator(self, endpoint, params=None):
        page = 1
        params = params or {}
        params["page"] = page

        while True:
            try:
                response_data = await self._request(endpoint, params=params)
                if response_data:
                    results = response_data['results']
                    if results is not None:
                        yield response_data
                    else:
                        continue

                # Check if there are more pages
                if "page" in response_data and "total_pages" in response_data:
                    page += 1
                    if page > response_data["total_pages"]:
                        break
                    params["page"] = page
                else:
                    break
            except json.JSONDecodeError:
                continue

    async def _request(self, endpoint, params=None):
        # Perform the actual HTTP request asynchronously
        # Implement your HTTP request logic here
        await asyncio.sleep(1)  # Simulating the asynchronous HTTP request delay
        response_data = {"page": 1, "total_pages": 3}  # Simulated response data
        print(response_data)
        return response_data

    async def get_option_data(self, ticker, price, session):
        today_str = datetime.now().strftime('%Y-%m-%d')
        seven_days_from_now_str = (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")

        base_url = "https://api.polygon.io/v3/snapshot/options/"
        price = await poly.get_stock_price(ticker)
        if price is not None:
            lower_strike = round(price * 0.97)
            upper_strike = round(price * 1.03)
            
            endpoint = f"{base_url}{ticker}"
            params = {
                "strike_price.gte": lower_strike,
                "strike_price.lte": upper_strike,
                "expiration_date.gte": today_str,
                "expiration_date.lte": seven_days_from_now_str,
                "limit": 250,
                "apiKey": YOUR_API_KEY
            }
            response_data = await self._request_all_pages_concurrently(session, endpoint, params=params, api_key=YOUR_API_KEY)
            response_data = json.loads(response_data)  # Convert the response data to a dictionary

            option_data = OptionSnapshotData(response_data)


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
                        expiry = expiry[5:]
                        skew = "🔥" if strike <= underlying_price else "🟢"
                        skew_metric = strike - underlying_price
                        if skew_metric < -5.5 or skew_metric > 5.5:
                            return [symbol, strike, underlying_price, expiry, iv, skew, skew_metric]
            return None

async def main():
    model = ConcurrentModel()
    async with aiohttp.ClientSession() as session:
        async for data in model.option_chain_generator("AAPL"):
            result = await model.get_option_data(data.ask, data.price, session)
            if result is not None:
                print(result)

# Run the main asynchronous function
asyncio.run(main())