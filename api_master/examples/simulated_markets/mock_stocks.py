import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from cfg import OVERBOUGHT_1HOUR,OVERBOUGHT_1MIN,OVERBOUGHT_DAY,OVERBOUGHT_WEEK,OVERSOLD_1HOUR,OVERSOLD_1MIN,OVERSOLD_DAY,OVERSOLD_WEEK,SUPER_OVERBOUGHT,SUPER_OVERSOLD
from cfg import upside_day,upside_scalps, downside_day,downside_scalps
import numpy as np
from simulated_client import SimulatedClient
from examples.simulated_markets.skewfinder import pc
from sdks.polygon_sdk.technical_conditions import check_macd_condition_bearish,check_macd_condition_bullish,check_rsi_condition_bearish,check_rsi_condition_bullish
import random
from helpers import generate_stock_embed, generate_options_embed
from cfg import keyword_categories, keyword_webhooks
from news_processor import news_main
import asyncio
from typing import Union
from cfg import thirty_days_ago_str
from sdks.datamaster import DataMaster
import pandas as pd
from sdks.helpers.helpers import human_readable, extract_underlying_symbol
import aiohttp
from discord_webhook import AsyncDiscordWebhook,DiscordEmbed
from hooks.hook_dicts import stock_exchange_hooks, sector_hooks, options_exchange_hooks
from sdks.polygon_sdk.list_sets import sublist1, market_sectors
from typing import List
from datetime import datetime
from cfg import optvol_100kplus,optvol_10kto20k,optvol_20to50k,optvol_50to100k,optvol_5k10k
from cfg import new_52_low,new_52_high,near_52_low,near_52_high, skew1,skew2,skew3
from cfg import spx, coin, bidu, tgt, ual
from sdks.helpers.helpers import build_option_embed, build_embed
from cfg import PRIOR_REFERENCE, CROSS_TRADE, INTERMARKET_SWEEPS, SSR, OPENING_TRADE,ODD_LOT, OFFICIAL_CLOSE,single_auction_non_iso,options_floor_trade, multileg_auto,multileg_auction,multi_vs_single,multiauto_vs_single,multileg_floor_trade,option_sweeps
from polygon_enhanced.polygon_enhanced.websocket.models import EquityAgg,EquityQuote,EquityTrade
from cfg import vol1k_to5k,vol5k_to10k,vol500_to1k,vol_10kplus,above_avg_volume,below_avg_volume,squeeze_potential, hex_colors, fire_sale, accumulation,earnings_week, seven_days_from_now_str,options_auto_trade, multi_cross, earnings_today, today_str, YOUR_API_KEY, NEXT_DAY, SLOW_ASK,OPENING_PRINTS, CLOSING_PRINTS,DEFICIENT,CORRECTED_CLOSE, OPENING_PRINTS, DERIVATIVELY
from sdks.polygon_sdk.mapping_dicts import option_condition_dict,TAPES, stock_condition_dict, option_condition_desc_dict, quote_conditions, STOCK_EXCHANGES, indicators,quote_conditions,OPTIONS_EXCHANGES
from sdks.models.test_events import TestStocksEvent, TestOptionsEvent, TestIndicesEvent
from discord_webhook import AsyncDiscordWebhook, DiscordEmbed
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
from asyncio import Queue
from sdks.datamaster import DataMaster
from sdks.polygon_sdk.masterSDK import MasterSDK
from disnake.ext import commands
import disnake
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
df = pd.read_csv('files/stocks/all_snapshots.csv') #create this  file in 'get_latest_ticker_data.py'
df2 = pd.read_csv('files/options/all_options_data.csv') #you must download this spreadsheet from the "get_latest_options_data.py" file.
df3 = pd.read_csv('files/indices/all_indices_data.csv') #you must download this spreadsheet from the "get_latest_options_data.py" file.
client = SimulatedClient()
master = MasterSDK()
webull = AsyncWebullSDK()
poly = AsyncPolygonSDK(YOUR_API_KEY)


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

async def get_rsi_async(ticker, timespan, window, limit):
    tasks = []
    for symbol in ticker:
        task = await poly.get_rsi(symbol=symbol, timespan=timespan, window=window, limit=limit)
        tasks.append(task)

    rsi_results = await asyncio.gather(*tasks)
    return rsi_results

