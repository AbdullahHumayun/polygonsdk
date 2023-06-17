import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
import asyncio
from api_master.cfg import YOUR_API_KEY

sdk = AsyncPolygonSDK(YOUR_API_KEY)
async def main():

    ticker="SPY"
    aggs = await sdk.get_aggregates(ticker, 1, "day", from_date="2023-01-01", to_date = "2023-05-16",limit = 2000)
    close = aggs.close
    open = aggs.open
    high = aggs.high
    low = aggs.low
    time = aggs.timestamp
    df = await sdk.find_gaps(open, high, low, close, time)
    

    df.to_csv(f'files/stocks/gaps/{ticker}_gaps.csv')

    print(df)

asyncio.run(main())