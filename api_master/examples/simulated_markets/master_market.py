import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import psycopg2
from cfg import upside_day, upside_scalps, downside_day, downside_scalps, OVERBOUGHT_1HOUR,OVERBOUGHT_1MIN,OVERBOUGHT_DAY,OVERBOUGHT_WEEK,SUPER_OVERBOUGHT, option_sweeps,OVERSOLD_1HOUR,OVERSOLD_1MIN,OVERSOLD_DAY,OVERSOLD_WEEK,options_auto_trade,options_cross, SUPER_OVERSOLD
from polygon_enhanced.polygon_enhanced.websocket.models import EquityAgg,EquityQuote,EquityTrade, WebSocketMessage, Market
from polygon_enhanced.polygon_enhanced.websocket import WebSocketClient
from cfg import hex_colors
from asyncio import Queue
from sdks.helpers.helpers import build_embed, build_stock_condition_embed, build_exchange_embed, build_sector_embed
from hooks.hook_dicts import stock_condition_hooks,stock_exchange_hooks,option_condition_hooks,options_exchange_hooks, sector_hooks
from discord_webhook import AsyncDiscordWebhook, DiscordEmbed
import asyncio
import random
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.polygon_sdk.list_sets import stock_condition_dict, STOCK_EXCHANGES, TAPES, quote_conditions, indicators, market_sectors, subscriptions, options_condition_dict, OPTIONS_EXCHANGES, sublist1
from sdks.polygon_sdk.technical_conditions import check_macd_condition_bearish,check_macd_condition_bullish,check_rsi_condition_bearish,check_rsi_condition_bullish
from cfg import optionConditionsDict,stockQuoteConditionsDictionary,stockQuoteIndicatorsDictionary,stockConditionsDictionary,indicatorsDictionary, stockExchangeDictionary, optionsExchangeDescriptionDictionary,stockExchangeDescriptionDictionary,sectorDescriptions
from cfg import YOUR_API_KEY

poly = AsyncPolygonSDK(YOUR_API_KEY)
from datetime import datetime
# Define the queues for each data type
# Limit of concurrent tasks
semaphore = asyncio.Semaphore(100)
queues = {
    "stockTrade": asyncio.Queue(),
    "optionTrade": asyncio.Queue(),
    "stockAgg": asyncio.Queue(),
    "optionAgg": asyncio.Queue(),
    "stockQuote": asyncio.Queue(),
    "optionQuote": asyncio.Queue(),
}

symbol_to_sector = {symbol: sector for sector, symbols in market_sectors.items() for symbol in symbols}  
async def send_discord_options_message(webhook_url, message_data):
    


    webhook = AsyncDiscordWebhook(webhook_url,content=f"> <@375862240601047070>\n\n> **{str(message_data)}**")
    if webhook_url is not None:
        await webhook.execute()


async def send_discord_message(webhook_url, message_data):



    webhook = AsyncDiscordWebhook(webhook_url,content=f"> <@375862240601047070>\n\n> **{str(message_data)}**")
    if webhook_url is not None:
        await webhook.execute()

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



