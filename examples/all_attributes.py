"""FILE SHOWING ALL AVAILABLE ATTRIBUTES FROM THE PROGRAM"""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio


from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
from sdks.fudstop_sdk.fudstop_sdk import fudstopSDK
from sdks.helpers.helpers import human_readable

from cfg import YOUR_API_KEY, five_days_ago_str, today_str

poly = AsyncPolygonSDK(YOUR_API_KEY)
webull = AsyncWebullSDK()
fudstop = fudstopSDK()

ticker = "AMC"

async def polygon_attributes(ticker):

    single_snapshot = await poly.get_stock_snapshot(ticker=ticker)
    
    day_open = single_snapshot.stock_day.open
    day_high = single_snapshot.stock_day.high
    day_low = single_snapshot.stock_day.low
    day_close = single_snapshot.stock_day.close
    day_vol = single_snapshot.stock_day.volume
    day_vwap = single_snapshot.stock_day.vwap

    last_trade_conditions = single_snapshot.last_trade.conditions
    last_trade_exchange = single_snapshot.last_trade.trade_exchange
    last_trade_id = single_snapshot.last_trade.trade_id
    last_trade_price = single_snapshot.last_trade.trade_price
    last_trade_size = single_snapshot.last_trade.trade_size
    last_trade_timestamp = single_snapshot.last_trade.trade_timestamp

    bid_price = single_snapshot.stock_last_quote.bid_price
    bid_size = single_snapshot.stock_last_quote.bid_size
    ask_price = single_snapshot.stock_last_quote.ask_price
    ask_size = single_snapshot.stock_last_quote.ask_size

    min_close = single_snapshot.stock_minute_bar.close
    min_open = single_snapshot.stock_minute_bar.open
    min_high = single_snapshot.stock_minute_bar.high
    min_low = single_snapshot.stock_minute_bar.low
    min_vwap = single_snapshot.stock_minute_bar.vwap
    min_volume = single_snapshot.stock_minute_bar.volume
    min_accumulated = single_snapshot.stock_minute_bar.accumulated_volume

    prev_open = single_snapshot.prev_day.open
    prev_close = single_snapshot.prev_day.close
    prev_high = single_snapshot.prev_day.high
    prev_low = single_snapshot.prev_day.low
    prev_vol = single_snapshot.prev_day.volume
    prev_vwap = single_snapshot.prev_day.vwap

    change_percent = single_snapshot.today_changep
    dollar_change = single_snapshot.today_change

    
    print(f"{ticker}'s Day Stats:")
    print(f"--------------")
    print(f"Open: ${day_open}")
    print(f"High: ${day_high}")
    print(f"Low: ${day_low}")
    print(f"Close: ${day_close}")
    print(f"VWAP: ${day_vwap}")
    print(f"Volume: {day_vol}")
    print(f"Change Percent: {change_percent}%")
    print(f"Dollar Change: {dollar_change}")
    print()
    print(f"{ticker}'s Last Trade:")
    print(f"--------------")
    print(f"Size: {last_trade_size}")
    print(f"Price: {last_trade_price}")
    print(f"ID: {last_trade_id}")
    print(f"Condition: {last_trade_conditions}")
    print(f"Exchange: {last_trade_exchange}")
    print(f"Timestamp: {last_trade_timestamp}")
    print()
    print(f"{ticker}'s Last Quote:")
    print(f"--------------")
    print(f"Ask Price: ${ask_price} Size: {ask_size}")
    print(f"Bid Price: ${bid_price} Size: {bid_size}")
    print()
    print(f"{ticker}'s Last Minute Data:")
    print(f"---------------")
    print(f"Open: ${min_open}")
    print(f"High: ${min_high}")
    print(f"Low: ${min_low}")
    print(f"Close: ${min_close}")
    print(f"VWAP: ${min_vwap}")
    print(f"Volume: {min_volume}")
    print(f"Accumulated Volume: {min_accumulated}")
    print()
    print(f"{ticker}'s Previous Day Data:")
    print(f"---------------")
    print(f"Open: ${prev_open}")
    print(f"High: ${prev_high}")
    print(f"Low: ${prev_low}")
    print(f"Close: ${prev_close}")
    print(f"VWAP: ${prev_vwap}")
    print(f"Volume: {prev_vol}")
    print()



    aggs = await poly.get_aggregates(ticker=ticker, multiplier=1, timespan="hour", from_date=five_days_ago_str, to_date=today_str)

    close = aggs.close # list
    open = aggs.open # list
    high = aggs.high # list
    low = aggs.low # list
    timestamp = await poly.format_timestamps_list(aggs.timestamp)  # list converted

    volume = aggs.volume # list
    vwap = aggs.volume_weighted_average # list
    print(f"{ticker} Aggs Close: ${close}")
    print(f"{ticker} Aggs Open: ${close}")
    print(f"{ticker} Aggs High: ${close}")
    print(f"{ticker} Aggs Low: ${close}")
    print(f"{ticker} Aggs Timestamp: ${timestamp}")
    print(f"{ticker} Aggs Timestamp: {volume}")
    print(f"{ticker} Aggs Timestamp: ${vwap}")
    print()

    
    rsi = await poly.get_rsi(symbol=ticker, timespan="day", adjusted=True, window=14, limit=1)
    print(rsi)

    macd, histogram, signal = await poly.get_macd(symbol=ticker, timespan="day", adjusted=True, short_window=12, long_window=26, signal_window=9, limit=5)

    print(f"{ticker} MACD: {macd}")
    print(f"{ticker} MACD Histogram: {histogram}")
    print(f"{ticker} MACD Signal: {signal}")
    print()

    ema_list, ema_timestamps  = await poly.get_exponential_moving_average(symbol=ticker, timespan="hour", adjusted=True, window=21, limit=5)

    print(f"{ticker}'s latest VWAP: ${vwap}")
    print(f"{ticker} 21 EMA Historic List: {ema_list}")
    print()

    sma_list, sma_timestamps  = await poly.get_exponential_moving_average(symbol=ticker, timespan="hour", adjusted=True, window=50, limit=5)

    print(f"{ticker}'s latest VWAP: ${vwap}")
    print(f"{ticker} SMA 50 Historic List: {sma_list}")
    print()

    support, resistance = await poly.get_support_resistance_levels(stock_ticker=ticker, multiplier=1, timespan="hour", from_date=five_days_ago_str, to_date=today_str)
    
    print(f"{ticker}'s Resistance: ${resistance}")
    print(f"{ticker}'s VWAP: ${vwap}")
    print(f"{ticker}'s Support: ${support}")



asyncio.run(polygon_attributes(ticker=ticker))