async def process_ticker():

    while True:


        i = random.choice(sublist1)
        print(i)


        
        histh = await poly.get_macd(i, timespan="hour")
        rsih = await poly.get_rsi(i, timespan="hour")
        histd= await poly.get_macd(i, timespan="day")
        rsid = await poly.get_rsi(i, timespan="day")
        rsim = await poly.get_rsi(i, timespan="minute")


        check_bull_macdh, check_bull_rsih, check_bear_macdh, check_bear_rsih, check_bull_macdd, check_bull_rsid, check_bear_macdd, check_bear_rsid, check_bear_rsim, check_bull_rsim = await asyncio.gather(
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
        )

        description = "```py\nThe '💫Momentum💫 Scalps' channel highlights stocks with high potential for swift price changes by utilizing the oversold / overbought RSI combined with an iminent MACD Cross.```"
        if check_bull_rsih is True and check_bull_macdh is True:

 
       
            embed = DiscordEmbed(title=f"Upside 💫Momentum💫 Scalps - HOUR", description=f"```py\nThe 'Upside 💫Momentum💫 Scalps' channel highlights stocks with high potential for swift price changes. These stocks are pre-filtered by market cap and evaluated based on key indicators: the Relative Strength Index (RSI) and the Moving Average Convergence Divergence (MACD) cross. The RSI indicates whether a stock is overbought or oversold, while a MACD cross suggests a potential price movement trend. This makes these stocks prime for quick 'scalp' trades, although any trading strategy should be approached with careful analysis and risk management.```", color=hex_colors['green'])


    
    
            embed.set_footer(text=f"{i}")
            embed.add_embed_field(name=f"Before Jumping in:", value=f"> **NFA**\n> ✅ Check the spread\n> ✅ Look for a CALL IV skew as a bonus\n> ❓ (*the lowest IV would be at a strike ABOVE the current price*)\n> ✅ Verify technicals (🐂 macd cross, oversold RSI)")
            
            
            
            await build_embed(i, embed, upside_scalps)
        if check_bear_rsih is True and check_bear_macdh is True:
        
            embed = DiscordEmbed(title=f"Downside💫Scalps - HOUR - {i}", description=description, color=hex_colors['red'])

            embed.add_embed_field(name=f"Before Jumping in:", value=f"> **NFA**\n> ✅ Check the spread\n> ✅ Look for a PUT IV skew as a bonus\n> ❓ (*the lowest IV would be at a strike BELOW the current price*)\n> ✅ Verify technicals (🐻 macd cross, overbought RSI)")
          
            await build_embed(i, embed, downside_scalps)

        if check_bull_rsid is True and check_bull_macdd is True:
            embed = DiscordEmbed(title=f"Upside💫 Scalps - DAILY - {i}", description=description, color=hex_colors['green'])



            embed.add_embed_field(name=f"Before Jumping in:", value=f"> **NFA**\n> ✅ Check the spread\n> ✅ Look for a CALL IV skew as a bonus\n> ❓ (*the lowest IV would be at a strike ABOVE the current price*)\n> ✅ Verify technicals (🐂 macd cross, oversold RSI)")
            
            await build_embed(i, embed, upside_day)
        
           

        if check_bear_rsid is True and check_bear_macdd is True:

            embed = DiscordEmbed(title=f"Downside💫 Scalps - DAILY - {i}", description=description, color=hex_colors['red'])
           
    

            embed.set_footer(text="🔴 AT THE MONEY PUTS - 2-3+ WEEKS OUT! EXPLOIT THE MOMENTUM")
            embed.add_embed_field(name=f"Before Jumping in:", value=f"> **NFA**\n> ✅ Check the spread\n> ✅ Look for an PUT IV skew as a bonus\n> ❓ (*the lowest IV would be at a strike BELOW the current price*)\n> ✅ Verify technicals (🐻 macd cross, overbought RSI)")

            await build_embed(i, embed, downside_day)
    
           

        if check_bear_rsid is True and check_bear_macdd is True:
            embed = DiscordEmbed(title=f"Downside💫 Scalps - DAILY - {i}", description=description, color=hex_colors['red'])
  
            embed.set_footer(text="🔴 AT THE MONEY PUTS - 2-3+ WEEKS OUT! EXPLOIT THE MOMENTUM")
            embed.add_embed_field(name=f"Before Jumping in:", value=f"> **NFA**\n> ✅ Check the spread\n> ✅ Look for an PUT IV skew as a bonus\n> ❓ (*the lowest IV would be at a strike BELOW the current price*)\n> ✅ Verify technicals (🐻 macd cross, overbought RSI)")

            await build_embed(i, embed, downside_day)

    

        if check_bear_rsim is True:
           
            embed = DiscordEmbed(title=f"Minute-RSI Scan", description=f"```py\nScanner picked up an overbought minute RSI for {i}```", color=hex_colors['red'])
            embed.set_footer(text="🔴 Overbought - 1 Minute")

            await build_embed(i, embed, "https://discord.com/api/webhooks/1124185627915718716/1QKeXOmDbAv3oTw63Tto-ls0xvzeKcffoRwE8rRlm8CHIZ3dG4HyNuWunNdCHhS2UPYu")


        if check_bull_rsim is True:

            embed = DiscordEmbed(title=f"Minute-RSI Scan", description=f"```py\nScanner picked up an overbought minute RSI for {i}```", color=hex_colors['red'])
            embed.set_footer(text="🟢 Oversold - 1 Minute")

            await build_embed(i, embed, "https://discord.com/api/webhooks/1124185429307044030/z5DpGErTFYQ-ydEfULw8mt4UpYW-58uwk_fV7bfd4ycCepmxuCxZelauBlFMr_k98Ml_")



