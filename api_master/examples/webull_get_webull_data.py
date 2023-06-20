import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from webull_webull_data import Webull


import asyncio
import pprint


#gets all webull data across all functions
async def process_data():
    webull = Webull()
    await webull.fetch_data('AAPL')
    pprint.pprint(webull.__dict__)

asyncio.run(process_data())