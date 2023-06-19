import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

"""
Main Stock Market File
----------------------

This file utilizes the polygon.io real-time websocket cluster for stock market data analysis and processing.
All attributes pertaining to discord webhooks must be replaced with your discord's webhook URLs.
Attributes can be found in discord_utils/hooks/channel_webhooks. Replace "YOUR WEBHOOK URL" with the appropriate URL for your server.
"""

from polygon.websocket import WebSocketMessage,EquityTrade, WebSocketClient, Market
from asyncio import Queue
import asyncio
import numpy as np
##import SDKS, config files
from cfg import YOUR_API_KEY, five_days_from_now_str, five_days_ago_str
from discord_webhook import AsyncDiscordWebhook, DiscordEmbed
from sdks.polygon_sdk.technical_conditions import check_macd_condition_bearish, check_macd_condition_bullish,check_rsi_condition_bearish,check_rsi_condition_bullish
from cfg import today_str
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK, thresholds
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK

#different ticker-hooks to send ticker-specific messages to discord

from _discord.hooks.hook_dicts import (
    china_hooks,
    india_hooks,
    index_hooks,
    meme_hooks,
    russia_hooks,
    ETF_BROAD_MARKET_HOOKS
)

#this program will check for the following conditions in real-time. Replace the attribute name with your discord server's webhook URL.




from _discord.hooks.channel_webhooks import (
    sell,
    strongbuy,
    underperform,
    holdrating,
    oversold,
    overbought,
    overbought_1day,
    overbought_week,
    oversold_1day,
    oversold_week,
    eightypercent,
    tenorless,
    twentytoforty,
    fortytoeighty,
    onehundredplus,
    firesale,
    accumulate,
    neutzone,
    aboveavgvolume,
    belowavgvolume,
    fiftyhighh,
    fiftylowh,
    earningstoday,
    weekbanana,
    daybanana,
    hourbanana
)



polyoptions = PolygonOptionsSDK("YOUR API KEY") #replace with your polygon.io key - visit https://www.polygon.io to get a key. use code FUDSTOP at checkout for an exclusive discount.
polygon = AsyncPolygonSDK("YOUR API KEY") #replace with your polygon.io key - visit https://www.polygon.io to get a key. use code FUDSTOP at checkout for an exclusive discount.
webull = AsyncWebullSDK() #no key needed other than the headers for news functions






async def check_conditions(symbol, timespan):
    """
    This function checks the MACD and RSI conditions for a given stock symbol and timeframe in real-time. It also retrieves additional stock market data using the polygon.io and Webull SDKs combined.
    This function will accurately find iminent bullish MAC-D crossovers while the web-socket cluster is active.

    Webhooks used:
        >>> weekbanana: Tickers with iminent bullish MAC-D cross on the weekly timeframe. ('banana shape')
        >>> daybanana: Tickers with iminent bullish MAC-D cross on the daily timeframe. ('banana shape')
        >>> hourbanana: Tickers with iminent bullish MAC-D cross on the daily timeframe. ('banana shape')
    Parameters:
        symbol (str): The stock symbol to check the conditions for. (passed from the websocket)
        
        timespan (str): The timeframe to check the conditions for.
    
    Returns:
        Webhook messages to discord when the conditions are met. (or terminal)
    """
    macd, hist, signal = await polygon.get_macd(symbol, timespan=timespan, limit=50)
    rsi = await polygon.get_rsi(symbol, timespan=timespan, limit=50)

    macd_condition = check_macd_condition_bullish(hist)
    rsi_condition = check_rsi_condition_bullish(rsi)
    stock_data = await webull.get_webull_stock_data(symbol)
    vol_anal = await webull.get_webull_vol_analysis_data(symbol)
    buy = float(vol_anal.buyVolume)
    sell = float(vol_anal.sellVolume)
    neut = float(vol_anal.nVolume)
    fiftyhigh = stock_data.fifty_high
    fiftylow = stock_data.fifty_low
    close = stock_data.web_stock_close
    high = stock_data.web_stock_high
    low = stock_data.web_stock_low
    open = stock_data.web_stock_open
    changeratio = round(float(stock_data.web_change_ratio)*100,2)
    vol = float(stock_data.web_stock_vol)
    vr = stock_data.web_vibrate_ratio
    
    
    ##scans incoming tickers and checks for MAC-D crossover on the weekly
    if macd_condition and rsi_condition and timespan == "week":
        print(f'{symbol} meets the MACD and RSI criteria for the week!')

        weekbananahook=AsyncDiscordWebhook(weekbanana)
        weekbananaembed = DiscordEmbed(title=f"🍌", description=f"> 🍌 **RIPE BANANA WITH OVERSOLD RSI!** 🍌", color=f"FFFF00")
        weekbananaembed.add_embed_field(name=f'Ticker:', value=f"> **{symbol}**\n\n> Timeframe: **WEEK**")
        weekbananaembed.add_embed_field(name=f"Day Stats", value=f"> Open: **${open}**\n> High: **${high}**\n> Last: **${close}**\n> Low: **${low}**\n> Change: **{changeratio}%**")
        weekbananaembed.add_embed_field(name=f"Volume Analysis:", value=f"> Buy: **{buy:,}**\n> Neut: **{neut:,}**\n> Sell: **{sell:,}**\n> Total: **{vol:,}**")
        weekbananaembed.add_embed_field(name="Year High/Low:", value=f"> High: **${fiftyhigh}**\n> Low: **${fiftylow}**")
        weekbananaembed.add_embed_field(name=f"Vibration:", value=f"> **{vr}**")
        weekbananahook.add_embed(weekbananaembed)
        await weekbananahook.execute()
    else:
        print(f"{symbol} does NOT meet criteria for the week.")
    
    ##scans incoming tickers and checks for MAC-D crossover on the daily
    if macd_condition and rsi_condition and timespan == "day":
        print(f'{symbol} meets the MACD and RSI criteria for the day!!')
        daybananahook=AsyncDiscordWebhook(daybanana)
        daybananaembed = DiscordEmbed(title=f"🍌", description=f"> 🍌 **RIPE BANANA WITH OVERSOLD RSI!** 🍌", color=f"FFFF00")
        daybananaembed.add_embed_field(name=f'Ticker:', value=f"> **{symbol}**\n\n> Timeframe: **DAY**")
        daybananaembed.add_embed_field(name=f"Day Stats", value=f"> Open: **${open}**\n> High: **${high}**\n> Last: **${close}**\n> Low: **${low}**\n> Change: **{changeratio}%**")
        daybananaembed.add_embed_field(name=f"Volume Analysis:", value=f"> Buy: **{buy:,}**\n> Neut: **{neut:,}**\n> Sell: **{sell:,}**\n> Total: **{vol:,}**")
        daybananaembed.add_embed_field(name="Year High/Low:", value=f"> High: **${fiftyhigh}**\n> Low: **${fiftylow}**")
        daybananaembed.add_embed_field(name=f"Vibration:", value=f"> **{vr}**")
        daybananahook.add_embed(daybananaembed)
        await daybananahook.execute()
    else:
        print(f"{symbol} does NOT meet criteria for the day.")

    ##scans incoming tickers and checks for MAC-D crossover on the hour
    if macd_condition and rsi_condition and timespan == "hour":
        print(f'{symbol} meets the MACD and RSI criteria for the hour!!')

        hourbananahook=AsyncDiscordWebhook(hourbanana, content="YOUR MESSAGE")
        hourbananaembed = DiscordEmbed(title=f"🍌", description=f"> 🍌 **RIPE BANANA WITH OVERSOLD RSI!** 🍌", color=f"FFFF00")
        hourbananaembed.add_embed_field(name=f'Ticker:', value=f"> **{symbol}**")
        hourbananaembed.add_embed_field(name=f"Timeframe:",value=f"> 1 HOUR! 🍌")
        hourbananahook.add_embed(hourbananaembed)
        await hourbananahook.execute()
    else:
        print(f"{symbol} does NOT meet criteria for the hour.")


