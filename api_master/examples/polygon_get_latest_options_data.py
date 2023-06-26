"""FOR HIGH TIER SUBSCRIBERS"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from cfg import YOUR_API_KEY, today_str
polyoptions = PolygonOptionsSDK(YOUR_API_KEY)
import aiohttp

async def get_all_options_data():
    # Create a PolyOptions instance


    # Fetch all option contracts concurrently
    contracts_task = polyoptions.fetch_all_option_contracts(
        expiration_date_gte=str(today_str),  # the expiration will be after today
        expiration_date_lte="2023-06-30"  # select your desired date range
    )

    contracts = await contracts_task

    # Get snapshots of all contracts concurrently
    snapshots_task = polyoptions.get_snapshots(contracts, 'files/options/all_options_data.csv')

    await snapshots_task

    print(f"Data has been successfully saved to files/options/all_options_data.csv")

async def main():
    # Create an aiohttp session
    async with aiohttp.ClientSession() as session:
        # Run get_all_options_data concurrently
        await asyncio.gather(
            get_all_options_data(),
           
        )

# Run the main function
asyncio.run(main())



