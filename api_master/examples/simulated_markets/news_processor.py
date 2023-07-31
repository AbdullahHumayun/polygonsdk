import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cfg import hex_colors
from discord_webhook import AsyncDiscordWebhook, DiscordEmbed
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import keywords_to_check,keyword_categories,keyword_webhooks
from cfg import YOUR_API_KEY
from sdks.polygon_sdk.list_sets import subscriptions as tickers
import asyncio

polygon = AsyncPolygonSDK(YOUR_API_KEY)

processed_ids = set()
async def process_news_item(description, title, image, thumbnail, id, name, author, news_tickers, url, homepage_urls, keywords):
    if id in processed_ids:
        return
    if keywords is not None:
        for keyword in keywords:
            if keyword is not None:
                # loop through each webhook url and its associated keywords
                for webhook_url, webhook_keywords in keyword_webhooks.items():
                    if keyword in webhook_keywords:
                        hook = AsyncDiscordWebhook(url=webhook_url, content="<@375862240601047070>")
                        embed = DiscordEmbed(title=title, description=f"```py\n{description}```", color=hex_colors['magenta'], url=url)
                        embed.add_embed_field(name="Publisher:", value=f"> **{name}**")
                        if homepage_urls is not None:
                            embed.add_embed_field(name=f"Homepage URL:", value=f"> **{homepage_urls}**")
                        if news_tickers is not None:
                            embed.add_embed_field(name=f"Tickers Mentioned:", value=f"> **{news_tickers}**")
                        if author is not None:
                            embed.set_author(name=author)
                        embed.set_image(url=image)
                        embed.set_thumbnail(url=thumbnail)
                        embed.set_timestamp()
                        hook.add_embed(embed)
                        await hook.execute()
                        processed_ids.add(id)
                        # Break out of the loop as soon as we find a match
                        break

async def news_main():
    while True:
        news_list = await polygon.process_news()
        if news_list is not None and len(news_list.keywords) > 0:
            tasks = []
            # Iterate through each news item first
            for description, title, image, thumbnail, id, name, author, news_tickers, url, homepage_urls, keywords in zip(news_list.description, news_list.title, news_list.image_url, news_list.logo_url, news_list.id, news_list.name, news_list.author, news_list.tickers, news_list.article_url, news_list.homepage_url, news_list.keywords):
                # Create a new task for each news item
                task = asyncio.create_task(process_news_item(description, title, image, thumbnail, id, name, author, news_tickers, url, homepage_urls, keywords))
                tasks.append(task)


            return tasks