async def process_analyst_ratings(symbol: str):
    """
    Process volume analysis and analyst ratings for a given stock symbol.
    Execute Discord webhooks based on the analyst rating suggestion.
    
    Utilizes the WebullSDK.
    
    Webhooks used:
        >>> strongbuy: Stocks with an overall analyst rating of STRONGBUY or BUY will be sent to the corresponding webhook.
        >>> buy: Stocks with an overall analyst rating of BUY will be sent to the corresponding webhook.
        >>> hold: Stocks with an overall analyst rating of HOLD will be sent to the corresponding webhook.
        >>> underperform: Stocks with an overall analyst rating of UNDERPERFORM will be sent to the corresponding webhook.
        >>> sell: Stocks with an overall analyst rating of SELL will be sent to the corresponding webhook.
    
    Parameters:
        symbol (str): The stock symbol to process the volume analysis for.
        (passed from the websocket)
    Returns:
        Webhook messages to discord when the conditions are met. (or terminal)
    """
    
    analyst_ratings = await webull.get_analysis_data(symbol) #get the analyst ratings
    
    if analyst_ratings is not None:
        rating_suggestion = analyst_ratings.rating_suggestion
        print(analyst_ratings.rating_suggestion)
        # Check if the rating_suggestion meets your criteria
        rating_info = {
            "underPerform": {
                "hook": AsyncDiscordWebhook(underperform, content="YOUR MESSAGE"),
                "color": "FFA500",
                "thumbnail": underperform
            },
            "buy": {
                "hook": AsyncDiscordWebhook(strongbuy, content="YOUR MESSAGE"),
                "color": "00FF00",
                "thumbnail": strongbuy
            },
            "strongBuy": {
                "hook": AsyncDiscordWebhook(strongbuy, content="YOUR MESSAGE"),
                "color": "00FF00",
                "thumbnail": strongbuy
            },
            "sell": {
                "hook": AsyncDiscordWebhook(sell, content="YOUR MESSAGE"),
                "color": "FF0000",
                "thumbnail": sell
            },
            "hold": {
                "hook": AsyncDiscordWebhook(holdrating, content="YOUR MESSAGE"),
                "color": "FFFFFF",
                "thumbnail": holdrating,
            }
        }
        
        if rating_suggestion in rating_info:
            rating = rating_info[rating_suggestion]
            message = f"Symbol {symbol} has a rating of {rating_suggestion}."
            embed = DiscordEmbed(title=f"Analyst Ratings - {symbol}", description=f"```py\n{symbol} currently has an overall analyst rating of {rating_suggestion}.```", color=rating["color"])
            embed.add_embed_field(name="Message:", value=f"> **{message}**")
            logo = await polygon.get_polygon_logo(symbol)
            if rating["thumbnail"] is not None:
                embed.set_thumbnail(rating["thumbnail"])
            embed.set_timestamp()
            rating["hook"].add_embed(embed)
            await rating["hook"].execute()
            print(rating_suggestion)
        else:
            print(f"Invalid rating suggestion {rating_suggestion} for symbol {symbol}")
    else:
        print(f"No analyst ratings found for symbol {symbol}")

        
