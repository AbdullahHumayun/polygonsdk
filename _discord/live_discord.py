from polygon.websocket import WebSocketClient, WebSocketMessage, EquityAgg, Market, EquityTrade
from asyncio import Queue, BoundedSemaphore
import asyncio
import numpy as np
from sdks.polygon_sdk.technical_conditions import check_macd_condition_bearish,check_macd_condition_bullish,check_rsi_condition_bearish,check_rsi_condition_bullish

from _discord.embeddings import send_daybanana,send_hourbanana,send_weekbanana


from _discord.hooks.hook_dicts import china_hooks,india_hooks,index_hooks,meme_hooks,russia_hooks,ETF_BROAD_MARKET_HOOKS
from _discord.hooks.channel_webhooks import sell,strongbuy,underperform,holdrating, oversold,overbought, overbought_1day,overbought_week,oversold_1day,oversold_week, eightypercent,tenorless,twentytoforty,fortytoeighty, onehundredplus
from _discord.hooks.channel_webhooks import firesale,accumulate,neutzone, aboveavgvolume, belowavgvolume, fiftyhighh,fiftylowh, earningstoday, weekbanana,daybanana,hourbanana, lowfloat
c = WebSocketClient(YOUR_API_KEY, subscriptions=["T.*"], market= Market.Stocks)

from cfg import today_str, YOUR_API_KEY, five_days_from_now_str
from discord_webhook import AsyncDiscordWebhook, DiscordEmbed
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK, thresholds
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
polyoptions = PolygonOptionsSDK(YOUR_API_KEY)
polygon = AsyncPolygonSDK(YOUR_API_KEY)
webull = AsyncWebullSDK()
import logging
semaphore = BoundedSemaphore(10)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Master:
    def __init__(self, symbol=None):
        self.symbol = symbol


    async def check_conditions(symbol, timespan):
        timespans = ["week", "day", "hour"]
        conditions_met = {timespan: False for timespan in timespans}

        async def get_conditions(timespan):
            macd, hist, signal = await polygon.get_macd(symbol, timespan=timespan, limit=50)
            rsi = await polygon.get_rsi(symbol, timespan=timespan, limit=50)

            macd_condition = await check_macd_condition_bullish(hist)
            rsi_condition = await check_rsi_condition_bullish(rsi)

            return timespan, macd_condition and rsi_condition

        tasks = [get_conditions(timespan) for timespan in timespans]
        results = await asyncio.gather(*tasks)

        for timespan, met in results:
            conditions_met[timespan] = met


        tasks = []
        
        for timespan, met in conditions_met.items():
            if met:
                if timespan == "week":
                    tasks.append(send_weekbanana(symbol))
                elif timespan == "day":
                    print(f'{symbol} meets the MACD and RSI criteria for the day!!')
                    tasks.append(send_daybanana(symbol))
                elif timespan == "hour":
                    print(f'{symbol} meets the MACD and RSI criteria for the hour!!')
                    tasks.append(send_hourbanana(symbol))
                else:
                    print(f"{symbol} does NOT meet criteria for the hour.")
        
        if tasks:
            await asyncio.gather(*tasks)


    async def process_vol_analysis(self, symbol: str):


        analyst_ratings = await webull.get_analysis_data(symbol)
        
        if analyst_ratings is not None:
            rating_suggestion = analyst_ratings.rating_suggestion
            print(analyst_ratings.rating_suggestion)
      
            rating_info = {
                "underPerform": {
                    "hook": AsyncDiscordWebhook(underperform, content="<@375862240601047070>"),
                    "color": "FFA500",
                    "thumbnail": underperform
                },
                "buy": {
                    "hook": AsyncDiscordWebhook(strongbuy, content="<@375862240601047070>"),
                    "color": "00FF00",
                    "thumbnail": strongbuy
                },
                "strongBuy": {
                    "hook": AsyncDiscordWebhook(strongbuy, content="<@375862240601047070>"),
                    "color": "00FF00",
                    "thumbnail": strongbuy
                },
                "sell": {
                    "hook": AsyncDiscordWebhook(sell, content="<@375862240601047070>"),
                    "color": "FF0000",
                    "thumbnail": sell
                },
                "hold": {
                    "hook": AsyncDiscordWebhook(holdrating, content="<@375862240601047070>"),
                    "color": "FFFFFF",
                    "thumbnail": None
                }
            }
            
            if rating_suggestion in rating_info:
                rating = rating_info[rating_suggestion]
                message = f"Symbol {symbol} has a rating of {rating_suggestion}."
                embed = DiscordEmbed(title=f"Analyst Ratings - {symbol}", description=f"```py\n{symbol} currently has an overall analyst rating of {rating_suggestion}.```", color=rating["color"])
                embed.add_embed_field(name="Message:", value=f"> **{message}**")
                logo = await polygon.get_polygon_logo(symbol)
                if rating["thumbnail"] is not None:
                    embed.set_thumbnail(logo)
                embed.set_footer(text=f"{symbol} | Data provided by Polygon.io")
                embed.set_timestamp()
                rating["hook"].add_embed(embed)
                await rating["hook"].execute()
            else:
                print(f"Invalid rating suggestion {rating_suggestion} for symbol {symbol}")
        else:
            print(f"No analyst ratings found for symbol {symbol}")

