


from api_master.sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from api_master.cfg import YOUR_API_KEY, today_str
from api_master._discord import emojis as e
import json




from asyncio import Queue

from discord_webhook import DiscordEmbed,AsyncDiscordWebhook

from api_master.polygon_enhanced.polygon_enhanced.websocket import EquityAgg, Market, WebSocketMessage, EquityTrade
from api_master.polygon_enhanced.polygon_enhanced.websocket import EquityQuote

from api_master.polygon_enhanced.polygon_enhanced import WebSocketClient


from api_master.sdks.polygon_sdk.aggregates import AggregatesData

from api_master.sdks.helpers.helpers import human_readable
# from plotting.plot_images import create_plot_image

import asyncio
import re


from api_master.sdks.polygon_sdk.mapping_dicts import option_condition_dict, OPTIONS_EXCHANGES, quote_conditions, indicators, stock_condition_dict,STOCK_EXCHANGES
from typing import List
import pandas as pd
from datetime import datetime

from api_master.sdks.webull_sdk.webull_sdk import AsyncWebullSDK
from datetime import datetime, timedelta
from api_master.sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from discord_webhook import AsyncDiscordWebhook
opts = PolygonOptionsSDK(YOUR_API_KEY)

now = datetime.now()
five_days_from_now = now + timedelta(days=35)
five_days_from_now_str = five_days_from_now.strftime('%Y-%m-%d')
from datetime import datetime


today = datetime.today()

subscriptions = ["A.*,T.*"]

webull = AsyncWebullSDK()
polyoptions = PolygonOptionsSDK(YOUR_API_KEY)
cli = WebSocketClient(subscriptions=subscriptions, api_key=YOUR_API_KEY, market=Market.Options) 
async_sdk = AsyncPolygonSDK(YOUR_API_KEY)
today_str = today.strftime('%Y-%m-%d')