async def process_rsi(symbol: str):
    """
    Process RSI (Relative Strength Index) for a given stock symbol on different timeframes.
    Execute Discord webhooks based on the RSI values.

    Webhooks used:

        >>> oversold: Returns tickers that are trading oversold on the 1-hour timeframe to their Discord Channel in real time. (30 or below)
        >>> overbought: Returns tickers that are trading overbought on the 1-hour timeframe to their Discord Channel in real time. (70 or above)
        >>> oversold_1day: Returns tickers that are trading oversold on the 1-day timeframe to their Discord Channel in real time. (30 or below)
        >>> overbought_1day: Returns tickers that are trading overbought on the 1-day timeframe to their Discord Channel in real time. (70 or above)
        >>> oversold_week: Returns tickers that are trading overbought on the 1-week timeframe to their Discord Channel in real time. (30 or below)
        >>> overbought_week: Returns tickers that are trading overbought on the 1-week timeframe to their Discord Channel in real time. (70 or above)

    Parameters:
        symbol (str): The stock symbol to process the RSI for. (passed from websocket)
        timespan: The timespan to scan. Choose from minute, day, hour, week, month, quarter, year

    Returns:
        Webhook messages to discord when the conditions are met. (or terminal)
    """
    rsihour = await polygon.get_rsi(ticker=symbol,timespan="hour")
    rsiday = await polygon.get_rsi(ticker=symbol,timespan="day")
    rsiweek = await polygon.get_rsi(ticker=symbol,timespan="week")
    
    if rsihour is not None and len(rsihour) > 0:
        if float(rsihour[0]) >= 70:
            overboughthook = AsyncDiscordWebhook(overbought, content= "YOUR MESSAGE")
            embed = DiscordEmbed(title=f"Overbought RSI {symbol}", description=f"```py\n{symbol} is currently trading with an overbought RSI of {round(float(rsihour[0]),2)} on the hour timeframe.```")
            embed.set_footer(text=f"{symbol} | Data provided by Polygon.io")
            overboughthook.add_embed(embed)
            await overboughthook.execute()

        elif float(rsihour[0]) <= 30:
            oversoldhook = AsyncDiscordWebhook(oversold, content= "YOUR MESSAGE")
            embed = DiscordEmbed(title=f"Oversold RSI {symbol}", description=f"```py\n{symbol} is currently trading with an oversold RSI of {round(float(rsihour[0]),2)} on the hour timeframe.```")
            embed.set_footer(text=f"{symbol} | Data provided by Polygon.io")
            oversoldhook.add_embed(embed)
            await oversoldhook.execute()

    if rsiday is not None and len(rsiday) > 0:
        if float(rsiday[0]) >= 70:
            overboughthook = AsyncDiscordWebhook(overbought_1day, content= "YOUR MESSAGE")
            embed = DiscordEmbed(title=f"Overbought RSI {symbol}", description=f"```py\n{symbol} is currently trading with an overbought RSI of {round(float(rsiday[0]),2)} on the hour timeframe.```")
            embed.set_footer(text=f"{symbol} | Data provided by Polygon.io")
            overboughthook.add_embed(embed)
            
            await overboughthook.execute()

        elif float(rsiday[0]) <= 30:
            oversoldhook = AsyncDiscordWebhook(oversold_1day, content= "YOUR MESSAGE")
            embed = DiscordEmbed(title=f"Oversold RSI {symbol}", description=f"```py\n{symbol} is currently trading with an oversold RSI of {round(float(rsiday[0]),2)} on the hour timeframe.```")
            embed.set_footer(text=f"{symbol} | Data provided by Polygon.io")
            oversoldhook.add_embed(embed)
            await oversoldhook.execute()

    if rsiweek is not None and len(rsiweek) > 0:
        if float(rsiweek[0]) >= 70:
            overboughthook = AsyncDiscordWebhook(overbought_week, content= "YOUR MESSAGE")
            embed = DiscordEmbed(title=f"Overbought RSI {symbol}", description=f"```py\n{symbol} is currently trading with an overbought RSI of {round(float(rsiweek[0]),2)} on the hour timeframe.```")
            embed.set_footer(text=f"{symbol} | Data provided by Polygon.io")
            overboughthook.add_embed(embed)
            
            await overboughthook.execute()

        elif float(rsiweek[0]) <= 30:
            oversoldhook = AsyncDiscordWebhook(oversold_week, content= "YOUR MESSAGE")
            embed = DiscordEmbed(title=f"Oversold RSI {symbol}", description=f"```py\n{symbol} is currently trading with an oversold RSI of {round(float(rsiweek[0]),2)} on the hour timeframe.```")
            embed.set_footer(text=f"{symbol} | Data provided by Polygon.io")
            oversoldhook.add_embed(embed)
            
            await oversoldhook.execute()