async def process_rsi(symbol: str):
    rsihour_task = polygon.get_rsi(ticker=symbol, timespan="hour")
    rsiday_task = polygon.get_rsi(ticker=symbol, timespan="day")
    rsiweek_task = polygon.get_rsi(ticker=symbol, timespan="week")
    logo_task = polygon.get_polygon_logo(symbol)

    rsiday_tickers = set()
    rsiweek_tickers = set()

    rsihour, rsiday, rsiweek, logo = await asyncio.gather(rsihour_task, rsiday_task, rsiweek_task, logo_task)
    if rsihour is not None and len(rsihour) > 0:
        if float(rsihour[0]) >= 70:
            overboughthook = AsyncDiscordWebhook(overbought, content= "<@375862240601047070>")
            embed = DiscordEmbed(title=f"Overbought RSI {symbol}", description=f"```py\n{symbol} is currently trading with an overbought RSI of {round(float(rsihour[0]),2)} on the hour timeframe.```")
            embed.set_footer(text=f"{symbol} | Data provided by Polygon.io")
            embed.set_timestamp()
            overboughthook.add_embed(embed)
            await overboughthook.execute()

        elif float(rsihour[0]) <= 30:
            oversoldhook = AsyncDiscordWebhook(oversold, content= "<@375862240601047070>")
            embed = DiscordEmbed(title=f"Oversold RSI {symbol}", description=f"```py\n{symbol} is currently trading with an oversold RSI of {round(float(rsihour[0]),2)} on the hour timeframe.```")
            embed.set_footer(text=f"{symbol} | Data provided by Polygon.io")
            embed.set_thumbnail(logo)
            embed.set_timestamp()
            oversoldhook.add_embed(embed)
            await oversoldhook.execute()

    if rsiday is not None and len(rsiday) > 0:
        if float(rsiday[0]) >= 70:
            # If the ticker has already been processed today, skip it
            if symbol in rsiday_tickers:
                return

            # Add the ticker to the set of processed tickers
            rsiday_tickers.add(symbol)

            overboughthook = AsyncDiscordWebhook(overbought_1day, content= "<@375862240601047070>")
            embed = DiscordEmbed(title=f"Overbought RSI {symbol}", description=f"```py\n{symbol} is currently trading with an overbought RSI of {round(float(rsiday[0]),2)} on the hour timeframe.```")
            embed.set_footer(text=f"{symbol} | Data provided by Polygon.io")
            embed.set_timestamp()
            overboughthook.add_embed(embed)
            
            await overboughthook.execute()

        elif float(rsiday[0]) <= 30:
            if symbol in rsiday_tickers:
                return
            rsiday_tickers.add(symbol)
            oversoldhook = AsyncDiscordWebhook(oversold_1day, content= "<@375862240601047070>")
            embed = DiscordEmbed(title=f"Oversold RSI {symbol}", description=f"```py\n{symbol} is currently trading with an oversold RSI of {round(float(rsiday[0]),2)} on the hour timeframe.```")
            embed.set_footer(text=f"{symbol} | Data provided by Polygon.io")
            embed.set_timestamp()
            embed.set_thumbnail(logo)
            oversoldhook.add_embed(embed)
            await oversoldhook.execute()

    if rsiweek is not None and len(rsiweek) > 0:
        if float(rsiweek[0]) >= 70:
            if symbol in rsiweek_tickers:
                return
            rsiweek_tickers.add(symbol)
            overboughthook = AsyncDiscordWebhook(overbought_week, content= "<@375862240601047070>")
            embed = DiscordEmbed(title=f"Overbought RSI {symbol}", description=f"```py\n{symbol} is currently trading with an overbought RSI of {round(float(rsiweek[0]),2)} on the hour timeframe.```")
            embed.set_footer(text=f"{symbol} | Data provided by Polygon.io")
            overboughthook.add_embed(embed)
            
            await overboughthook.execute()

        elif float(rsiweek[0]) <= 30:
            if symbol in rsiweek_tickers:
                return
            rsiweek_tickers.add(symbol)
            oversoldhook = AsyncDiscordWebhook(oversold_week, content= "<@375862240601047070>")
            embed = DiscordEmbed(title=f"Oversold RSI {symbol}", description=f"```py\n{symbol} is currently trading with an oversold RSI of {round(float(rsiweek[0]),2)} on the hour timeframe.```")
            embed.set_footer(text=f"{symbol} | Data provided by Polygon.io")
            embed.set_thumbnail(logo)
            embed.set_timestamp()
            oversoldhook.add_embed(embed)
            
            await oversoldhook.execute()