async def process_ticker(i):

    while True:
        i = random.choice(sublist1)

   
        check_bull_macdh, check_bull_rsih, check_bear_macdh, check_bear_rsih, check_bull_macdd, check_bull_rsid, check_bear_macdd, check_bear_rsid, check_bear_rsim, check_bull_rsim,histh, rsih, histd, rsid, rsim, rsiw = await check_all_macd_rsi_conditions(i)


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

            asyncio.create_task(build_embed(i, embed, "https://discord.com/api/webhooks/1124185627915718716/1QKeXOmDbAv3oTw63Tto-ls0xvzeKcffoRwE8rRlm8CHIZ3dG4HyNuWunNdCHhS2UPYu"))


        if check_bull_rsim is True:

            embed = DiscordEmbed(title=f"Minute-RSI Scan", description=f"```py\nScanner picked up an overbought minute RSI for {i}```", color=hex_colors['red'])
            embed.set_footer(text="🟢 Oversold - 1 Minute")

            asyncio.create_task(build_embed(i, embed, "https://discord.com/api/webhooks/1124185429307044030/z5DpGErTFYQ-ydEfULw8mt4UpYW-58uwk_fV7bfd4ycCepmxuCxZelauBlFMr_k98Ml_"))





        if rsih is not None and rsim is not None and rsid is not None and rsiw is not None:
            rsi_tasks = []
            if rsim[0] <= 30:
                embed = DiscordEmbed(title=f"🐂 Oversold RSI - 1 Min - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsim[0]),2)} on the 1 minute.```", color=hex_colors['green'])
                embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsim[0]),2)}**\n> 1hour: **{round(float(rsih[0]),2)}**\n> Day: **{round(float(rsid[0]),2)}**\n> Week: **{round(float(rsiw[0]),2)}**")
                asyncio.create_task(build_embed(i, embed, OVERSOLD_1MIN))
            elif rsih[0] <= 30:
                embed = DiscordEmbed(title=f"🐂 Oversold RSI - 1 Hour - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsih[0]),2)} on the daily.```", color=hex_colors['green'])
                embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsim[0]),2)}**\n> 1hour: **{round(float(rsih[0]),2)}**\n> Day: **{round(float(rsid[0]),2)}**\n> Week: **{round(float(rsiw[0]),2)}**")
                asyncio.create_task(build_embed(i, embed, OVERSOLD_1HOUR))
            elif rsid[0] <= 30:
                embed = DiscordEmbed(title=f"🐂 Oversold RSI - 1 Day - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsid[0]),2)} on the hourly.```", color=hex_colors['green'])
                embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsim[0]),2)}**\n> 1hour: **{round(float(rsih[0]),2)}**\n> Day: **{round(float(rsid[0]),2)}**\n> Week: **{round(float(rsiw[0]),2)}**")
                asyncio.create_task(build_embed(i, embed, OVERSOLD_DAY))

            elif rsid[0] <= 30:
                embed = DiscordEmbed(title=f"🐂 Oversold RSI - 1 Week - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsid[0]),2)} on the hourly.```", color=hex_colors['green'])
                embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsim[0]),2)}**\n> 1hour: **{round(float(rsih[0]),2)}**\n> Day: **{round(float(rsid[0]),2)}**\n> Week: **{round(float(rsiw[0]),2)}**")
                asyncio.create_task(build_embed(i, embed, OVERSOLD_WEEK))
            
            elif rsiw[0] <= 30:
                embed = DiscordEmbed(title=f"🐂 Oversold RSI - 1 Week - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsid[0]),2)} on the weekly.```", color=hex_colors['green'])
                embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsim[0]),2)}**\n> 1hour: **{round(float(rsih[0]),2)}**\n> Day: **{round(float(rsid[0]),2)}**\n> Week: **{round(float(rsiw[0]),2)}**")
                asyncio.create_task(build_embed(i, embed, OVERBOUGHT_WEEK))
            elif rsim[0] >= 70:
                embed = DiscordEmbed(title=f"🐻 Overbought RSI - 1 Min - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsim[0]),2)} on the 1 minute.```", color=hex_colors['red'])
                embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsim[0]),2)}**\n> 1hour: **{round(float(rsih[0]),2)}**\n> Day: **{round(float(rsid[0]),2)}**\n> Week: **{round(float(rsiw[0]),2)}**")
                asyncio.create_task(build_embed(i, embed, OVERBOUGHT_1MIN))
            elif rsih[0] >= 70:
                embed = DiscordEmbed(title=f"🐻 Overbought RSI - 1 Hour - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsih[0]),2)} on the hourly.```", color=hex_colors['red'])
                embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsim[0]),2)}**\n> 1hour: **{round(float(rsih[0]),2)}**\n> Day: **{round(float(rsid[0]),2)}**\n> Week: **{round(float(rsiw[0]),2)}**")
                asyncio.create_task(build_embed(i, embed, OVERBOUGHT_1HOUR))
            elif rsid[0] >= 70:
                embed = DiscordEmbed(title=f"🐻 Overbought RSI - 1 Day - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsid[0]),2)} on the daily.```", color=hex_colors['red'])
                embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsim[0]),2)}**\n> 1hour: **{round(float(rsih[0]),2)}**\n> Day: **{round(float(rsid[0]),2)}**\n> Week: **{round(float(rsiw[0]),2)}**")
                asyncio.create_task(build_embed(i, embed, OVERBOUGHT_DAY))
            elif rsiw[0] >= 70:
                embed = DiscordEmbed(title=f"🐻 Overbought RSI - 1 Week - {i}", description=f"```py\nThe RSI for {i} is currently trading at {round(float(rsid[0]),2)} on the weekly.```", color=hex_colors['red'])
                embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsim[0]),2)}**\n> 1hour: **{round(float(rsih[0]),2)}**\n> Day: **{round(float(rsid[0]),2)}**\n> Week: **{round(float(rsiw[0]),2)}**")
                asyncio.create_task(build_embed(i, embed, OVERBOUGHT_WEEK))


            elif rsiw[0] <= 30 and rsid[0] <= 30 and rsih[0] <= 30:
                embed = DiscordEmbed(title=f"🐂 SUPER OVERSOLD RSI {i}", description=f"```py\n{i} exhibits SUPER OVERSOLD RSI - With an oversold RSI on the hourly, daily, and weekly timeframes.```", color=hex_colors['green'])
                embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsim[0]),2)}**\n> 1hour: **{round(float(rsih[0]),2)}**\n> Day: **{round(float(rsid[0]),2)}**\n> Week: **{round(float(rsiw[0]),2)}**")
                asyncio.create_task(await build_embed(i, embed, SUPER_OVERSOLD))
            
            elif rsiw[0] >= 65 and rsid[0] >=65 and rsih[0] >=65:
                embed = DiscordEmbed(title=f"🐻 SUPER OVERBOUGHT RSI {i}", description=f"```py\n{i} exhibits SUPER OVERBOUGHT RSI - With an oversold RSI on the hourly, daily, and weekly timeframes.```", color=hex_colors['red'])
                embed.add_embed_field(name=f"RSI Snapshot:", value=f"> 1min: **{round(float(rsim[0]),2)}**\n> 1hour: **{round(float(rsih[0]),2)}**\n> Day: **{round(float(rsid[0]),2)}**\n> Week: **{round(float(rsiw[0]),2)}**")

                asyncio.create_task(build_embed(i, embed, SUPER_OVERBOUGHT))

            


            

