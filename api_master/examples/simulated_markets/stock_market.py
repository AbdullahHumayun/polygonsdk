import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))




from typing import List
from cfg import keyword_categories,keyword_webhooks,keywords_to_check

from cfg import YOUR_API_KEY, RETAIL_INTEREST_BID, technicals_webhooks
from hooks.hook_dicts import stock_exchange_hooks, sector_hooks, options_exchange_hooks
from cfg import sector_hooks
from sdks.polygon_sdk.list_sets import etfs_list, subscriptions, OPTIONS_EXCHANGES,sublist1, options_condition_dict, crypto_exchanges, crypto_conditions_dict
import asyncio
from cfg import OVERSOLD_1HOUR,OVERBOUGHT_1HOUR,OVERBOUGHT_1MIN,OVERBOUGHT_DAY,OVERSOLD_1MIN,OVERSOLD_DAY, OVERBOUGHT_WEEK,OVERSOLD_WEEK, SUPER_OVERBOUGHT,SUPER_OVERSOLD
from collections import defaultdict

from discord_webhook import AsyncDiscordWebhook, DiscordEmbed
from cfg import hex_colors, PRIOR_REFERENCE, SHORT_APPENDAGE, LONG_APPENDAGE, CORRECTED_CLOSE,REDEMPTION_SUSPENSION, CLOSING_PRINTS,ORDER_INFLUX,konviction, DEFICIENT,CROSS_TRADE,INTERMARKET_SWEEPS,OPENING_TRADE,ODD_LOT, RETAIL_INTEREST_BID,RETAIL_INTEREST_BID_AND_ASK,RETAIL_INTEREST_ASK
from cfg import SSR,NEXT_DAY,vol1k_to5k,vol500_to1k,vol5k_to10k,vol_10kplus,squeeze_potential,near_52_high,near_52_low,new_52_high,new_52_low,accumulation,fire_sale
from cfg import OFFICIAL_CLOSE, earnings_today,earnings_week, seven_days_from_now_str,above_avg_volume,below_avg_volume,today_str
from polygon_enhanced.polygon_enhanced import WebSocketClient


from polygon_enhanced.polygon_enhanced.websocket.models import EquityTrade,EquityQuote, Market, EquityAgg, CryptoTrade

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
from polygon_enhanced.polygon_enhanced.websocket.models.models import IndexValue
poly = AsyncPolygonSDK(YOUR_API_KEY)
webull = AsyncWebullSDK()

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



    



