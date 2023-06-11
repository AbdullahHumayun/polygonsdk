import asyncio

from examples.webull_data import Webull


import asyncio
import pprint

async def process_data():
    webull = Webull()
    await webull.fetch_data('AAPL')
    pprint.pprint(webull.__dict__)

asyncio.run(process_data())