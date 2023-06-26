import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))




from sdks.rss_sdk.sdk import RSSSDK
from cfg import today_str, YOUR_FMP_KEY

import asyncio


async def main():

    # Example usage
    rss_feed_url = f'https://financialmodelingprep.com/api/v4/rss_feed?limit=100&type=10&from={today_str}to={today_str}&isDone=true&apikey={YOUR_FMP_KEY}'
    posts_generator = RSSSDK.fetch_new_posts(rss_feed_url)


    title = [i['title'] if 'title' in i else None for i in posts_generator]
    date = [i['date'] if 'date' in i else None for i in posts_generator]
    link = [i['link'] if 'link' in i else None for i in posts_generator]
    cik = [i['ck'] if 'cik' in i else None for i in posts_generator]
    form = [i['form_type'] if 'form_type' in i else None for i in posts_generator]
    ticker = [i['ticker'] if 'ticker' in i else None for i in posts_generator]
    done = [i['done'] if 'done' in i else None for i in posts_generator]

    print(done)


asyncio.run(main())