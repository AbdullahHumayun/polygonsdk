"""WARNING DON'T RUN THIS FILE WITH FREE-TIER OR YOU'LL USE UP YOUR API CREDITS INSTANTLY"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from cfg import YOUR_API_KEY
polyoptions = PolygonOptionsSDK(YOUR_API_KEY)


async def get_all_options_data():

    contracts  = await polyoptions.fetch_all_option_contracts(
        expiration_date_gte="2023-05-18", #the expiration will be after today
        expiration_date_lte="2023-07-01", #select your desired date range
        )


    await polyoptions.get_snapshots(contracts,'files/options/all_options_data.csv')

    print(f"Data has been successfully saved to files/options/all_options_data.csv")
asyncio.run(get_all_options_data())