async def process_ownersip(symbol: str):
    """
    Process institutional ownership data for a given stock symbol using the WebullSDK.
    Execute Discord webhooks based on the institutional ownership ratio.

    Webhooks used:
        >>> onehundredplus: Returns tickers with institutional ownership exceeding 100% of the outstanding shares.
        >>> eightypercent: Returns tickers with institutional ownership of 80% or more of the outstanding shares.
        >>> fortytoeighty: Returns tickers with institutional ownership of 40-80% of the outstanding shares.
        >>> twentytoforty: Returns tickers with institutional ownership of 20-40% of the outstanding shares.
        >>> tenorless: Returns tickers with institutional ownership of 10% or less of the outstanding shares.
        

    Parameters:
        symbol (str): The stock symbol to process the ownership data for. (passed from websocket stream)

    Returns:
        Webhook messages to discord when the conditions are met. (or terminal)
    """

    inst = await webull.get_institutional_holdings(symbol)
    if inst is not None:
        ratio = round(float(inst.institution_holding.stat.holding_ratio)*100,2)
        print(ratio)


        if ratio is not None and ratio >= 80:
            ownership80 = AsyncDiscordWebhook(eightypercent)
            ownershipembed80 = DiscordEmbed(title=f"Institutional Ownership - {symbol}", description=f"```py\n{symbol} currently has an institutional ownership ratio of {ratio}%.```")
            logo = await polygon.get_polygon_logo(symbol)
            ownershipembed80.set_thumbnail(logo)
            ownershipembed80.set_timestamp()
            ownershipembed80.set_footer(text=f"{symbol} | Data provided by Polygon.io")
            ownership80.add_embed(ownershipembed80)

            await ownership80.execute()
            await asyncio.sleep(5)  # Pause for 5 seconds before proceeding to prevent rate issues with discord.
            
        if ratio is not None and ratio  >= 50 and ratio < 80:
            ownership50 = AsyncDiscordWebhook(fortytoeighty)
            ownershipembed50 = DiscordEmbed(title=f"Institutional Ownership - {symbol}", description=f"```py\n{symbol} currently has an institutional ownership ratio of {ratio}%.```")
            logo = await polygon.get_polygon_logo(symbol)
            ownershipembed50.set_thumbnail(logo)
            ownershipembed50.set_timestamp()
            ownershipembed50.set_footer(text=f"{symbol} | Data provided by Polygon.io")
            ownership50.add_embed(ownershipembed50)

            await ownership50.execute()
            await asyncio.sleep(5)  # Pause for 5 seconds before proceeding to prevent rate issues with discord.

        if ratio is not None and ratio  >= 20 and ratio < 50:
            ownership = AsyncDiscordWebhook(twentytoforty)
            ownershipembed = DiscordEmbed(title=f"Institutional Ownership -", description=f"```py\n{symbol} currently has an institutional ownership ratio of {ratio}%.```")
            logo = await polygon.get_polygon_logo(symbol)
            ownershipembed.set_thumbnail(logo)
            ownershipembed.set_timestamp()
            ownershipembed.set_footer(text=f"{symbol} | Data provided by Polygon.io")
            ownership.add_embed(ownershipembed)

            await ownership.execute()
            await asyncio.sleep(5)  # Pause for 5 seconds before proceeding to prevent rate issues with discord.

        if ratio is not None and ratio < 20:
            ownership20 = AsyncDiscordWebhook(tenorless)
            ownershipembed20 = DiscordEmbed(title=f"Institutional Ownership -", description=f"```py\n{symbol} currently has an institutional ownership ratio of {ratio}%.```")
            logo = await polygon.get_polygon_logo(symbol)
            ownershipembed20.set_thumbnail(logo)
            ownershipembed20.set_timestamp()
            ownershipembed20.set_footer(text=f"{symbol} | Data provided by Polygon.io")
            ownership20.add_embed(ownershipembed20)

            await ownership20.execute()
            await asyncio.sleep(5)  # Pause for 5 seconds before proceeding to prevent rate issues with discord.

        if ratio is not None and ratio >= 100:
            ownership100 = AsyncDiscordWebhook(onehundredplus)
            ownershipembed100 = DiscordEmbed(title=f"Institutional Ownership -", description=f"```py\n{symbol} currently has an institutional ownership ratio of {ratio}%.```")
            logo = await polygon.get_polygon_logo(symbol)
            ownershipembed100.set_thumbnail(logo)
            ownershipembed100.set_timestamp()
            ownershipembed100.set_footer(text=f"{symbol} | Data provided by Polygon.io")
            ownership100.add_embed(ownershipembed100)

            await ownership100.execute()
            await asyncio.sleep(5)  # Pause for 5 seconds before proceeding to prevent rate issues with discord.

