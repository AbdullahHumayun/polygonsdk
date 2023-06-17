from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY
polygon = AsyncPolygonSDK(YOUR_API_KEY)
from asyncio import Semaphore

sem = Semaphore()


async def check_macd_condition_bullish(hist):
    if len(hist) < 3:
        return False

    last_three_values = hist[:3]
    print(last_three_values)
    return (
        abs(last_three_values[0] - (-0.03)) < 0.02
        and all(last_three_values[i] > last_three_values[i + 1] for i in range(len(last_three_values) - 1))
    )

async def check_macd_condition_bearish(hist):
    if len(hist) < 3:
        return False

    last_three_values = hist[:3]
    print(last_three_values)
    return (
        abs(last_three_values[0] - 0.03) < 0.02
        and all(last_three_values[i] < last_three_values[i + 1] for i in range(len(last_three_values) - 1))
    )

async def check_rsi_condition_bullish(rsi):
    if not rsi:
        return False
    return rsi[0] <= 32


async def check_rsi_condition_bearish(rsi):
    if not rsi:
        return False
    return rsi[0] >= 68

async def get_macd_rsi(ticker, queue):
    async with sem:
        macd, hist, signal = await polygon.get_macd(ticker, timespan="week", limit=50)
        rsi = await polygon.get_rsi(ticker, timespan="week", limit=50)

    await queue.put((ticker, hist, rsi))