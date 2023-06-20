import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from menus.pagination import AlertMenus

import disnake
import asyncio
from disnake.ext import commands
intents=disnake.Intents.all()
from tabulate import tabulate
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
from trial import find_lowest_iv,get_near_the_money2,get_price_data,get_near_the_money

from 

from cfg import YOUR_API_KEY, YOUR_DISCORD_BOT_TOKEN


polygon = AsyncPolygonSDK(YOUR_API_KEY)
poly_options = PolygonOptionsSDK(YOUR_API_KEY)
webull = AsyncWebullSDK()


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

greenfire="<a:_:1043589872885174292>"
redfire="<a:_:1043589715145805934>"
@bot.slash_command()
async def iv_tv(inter: disnake.AppCmdInter, ticker= str):  # default ticker to SPX if not provided
    await inter.response.defer()
    while True:
        price = await get_price_data(ticker=ticker)
        lower_strike = 0.98 * price
        upper_strike = 1.02 * price

        atm_options = await get_near_the_money(ticker, lower_strike=lower_strike, upper_strike=upper_strike, today_str="2023-06-20")
        print(atm_options)
        redfire = "🔥"  # Red flame emoji
        greenfire = "🟢"  # Green flame emoji

        low_iv_data = await find_lowest_iv(atm_options)
        table = []

        for k in low_iv_data:
            for i in range(25):
                try:
                    strike = k[i]['strike']
                    expiry = k[i]['expiry']
                    name = k[i]['expiry']
                    iv = k[i]['iv']
                    change = k[i]['percent_change']
                    volume = k[i]['volume']
                    oi = k[i]['oi']
                    mid = k[i]['mid']
                    skew = redfire if strike < price else greenfire

                    row = [expiry[5::1], f"${price}", skew, f"${strike}", f"{round(float(iv)*100, 4)}", f"${mid}", f"{volume}"]
                    table.append(row)
                except IndexError:
                    continue

                table_formatted = tabulate(table, headers=['Expiry', 'Price', 'Skew', 'Low Strike', 'IV', 'Mid', 'Volume'], tablefmt='fancy')

                embed = disnake.Embed(title=f"{ticker} IV TV")
                embed.add_field(name="Color:", value="```A 🔥 is a put skew for that expiration. A 🟢  is a call skew for that expiration.```")
                embed.set_footer(text=f'Viewing Skews for {ticker}', icon_url=await polygon.get_polygon_logo(ticker))
                embed.description = f"`{table_formatted}`"
                await inter.edit_original_message(embed=embed)



extensions = []
cogs_directory = os.path.join(os.path.dirname(__file__), 'cogs')

for filename in os.listdir(cogs_directory):
    if filename.endswith('.py'):
        extension_name = filename[:-3]  # Remove the .py extension
        extensions.append(f'cogs.{extension_name}')

for extension in extensions:
    bot.load_extension(f'bot.{extension}')

bot.run(YOUR_DISCORD_BOT_TOKEN)