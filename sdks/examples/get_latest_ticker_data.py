import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

import asyncio
import csv
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY
import pandas as pd
polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)


filename="files/stocks/all_snapshots.csv"

async def get_all_ticker_data():
    """Gets all snapshots market-wide and saves
    to CSV for further analysis / testing purposes."""

    await polygonsdk.write_snapshots_to_csv()

    print(f"Data has been successfully saved to files/stocks/all_snapshots.csv.")
asyncio.run(get_all_ticker_data())

