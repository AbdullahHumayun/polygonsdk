from discord_webhook import DiscordEmbed, AsyncDiscordWebhook
from cfg import konviction, VWAP_DIFFERENTIAL
from sdks.polygon_sdk.masterSDK import MasterSDK
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from sdks.helpers.helpers import human_readable
from cfg import YOUR_API_KEY, hex_colors, spx, sector_hooks
from sdks.polygon_sdk.list_sets import stock_condition_dict, STOCK_EXCHANGES, TAPES, quote_conditions, indicators, market_sectors, subscriptions, OPTIONS_EXCHANGES, option_condition_dict


import asyncio

poly_opts = PolygonOptionsSDK(YOUR_API_KEY)
poly = AsyncPolygonSDK(YOUR_API_KEY)
master = MasterSDK()

symbol_to_sector = {symbol: sector for sector, symbols in market_sectors.items() for symbol in subscriptions}
async def create_vwap_differential(data):
    symbol = data['symbol']
    underlying_ticker = await poly_opts.extract_underlying_symbol(symbol)
    option_ticker = human_readable(symbol)
    if (data['last_price'] - data['day_vwap']) / data['day_vwap'] >= 50:
        hook = AsyncDiscordWebhook(VWAP_DIFFERENTIAL)

        print("The closing price is more than 50% less than the aggregate VWAP.")
        optsnap_task = asyncio.create_task(master.get_universal_snapshot(data['symbol']))
        rsi_minute_task = asyncio.create_task(poly.get_rsi(underlying_ticker, timespan="minute"))
        rsi_hour_task = asyncio.create_task(poly.get_rsi(underlying_ticker, timespan="hour"))
        rsi_day_task = asyncio.create_task(poly.get_rsi(underlying_ticker, timespan="day"))
        rsi_week_task = asyncio.create_task(poly.get_rsi(underlying_ticker, timespan="week"))

        optsnap, rsi_minute, rsi_hour, rsi_day, rsi_week = await asyncio.gather(optsnap_task, rsi_minute_task, rsi_hour_task, rsi_day_task, rsi_week_task)

        if data['day_vwap'] is not None and data['last_price'] is not None:
            vwap_differential = (data['last_price'] - data['day_vwap']) / data['day_vwap']
        else:
            vwap_differential = None


        if data['total_volume'] is not None and data['volume'] is not None and data['total_volume'] != 0:
            trade_percent_of_volume = data['total_volume'] / data['volume']
        else:
            trade_percent_of_volume = None

        open = optsnap.open[0]
        high = optsnap.high[0]
        last = optsnap.close[0]
        low = optsnap.low[0]
        conditions = optsnap.conditions[0]
        changep = optsnap.change_percent[0]
        if changep is not None and changep < 0:
            color = hex_colors['red']
        elif changep is not None and changep > 0:
            color = hex_colors['green']
        else:
            color = hex_colors['yellow']
        embed = DiscordEmbed(title = f"{option_ticker}", description=f"```py\nThis option contract is currently priced 50% below its' aggregated VWAP price on the day.```", color=color)
        embed.add_embed_field(name=f"Day Stats:", value=f"> Open: **${open}**\n> High: **${high}**\n> Last: **${last}**\n> Low: **${low}**\n> Change%: **{changep}%**")
        embed.add_embed_field(name=f"Trade Capture:", value=f"> Traded Size: **{float(data['volume']):,}**\n> Traded Price: *$*{data['last_price']}**\n> Capture Time: **{data['start_time']}**")
        embed.add_embed_field(name=f"Official Open:", value=f"> **${data['official_open']}**\n> VWAP: **${data['day_vwap']}**\n> VWAP Differential: **{round(float(vwap_differential)*100,2)}%**")
        embed.add_embed_field(name=f"Greeks:", value=f"> Delta: **{round(float(optsnap.delta[0]),2)}**\n> Gamma: **{round(float(optsnap.gamma[0]),2)}**\n> Theta: **{round(float(optsnap.theta[0]),2)}**\n> Vega: **{round(float(optsnap.vega[0]),2)}**\n> IV: **{round(float(optsnap.implied_volatility[0])*100,2)}%**")
        embed.add_embed_field(name=f"OI vs VOL:", value=f"> **{float(optsnap.open_interest[0]):,}**\n> *vs*\n> **{float(optsnap.volume[0]):,}**")
        embed.add_embed_field(name=f"Quote Capture:", value=f"> Bid Size: **${optsnap.bid_size[0]}**\n> Ask Size: **${optsnap.ask_size[0]}**\n> Bid Price: **${optsnap.bid[0]}**\n> Ask Price: **${optsnap.ask[0]}**")
        embed.add_embed_field(name=f"Trade Condition:", value=f"> **{optsnap.conditions[0]}")
        if rsi_minute is not None and rsi_day is not None and rsi_hour is not None and rsi_week is not None:
            embed.add_embed_field(name=f"RSI Snapshot:", value=f"> Minute: **{round(float(rsi_minute[0]),2)}**\n> Hour: **{round(float(rsi_hour[0]),2)}**\n> Day: **{round(float(rsi_day[0]),2)}**\n> Week: **{round(float(rsi_week[0]),2)}")
        embed.set_thumbnail(await poly.get_polygon_logo(underlying_ticker))
        embed.set_timestamp()
        embed.set_footer(text=f"{option_ticker}")
        hook.add_embed(embed)
 
        await hook.execute()



