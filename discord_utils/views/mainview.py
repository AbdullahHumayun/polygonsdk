import disnake
from ..selectmenus.mainselect import FTDShortSelect
import requests
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from typing import List
from datetime import datetime
import asyncio
today = datetime.today()
from cfg import YOUR_API_KEY
polygon = AsyncPolygonSDK(YOUR_API_KEY)


def send_embeds(symbols):
    max_embed_description_length = 4096

    current_embed_description = ""
    embeds = []

    for entry in symbols:
        formatted_entry = f"{entry} - Report Time: postmarket\n"

        # Check if the current description plus the new entry would exceed the limit
        if len(current_embed_description) + len(formatted_entry) > max_embed_description_length:
            embed = disnake.Embed(title="Earnings Tickers", description=f"```py\n{current_embed_description}\n```", color=disnake.Color.random())
            embeds.append(embed)
            current_embed_description = ""

        current_embed_description += formatted_entry

    # Create the last embed for remaining data
    if current_embed_description:
        embed = disnake.Embed(title="Earnings Tickers", description=f"```py\n{current_embed_description}\n```", color=disnake.Color.random())
        embeds.append(embed)

    return embeds




def generate_sectors_url(sectors: List[str]) -> str:
    sectors_url = ""
    for sector in sectors:
        sectors_url += f"&sectors[]={sector}"
    return sectors_url


class MainView(disnake.ui.View):
    def __init__(self, bot, ticker):
        self.ticker=ticker
        self.bot=bot
        super().__init__(timeout=None)
        self.add_item(FTDShortSelect(bot, ticker))




