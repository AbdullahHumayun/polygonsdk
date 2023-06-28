
import aiohttp
from api_master.sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK

from collections import defaultdict
from api_master.sdks.polygon_sdk.universal_snapshot import UniversalOptionSnapshot,UniversalSnapshot
import asyncio
import pandas as pd
from api_master.sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
import numpy as np
from tabulate import tabulate
from api_master.cfg import YOUR_API_KEY, today_str, thirty_days_from_now_str, two_years_from_now_str
opts = PolygonOptionsSDK(YOUR_API_KEY)
poly = AsyncPolygonSDK(YOUR_API_KEY)

async def main():
    atm_calls, atm_puts = await opts.get_near_the_money_options("GME")


                            # Rename volume column for clarity
    filtered_calls = atm_calls.rename(columns={'vol': 'call_volume'})
    filtered_puts = atm_puts.rename(columns={'vol': 'put_volume'})

asyncio.run(main())