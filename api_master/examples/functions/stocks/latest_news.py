import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY

polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)
ticker="AAPL"
async def news(ticker):
    """
    Retrieve the latest news for a specific ticker and print the details.

    This function retrieves the latest news for a given ticker using the AsyncPolygonSDK,
    and prints the title, description, source URL, published date, publisher information,
    news image, news keywords, and tickers mentioned in the news.

    Args:
        ticker (str): The ticker symbol for the stock.

    Returns:
        None
    """

    news = await polygonsdk.get_ticker_narrative(ticker)
    desc = [i.description for i in news]
    news_keywords = [i.keywords for i in news]
    mentioned_tickers = [i.tickers for i in news]
    published = [i.pub_time for i in news]
    news_url = [i.news_url for i in news]
    publisher_homepage = [i.homepage_url for i in news]
    news_image = [i.image_url for i in news]
    publisher_logo = [i.logo_url for i in news]
    publisher_name = [i.name for i in news]
    title = [i.title for i in news]

    print(f"Latest News for {ticker[0]}:")
    print()
    print(f"Title: {title[0]}")
    print()
    print(f"Description: {desc[0]}")
    print()
    print(f"Source URL: {news_url[0]}")
    print(f"Published: {published[0]}")
    print(f"Publisher: {publisher_name[0]}")
    print(f"Publisher Website: {publisher_homepage[0]}")
    print(f"Publisher Logo: {publisher_logo[0]}")
    print(f"News Image: {news_image[0]}")
    print()
    print(f"News Keywords: {news_keywords[0]}")
    print(f"Tickers Mentioned: {mentioned_tickers[0]}")

asyncio.run(news(ticker))
