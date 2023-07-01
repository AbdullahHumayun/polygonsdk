from polygon_enhanced.polygon_enhanced.websocket.models import EquityAgg,EquityTrade
from polygon_enhanced.polygon_enhanced.websocket.models.models import EquityQuote
from polygon_enhanced.polygon_enhanced.websocket import WebSocketClient, WebSocketMessage, Market
from discord_webhook import AsyncDiscordWebhook
from cfg import YOUR_API_KEY

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK

poly = AsyncPolygonSDK(YOUR_API_KEY)

from typing import List
import asyncio
import datetime
from tabulate import tabulate
import disnake
from disnake.ext import commands
import aiohttp
from cfg import YOUR_DISCORD_BOT_TOKEN, YOUR_API_KEY
bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all())

class PolygonStockMarket:
    def __init__(self):
        
        self.api_key = YOUR_API_KEY
        
    async def start_stream(self, subscriptions):
        self.c = WebSocketClient(api_key=YOUR_API_KEY, subscriptions=[subscriptions], market=Market.Stocks)






    async def handle_msg(self, msgs: WebSocketMessage, message):
        # Instantiate a cache dictionary to store the ATM tickers
        for m in msgs:
            if isinstance(m, EquityTrade):
                # Extract trade data from the EquityTrade object
                trade_conditions = m.conditions
                day_of_week = m.day_of_week
                exchange = m.exchange
                large_trade = m.is_large_trade
                trade_price = m.price
                trade_size = m.size
                symbol = m.symbol

                data = [
                    ["Trade Conditions", trade_conditions],
                    ["Day of Week", day_of_week],
                    ["Exchange", exchange],
                    ["Large Trade", large_trade],
                    ["Trade Price", trade_price],
                    ["Trade Size", trade_size],
                    ["Symbol", m.symbol]
                ]
                rsi = await poly.get_rsi(symbol=m.symbol,timespan="hour")
                if rsi is not None:

                    rsi_data = rsi.rsi_value[0]
                    print(rsi_data)

                else:
                    continue

                print(f"{symbol} : {trade_conditions} | RSI: {rsi_data}")
                embed = disnake.Embed(title="New System Test", color=disnake.Colour.random())


                table = tabulate(data, headers=["Attribute", "Value"], tablefmt="fancy")
                embed.add_field(name="Test", value=f"```{table}```")

                
                # Add all items from data_dict to equity_trade dictionary using symbol as key

                await message.edit(embed=embed)

    async def run_stream(self, inter:disnake.AppCommandInter):

        await inter.response.defer()
        embed = disnake.Embed(title="Test")
        message = await inter.edit_original_message(embed=embed)
        await self.c.connect(lambda msgs: self.handle_msg(msgs, message))
        # wait 30 seconds then close the connection
        await asyncio.sleep(30)
        await self.c.close()