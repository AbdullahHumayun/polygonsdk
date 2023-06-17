import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


import mplfinance as mpf
import pandas as pd
import numpy as np
from cfg import YOUR_API_KEY, today_str
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
sdk = AsyncPolygonSDK(YOUR_API_KEY)

import matplotlib.pyplot as plt
import mplfinance as mpf

from discord_webhook import AsyncDiscordWebhook, DiscordEmbed



async def send_to_discord(buf, filename, webhook_url: AsyncDiscordWebhook, embed: DiscordEmbed):

    
    # Create file
    with open(filename, "rb") as f:
        webhook_url.add_file(file=f.read(), filename=filename)

    # Add embed object to webhook
    embed.set_image(url=f'attachment://{filename}')
    webhook_url.add_embed(embed)

    # Execute the webhook
    await webhook_url.execute()

async def logo(ticker):
    ticker_logo = await sdk.get_polygon_logo(ticker)
    return ticker_logo



async def scan_morning_star(symbol, multiplier):
    aggs = await sdk.get_aggregates(ticker=symbol, multiplier=multiplier, timespan="day", from_date="2023-04-12", to_date=today_str, order="desc", limit=100)

    if aggs is not None:
        closes = aggs.close
        opens = aggs.open
        lows = aggs.low
        highs = aggs.high
        volumes = aggs.volume
        timestamps = aggs.timestamp

        if len(opens) < 3 or len(closes) < 3 or len(highs) < 3 or len(lows) < 3:
            return False

        first_open = opens[0]
        print(f"{first_open} {symbol}")
        first_low = lows[0]
        second_open = opens[1]
        second_close = closes[1]
        second_high = highs[1]
        third_low = lows[2]


        if first_low > second_high and \
        third_low > second_high and second_close > second_open:
            return True
        else:
            return False
  


async def scan_evening_star(symbol, multiplier):

    aggs = await sdk.get_aggregates(ticker=symbol, multiplier=multiplier, timespan="day", from_date="2023-04-12", to_date=today_str, order="desc", limit=100)
    if aggs is not None:
        closes = aggs.close
        opens = aggs.open
        lows = aggs.low
        highs = aggs.high
        volumes = aggs.volume
        timestamps = aggs.timestamp

        datas = { 
            'Close': closes,
            'Open': opens,
            'High': highs,
            'Low': lows,
            'Volume': volumes,
            'Timestamp': pd.to_datetime(timestamps, unit='ms')
        }

        df = pd.DataFrame(datas)
        if df.empty:
            print("The DataFrame is empty.")
            return False

    
        for i in range(10, len(df)):
            candle_0 = df.iloc[i-2]
            candle_1 = df.iloc[i-1]
            candle_2 = df.iloc[i]
            if (
                candle_1['Low'] > candle_0['High'] and\
                candle_1['Low'] > candle_2['Close'] and\
                candle_1['Close'] < candle_0['Open'] and\
                candle_1['Close'] < candle_2['Open']
                

            ):
                return True
            else:
                return False
            



async def scan_bearish_engulfing(df):
    bearish_engulfing_patterns = []
    for i in range(1, len(df)):
        candle_0 = df.iloc[i-2]
        candle_1 = df.iloc[i]
        candle_2 = df.iloc[i-2]

        if (
            candle_0['Close'] > candle_0['Open'] and
            candle_1['Low'] > candle_0['High'] and
            candle_1['Low'] > candle_2['Close'] and
            candle_1['Close'] < candle_0['Open']
        ):
            bearish_engulfing_patterns.append((candle_0.name, candle_1.name))

    return bearish_engulfing_patterns


def scan_bullish_engulfing(df):
    bullish_engulfing_patterns = []
    for i in range(1, len(df)):
        candle_0 = df.iloc[i-1]
        candle_1 = df.iloc[i]

        if (
            candle_0['Close'] < candle_0['Open'] and
            candle_1['Close'] > candle_1['Open'] and
            candle_1['Open'] < candle_0['Close'] and
            candle_1['Close'] > candle_0['Open']
        ):
            bullish_engulfing_patterns.append((candle_0.name, candle_1.name))

    return bullish_engulfing_patterns






async def get_logo(ticker):
    logo = await sdk.get_polygon_logo(ticker)
    return logo


async def get_rsi(ticker):
    rsi = await sdk.get_rsi(ticker, limit=60)
    return rsi