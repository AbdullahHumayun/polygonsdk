import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))



from embeddings import create_vwap_differential,spx_trades, send_to_sectors, send_exchanges
from typing import List
from cfg import YOUR_API_KEY, RETAIL_INTEREST_BID
from hooks.hook_dicts import stock_exchange_hooks, sector_hooks, options_exchange_hooks
from cfg import sector_hooks, spx
from cfg import VWAP_DIFFERENTIAL
import asyncio
from sdks.polygon_sdk.list_sets import OPTIONS_EXCHANGES, option_condition_dict
from sdks.helpers.helpers import human_readable
from collections import defaultdict
from sdks.polygon_sdk.masterSDK import MasterSDK
from discord_webhook import AsyncDiscordWebhook, DiscordEmbed
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from cfg import hex_colors, PRIOR_REFERENCE, CORRECTED_CLOSE, CLOSING_PRINTS,ORDER_INFLUX,konviction, DEFICIENT,CROSS_TRADE,INTERMARKET_SWEEPS,OPENING_TRADE,ODD_LOT, RETAIL_INTEREST_BID,RETAIL_INTEREST_BID_AND_ASK,RETAIL_INTEREST_ASK
from cfg import SSR,NEXT_DAY,vol1k_to5k,vol500_to1k,vol5k_to10k,vol_10kplus,squeeze_potential,near_52_high,near_52_low,new_52_high,new_52_low,accumulation,fire_sale
from cfg import OFFICIAL_CLOSE, earnings_today,earnings_week, seven_days_from_now_str,above_avg_volume,below_avg_volume,today_str
from polygon_enhanced.polygon_enhanced import WebSocketClient


from polygon_enhanced.polygon_enhanced.websocket.models import EquityQuote, Market, EquityAgg
from polygon_enhanced.polygon_enhanced.websocket.models.models import EquityTrade

from datetime import datetime
import disnake
from disnake.ext import commands
from sdks.helpers.helpers import build_embed
bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all())
from sdks.polygon_sdk.list_sets import stock_condition_dict, STOCK_EXCHANGES, TAPES, quote_conditions, indicators, market_sectors, subscriptions
import aiohttp
from asyncio import Queue
from pymongo import MongoClient
from polygon.websocket import WebSocketMessage
import traceback
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
poly = AsyncPolygonSDK(YOUR_API_KEY)
webull = AsyncWebullSDK()
master = MasterSDK()
c = WebSocketClient(subscriptions=["A.*,T.*,Q.*"], api_key=YOUR_API_KEY, market=Market.Options)
poly_opts = PolygonOptionsSDK(YOUR_API_KEY)

webull_cache = {}
# Function to get data from Webull with caching
async def get_webull_data_with_cache(ticker, data_type):
    if ticker not in webull_cache:
        webull_cache[ticker] = {}

    if data_type not in webull_cache[ticker]:
        if data_type == "stock_data":
            webull_cache[ticker][data_type] = await webull.get_webull_stock_data(ticker=ticker)
        elif data_type == "short_interest":
            webull_cache[ticker][data_type] = await webull.get_short_interest(ticker)
        elif data_type == "volume_analysis":
            webull_cache[ticker][data_type] = await webull.get_webull_vol_analysis_data(ticker)

    return webull_cache[ticker][data_type]




symbol_to_sector = {symbol: sector for sector, symbols in market_sectors.items() for symbol in subscriptions}
async def handle_msg(msgs: WebSocketMessage, queue: Queue):
    send_tasks = []  # List to hold all send tasks

    for m in msgs:

        message_data = {}
   
    if isinstance(m, EquityTrade):
        message_data['type'] = 'EquityTrade'
        message_data['symbol'] = m.symbol
        message_data['price'] = m.price
        message_data['size'] = m.size
        message_data['timestamp'] = datetime.fromtimestamp(m.timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S')
        message_data['conditions'] = [option_condition_dict.get(condition) for condition in m.conditions] if m.conditions is not None else []
        message_data['exchange'] = OPTIONS_EXCHANGES.get(m.exchange)
        tasks = []




    if isinstance(m, EquityAgg):
        message_data['type'] = 'EquityAgg'
        message_data['symbol'] = m.symbol
        message_data['official_open'] = m.official_open_price
        message_data['last_price'] = m.close
        message_data['total_volume'] = m.accumulated_volume
        message_data['volume'] = m.volume
        message_data['day_vwap'] = m.aggregate_vwap
        message_data['average_size'] = m.average_size
        message_data['otc'] = m.otc
        message_data['start_time'] = datetime.fromtimestamp(m.start_timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S')
        message_data['end_time'] = datetime.fromtimestamp(m.end_timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S')



    elif isinstance(m, EquityQuote):
        message_data['type'] = 'EquityQuote'
        message_data['symbol'] = m.symbol
        message_data['ask'] = m.ask_price
        message_data['bid'] = m.bid_price
        message_data['indicator'] = [indicators.get(indicator) for indicator in m.indicators] if m.indicators is not None else []
        message_data['condition'] = quote_conditions.get(m.condition)
        message_data['ask_size'] = m.ask_size
        message_data['bid_size'] = m.bid_size
        message_data['tape'] = TAPES.get(m.tape)
        message_data['timestamp'] = datetime.fromtimestamp(m.timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S')
        message_data['ask_exchange'] = OPTIONS_EXCHANGES.get(m.ask_exchange_id)
        message_data['bid_exchange'] = OPTIONS_EXCHANGES.get(m.bid_exchange_id)

        message_data['discord_webhook_url'] = options_exchange_hooks.get(message_data['bid_exchange'])
        # Check if the exchange matches a Discord channel


    await queue.put(message_data)

async def consume(queue: asyncio.Queue):

    while True:
        
        data = await queue.get()
        symbol = data['symbol']
        underlying_ticker = await poly_opts.extract_underlying_symbol(symbol)
        option_ticker = human_readable(symbol)
        if data['type'] == 'EquityTrade':
            # Check if the exchange matches a Discord channel


            
            ticker = await poly_opts.extract_underlying_symbol(data['symbol'])
            sector = symbol_to_sector.get(ticker)
            if sector and data['size'] >= 100:
                await send_to_sectors(data)

            sector = symbol_to_sector.get(data['symbol'])
            if sector and data['size'] is not None and data['size'] >= 100:
                # Get the webhook URL for the sector
                webhook_url = sector_hooks.get(sector)
                
                if webhook_url:
                    # Create the webhook object
                    webhook = AsyncDiscordWebhook(webhook_url, content="<@375862240601047070>")

                    # Create the embed message
                    embed = DiscordEmbed(title=f"Last Trade: {data['symbol']}",
                                            description=f"> Trade: **{data['size']}** shares @ **${data['price']}**\n\n> Conditions: **{data['conditions']}**\n\n> Exchange: **{data['exchange']}**")
                    webhook.add_embed(embed)

                    # Create a task for sending the webhook message to the corresponding sector channel
                    asyncio.create_task(build_embed(data['symbol'], embed, webhook_url))
                
                    print(f"EXECUTED WEBHOOK")



        if data['type'] == 'EquityAgg':

            if data['volume'] >= 1000:


                await create_vwap_differential(data)


                


from cfg import keyword_categories, keyword_webhooks, keywords_to_check





async def main():
    
    data_queue = Queue()

    asyncio.create_task(c.connect(lambda msg: asyncio.create_task(handle_msg(msg, data_queue))))
    num_workers = 15  # You can adjust this value based on your requirements
    sdk_tasks = [
        consume(data_queue) for _ in range(num_workers)
    ]

    await asyncio.gather(*sdk_tasks)



asyncio.run(main())
