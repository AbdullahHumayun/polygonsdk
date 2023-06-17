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
    stock_symbol = "AAPL"

    option_symbol = await polyopt.generate_option_symbol(
        underlying_symbol="F", 
        expiration_date="2023-05-19", 
        option_type="C", 
        strike_price=11.5) #options take 'O:' (when generated - this is included in the query)

    forex_symbol = "C:EURUSD" #forex take 'C:'

    crypto_symbol = "X:BTCUSD" #crypto take 'X:'

    indicies_symbol = "I:DJI" #indices take 'I:'




    stock_ema, stock_ema_timestamp = await poly.get_exponential_moving_average(
        symbol=stock_symbol,
        timespan="quarter",
        adjusted=True,
        window=64, 
        limit=100
        )

    forex_ema, forex_ema_timestamp = await poly.get_exponential_moving_average(
        symbol=forex_symbol, 
        timespan="day", 
        adjusted=True, 
        window=251, 
        limit=100
        )
    


    crypto_ema, crypto_ema_timestamp = await poly.get_exponential_moving_average(
        symbol=crypto_symbol, 
        timespan="day", 
        adjusted=True, 
        window=200, 
        limit=10
        )

    option_ema, options_ema_timestamp = await poly.get_exponential_moving_average(
        symbol=option_symbol, 
        timespan="hour", 
        adjusted=True, 
        window=21, 
        limit=5
        )

    indices_ema, indices_ema_timestamp  = await poly.get_exponential_moving_average(
        symbol=indicies_symbol, 
        timespan="hour", 
        adjusted=True, 
        window=50, 
        limit=200
        )
    
    print(f"STOCK EMA64 FOR {stock_symbol}: {stock_ema[0]} {stock_ema_timestamp[0]}")

    print(f"OPTION EMA251 FOR {option_symbol}: {option_ema[0]} {stock_ema_timestamp[0]}")

    print(f"FOREX EMA200 FOR {forex_symbol}: {forex_ema[0]} {stock_ema_timestamp[0]}")

    print(f"CRYPTO EMA21 FOR {crypto_symbol}: {crypto_ema[0]} {stock_ema_timestamp[0]}")

    print(f"INDICES EMA50 LATEST TIMESTAMPS FOR {indicies_symbol}: {indices_ema[0]} {stock_ema_timestamp[0]}")


asyncio.run(main())