async def consume(queue: asyncio.Queue):
    send_tasks=[]
    while True:

        data = await queue.get()
        if data['symbol'] in sublist1:
            print(data)
            

            if Market.Stocks:
                if data['type'] =='T':
                

                    # Check if the exchange matches a Discord channel
                    if data['symbol'] in subscriptions:
                        discord_webhook_url = stock_exchange_hooks.get(data['exchange'])
                        if discord_webhook_url and data['size'] > 1000:
                            embed = DiscordEmbed(title=f"Last Trade: {data['symbol']}",
                            description=f"> {data}")
                            # Create a task for sending the message and add it to the list
                            task = asyncio.create_task(build_embed(data['symbol'],embed, discord_webhook_url))
                            send_tasks.append(task)

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
                                task = asyncio.create_task(build_embed(data['symbol'], embed, webhook_url))
                                send_tasks.append(task)
                                print(f"EXECUTED WEBHOOK")

                    data['conditions'] = [stock_condition_dict.get(c, f"Unknown condition {c}") for c in data['conditions']]
                    # Create tasks for last_trade_condition and last_quote_condition

            

                    if data['conditions'] is not None and 22 in data['conditions']:
                        embed = DiscordEmbed(title=f"Prior Reference Price - {data['symbol']}", description=f"```py\n{data['symbol']} flagged with a condition code of 'Prior Reference Price.```", color=hex_colors['blue'])
                        await build_embed(data['symbol'],embed,PRIOR_REFERENCE)

                    elif data['conditions'] is not None and 8 in data['conditions']:
                        embed = DiscordEmbed(title=f"Closing Prints - {data['symbol']}", description=f"```py\nClosing Prints Detecteed```", color=hex_colors['red'])
                        await build_embed(data['symbol'],embed,CLOSING_PRINTS)


                    elif data['conditions'] is not None and 38 in data['conditions']:
                        embed = DiscordEmbed(title=f"Corrected Close - {data['symbol']}", description=f"```py\nCorrected Close```", color=hex_colors['yellow'])
                        await build_embed(data['symbol'],embed,CORRECTED_CLOSE)
                    elif data['conditions'] is not None and 20 in data['conditions']:
                        embed = DiscordEmbed(title=f"Next Day - {data['symbol']}", description=f"```py\nNext Day```", color=hex_colors['yellow'])
                        await build_embed(data['symbol'],embed,NEXT_DAY)
                    elif data['conditions'] is not None and 63 in data['conditions']:
                        embed = DiscordEmbed(title=f"Deficient - {data['symbol']}", description=f"```py\nFinancially Deficient - Doesn't meet listing standards.```", color=hex_colors['green'])
                        await build_embed(data['symbol'],embed,DEFICIENT)
                    elif data['conditions'] is not None and 9 in data['conditions']:
                        embed = DiscordEmbed(title=f"Cross Trade - {data['symbol']}", description=f"```py\nCross Trade Detected```", color=hex_colors['orange'])
                        await build_embed(data['symbol'],embed,CROSS_TRADE)
                    elif data['conditions'] is not None and 14 in data['conditions']:
                        embed = DiscordEmbed(title=f"Intermarket Sweep - {data['symbol']}", description=f"```py\nIntermarket Sweep Detected```", color=hex_colors['yellow'])
                        await data['symbol'],embed, INTERMARKET_SWEEPS
                    elif data['conditions'] is not None and 60 in data['conditions']:
                        embed = DiscordEmbed(title=f"SSR In Effect  - {data['symbol']}", description=f"```py\nThe Short Sale Rule is in effect for this ticker - meaning it cannot be shorted on a down-tick and has fallen 10% within the last trading day. SSR will remain active until the following business day at close.```", color=hex_colors['red'])
                        await build_embed(data['symbol'],embed, SSR)
                    elif data['conditions'] is not None and 17 in data['conditions']:
                        embed = DiscordEmbed(title=f"Opening Trade  - {data['symbol']}", description=f"```py\nThis trade has been flagged as a Market Center Opening Trade```", color=hex_colors['green'])
                        await build_embed(data['symbol'],embed, OPENING_TRADE)
                    elif data['conditions'] is not None and 15 in data['conditions']:
                        embed = DiscordEmbed(title=f"Official Close  - {data['symbol']}", description=f"```py\nThis trade has been flagged as a Market Center Official Close```", color=hex_colors['green'])
                        await build_embed(data['symbol'],embed, OFFICIAL_CLOSE)
                    elif data['conditions'] is not None and data['conditions'] == 37:
                        embed = DiscordEmbed(title=f"Odd Lot Trade  - {data['symbol']}", description=f"```py\nThis trade has been flagged as an odd lot trade.```", color=hex_colors['green'])
                        await build_embed(data['symbol'],embed, ODD_LOT)


                    if data['size'] is not None and data['size'] >= 500 and data['size'] <= 999:
                        embed= DiscordEmbed(title=f"Trade - 500 to 1k Volume", description=f"```py\n{data['symbol']} just traded for a size of {data['size']} at a price of ${data['price']}```")
                        await build_embed(data['symbol'], embed, vol500_to1k)
                    elif data['size'] is not None and data['size'] >= 1000 and data['size'] <= 4999:
                        embed= DiscordEmbed(title=f"Trade - 1k to 5k Volume", description=f"```py\n{data['symbol']} just traded for a size of {data['size']} at a price of ${data['price']}```")
                        await build_embed(data['symbol'], embed, vol1k_to5k)

                    elif data['size'] is not None and data['size'] >= 5000 and data['size'] <= 9999:
                        embed= DiscordEmbed(title=f"Trade - 5k to 10k Volume", description=f"```py\n{data['symbol']} just traded for a size of {data['size']} at a price of ${data['price']}```")
                        await build_embed(data['symbol'], embed, vol5k_to10k)

                    elif data['size'] is not None and data['size'] >= 10000:
                        embed= DiscordEmbed(title=f"Trade - 10k Plus Volume", description=f"```py\n{data['symbol']} just traded for a size of {data['size']} at a price of ${data['price']}```")
                        await build_embed(data['symbol'], embed, vol_10kplus)


                    volume_analysis_task = get_webull_data_with_cache(data['symbol'], "volume_analysis")
                    stock_data_task = get_webull_data_with_cache(data['symbol'], "stock_data")
                    short_interest_task = get_webull_data_with_cache(data['symbol'], "short_interest")

                    vol_analysis, stock_data, short_interest = await asyncio.gather(volume_analysis_task, stock_data_task, short_interest_task)

                    if short_interest is not None and len(short_interest.short_int) > 0:
                        short_int = float(short_interest.short_int[0])
                    else:
                        short_int = None
                    if stock_data is not None and stock_data.outstanding_shares is not None:
                        total_shares = float(stock_data.outstanding_shares)
                    else:
                        total_shares = None
                    if short_int is not None and total_shares is not None:
                        short_percentage_of_float = (short_int / total_shares) * 100
                    else:
                        short_percentage_of_float = 0

                    if short_percentage_of_float >= 35 and stock_data is not None and stock_data.avg_10d_vol is not None and stock_data.web_stock_vol is not None and float(stock_data.web_stock_vol) <= (float(stock_data.avg_10d_vol)):
                        embed = DiscordEmbed(title=f"Squeeze Potential - {data['symbol']}", description=f"```py\nThis feed returns tickers exhibiting signs of a potential squeeze. Short interest % of float > 25 - volume is below average.```", color=hex_colors['green'])
                        await build_embed(data['symbol'], embed, squeeze_potential)
                    elif stock_data is not None and stock_data.web_stock_close is not None and stock_data.fifty_high is not None and float(stock_data.web_stock_close) > 0.95 * float(stock_data.fifty_high):
                        embed = DiscordEmbed(title=f"{data['symbol']} is Near 52 week Highs! {data['symbol']}", description=f"```py\nThis feed returns tickers trading within 5% of their 52 week high```", color=hex_colors['red'])
                        await build_embed(data['symbol'], embed, near_52_high)

                    elif stock_data is not None and stock_data.web_stock_close is not None and stock_data.fifty_low is not None and float(stock_data.web_stock_close) < 0.05 * float(stock_data.fifty_low):
                        embed = DiscordEmbed(title=f"{data['symbol']} is Near 52 week Lows! {data['symbol']}", description=f"```py\nThis feed returns tickers trading within 5% of their 52 week high```", color=hex_colors['green'])
                        await build_embed(data['symbol'], embed, near_52_low)    

                    elif stock_data is not None and stock_data.fifty_high == stock_data.web_stock_close:
                        embed = DiscordEmbed(
                            title=f"{data['symbol']} is Pushing 52 week Highs! {data['symbol']}",
                            description=f"```py\nThis feed returns tickers trading within 5% of their 52 week high```",
                            color=hex_colors['red']
                        )
                        await build_embed(data['symbol'], embed, new_52_high)

                    elif stock_data is not None and stock_data.fifty_low == stock_data.web_stock_close:
                        embed = DiscordEmbed(
                            title=f"{data['symbol']} is Pushing 52 week Lows! {data['symbol']}",
                            description=f"```py\nThis feed returns tickers trading within 5% of their 52 week high```",
                            color=hex_colors['green']
                        )
                        await build_embed(data['symbol'], embed, new_52_low)
                    elif stock_data.last_earnings is not None and stock_data.last_earnings == today_str:
                        embed = DiscordEmbed(title=f"Earnings Today!", description=f"```py\n{data['symbol']} has earnings today.```", color=hex_colors['yellow'])
                        await build_embed(data['symbol'], embed, earnings_today)
                    elif stock_data.avg_10d_vol is not None and stock_data.web_stock_vol is not None and float(stock_data.web_stock_vol) >= (float(stock_data.avg_10d_vol) * 1.25):
                        embed = DiscordEmbed(title=f"Above Average Volume - {data['symbol']}", description=f"```py\n{data['symbol']} is currently trading ABOVE average volume.```", color=hex_colors['red'])
                        await build_embed(data['symbol'], embed, above_avg_volume)
                    elif stock_data.avg_10d_vol is not None and stock_data.web_stock_vol is not None and float(stock_data.web_stock_vol) <= (float(stock_data.avg_10d_vol) * 0.75):
                        embed = DiscordEmbed(title=f"Below Average Volume - {data['symbol']}", description=f"```py\n{data['symbol']} is currently trading BELOW average volume.```", color=hex_colors['green'])
                        await build_embed(data['symbol'], embed, below_avg_volume)
                    elif stock_data.last_earnings is not None and stock_data.last_earnings <= seven_days_from_now_str:
                        embed = DiscordEmbed(title=f"Earnings Week!", description=f"```py\nThis feed is returning tickers that have earnings this week. {data['symbol']} is one of them!```", color=hex_colors['blue'])
                        embed.add_embed_field(name=f"Earnings:", value=f"> **{stock_data.last_earnings}**")
                        await build_embed(data['symbol'], embed, earnings_week)


                    if vol_analysis.buyVolume is not None and vol_analysis.totalVolume is not None and vol_analysis.buyVolume >= 0.75 * vol_analysis.totalVolume:
                        embed = DiscordEmbed(title=f"🚀 Accumulation of {data['symbol']} 🚀", description=f"```py\nThis feed is returning tickers with at least 75% of the volume on the day recorded as BUY VOLUME. Accumulation of {data['symbol']}!```", color=hex_colors['green'])
                        await build_embed(data['symbol'], embed, accumulation)
                    elif vol_analysis.sellVolume is not None and vol_analysis.totalVolume is not None and vol_analysis.sellVolume >= 0.75 * vol_analysis.totalVolume:
                        embed = DiscordEmbed(title=f"🔥 FIRE SALE of {data['symbol']} 🔥", description=f"```py\nThis feed is returning tickers with at least 75% of the volume on the day recorded as SELL VOLUME. FIRE SALE of {data['symbol']}!```", color=hex_colors['red'])
                        await build_embed(data['symbol'], embed, fire_sale)



                


                if data['type'] == 'Q':
                    indicator = data['indicator'] if 'indicator' in data else None
                    if 'Redemptions Suspended' in indicator:
                        embed = DiscordEmbed(title=f"Redemptions Suspended - {data['symbol']}", description=f"```py\n{data['symbol']} has flagged the quote condition: REDEMPTIONS SUSPENDED.```\n> **A redemption suspension is a temporary measure whereby investors in a fund are unable to withdraw, or 'redeem' the capital they invested in the fund. The term is mostly associated with hedge funds, which often reserve the right to impose redemption suspensions under certain rare circumstances.**", color=hex_colors['red'])
                        await build_embed(data['symbol'], embed, REDEMPTION_SUSPENSION)



