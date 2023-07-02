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
from cfg import YOUR_API_KEY

from asyncio import Queue

master = MasterSDK()
webull = AsyncWebullSDK()
sdk = AsyncPolygonSDK(YOUR_API_KEY)
df = pd.read_csv('files/stocks/all_snapshots.csv') #you must first download this file by running the "get_latest_ticker_data.py" file.

from tabulate import tabulate

async def consume(queue: asyncio.Queue):
    while True:
        ticker_list = await webull.top_active_stocks()
        tickers = ticker_list.symbol

        tasks = []
        skews_outside_range = []
        for ticker in tickers:
            tasks.append(process_ticker(ticker, skews_outside_range))

        await asyncio.gather(*tasks)

        table = tabulate(skews_outside_range, headers='keys', tablefmt='psql', showindex=False)
        print(table)

async def process_ticker(ticker, skews_outside_range):
    x = await master.get_near_the_money_single(ticker, 5)
    try:
        skew = await master.find_skew(x)

        if 'Close' not in skew.columns or 'Skew' not in skew.columns:
            return

        skew['skew_metric'] = skew['Strike'] - skew['💲']
        print(skew['skew_metric'])
        mask = (skew['skew_metric'] < -5) | (skew['skew_metric'] > 5)
        selected_columns = skew[mask][['Sym', '💲',  'Skew', '🗓️', 'IV']]
        skews_outside_range.extend(selected_columns.to_dict('records'))
    except AttributeError:
        return
    
async def handle_msg(msgs: List[TestStocksEvent], queue: Queue):
    for m in msgs:

        
        await queue.put(m)

async def send_messages(handler, queue):  # pass queue as an argument
    while True:
        # Select a random row from the DataFrame
        index = random.randint(0, len(df) - 1)
        row = df.iloc[index]

        # Create TestStocksEvent object from row data
        event = TestStocksEvent.from_row(row)

        # Call the handler with the message
        await handler([event], queue)
        await asyncio.sleep(0.01)

# async def main():
#     data_queue = Queue() 

#     num_workers = 15  # adjust this value based on your requirements
#     sdk_tasks = [
#         consume(data_queue) for _ in range(num_workers)
#     ]

#     sdk_tasks.append(asyncio.create_task(send_messages(handle_msg, data_queue)))

#     await asyncio.gather(*sdk_tasks)  # include consume_task in gather()

# asyncio.run(main())