processed_tickers = set()



async def process_low_float(symbol):
    data = await webull.get_webull_stock_data(symbol)
    logo = await polygon.get_polygon_logo(symbol)
    fifty_high = data.fifty_high
    fifty_low = data.fifty_low
    last_er=data.last_earnings
    outshares=data.outstanding_shares
    avgvol = data.avg_10d_vol
    totshares=data.total_shares
    changep=round(float(data.web_change_ratio)*100,2)
    name=data.web_name
    c=data.web_stock_close
    h=data.web_stock_high
    l=data.web_stock_low
    o=data.web_stock_open
    v=data.web_stock_vol
    if totshares is not None and totshares < 10000000:
        print(f"Outstanding Shares: {totshares['outstanding_shares']}")  # Debugging statement
        if totshares < 10000000:
            print("The total outstanding shares are less than 10 million.")
            low_floathook = AsyncDiscordWebhook(lowfloat, content="<@375862240601047070>")
            embed = DiscordEmbed(title=f"LOW FLOAT STOCKS", description=f"```py\nThis feed is returning tickers that have an outstanding share count of less than or equal to 10 million.```")
            embed.add_embed_field(name=f"{name}", value=f"> **{symbol}**")
            embed.add_embed_field(name=f"52week Stats:", value=f"> High: **${fifty_high}**\n> Now: **${c}**\n> Low: **${fifty_low}**")
            embed.add_embed_field(name=f"Day Stats:", value=f"> Open: **${o}**\n> High: **${h}**\n Last: **${c}**\n> Low: **${l}**")
            embed.add_embed_field(name=f"Volume Today:", value=f"> Total: **{float(v):,}**\n> 10d AVG: **{float(avgvol):,}**\n\n> Change on Day: **{changep}%**")
            embed.add_embed_field(name=f"Float:", value=f"> **{float(outshares)}**")
            embed.add_embed_field(name=f"Next ER:", value=f"```py\n{last_er}```")
            embed.set_thumbnail(logo)
            embed.set_timestamp()
            embed.set_footer(text=f"{symbol} | Data Provided by Polygon.io | Use code FUDSTOP at checkout.")
            low_floathook.add_embed(embed)
            await low_floathook.execute()

            
