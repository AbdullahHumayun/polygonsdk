import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import asyncio
import pandas as pd

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY, today_str

poly = AsyncPolygonSDK(YOUR_API_KEY)
ticker = "MSFT"

async def main():

    roc = await poly.get_rate_of_change_and_rocma(ticker, "day", 1, from_date="2023-04-01", to_date=today_str, window=10)
    print(roc)

asyncio.run(main())