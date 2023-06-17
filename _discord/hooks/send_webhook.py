import aiohttp
from discord_webhook import AsyncDiscordWebhook, DiscordEmbed
from sdks.helpers.helpers import human_readable

async def send_webhook(webhook_url, logo, description,symb, price, ask, mid, bid, bid_size, ask_size, break_even, 
                       change_to_break_even, contract_type, day_change, day_change_percent, 
                       close, high, open, low, decoded_conditions, last_trade_exchange, 
                       last_sip_timestamp, last_trade_price, last_trade_size, previous_close, 
                       day_volume, day_vwap, delta, gamma, theta, vega, iv, expiration, strike, 
                       exercise_style, under_ticker, oi, er_date, avg_10d_vol, avg_3m_vol, fifty_high, 
                       fifty_low, outstanding_shares, total_shares, name, underlying_vol, underlying_changep, 
                       underlying_price, underlying_high, underlying_low, underlying_open, underlying_vibration_ratio, 
                       underlying_total_volume, underlying_buy_volume, underlying_sell_volume, underlying_n_volume, underlying_avg_price,
                       option_buy_volume, option_neutral_volume, option_sell_volume, option_sweep_volume, option_multi_leg, option_stock_multi, option_total_volume, num_option_trades, short_int:str=None, dtc: str=None, settlement_date:str = None, avg_volume: str=None):
    # Create a new embed
    embed = DiscordEmbed(title="New Trade Alert", description=description)
    
    # Add fields to the embed
    embed.add_embed_field(name="Symbol", value=f"> **{human_readable(symb)}**")
    embed.add_embed_field(name=f"{under_ticker} Price", value=f"> **${price}**")
    embed.add_embed_field(name="Option Volume", value=f"> **{day_volume}**")
    embed.add_embed_field(name=f"Option Volume Analysis:", value=f"> Buy: **{float(option_buy_volume):,}**\n> Neutral: **{float(option_neutral_volume):,}**\n> Sell: **{float(option_sell_volume):,}\n> Sweep: **{float(option_sweep_volume):,}**\n> Multi-Leg: **{float(option_multi_leg):,}**\n> Total: **{float(option_total_volume):,}**")
    embed.add_embed_field(name=f"Last Trade Info:", value=f"> Size: **{float(last_trade_size):,}**\n> Price: **${last_trade_price}**")
    embed.add_embed_field(name="Conditions", value=f"**{decoded_conditions}**")
    embed.add_embed_field(name=f"Greeks:", value=f"> Gamma: **{round(float(gamma),4)}**\n> Delta: **{round(float(delta),4)}**\n> Vega: **{round(float(vega),4)}**\n> Theta: **{round(float(theta),4)}**")
    embed.add_embed_field(name=f"Open Interest:", value=f"> **{float(oi):,}**")
    embed.add_embed_field(name=f"IV:", value=f"> **{round(float(iv)*100,2)}**%")
    embed.add_embed_field(name=f"Bid/Ask:", value=f"> Bid: **${bid}** @ size: **{bid_size}**\n> Ask: **${ask}** @ size: **{ask_size}**")
    embed.add_embed_field(name=f"Day Stats:", value=f"> Open: **${open}**\n> High: **${high}**\n> Last: **${close}**\n> Low: **${low}**")
    embed.add_embed_field(name=f"Change on Day:", value=f"> **{float(day_change_percent)*100}%**")
    embed.add_embed_field(name=f"Day Vwap:", value=f"> **${day_vwap}**")
    embed.set_thumbnail(logo)
    embed.set_timestamp()
    embed.set_footer(text=f"{symb}")

    # Set the author and footer of the embed
    embed.set_author(name="FUDSTOP Trading")


    # Add the embed to the webhook and execute
    webhook_url.add_embed(embed)
    await webhook_url.execute()


async def send_stock_webhook(webhook_url, logo, description, symbol, change_percent, conditions,close, high, open, low, last_trade_price, last_trade_size, day_volume, er_date, avg_10d_vol, avg_3m_vol, fifty_high, fifty_low, outstanding_shares, total_shares, name, underlying_vol, underlying_changep, underlying_price, underlying_high, underlying_low, underlying_open, underlying_vibration_ratio, underlying_total_volume, underlying_buy_volume, underlying_sell_volume, underlying_n_volume, underlying_avg_price, color, short_int:str=None, dtc: str=None, settlement_date:str = None, avg_volume: str=None, ticker_id: str=None):
    # Create a new embed
    
    embed = DiscordEmbed(title=f"New Trade Alert - {symbol}", description=f"**{description}**")

    # Add fields to the embed
    embed.add_embed_field(name=f"{symbol} Price", value=f"> **${last_trade_price}**")
    embed.add_embed_field(name="Stock Volume", value=f"> **{float(day_volume):,}**")
    embed.add_embed_field(name=f"Stock Volume Analysis:", value=f"> Buy: **{float(underlying_buy_volume):,}**\n> Neut: **{float(underlying_n_volume):,}**\n> Sell: **{float(underlying_sell_volume):,}**")
    embed.add_embed_field(name=f"Last Trade Info:", value=f"> Size: **{float(last_trade_size):,}**\n> Price: **${last_trade_price}**\n> Average Price: **${underlying_avg_price}**")
    embed.add_embed_field(name="Conditions", value=f"**{conditions}**")
    embed.add_embed_field(name=f"Day Stats:", value=f"> Open: **${open}**\n> High: **${high}**\n> Last: **${close}**\n> Low: **${low}**")
    embed.add_embed_field(name=f"Change on Day:", value=f"> **{round(float(change_percent),2)}%**")
    embed.add_embed_field(name=f"Next Earnings:", value=f"```py\n{er_date}```")

    
    embed.set_footer(text=f"Data Provided by Polygon.io - use code FUDSTOP")
    embed.set_thumbnail(logo)
    embed.set_timestamp()
    # Set the author and footer of the embed
    embed.set_author(name="FUDSTOP Trading")


    # Add the embed to the webhook and execute
    webhook_url.add_embed(embed)
    await webhook_url.execute()

