import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))




from typing import List
import random
import asyncio
from datetime import datetime
from sdks.models.test_events import TestStocksEvent, STOCK_EXCHANGES

from sdks.polygon_sdk.mapping_dicts import stock_condition_dict, option_condition_dict, OPTIONS_EXCHANGES

import pandas as pd

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK

from cfg import YOUR_API_KEY

from _discord.hooks.hook_dicts import stock_exchange_hooks
from discord_webhook import AsyncDiscordWebhook, DiscordEmbed
from asyncio import Queue
from _discord.embeddings import Data

sdk = AsyncPolygonSDK(YOUR_API_KEY)
df = pd.read_csv('files/stocks/all_snapshots.csv') #create this  file in 'get_latest_ticker_data.py'

class MockDiscord(Data):
    def __init__(self, symbol=None):
        self.symbol = symbol
        self.last_exchange = None
        self.buyvol = None
    async def consume(self, queue: Queue):
        
        while True:
            tasks=[]
            m = await queue.get()
            self.ask = m.last_quote_ask_price
            self.bid = m.last_quote_bid_price
            self.bid_size = m.last_quote_bid_size
            self.ask_size = m.last_quote_ask_size
            self.snapshot_close = m.close
            self.snapshot_low = m.low
            self.snapshot_open = m.open
            self.snapshot_high = m.high
            self.today_change_percent = m.today_change_percent
            self.today_change = m.today_change
            self.snapshot_volume = m.volume
            self.prev_volume = m.prev_volume
            self.prev_vwap = m.prev_vwap
            self.snapshot_vwap = m.vwap
            self.snapshot_exchange = STOCK_EXCHANGES.get(m.last_exchange)
            self.conditions = [stock_condition_dict.get(condition, 'Unknown') for condition in m.last_trade_conditions]
            self.snapshot_size = m.last_size
            self.snapshot_price = m.last_price
            self.minute_close = m.min_close
            self.minute_high = m.min_high
            self.minute_low = m.min_low
            self.minute_open = m.min_open
            self.minute_volume = m.min_volume
            self.minute_accumulated_volume = m.min_av
            self.minute_vwap = m.min_vwap
            self.prev_close = m.prev_close
            self.prev_high = m.prev_high
            self.prev_low = m.prev_low
            self.prev_open = m.prev_open
            self.prev_volume = m.prev_volume
            await asyncio.sleep(5)
            for name, webhook_url in stock_exchange_hooks.items():
                exchange_hook = AsyncDiscordWebhook(webhook_url, content="<@375862240601047070>")
                embed = DiscordEmbed(title=f"Exchange Feed - {self.snapshot_exchange}")
                exchange_hook.add_embed(embed)
                asyncio.create_task(self.send_webhook(exchange_hook))
                await asyncio.sleep(2.5)

            for name, webhook_url in OPTIONS_EXCHANGES.items():
                exchange_hook = AsyncDiscordWebhook(webhook_url, content="<@375862240601047070>")
                embed = DiscordEmbed(title=f"Exchange Feed - {self.snapshot_exchange}")
                exchange_hook.add_embed(embed)
                asyncio.create_task(self.send_webhook(exchange_hook))
                await asyncio.sleep(2.5)

            for name, webhook_url in option_condition_dict.items():
                exchange_hook = AsyncDiscordWebhook(webhook_url, content="<@375862240601047070>")
                embed = DiscordEmbed(title=f"Exchange Feed - {self.snapshot_exchange}")
                exchange_hook.add_embed(embed)
                asyncio.create_task(self.send_webhook(exchange_hook))
                await asyncio.sleep(2.5)

    async def send_webhook(self, webhook):
        retries = 0
        while retries < 5:
            await webhook.execute()
            break



        retries += 1
    
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

async def main():
    data = MockDiscord()

    data_queue = Queue() 

    num_workers = 15  # adjust this value based on your requirements
    sdk_tasks = [
        data.consume(data_queue) for _ in range(num_workers)
    ]

    sdk_tasks.append(asyncio.create_task(send_messages(handle_msg, data_queue)))

    await asyncio.gather(*sdk_tasks)  # include consume_task in gather()

asyncio.run(main())