async def consume_stockTrade():
    while True:
        data = await queues["stockTrade"].get()
        print(data)
        if data['stockSymbol'] in sublist1:
            embed = DiscordEmbed(title=f"Stock Trade - {data['stockSymbol']}", description=f"```py\n{data}```")
            if data['tradeConditions'] is not None:
                for condition in data['tradeConditions']:
                    if condition in stockConditionsDictionary:
                        webhook_url = stockConditionsDictionary[condition]
                        asyncio.create_task(send_discord_message(webhook_url, data))
                        print(condition)




            if data['tradeExchange'] is not None and data['tradeSize'] is not None and data['tradeSize'] >= 1000:
                if data['tradeExchange'] in stockExchangeDictionary:
                    exchange_discord_webhook_urls = stockExchangeDictionary[data['tradeExchange']]
                    embed_description = stockExchangeDescriptionDictionary[data['tradeExchange']]
                    embed_title = data['tradeExchange']
                    embed = DiscordEmbed(title=embed_title, description=f"```py\n{embed_description}```", color=hex_colors['magenta'])
                    asyncio.create_task(build_exchange_embed(data['stockSymbol'],exchange_discord_webhook_urls,embed))
                    print(data['tradeExchange'])



async def consume_optionTrade():
    send_tasks = []
    while True:
        data = await queues["optionTrade"].get()

        conditions = data['tradeConditions'] if 'tradeConditions' in data else []
        opt_exchange = data['tradeExchange']

        exchange_discord_webhook_urls = options_exchange_hooks.get(opt_exchange)
        for condition in conditions:
            webhook_url = optionConditionsDict[condition] if condition is not None else None
            async with semaphore:
                task = asyncio.create_task(send_discord_message(webhook_url, data))
                send_tasks.append(task)
        if exchange_discord_webhook_urls in options_exchange_hooks.keys():
            embed = DiscordEmbed(title=f"Trade out of {opt_exchange}", description=f"> {data}")
            async with semaphore:
                task = asyncio.create_task(send_discord_message(exchange_discord_webhook_urls, data))
                send_tasks.append(task)