async def process_webull_data(symbol: str):
    """
    Process Webull data for a given stock symbol.
    Execute Discord webhooks based on different data conditions.

    Webhooks used:
        >>> fiftyhigh: Returns tickers to discord pushing their 52-week highs.
        >>> fiftylow: Returns tickers to discord pushing their 52-week lows.
            
        >>> firesale: Stocks with 75% or more of the overall volume recorded as SELL volume will be sent to the corresponding webhook..
        >>> accumulation: Stocks with 75% or more of the overall volume recorded as BUY volume will be sent to the corresponding webhook.
        >>> neutzone: Stocks with 75% or more of the overall volume recorded as NEUTRAL volume will be sent to the corresponding webhook.
        
        >>> earningstoday: Stocks with earnings expected to be reporting for the current day. (After-Hours only unless you start the socket stream in pre-market)
        
        >>> fin_scorebad: Tickers with calculated financial ratios that don't meet industry standards.
        >>> fin_scoregood: Tickers with calculated financial ratios that exceed industry standards.
    Parameters:
        symbol (str): The stock symbol to process the Webull data for.

    Returns:
        Webhook messages to discord when the conditions are met. (or terminal)
    """
    webull_data = await webull.get_webull_vol_analysis_data(symbol)
    stock_data = await webull.get_webull_stock_data(symbol)
    fiftyhigh=stock_data.fifty_high
    fiftylow=stock_data.fifty_low
    next_er=stock_data.last_earnings
    close=stock_data.web_stock_close
    high=stock_data.web_stock_high
    low=stock_data.web_stock_low
    open=stock_data.web_stock_open
    changeratio=stock_data.web_change_ratio
    buy = webull_data.buyVolume
    sell = webull_data.sellVolume
    neut = webull_data.nVolume
    totalvol = webull_data.totalVolume
    avg_price = webull_data.avePrice
    avgvol = stock_data.avg_10d_vol
    avg3mvol = stock_data.avg_vol3m
    out_shares = stock_data.outstanding_shares
    name = stock_data.web_name
    total_shares = stock_data.total_shares


    if close == fiftyhigh:
        fiftyhighhook = AsyncDiscordWebhook(fiftyhighh)
        fiftyhighembed = DiscordEmbed(title=f"52 Week Highs!", description=f"```py\n{symbol} is pushing its' 52 week high!```", color="800000")
        fiftyhighembed.add_embed_field(name=f"Change Ratio:", value=f"> **{round(float(changeratio)*100,2)}%**")
        fiftyhighembed.add_embed_field(name=f"52 Stats:", value=f"> 52High: **${fiftyhigh}**\n> Current: **${close}**\n> 52low: **${fiftylow}**")
        fiftyhighembed.add_embed_field(name=f"Volume Analysis:", value=f"> Buy: **{float(buy):,}**\n> Neut: **{float(neut):,}**\n> Sell: **{float(sell):,}**\n> Total: **{float(totalvol):,}**")
        fiftyhighembed.add_embed_field(name=f"Next ER:", value=f"> **{next_er}**")
        fiftyhighhook.add_embed(fiftyhighembed)
        fiftyhighembed.set_footer(text=f"{symbol} | Data provided by Polygon.io")
        await fiftyhighhook.execute()

    if close == fiftylow:
        fiftylowhook = AsyncDiscordWebhook(fiftylowh)
        fiftylowembed = DiscordEmbed(title=f"52 Week Highs!", description=f"```py\n{symbol} is pushing its' 52 week low!", color="FFA500")
        fiftylowembed.add_embed_field(name=f"Change Ratio:", value=f"> **{round(float(changeratio)*100,2)}%**")
        fiftylowembed.add_embed_field(name=f"52 Stats:", value=f"> 52High: **${fiftyhigh}**\n> Current: **${close}**\n> 52low: **${fiftylow}**")
        fiftylowembed.add_embed_field(name=f"Volume Analysis:", value=f"> Buy: **{float(buy):,}**\n> Neut: **{float(neut):,}**\n> Sell: **{float(sell):,}**\n> Total: **{float(totalvol):,}**")
        fiftylowembed.add_embed_field(name=f"Next ER:", value=f"> **{next_er}**")
        fiftylowhook.add_embed(fiftylowembed)
        fiftylowembed.set_footer(text=f"{symbol} | Data provided by Polygon.io")
        await fiftylowhook.execute()


    if buy >= (0.75 * totalvol):
        accumulatehook = AsyncDiscordWebhook(accumulate)
        accumulateembed = DiscordEmbed(title=f"Accumulation of Stock", description=f"> **{symbol} currently has 75% or more of the total volume on the day recorded as BUY volume.**", color="00FF00")
        accumulateembed.add_embed_field(name=f"Volume Analysis:",value=f"> Buy: **{float(buy):,}**\n> Neut: **{float(neut):,}**\n> Sell: **{float(sell):,}**\n> Total: **{float(totalvol):,}**")
        accumulateembed.add_embed_field(name=f"Avg. Price:", value=f"> **${avg_price}**")
        accumulateembed.add_embed_field(name=f"Day Stats:", value=f"> Open: **${open}**\n> High: **${high}**\n> Last: **${close}**\n> Low: **${low}**\n> Change%: **{round(float(changeratio)*100,2)}%**")
        accumulateembed.add_embed_field(name=f"52week High / Low:",value=f"> High: **${fiftyhigh}**\n> Low: **${fiftylow}**")
        accumulateembed.add_embed_field(name=f"Next ER:", value=f"> **{next_er}**")
        accumulateembed.set_footer(text=f"{symbol} | Data provided by polygon.io. Use code FUDSTOP at checkout")
        accumulatehook.add_embed(accumulateembed)
        await accumulatehook.execute()

    if sell >= (0.75 * totalvol):
        firesalehook = AsyncDiscordWebhook(firesale)
        firesaleembed = DiscordEmbed(title=f"Catipulation of Stock", description=f"> **{symbol} currently has 75% or more of the total volume on the day recorded as SELL volume.**", color="FF0000")
        firesaleembed.add_embed_field(name=f"Volume Analysis:",value=f"> Buy: **{float(buy):,}**\n> Neut: **{float(neut):,}**\n> Sell: **{float(sell):,}**\n> Total: **{float(totalvol):,}**")
        firesaleembed.add_embed_field(name=f"Avg. Price:", value=f"> **${avg_price}**")
        firesaleembed.add_embed_field(name=f"Day Stats:", value=f"> Open: **${open}**\n> High: **${high}**\n> Last: **${close}**\n> Low: **${low}**\n> Change%: **{round(float(changeratio)*100,2)}%**")
        firesaleembed.add_embed_field(name=f"52week High / Low:",value=f"> High: **${fiftyhigh}**\n> Low: **${fiftylow}**")
        firesaleembed.add_embed_field(name=f"Next ER:", value=f"> **{next_er}**")
        firesaleembed.set_footer(text=f"{symbol} | Data provided by polygon.io. Use code FUDSTOP at checkout")
        firesalehook.add_embed(firesaleembed)
        await firesalehook.execute()

    if neut >= (0.75 * totalvol):
        neutzonehook = AsyncDiscordWebhook(neutzone)
        neutzoneembed = DiscordEmbed(title=f"Holding the Stock", description=f"> **{symbol} currently has 75% or more of the total volume on the day recorded as NEUTRAL volume.**", color="808080")
        neutzoneembed.add_embed_field(name=f"Volume Analysis:",value=f"> Buy: **{float(buy):,}**\n> Neut: **{float(neut):,}**\n> Sell: **{float(sell):,}**\n> Total: **{float(totalvol):,}**")
        neutzoneembed.add_embed_field(name=f"Avg. Price:", value=f"> **${avg_price}**")
        neutzoneembed.add_embed_field(name=f"Day Stats:", value=f"> Open: **${open}**\n> High: **${high}**\n> Last: **${close}**\n> Low: **${low}**\n> Change%: **{round(float(changeratio)*100,2)}%**")
        neutzoneembed.add_embed_field(name=f"52week High / Low:",value=f"> High: **${fiftyhigh}**\n> Low: **${fiftylow}**")
        neutzoneembed.add_embed_field(name=f"Next ER:", value=f"> **{next_er}**")
        neutzoneembed.set_footer(text=f"{symbol} | Data provided by polygon.io. Use code FUDSTOP at checkout")
        neutzonehook.add_embed(neutzoneembed)
        await neutzonehook.execute()


    if float(totalvol) >= (1.5 * float(avgvol)):
        aboveavghook = AsyncDiscordWebhook(aboveavgvolume)
        aboveavghookembed = DiscordEmbed(title=f"Above Average Volume", description=f"> **{symbol} is currently trading 1.5x above its' 10 day average volume.**", color="FF00FF")
        aboveavghookembed.add_embed_field(name=f"Volume Analysis:",value=f"> Buy: **{float(buy):,}**\n> Neut: **{float(neut):,}**\n> Sell: **{float(sell):,}**\n> Total: **{float(totalvol):,}**")
        aboveavghookembed.add_embed_field(name=f"Avg. Price:", value=f"> **${avg_price}**")
        aboveavghookembed.add_embed_field(name=f"Day Stats:", value=f"> Open: **${open}**\n> High: **${high}**\n> Last: **${close}**\n> Low: **${low}**\n> Change%: **{round(float(changeratio)*100,2)}%**")
        aboveavghookembed.add_embed_field(name=f"52week High / Low:",value=f"> High: **${fiftyhigh}**\n> Low: **${fiftylow}**")
        aboveavghookembed.add_embed_field(name=f"Next ER:", value=f"> **{next_er}**")
        aboveavghookembed.add_embed_field(name=f"Volume Snapshot:", value=f"> Avg: **{float(avgvol):,}**\n> VS.\n> Current: **{float(totalvol):,}**")
        aboveavghookembed.set_footer(text=f"{symbol} | Data provided by polygon.io. Use code FUDSTOP at checkout")
        aboveavghook.add_embed(aboveavghookembed)
        await aboveavghook.execute()

    if next_er == today_str:
        financial_score = await webull.financial_score(symbol)
        print(financial_score)
        earnings_today = AsyncDiscordWebhook(earningstoday)
        earnings_todayembed = DiscordEmbed(title=f"Earnings Today", description=f"```py\n{symbol} reportedly has earnings today.```")
        earnings_today.add_embed(earnings_todayembed)
        earnings_todayembed.set_footer(text=f"{symbol} | Data provided by polygon.io. Use code FUDSTOP at checkout")
        await earnings_today.execute()



    if next_er is not None and next_er is not "" and next_er <= five_days_from_now_str:
        logo = await polygon.get_polygon_logo(symbol)
        
        result= await webull.financial_score(symbol)
        print(result)        
        


        if result is not None:
                        # Print the result for each ratio
            output_list = []
            for k, v in result.items():
                check = ":white_check_mark:" if isinstance(v, float) and thresholds.get(k) and isinstance(thresholds[k], tuple) and thresholds[k][0] <= v <= thresholds[k][1] or isinstance(thresholds.get(k), (int, float)) and (isinstance(v, float) and thresholds.get(k) is not None and float(v) >= thresholds[k] or not isinstance(v, float) and thresholds.get(k, 0) == 0) else ":x:"
                if isinstance(v, float):
                    output_list.append(f"{check} **{k}: {float(v):,.2f}**")
                elif v is None:
                    output_list.append(f"{check} **{k}: N/A**")
                else:
                    output_list.append(f"{check} **{k}: {v}**")

                    if result['score'] is not None and result['score'] > 11:
                    
                        fin_scoregood = AsyncDiscordWebhook("YOUR WEBHOOK URL")
                        description = '\n'.join(output_list)
                        fin_scoreembed = DiscordEmbed(title=f"Earnings Soon! with Score", description=description, color="00FF00")
                        fin_scoreembed.set_thumbnail(logo)
                        fin_scoreembed.add_embed_field(name=f"Company Name:", value=f"> **{name}**\n> Outstanding Shares: **{float(out_shares):,}**\n> Total Shares: **{float(total_shares):,}**")
                        fin_scoreembed.add_embed_field(name=f"Day Stats:", value=f"> Open: **${open}**\n> High: **${high}**\n> Last: **${close}**\n> Low: **${low}**\n> Avg Price: **${avg_price}**\n\n> Change: **{round(float(changeratio)*100,2)}%**")
                        fin_scoreembed.add_embed_field(name=f"Vol. Analysis:", value=f"> Buy: **{float(buy):,}**\nNeut: **{float(neut):,}**\n> Sell: **{float(sell):,}**\n> Total: **{float(totalvol):,}**")
                        fin_scoreembed.add_embed_field(name=f"52week Stats:", value=f"> 52high: **${fiftyhigh}**\n> 52low: **${fiftylow}**")
                        fin_scoreembed.set_footer(text=f"{symbol} | Data provided by polygon.io. Use code FUDSTOP at checkout")
                        fin_scoregood.add_embed(fin_scoreembed)
                        await fin_scoregood.execute()
                    if result['score'] is not None and result['score'] < 6:
                        fin_scorebad = AsyncDiscordWebhook("YOUR WEBHOOK_URL")
                        description = '\n'.join(output_list)
                        fin_scoreembed = DiscordEmbed(title=f"Earnings Soon! with Score", description=description, color="FF0000")
                        fin_scoreembed.set_thumbnail(logo)
                        fin_scoreembed.add_embed_field(name=f"Company Name:", value=f"> **{name}**\n> Outstanding Shares: **{float(out_shares):,}**\n> Total Shares: **{float(total_shares):,}**")
                        fin_scoreembed.add_embed_field(name=f"Day Stats:", value=f"> Open: **${open}**\n> High: **${high}**\n> Last: **${close}**\n> Low: **${low}**\n> Avg Price: **${avg_price}**\n\n> Change: **{round(float(changeratio)*100,2)}%**")
                        fin_scoreembed.add_embed_field(name=f"Vol. Analysis:", value=f"> Buy: **{float(buy):,}**\nNeut: **{float(neut):,}**\n> Sell: **{float(sell):,}**\n> Total: **{float(totalvol):,}**")
                        fin_scoreembed.add_embed_field(name=f"52week Stats:", value=f"> 52high: **${fiftyhigh}**\n> 52low: **${fiftylow}**")
                        fin_scoreembed.set_footer(text=f"{symbol} | Data provided by polygon.io. Use code FUDSTOP at checkout")
                        fin_scorebad.add_embed(fin_scoreembed)
                        await fin_scorebad.execute()


