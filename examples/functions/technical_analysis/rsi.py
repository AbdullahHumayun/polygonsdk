import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY, today_str

sdk = AsyncPolygonSDK(YOUR_API_KEY)

ticker = ""
timespan = "day" #choose between day / minute / year / quarter / hour / week
from_date = "" #define how far back you'd like to go
to_date = today_str
limit = "" # max 50000

async def get_rsi(ticker, timespan, from_date, to_date, limit):
    await sdk.get_rsi(symbol=ticker,timespan=timespan,from_date=from_date, to_date=to_date,limit=limit)
    print(get_rsi)
    return 
