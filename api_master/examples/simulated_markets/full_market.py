#TODO: Clean imports (lol)

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from cfg import UNUSUAL_OPTIONS
from datetime import datetime
from sdks.polygon_sdk.masterSDK import MasterSDK
from sdks.helpers.helpers import human_readable
from helpers import convert_exchanges_and_conditions_options
from cfg import stockQuoteConditionsDictionary,spx100calls,spx100puts, indicatorsDictionary, optvol_100kplus,optvol_20to50k,optvol_5k10k
from cfg import YOUR_API_KEY
from cfg import zero_dte
from sdks.polygon_sdk.list_sets import OPTIONS_EXCHANGES,sublist1, options_condition_dict
import asyncio
from cfg import OVERSOLD_1HOUR,OVERBOUGHT_1HOUR,OVERBOUGHT_1MIN,OVERBOUGHT_DAY,OVERSOLD_1MIN,OVERSOLD_DAY, OVERBOUGHT_WEEK,OVERSOLD_WEEK, SUPER_OVERBOUGHT,SUPER_OVERSOLD
from collections import defaultdict
from news_processor import news_main
from discord_webhook import AsyncDiscordWebhook, DiscordEmbed
from cfg import hex_colors
from cfg import vol1k_to5k,vol500_to1k,vol5k_to10k,vol_10kplus,squeeze_potential,near_52_high,near_52_low,new_52_high,new_52_low,accumulation,fire_sale
from cfg import earnings_today,earnings_week, seven_days_from_now_str,above_avg_volume,below_avg_volume,today_str
from polygon_enhanced.polygon_enhanced import WebSocketClient

from sdks.polygon_sdk.list_sets import stock_condition_dict, STOCK_EXCHANGES, quote_conditions, indicators, market_sectors
from asyncio import Queue
from pymongo import MongoClient
from sdks.helpers.helpers import build_embed,build_option_embed
from polygon.websocket import WebSocketMessage
from polygon import WebSocketClient
from polygon_enhanced.polygon_enhanced.websocket.models import EquityAgg,EquityQuote,EquityTrade, Market, WebSocketMessage
from sdks.polygon_sdk.technical_conditions import check_macd_condition_bearish,check_macd_condition_bullish,check_rsi_condition_bearish,check_rsi_condition_bullish
import random

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import upside_day,upside_scalps,downside_day,downside_scalps
from cfg import YOUR_API_KEY
import asyncio
from sdks.polygon_sdk.list_sets import sublist1
from sdks.polygon_sdk.list_sets import OPTIONS_EXCHANGES, STOCK_EXCHANGES, option_condition_dict, stock_condition_dict
from cfg import spycalls,spyputs
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
webull = AsyncWebullSDK()
poly = AsyncPolygonSDK(YOUR_API_KEY)
master = MasterSDK()
# Create a cache dictionary for Webull data
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

async def check_all_macd_rsi_conditions(i):

    tasks = [
                poly.get_macd(i, timespan="hour"),
                poly.get_rsi(i, timespan="hour"),
                poly.get_macd(i, timespan="day"),
                poly.get_rsi(i, timespan="day"),
                poly.get_rsi(i, timespan="minute"),
                poly.get_rsi(i, timespan="week"),
            ]

            # Use asyncio.gather to run the tasks concurrently
    histh, rsih, histd, rsid, rsim, rsiw = await asyncio.gather(*tasks)
    tasks2 = [
                    check_macd_condition_bullish(histh),
                    check_rsi_condition_bullish(rsih),
                    check_macd_condition_bearish(histh),
                    check_rsi_condition_bearish(rsih),
                    check_macd_condition_bullish(histd),
                    check_rsi_condition_bullish(rsid),
                    check_macd_condition_bearish(histd),
                    check_rsi_condition_bearish(rsid),
                    check_rsi_condition_bearish(rsim),
                    check_rsi_condition_bullish(rsim),
                ]

    check_bull_macdh, check_bull_rsih, check_bear_macdh, check_bear_rsih, check_bull_macdd, check_bull_rsid, check_bear_macdd, check_bear_rsid, check_bear_rsim, check_bull_rsim = await asyncio.gather(*tasks2)

    return check_bull_macdh, check_bull_rsih, check_bear_macdh, check_bear_rsih, check_bull_macdd, check_bull_rsid, check_bear_macdd, check_bear_rsid, check_bear_rsim, check_bull_rsim,histh, rsih, histd, rsid, rsim, rsiw