async def consume(queue: asyncio.Queue):
    

    while True:
        
        data = await queue.get()
        for msgs in data:
            print(data)
            




            if isinstance(msgs, TestStocksEvent):
                try:
                    # Create tasks for last_trade_condition and last_quote_condition
                    trade_condition_task = asyncio.create_task(poly.last_trade_condition(msgs.symbol))
                    quote_condition_task = asyncio.create_task(poly.last_quote_condition(msgs.symbol))

                    # Append the tasks to the list


                    # Wait for all tasks to complete concurrently
                    results = await asyncio.gather(trade_condition_task, quote_condition_task)
                    flattened_results = [item for sublist1 in results for item in sublist1]
                    if msgs.last_trade_conditions is not None and "22" in str(msgs.last_trade_conditions):
                        embed = DiscordEmbed(title=f"Prior Reference Price - {msgs.symbol}", description=f"```py\n{msgs.symbol} flagged with a condition code of 'Prior Reference Price.```", color=hex_colors['blue'])
                        await build_embed(msgs.symbol,embed,PRIOR_REFERENCE)

                    elif msgs.last_trade_conditions is not None and "8" in str(msgs.last_trade_conditions):
                        embed = DiscordEmbed(title=f"Closing Print`py\nClosing Prints Detecteed```", color=hex_colors['red'])
                        await build_embed(msgs.symbol,embed,CLOSING_PRINTS)

                    elif results is not None and "38" in flattened_results:
                        embed = DiscordEmbed(title=f"Corrected Close - {msgs.symbol}", description=f"```py\nCorrected Close```", color=hex_colors['yellow'])
                        await build_embed(msgs.symbol,embed,CORRECTED_CLOSE)
                    elif results is not None and 20 in flattened_results:
                        embed = DiscordEmbed(title=f"Next Day - {msgs.symbol}", description=f"```py\nNext Day```", color=hex_colors['yellow'])
                        await build_embed(msgs.symbol,embed,NEXT_DAY)
                    elif msgs.last_trade_conditions is not None and 63 in str(msgs.last_trade_conditions):
                        embed = DiscordEmbed(title=f"Deficient - {msgs.symbol}", description=f"```py\nFinancially Deficient - Doesn't meet listing standards.```", color=hex_colors['green'])
                        await build_embed(msgs.symbol,embed,DEFICIENT)
                    elif msgs.last_trade_conditions is not None and 9 in str(msgs.last_trade_conditions):
                        embed = DiscordEmbed(title=f"Cross Trade - {msgs.symbol}", description=f"```py\nCross Trade Detected```", color=hex_colors['orange'])
                        await build_embed(msgs.symbol,embed,CROSS_TRADE)
                    elif results is not None and 14 in flattened_results:
                        embed = DiscordEmbed(title=f"Intermarket Sweep - {msgs.symbol}", description=f"```py\nIntermarket Sweep Detected```", color=hex_colors['yellow'])
                        await build_embed(msgs.symbol,embed, INTERMARKET_SWEEPS)
                    elif msgs.last_trade_conditions is not None and 60 in str(msgs.last_trade_conditions):
                        embed = DiscordEmbed(title=f"SSR In Effect  - {msgs.symbol}", description=f"```py\nThe Short Sale Rule is in effect for this ticker - meaning it cannot be shorted on a down-tick and has fallen 10% within the last trading day. SSR will remain active until the following business day at close.```", color=hex_colors['red'])
                        await build_embed(msgs.symbol,embed, SSR)
                    elif msgs.last_trade_conditions is not None and 17 in str(msgs.last_trade_conditions):
                        embed = DiscordEmbed(title=f"Opening Trade  - {msgs.symbol}", description=f"```py\nThis trade has been flagged as a Market Center Opening Trade```", color=hex_colors['green'])
                        await build_embed(msgs.symbol,embed, OPENING_TRADE)
                    if results is not None and 15 in flattened_results:
                        embed = DiscordEmbed(title=f"Official Close  - {msgs.symbol}", description=f"```py\nThis trade has been flagged as a Market Center Official Close```", color=hex_colors['green'])
                        await build_embed(msgs.symbol,embed, OFFICIAL_CLOSE)
                    if results is not None and 37 in flattened_results:
                        embed = DiscordEmbed(title=f"Odd Lot Trade  - {msgs.symbol}", description=f"```py\nThis trade has been flagged as an odd lot trade.```", color=hex_colors['green'])
                        await build_embed(msgs.symbol,embed, ODD_LOT)

                except TypeError:
                    continue

                rsi_hour_task = await get_rsi_async(msgs.symbol, timespan="hour", window=14, limit=1)
                rsi_minute_task = await get_rsi_async(msgs.symbol, timespan="minute", window=14, limit=1)
                rsi_day_task = await get_rsi_async(msgs.symbol, timespan="day", window=14, limit=1)
                rsi_week_task = await get_rsi_async(msgs.symbol, timespan="week", window=14, limit=1)

                rsi_hour, rsi_minute, rsi_day, rsi_week = await asyncio.gather(
                    rsi_hour_task, rsi_minute_task, rsi_day_task, rsi_week_task
                )

                
                print(rsi_hour,rsi_day,rsi_week,rsi_minute)
                if rsi_hour is not None and rsi_minute is not None and rsi_day is not None and rsi_week is not None:
                    if rsi_minute[0] <= 30:
                        embed = DiscordEmbed(title=f"🐂 Oversold RSI - 1 Min - {msgs.symbol}", description=f"```py\nThe RSI for {msgs.symbol} is currently trading at {round(float(rsi_minute[0]),2)} on the 1 minute.```", color=hex_colors['green'])
                        embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsi_minute[0]),2)}**\n> 1hour: **{round(float(rsi_hour[0]),2)}**\n> Day: **{round(float(rsi_day[0]),2)}**\n> Week: **{round(float(rsi_week[0]),2)}**")
                        await build_embed(msgs.symbol, embed, OVERSOLD_1MIN)
                    elif rsi_hour[0] <= 30:
                        embed = DiscordEmbed(title=f"🐂 Oversold RSI - 1 Hour - {msgs.symbol}", description=f"```py\nThe RSI for {msgs.symbol} is currently trading at {round(float(rsi_hour[0]),2)} on the daily.```", color=hex_colors['green'])
                        embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsi_minute[0]),2)}**\n> 1hour: **{round(float(rsi_hour[0]),2)}**\n> Day: **{round(float(rsi_day[0]),2)}**\n> Week: **{round(float(rsi_week[0]),2)}**")
                        await build_embed(msgs.symbol, embed, OVERSOLD_1HOUR)
                    elif rsi_day[0] <= 30:
                        embed = DiscordEmbed(title=f"🐂 Oversold RSI - 1 Day - {msgs.symbol}", description=f"```py\nThe RSI for {msgs.symbol} is currently trading at {round(float(rsi_day[0]),2)} on the hourly.```", color=hex_colors['green'])
                        embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsi_minute[0]),2)}**\n> 1hour: **{round(float(rsi_hour[0]),2)}**\n> Day: **{round(float(rsi_day[0]),2)}**\n> Week: **{round(float(rsi_week[0]),2)}**")
                        await build_embed(msgs.symbol, embed, OVERSOLD_DAY)

                    elif rsi_day[0] <= 30:
                        embed = DiscordEmbed(title=f"🐂 Oversold RSI - 1 Week - {msgs.symbol}", description=f"```py\nThe RSI for {msgs.symbol} is currently trading at {round(float(rsi_day[0]),2)} on the hourly.```", color=hex_colors['green'])
                        embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsi_minute[0]),2)}**\n> 1hour: **{round(float(rsi_hour[0]),2)}**\n> Day: **{round(float(rsi_day[0]),2)}**\n> Week: **{round(float(rsi_week[0]),2)}**")
                        await build_embed(msgs.symbol, embed, OVERSOLD_WEEK)
                    
                    elif rsi_week[0] <= 30:
                        embed = DiscordEmbed(title=f"🐂 Oversold RSI - 1 Week - {msgs.symbol}", description=f"```py\nThe RSI for {msgs.symbol} is currently trading at {round(float(rsi_day[0]),2)} on the weekly.```", color=hex_colors['green'])
                        embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsi_minute[0]),2)}**\n> 1hour: **{round(float(rsi_hour[0]),2)}**\n> Day: **{round(float(rsi_day[0]),2)}**\n> Week: **{round(float(rsi_week[0]),2)}**")
                        await build_embed(msgs.symbol, embed, OVERBOUGHT_WEEK)
                    elif rsi_minute[0] >= 70:
                        embed = DiscordEmbed(title=f"🐻 Overbought RSI - 1 Min - {msgs.symbol}", description=f"```py\nThe RSI for {msgs.symbol} is currently trading at {round(float(rsi_minute[0]),2)} on the 1 minute.```", color=hex_colors['red'])
                        embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsi_minute[0]),2)}**\n> 1hour: **{round(float(rsi_hour[0]),2)}**\n> Day: **{round(float(rsi_day[0]),2)}**\n> Week: **{round(float(rsi_week[0]),2)}**")
                        await build_embed(msgs.symbol, embed, OVERBOUGHT_1MIN)
                    elif rsi_hour[0] >= 70:
                        embed = DiscordEmbed(title=f"🐻 Overbought RSI - 1 Hour - {msgs.symbol}", description=f"```py\nThe RSI for {msgs.symbol} is currently trading at {round(float(rsi_hour[0]),2)} on the hourly.```", color=hex_colors['red'])
                        embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsi_minute[0]),2)}**\n> 1hour: **{round(float(rsi_hour[0]),2)}**\n> Day: **{round(float(rsi_day[0]),2)}**\n> Week: **{round(float(rsi_week[0]),2)}**")
                        await build_embed(msgs.symbol, embed, OVERBOUGHT_1HOUR)
                    elif rsi_day[0] >= 70:
                        embed = DiscordEmbed(title=f"🐻 Overbought RSI - 1 Day - {msgs.symbol}", description=f"```py\nThe RSI for {msgs.symbol} is currently trading at {round(float(rsi_day[0]),2)} on the daily.```", color=hex_colors['red'])
                        embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsi_minute[0]),2)}**\n> 1hour: **{round(float(rsi_hour[0]),2)}**\n> Day: **{round(float(rsi_day[0]),2)}**\n> Week: **{round(float(rsi_week[0]),2)}**")
                        await build_embed(msgs.symbol, embed, OVERBOUGHT_DAY)
                    elif rsi_week[0] >= 70:
                        embed = DiscordEmbed(title=f"🐻 Overbought RSI - 1 Week - {msgs.symbol}", description=f"```py\nThe RSI for {msgs.symbol} is currently trading at {round(float(rsi_day[0]),2)} on the weekly.```", color=hex_colors['red'])
                        embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsi_minute[0]),2)}**\n> 1hour: **{round(float(rsi_hour[0]),2)}**\n> Day: **{round(float(rsi_day[0]),2)}**\n> Week: **{round(float(rsi_week[0]),2)}**")
                        await build_embed(msgs.symbol, embed, OVERBOUGHT_WEEK)


                    elif rsi_week[0] <= 30 and rsi_day[0] <= 30 and rsi_hour[0] <= 30:
                        embed = DiscordEmbed(title=f"🐂 SUPER OVERSOLD RSI {msgs.symbol}", description=f"```py\n{msgs.symbol} exhibits SUPER OVERSOLD RSI - With an oversold RSI on the hourly, daily, and weekly timeframes.```", color=hex_colors['green'])
                        embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsi_minute[0]),2)}**\n> 1hour: **{round(float(rsi_hour[0]),2)}**\n> Day: **{round(float(rsi_day[0]),2)}**\n> Week: **{round(float(rsi_week[0]),2)}**")
                        await build_embed(msgs.symbol, embed, SUPER_OVERSOLD)
                    
                    elif rsi_week[0] >= 70 and rsi_day[0] <= 30 and rsi_hour[0] <= 30:
                        embed = DiscordEmbed(title=f"🐻 SUPER OVERBOUGHT RSI {msgs.symbol}", description=f"```py\n{msgs.symbol} exhibits SUPER OVERBOUGHT RSI - With an oversold RSI on the hourly, daily, and weekly timeframes.```", color=hex_colors['red'])
                        embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsi_minute[0]),2)}**\n> 1hour: **{round(float(rsi_hour[0]),2)}**\n> Day: **{round(float(rsi_day[0]),2)}**\n> Week: **{round(float(rsi_week[0]),2)}**")

                        await build_embed(msgs.symbol, embed, SUPER_OVERBOUGHT)
                
                    if msgs.last_size is not None and msgs.last_size >= 500 and msgs.last_size <= 999:
                        embed= DiscordEmbed(title=f"Trade - 500 to 1k Volume", description=f"```py\n{msgs.symbol} just traded for a size of {msgs.last_size} at a price of ${msgs.last_price}```")
                        await build_embed(msgs.symbol, embed, vol500_to1k)
                    if msgs.last_size is not None and msgs.last_size >= 1000 and msgs.last_size <= 4999:
                        embed= DiscordEmbed(title=f"Trade - 1k to 5k Volume", description=f"```py\n{msgs.symbol} just traded for a size of {msgs.last_size} at a price of ${msgs.last_price}```")
                        await build_embed(msgs.symbol, embed, vol1k_to5k)

                    if msgs.last_size is not None and msgs.last_size >= 5000 and msgs.last_size <= 9999:
                        embed= DiscordEmbed(title=f"Trade - 5k to 10k Volume", description=f"```py\n{msgs.symbol} just traded for a size of {msgs.last_size} at a price of ${msgs.last_price}```")
                        await build_embed(msgs.symbol, embed, vol5k_to10k)

                    if msgs.last_size is not None and msgs.last_size >= 10000:
                        embed= DiscordEmbed(title=f"Trade - 10k Plus Volume", description=f"```py\n{msgs.symbol} just traded for a size of {msgs.last_size} at a price of ${msgs.last_price}```")
                        await build_embed(msgs.symbol, embed, vol_10kplus)


                    volume_analysis_task = get_webull_data_with_cache(msgs.symbol, "volume_analysis")
                    stock_data_task = get_webull_data_with_cache(msgs.symbol, "stock_data")
                    short_interest_task = get_webull_data_with_cache(msgs.symbol, "short_interest")

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
                        embed = DiscordEmbed(title=f"Squeeze Potential - {msgs.symbol}", description=f"```py\nThis feed returns tickers exhibiting signs of a potential squeeze. Short interest % of float > 25 - volume is below average.```", color=hex_colors['green'])
                        await build_embed(msgs.symbol, embed, squeeze_potential)
        
                    if stock_data is not None and stock_data.web_stock_close is not None and stock_data.fifty_high is not None and float(stock_data.web_stock_close) > 0.95 * float(stock_data.fifty_high):
                        embed = DiscordEmbed(title=f"{msgs.symbol} is Near 52 week Highs! {msgs.symbol}", description=f"```py\nThis feed returns tickers trading within 5% of their 52 week high```", color=hex_colors['red'])
                        await build_embed(msgs.symbol, embed, near_52_high)

                    if stock_data is not None and stock_data.web_stock_close is not None and stock_data.fifty_low is not None and float(stock_data.web_stock_close) < 0.05 * float(stock_data.fifty_low):
                        embed = DiscordEmbed(title=f"{msgs.symbol} is Near 52 week Lows! {msgs.symbol}", description=f"```py\nThis feed returns tickers trading within 5% of their 52 week high```", color=hex_colors['green'])
                        await build_embed(msgs.symbol, embed, near_52_low)

                    if stock_data is not None and stock_data.fifty_high == stock_data.web_stock_close:
                        embed = DiscordEmbed(title=f"{msgs.symbol} is Pushing 52 week Highs! {msgs.symbol}", description=f"```py\nThis feed returns tickers trading within 5% of their 52 week high```", color=hex_colors['red'])
                        await build_embed(msgs.symbol, embed, new_52_high)

                    if stock_data is not None and stock_data.fifty_low == stock_data.web_stock_close:
                        embed = DiscordEmbed(title=f"{msgs.symbol} is Pushing 52 week Lows! {msgs.symbol}", description=f"```py\nThis feed returns tickers trading within 5% of their 52 week high```", color=hex_colors['green'])
                        await build_embed(msgs.symbol, embed, new_52_low)


                    if vol_analysis.buyVolume is not None and vol_analysis.totalVolume is not None and vol_analysis.buyVolume >= 0.75 * vol_analysis.totalVolume:
                        embed = DiscordEmbed(title=f"🚀 Accumulation of {msgs.symbol} 🚀", description=f"```py\nThis feed is returning tickers with at least 75% of the volume on the day recorded as BUY VOLUME. Accumulation of {msgs.symbol}!```", color=hex_colors['green'])
                        await build_embed(msgs.symbol, embed, accumulation)
                    if vol_analysis.sellVolume is not None and vol_analysis.totalVolume is not None and vol_analysis.sellVolume >= 0.75 * vol_analysis.totalVolume:
                        embed = DiscordEmbed(title=f"🔥 FIRE SALE of {msgs.symbol} 🔥", description=f"```py\nThis feed is returning tickers with at least 75% of the volume on the day recorded as SELL VOLUME. FIRE SALE of {msgs.symbol}!```", color=hex_colors['red'])
                        await build_embed(msgs.symbol, embed, fire_sale)

                    if stock_data.last_earnings is not None and stock_data.last_earnings == today_str:
                        embed = DiscordEmbed(title=f"Earnings Today!", description=f"```py\n{msgs.symbol} has earnings today.```", color=hex_colors['yellow'])
                        await build_embed(msgs.symbol, embed, earnings_today)

                    if stock_data.last_earnings is not None and stock_data.last_earnings <= seven_days_from_now_str:
                        embed = DiscordEmbed(title=f"Earnings Week!", description=f"```py\nThis feed is returning tickers that have earnings this week. {msgs.symbol} is one of them!```", color=hex_colors['blue'])
                        embed.add_embed_field(name=f"Earnings:", value=f"> **{stock_data.last_earnings}**")
                        await build_embed(msgs.symbol, embed, earnings_week)


                    if stock_data.avg_10d_vol is not None and stock_data.web_stock_vol is not None and float(stock_data.web_stock_vol) >= (float(stock_data.avg_10d_vol) * 1.25):
                        embed = DiscordEmbed(title=f"Above Average Volume - {msgs.symbol}", description=f"```py\n{msgs.symbol} is currently trading ABOVE average volume.```", color=hex_colors['red'])
                        await build_embed(msgs.symbol, embed, above_avg_volume)

                    if stock_data.avg_10d_vol is not None and stock_data.web_stock_vol is not None and float(stock_data.web_stock_vol) <= (float(stock_data.avg_10d_vol) * 0.75):
                        embed = DiscordEmbed(title=f"Below Average Volume - {msgs.symbol}", description=f"```py\n{msgs.symbol} is currently trading BELOW average volume.```", color=hex_colors['green'])
                        await build_embed(msgs.symbol, embed, below_avg_volume)


                if isinstance(msgs, TestOptionsEvent):
                    option_ticker = str(msgs.ticker)
                    ticker = human_readable(option_ticker)
                    
                    if msgs.last_trade_size is not None and msgs.last_trade_price is not None:
                        last_trade_size = msgs.last_trade_size
                        last_trade_price = msgs.last_trade_price
                        
                        if 500 <= last_trade_size <= 999:
                            embed = DiscordEmbed(title=f"Trade - 500 to 1k Volume", description=f"```py\n{ticker} just traded for a size of {last_trade_size} at a price of ${last_trade_price}```")
                            asyncio.create_task(build_option_embed(msgs.ticker, embed, vol500_to1k))
                        if 1000 <= last_trade_size <= 4999:
                            embed = DiscordEmbed(title=f"Trade - 1k to 5k Volume", description=f"```py\n{ticker} just traded for a size of {last_trade_size} at a price of ${last_trade_price}```")
                            asyncio.create_task(build_option_embed(msgs.ticker, embed, vol1k_to5k))
                        if 5000 <= last_trade_size <= 9999:
                            embed = DiscordEmbed(title=f"Trade - 5k to 10k Volume", description=f"```py\n{ticker} just traded for a size of {last_trade_size} at a price of ${last_trade_price}```")
                            asyncio.create_task(build_option_embed(msgs.ticker, embed, vol5k_to10k))
                        if last_trade_size >= 10000:
                            embed = DiscordEmbed(title=f"Trade - 10k Plus Volume", description=f"```py\n{ticker} just traded for a size of {last_trade_size} at a price of ${last_trade_price}```")
                            asyncio.create_task(build_option_embed(msgs.ticker, embed, vol_10kplus))

                    if msgs.day_volume is not None:
                        day_volume = float(msgs.day_volume)
                        
                        if 5000 <= day_volume <= 9999:
                            embed = DiscordEmbed(title=f"Day Volume - 5,000 to 10,000", description=f"```py\n{ticker} has {day_volume:,} volume on the day.```")
                            asyncio.create_task(build_option_embed(msgs.ticker, embed, optvol_5k10k))
                        if 10000 <= day_volume <= 19999:
                            embed = DiscordEmbed(title=f"Day Volume - 10,000 to 19,000", description=f"```py\n{ticker} has {day_volume:,} volume on the day.```")
                            asyncio.create_task(build_option_embed(msgs.ticker, embed, optvol_10kto20k))
                        if 20000 <= day_volume <= 50000:
                            embed = DiscordEmbed(title=f"Day Volume - 20,000 to 50,000", description=f"```py\n{ticker} has {day_volume:,} volume on the day.```")
                            asyncio.create_task(build_option_embed(msgs.ticker, embed, optvol_20to50k))
                        if 50000 <= day_volume <= 99999:
                            embed = DiscordEmbed(title=f"Day Volume - 50,000 to 100,000", description=f"```py\n{ticker} has {day_volume:,} volume on the day.```")
                            asyncio.create_task(build_option_embed(msgs.ticker, embed, optvol_50to100k))
                        if day_volume >= 100000:
                            embed = DiscordEmbed(title=f"Day Volume - 100,000++", description=f"```py\n{ticker} has {day_volume:,} volume on the day.```")
                            asyncio.create_task(build_option_embed(msgs.ticker, embed, optvol_50to100k))

                    if msgs.last_trade_conditions is not None:
                        last_trade_conditions = msgs.last_trade_conditions
                        
                        if last_trade_conditions == 232:
                            embed = DiscordEmbed(title=f"Multileg Auto Electronic Trade", description=f"```py\n{ticker}```\n> **Transaction represents an electronic execution of a multi-leg order traded in a complex order book.**", color=hex_colors['blue'])
                            asyncio.create_task(build_option_embed(msgs.ticker, embed, multileg_auto))
                        if last_trade_conditions == 227:
                            embed = DiscordEmbed(title=f"Single Leg Auction - Non ISO", description=f"```py\n{ticker}```\n> **Transaction was the execution of an electronic order which was \"stopped\" at a price and traded in a two-sided auction mechanism that goes through an exposure period. Such auctions mechanisms include and are not limited to Price Improvement, Facilitation, or Solicitation Mechanism.**", color=hex_colors['blue'])
                            asyncio.create_task(build_option_embed(msgs.ticker, embed, single_auction_non_iso))
                        if last_trade_conditions == 233:
                            embed = DiscordEmbed(title=f"Multi-Leg Auction", description=f"```py\n{ticker}```\n> **Transaction was the execution of an electronic multi-leg order which was stopped at a price and traded in a two-sided auction mechanism that goes through an exposure period in a complex order book. Such auctions mechanisms include and are not limited to Price Improvement, Facilitation, or Solicitation Mechanism.**", color=hex_colors['blue'])
                            asyncio.create_task(build_option_embed(msgs.ticker, embed, multileg_auction))
                        if last_trade_conditions == 235:
                            embed = DiscordEmbed(title=f"Multi-Leg Floor Trade", description=f"```py\n{ticker}```\n> **Transaction represents a non-electronic multi-leg order trade executed against other multi-leg order(s) on a trading floor. Execution of Paired and Non-Paired Auctions and Cross orders on an exchange floor are also included in this category.**", color=hex_colors['blue'])
                            asyncio.create_task(build_option_embed(msgs.ticker, embed, multileg_floor_trade))
                        if last_trade_conditions == 219:
                            embed = DiscordEmbed(title=f"Intermarket Sweep Order", description=f"```py\n{ticker}```\n> **Transaction was the execution of an order identified as an Intermarket Sweep Order. Process like normal transaction.**", color=hex_colors['blue'])
                            asyncio.create_task(build_option_embed(msgs.ticker, embed, option_sweeps))
                        if last_trade_conditions == 242:
                            embed = DiscordEmbed(title=f"Stock Options Floor Trade", description=f"```py\n{ticker}```\n> **Transaction represents a non-electronic multi-leg order stock/options trade executed on a trading floor in a complex order book. Execution of Paired and Non-Paired Auctions and Cross orders on an exchange floor are also included in this category.**", color=hex_colors['blue'])
                            asyncio.create_task(build_option_embed(msgs.ticker, embed, options_floor_trade))
                        if last_trade_conditions == 234:
                            embed = DiscordEmbed(title=f"Multi-Leg Cross", description=f"```py\n{ticker}```\n> **Transaction was the execution of an electronic multi-leg order which was \"stopped\" at a price and traded in a two-sided crossing mechanism that does not go through an exposure period. Such crossing mechanisms include and are not limited to Customer to Customer Cross and QCC with two or more options legs.**", color=hex_colors['blue'])
                            asyncio.create_task(build_option_embed(msgs.ticker, embed, multi_cross))
                        if last_trade_conditions == 236:
                            embed = DiscordEmbed(title=f"Multi Leg auto-electronic trade against single leg(s)", description=f"```py\n{ticker}```\n> **Transaction represents an electronic execution of a multi-leg order traded against single leg orders/quotes.**", color=hex_colors['yellow'])
                            asyncio.create_task(build_option_embed(msgs.ticker, embed, multiauto_vs_single))
                        if last_trade_conditions == 239:
                            embed = DiscordEmbed(title=f"Multi Leg floor trade against single leg(s)", description=f"```py\n{ticker}```\n> **Transaction represents a non-electronic multi-leg order trade executed on a trading floof against single leg orders/quotes. Such auctions mechanisms include and are not limited to Price Improvement, Facilitation, or Solicitation Mechanism.**", color=hex_colors['yellow'])
                            asyncio.create_task(build_option_embed(msgs.ticker, embed, multi_vs_single))
                        if last_trade_conditions == 240:
                            embed = DiscordEmbed(title=f"Stock Options Auto Electronic Trade", description=f"```py\n{ticker}```\n> **Transaction represents the an electronic execution of a multi-leg stock/options order traded in a complex order book.**", color=hex_colors['magenta'])
                            asyncio.create_task(build_option_embed(msgs.ticker, embed, options_auto_trade))


