


import requests
import time
from cfg import today_str, YOUR_FMP_KEY
import asyncio


class RSSSDK:


    def fetch_new_posts(url):
        last_update_time = None

        while True:
            response = requests.get(url)
            if response.status_code != 200:
                raise Exception("Failed to fetch RSS feed.")

            feed_data = response.json()

            for post in feed_data:
                post_time = post['date']
                if post_time != last_update_time:
                    last_update_time = post_time
                    yield post

            time.sleep(60)  # Wait for 60 seconds before fetching the feed again



