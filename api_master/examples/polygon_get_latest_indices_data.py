import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
import pandas as pd
from sdks.polygon_sdk.indices_snapshot import IndicesData
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY
polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)


async def get_all_indices_data():

    indices = await polygonsdk.get_all_indices()
    df = pd.DataFrame(indices.data_dict)

    df.to_csv('files/indices/all_indices_data.csv', index=False)



async def get_top_indices():

    indices = await polygonsdk.get_all_indices()
    df = pd.DataFrame(indices.data_dict)

    # Sort the DataFrame by 'change_percent' in descending order and get the top 50
    top_gainers = df.sort_values('change_percent', ascending=False).head(50)
    top_gainers['type'] = 'gainer'

    # Sort the DataFrame by 'change_percent' in ascending order and get the top 50
    top_losers = df.sort_values('change_percent', ascending=True).head(50)
    top_losers['type'] = 'loser'

    # Concatenate the two DataFrames
    top_indices = pd.concat([top_gainers, top_losers])

    # Save the top indices to a CSV file
    top_indices.to_csv('files/indices/top_indices.csv', index=False)

asyncio.run(get_all_indices_data())