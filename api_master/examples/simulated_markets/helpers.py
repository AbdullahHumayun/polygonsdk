import csv
from sdks.polygon_sdk.list_sets import sublist1, OPTIONS_EXCHANGES, STOCK_EXCHANGES,stock_condition_dict, option_condition_desc_dict, option_condition_dict
from discord_webhook import AsyncDiscordWebhook, DiscordEmbed
from sdks.models.test_events import TestOptionsEvent
from sdks.helpers.helpers import human_readable
from cfg import sector_hooks
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY
polygon = AsyncPolygonSDK(YOUR_API_KEY)
from polygon_enhanced.polygon_enhanced.websocket.models import EquityAgg,EquityQuote,EquityTrade
import asyncio

def write_to_csv(output_list, file_name="files/options/search_data/option_data.csv"):
    with open(file_name, mode="a", newline='') as csvfile:

        fieldnames = ["Option Symbol", "Strike Price", "Contract Type", "Expiration Date", "Delta", "Day Change Percent", 
                      "Implied Volatility", "Underlying Price", "Break Even Price", "Result", "Day Volume", 
                      "Day VWAP", "Underlying", "Open Interest"]
        
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header only if the file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerow(output_list)


async def convert_exchanges_and_conditions_options(m):
    """Converts polygon exchange and condition ids 
    to their respective names for the options cluster.
    """
    if m is not None:
        opt_exchange = OPTIONS_EXCHANGES.get(m.exchange)
        conditions = [option_condition_dict.get(condition) for condition in m.conditions]
        return opt_exchange, conditions

async def send_discord_message(webhook_url, message_data):
        webhook = AsyncDiscordWebhook(webhook_url,content=f"> <@375862240601047070>\n\n> **{str(message_data)}**")
        await webhook.execute()


async def convert_exchanges_and_conditions_stocks(m):
    if m is not None:
        stock_exchanges = STOCK_EXCHANGES.get(m.exchange)
        conditions = [stock_condition_dict.get(condition) for condition in m.conditions] if m.conditions is not None else []

        return stock_exchanges, conditions
    

async def send_messages_raw(webhook_url, m):
    if isinstance(m, EquityTrade):
        # Create the webhook object
        webhook = AsyncDiscordWebhook(webhook_url, content="<@everyone>")

        # Create the embed message
        embed = DiscordEmbed(title=f"TRADES",
                                description=f"> **{m}**")
        webhook.add_embed(embed)

        # Create a task for sending the webhook message to the corresponding sector channel
        await send_discord_message(webhook_url, m)
        print(f"EXECUTED WEBHOOK")
 
    elif isinstance(m, EquityAgg):
        # Create the webhook object
        webhook = AsyncDiscordWebhook(webhook_url, content="<@everyone>")

        # Create the embed message
        embed = DiscordEmbed(title=f"AGGS",
                                description=f"> **{m}**")
        webhook.add_embed(embed)

        # Create a task for sending the webhook message to the corresponding sector channel
        await send_discord_message(webhook_url, m)
        print(f"EXECUTED WEBHOOK")
    elif isinstance(m, EquityQuote):
        # Create the webhook object
        webhook = AsyncDiscordWebhook(webhook_url, content="<@everyone>")

        # Create the embed message
        embed = DiscordEmbed(title=f"QUOTES",
                                description=f"> **{m}**")
        webhook.add_embed(embed)

        # Create a task for sending the webhook message to the corresponding sector channel
        await send_discord_message(webhook_url, m)
        print(f"EXECUTED WEBHOOK")


async def generate_stock_embed(webhook_url,m, color):
    webhook = AsyncDiscordWebhook(webhook_url)
    embed = DiscordEmbed(title=f"Test Event - Stocks", description=f"```py\nThis is a test feed using the most up-to-date data as of market close on Friday.```\n\n> Ticker: **{m.symbol}**", color=color)
    embed.add_embed_field(name=f"Day Stats:", value=f"> Open: **${m.open}**\n> High: **${m.high}**\n> Low: **${m.low}**\n> Close: **${m.close}**\n> Vol: **{float(m.volume):,}**\n> VWAP: **${m.vwap}**")
    embed.add_embed_field(name=f"Prev. Day:", value=f"> pOpen: **${m.prev_open}**\n> pHigh: **${m.prev_high}**\n> pLow: **${m.prev_low}**\n> pClose: **${m.prev_close}**\n> pVol: **{float(m.prev_volume):,}**\n> pVWAP: **${m.prev_vwap}**")
    embed.add_embed_field(name=f"Last Minute Data:", value=f"> mOpen: **${m.min_open}**\n> mHigh: **${m.min_high}**\n> mLow: **${m.min_low}**\n> mClose: **${m.min_close}**\n> mVol: **{float(m.min_volume):,}**\n> Accumulated Vol: **{float(m.min_av):,}**\n> mVWAP: **${m.min_vwap}**")
    embed.add_embed_field(name=f"Last Trade:", value=f"> Size: **{float(m.last_size)}**\n> Price: **${m.last_price}**\n> Exchange: **{m.last_exchange}**\n> Conditions: **{m.last_trade_conditions}**")
    embed.add_embed_field(name=f"Last Quote:", value=f"> Bid: **${m.last_quote_bid}\n> **Ask: **{m.last_quote_ask}**\n> Bid Size: **{m.last_quote_bid_size}**\n> Ask Size: **{m.last_quote_ask_size}**")
    embed.add_embed_field(name=f"Today's Change:", value=f"**{m.today_change_percent}%**")
    embed.set_thumbnail(await polygon.get_polygon_logo(m.symbol))
    embed.set_timestamp()
    webhook.add_embed(embed)
    await webhook.execute()


async def generate_options_embed(webhook_url,m: TestOptionsEvent, color):
    webhook = AsyncDiscordWebhook(webhook_url)
    embed = DiscordEmbed(title=f"Test Event - Options", description=f"```py\nThis is a test feed using the most up-to-date data as of market close on Friday.```\n\n> Ticker: **{human_readable(m.ticker)}**", color=color)
    embed.add_embed_field(name=f"Day Stats:", value=f"> Open: **${m.day_open}**\n> High: **${m.day_high}**\n> Low: **${m.day_low}**\n> Close: **${m.day_close}**\n> VWAP: **${m.day_vwap}**")
    embed.add_embed_field(name=f"Greeks:", value=f"> Delta: **{round(float(m.delta),2)}**\n> Gamma: **{round(float(m.gamma),2)}**\n> Theta: **{round(float(m.theta),2)}**\n> Vega: **{round(float(m.vega),2)}**\n> IV: **{round(float(m.implied_volatility),2)}%**")
    embed.add_embed_field(name=f"Vol & OI:",value=f"> VOL: **{float(m.day_volume):,}**\n> OI: **{float(m.open_interest):,}**")
    embed.add_embed_field(name=f"Last Trade:", value=f"> Size: **{float(m.last_trade_size)}**\n> Price: **${m.price}**\n> Exchange: **{m.expiration_date}**\n> Conditions: **{m.last_trade_conditions}**")       
    embed.add_embed_field(name=f"Last Quote:", value=f"> Bid: **${m.bid}\n> Mid: **${m.midpoint}**\n> **Ask: **{m.ask}**\n> Bid Size: **{m.bid_size}**\n> Ask Size: **{m.ask_size}**")
    embed.add_embed_field(name=f"Today's Change:", value=f"**{m.day_change_percent}%**")
    embed.set_thumbnail(await polygon.get_polygon_logo(m.underlying_ticker))
    embed.set_timestamp()
    webhook.add_embed(embed)
    await webhook.execute()