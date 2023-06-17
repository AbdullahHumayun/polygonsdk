import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

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
        underlying_symbol="AAPL", 
        expiration_date="2023-05-19", 
        option_type="C", 
        strike_price=160) #options take 'O:' (when generated - this is included in the query)

    forex_symbol = "C:EURUSD" #forex take 'C:'

    crypto_symbol = "X:BTCUSD" #crypto take 'X:'

    indicies_symbol = "I:DJI" #indices take 'I:'




    stock_sma = await poly.get_simple_moving_average(
        symbol=stock_symbol,
        timespan="quarter",
        adjusted=True,
        window=64, 
        limit=100
        )

    forex_sma = await poly.get_simple_moving_average(
        symbol=forex_symbol, 
        timespan="day", 
        adjusted=True, 
        window=251, 
        limit=100
        )
    


    crypto_sma = await poly.get_simple_moving_average(
        symbol=crypto_symbol, 
        timespan="day", 
        adjusted=True, 
        window=200, 
        limit=10
        )

    option_sma = await poly.get_simple_moving_average(
        symbol=option_symbol, 
        timespan="hour", 
        adjusted=True, 
        window=21, 
        limit=5
        )


    
    print(f"STOCK SMA64 FOR {stock_symbol}: {stock_sma[0]}")
    print()
    print(f"OPTION SMA251 FOR {option_symbol}: {option_sma[0]}")
    print()
    print(f"FOREX SMA200 FOR {forex_symbol}: {forex_sma[0]}")
    print()
    print(f"CRYPTO SMA21 FOR {crypto_symbol}: {crypto_sma[0]}")



asyncio.run(main())