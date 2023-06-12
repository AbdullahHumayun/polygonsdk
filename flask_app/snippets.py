snippets = {
    "Bollinger Bands": {
        "code": """
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

import asyncio

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY, today_str

poly = AsyncPolygonSDK(YOUR_API_KEY)
ticker = "NVDA"

async def main():

    x = await poly.get_bollinger_bands(symbol="GME",multiplier=1, timespan="hour", from_date="2023-04-01", to_date=today_str, window=20, num_std_dev=2)
    for i in x:
        print(i)

asyncio.run(main())
""",
    },
    "Get all Stock Snapshots": {
        "code": """
import asyncio
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY

polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)

filename="files/stocks/all_snapshots.csv"

async def get_all_ticker_data():
    \"\"\"Gets all snapshots market-wide and saves
    to CSV for further analysis / testing purposes.\"\"\"

    await polygonsdk.write_snapshots_to_csv()

    print(f"Data has been successfully saved to files/stocks/all_snapshots.csv.")
asyncio.run(get_all_ticker_data())
""",
    },
}