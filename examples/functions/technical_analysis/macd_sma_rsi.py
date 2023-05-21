import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

"""
PLOT CHARTS USING AGGREGATES DATA
"""
import asyncio
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY
poly = AsyncPolygonSDK(YOUR_API_KEY)



ticker="AMD"
multiplier=1
timespan="hour"

order="desc"
limit=100


async def main():


    print(ticker)
    macd, histogram, signal = await poly.get_macd(ticker, timespan="hour", limit=100)
    
    sma21 = await poly.get_simple_moving_average(ticker, timespan="hour", window=9)
    sma9 = await poly.get_simple_moving_average(ticker, timespan="hour", window=21)

    rsi = await poly.get_rsi(ticker,timespan="hour")

    print(rsi)

    print(sma9)
    print(sma21)
    print(histogram)
    print(signal)
asyncio.run(main())


