import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import List
from asyncio import Queue
import random
import csv
import asyncio
import pandas as pd
from sdks.helpers.helpers import human_readable
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from sdks.models.test_events import TestOptionsEvent, option_condition_dict, OPTIONS_EXCHANGES

from sdks.helpers.helpers import extract_underlying_symbol
from sdks.simulated_markets.helpers import write_to_csv
from cfg import YOUR_API_KEY
from cachetools import TTLCache
sdk = PolygonOptionsSDK(YOUR_API_KEY)
queue = asyncio.Queue()
df = pd.read_csv('files/options/all_options_data.csv')

async def handle_msg(queue: asyncio.Queue, msgs: List[TestOptionsEvent]):
    tasks = []
    for m in msgs:
        option_symbol = m.ticker
        underlying_ticker = m.underlying_ticker
        tasks.append(queue.put((option_symbol, underlying_ticker)))
        await process_snapshot(option_symbol, underlying_ticker)

    await asyncio.gather(*[task for task in tasks if task is not None])

snapshot_cache = TTLCache(maxsize=2000, ttl=60)
# Bounded semaphore to limit concurrent tasks1
semaphore = asyncio.BoundedSemaphore(40)
async def send_messages(handler):
    while True:
        # Select a random row from the DataFrame
        # Select a random row from the DataFrame
        index = random.randint(0, len(df) - 1)
        row = df.iloc[index]

        # Create TestOptionsEvent object from row data
        event = TestOptionsEvent.from_row(row)

        # Print the created TestOptionsEvent object


        await handler([event])


async def process_snapshot(option_symbol: str, underlying_ticker):
    # Acquire the semaphore
    async with semaphore:

        snapshot = await sdk.get_option_contract_snapshot(underlying_asset=underlying_ticker, option_contract=option_symbol)
        # Retrieve the RSI value from the cache



        # Option Symbol Details
        option_symbol = snapshot.option_symbol
        strike_price = snapshot.strike_price
        contract_type = snapshot.contract_type
        expiration_date = snapshot.expiration_date
        break_even_price = snapshot.break_even_price

        # Day Information
 
        day_change_percent = snapshot.day_change_percent
        day_volume = snapshot.day_volume
        day_vwap = snapshot.day_vwap


        # Greeks and Volatility
        delta = snapshot.delta
        implied_volatility = snapshot.implied_volatility
        open_interest = snapshot.open_interest

        # Quote Data
        ask = snapshot.ask
        ask_size = snapshot.ask_size
        bid = snapshot.bid
        bid_size = snapshot.bid_size

        # Trade Information
        conditions = snapshot.conditions
        underlying_price = snapshot.underlying_price

        results = []

        print(f"Snapshot Processed for {human_readable(option_symbol)}")
        # Check if the option is a put with high implied volatility and nearing its break-even price
        if (implied_volatility is not None 
            and implied_volatility <= 0.53 
            and implied_volatility >= 0.22
            and underlying_price >= 5 
            and bid >= 0.07 
            and ask <= 2.00
            and abs(bid - ask) <= 0.03
            and bid_size is not None
            and ask_size is not None
            and bid_size > (ask_size * 10)
            and day_volume is not None
            and open_interest is not None
            and day_volume > (open_interest * 2)):
            
 
                
            results.append({"Underlying": underlying_ticker, "Strike Price": strike_price, "Contract Type": contract_type, "Expiration Date": expiration_date, "Day Volume": day_volume, "Day VWAP": day_vwap, "Open Interest": open_interest, "Delta": delta, "Day Change Percent": day_change_percent, "Implied Volatility": implied_volatility, "Underlying Price": underlying_price, "Break Even Price": break_even_price})

        # Save the results to a CSV file
        for result in results:
            write_to_csv(result)



async def worker(queue: asyncio.Queue):
    while True:
        option_symbol, symbol = await queue.get()
        await process_snapshot(option_symbol, symbol)
        queue.task_done()


async def main():
    # Create a queue to pass symbols between handle_msg and workers
    queue = asyncio.Queue()

    # Create a fixed number of worker tasks
    num_workers = 32
    worker_tasks = [asyncio.create_task(worker(queue)) for _ in range(num_workers)]

    await send_messages(lambda msgs: handle_msg(queue, msgs))

    # Cancel the worker tasks
    for task in worker_tasks:
        task.cancel()

    # Wait for the worker tasks to finish
    await asyncio.gather(*worker_tasks, return_exceptions=True)




asyncio.run(main())