async def process_webull_data(symbol: str):
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
    logo = await polygon.get_polygon_logo(symbol)

    if close == fiftyhigh:
        fiftyhighhook = AsyncDiscordWebhook(fiftyhighh, content="<@375862240601047070>")
        fiftyhighembed = DiscordEmbed(title=f"52 Week Highs!", description=f"```py\n{symbol} is pushing its' 52 week high!```", color="800000")
        fiftyhighembed.add_embed_field(name=f"Change Ratio:", value=f"> **{round(float(changeratio)*100,2)}%**")
        fiftyhighembed.add_embed_field(name=f"52 Stats:", value=f"> 52High: **${fiftyhigh}**\n> Current: **${close}**\n> 52low: **${fiftylow}**")
        fiftyhighembed.add_embed_field(name=f"Volume Analysis:", value=f"> Buy: **{float(buy):,}**\n> Neut: **{float(neut):,}**\n> Sell: **{float(sell):,}**\n> Total: **{float(totalvol):,}**")
        fiftyhighembed.add_embed_field(name=f"Next ER:", value=f"> **{next_er}**")
        fiftyhighembed.set_timestamp()
        fiftyhighembed.set_footer(text=f"{symbol} | Data provided by Polygon.io")
        fiftyhighhook.add_embed(fiftyhighembed)

        await fiftyhighhook.execute()

    if close == fiftylow:
        fiftylowhook = AsyncDiscordWebhook(fiftylowh, content="<@375862240601047070>")
        fiftylowembed = DiscordEmbed(title=f"52 Week Highs!", description=f"```py\n{symbol} is pushing its' 52 week low!", color="FFA500")
        fiftylowembed.add_embed_field(name=f"Change Ratio:", value=f"> **{round(float(changeratio)*100,2)}%**")
        fiftylowembed.add_embed_field(name=f"52 Stats:", value=f"> 52High: **${fiftyhigh}**\n> Current: **${close}**\n> 52low: **${fiftylow}**")
        fiftylowembed.add_embed_field(name=f"Volume Analysis:", value=f"> Buy: **{float(buy):,}**\n> Neut: **{float(neut):,}**\n> Sell: **{float(sell):,}**\n> Total: **{float(totalvol):,}**")
        fiftylowembed.add_embed_field(name=f"Next ER:", value=f"> **{next_er}**")
        fiftylowembed.set_footer(text=f"{symbol} | Data provided by Polygon.io")
        fiftylowhook.add_embed(fiftylowembed)
        
        await fiftylowhook.execute()


    if buy >= (0.75 * totalvol):
        accumulatehook = AsyncDiscordWebhook(accumulate, content="<@375862240601047070>")
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
        firesalehook = AsyncDiscordWebhook(firesale, content="<@375862240601047070>")
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
        neutzonehook = AsyncDiscordWebhook(neutzone, content="<@375862240601047070>")
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
        aboveavghook = AsyncDiscordWebhook(aboveavgvolume, content="<@375862240601047070>")
        aboveavghookembed = DiscordEmbed(title=f"Above Average Volume", description=f"> **{symbol} is currently trading 1.5x above its' 10 day average volume.**", color="FF00FF")
        aboveavghookembed.add_embed_field(name=f"Volume Analysis:",value=f"> Buy: **{float(buy):,}**\n> Neut: **{float(neut):,}**\n> Sell: **{float(sell):,}**\n> Total: **{float(totalvol):,}**")
        aboveavghookembed.add_embed_field(name=f"Avg. Price:", value=f"> **${avg_price}**")
        aboveavghookembed.add_embed_field(name=f"Day Stats:", value=f"> Open: **${open}**\n> High: **${high}**\n> Last: **${close}**\n> Low: **${low}**\n> Change%: **{round(float(changeratio)*100,2)}%**")
        aboveavghookembed.add_embed_field(name=f"52week High / Low:",value=f"> High: **${fiftyhigh}**\n> Low: **${fiftylow}**")
        aboveavghookembed.add_embed_field(name=f"Next ER:", value=f"> **{next_er}**")
        aboveavghookembed.add_embed_field(name=f"Volume Snapshot:", value=f"> Avg: **{float(avgvol):,}**\n> VS.\n> Current: **{float(totalvol):,}**")
        aboveavghookembed.set_footer(text=f"{symbol} | Data provided by polygon.io. Use code FUDSTOP at checkout")
        aboveavghookembed.set_timestamp()
        aboveavghookembed.set_thumbnail(logo)
        aboveavghook.add_embed(aboveavghookembed)
        await aboveavghook.execute()

    if next_er == today_str:
        financial_score = await webull.financial_score(symbol)
        print(financial_score)
        earnings_today = AsyncDiscordWebhook(earningstoday, content="<@375862240601047070>")
        earnings_todayembed = DiscordEmbed(title=f"Earnings Today", description=f"```py\n{symbol} reportedly has earnings today.```")
        earnings_todayembed.set_footer(text=f"{symbol} | Data provided by polygon.io. Use code FUDSTOP at checkout")
        earnings_todayembed.set_timestamp()
        earnings_todayembed.set_thumbnail(logo)
        earnings_today.add_embed(earnings_todayembed)
        
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
                    
                        fin_scoregood = AsyncDiscordWebhook("https://discord.com/api/webhooks/1099711217628622858/5eqhKyCnNySog9CY1YqXvmOU_MWX4UB7fVWmOrDHHjTmhZjXGyi9yynMkt6L2CeYTOMR")
                        description = '\n'.join(output_list)
                        fin_scoreembed = DiscordEmbed(title=f"Earnings Soon! with Score", description=description, color="00FF00")
                        fin_scoreembed.set_thumbnail(logo)
                        fin_scoreembed.add_embed_field(name=f"Company Name:", value=f"> **{name}**\n> Outstanding Shares: **{float(out_shares):,}**\n> Total Shares: **{float(total_shares):,}**")
                        fin_scoreembed.add_embed_field(name=f"Day Stats:", value=f"> Open: **${open}**\n> High: **${high}**\n> Last: **${close}**\n> Low: **${low}**\n> Avg Price: **${avg_price}**\n\n> Change: **{round(float(changeratio)*100,2)}%**")
                        fin_scoreembed.add_embed_field(name=f"Vol. Analysis:", value=f"> Buy: **{float(buy):,}**\nNeut: **{float(neut):,}**\n> Sell: **{float(sell):,}**\n> Total: **{float(totalvol):,}**")
                        fin_scoreembed.add_embed_field(name=f"52week Stats:", value=f"> 52high: **${fiftyhigh}**\n> 52low: **${fiftylow}**")
                        fin_scoreembed.set_footer(text=f"{symbol} | Data provided by polygon.io. Use code FUDSTOP at checkout")
                        fin_scoreembed.set_timestamp()
                        fin_scoregood.add_embed(fin_scoreembed)
                        await fin_scoregood.execute()
                    if result['score'] is not None and result['score'] < 6:
                        badfin_scorebad = AsyncDiscordWebhook("https://discord.com/api/webhooks/1099714824704897024/Nv6hIaapicfCL2qh7fXGnplvC6rHITD5jjJxXfK9kAHt5pBOqSofcgQtSKwsFHaVvSPM")
                        baddescription = '\n'.join(output_list)
                        badfin_scoreembed = DiscordEmbed(title=f"Earnings Soon! with Score", description=baddescription, color="FF0000")
                        badfin_scoreembed.set_thumbnail(logo)
                        badfin_scoreembed.add_embed_field(name=f"Company Name:", value=f"> **{name}**\n> Outstanding Shares: **{float(out_shares):,}**\n> Total Shares: **{float(total_shares):,}**")
                        badfin_scoreembed.add_embed_field(name=f"Day Stats:", value=f"> Open: **${open}**\n> High: **${high}**\n> Last: **${close}**\n> Low: **${low}**\n> Avg Price: **${avg_price}**\n\n> Change: **{round(float(changeratio)*100,2)}%**")
                        badfin_scoreembed.add_embed_field(name=f"Vol. Analysis:", value=f"> Buy: **{float(buy):,}**\nNeut: **{float(neut):,}**\n> Sell: **{float(sell):,}**\n> Total: **{float(totalvol):,}**")
                        badfin_scoreembed.add_embed_field(name=f"52week Stats:", value=f"> 52high: **${fiftyhigh}**\n> 52low: **${fiftylow}**")
                        badfin_scoreembed.set_footer(text=f"{symbol} | Data provided by polygon.io. Use code FUDSTOP at checkout")
                        badfin_scoreembed.set_timestamp()
                        badfin_scorebad.add_embed(badfin_scoreembed)
                        await badfin_scorebad.execute()
