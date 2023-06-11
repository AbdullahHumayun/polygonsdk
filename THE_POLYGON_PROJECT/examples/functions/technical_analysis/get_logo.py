import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

import asyncio

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY


sdk = AsyncPolygonSDK(YOUR_API_KEY)
ticker="AAPL"

class Logo:
    def __init__(self, ticker=None):
        self.ticker = ticker
    #Prints company logo URL
    async def logo(self, ticker):
        self.ticker_logo = await sdk.get_polygon_logo(ticker)
        print(self.ticker_logo)

        return Logo(self.ticker_logo)


async def main():

    ticker = ticker

asyncio.run(Logo().logo(ticker))
