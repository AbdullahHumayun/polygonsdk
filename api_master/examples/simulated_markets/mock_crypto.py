import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))






from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage, Market, CryptoTrade
from typing import List
import asyncio
from cfg import YOUR_API_KEY
from datetime import datetime
from sdks.polygon_sdk.list_sets import crypto_conditions_dict,crypto_exchanges
c = WebSocketClient(subscriptions=["XT.*"], market=Market.Crypto, api_key=YOUR_API_KEY)
from discord_webhook import DiscordEmbed,AsyncDiscordWebhook
from cfg import btc,eth,COINBASE,KRAKEN,BITFINEX,BITSTAMP,xrp,jasmy, hex_colors
async def handle_msg(msgs: List[WebSocketMessage]):
    
    for m in msgs:
        message_data = {}
        if isinstance(m, CryptoTrade):
            message_data['type'] = 'CryptoTrade'
            message_data['pair'] = m.pair
            message_data['price'] = m.price
            message_data['size'] = m.size
            message_data['timestamp'] = datetime.fromtimestamp(m.timestamp / 1000.0).strftime('%Y-%m-%d %H:%M:%S')
            message_data['exchange'] = crypto_exchanges.get(m.exchange)
            message_data['conditions'] = crypto_conditions_dict.get(*m.conditions)
            print(message_data['conditions'])
            if m.size is not None and m.price is not None:
                dollar_cost = float(m.size) * float(m.price)
            if message_data['conditions'] == "Buy Side":
                color = hex_colors['green']
            elif message_data['conditions'] == "Sell Side":
                color = hex_colors['red']
            else:
                color = None

            if m.pair == "BTC-USD" and dollar_cost is not None and dollar_cost >= 500:
                hook = AsyncDiscordWebhook(btc, content=f"<@375862240601047070>")
                embed = DiscordEmbed(title=f"Crypto Trade - {m.pair}", description=f"```py\n{message_data['timestamp']}```", color=color)
                embed.add_embed_field(name=f"Trade Info:", value=f"> Size: **{float(m.size):,}**\n> Price: **{m.price}**\n> Dollar Cost: **${dollar_cost}**")
                embed.add_embed_field(name=f"Exchange:", value=f"> **{message_data['exchange']}**")
                embed.add_embed_field(name=f"Side of Market:", value=f"> **{message_data['conditions']}**")
                embed.set_thumbnail("https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Bitcoin.svg/1200px-Bitcoin.svg.png")
                hook.add_embed(embed)
                await hook.execute()


            if m.pair == "ETH-USD" and dollar_cost is not None and dollar_cost >= 500:
                hook = AsyncDiscordWebhook(eth, content=f"<@375862240601047070>")
                embed = DiscordEmbed(title=f"Crypto Trade - {m.pair}", description=f"```py\n{message_data['timestamp']}```", color=color)
                embed.add_embed_field(name=f"Trade Info:", value=f"> Size: **{float(m.size):,}**\n> Price: **{m.price}**\n> Dollar Cost: **${dollar_cost}**")
                embed.add_embed_field(name=f"Exchange:", value=f"> **{message_data['exchange']}**")
                embed.add_embed_field(name=f"Side of Market:", value=f"> **{message_data['conditions']}**")
                embed.set_thumbnail("https://ethereum.org/static/6b935ac0e6194247347855dc3d328e83/13c43/eth-diamond-black.png")
                hook.add_embed(embed)
                await hook.execute()
            if m.pair == "XRP-USD" and dollar_cost is not None and dollar_cost >= 500:
                hook = AsyncDiscordWebhook(xrp, content=f"<@375862240601047070>")
                embed = DiscordEmbed(title=f"Crypto Trade - {m.pair}", description=f"```py\n{message_data['timestamp']}```", color=color)
                embed.add_embed_field(name=f"Trade Info:", value=f"> Size: **{float(m.size):,}**\n> Price: **{m.price}**\n> Dollar Cost: **${dollar_cost}**")
                embed.add_embed_field(name=f"Exchange:", value=f"> **{message_data['exchange']}**")
                embed.add_embed_field(name=f"Side of Market:", value=f"> **{message_data['conditions']}**")
                embed.set_thumbnail("https://seeklogo.com/images/R/ripple-xrp-logo-E97D62205B-seeklogo.com.png")
                hook.add_embed(embed)
                await hook.execute()
            if m.pair == "JASMY-USD" and dollar_cost is not None and dollar_cost >= 500:
                hook = AsyncDiscordWebhook(jasmy, content=f"<@375862240601047070>")
                embed = DiscordEmbed(title=f"Crypto Trade - {m.pair}", description=f"```py\n{message_data['timestamp']}```", color=color)
                embed.add_embed_field(name=f"Trade Info:", value=f"> Size: **{float(m.size):,}**\n> Price: **{m.price}**\n> Dollar Cost: **${dollar_cost}**")
                embed.add_embed_field(name=f"Exchange:", value=f"> **{message_data['exchange']}**")
                embed.add_embed_field(name=f"Side of Market:", value=f"> **{message_data['conditions']}**")
                embed.set_thumbnail("https://altcoinsbox.com/wp-content/uploads/2023/04/jasmycoin-logo.png")
                hook.add_embed(embed)
                await hook.execute()


            if m.exchange is not None and m.exchange == "Coinbase":
                hook = AsyncDiscordWebhook(COINBASE, content=f"<@375862240601047070>")
                embed = DiscordEmbed(title=f"Exchange Trade: {message_data['exchange']}", description=f"```py\n{message_data['timestamp']}**", color=color)
                embed.add_embed_field(name=f"Trade Info:", value=f"> Size: **{float(m.size):,}**\n> Price: **{m.price}**\n> Dollar Cost: **${dollar_cost}**")
                embed.add_embed_field(name=f"Exchange:", value=f"> **{message_data['exchange']}**")
                embed.add_embed_field(name=f"Side of Market:", value=f"> **{message_data['conditions']}**")
                embed.set_thumbnail("https://images.ctfassets.net/c5bd0wqjc7v0/3dFdY6GvgLgCIXmBiN6eiA/d4acc5d4c5d557566cf0e46f9b58de43/icon-buy-and-sell.svg")
                hook.add_embed(embed)     
                await hook.execute()     

            if message_data['exchange'] is not None and message_data['exchange'] == "Kraken":
                hook = AsyncDiscordWebhook(KRAKEN, content=f"<@375862240601047070>")
                embed = DiscordEmbed(title=f"Exchange Trade: {message_data['exchange']}", description=f"```py\n{message_data['timestamp']}**", color=color)
                embed.add_embed_field(name=f"Trade Info:", value=f"> Size: **{float(m.size):,}**\n> Price: **{m.price}**\n> Dollar Cost: **${dollar_cost}**")
                embed.add_embed_field(name=f"Exchange:", value=f"> **{message_data['exchange']}**")
                embed.add_embed_field(name=f"Side of Market:", value=f"> **{message_data['conditions']}**")
                embed.set_thumbnail("https://upload.wikimedia.org/wikipedia/en/thumb/4/48/Seattle_Kraken_official_logo.svg/1200px-Seattle_Kraken_official_logo.svg.png")

                hook.add_embed(embed)     
                await hook.execute()      

            if message_data['exchange'] is not None and message_data['exchange'] == "Bitstamp":
                hook = AsyncDiscordWebhook(BITSTAMP, content=f"<@375862240601047070>")
                embed = DiscordEmbed(title=f"Exchange Trade: {message_data['exchange']}", description=f"```py\n{message_data['timestamp']}**", color=color)
                embed.add_embed_field(name=f"Trade Info:", value=f"> Size: **{float(m.size):,}**\n> Price: **{m.price}**\n> Dollar Cost: **${dollar_cost}**")
                embed.add_embed_field(name=f"Exchange:", value=f"> **{message_data['exchange']}**")
                embed.add_embed_field(name=f"Side of Market:", value=f"> **{message_data['conditions']}**")
                embed.set_thumbnail("https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Bitstamp-vector-logo.svg/1200px-Bitstamp-vector-logo.svg.png")
                hook.add_embed(embed)     
                await hook.execute()  

            if message_data['exchange'] is not None and message_data['exchange'] == "Bitfinex":
                hook = AsyncDiscordWebhook(BITFINEX, content=f"<@375862240601047070>")
                embed = DiscordEmbed(title=f"Exchange Trade: {message_data['exchange']}", description=f"```py\n{message_data['timestamp']}**", color=color)
                embed.add_embed_field(name=f"Trade Info:", value=f"> Size: **{float(m.size):,}**\n> Price: **{m.price}**\n> Dollar Cost: **${dollar_cost}**")
                embed.add_embed_field(name=f"Exchange:", value=f"> **{message_data['exchange']}**")
                embed.add_embed_field(name=f"Side of Market:", value=f"> **{message_data['conditions']}**")
                embed.set_thumbnail("https://bitfinex.com/images/thumbnails/bitfinex-2.png")
                hook.add_embed(embed)     
                await hook.execute()  
        print(message_data)

async def main():
    await asyncio.gather(c.connect(handle_msg))


asyncio.run(main())