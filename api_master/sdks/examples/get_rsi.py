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
        underlying_symbol="KRE", 
        expiration_date="2023-05-19", 
        option_type="C", 
        strike_price=20) #options take 'O:' (when generated - this is included in the query)

    forex_symbol = "C:EURUSD" #forex take 'C:'

    crypto_symbol = "X:BTCUSD" #crypto take 'X:'

    indicies_symbol = "I:DJI" #indices take 'I:'




    stock_rsi = await poly.get_rsi(
        symbol="GME",
        timespan="quarter",
        adjusted=True,
        window=14, 
        limit=100
        )

    forex_rsi = await poly.get_rsi(
        symbol=forex_symbol, 
        timespan="month", 
        adjusted=True, 
        window=14, 
        limit=21
        )

    crypto_rsi = await poly.get_rsi(
        symbol=crypto_symbol, 
        timespan="day", 
        adjusted=True, 
        window=14, 
        limit=10
        )

    option_rsi = await poly.get_rsi(
        symbol=option_symbol, 
        timespan="hour", 
        adjusted=True, 
        window=14, 
        limit=5
        )

    indicies_rsi = await poly.get_rsi(
        symbol=indicies_symbol, 
        timespan="hour", 
        adjusted=True, 
        window=14, 
        limit=10
        )

    print(f"STOCK RSI FOR {stock_symbol}: {stock_rsi.rsi_value[0]}") 

    print(f"OPTION RSI FOR {option_symbol}: {option_rsi.rsi_value[0]}")

    print(f"FOREX RSI FOR {forex_symbol}: {forex_rsi.rsi_value[0]}")

    print(f"CRYPTO RSI FOR {crypto_symbol}: {crypto_rsi.rsi_value[0]}")

    print(f"INDICES RSI FOR {indicies_symbol}: {indicies_rsi.rsi_value[0]}")


asyncio.run(main())