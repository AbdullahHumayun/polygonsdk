import asyncio
""""
>>>  Un-comment the service you have to download fresh data for it

This is how to easily gather data for any subscription service to analyze markets.
"""
#from get_data.get_all_options_data import get_all_options_data
#from get_data.get_latest_crypto_data import get_all_crypto_data
#from get_data.get_latest_forex_data import get_forex_data
#from get_data.get_latest_indices_data import get_all_indices_data
from get_latest_ticker_data import get_all_ticker_data

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK

from cfg import YOUR_API_KEY, today_str

poly = AsyncPolygonSDK(YOUR_API_KEY)
polyoptions = PolygonOptionsSDK(YOUR_API_KEY)




async def get_your_data():



    # options = await get_all_options_data() 


    # forex = await get_forex_data()


    # crypto = await get_all_crypto_data()


    # indices = await get_all_indices_data()

    stocks = await get_all_ticker_data() 






asyncio.run(get_your_data())




