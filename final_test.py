
import aiohttp
from api_master.sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK


import asyncio
from api_master.sdks.polygon_sdk.masterSDK import MasterSDK
import pandas as pd
from api_master.sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
import numpy as np
from tabulate import tabulate

opts = PolygonOptionsSDK(YOUR_API_KEY)
poly = AsyncPolygonSDK(YOUR_API_KEY)
import json
from api_master.sdks.polygon_sdk.news import TickerNews
master = MasterSDK()
async def get_news(session, url, previous_articles):
    async with session.get(url) as resp:
        r = await resp.json()
        results = r['results'] if 'results' in r else None

        current_articles = set(json.dumps(article, sort_keys=True) for article in results)
        new_articles = current_articles - previous_articles

        return current_articles, new_articles

async def main():
    previous_articles = set()

    url = f"https://api.polygon.io/v2/reference/news?limit=10&apiKey={YOUR_API_KEY}"

    async with aiohttp.ClientSession() as session:
        while True:
            current_articles, new_articles = await get_news(session, url, previous_articles)

            for article in new_articles:
                article = json.loads(article)
                keywords = TickerNews(article).keywords
                for keyword in keywords:
                    print(keyword)

            previous_articles = current_articles

            await asyncio.sleep(60)  # Sleep for a minute before checking again

asyncio.run(main())