async def process_hour_mas(symbol:str):
    """
    Processes the 251, 200, 50, and 21 moving averages in real-time to
    check for breakout / breakdown criteria and then send the ticker that
    meets criteria to Discord in real time.
    
    Webhooks used:
        >>> breakouts: Sends tickers that meet breakout (bullish) criteria to Discord.
        >>> breakdowns: Sends tickers that meet breakdown (bearish) criteria to Discord.

    Parameters:
        symbol (str): The stock symbol to process the moving averages for.
        (passed from websocket connection)
    Returns:
        Webhook messages to discord when the conditions are met. (or terminal)
    """
    
    data = await webull.get_webull_stock_data(symbol)
    close = data.web_stock_close
    high = data.web_stock_high
    open = data.web_stock_open
    low = data.web_stock_low
    ma21 = await polygon.get_simple_moving_average(symbol,timespan="day", window=21)
    ma50 = await polygon.get_simple_moving_average(symbol,timespan="day", window= 50)
    ma200 = await polygon.get_simple_moving_average(symbol,timespan="day", window= 200)
    ma251 = await polygon.get_simple_moving_average(symbol,timespan= "day", window= 251)
    
    hourma21 = await polygon.get_simple_moving_average(symbol,timespan="hour", window=21)
    hourma50 = await polygon.get_simple_moving_average(symbol,timespan="hour", window= 50)
    hourma200 = await polygon.get_simple_moving_average(symbol,timespan="hour", window= 200)
    hourma251 = await polygon.get_simple_moving_average(symbol,timespan= "hour", window= 251)
 
    if (
        ma21 is not None
        and ma50 is not None
        and ma200 is not None
        and ma251 is not None
        and hourma21 is not None
        and hourma50 is not None
        and hourma200 is not None
        and hourma251 is not None
    ):
        if (
            np.all(ma21 > ma50)
            and np.all(ma50 > ma200)
            and np.all(ma200 > ma251)
            and np.all(hourma21 > hourma50)
            and np.all(hourma50 > hourma200)
            and np.all(hourma200 > hourma251)
        ):
            breakouts = AsyncDiscordWebhook("YOUR WEBHOOK URL") #replace with your URL
            breakoutembed = DiscordEmbed(title=f"Stock Breakouts", description=f"```py\nA stock breakout is detected! The shorter-term moving averages are above the longer-term ones, indicating a potential upward trend. Always perform your own research before making any investment decisions. NFA.```", color="00FF00")
            breakoutembed.add_embed_field(name=f"Ticker:", value=f"```py\n{symbol}```")
            breakoutembed.add_embed_field(name=f"DAILY MAS", value=f"> MA 252: **{round(float(ma251[0]),2)}**\n> MA 200: **{round(float(ma200[0]),2)}**\n> MA 50: **{round(float(ma50[0]),2)}**\n> MA 21: **{round(float(ma21[0]),2)}**")
            breakoutembed.add_embed_field(name=f"HOURLY MAS", value=f"> H-MA 252: **{round(float(hourma251[0]),2)}**\n> H-MA 200: **{round(float(hourma200[0]),2)}**\n> H-MA 50: **{round(float(hourma50[0]),2)}**\n> H-MA 21: **{round(float(hourma21[0]),2)}**")
            breakoutembed.add_embed_field(name=f"Breakout Reason:", value=f"The 21-day MA is above the 50-day MA, which is above the 200-day MA, and the 200-day MA is above the 251-day MA. This indicates a strong upward trend.")
            breakoutembed.add_embed_field(name=f"Stats:", value=f"> Day Open: **${open}**\n> Day High: **${high}**\n> Last: **${close}**\n> Day Low: **${low}**")
            breakouts.add_embed(breakoutembed)
            await breakouts.execute()
        elif (
            np.all(ma21 < ma50)
            and np.all(ma50 < ma200)
            and np.all(ma200 < ma251)
            and np.all(hourma21 < hourma50)
            and np.all(hourma50 < hourma200)
            and np.all(hourma200 < hourma251)
        ):
            breakdowns = AsyncDiscordWebhook("YOUR WEBHOOK URL") #replace with your URL
            breakdownembed = DiscordEmbed(title=f"Stock Breakdowns", description=f"```py\nA stock breakdown is detected! The shorter-term moving averages are below the longer-term ones, indicating a potential downward trend. Always perform your own research before making any investment decisions. NFA.```", color="FF0000")
            breakdownembed.add_embed_field(name=f"Ticker:", value=f"```py\n{symbol}```")
            breakdownembed.add_embed_field(name=f"DAILY MAS", value=f"> MA 252: **{round(float(ma251[0]),2)}**\n> MA 200: **{round(float(ma200[0]),2)}**\n> MA 50: **{round(float(ma50[0]),2)}**\n> MA 21: **{round(float(ma21[0]),2)}**")
            breakdownembed.add_embed_field(name=f"HOURLY MAS", value=f"> H-MA 252: **{round(float(hourma251[0]),2)}**\n> H-MA 200: **{round(float(hourma200[0]),2)}**\n> H-MA 50: **{round(float(hourma50[0]),2)}**\n> H-MA 21: **{round(float(hourma21[0]),2)}**")
            breakdownembed.add_embed_field(name=f"Breakdown Reason:", value=f"The 21-day MA is below the 50-day MA, which is below the 200-day MA, and the 200-day MA is below the 251-day MA. This indicates a strong downward trend.")
            breakdownembed.add_embed_field(name=f"Stats:", value=f"> Day Open: **${open}**\n> Day High: **${high}**\n> Last: **${close}**\n> Day Low: **${low}**")
            breakdowns.add_embed(breakdownembed)
            await breakdowns.execute()
    print("Moving averages are diverging (potential reversal)")

