import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))



from polygon_sdk.async_polygon_sdk import AsyncPolygonSDK

from typing import List
import random
import asyncio
from datetime import datetime
from sdks.models.test_events import TestStocksEvent, EQUITY_TRADE_CONDITIONS
import pandas as pd

from polygon_sdk.async_polygon_sdk import AsyncPolygonSDK

from cfg import YOUR_API_KEY

from asyncio import Queue


sdk = AsyncPolygonSDK(YOUR_API_KEY)
df = pd.read_csv('files/stocks/all_snapshots.csv')


from discord_webhook import AsyncDiscordWebhook, DiscordEmbed
async def consume(queue: Queue):
    while True:
        m = await queue.get()
        ask = m.last_quote_ask_price
        close =m.close
        low=m.low
        open = m.open
        high = m.high
        volume = m.volume
        prev_volume = m.prev_volume
        prev_vwap = m.prev_vwap
        vwap = m.vwap
        bid = m.last_quote_bid_price
        conditions = m.last_trade_conditions
        print(open, high)
        # Process the event as necessary
        if volume > prev_volume:
            hook = AsyncDiscordWebhook("https://discord.com/api/webhooks/1109345997802459147/H2b9X9sYvgVYJCH64zpGrcV6EyCtgy65_8zk5kfcFTOOAyMYTC7gwb_273KBD0toqXeg")
            embed = DiscordEmbed(title=f"TRADE DETECTED!", description=f"> {m.symbol} is trading with more volume than yesterday!")
            embed.add_embed_field(name=f"> Volume Today:", value=f"> **{volume}**")
            embed.add_embed_field(name=f"> Volume Yesterday:", value=f"> **{prev_volume}**")
            hook.add_embed(embed)
            await hook.execute()

async def handle_msg(msgs: List[TestStocksEvent], queue: Queue):
    for m in msgs:
        m.symbol
        
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
    data_queue = Queue() 

    num_workers = 15  # adjust this value based on your requirements
    sdk_tasks = [
        consume(data_queue) for _ in range(num_workers)
    ]

    sdk_tasks.append(asyncio.create_task(send_messages(handle_msg, data_queue)))

    await asyncio.gather(*sdk_tasks)  # include consume_task in gather()

asyncio.run(main())