async def handle_msg(msgs: WebSocketMessage):

    for m in msgs:




        if isinstance(m, EquityAgg):

            symbol = m.symbol
            v = m.volume
            av = m.accumulated_volume
            c = m.close
            op = m.official_open_price
            av = m.accumulated_volume
            symb = str(m.symbol)


        
            sym = human_readable(symb)
            if v is not None and v >= 5000:
                print(f"VOL 5K + FOUND")

                try:
                    whsymb = symb[2:]
                except TypeError:
                    whsymb = "none"
                underlying_symbol = await polyoptions.extract_underlying_symbol(symb)
                
                snapshot = await polyoptions.get_option_contract_snapshot(underlying_symbol, symb)
                if snapshot:
                    expiration_date = datetime.strptime(snapshot, '%Y-%m-%d').date()
                    current_date = datetime.today().date()
                    days_until_expiration = (expiration_date - current_date).days
                    bid = snapshot.bid
                    ask = snapshot.ask
                    contract_change_percent=round(float(snapshot.day_change_percent), 2) if snapshot.day_change_percent is not None else None
                else:
                    continue








                under_price = AggregatesData(underlying_symbol)
                print(under_price)
                dollar_cost = c * v * 100
                print(dollar_cost)
                # Proceed with trade processing

                sym = human_readable(symb)
                print(f"***********************************{sym}*******************************************")






            




                ticker, symbol = await webull.fetch_ticker_id(underlying_symbol)
                stats = await webull.get_webull_stock_data(ticker)

                try:
                    price = stats.web_stock_close
                    changep = stats.web_change_ratio
                    high = stats.web_stock_high
                    low = stats.web_stock_low

                except (AttributeError,TypeError,IndexError):
                    print(f"ERRORRR!!")
                    continue
                

                webull_vol_anal = await webull.get_webull_vol_analysis_data(ticker)
                buyVolume = webull_vol_anal.buyVolume
                totalVolume = webull_vol_anal.totalVolume
                sellVolume = webull_vol_anal.sellVolume
                nVolume = webull_vol_anal.nVolume

                

                differential = float(ask) - (bid)
                
                try:
                    buy_percentage = (buyVolume / totalVolume) * 100
                except ZeroDivisionError:
                    buy_percentage = 0.1
                try:
                    sell_percentage = (sellVolume / totalVolume) * 100
                except ZeroDivisionError:
                    sell_percentage = 0.1
                try:
                    neutral_percentage = (nVolume / totalVolume) * 100
                except ZeroDivisionError:
                    neutral_percentage = 0.1
                print(buy_percentage,sell_percentage,neutral_percentage)



      
                
                special = AsyncDiscordWebhook("YOUR_HOOK", content="@everyone")
                specem = DiscordEmbed(title=f"{e.ls}{e.lp}{e.le}{e.lc}{e.li}{e.la}{e.ll}", description=f"```py\n{sym}\n{underlying_symbol} Price: ${price}\n\nThis surge has primary buy volume, is unusual, and is a high chance of buy to open. Pay attention to the expiration date and price % change on the day as well as current price vs strike price.```")
                
                specem.add_embed_field(name=f"Bid / Ask", value=f"```py\nBid: **${bid}**\nAsk: **${ask}**```")

                specem.add_embed_field(name=f"TRADE VOLUME TOTAL:", value=f"```py\n{float(v):,}```")
                specem.add_embed_field(name=f"Underlying Order Flow:", value=f"> {e.greenfire} Buy: **{buyVolume:,}**\n> {e.greyfire} Neutral: **{nVolume:,}**\n> {e.redfire} Sell: **{sellVolume:,}**")
                specem.add_embed_field(name=f"Price Traded:", value=f"```py\nThis contract was traded at ${c}```")
                specem.add_embed_field(name=f"Dollar Cost:", value=f"```py\n${float(dollar_cost):,}```")
                specem.set_thumbnail(await async_sdk.get_polygon_logo(underlying_symbol))
                specem.set_footer(text=f"{whsymb}")
                specem.set_timestamp()
                special.add_embed(specem)
                await special.execute()
                print(f"SPECIAL<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>EXECUTED<><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
                print(f"SPECIAL<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>EXECUTED<><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
                print(f"SPECIAL<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>EXECUTED<><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
                print(f"SPECIAL<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>EXECUTED<><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
                print(f"SPECIAL<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>EXECUTED<><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
                print(f"SPECIAL<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>EXECUTED<><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
                print(f"SPECIAL<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>EXECUTED<><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
                print(f"SPECIAL<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>EXECUTED<><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
                print(f"SPECIAL<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>EXECUTED<><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
                print()





                if bid >= 0.20 and sym.startswith("VIX") or sym.startswith("SPY") or sym.startswith("NDX") or sym.startswith("QQQ") or sym.startswith("IWM") or sym.startswith("SPX") and days_until_expiration <=6:
                    indexsurge = AsyncDiscordWebhook("YOUR_HOOK", content="<@375862240601047070>")
                    pct = round(v / av * 100,ndigits=2)
                    premdisc = round(((c - op) / op) * 100, ndigits=2)


                    inembed = DiscordEmbed(title=f"{e.li}{e.ln}{e.ld} {e.greensignal} {e.ls}{e.lu}{e.lr}{e.lg}{e.le}", description=f"```py\n{sym}\n\nPrice: ${price}```")
                    inembed.add_embed_field(name=f"Surge Volume vs. Total Volume:", value=f"```py\n{v:,} / {av:,}```", inline=True)
                    inembed.add_embed_field(name=f"Surge % of Volume:", value=f"> **{pct}%**", inline=True)
                    inembed.add_embed_field(name=f"Dollar Cost:", value=f"```py\n${float(dollar_cost):,}```")
                    inembed.add_embed_field(name=f"Price Paid / Avg Cost:", value=f"> **${c}** with the contract trading **{contract_change_percent}%**", inline=True)

                    inembed.add_embed_field(name=f"Contract Price:", value=f"> {e.greencheck} Bid: **${bid}**\n> {e.confirmed}\n> {e.redcheck} Ask: **${ask}**")
                   
                    inembed.add_embed_field(name=f"Price Traded:", value=f"```py\nThis contract was traded at ${c}```")
                    inembed.set_thumbnail(await async_sdk.get_polygon_logo(underlying_symbol))
                    inembed.set_footer(text=f"{whsymb}")
                    inembed.set_timestamp()



                    indexsurge.add_embed(inembed)
                    await indexsurge.execute()

                if v is not None and v >= 20000 and days_until_expiration <= 15:

                    fortysurge = AsyncDiscordWebhook("YOUR_HOOK", content="<@375862240601047070>")
                    pct = round(v / av * 100,ndigits=2)



                    
                    fortyembed = DiscordEmbed(title=f"{e.pink2}{e.pink0}{e.lk} + {e.lightningstrike} {e.ls}{e.lu}{e.lr}{e.lg}{e.le}", description=f"```py\n{sym}```")
                    fortyembed.add_embed_field(name=f"Surge Volume vs. Total Volume:", value=f"```py\n{v:,} / {av:,}```", inline=True)
                    fortyembed.add_embed_field(name=f"Surge % of Volume:", value=f"```py\n{pct}%```", inline=True)
                    fortyembed.add_embed_field(name=f"Dollar Cost:", value=f"```py\n${float(dollar_cost):,}```")
                    fortyembed.add_embed_field(name=f"Price Paid / Avg Cost:", value=f"> **${c}** with the contract trading **{contract_change_percent}%**", inline=True)
                    fortyembed.add_embed_field(name=f"Contract Price:", value=f"> {e.greencheck} Bid: **${bid}**\n\n> {e.confirmed}\n{e.redcheck} Ask: **${ask}**")
                    fortyembed.add_embed_field(name=f"Price Traded:", value=f"```py\nThis contract was traded at ${c}```")
                    fortyembed.set_footer(text=f"{whsymb}")
                    fortyembed.set_timestamp()
                    fortysurge.add_embed(fortyembed)

                    await fortysurge.execute()


        elif isinstance(m, EquityTrade):
            symbol = m.symbol
            symb = human_readable(symbol)
            underlying_symbol=  await polyoptions.extract_underlying_symbol(symbol)

            size = m.size
            price = m.price

            conditions = [option_condition_dict.get(condition) for condition in m.conditions] if m.conditions is not None else []


            if "Multi Leg Floor Trade of Proprietary Products" in conditions and size >= 500:
                print("hi")
                hook = AsyncDiscordWebhook("YOUR_HOOK", content=f"<@375862240601047070>")
                hookem = DiscordEmbed(title=f"Multi Leg Floor Trade of Proprietary Products", description=f"```py\n{symb}```\n> **Transaction represents execution of a proprietary product non-electronic multi leg order with at least 3 legs. The trade price may be outside the current NBBO.**")
                hookem.add_embed_field(name=f"Volume:", value=f"> **{m.size}**")
                hookem.add_embed_field(name=f"Price Paid:", value=f"> **{m.price}**")

                hookem.set_timestamp()
                hookem.set_footer(text=f"{symbol.replace('O:','')}")
                hook.add_embed(hookem)
                
                await hook.execute()

            if "Multi Leg Auction" in conditions and size >= 500:
                print("hi")
                hook = AsyncDiscordWebhook("YOUR_HOOK", content=f"<@375862240601047070>")
                hookem = DiscordEmbed(title=f"Multi Leg Auction", description=f"```py\n{symb}```\n> **Transaction was the execution of an electronic multi leg order which was “stopped” at a price and traded in a two sided auction mechanism that goes through an exposure period in a complex order book. Such auctions mechanisms include and not limited to Price Improvement, Facilitation or Solicitation Mechanism.**")
                hookem.add_embed_field(name=f"Volume:", value=f"> **{m.size}**")
                hookem.set_timestamp()
                hookem.set_footer(text=f"{symbol.replace('O:','')}")
                hook.add_embed(hookem)
                await hook.execute()

            if 'Multi Leg floor trade against single leg(s)' in conditions and size >= 500:
                print("hi")
                hook = AsyncDiscordWebhook("YOUR_HOOK", content=f"<@375862240601047070>")
                hookem = DiscordEmbed(title=f"Multi Leg trade against single leg(s)", description=f"```py\n{symb}```\n> **Transaction represents an electronic execution of a multi Leg order traded against single leg orders/ quotes.**")
                hookem.add_embed_field(name=f"Volume:", value=f"> **{m.size}**")
                hookem.set_timestamp()
                hookem.set_footer(text=f"{symbol.replace('O:','')}")
                hook.add_embed(hookem)
                await hook.execute()        

            if 'Single Leg Auction Non ISO' in conditions and size >= 500:
                hook = AsyncDiscordWebhook("YOUR_HOOK", content=f"<@375862240601047070>")
                hookem = DiscordEmbed(title=f"Single-Leg Auction (NON SWEEP)", description=f"```py\n{symb}```\n> **Transaction was the execution of an electronic order which was “stopped” at a price and traded in a two sided auction mechanism that goes through an exposure period. Such auctions mechanisms include and not limited to Price Improvement, Facilitation or Soliciation Mechanism.**")
                hookem.add_embed_field(name=f"Volume:", value=f"> **{m.size}**")
                hookem.set_timestamp()
                hookem.set_footer(text=f"{symbol.replace('O:','')}")
                hook.add_embed(hookem)
                await hook.execute()


            symbol = underlying_symbol

async def main():

    print("Starting main function...")

    await cli.connect(handle_msg)




asyncio.run(main())




















