async def process_ownersip(symbol: str):
    global processed_tickers
    # If the ticker has already been processed today, skip it
    if symbol in processed_tickers:
        return

    # Add the ticker to the set of processed tickers
    processed_tickers.add(symbol)
    inst = await webull.get_institutional_holdings(symbol)
    if inst is not None:
        ratio = round(float(inst.institution_holding.stat.holding_ratio)*100,2)
        print(ratio)


        if ratio is not None and ratio >= 80:
            ownership80 = AsyncDiscordWebhook(eightypercent, content= "<@375862240601047070>")
            ownershipembed80 = DiscordEmbed(title=f"Institutional Ownership - {symbol}", description=f"```py\n{symbol} currently has an institutional ownership ratio of {ratio}%.```")
            logo = await polygon.get_polygon_logo(symbol)
            ownershipembed80.set_thumbnail(logo)
            ownershipembed80.set_timestamp()
            ownershipembed80.set_footer(text=f"{symbol} | Data provided by Polygon.io")
            ownership80.add_embed(ownershipembed80)

            await ownership80.execute()
            await asyncio.sleep(5)  # Pause for 5 seconds before proceeding
        if ratio is not None and ratio  >= 50 and ratio < 80:
            ownership50 = AsyncDiscordWebhook(fortytoeighty, content= "<@375862240601047070>")
            ownershipembed50 = DiscordEmbed(title=f"Institutional Ownership - {symbol}", description=f"```py\n{symbol} currently has an institutional ownership ratio of {ratio}%.```")
            logo = await polygon.get_polygon_logo(symbol)
            ownershipembed50.set_thumbnail(logo)
            ownershipembed50.set_timestamp()
            ownershipembed50.set_footer(text=f"{symbol} | Data provided by Polygon.io")
            ownership50.add_embed(ownershipembed50)

            await ownership50.execute()
            await asyncio.sleep(5)  # Pause for 5 seconds before proceeding

        if ratio is not None and ratio  >= 20 and ratio < 50:
            ownership = AsyncDiscordWebhook(twentytoforty, content= "<@375862240601047070>")
            ownershipembed = DiscordEmbed(title=f"Institutional Ownership -", description=f"```py\n{symbol} currently has an institutional ownership ratio of {ratio}%.```")
            logo = await polygon.get_polygon_logo(symbol)
            ownershipembed.set_thumbnail(logo)
            ownershipembed.set_timestamp()
            ownershipembed.set_footer(text=f"{symbol} | Data provided by Polygon.io")
            ownership.add_embed(ownershipembed)

            await ownership.execute()
            await asyncio.sleep(5)  # Pause for 5 seconds before proceeding

        if ratio is not None and ratio < 20:
            ownership20 = AsyncDiscordWebhook(tenorless, content= "<@375862240601047070>")
            ownershipembed20 = DiscordEmbed(title=f"Institutional Ownership -", description=f"```py\n{symbol} currently has an institutional ownership ratio of {ratio}%.```")
            logo = await polygon.get_polygon_logo(symbol)
            ownershipembed20.set_thumbnail(logo)
            ownershipembed20.set_timestamp()
            ownershipembed20.set_footer(text=f"{symbol} | Data provided by Polygon.io")
            ownership20.add_embed(ownershipembed20)

            await ownership20.execute()
            await asyncio.sleep(5)  # Pause for 5 seconds before proceeding

        if ratio is not None and ratio >= 100:
            ownership100 = AsyncDiscordWebhook(onehundredplus, content= "<@375862240601047070>")
            ownershipembed100 = DiscordEmbed(title=f"Institutional Ownership -", description=f"```py\n{symbol} currently has an institutional ownership ratio of {ratio}%.```")
            logo = await polygon.get_polygon_logo(symbol)
            ownershipembed100.set_thumbnail(logo)
            ownershipembed100.set_timestamp()
            ownershipembed100.set_footer(text=f"{symbol} | Data provided by Polygon.io")
            ownership100.add_embed(ownershipembed100)

            await ownership100.execute()

            await asyncio.sleep(5)  # Pause for 5 seconds before proceeding


