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


ticker="SPY"
multiplier=1
timespan="day"
from_date="2023-05-01"
to_date="2023-05-18"
order="desc"
limit=100


async def main():
    aggs = await poly.get_aggregates(ticker, multiplier, timespan, from_date, to_date, order, limit)

    close = aggs.close
    open = aggs.open
    high = aggs.high
    low = aggs.low
    volume = aggs.volume
    timestamp = aggs.timestamp

    data = {
        'Open': open,
        'High': high,
        'Low': low,
        'Close': close,
        'Time': timestamp,
        'Volume': volume
    }

    df = pd.DataFrame(data)

    # Convert timestamp to datetime and set it as index
    df['Time'] = pd.to_datetime(df['Time'], unit='ms')
    df.set_index('Time', inplace=True)
    df.sort_index(inplace=True)
    # Rename columns to match mplfinance requirements
    df.rename(columns={'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume'}, inplace=True)

    # Plot the candlestick chart using mplfinance
    mpf.plot(df, type='candle', style='nightclouds', title=f'{ticker} - {multiplier} {timespan}', ylabel='Price ($)', volume=True, ylabel_lower='Volume')

asyncio.run(main())