symbol_to_sector = {symbol: sector for sector, symbols in market_sectors.items() for symbol in symbols}  
async def stock_handler(msgs: List[TestStocksEvent], queue: Queue):
    send_tasks = []  # List to hold all send tasks

    for m in msgs:
        if m.today_change_percent <= 0:
            color = hex_colors['red']
        elif m.today_change_percent >= 0:
            color = hex_colors['green']
        else:
            color = hex_colors['gold']
        # Create the embed message
        m.last_exchange = STOCK_EXCHANGES.get(m.last_exchange)

        # Check if the exchange matches a Discord channel
        discord_webhook_url = stock_exchange_hooks.get(m.last_exchange)
        if discord_webhook_url:
            # Create a task for sending the message and add it to the list
            send_tasks.append(asyncio.create_task(generate_stock_embed(discord_webhook_url, m, color)))

        sector = symbol_to_sector.get(m.symbol)
        if sector:
            # Get the webhook URL for the sector
            webhook_url = sector_hooks.get(sector)

            if webhook_url:
                # Create the webhook object
                webhook = AsyncDiscordWebhook(webhook_url, content="<@375862240601047070>")




                # Create a task for sending the webhook message to the corresponding sector channel
                asyncio.create_task(generate_stock_embed(webhook_url, m, color))
                
                print(f"EXECUTED WEBHOOK")


    await queue.put(msgs)
    

