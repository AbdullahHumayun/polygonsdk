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

import aiohttp



from cfg import YOUR_API_KEY, YOUR_DISCORD_BOT_TOKEN
from trial2 import get_near_the_money_options2, get_price

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



@bot.slash_command()
async def main(ctx: disnake.AppCmdInter):
    await ctx.response.defer()

    async with aiohttp.ClientSession() as session:
        while True:
            try:
                tickers = ["AAPL","AMZN","MSFT","GOOG","KRE","WFC","JNJ","CVX","VZ","BAC","AMD","U","W","SNAP","META","MA","QCOM", "NVDA", "TSLA", "SHOP", "TGT", "WMT", "BABA", "CSCO", "COIN", "PYPL", "NKE", "PEP"]

                tasks = []
                for ticker in tickers:
                    tasks.append(get_price(session, ticker))

                prices = await asyncio.gather(*tasks)

                table_data = []

                for ticker, price in zip(tickers, prices):
                    lower_strike = round(price * 0.95)
                    upper_strike = round(price * 1.05)
                    lowest_iv_row = await get_near_the_money_options2(session, ticker=ticker, lower_strike=lower_strike, upper_strike=upper_strike)

                    low_strike = lowest_iv_row['strike_price']
                    low_iv = round(float(lowest_iv_row['implied_volatility'])*100, 6)
                    low_exp = lowest_iv_row['expiration_date']
                    low_contract_type = lowest_iv_row['contract_type']
                    low_iv_price = lowest_iv_row['underlying_price']
                    volume = lowest_iv_row['day_volume']
                    skew_metric = round(low_strike - price, 2)  # Skew metric: Difference between lowest IV strike and current price
                    if low_strike > price:
                        emoji = "🟩"
                    else:
                        emoji = "🔥"
                    table_data.append([ticker, low_iv_price, low_strike, emoji, low_iv, low_exp, volume, skew_metric])

                # Sort table data based on skew metric in ascending order
                table_data.sort(key=lambda x: x[-1])

                # Extract only the necessary columns for display
                display_data = [row[:-1] for row in table_data]

                headers = ["Ticker", "Price", "Skew", "Type", "IV", "Exp", "Volume"]
                table = tabulate(display_data, headers=headers, tablefmt="fancy")
                embed = disnake.Embed(title=f"Skew-De-Bop Monitor", description=f"```\n{table}\n```")
                await ctx.edit_original_message(embed=embed)

                await asyncio.sleep(60)  # Delay between iterations (e.g., 60 seconds)

            except Exception as e:
                print(f"An error occurred: {e}")







extensions = []
cogs_directory = os.path.join(os.path.dirname(__file__), 'cogs')

for filename in os.listdir(cogs_directory):
    if filename.endswith('.py'):
        extension_name = filename[:-3]  # Remove the .py extension
        extensions.append(f'cogs.{extension_name}')

for extension in extensions:
    bot.load_extension(f'bot.{extension}')

bot.run(YOUR_DISCORD_BOT_TOKEN)