"""OPTIONS FUNCTIONS FOR THE POLYGONSDK"""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
import pandas as pd

from cfg import YOUR_API_KEY

from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK


webull = AsyncWebullSDK()
poly = AsyncPolygonSDK(YOUR_API_KEY)
polyoptions = PolygonOptionsSDK(YOUR_API_KEY)


ticker="GME"
async def fetch_entire_chain():
    all_options = await polyoptions.get_option_chain_all(ticker)



    # Create a DataFrame from the dictionary
    df = pd.DataFrame([option.to_dict() for option in all_options])
    # Save the DataFrame to a CSV file
    df.to_csv(f'files/options/ticker_chains/all_{ticker}_chains.csv', index=False)

# Run the main function
asyncio.run(fetch_entire_chain())