async def consume_stockQuote():
    send_tasks=[]
    while True:
        
        
        data = await queues["stockQuote"].get()
        if data['stockSymbol'] in sublist1:
            print(data)
            condition = data['stockQuoteCondition']
            ask_exchange = data['askExchange']
            bid_exchange = data['bidExchange']
            indicators = data['stockQuoteIndicator']
            print(indicators)
            if condition is not None:
                if condition in stockQuoteConditionsDictionary:
                    webhook_url = stockQuoteConditionsDictionary[condition]
                    send_tasks.append(asyncio.create_task(send_discord_message(webhook_url, data)))



                    print(condition)
            for quoteIndicator in indicators:
                if quoteIndicator is not None:
                    webhook_url = indicatorsDictionary[quoteIndicator]
                    send_tasks.append(asyncio.create_task(send_discord_message(webhook_url, data)))



            if bid_exchange in stock_exchange_hooks:
                webhook_url = stock_exchange_hooks[bid_exchange]
                title = data['bidExchange']
                description = stockExchangeDescriptionDictionary[bid_exchange]
                embed = DiscordEmbed(title=title, description=f"```py\n{description}```", color=hex_colors['blue'])
                if webhook_url is not None:
                    send_tasks.append(asyncio.create_task(build_exchange_embed(data['stockSymbol'],webhook_url, embed)))





            sector = symbol_to_sector.get(data['stockSymbol'])
            if sector:
                # Get the webhook URL for the sector
                webhook_url = sector_hooks.get(sector)
                if webhook_url is not None:
                    # Create the webhook object
                    webhook = AsyncDiscordWebhook(webhook_url,rate_limit_retry=True, content="<@375862240601047070>")
                    
                    # Create the embed message
                    embed = DiscordEmbed(title=f"{sector}",color=hex_colors['blue'])
                    embed.description = sectorDescriptions[sector]
                    #webhook.add_embed(embed)

                    # Create a task for sending the webhook message to the corresponding sector channel
                    asyncio.create_task(build_sector_embed(data['stockSymbol'],webhook_url, embed))

async def consume_optionQuote():
    while True:
        data = await queues["optionQuote"].get()






async def consume_optionAgg():
    while True:
        data = await queues["optionAgg"].get()
        if data['accumulatedVolume'] >= 500:
            print(f"OOOOOOOOOOOOOOOOOOOOOO")





async def consume_stockAgg():
    while True:
        data = await queues["stockAgg"].get()
        if data['closePrice'] >= 5:
            print(f"KL")


