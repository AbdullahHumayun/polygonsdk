import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))


import asyncio

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY

symbol = "BAC"
polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)


async def exponential_moving_average(ticker):
    """
    Calculate and retrieve exponential moving averages (EMA) for a given stock ticker.

    This function calculates and retrieves the exponential moving averages (EMA) for the specified stock ticker
    using the AsyncPolygonSDK. It calculates the EMA for two different windows (50 and 21) and retrieves additional
    information such as VWAP price, EMA trends, and historic data. The retrieved data is then displayed.

    Args:
        ticker (str): The ticker symbol for the stock.


    """
    ema_50, timestamps = await polygonsdk.get_exponential_moving_average(
        symbol=symbol,
        timespan="minute",
        adjusted=True,
        window=50,
        limit=10
    )  # for 50 EMA

    ema_21, timestamps = await polygonsdk.get_exponential_moving_average(
        symbol=symbol,
        timespan="minute",
        adjusted=True,
        window=21,
        limit=10
    )  # for 21 EMA



    print(f"EMA21: {ema_21}")
    print(f"EMA50: {ema_50}")



asyncio.run(exponential_moving_average(symbol))