async def process_ticker():

    while True:
        i = random.choice(sublist1)

   
        check_bull_macdh, check_bull_rsih, check_bear_macdh, check_bear_rsih, check_bull_macdd, check_bull_rsid, check_bear_macdd, check_bear_rsid, check_bear_rsim, check_bull_rsim,histh, rsih, histd, rsid, rsim, rsiw = await asyncio.create_task(check_all_macd_rsi_conditions(i))


        # Now run the check conditions concurrently
        

        description = "```py\nThe '💫Momentum💫 Scalps' channel highlights stocks with high potential for swift price changes by utilizing the oversold / overbought RSI combined with an iminent MACD Cross.```"
        if check_bull_rsih is True and check_bull_macdh is True:


    
            embed = DiscordEmbed(title=f"Upside 💫Momentum💫 Scalps - HOUR", description=f"```py\nThe 'Upside 💫Momentum💫 Scalps' channel highlights stocks with high potential for swift price changes. These stocks are pre-filtered by market cap and evaluated based on key indicators: the Relative Strength Index (RSI) and the Moving Average Convergence Divergence (MACD) cross. The RSI indicates whether a stock is overbought or oversold, while a MACD cross suggests a potential price movement trend. This makes these stocks prime for quick 'scalp' trades, although any trading strategy should be approached with careful analysis and risk management.```", color=hex_colors['green'])


    
    
            embed.set_footer(text=f"{i}")
            embed.add_embed_field(name=f"Before Jumping in:", value=f"> **NFA**\n> ✅ Check the spread\n> ✅ Look for a CALL IV skew as a bonus\n> ❓ (*the lowest IV would be at a strike ABOVE the current price*)\n> ✅ Verify technicals (🐂 macd cross, oversold RSI)")
            
            
            
            asyncio.create_task(build_embed(i, embed, upside_scalps))
        if check_bear_rsih is True and check_bear_macdh is True:
        
            embed = DiscordEmbed(title=f"Downside💫Scalps - HOUR - {i}", description=description, color=hex_colors['red'])

            embed.add_embed_field(name=f"Before Jumping in:", value=f"> **NFA**\n> ✅ Check the spread\n> ✅ Look for a PUT IV skew as a bonus\n> ❓ (*the lowest IV would be at a strike BELOW the current price*)\n> ✅ Verify technicals (🐻 macd cross, overbought RSI)")
        
            asyncio.create_task(build_embed(i, embed, downside_scalps))

        if check_bull_rsid is True and check_bull_macdd is True:
            embed = DiscordEmbed(title=f"Upside💫 Scalps - DAILY - {i}", description=description, color=hex_colors['green'])



            embed.add_embed_field(name=f"Before Jumping in:", value=f"> **NFA**\n> ✅ Check the spread\n> ✅ Look for a CALL IV skew as a bonus\n> ❓ (*the lowest IV would be at a strike ABOVE the current price*)\n> ✅ Verify technicals (🐂 macd cross, oversold RSI)")
            
            asyncio.create_task(build_embed(i, embed, upside_day))
        
        

        if check_bear_rsid is True and check_bear_macdd is True:

            embed = DiscordEmbed(title=f"Downside💫 Scalps - DAILY - {i}", description=description, color=hex_colors['red'])
        
    

            embed.set_footer(text="🔴 AT THE MONEY PUTS - 2-3+ WEEKS OUT! EXPLOIT THE MOMENTUM")
            embed.add_embed_field(name=f"Before Jumping in:", value=f"> **NFA**\n> ✅ Check the spread\n> ✅ Look for an PUT IV skew as a bonus\n> ❓ (*the lowest IV would be at a strike BELOW the current price*)\n> ✅ Verify technicals (🐻 macd cross, overbought RSI)")

            asyncio.create_task(build_embed(i, embed, downside_day))
    
        

        if check_bear_rsid is True and check_bear_macdd is True:
            embed = DiscordEmbed(title=f"Downside💫 Scalps - DAILY - {i}", description=description, color=hex_colors['red'])

            embed.set_footer(text="🔴 AT THE MONEY PUTS - 2-3+ WEEKS OUT! EXPLOIT THE MOMENTUM")
            embed.add_embed_field(name=f"Before Jumping in:", value=f"> **NFA**\n> ✅ Check the spread\n> ✅ Look for an PUT IV skew as a bonus\n> ❓ (*the lowest IV would be at a strike BELOW the current price*)\n> ✅ Verify technicals (🐻 macd cross, overbought RSI)")

            asyncio.create_task(build_embed(i, embed, downside_day))

    

        if check_bear_rsim is True:
        
            embed = DiscordEmbed(title=f"Minute-RSI Scan", description=f"```py\nScanner picked up an overbought minute RSI for {i}```", color=hex_colors['red'])
            embed.set_footer(text="🔴 Overbought - 1 Minute")

            asyncio.create_task(build_embed(i, embed, OVERSOLD_1MIN))


        if check_bull_rsim is True:

            embed = DiscordEmbed(title=f"Minute-RSI Scan", description=f"```py\nScanner picked up an overbought minute RSI for {i}```", color=hex_colors['red'])
            embed.set_footer(text="🟢 Oversold - 1 Minute")

            asyncio.create_task(build_embed(i, embed, ""))





        if rsih is not None and rsim is not None and rsid is not None and rsiw is not None:
            if rsim[0] <= 30:
                embed = DiscordEmbed(title=f"🐂 Oversold RSI - 1 Min - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsim[0]),2)} on the 1 minute.```", color=hex_colors['green'])
                embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsim[0]),2)}**\n> 1hour: **{round(float(rsih[0]),2)}**\n> Day: **{round(float(rsid[0]),2)}**\n> Week: **{round(float(rsiw[0]),2)}**")
                asyncio.create_task(build_embed(i, embed, OVERSOLD_1MIN))
            if rsih[0] <= 30:
                embed = DiscordEmbed(title=f"🐂 Oversold RSI - 1 Hour - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsih[0]),2)} on the daily.```", color=hex_colors['green'])
                embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsim[0]),2)}**\n> 1hour: **{round(float(rsih[0]),2)}**\n> Day: **{round(float(rsid[0]),2)}**\n> Week: **{round(float(rsiw[0]),2)}**")
                asyncio.create_task(build_embed(i, embed, OVERSOLD_1HOUR))
            if rsid[0] <= 30:
                embed = DiscordEmbed(title=f"🐂 Oversold RSI - 1 Day - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsid[0]),2)} on the hourly.```", color=hex_colors['green'])
                embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsim[0]),2)}**\n> 1hour: **{round(float(rsih[0]),2)}**\n> Day: **{round(float(rsid[0]),2)}**\n> Week: **{round(float(rsiw[0]),2)}**")
                asyncio.create_task(build_embed(i, embed, OVERSOLD_DAY))

            if rsid[0] <= 30:
                embed = DiscordEmbed(title=f"🐂 Oversold RSI - 1 Week - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsid[0]),2)} on the hourly.```", color=hex_colors['green'])
                embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsim[0]),2)}**\n> 1hour: **{round(float(rsih[0]),2)}**\n> Day: **{round(float(rsid[0]),2)}**\n> Week: **{round(float(rsiw[0]),2)}**")
                asyncio.create_task(build_embed(i, embed, OVERSOLD_WEEK))
            
            if rsiw[0] <= 30:
                embed = DiscordEmbed(title=f"🐂 Oversold RSI - 1 Week - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsid[0]),2)} on the weekly.```", color=hex_colors['green'])
                embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsim[0]),2)}**\n> 1hour: **{round(float(rsih[0]),2)}**\n> Day: **{round(float(rsid[0]),2)}**\n> Week: **{round(float(rsiw[0]),2)}**")
                asyncio.create_task(build_embed(i, embed, OVERBOUGHT_WEEK))
            if rsim[0] >= 70:
                embed = DiscordEmbed(title=f"🐻 Overbought RSI - 1 Min - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsim[0]),2)} on the 1 minute.```", color=hex_colors['red'])
                embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsim[0]),2)}**\n> 1hour: **{round(float(rsih[0]),2)}**\n> Day: **{round(float(rsid[0]),2)}**\n> Week: **{round(float(rsiw[0]),2)}**")
                asyncio.create_task(build_embed(i, embed, OVERBOUGHT_1MIN))
            if rsih[0] >= 70:
                embed = DiscordEmbed(title=f"🐻 Overbought RSI - 1 Hour - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsih[0]),2)} on the hourly.```", color=hex_colors['red'])
                embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsim[0]),2)}**\n> 1hour: **{round(float(rsih[0]),2)}**\n> Day: **{round(float(rsid[0]),2)}**\n> Week: **{round(float(rsiw[0]),2)}**")
                asyncio.create_task(build_embed(i, embed, OVERBOUGHT_1HOUR))
            if rsid[0] >= 70:
                embed = DiscordEmbed(title=f"🐻 Overbought RSI - 1 Day - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsid[0]),2)} on the daily.```", color=hex_colors['red'])
                embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsim[0]),2)}**\n> 1hour: **{round(float(rsih[0]),2)}**\n> Day: **{round(float(rsid[0]),2)}**\n> Week: **{round(float(rsiw[0]),2)}**")
                asyncio.create_task(build_embed(i, embed, OVERBOUGHT_DAY))
            if rsiw[0] >= 70:
                embed = DiscordEmbed(title=f"🐻 Overbought RSI - 1 Week - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsid[0]),2)} on the weekly.```", color=hex_colors['red'])
                embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsim[0]),2)}**\n> 1hour: **{round(float(rsih[0]),2)}**\n> Day: **{round(float(rsid[0]),2)}**\n> Week: **{round(float(rsiw[0]),2)}**")
                asyncio.create_task(build_embed(i, embed, OVERBOUGHT_WEEK))


            if rsiw[0] <= 30 and rsid[0] <= 30 and rsih[0] <= 30:
                embed = DiscordEmbed(title=f"🐂 SUPER OVERSOLD RSI {i}", description=f"```py\n{i} exhibits SUPER OVERSOLD RSI - With an oversold RSI on the hourly, daily, and weekly timeframes.```", color=hex_colors['green'])
                embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsim[0]),2)}**\n> 1hour: **{round(float(rsih[0]),2)}**\n> Day: **{round(float(rsid[0]),2)}**\n> Week: **{round(float(rsiw[0]),2)}**")
                asyncio.create_task(await build_embed(i, embed, SUPER_OVERSOLD))
            
            if rsiw[0] >= 65 and rsid[0] >=65 and rsih[0] >=65:
                embed = DiscordEmbed(title=f"🐻 SUPER OVERBOUGHT RSI {i}", description=f"```py\n{i} exhibits SUPER OVERBOUGHT RSI - With an oversold RSI on the hourly, daily, and weekly timeframes.```", color=hex_colors['red'])
                embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsim[0]),2)}**\n> 1hour: **{round(float(rsih[0]),2)}**\n> Day: **{round(float(rsid[0]),2)}**\n> Week: **{round(float(rsiw[0]),2)}**")

                asyncio.create_task(build_embed(i, embed, SUPER_OVERBOUGHT))




