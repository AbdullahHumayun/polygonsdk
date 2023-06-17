"""YOUR MAIN FILE TO CONDUCT MARKET ANALYSIS"""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from cfg import YOUR_API_KEY

from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK

polyoptions = PolygonOptionsSDK(YOUR_API_KEY)


underlying_symbol = "F"
expiration_date = "2023-05-19"
option_type = "C"
strike_price = 11.5

async def get_option_symbol():

    option_symbol = await polyoptions.generate_option_symbol(underlying_symbol=underlying_symbol, expiration_date=expiration_date, option_type=option_type, strike_price=strike_price)
    print(option_symbol)
    



# Run the main function
asyncio.run(get_option_symbol())