async def process_big_trades(symbol: str, size: float):

    snapshot = await polygon.get_snapshot(symbol)
    askprice = snapshot.stock_last_quote.ask_price
    bidprice = snapshot.stock_last_quote.bid_price
    asksize = snapshot.stock_last_quote.ask_size
    bidsize = snapshot.stock_last_quote.bid_size

    price=snapshot.last_trade.trade_price
    size=snapshot.last_trade.trade_size
    prevclose = snapshot.prev_day.close
    prevopen = snapshot.prev_day.open
    prevhigh = snapshot.prev_day.high
    prevlow = snapshot.prev_day.low
    prevvol = snapshot.prev_day.volume
    prevvwap = snapshot.prev_day.vwap
    vwap = snapshot.stock_day.vwap
    vol = snapshot.stock_day.volume
    high = snapshot.stock_day.high
    close = snapshot.stock_day.close
    low = snapshot.stock_day.low
    changep = snapshot.today_changep
    hook_dicts = [china_hooks, index_hooks, meme_hooks, india_hooks, russia_hooks, ETF_BROAD_MARKET_HOOKS]
    for hooks in hook_dicts:
        if symbol in hooks and size >= 1000:
            logo = await polygon.get_polygon_logo(symbol)
            largetradehook = AsyncDiscordWebhook(hooks[symbol], content="<@375862240601047070>")
            embed = DiscordEmbed(title=f"LARGE TRADE DETECTED!", description=f"```py\nDAY STATS:```\n\n> Open: **${open}**\n> High: **${high}**\n> Last: **${close}**\n> Low: **${low}**\n\n> Volume: **{float(vol):,}**\n> VWAP: **${vwap}**", color="FFD700")
            embed.add_embed_field(name=f"LAST TRADE:", value=f"> Size: **{size:,}**\n> Price: **${price}**\n> Change on Day: **{changep}%**")
            embed.add_embed_field(name=f"LAST QUOTE:", value=f"> Ask: **${askprice}**\n> Ask Size: **{float(asksize):,}**\n> Bid: **${bidprice}**\n> Bid Size: **{float(bidsize):,}**")
            embed.add_embed_field(name=f"Previous Day:", value=f"> Open: **${prevopen}**\n> High: **${prevhigh}**\n> Close: **${prevclose}**\n> Low: **${prevlow}**\n\n> Volume: **{float(prevvol):,}**\n> VWAP: **${prevvwap}**")
            embed.set_footer(text=f"{symbol} | Data provided by polygon.io. Use code FUDSTOP")
            embed.set_thumbnail(logo)
            largetradehook.add_embed(embed)
            print("SENT")
            await largetradehook.execute()



