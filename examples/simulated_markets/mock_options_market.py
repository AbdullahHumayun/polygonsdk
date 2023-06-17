import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from typing import List
import random
import asyncio
from asyncio import Queue

from sdks.helpers.helpers import human_readable
from sdks.models.test_events import TestOptionsEvent
import pandas as pd



from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from cfg import YOUR_API_KEY

sdk= PolygonOptionsSDK(YOUR_API_KEY)



df = pd.read_csv('files/options/all_options_data.csv') #you must download this spreadsheet from the "get_latest_options_data.py" file.


async def handle_msg(msgs: List[TestOptionsEvent], queue: Queue):
    for m in msgs:

        await queue.put(m) 

async def send_messages(handler, queue: Queue): 
    while True:
        index = random.randint(0, len(df) - 1)
        row = df.iloc[index]
        event = TestOptionsEvent.from_row(row)
        await handler([event], queue) 
        await asyncio.sleep(0.001) 

async def consume(queue: Queue): 
    while True:
        m = await queue.get()
        #do something
        print(f"{human_readable(m.ticker)} | ASK: ${m.ask} | BID: ${m.bid} | VOLUME: ${m.day_volume}")



async def main():
    data_queue = Queue() 

    num_workers = 15  # adjust this value based on your requirements
    sdk_tasks = [
        consume(data_queue) for _ in range(num_workers)
    ]

    sdk_tasks.append(asyncio.create_task(send_messages(handle_msg, data_queue)))

    await asyncio.gather(*sdk_tasks)  # include consume_task in gather()

asyncio.run(main())
