"""
PLOT CHARTS USING AGGREGATES DATA
"""
import asyncio
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from cfg import YOUR_API_KEY
poly = PolygonOptionsSDK(YOUR_API_KEY)


underlying_symbol="SPY"
expiration_date="2023-05-22"
option_type="C"
strike_price="400"
multiplier=1
timespan="hour"
from_date="2023-01-01"
to_date="2023-05-22"
order="desc"
limit=100


async def main():

    ticker = await poly.generate_option_symbol(underlying_symbol,expiration_date,option_type,strike_price)
    print(ticker)
    aggs = await poly.get_aggregate_bars(ticker, multiplier, timespan, from_date, to_date,adjusted=True, limit=100)
    print(aggs)
    close = [i.close for i in aggs]
    high = [i.close for i in aggs]
    low = [i.close for i in aggs]
    open = [i.close for i in aggs]
    timestamp = [i.close for i in aggs]
    volume = [i.volume for i in aggs]
    vwap = [i.vw for i in aggs]
    num_trades = [i.number_of_trades for i in aggs]
    
    data = {
        'Open': open,
        'High': high,
        'Low': low,
        'Close': close,
        'Time': timestamp,
        'Volume': volume
    }
    print(data)
    df = pd.DataFrame(data)

    # Convert timestamp to datetime and set it as index
    df['Time'] = pd.to_datetime(df['Time'], unit='ms')
    df.set_index('Time', inplace=True)
    df.sort_index(inplace=True)
    # Rename columns to match mplfinance requirements
    df.rename(columns={'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume'}, inplace=True)

    # Plot the candlestick chart using mplfinance
    mpf.plot(df, type='candle', style='mike', title=f'{ticker} - {multiplier} {timespan}', ylabel='Price ($)', volume=True)

asyncio.run(main())

