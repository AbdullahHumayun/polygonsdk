import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
import pandas as pd
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY
polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)


async def get_forex_data():

    forex_snapshots = await polygonsdk.get_all_forex_snapshots()
    df = pd.DataFrame(vars(forex_snapshots))
    df.to_csv('files/forex/all_forex_snapshots.csv')


    print(f"Data has been successfully saved to files/forex/all_forex_snapshots.csv")



asyncio.run(get_forex_data())