async def options_handler(msgs: List[TestOptionsEvent], queue: Queue):
    send_tasks = []


    for m in msgs:
        if m.day_change_percent <= 0:
            color = hex_colors['red']
        elif m.day_change_percent >= 0:
            color = hex_colors['green']
        else:
            color = hex_colors['gold']
        exchange = OPTIONS_EXCHANGES.get(m.last_trade_exchange)  # Assuming TestOptionsEvent also has last_exchange

        discord_webhook_url = options_exchange_hooks.get(exchange)
        if discord_webhook_url:
            # Create a task for sending the message and add it to the list
            asyncio.create_task(generate_options_embed(discord_webhook_url, m, color))
    

        sector = None
        if sector:
            # Get the webhook URL for the sector
            webhook_url = sector_hooks.get(sector)

            if discord_webhook_url:
                # Create a task for sending the message and add it to the list
                asyncio.create_task(generate_options_embed(discord_webhook_url, m, color))
 

            if webhook_url:
                # Create the webhook object
                webhook = AsyncDiscordWebhook(webhook_url, content="<@375862240601047070>")

                # Create the embed message
                webhook = AsyncDiscordWebhook(webhook_url, content="<@375862240601047070>")
                if m.day_change_percent <= 0:
                    color = hex_colors['red']
                elif m.day_change_percent >= 0:
                    color = hex_colors['green']
                else:
                    color = hex_colors['gold']
                # Create the embed message






                asyncio.create_task(generate_options_embed(webhook, m, color))
                print(f"EXECUTED WEBHOOK")


    await queue.put(msgs)





