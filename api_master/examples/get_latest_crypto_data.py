import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import asyncio
import pandas as pd
from ..sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY
polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)


async def get_all_crypto_data():

    crypto_snapshots = await polygonsdk.get_all_crypto_snapshots()
    df = pd.DataFrame(vars(crypto_snapshots))
    df.to_csv('files/crypto/all_crypto_snapshots.csv')

    print(f"Data has been successfully saved to files/crypto/all_crypto_snapshots.csv")


asyncio.run(get_all_crypto_data())
