import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


import asyncio
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY, five_days_ago_str, today_str

polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)
ticker = "GME"

async def support_resistance_example(ticker):
    """
    Retrieve support and resistance levels for a given stock ticker.

    This function retrieves the support and resistance levels for the specified stock ticker using the AsyncPolygonSDK.
    The support and resistance levels are calculated based on the provided parameters: stock ticker, multiplier, timespan,
    and date range. The retrieved levels are then displayed.

    Args:
        ticker (str): The ticker symbol for the stock.



    """
    support, resistance = await polygonsdk.get_support_resistance_levels(
        stock_ticker=ticker,
        multiplier=30,
        timespan='minute',
        from_date=five_days_ago_str,
        to_date=today_str
    )
    print(f"Support for {ticker}: ${support}")
    print(f"Resistance for {ticker} ${resistance}")

asyncio.run(support_resistance_example(ticker))