async def send_discord_message(webhook_url, message_data):
        webhook = AsyncDiscordWebhook(webhook_url,content=f"> <@375862240601047070>\n\n> **{str(message_data)}**")
        await webhook.execute()

async def get_rsi_async(ticker, timespan, window, limit):
    tasks = []
    for symbol in ticker:
        task = await poly.get_rsi(symbol=symbol, timespan=timespan, window=window, limit=limit)
        tasks.append(task)

    rsi_results = await asyncio.gather(*tasks)
    return rsi_results
async def process_ticker(tickers):
    while True:
        for i in tickers:
            rsi_hour_task = await get_rsi_async(i, timespan="hour", window=14, limit=1)
            rsi_minute_task = await get_rsi_async(i, timespan="minute", window=14, limit=1)
            rsi_day_task = await get_rsi_async(i, timespan="day", window=14, limit=1)
            rsi_week_task = await get_rsi_async(i, timespan="week", window=14, limit=1)

            rsi_hour, rsi_minute, rsi_day, rsi_week = await asyncio.gather(
                rsi_hour_task, rsi_minute_task, rsi_day_task, rsi_week_task
            )

            
            print(rsi_hour,rsi_day,rsi_week,rsi_minute)
            if rsi_hour is not None and rsi_minute is not None and rsi_day is not None and rsi_week is not None:
                if rsi_minute[0] <= 30:
                    embed = DiscordEmbed(title=f"🐂 Oversold RSI - 1 Min - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsi_minute[0]),2)} on the 1 minute.```", color=hex_colors['green'])
                    embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsi_minute[0]),2)}**\n> 1hour: **{round(float(rsi_hour[0]),2)}**\n> Day: **{round(float(rsi_day[0]),2)}**\n> Week: **{round(float(rsi_week[0]),2)}**")
                    await build_embed(i, embed, OVERSOLD_1MIN)
                if rsi_hour[0] <= 30:
                    embed = DiscordEmbed(title=f"🐂 Oversold RSI - 1 Hour - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsi_hour[0]),2)} on the daily.```", color=hex_colors['green'])
                    embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsi_minute[0]),2)}**\n> 1hour: **{round(float(rsi_hour[0]),2)}**\n> Day: **{round(float(rsi_day[0]),2)}**\n> Week: **{round(float(rsi_week[0]),2)}**")
                    await build_embed(i, embed, OVERSOLD_1HOUR)
                if rsi_day[0] <= 30:
                    embed = DiscordEmbed(title=f"🐂 Oversold RSI - 1 Day - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsi_day[0]),2)} on the hourly.```", color=hex_colors['green'])
                    embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsi_minute[0]),2)}**\n> 1hour: **{round(float(rsi_hour[0]),2)}**\n> Day: **{round(float(rsi_day[0]),2)}**\n> Week: **{round(float(rsi_week[0]),2)}**")
                    await build_embed(i, embed, OVERSOLD_DAY)
                
                if rsi_week[0] <= 30:
                    embed = DiscordEmbed(title=f"🐂 Oversold RSI - 1 Week - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsi_day[0]),2)} on the weekly.```", color=hex_colors['green'])
                    embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsi_minute[0]),2)}**\n> 1hour: **{round(float(rsi_hour[0]),2)}**\n> Day: **{round(float(rsi_day[0]),2)}**\n> Week: **{round(float(rsi_week[0]),2)}**")
                    await build_embed(i, embed, OVERBOUGHT_WEEK)
                if rsi_minute[0] >= 70:
                    embed = DiscordEmbed(title=f"🐻 Overbought RSI - 1 Min - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsi_minute[0]),2)} on the 1 minute.```", color=hex_colors['red'])
                    embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsi_minute[0]),2)}**\n> 1hour: **{round(float(rsi_hour[0]),2)}**\n> Day: **{round(float(rsi_day[0]),2)}**\n> Week: **{round(float(rsi_week[0]),2)}**")
                    await build_embed(i, embed, OVERBOUGHT_1MIN)
                if rsi_hour[0] >= 70:
                    embed = DiscordEmbed(title=f"🐻 Overbought RSI - 1 Hour - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsi_hour[0]),2)} on the hourly.```", color=hex_colors['red'])
                    embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsi_minute[0]),2)}**\n> 1hour: **{round(float(rsi_hour[0]),2)}**\n> Day: **{round(float(rsi_day[0]),2)}**\n> Week: **{round(float(rsi_week[0]),2)}**")
                    await build_embed(i, embed, OVERBOUGHT_1HOUR)
                if rsi_day[0] >= 70:
                    embed = DiscordEmbed(title=f"🐻 Overbought RSI - 1 Day - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsi_day[0]),2)} on the daily.```", color=hex_colors['red'])
                    embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsi_minute[0]),2)}**\n> 1hour: **{round(float(rsi_hour[0]),2)}**\n> Day: **{round(float(rsi_day[0]),2)}**\n> Week: **{round(float(rsi_week[0]),2)}**")
                    await build_embed(i, embed, OVERBOUGHT_DAY)
                if rsi_week[0] >= 70:
                    embed = DiscordEmbed(title=f"🐻 Overbought RSI - 1 Week - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsi_day[0]),2)} on the weekly.```", color=hex_colors['red'])
                    embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsi_minute[0]),2)}**\n> 1hour: **{round(float(rsi_hour[0]),2)}**\n> Day: **{round(float(rsi_day[0]),2)}**\n> Week: **{round(float(rsi_week[0]),2)}**")
                    await build_embed(i, embed, OVERBOUGHT_WEEK)


                if rsi_week[0] <= 30 and rsi_day[0] <= 30 and rsi_hour[0] <= 30:
                    embed = DiscordEmbed(title=f"🐂 SUPER OVERSOLD RSI {i}", description=f"```py\n{i} exhibits SUPER OVERSOLD RSI - With an oversold RSI on the hourly, daily, and weekly timeframes.```", color=hex_colors['green'])
                    embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsi_minute[0]),2)}**\n> 1hour: **{round(float(rsi_hour[0]),2)}**\n> Day: **{round(float(rsi_day[0]),2)}**\n> Week: **{round(float(rsi_week[0]),2)}**")
                    await build_embed(i, embed, SUPER_OVERSOLD)
                
                if rsi_week[0] >= 70 and rsi_day[0] <= 30 and rsi_hour[0] <= 30:
                    embed = DiscordEmbed(title=f"🐻 SUPER OVERBOUGHT RSI {i}", description=f"```py\n{i} exhibits SUPER OVERBOUGHT RSI - With an oversold RSI on the hourly, daily, and weekly timeframes.```", color=hex_colors['red'])
                    embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsi_minute[0]),2)}**\n> 1hour: **{round(float(rsi_hour[0]),2)}**\n> Day: **{round(float(rsi_day[0]),2)}**\n> Week: **{round(float(rsi_week[0]),2)}**")
    
                    await build_embed(i, embed, SUPER_OVERBOUGHT)




