import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))






from typing import List
import random
import asyncio
from sdks.models.test_events import TestStocksEvent
import pandas as pd

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.polygon_sdk.masterSDK import MasterSDK
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
from sdks.polygon_sdk.list_sets import subscriptions
from cfg import YOUR_API_KEY

from asyncio import Queue
df = pd.read_csv('files/stocks/all_snapshots.csv') #create this  file in 'get_latest_ticker_data.py'
master = MasterSDK()
webull = AsyncWebullSDK()
sdk = AsyncPolygonSDK(YOUR_API_KEY)


from tabulate import tabulate

async def consume(queue: asyncio.Queue):
    while True:
        subscriptions

        tasks = []

        for ticker in subscriptions:
            print(ticker)
            tasks.append(process_ticker(ticker))

        await asyncio.gather(*tasks)

 

async def process_ticker(ticker):
    x = await master.get_near_the_money_single(ticker, 5)
    print(x)
async def handle_msg(msgs: List[TestStocksEvent], queue: Queue):
    for m in msgs:

        
        await queue.put(m)

async def send_messages(handler, queue):
    while True:
        index = random.randint(0, len(df) - 1)
        row = df.iloc[index]
        event = TestStocksEvent.from_row(row)
        await handler([event], queue)
        await asyncio.sleep(0.01)

async def main():
    data_queue = Queue() 

    num_workers = 15  # adjust this value based on your requirements
    sdk_tasks = [
        consume(data_queue) for _ in range(num_workers)
    ]

    sdk_tasks.append(asyncio.create_task(send_messages(handle_msg, data_queue)))

    await asyncio.gather(*sdk_tasks)  # include consume_task in gather()

asyncio.run(main())