async def handle_msg(msgs: WebSocketMessage, data_queue: Queue):

    for m in msgs:
        if m.symbol == 'CTEST.A':
            continue
        elif m.symbol == 'PTEST.A':
            continue
        elif m.symbol == 'MTEST.A':
            continue
        elif m.symbol == 'ATEST.A':
            continue
        if isinstance(m, EquityTrade):
            data = {
                "symbol": m.symbol,
                "accumulated_volume": m.price,
                "size": m.size,
                "aggregate_vwap": m.conditions,
                "official_open_price": m.exchange,
                "conditions": m.conditions
            }
            await data_queue.put(data)



async def process_conditions(symbol):
    await asyncio.gather(
        Master(symbol).check_conditions(symbol, timespan="day"),
        Master(symbol).check_conditions(symbol, timespan="hour"),
        Master(symbol).check_conditions(symbol, timespan="week"),
    )

async def process_data(data_queue: Queue):
    while True:
        try:
            data = await data_queue.get()
            symbol = data['symbol']
            size = data['size']

            # Acquire the semaphore
            async with semaphore:
                await asyncio.gather(
                    process_rsi(symbol),
                    process_ownersip(symbol),
                    process_big_trades(symbol, size),
                    process_webull_data(symbol),
                    return_exceptions=True
                )
                await process_conditions(symbol)

        except Exception as e:
            logger.error(f"An error occurred while processing data: {e}")
        finally:
            # Mark the task as done in the queue
            data_queue.task_done()



async def main():
    data_queue = Queue()

    asyncio.create_task(c.connect(lambda msg: asyncio.create_task(handle_msg(msg, data_queue))))

    num_workers = 20  # You can adjust this value based on your requirements
    sdk_tasks = [
        process_data(data_queue) for _ in range(num_workers)
    ]

    await asyncio.gather(*sdk_tasks)

asyncio.run(main())