async def process_big_trades(symbol: str, size: float):
    """
    Processes big trades with a threshold that you can set and then returns the data to the 
    corresponding 'ticker' Discord channel. Default: 10,000 shares
    
    Webhooks used:
        >>> Webhooks found in the 'india_adrs' dictionary for india tickers.
        >>> Webhooks found in the 'china_adrs' dictionary for china tickers.
        >>> Webhooks found in the 'index_tickers' dictionary for index tickers.
        >>> Webhooks found in the 'ETF_AND_BROAD_MARKET' dictionary for etf and broad-market tickers.
        
        >>> webhooks can be found in: discord_utils/hooks/channel_webhooks. 
        >>> You will need to replace with the appropriate channel
            URL from your server.
    
    Parameters:
        symbol (str): The stock symbol to process the moving averages for.
        (passed from websocket connection)
    Returns:
        Webhook messages to discord when the trade conditions are met. (or terminal)
    """

    snapshot = await polygon.get_stock_snapshot(symbol)
    if snapshot is not None:
        if snapshot.stock_last_quote is not None:
            askprice = snapshot.last_quote_ask_price
            bidprice = snapshot.last_quote_bid_price
            asksize = snapshot.last_quote_ask_size
            bidsize = snapshot.last_quote_bid_size
        else:
            print("Error: stock_last_quote is None")
        
        price=snapshot.last_trade_price
        size=snapshot.last_trade_size
        prevclose = snapshot.prev_day_close
        prevopen = snapshot.prev_day_open
        prevhigh = snapshot.prev_day_high
        prevlow = snapshot.prev_day_low
        prevvol = snapshot.prev_day_volume
        prevvwap = snapshot.prev_day_vwap
        vwap = snapshot.stock_vw
        vol = snapshot.stock_v
        high = snapshot.stock_h
        close = snapshot.stock_c
        low = snapshot.stock_l
        changep = snapshot.stock_changep
    hook_dicts = [china_hooks, index_hooks, meme_hooks, india_hooks, russia_hooks, ETF_BROAD_MARKET_HOOKS]
    for hooks in hook_dicts: 
        if symbol in hooks and size >= 10000: #change to desired threshold
            largetradehook = AsyncDiscordWebhook(hooks[symbol])
            embed = DiscordEmbed(title=f"LARGE TRADE DETECTED!", description=f"```py\nDAY STATS:```\n\n> Open: **${open}**\n> High: **${high}**\n> Last: **${close}**\n> Low: **${low}**\n\n> Volume: **{float(vol):,}**\n> VWAP: **${vwap}**", color="FFD700")
            embed.add_embed_field(name=f"LAST TRADE:", value=f"> Size: **{size:,}**\n> Price: **${price}**\n> Change on Day: **{changep}%**")
            embed.add_embed_field(name=f"LAST QUOTE:", value=f"> Ask: **${askprice}**\n> Ask Size: **{float(asksize):,}**\n> Bid: **${bidprice}**\n> Bid Size: **{float(bidsize):,}**")
            embed.add_embed_field(name=f"Previous Day:", value=f"> Open: **${prevopen}**\n> High: **${prevhigh}**\n> Close: **${prevclose}**\n> Low: **${prevlow}**\n\n> Volume: **{float(prevvol):,}**\n> VWAP: **${prevvwap}**")
            embed.set_footer(name=f"{symbol} | Data provided by polygon.io. Use code FUDSTOP at checkout")
            largetradehook.add_embed(embed)
            print("SENT")
            await largetradehook.execute()



