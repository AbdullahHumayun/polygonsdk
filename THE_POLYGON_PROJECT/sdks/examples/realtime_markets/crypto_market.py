import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import asyncio
from typing import List
from polygon.websocket import WebSocketClient, WebSocketMessage, CryptoQuote, CryptoTrade, Market
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cachetools import TTLCache

from cfg import YOUR_API_KEY
poly = AsyncPolygonSDK(YOUR_API_KEY)
c = WebSocketClient(subscriptions=["XT.*, XQ.*"], market=Market.Crypto, api_key=YOUR_API_KEY)  # connect to the crypto market and subscribe to trades and quotes

# Cache to store recent RSI values for each symbol
rsi_cache = TTLCache(maxsize=1000, ttl=60)

# Bounded semaphore to limit concurrent tasks
semaphore = asyncio.BoundedSemaphore(50)


async def process_rsi(symbol: str):
    # Acquire the semaphore
    async with semaphore:
        rsi = await poly.crypto_rsi(pair=symbol, timespan="hour")
        rsi_value = rsi.rsi_value[0]

        # Store the RSI value in the cache
        rsi_cache[symbol] = rsi_value

        # Retrieve the RSI value from the cache
        cached_rsi = rsi_cache.get(symbol)



async def worker(queue: asyncio.Queue):
    while True:
        symbol = await queue.get()
        await process_rsi(symbol)
        queue.task_done()

async def handle_msg(queue: asyncio.Queue, msgs: List[WebSocketMessage]):
    tasks = []
    for m in msgs:
        if isinstance(m, CryptoQuote):
            pair = m.pair
            tasks.append(queue.put(pair))

        elif isinstance(m, CryptoTrade):
            pair = m.pair
            tasks.append(queue.put(pair))
            print(f"{pair} just traded for {m.size} shares at ${m.price} for a cost of ${m.size * m.price}. The RSI is currently {rsi_cache.get(pair, 'N/A')}.")

    # Wait for all tasks to be added to the queue
    await asyncio.gather(*[task for task in tasks if task is not None])


            
 

async def main():
    # Create a queue to pass symbols between handle_msg and workers
    queue = asyncio.Queue()

    # Create a fixed number of worker tasks
    num_workers = 20
    worker_tasks = [asyncio.create_task(worker(queue)) for _ in range(num_workers)]

    # Connect to the WebSocket and process messages
    await c.connect(lambda msgs: handle_msg(queue, msgs))

    # Cancel the worker tasks
    for task in worker_tasks:
        task.cancel()

    # Wait for the worker tasks to finish
    await asyncio.gather(*worker_tasks, return_exceptions=True)

asyncio.run(main())