async def send_stock_messages(stock_handler, queue):  # Only takes stock_handler
    while True:
        index2 = random.randint(0, len(df) - 1)
        row2 = df.iloc[index2]
        event_stocks = TestStocksEvent.from_row(row2)

        # Call the handler with the message
        await stock_handler([event_stocks], queue)
        await asyncio.sleep(0.001)


async def send_indices_messages(indices_handler, queue):  # Only takes options_handler
    while True:

        index = random.randint(0, len(df) - 1)
        row = df.iloc[index]
 
        event_indices = TestIndicesEvent.from_row(row)

        # Call the handler with the message
        await indices_handler([event_indices], queue)
async def send_options_messages(options_handler, queue):  # Only takes options_handler
    while True:
        index = random.randint(0, len(df2) - 1)
        row = df2.iloc[index]
        event_options = TestOptionsEvent.from_row(row)

        # Call the handler with the message
        await options_handler([event_options], queue)
        await asyncio.sleep(0.001)

processed_ids = set()

async def process_news_item(description, title, image, thumbnail, id, name, author, news_tickers, url, homepage_urls, keywords):
    if id in processed_ids:
        return
    if keywords is not None:
        for keyword in keywords:
            if keyword is not None:
                # loop through each webhook url and its associated keywords
                for webhook_url, webhook_keywords in keyword_webhooks.items():
                    if keyword in webhook_keywords:
                        hook = AsyncDiscordWebhook(url=webhook_url, content="<@375862240601047070>")
                        embed = DiscordEmbed(title=title, description=f"```py\n{description}```", color=hex_colors['magenta'], url=url)
                        embed.add_embed_field(name="Publisher:", value=f"> **{name}**")
                        if homepage_urls is not None:
                            embed.add_embed_field(name=f"Homepage URL:", value=f"> **{homepage_urls}**")
                        if news_tickers is not None:
                            embed.add_embed_field(name=f"Tickers Mentioned:", value=f"> **{news_tickers}**")
                        if author is not None:
                            embed.set_author(name=author)
                        embed.set_image(url=image)
                        embed.set_thumbnail(url=thumbnail)
                        embed.set_timestamp()
                        hook.add_embed(embed)
                        await hook.execute()
                        processed_ids.add(id)
                        # Break out of the loop as soon as we find a match
                        break


async def main():
    tickers = sublist1
    data_queue = Queue()

    # Define the number of workers
    num_messages_workers = 6 

    # Create multiple consumer tasks
    consumer_tasks = [
        asyncio.create_task(consume(data_queue)) for _ in range(num_messages_workers)
    ]

    # Create multiple tasks for sending stock messages
    stock_messages_tasks = [asyncio.create_task(send_stock_messages(stock_handler, data_queue)) for _ in range(num_messages_workers)]
    options_messages_task = [asyncio.create_task(send_options_messages(options_handler, data_queue)) for _ in range(num_messages_workers)]
    process_ticker_task = [asyncio.create_task(process_ticker()) for _ in range(num_messages_workers)]
    # Create a task for the news processor
    news_processor_task = await news_main()

    # Run the client
    await client.run()

    # Gather all tasks
    await asyncio.gather(*consumer_tasks, *stock_messages_tasks, *options_messages_task,news_processor_task)
    await asyncio.gather(*process_ticker_task)
    
asyncio.run(main())