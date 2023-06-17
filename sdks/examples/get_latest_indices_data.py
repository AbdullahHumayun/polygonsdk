import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY
polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)


async def get_all_indices_data():

    await polygonsdk.get_all_indices()


    print(f"Data has been successfully saved to files/indices/indices_data.csv")

asyncio.run(get_all_indices_data())