from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
import asyncio
from cfg import YOUR_API_KEY
import pandas as pd
poly = AsyncPolygonSDK(YOUR_API_KEY)
import aiohttp
async def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "Accept-Encoding": "gzip, deflate",

    }

    ticker = "AAPL"
    cik = await poly.get_cik(ticker)
    
    async with aiohttp.ClientSession() as session:
        url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                print(data)
                entity_public_float = data['facts']['dei']["EntityPublicFloat"]
                float_units = entity_public_float['units']
                USD = float_units['USD']

                df = pd.DataFrame(USD)
                print(df)


                
asyncio.run(main())