symbol_to_sector = {symbol: sector for sector, symbols in market_sectors.items() for symbol in symbols}  
async def handle_msg(market, msgs: WebSocketMessage, queue: Queue):
   

    
    for m in msgs:
        message_data = {}

        if isinstance(m, IndexValue):
            message_data['type'] = 'IndexValue'
            message_data['symbol'] = m.symbol
     
        if isinstance(m, EquityTrade):
            message_data['type'] = 'EquityTrade'
            message_data['symbol'] = m.symbol
            if m.symbol.startswith('O:'):
                message_data['symbol'] = m.symbol
                message_data['type'] = m.event_type
                message_data['exchange'] = OPTIONS_EXCHANGES.get(m.exchange)
                message_data['conditions'] = [options_condition_dict.get(condition) for condition in m.conditions] if m.conditions is not None else []
                message_data['price'] = m.price
                message_data['size'] = m.size
                message_data['timestamp'] = datetime.fromtimestamp(m.timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S')
          
            else:
                message_data['symbol'] = m.symbol
                message_data['type'] = m.event_type
                message_data['conditions'] = [stock_condition_dict.get(condition) for condition in m.conditions] if m.conditions is not None else []
                message_data['exchange'] = STOCK_EXCHANGES.get(m.exchange)
                message_data['price'] = m.price
                message_data['size'] = m.size
                message_data['timestamp'] = datetime.fromtimestamp(m.timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S')
        
        elif isinstance(m, EquityAgg):
            message_data['type'] = m.event_type
            message_data['symbol'] = m.symbol
            message_data['official_open'] = m.official_open_price
            message_data['last_price'] = m.close
            message_data['total_volume'] = m.accumulated_volume
            message_data['volume'] = m.volume
            message_data['day_vwap'] = m.aggregate_vwap
            #message_data['average_size'] = m.average_size
            message_data['otc'] = m.otc
            message_data['start_time'] = datetime.fromtimestamp(m.start_timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S')
            message_data['end_time'] = datetime.fromtimestamp(m.end_timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S') if m.end_timestamp is not None else None
            await queue.put(message_data)

        if isinstance(m, EquityQuote):
            if message_data['symbol'].startswith('O:'):
                message_data['type'] = m.event_type
                message_data['symbol'] = m.symbol
                message_data['ask'] = m.ask_price
                message_data['bid'] = m.bid_price
                message_data['ask_size'] = m.ask_size
                message_data['bid_size'] = m.bid_size
                message_data['timestamp'] = datetime.fromtimestamp(m.timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S')

                message_data['ask_exchange'] = OPTIONS_EXCHANGES.get(m.ask_exchange_id)
                message_data['bid_exchange'] = OPTIONS_EXCHANGES.get(m.bid_exchange_id)
        
            else:
                message_data['symbol'] = m.symbol
                message_data['type'] = m.event_type
                message_data['ask'] = m.ask_price
                message_data['bid'] = m.bid_price
                message_data['indicator'] = [indicators.get(indicator) for indicator in m.indicators] if m.indicators is not None else []
                message_data['condition'] = quote_conditions.get(m.condition)
                message_data['ask_size'] = m.ask_size
                message_data['bid_size'] = m.bid_size
                message_data['tape'] = TAPES.get(m.tape)
                message_data['timestamp'] = datetime.fromtimestamp(m.timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S')

                message_data['ask_exchange'] = STOCK_EXCHANGES.get(m.ask_exchange_id)
                message_data['bid_exchange'] = STOCK_EXCHANGES.get(m.bid_exchange_id)
        await queue.put(message_data)





        
 

from bot.get_stuff import news_main


async def main():
    data_queue = Queue()

    # Create tasks for websocket connections
    markets = [Market.Stocks, Market.Options]
    connection_tasks = [
        asyncio.create_task(
            WebSocketClient(subscriptions=["T.*,Q.*,A.*"], api_key=YOUR_API_KEY, market=market).connect(
                lambda msg: asyncio.create_task(handle_msg(market, msg, data_queue))
            )
        )
        for market in markets
    ]

    # Create tasks for consuming data
    consume_tasks = await consume(data_queue)

    # Create task for news processing
    #news_task = asyncio.create_task(news_main())

    # Wait for all tasks to complete
    await asyncio.gather(*connection_tasks, consume_tasks)

asyncio.run(main())