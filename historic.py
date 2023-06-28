import requests
from api_master.cfg import YOUR_API_KEY, today_str, fifteen_days_from_now_str
import asyncio
from api_master.sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from api_master.sdks.polygon_sdk.universal_snapshot import UniversalOptionSnapshot,UniversalSnapshot, CallsOrPuts
from api_master.sdks.helpers.helpers import chunk_list
polygon = AsyncPolygonSDK(YOUR_API_KEY)
import aiohttp

expired = False
ticker = "SPX"
type="put"
order="desc"


async def get_expired_contracts():
    async with aiohttp.ClientSession() as session:
        initial_url=f"https://api.polygon.io/v3/reference/options/contracts?underlying_ticker={ticker}&expiration_date.gt={today_str}&expiration_date.lte={fifteen_days_from_now_str}&contract_type={type}&expired={expired}&order=desc&limit=250&apiKey={YOUR_API_KEY}"
        async with session.get(initial_url) as resp:
            results = await polygon._request_all_pages(initial_url)
            if results is not None:
                print(results)

                option_data = CallsOrPuts(results)


                
                # Assuming option_data.ticker gives a list of tickers

                symbols_list = option_data.ticker
                print(symbols_list)
                chunks = list(chunk_list(symbols_list, 250))
                print(chunks)
                # Create a dictionary to hold results grouped by expiration date

                for chunk in chunks:
                    # Use chunk for API request
                    # Each chunk will contain max 250 items
                    chunk = str(chunk).replace("'","").replace(']','').replace('[','').replace(' ','')
                    async with session.get(f"https://api.polygon.io/v3/snapshot?ticker.any_of={chunk}&apiKey={YOUR_API_KEY}") as response:
                        near_money = await response.json(content_type=None)
                        near_money_results = near_money['results']
                        print(near_money_results)


asyncio.run(get_expired_contracts())