# Setup the connection to PostgreSQL
conn = psycopg2.connect(
    dbname="mydb21",
    user="postgres",
    password="326058xX##",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS stockQuote;
DROP TABLE IF EXISTS optionTrade;
DROP TABLE IF EXISTS stockTrade;
DROP TABLE IF EXISTS optionAgg;
DROP TABLE IF EXISTS stockAgg;
DROP TABLE IF EXISTS optionQuote;
''')
conn.commit()


# Create the tables
cur.execute('''
CREATE TABLE stockQuote (
    type TEXT,
    stockSymbol TEXT,
    stockQuoteCondition TEXT,
    stockQuoteIndicator TEXT[],
    askPrice NUMERIC,
    bidPrice NUMERIC,
    askSize INTEGER,
    bidSize INTEGER,
    askExchange TEXT,
    bidExchange TEXT,
    quoteTimestamp TIMESTAMP
);

CREATE TABLE optionTrade (
    optionSymbol TEXT,
    type TEXT,
    tradeExchange TEXT,
    tradePrice NUMERIC,
    tradeSize INTEGER,
    tradeConditions TEXT[],
    tradeTimestamp TIMESTAMP
);

CREATE TABLE stockTrade (
    stockSymbol TEXT,
    type TEXT,
    tradeExchange TEXT,
    tradePrice NUMERIC,
    tradeSize INTEGER,
    tradeConditions TEXT[],
    tradeTimestamp TIMESTAMP
);

CREATE TABLE optionAgg (
    optionSymbol TEXT,
    type TEXT,
    closePrice NUMERIC,
    highPrice NUMERIC,
    lowPrice NUMERIC,
    openPrice NUMERIC,
    volume INTEGER,
    officialOpen INTEGER,
    accumulatedVolume INTEGER,
    vwapPrice INTEGER,
    aggTimestamp TIMESTAMP
);

CREATE TABLE stockAgg (
    type TEXT,
    stockSymbol TEXT,
    closePrice NUMERIC,
    highPrice NUMERIC,
    lowPrice NUMERIC,
    openPrice NUMERIC,
    volume INTEGER,
    officialOpen INTEGER,
    accumulatedVolume INTEGER,
    vwapPrice INTEGER,
    
    aggTimestamp TIMESTAMP
);

CREATE TABLE optionQuote (
    type TEXT,
    optionSymbol TEXT,
    stockQuoteCondition TEXT,
    stockQuoteIndicator TEXT[],
    askPrice NUMERIC,
    bidPrice NUMERIC,
    askSize INTEGER,
    bidSize INTEGER,
    askExchange TEXT,
    bidExchange TEXT,
    quoteTimestamp TIMESTAMP
);
''')
conn.commit()


async def handle_msg(msgs: WebSocketMessage):
    for m in msgs:
        data = None
        if isinstance(m, EquityTrade) and m.symbol.startswith('O:'):
            data = { 
                'optionSymbol': m.symbol,
                'type': 'optionTrade',
                'tradeExchange': OPTIONS_EXCHANGES.get(m.exchange),
                'tradePrice': m.price,
                'tradeSize': m.size,
                'tradeConditions': [optionConditionsDict.get(condition) for condition in m.conditions] if m.conditions is not None else [],
                'tradeTimestamp': datetime.fromtimestamp(m.trf_timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S') if m.trf_timestamp is not None else None
            }
            if data is not None:
                cur.execute(
                    "INSERT INTO optionTrade (optionSymbol, type, tradeExchange, tradePrice, tradeSize, tradeConditions, tradeTimestamp) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (data['optionSymbol'], data['type'], data['tradeExchange'], data['tradePrice'], data['tradeSize'], data['tradeConditions'], data['tradeTimestamp'])
                )  
        elif isinstance(m, EquityTrade) and not m.symbol[0].startswith('O:') and m.symbol in sublist1:
            data = { 
                'stockSymbol': m.symbol,
                'type': 'stockTrade',
                'tradeExchange': STOCK_EXCHANGES.get(m.exchange),
                'tradePrice': m.price,
                'tradeSize': m.size,
                'tradeConditions': [stock_condition_dict.get(condition) for condition in m.conditions] if m.conditions is not None else [],
                'tradeTimestamp': datetime.fromtimestamp(m.trf_timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S') if m.trf_timestamp is not None else None
            }
            if data is not None:
                cur.execute(
                    "INSERT INTO stockTrade (stockSymbol, type, tradeExchange, tradePrice, tradeSize, tradeConditions, tradeTimestamp) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (data['stockSymbol'], data['type'], data['tradeExchange'], data['tradePrice'], data['tradeSize'], data['tradeConditions'], data['tradeTimestamp']))
          
        elif isinstance(m, EquityAgg) and any(m.symbol.startswith('O:') and m.symbol.replace('O:', "").startswith(ticker) for ticker in sublist1):
        
            data = { 
                'optionSymbol': m.symbol,
                'type': 'optionAgg',
                'closePrice': m.close,
                'highPrice': m.high,
                'lowPrice': m.low,
                'openPrice': m.open,
                'volume': m.volume,
                'officialOpen': m.official_open_price,
                'accumulatedVolume': m.accumulated_volume,
                'vwapPrice': m.vwap,
                'aggTimestamp': datetime.fromtimestamp(m.end_timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S') if m.end_timestamp is not None else None
            }
            if data is not None:
                cur.execute(
                    "INSERT INTO optionAgg (optionSymbol, type, closePrice, highPrice, lowPrice, openPrice, volume, officialOpen, accumulatedVolume, vwapPrice, aggTimestamp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (data['optionSymbol'], data['type'], data['closePrice'], data['highPrice'], data['lowPrice'], data['openPrice'], data['volume'], data['officialOpen'], data['accumulatedVolume'], data['vwapPrice'], data['aggTimestamp'])
                )
        elif isinstance(m, EquityAgg) and not m.symbol.startswith('O:') and m.symbol in sublist1:
            data = {
                'stockSymbol': m.symbol,
                'type': 'stockAgg',
                'closePrice': m.close,
                'highPrice': m.high,
                'lowPrice': m.low,
                'openPrice': m.open,
                'volume': m.volume,
                'officialOpen': m.official_open_price,
                'accumulatedVolume': m.accumulated_volume,
                'vwapPrice': m.vwap,
                'aggTimestamp': datetime.fromtimestamp(m.end_timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S') if m.end_timestamp is not None else None
            }










            if data is not None:
                cur.execute(
                    "INSERT INTO stockAgg (stockSymbol, type, closePrice, highPrice, lowPrice, openPrice, volume, officialOpen, accumulatedVolume, vwapPrice, aggTimestamp) VALUES (%s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s)",
                    (data['stockSymbol'], data['type'], data['closePrice'], data['highPrice'], data['lowPrice'], data['openPrice'], data['volume'], data['officialOpen'], data['accumulatedVolume'], data['vwapPrice'], data['aggTimestamp'])
                )
        elif isinstance(m, EquityQuote) and m.symbol.startswith('O:'):
            data = { 
                'optionSymbol': m.symbol,
                'type': 'optionQuote',
                'askPrice': m.ask_price,
                'bidPrice': m.bid_price,
                'askSize': m.ask_size,
                'bidSize': m.bid_size,
                'askExchange': OPTIONS_EXCHANGES.get(m.ask_exchange_id),
                'bidExchange': OPTIONS_EXCHANGES.get(m.bid_exchange_id),
                'quoteTimestamp': datetime.fromtimestamp(m.timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S') if m.timestamp is not None else None
            }
            if data is not None:
                cur.execute(
                    "INSERT INTO optionQuote (optionSymbol, type, askPrice, bidPrice, askSize, bidSize, askExchange, bidExchange, quoteTimestamp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (data['optionSymbol'], data['type'], data['askPrice'], data['bidPrice'], data['askSize'], data['bidSize'], data['askExchange'], data['bidExchange'], data['quoteTimestamp'])
                )
        elif isinstance(m, EquityQuote) and not m.symbol.startswith('O:') and m.symbol in sublist1:
            data = { 
                'stockSymbol': m.symbol,
                'type': 'stockQuote',
                'askPrice': m.ask_price,
                'bidPrice': m.bid_price,
                'askSize': m.ask_size,
                'bidSize': m.bid_size,
                'stockQuoteCondition': quote_conditions.get(m.condition),
                'stockQuoteIndicator': [indicators.get(i) for i in m.indicators] if m.indicators is not None else [],
                'askExchange': STOCK_EXCHANGES.get(m.ask_exchange_id),
                'bidExchange': STOCK_EXCHANGES.get(m.bid_exchange_id),
                'quoteTimestamp': datetime.fromtimestamp(m.timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S') if m.timestamp is not None else None
            }
            if data is not None:
                cur.execute(
                    "INSERT INTO stockQuote (stockSymbol, type, askPrice, bidPrice, askSize, bidSize, stockQuoteCondition, stockQuoteIndicator, askExchange, bidExchange, quoteTimestamp) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (data['stockSymbol'],data['type'], data['askPrice'], data['bidPrice'], data['askSize'], data['bidSize'], data['stockQuoteCondition'], data['stockQuoteIndicator'], data['askExchange'], data['bidExchange'], data['quoteTimestamp'])
                )

        if data is not None:
            queue = queues.get(data['type'])
            if queue is not None:
                await queue.put(data)



async def main():
    # Queues for each data type
    queues = {
        "stockTrade": asyncio.Queue(),
        "optionTrade": asyncio.Queue(),
        "stockAgg": asyncio.Queue(),
        "optionAgg": asyncio.Queue(),
        "stockQuote": asyncio.Queue(),
        "optionQuote": asyncio.Queue(),
    }

    markets = [Market.Stocks, Market.Options]

    # Create websocket connections for each market
    connection_tasks = [
        asyncio.create_task(
            WebSocketClient(
                subscriptions=["T.*,Q.*,A.*"],
                api_key=YOUR_API_KEY,
                market=market,
            ).connect(
                lambda msg: asyncio.create_task(handle_msg(msg))  # Updated handle_msg function
            )
        )
        for market in markets
    ]

    # Create tasks for each queue consumer
    consumer_tasks = [
        asyncio.create_task(consume_stockTrade()),
        asyncio.create_task(consume_optionTrade()),
        asyncio.create_task(consume_stockAgg()),
        asyncio.create_task(consume_optionAgg()),
        asyncio.create_task(consume_stockQuote()),
        asyncio.create_task(consume_optionQuote()),
    ]

    # Await all tasks
    await asyncio.gather(*connection_tasks, *consumer_tasks)

asyncio.run(main())