import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from discord_webhook import AsyncDiscordWebhook, DiscordEmbed
from typing import List
import pandas as pd
import random
from cfg import skew_indices_hook,china_indices_hook,benchmark_indices_hook,us_dollar_hook,us_dollar, futures_indices_hook,volatility_indices_hook, spx_dispersion_hook,cloud_indices_hook,short_indices_hook
import asyncio
from sdks.models.test_events import TestIndicesEvent
from cfg import skew_indices,china_indices,volatility_indices, short_indices, spx_dispersion_indices, cloud, benchmark, futures

import logging

logging.basicConfig(level=logging.INFO)
df = pd.read_csv('files/indices/all_indices_data.csv')
class SimulatedClient:
    def __init__(self):
        self.queue = asyncio.Queue()

    async def send_indices_messages(self):
        while True:
            index = random.randint(0, len(df) - 1)
            row = df.iloc[index]
            event_indices = TestIndicesEvent.from_row(row)
            await self.queue.put([event_indices])
            await asyncio.sleep(0.001)

    async def print_messages(self, term):
        names = []
        while True:
            
            message = await self.queue.get()
            for m in message:
                if isinstance(m, TestIndicesEvent):
                    m.name = str(m.name)
                    if m.name is not None and isinstance(m.name, str) and f'{term}' in m.name:
                        if m.name not in names:
                            names.append(m.name)
                    if m.name in skew_indices:
                        await self.create_embed(skew_indices_hook,m)
       
                    if m.name in china_indices:
                        await self.create_embed(china_indices_hook,m)
        
                    if m.name in volatility_indices:
                        await self.create_embed(volatility_indices_hook,m)
     
                    if m.name in spx_dispersion_indices:
                        await self.create_embed(spx_dispersion_hook,m)
                    if m.name in cloud:
                        await self.create_embed(cloud_indices_hook,m)

                    if m.name in short_indices:
                        await self.create_embed(short_indices_hook,m)

                    if m.name in futures:
                        await self.create_embed(futures_indices_hook,m)

                    if m.name in benchmark:
                        await self.create_embed(benchmark_indices_hook, m)

                    if m.name in us_dollar:
                        await self.create_embed(us_dollar_hook, m)
            print(names)
             
    async def create_embed(self, webhook_url: AsyncDiscordWebhook, m: TestIndicesEvent):

        embed = DiscordEmbed(title=f"{m.ticker}",description=f"> {m.name}\n\n```py\n{m}```")
        embed.set_timestamp()
        embed.set_footer(text=f"{m.ticker} | Data Provided by Polygon.io")
        webhook_url.add_embed(embed)


        await webhook_url.execute()




    async def run(self):
        #logging.info('Starting tasks')
        send_task = asyncio.create_task(self.send_indices_messages())
        print_task = asyncio.create_task(self.print_messages(term="Technology"))
        await asyncio.gather(send_task, print_task)






