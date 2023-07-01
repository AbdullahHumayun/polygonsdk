import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
from sdks.polygon_sdk.universal_snapshot import UniversalOptionSnapshot,UniversalSnapshot
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
import aiohttp
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from sdks.helpers.helpers import human_readable, extract_underlying_symbol
from polygon_enhanced.polygon_enhanced import WebSocketClient
from polygon_enhanced.polygon_enhanced.websocket import WebSocketMessage, Market
from polygon_enhanced.polygon_enhanced.websocket.models import EquityAgg,EquityTrade
from polygon_enhanced.polygon_enhanced.websocket import EquityQuote
from discord_webhook import AsyncDiscordWebhook, DiscordEmbed
from typing import List
import disnake
from disnake.ext import commands
from cfg import YOUR_API_KEY, YOUR_DISCORD_BOT_TOKEN, today_str, fifteen_days_from_now_str
import asyncio
from tabulate import tabulate
webull = AsyncWebullSDK()

poly = AsyncPolygonSDK(YOUR_API_KEY)

opts = PolygonOptionsSDK(YOUR_API_KEY)


symbols = ['SPY', 'SPX', 'VIX', 'QQQ', 'IWM', 'TSLA', 
           'AAPL', 'AMZN', 'AMC', 'SLV', 'BAC', 'F', 'HYG', 
           'TLT', 'NVDA', 'AMD', 'INTC', 'PLTR', 'XLF', 'EEM', 
           'GOOGL', 'CCL', 'NKLA', 'SOFI', 'AAL', 'MSFT', 'BABA', 
           'META', 'C', 'ATVI', 'GDX', 'UBER', 'GOOG', 'NIO', 'WFC', 
           'GLD', 'PFE', 'EWZ', 'FXI', 'SNAP', 'VALE', 'DIS', 'KRE', 
           'T', 'MU', 'PYPL', 'PBR', 'RIVN', 'JPM', 'ET', 'XLE', 'LCID', 
           'MARA', 'TQQQ', 'XOM', 'VZ', 'GM', 'RIG', 'COIN', 'MULN', 'GOLD', 
           'CHPT', 'WBD', 'CSCO', 'NU', 'UNG', 'PLUG', 'OXY', 'SCHW', 'JD', 
           'SPCE', 'UVXY', 'KWEB', 'SHOP', 'MPW', 'NFLX', 'SQQQ', 'TSM', 'DAL', 
           'ENVX', 'FCX', 'BITO', 'PARA', 'TLRY', 'RIOT', 'CVNA', 'BA', 'NKE', 
           'KO', 'DKNG', 'U', 'ORCL', 'NCLH', 'ARKK', 'SQ', 'PINS', 'AI', 'DVN', 'MS', 'SOXL']

c = WebSocketClient(subscriptions=["T.*,A.*,Q.*"], api_key= YOUR_API_KEY, market=Market.Options)
option_data = {}
bot = commands.Bot(commands.Bot(command_prefix=">>", intents=disnake.Intents.all()))
async def handle_msg(msgs: WebSocketMessage, message):
    # Instantiate a cache dictionary to store the ATM tickers

    equity_trade = {}
    print(trade_conditions)
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


            data_dict = { 

                "conditions": trade_conditions,
                "day_of_week": day_of_week,
                "large_trade": large_trade,
                "trade_price": trade_price,
                "trade_size": trade_size,
                "symbol": symbol
            }

      

            equity_trade.add

            if large_trade:
                color = disnake.Colour.dark_red()
            else:
                color = disnake.Colour.dark_grey()

            if "Automatic Execution" in trade_conditions:
                color = disnake.Colour.dark_orange()
            elif 'Single Leg Auction Non ISO' in trade_conditions:
                color = disnake.Colour.dark_magenta()
            elif 'Multi Leg auto-electronic trade against single leg(s)' in trade_conditions:
                color = disnake.Colour.dark_gold()
            elif 'Multi Leg auto-electronic trade' in trade_conditions:
                color = disnake.Colour.yellow()

            data = [
                ["Trade Conditions", trade_conditions],
                ["Day of Week", day_of_week],
                ["Exchange", exchange],
                ["Large Trade", large_trade],
                ["Trade Price", trade_price],
                ["Trade Size", trade_size],
                ["Symbol", human_readable(symbol)]
            ]

            embed = disnake.Embed(title="New System Test", color=color)

            if symbol in ["O:SPXW230630C04440000", "O:SPXW230630P04440000"]:
                table = tabulate(data, headers=["Attribute", "Value"], tablefmt="fancy")
                embed.add_field(name="Test", value=f"```{table}```")

            await message.edit(embed=embed)

        elif isinstance(m, EquityAgg):
           data_dict = { 
               

           'total_volume': m.accumulated_volume,
            'agg_vwap':m.aggregate_vwap,
            'avg_size':m.average_size,
            'last_price':m.close,
            'timestamp':m.end_timestamp,
            'official_open':m.official_open_price,

           }


       

@bot.slash_command()
async def main(inter: disnake.AppCmdInter):
    """Start streaming options"""
    await inter.response.defer()
    embed = disnake.Embed(title="Test")
    message = await inter.edit_original_message(embed=embed)
    await c.connect(lambda msgs: handle_msg(msgs, message))

bot.run(YOUR_DISCORD_BOT_TOKEN)
































