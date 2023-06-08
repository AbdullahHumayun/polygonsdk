import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from menus.pagination import AlertMenus

import disnake
from disnake.ext import commands
intents=disnake.Intents.all()
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK

from cfg import YOUR_API_KEY
from cfg_discord import discord_bot_token

polygon = AsyncPolygonSDK(YOUR_API_KEY)
poly_options = PolygonOptionsSDK(YOUR_API_KEY)
webull = AsyncWebullSDK()
intents = disnake.Intents.all()

class PersistentViewBot(commands.Bot):
    def __init__(self, command_prefix, intents, ticker=None, embeds=None):
        self.ticker = ticker
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.persistent_views_added = False
        self.embeds = embeds

    async def on_ready(self):
        if not self.persistent_views_added:
            view = AlertMenus(self.embeds)
            self.add_view(view)
            self.persistent_views_added = True

        print(f"Logged in as {self.user} (ID: {self.user.id})")


   



bot = PersistentViewBot(command_prefix=">>", intents=intents)

bot.load_extensions("bot\cogs")
bot.run(discord_bot_token)