async def spx_trades(data):

    ticker = data['symbol']
    if 'SPXW' in data['symbol'] and data['size'] >= 100:
        snapshot_data = await master.get_universal_snapshot(data['symbol'])
        conditions = [option_condition_dict.get(condition) for condition in snapshot_data.conditions[0]] if snapshot_data.conditions is not None else []
        if snapshot_data.open_interest is not None and snapshot_data.volume is not None and snapshot_data.open_interest < snapshot_data.volume:
            answer = "Yes"
        else:
            answer = "No"
        hook = AsyncDiscordWebhook(spx, content=f"<@375862240601047070>")
        hook2 = AsyncDiscordWebhook(konviction)
        embed=DiscordEmbed(title=f"SPX Trade (100+ Volume)", description=f"```py\n{ticker} just traded for {data['size']} contracts @ price: #{data['price']}```", color=hex_colors['yellow'])
        embed.add_embed_field(name=f"Contract Stats:", value=f"> Open: **${snapshot_data.open[0]}**\n> High: **${snapshot_data.high[0]}**\n> Last: **${snapshot_data.close[0]}**\n> Low: **${snapshot_data.low[0]}**")
        embed.add_embed_field(name=f"Session Stats:", value=f"> Change Percent: **{round(float(snapshot_data.change_percent[0]),2)}%**")
        embed.add_embed_field(name=f"Vol vs OI:", value=f"> Vol: **{float(snapshot_data.volume[0]):,}**\n> OI: **{float(snapshot_data.open_interest[0]):,}**\n> Unusual? **{answer}**")
        if snapshot_data.gamma is not [None]:
            embed.add_embed_field(name=f"Greeks:", value=f"> Delta: **{round(float(snapshot_data.delta[0]),2)}**\n> Gamma: **{round(float(snapshot_data.gamma[0]),2)}**\n> Vega: **{round(float(snapshot_data.vega),2)}**\n> Theta: **{round(float(snapshot_data.theta),2)}**\n> IV: **{round(float(snapshot_data.implied_volatility[0])*100,2)}%**", inline=False)
        embed.add_embed_field(name=f"Last Trade:", value=f"> Size: **{snapshot_data.trade_size[0]}**\n> Price: **{snapshot_data.trade_price[0]}**\n> Exchange: **{OPTIONS_EXCHANGES.get(snapshot_data.exchange[0])}**\n> Condition: **{conditions}**")
        embed.add_embed_field(name=f"Last Quote:", value=f"> Bid: **${snapshot_data.bid[0]}**\n> Bid Size: **{snapshot_data.bid_size[0]}**\n> Mid: **${snapshot_data.midpoint[0]}**\n> Ask: **${snapshot_data.ask[0]}**\n> Ask Size: **{snapshot_data.ask_size[0]}**")
        embed.add_embed_field(name=f"Underlying:", value=f"> {snapshot_data.underlying_ticker[0]}'s price: **${snapshot_data.underlying_price[0]}**")
        embed.set_footer(text=f"{data['symbol']}")
        embed.set_timestamp()
        hook.add_embed(embed)
        hook2.add_embed(embed)
        await hook.execute()
        await hook2.execute()
        print(data['symbol'])


async def send_to_sectors(data):

    ticker = await poly_opts.extract_underlying_symbol(data['symbol'])
    if data['symbol'] is not None:
        symb = human_readable(data['symbol'])
    else:
        symb=  None
    sector = symbol_to_sector.get(ticker)
    # Get the webhook URL for the sector
    webhook_url = sector_hooks.get(sector)
    tasks = []
    if webhook_url:
        # Create the webhook object
        webhook = AsyncDiscordWebhook(webhook_url, content="<@375862240601047070>")

        # Create the embed message
        if symb is not None:
            embed = DiscordEmbed(title=f"Last Trade: {symb}",
                                description=f"> Trade: **{data['size']}** shares @ **${data['price']}**\n\n> Conditions: **{data['conditions']}**\n\n> Exchange: **{data['exchange']}**")
            webhook.add_embed(embed)

        # Create a task for sending the webhook message to the corresponding sector channel
        task = asyncio.create_task(webhook.execute())
        tasks.append(task)
        await webhook.execute()
        print(f"EXECUTED WEBHOOK")


async def send_exchanges(webhook_url, data):
        webhook2 = AsyncDiscordWebhook(konviction)
        if data['symbol'] is not None and data['size'] > 500:
            symb = human_readable(data['symbol'])
            underlying_ticker = await poly_opts.extract_underlying_symbol(data['symbol'])
        else:
            symb = None

        if symb is not None:
            exchange = OPTIONS_EXCHANGES.get(data['exchange'])
            webhook = AsyncDiscordWebhook(webhook_url,content=f"> <@375862240601047070>")
            embed = DiscordEmbed(title=f"Large Trade - {symb}", description=f"> Trade Price:\n> **${data['price']}**\n> Last Price: **${data['size']}**\n> Exchange: **{exchange}**")
            embed.add_embed_field(name=f"Timestamp:", value=f"> **{data['timestamp']}**")
            embed.set_thumbnail(await poly.get_polygon_logo(underlying_ticker))
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook2.add_embed(embed)
            await webhook.execute()
            await webhook2.execute()