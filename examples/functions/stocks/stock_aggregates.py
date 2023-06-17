import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
import pandas as pd

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY, five_days_ago_str, today_str

polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)
ticker = "GME"

async def stock_aggregates_example(ticker):
    """
    Retrieve stock aggregates data for a given ticker and save it to a CSV file.

    This function retrieves stock aggregates data for the specified ticker using the AsyncPolygonSDK.
    The data includes open, close, high, low prices, volume, volume-weighted average price (VWAP),
    and timestamps. The retrieved data is then displayed and saved to a CSV file.

    Args:
        ticker (str): The ticker symbol for the stock.

 
    """

    stock_aggregates_data = await polygonsdk.get_aggregates(
        ticker=ticker,
        multiplier=1,
        timespan="day",
        from_date=five_days_ago_str,
        to_date=today_str,
        order="desc"
    )

    open_prices = stock_aggregates_data.open
    close_prices = stock_aggregates_data.close
    high_prices = stock_aggregates_data.high
    low_prices = stock_aggregates_data.low
    volume = stock_aggregates_data.volume
    vwap = stock_aggregates_data.volume_weighted_average
    timestamps = await polygonsdk.format_timestamps_list(stock_aggregates_data.timestamp)

    # Display the retrieved data
    print(f"Open Prices: {open_prices}")
    print(f"Close Prices: {close_prices}")
    print(f"High Prices: {high_prices}")
    print(f"Low Prices: {low_prices}")
    print(f"Volume: {volume}")
    print(f"VWAP: {vwap}")
    print(f"Timestamps: {timestamps}")

    df = pd.DataFrame(stock_aggregates_data.results)
    try:
        df[timestamps] = pd.to_datetime(df['t'], unit='ms')
    except KeyError:
        print(f'Not enough data to convert timestamps to datetime - leaving in Unix MS format.')
        timestamps = stock_aggregates_data.timestamp
    df.to_csv(f'files/stocks/{ticker}_aggregates.csv')

    print(df)

asyncio.run(stock_aggregates_example(ticker=ticker))