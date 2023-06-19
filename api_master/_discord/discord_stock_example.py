import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import datetime

from polygon.websocket import WebSocketMessage, WebSocketClient, Market, EquityAgg, EquityQuote, EquityTrade
from polygon.websocket import WebSocketClient
from typing import List
import asyncio

from cfg import YOUR_API_KEY
from sdks.polygon_sdk.mapping_dicts import stock_condition_dict, STOCK_EXCHANGES, TAPES, quote_conditions, indicators
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK

from asyncio import Queue
import csv

from discord_webhook import AsyncDiscordWebhook, DiscordEmbed

poly = AsyncPolygonSDK(YOUR_API_KEY) #create instance of polygon SDK
c = WebSocketClient(subscriptions=["T.*,A.*,Q.*"], market=Market.Stocks, api_key=YOUR_API_KEY) #connect to the options market trades, aggs, and quotes.






async def handle_msg(msgs: List[WebSocketMessage], queue: Queue):
    for m in msgs:
        message_data = {}

        if isinstance(m, EquityTrade):
            message_data['type'] = 'EquityTrade'
            message_data['symbol'] = m.symbol
            message_data['price'] = m.price
            message_data['size'] = m.size
            message_data['timestamp'] = datetime.datetime.fromtimestamp(m.timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S')
            message_data['conditions'] = [stock_condition_dict.get(condition) for condition in m.conditions]
            message_data['exchange'] = STOCK_EXCHANGES.get(m.exchange)

        elif isinstance(m, EquityAgg):
            message_data['type'] = 'EquityAgg'
            message_data['symbol'] = m.symbol
            message_data['official_open'] = m.official_open_price
            message_data['last_price'] = m.close
            message_data['total_volume'] = m.accumulated_volume
            message_data['volume'] = m.volume
            message_data['day_vwap'] = m.aggregate_vwap
            message_data['average_size'] = m.average_size
            message_data['otc'] = m.otc
            message_data['start_time'] = datetime.datetime.fromtimestamp(m.start_timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S')
            message_data['end_time'] = datetime.datetime.fromtimestamp(m.end_timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S')

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
            message_data['timestamp'] = datetime.datetime.fromtimestamp(m.timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S')
            message_data['ask_exchange'] = STOCK_EXCHANGES.get(m.ask_exchange_id)
            message_data['bid_exchange'] = STOCK_EXCHANGES.get(m.bid_exchange_id)

        await queue.put(message_data)


"""
Consumes queue data - packages and sends to discord using our csv file / live real-time websocket data
"""

ticker_webhook_dict =  {}


async def consume(queue: Queue):
    while True:
        m = await queue.get()
        message_type = m.get('type')

        if message_type == 'EquityTrade':
            symbol = m.get('symbol')
            price = m.get('price')
            size = float(m.get('size'))
            timestamp = m.get('timestamp')
            conditions = m.get('conditions')
            exchange = m.get('exchange')

            if symbol in ticker_webhook_dict:
                logo = await poly.get_polygon_logo(symbol)
                webhook_url = ticker_webhook_dict[symbol]

                webhook = AsyncDiscordWebhook(webhook_url)
                embed = DiscordEmbed(title=f"{symbol} Live Data", description=f"```py\nReal-time TRADE for {symbol}```")
                embed.add_embed_field(name=f"Trade Info:", value=f"> Price: **${price}**\n> Size: **{size}**")
                embed.add_embed_field(name=f"Conditions:", value=f"> **{conditions}**")
                embed.add_embed_field(name=f"Exchange", value=f"> **{exchange}**")
                embed.set_thumbnail(logo)
                embed.set_timestamp()
                embed.set_footer(text=f"{symbol} | Data Provided by Polygon.io")
                asyncio.create_task(send_webhooks(webhook, embed))

        elif message_type == 'EquityAgg':

            symbol = m.get('symbol')
            official_open = m.get('official_open')
            last_price = m.get('last_price')
            total_volume = float(m.get('total_volume'))
            volume = float(m.get('volume'))
            day_vwap = m.get('day_vwap')
            average_size = m.get('average_size')
            otc = m.get('otc')
            start_time = m.get('start_time')
            end_time = m.get('end_time')
            if symbol in ticker_webhook_dict:
                logo = await poly.get_polygon_logo(symbol)
                webhook_url = ticker_webhook_dict[symbol]
                webhook = AsyncDiscordWebhook(webhook_url)
                embed = DiscordEmbed(title=f"{symbol} Live Data", description=f"```py\nReal-time Aggregate for {symbol}```")
                embed.add_embed_field(name=f"Day Stats:", value=f"> Last Volume: **${volume:,}\n> Total Volume: **${total_volume:,}**")
                embed.add_embed_field(name=f"Pricing:", value=f"> Official Open: **${official_open}\n> Last Price: **${last_price}**\n> Day VWAP: **${day_vwap}**\n> Average Size: **{average_size}**")
                embed.add_embed_field(name=f"Over The Counter?", value=f"> **{otc}**")
                embed.add_embed_field(name=f"Timestamps:", value=f"> Start: **{start_time}**\n\n> End: **{end_time}**")
                embed.set_thumbnail(logo)
                embed.set_timestamp()
                embed.set_footer(text=f"{symbol} | Data Provided by Polygon.io")
                asyncio.create_task(send_webhooks(webhook, embed))



        elif message_type == 'EquityQuote':
            symbol = m.get('symbol')

            if symbol in ticker_webhook_dict:
                webhook_url = ticker_webhook_dict[symbol]
                logo = await poly.get_polygon_logo(symbol)
                webhook = AsyncDiscordWebhook(webhook_url)
                embed = DiscordEmbed(title=f"{symbol} Live Data", description=f"```py\nReal-time quote for {symbol}```")
                embed.add_embed_field(name=f"Spread:", value=f"> Bid: **${m.get('bid')}**\n> Ask: **${m.get('ask')}**\n> Bid Size: **{m.get('bid_size')}**\n> Ask Size: **{m.get('ask_size')}**")
                embed.add_embed_field(name=f"Exchanges:", value=f"> Bid Exchange: **{m.get('bid_exchange')}**\n> Ask Exchange: **{m.get('ask_exchange')}**")
                embed.add_embed_field(name=f"Tape Traded:", value=f"> **{m.get('tape')}**")
                embed.add_embed_field(name=f"Quote Condition:", value=f"> **{m.get('condition')}**")
                embed.add_embed_field(name=f"Quote Indicator:", value=f"> **{m.get('indicator')}**")
                embed.set_thumbnail(logo)
                embed.set_timestamp()
                embed.set_footer(text=f"{symbol} | Data Provided by Polygon.io")
                asyncio.create_task(send_webhooks(webhook, embed))
                
async def send_webhooks(webhook: AsyncDiscordWebhook, embed: DiscordEmbed):
    webhook.add_embed(embed)
    await webhook.execute()

async def main():
    data_queue = Queue()

    num_workers = 4
    sdk_tasks = [consume(data_queue) for _ in range(num_workers)]

    async def callback(msgs):
        await handle_msg(msgs, data_queue)

    connect_task = asyncio.create_task(c.connect(callback))
    sdk_tasks.append(connect_task)

    await asyncio.gather(*sdk_tasks)

asyncio.run(main())