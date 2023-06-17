import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY

import asyncio

poly = AsyncPolygonSDK(YOUR_API_KEY)
polyopt = PolygonOptionsSDK(YOUR_API_KEY)




async def main():

    #get symbols for each subscription
    stock_symbol = "KRE"

    option_symbol = await polyopt.generate_option_symbol(
        underlying_symbol="AMD", 
        expiration_date="2023-05-19", 
        option_type="C", 
        strike_price=100) #options take 'O:' (when generated - this is included in the query)

    forex_symbol = "C:EURUSD" #forex take 'C:'

    crypto_symbol = "X:BTCUSD" #crypto take 'X:'

    indicies_symbol = "I:DJI" #indices take 'I:'




    stock_macd, stock_histogram, stock_signal = await poly.get_macd(
        symbol="GME",
        timespan="quarter",
        adjusted=True,
        short_window=12,
        long_window=26,
        signal_window=9, 
        limit=100
        )

    forex_macd, forex_histogram, forex_signal = await poly.get_macd(
        symbol=forex_symbol, 
        timespan="month", 
        adjusted=True, 
        short_window=12,
        long_window=26,
        signal_window=9,
        limit=21
        )

    crypto_macd, crypto_histogram, crypto_signal = await poly.get_macd(
        symbol=crypto_symbol, 
        timespan="day", 
        adjusted=True, 
        short_window=12,
        long_window=26,
        signal_window=9,
        limit=10
        )

    option_macd, option_histogram, option_signal = await poly.get_macd(
        symbol=option_symbol, 
        timespan="hour", 
        adjusted=True, 
        short_window=12,
        long_window=26,
        signal_window=9,
        limit=5
        )

    indicies_macd, indices_histogram, indices_signal = await poly.get_macd(
        symbol=indicies_symbol, 
        timespan="minute", 
        adjusted=True, 
        short_window=12,
        long_window=26,
        signal_window=9,
        limit=5
        )

    print(f"STOCK MACD FOR {stock_symbol}: {stock_macd}")
    print(f"STOCK HISTOGRAM FOR {stock_symbol}: {stock_histogram}")
    print(f"STOCK SIGNAL FOR {stock_symbol}: {stock_signal}")
    print()
    print(f"OPTION MACD FOR {option_symbol}: {option_macd}")
    print(f"OPTION HISTOGRAM FOR {option_symbol}: {option_histogram}")
    print(f"OPTION SIGNAL FOR {option_symbol}: {option_signal}")
    print()
    print(f"FOREX MACD FOR {forex_symbol}: {forex_macd}")
    print(f"FOREX HISTOGRAM FOR {forex_symbol}: {forex_histogram}")
    print(f"FOREX SIGNAL FOR {forex_symbol}: {forex_signal}")
    print()
    print(f"CRYPTO MACD FOR {crypto_symbol}: {crypto_macd}")
    print(f"CRYPTO HISTOGRAM FOR {crypto_symbol}: {crypto_histogram}")
    print(f"CRYPTO SIGNAL FOR {crypto_symbol}: {crypto_signal}")
    print()
    print(f"INDICES MACD FOR {indicies_symbol}: {indicies_macd}")
    print(f"INDICES HISTOGRAM FOR {indicies_symbol}: {indices_histogram}")
    print(f"INDICES SIGNAL FOR {indicies_symbol}: {indices_signal}")


asyncio.run(main())