async def send_discord_message_with_embed(webhook_url, embed):
    webhook = AsyncDiscordWebhook(webhook_url,content=f"> <@375862240601047070>",rate_limit_retry=True)
    webhook.add_embed(embed)
    await webhook.execute()



async def send_discord_message(webhook_url, message_data):
    webhook = AsyncDiscordWebhook(webhook_url,content=f"> <@375862240601047070>\n\n> **{str(message_data)}**",rate_limit_retry=True)
    await webhook.execute()



symbol_to_sector = {symbol: sector for sector, symbols in market_sectors.items() for symbol in symbols}  
# Define the handle_queue function to process incoming messages from the WebSocket
async def handle_queue(msgs: WebSocketMessage,queue: Queue):
    message_data = {}
    stock_trade_send_tasks=[]
    option_trade_send_tasks=[]
    for m in msgs:
        
        if m.symbol.startswith('O:') and any(m.symbol.replace('O:', '').startswith(ticker) for ticker in sublist1):
            if m.event_type == 'A':
                message_data['event_type'] == 'optionAgg' if 'optionAgg' in message_data else None
                message_data['symbol'] = m.symbol
                message_data['officialOpen'] = m.official_open_price
                message_data['lastPrice'] = m.close
                message_data['accumulatedVolume'] = m.accumulated_volume
                message_data['vwapPrice'] = m.vwap
                message_data['volume'] = m.volume
                message_data['timestamp'] = datetime.fromtimestamp(m.end_timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S') if m.end_timestamp is not None else None

            elif m.event_type == 'T':
                message_data['event_type'] = 'optionTrade'
                message_data['symbol'] = m.symbol
                message_data['price'] = m.price
                message_data['size'] = m.size
                message_data['exchange'] = OPTIONS_EXCHANGES.get(m.exchange)
                message_data['conditions'] = [options_condition_dict.get(condition) for condition in m.conditions]
                message_data['timestamp'] = datetime.fromtimestamp(m.trf_timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S') if m.trf_timestamp is not None else None

                
                # exchange_discord_webhook_urls = options_exchange_hooks.get(m.exchange)
                # conditions = [options_condition_dict.get(condition) for condition in m.conditions]
                # exchange = OPTIONS_EXCHANGES.get(m.exchange)
                # for condition in conditions:
                #     webhook_url = optionConditionsDict[condition]
                #     task = asyncio.create_task(send_discord_message(webhook_url, m))
                #     option_trade_send_tasks.append(task)

                # exchange_discord_webhook_urls = options_exchange_hooks[exchange]
                # if exchange_discord_webhook_urls is not None:
                #     # Create a task for sending the message and add it to the list
                #     task = asyncio.create_task(send_discord_message(exchange_discord_webhook_urls, m))
                #     option_trade_send_tasks.append(task)



            elif m.event_type == 'Q':
                message_data['event_type'] = 'optionQuote'
                message_data['symbol'] = m.symbol
                message_data['askExchange'] = OPTIONS_EXCHANGES.get(m.ask_exchange_id)
                message_data['bidExchange'] = OPTIONS_EXCHANGES.get(m.bid_exchange_id)
                message_data['ask'] = m.ask_price
                message_data['askSize'] = m.ask_size
                message_data['bid'] = m.bid_price
                message_data['bidSize'] = m.bid_size
        


        if m.symbol in sublist1 and 'O:' not in m.symbol:

            if m.event_type == 'A':

                message_data['event_type'] = 'stockAgg'
                message_data['symbol'] = m.symbol
                message_data['officialOpen'] = m.official_open_price
                message_data['lastPrice'] = m.close
                message_data['accumulatedVolume'] = m.accumulated_volume
        
                message_data['vwapPrice'] = m.vwap
                message_data['volume'] = m.volume
                message_data['timestamp'] = datetime.fromtimestamp(m.end_timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S') if m.end_timestamp is not None else None


            elif m.event_type == 'T':
                message_data['event_type'] = 'stockTrade'
                message_data['symbol'] = m.symbol
                message_data['price'] = m.price
                message_data['size'] = m.size
                message_data['exchange'] = STOCK_EXCHANGES.get(m.exchange)
                message_data['conditions'] = [stock_condition_dict.get(condition) for condition in m.conditions] if m.conditions is not None else []
                message_data['timestamp'] = datetime.fromtimestamp(m.trf_timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S') if m.trf_timestamp is not None else None

                
                exchange_discord_webhook_urls = STOCK_EXCHANGES.get(m.exchange)
                conditions = [stock_condition_dict.get(condition) for condition in m.conditions] if m.conditions is not None else []
                exchange = STOCK_EXCHANGES.get(m.exchange)
                # for condition in conditions:
                #     webhook_url = stockConditionsDictionary[condition]
                #     task = asyncio.create_task(send_discord_message(webhook_url, m))
                #     stock_trade_send_tasks.append(task)


                # if exchange is not None:
                #     if exchange in stockExchangeDictionary:
                #         exchange_discord_webhook_urls = stockExchangeDictionary[exchange]
                #     # Create a task for sending the message and add it to the list
                #     task = asyncio.create_task(send_discord_message(exchange_discord_webhook_urls, m))
                #     stock_trade_send_tasks.append(task)


            elif m.event_type == 'Q':
                message_data['event_type'] = 'stockQuote'
                message_data['symbol'] = m.symbol
                message_data['askExchange'] = STOCK_EXCHANGES.get(m.ask_exchange_id)
                message_data['bidExchange'] = STOCK_EXCHANGES.get(m.bid_exchange_id)
                message_data['condition'] = quote_conditions.get(m.condition)
                message_data['indicator'] = [indicators.get(i) for i in m.indicators] if m.indicators is not None else []
                message_data['ask'] = m.ask_price
                message_data['askSize'] = m.ask_size
                message_data['bid'] = m.bid_price
                message_data['bidSize'] = m.bid_size


        if message_data is not None and 'event_type' in message_data:
            await queue.put(message_data)

symbol_to_sector = {symbol: sector for sector, symbols in market_sectors.items() for symbol in symbols}  
async def handle_stocks_msg(queue: asyncio.Queue):
    while True:
        data = await queue.get()
        if data is not None and data is not {}:
            if data['event_type'] == 'optionTrade':
                option_trade_send_tasks=[]






                if "C0" in data['symbol'] and str(data['symbol']).startswith('SPX'):
                    callhook = AsyncDiscordWebhook(spx100calls, content="<@375862240601047070>",rate_limit_retry=True)
                    embed = DiscordEmbed(title=f"{human_readable(data['symbol'])}",
                                        description=f"> Size: **{data['size']}**\n> Price: **${data['price']}**\n\n> Condition: **{data['conditions']}**\n> Exchange: **{data['exchange']}**", color=hex_colors['green'])
                    embed.set_timestamp()
                    embed.set_footer(text=f"{data['symbol']}")
                    callhook.add_embed(embed)
                    option_trade_send_tasks.append(asyncio.create_task(callhook.execute()))




                elif "P0" in data['symbol'] and str(data['symbol']).startswith("O:SPX"):
                    puthook = AsyncDiscordWebhook(spx100puts, content="<@375862240601047070>")
                    embed = DiscordEmbed(title=f"{human_readable(data['symbol'])}",
                                        description=f"> Size: **{data['size']}**\n> Price: **${data['price']}**\n\n> Condition: **{data['conditions']}**\n> Exchange: **{data['exchange']}**", color=hex_colors['red'])
                    embed.set_timestamp()
                    embed.set_footer(text=f"{data['symbol']}")
                    puthook.add_embed(embed)
                    option_trade_send_tasks.append(asyncio.create_task(puthook.execute()))



                if "C0" in data['symbol'] and str(data['symbol']).startswith("O:SPY"):
                    callhook = AsyncDiscordWebhook(spycalls, content="<@375862240601047070>")
                    embed = DiscordEmbed(title=f"{human_readable(data['symbol'])}",
                                        description=f"> Size: **{data['size']}**\n> Price: **${data['price']}**\n\n> Condition: **{data['conditions']}**\n> Exchange: **{data['exchange']}**", color=hex_colors['green'])
                    embed.set_timestamp()
                    embed.set_footer(text=f"{data['symbol']}")
                    callhook.add_embed(embed)
                    option_trade_send_tasks.append(asyncio.create_task(callhook.execute()))
                


                elif "P0" in data['symbol'] and str(data['symbol']).startswith("O:SPY"):
                    puthook = AsyncDiscordWebhook(spyputs, content="<@375862240601047070>")
                    embed = DiscordEmbed(title=f"{human_readable(data['symbol'])}",
                                        description=f"> Size: **{data['size']}**\n> Price: **${data['price']}**\n\n> Condition: **{data['conditions']}**\n> Exchange: **{data['exchange']}**", color=hex_colors['red'])
                    embed.set_timestamp()
                    embed.set_footer(text=f"{data['symbol']}")
                    puthook.add_embed(embed)
                    option_trade_send_tasks.append(asyncio.create_task(puthook.execute()))


                elif today_str_yymmdd in data['symbol']:
                    hook = AsyncDiscordWebhook(zero_dte, content="<@375862240601047070>")
                    embed = DiscordEmbed(title=f"0dte Trades - {human_readable(data['symbol'])}", description=f"```py\nThis feeds returns 0dte option trades across the market.```", color=hex_colors['teal'])
                    embed.add_embed_field(name=f"Last Trade:", value=f"> Trade Size: **{float(data['size']):,}**\n> Price: **${data['price']}**")
                    embed.add_embed_field(name=f"Details:", value=f"> Exchange: **{data['exchange']}**\n> Conditions: **{data['conditions']}**")
                    embed.set_footer(text=f"{data['symbol']} | Data Provided by Polygon.io")
                    hook.add_embed(embed)
                    option_trade_send_tasks.append(asyncio.create_task(hook.execute()))
                await asyncio.gather(*option_trade_send_tasks)


            elif data['event_type'] == "optionAgg" and data['volume']>= 100:

                option_agg_tasks = []

                if data['accumulated_volume'] is not None and data['accumulated_volume'] >= 500 and data['accumulated_volume'] <= 999:
                    embed= DiscordEmbed(title=f"Trade - 500 to 1k Volume", description=f"```py\n{data['symbol']} just traded for a size of {data['volume']} at a price of ${data['close']}```\n\nThe total volume on the day for {human_readable(data['symbol'])} is **{float(data['accumulated_volume']):,}**")
                    option_agg_tasks.append(asyncio.create_task(build_option_embed(data['symbol'], embed, optvol_5k10k)))
                elif data['accumulated_volume'] is not None and data['accumulated_volume'] >= 1000 and data['accumulated_volume'] <= 4999:
                    embed= DiscordEmbed(title=f"Trade - 1k to 5k Volume", description=f"```py\n{data['symbol']} just traded for a size of {data['volume']} at a price of ${data['close']}```\n\nThe total volume on the day for {human_readable(data['symbol'])} is **{float(data['accumulated_volume']):,}**")
                    option_agg_tasks.append(asyncio.create_task(build_option_embed(data['symbol'], embed, optvol_5k10k)))

                elif data['accumulated_volume'] is not None and data['accumulated_volume'] >= 5000 and data['accumulated_volume'] <= 9999:
                    embed= DiscordEmbed(title=f"Trade - 5k to 10k Volume", description=f"```py\n{data['symbol']} just traded for a size of {data['volume']} at a price of ${data['close']}```\n\nThe total volume on the day for {human_readable(data['symbol'])} is **{float(data['accumulated_volume']):,}**")
                    option_agg_tasks.append(asyncio.create_task(build_option_embed(data['symbol'], embed, optvol_20to50k)))

                elif data['accumulated_volume'] is not None and data['accumulated_volume'] >= 10000:
                    embed= DiscordEmbed(title=f"Trade - 10k Plus Volume", description=f"```py\n{data['symbol']} just traded for a size of {data['volume']} at a price of ${data['close']}```\n\nThe total volume on the day for {human_readable(data['symbol'])} is **{float(data['accumulated_volume']):,}**")
                    option_agg_tasks.append(asyncio.create_task(build_option_embed(data['symbol'], embed, optvol_100kplus)))
                

                snapshot_data = await master.get_universal_snapshot(data['symbol'])
                underlying_ticker=  snapshot_data.underlying_ticker
                underlying_price = snapshot_data.underlying_price
                volume = snapshot_data.volume
                oi = snapshot_data.open_interest
                rsi_snapshot = await poly.rsi_snapshot(underlying_ticker)
                if volume is not None and oi is not None and float(volume) > float(oi):
                    
                    embed = DiscordEmbed(title=f"Unusual Option Trade", description=f"```py\nThis feed is returning live unusual option trades. An unusual option trade is one where the volume exceeds the open interest.```\n> **TICKER:**\n\n**{human_readable(data['symbol'])}```")
                    embed.add_embed_field(name=f"Underlying Price:", value=f"> **${underlying_price}**", inline=False)
                    embed.add_embed_field(name=f"Contract Stats:", value=f"> Open: **${snapshot_data.open}**\n> High: **${snapshot_data.high}**\n> Low: **${snapshot_data.low}**\n> Last: **{snapshot_data.close}**\n> Change%: **{round(float(snapshot_data.change_percent),2)}**")
                    embed.add_embed_field(name=f"Greeks:", value=f"> Delta: **{round(float(snapshot_data.delta),2)}**\n> Gamma: **{round(float(snapshot_data.gamma),2)}**\n> Theta: **{round(float(snapshot_data.theta),2)}**\n> Vega: **{round(float(snapshot_data.vega),2)}**")
                    embed.add_embed_field(name=f"OI & VOl:", value=f"> OI: **{float(oi):,}**\n> VOL: **{float(volume):,}**")
                    embed.add_embed_field(name=f"Last Trade:", value=f"> Size: **{snapshot_data.trade_size}**\n> Price: **{snapshot_data.trade_price}**\n> Condition: **{snapshot_data.conditions}**\n> Exchange: **{snapshot_data.exchange}**")
                    embed.add_embed_field(name=f"Last Quote:", value=f"> Bid: **${snapshot_data.bid}**\n> Bid Size: **{snapshot_data.bid_size}**\n> Ask: **${snapshot_data.ask}**\n> Ask Size: **{snapshot_data.ask_size}**\n> Mid: **${snapshot_data.midpoint}**")
                    embed.add_embed_field(name=f"IV:", value=f"> **{round(float(snapshot_data.implied_volatility)*100,2)}%**")
                    embed.add_embed_field(name=f"RSI Snapshot:", value=f"```{rsi_snapshot}```")
                    embed.set_thumbnail(await poly.get_polygon_logo(underlying_ticker))
                    await send_discord_message_with_embed(UNUSUAL_OPTIONS, embed)
                    

                await asyncio.gather(*option_agg_tasks)
            elif data['event_type'] == 'stockTrade':



                if data['size'] is not None and data['size'] >= 500 and data['size'] <= 999:
                    embed= DiscordEmbed(title=f"Trade - 500 to 1k Volume", description=f"```py\n{data['symbol']} just traded for a size of {data['size']} at a price of ${data['size']}```")
                    asyncio.create_task(build_embed(data['symbol'], embed, vol500_to1k))
                elif data['size'] is not None and data['size'] >= 1000 and data['size'] <= 4999:
                    embed= DiscordEmbed(title=f"Trade - 1k to 5k Volume", description=f"```py\n{data['symbol']} just traded for a size of {data['size']} at a price of ${data['size']}```")
                    asyncio.create_task(build_embed(data['symbol'], embed, vol1k_to5k))

                elif data['size'] is not None and data['size'] >= 5000 and data['size'] <= 9999:
                    embed= DiscordEmbed(title=f"Trade - 5k to 10k Volume", description=f"```py\n{data['symbol']} just traded for a size of {data['size']} at a price of ${data['size']}```")
                    asyncio.create_task(build_embed(data['symbol'], embed, vol5k_to10k))

                elif data['size'] is not None and data['size'] >= 10000:
                    embed= DiscordEmbed(title=f"Trade - 10k Plus Volume", description=f"```py\n{data['symbol']} just traded for a size of {data['size']} at a price of ${data['size']}```")
                    asyncio.create_task(build_embed(data['symbol'], embed, vol_10kplus))
                volume_analysis_task = asyncio.create_task(webull.get_webull_vol_analysis_data(data['symbol']))
                stock_data_task = asyncio.create_task(webull.get_webull_stock_data(data['symbol']))
                short_interest_task = asyncio.create_task(webull.get_short_interest(data['symbol']))

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

                if short_percentage_of_float >= 25 and stock_data is not None and stock_data.avg_10d_vol is not None and stock_data.web_stock_vol is not None and float(stock_data.web_stock_vol) <= (float(stock_data.avg_10d_vol)):
                    embed = DiscordEmbed(title=f"Squeeze Potential - {data['symbol']}", description=f"```py\nThis feed returns tickers exhibiting signs of a potential squeeze. Short interest % of float > 25 - volume is below average.```", color=hex_colors['green'])
                    asyncio.create_task(build_embed(data['symbol'], embed, squeeze_potential))
    
                elif stock_data is not None and stock_data.web_stock_close is not None and stock_data.fifty_high is not None and float(stock_data.web_stock_close) > 0.95 * float(stock_data.fifty_high):
                    embed = DiscordEmbed(title=f"{data['symbol']} is Near 52 week Highs! {data['symbol']}", description=f"```py\nThis feed returns tickers trading within 5% of their 52 week high```", color=hex_colors['red'])
                    asyncio.create_task(build_embed(data['symbol'], embed, near_52_high))

                elif stock_data is not None and stock_data.web_stock_close is not None and stock_data.fifty_low is not None and float(stock_data.web_stock_close) < 0.05 * float(stock_data.fifty_low):
                    embed = DiscordEmbed(title=f"{data['symbol']} is Near 52 week Lows! {data['symbol']}", description=f"```py\nThis feed returns tickers trading within 5% of their 52 week high```", color=hex_colors['green'])
                    asyncio.create_task(build_embed(data['symbol'], embed, near_52_low))

                elif stock_data is not None and stock_data.fifty_high == stock_data.web_stock_close:
                    embed = DiscordEmbed(title=f"{data['symbol']} is Pushing 52 week Highs! {data['symbol']}", description=f"```py\nThis feed returns tickers trading within 5% of their 52 week high```", color=hex_colors['red'])
                    asyncio.create_task(build_embed(data['symbol'], embed, new_52_high))

                elif stock_data is not None and stock_data.fifty_low == stock_data.web_stock_close:
                    embed = DiscordEmbed(title=f"{data['symbol']} is Pushing 52 week Lows! {data['symbol']}", description=f"```py\nThis feed returns tickers trading within 5% of their 52 week high```", color=hex_colors['green'])
                    asyncio.create_task(build_embed(data['symbol'], embed, new_52_low))


                if vol_analysis.buyVolume is not None and vol_analysis.totalVolume is not None and vol_analysis.buyVolume >= 0.75 * vol_analysis.totalVolume:
                    embed = DiscordEmbed(title=f"🚀 Accumulation of {data['symbol']} 🚀", description=f"```py\nThis feed is returning tickers with at least 75% of the volume on the day recorded as BUY VOLUME. Accumulation of {data['symbol']}!```", color=hex_colors['green'])
                    asyncio.create_task(build_embed(data['symbol'], embed, accumulation))
                if vol_analysis.sellVolume is not None and vol_analysis.totalVolume is not None and vol_analysis.sellVolume >= 0.75 * vol_analysis.totalVolume:
                    embed = DiscordEmbed(title=f"🔥 FIRE SALE of {data['symbol']} 🔥", description=f"```py\nThis feed is returning tickers with at least 75% of the volume on the day recorded as SELL VOLUME. FIRE SALE of {data['symbol']}!```", color=hex_colors['red'])
                    asyncio.create_task(build_embed(data['symbol'], embed, fire_sale))

                if stock_data.last_earnings is not None and stock_data.last_earnings == today_str:
                    embed = DiscordEmbed(title=f"Earnings Today!", description=f"```py\n{data['symbol']} has earnings today.```", color=hex_colors['yellow'])
                    asyncio.create_task(build_embed(data['symbol'], embed, earnings_today))

                elif stock_data.last_earnings is not None and stock_data.last_earnings <= seven_days_from_now_str:
                    embed = DiscordEmbed(title=f"Earnings Week!", description=f"```py\nThis feed is returning tickers that have earnings this week. {data['symbol']} is one of them!```", color=hex_colors['blue'])
                    embed.add_embed_field(name=f"Earnings:", value=f"> **{stock_data.last_earnings}**")
                    asyncio.create_task(build_embed(data['symbol'], embed, earnings_week))###


                if stock_data.avg_10d_vol is not None and stock_data.web_stock_vol is not None and float(stock_data.web_stock_vol) >= (float(stock_data.avg_10d_vol) * 1.25):
                    embed = DiscordEmbed(title=f"Above Average Volume - {data['symbol']}", description=f"```py\n{data['symbol']} is currently trading ABOVE average volume.```", color=hex_colors['red'])
                    asyncio.create_task(build_embed(data['symbol'], embed, above_avg_volume))

                elif stock_data.avg_10d_vol is not None and stock_data.web_stock_vol is not None and float(stock_data.web_stock_vol) <= (float(stock_data.avg_10d_vol) * 0.75):
                    embed = DiscordEmbed(title=f"Below Average Volume - {data['symbol']}", description=f"```py\n{data['symbol']} is currently trading BELOW average volume.```", color=hex_colors['green'])
                    asyncio.create_task(build_embed(data['symbol'], embed, below_avg_volume)) ####

            elif data['event_type'] == "stockQuote":
                condition = data['condition']
                quote_indicators = data['indicator']

                if condition in stockQuoteConditionsDictionary and condition is not None:
                    webhook_url = indicatorsDictionary[quoteIndicator]
                    asyncio.create_task(send_discord_message(webhook_url, data))
                    print(quote_indicators)
                for quoteIndicator in quote_indicators:
                    if quoteIndicator is not None:
                        webhook_url = indicatorsDictionary[quoteIndicator]
                        asyncio.create_task(send_discord_message(webhook_url, data))
                        print(quote_indicators)


# processed_ids = set()
# async def process_news_item(description, title, image, thumbnail, id, name, author, news_tickers, url, homepage_urls, keywords):
#     while True:
#         if id in processed_ids:
#             return
#         if keywords is not None:
#             for keyword in keywords:
#                 if keyword is not None:
#                     # loop through each webhook url and its associated keywords
#                     for webhook_url, webhook_keywords in keyword_webhooks.items():
#                         if keyword in webhook_keywords:
#                             hook = AsyncDiscordWebhook(url=webhook_url, content="<@375862240601047070>")
#                             embed = DiscordEmbed(title=title, description=f"```py\n{description}```", color=hex_colors['magenta'], url=url)
#                             embed.add_embed_field(name="Publisher:", value=f"> **{name}**")
#                             if homepage_urls is not None:
#                                 embed.add_embed_field(name=f"Homepage URL:", value=f"> **{homepage_urls}**")
#                             if news_tickers is not None:
#                                 embed.add_embed_field(name=f"Tickers Mentioned:", value=f"> **{news_tickers}**")
#                             if author is not None:
#                                 embed.set_author(name=author)
#                             embed.set_image(url=image)
#                             embed.set_thumbnail(url=thumbnail)
#                             embed.set_timestamp()
#                             hook.add_embed(embed)
#                             await hook.execute()
#                             processed_ids.add(id)
#                             # Break out of the loop as soon as we find a match
#                             break




async def main():
    markets = [Market.Stocks, Market.Options]
    data_queue = Queue()
    connection_tasks = [
        asyncio.create_task(
            WebSocketClient(
                subscriptions=["T.*,Q.*,A.*"],
                api_key=YOUR_API_KEY,
                market=market,
            ).connect(
                lambda msg: asyncio.create_task(handle_queue(msg, data_queue))  # Updated handle_msg function
            )
        )
        for market in markets
    ]

    num_workers = 15  # You can adjust this value based on your requirements
    sdk_tasks = [
        handle_stocks_msg(data_queue) for _ in range(num_workers)
    ]

    await asyncio.gather(*sdk_tasks, *connection_tasks)


    await process_ticker()
asyncio.run(main())