async def handle_msg(msgs: WebSocketMessage, data_queue: Queue):
    """
    Handle incoming messages from a WebSocket stream and put relevant data into a queue to
    increase throughout.

    Parameters:
        msgs (WebSocketMessage): The incoming messages from the WebSocket stream.
        data_queue (Queue): The queue to put the extracted data into.

    Returns:
        Real-time websocket messages.
    """
    for m in msgs:
        if isinstance(m, EquityTrade):
            print(m)
            data = {
                "symbol": m.symbol,
                "accumulated_volume": m.price,
                "size": m.size,
                "aggregate_vwap": m.conditions,
                "official_open_price": m.exchange,
                "conditions": m.conditions
            }
            await data_queue.put(data)
            await process_big_trades(data["symbol"], data["size"])
async def process_conditions(symbol):
    """
    Process various conditions for a given stock symbol and
    run them concurrently.

    """
    await asyncio.gather(
        check_conditions(symbol, timespan="day"),
        check_conditions(symbol, timespan="hour"),
        check_conditions(symbol, timespan="week"),
    )
async def process_data(data_queue: Queue):
    """
    Process data from the data queue by executing various processing functions
    concurrently to increase message throughput.
    """
    while True:
        data = await data_queue.get()
        symbol = data['symbol']
        size = data['size']
        await asyncio.gather(
            process_rsi(symbol),
            process_analyst_ratings(symbol),
            process_ownersip(symbol),
            process_big_trades(symbol, size),
            process_webull_data(symbol),
        )
        await process_conditions(symbol) 

c = WebSocketClient(YOUR_API_KEY, Market.Stocks,verbose=True)
async def main():
    """
    Main function to run the data processing and handling tasks.
    With all default settings - should return around 2,5000 to 3,000 messages per hour
    to Discord scanning for all conditions herein.
    """

    data_queue = Queue()

    asyncio.create_task(c.connect(lambda msg: asyncio.create_task(handle_msg(msg, data_queue))))

    num_workers = 4  # You can adjust this value based on your requirements
    sdk_tasks = [
        process_data(data_queue) for _ in range(num_workers)
    ]

    await asyncio.gather(*sdk_tasks)

asyncio.run(main())
