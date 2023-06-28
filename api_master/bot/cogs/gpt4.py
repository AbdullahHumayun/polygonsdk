import disnake
import openai
import asyncio
import json

from cfg import YOUR_OPENAI_KEY, YOUR_API_KEY
from disnake.ext import commands
from _discord import emojis
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK


webull = AsyncWebullSDK()
poly = AsyncPolygonSDK(YOUR_API_KEY)





mybot = commands.Bot(command_prefix="!")
class GPT4(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot=bot



    @commands.slash_command()
    async def gpt4(inter):
        pass




def setup(bot:commands.Bot):
    bot.add_cog(GPT4(bot))
    print(f"> Extension {__name__} is ready\n")