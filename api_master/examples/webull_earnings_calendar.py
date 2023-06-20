import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

import pandas as pd

from sdks.webull_sdk.top_gainers import Ticker
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
from cfg import today_str

sdk = AsyncWebullSDK()


async def earnings_calendar(date=today_str):





    calendar = await sdk.get_earnings_calendar(today_str)


    release_id = [i.earning_release_id for i in calendar]
    eps = [i.eps for i in calendar]
    earnings_release_id = [i.earning_release_id for i in calendar]
    is_live = [i.is_live for i in calendar]
    last_release_date = [i.last_release_date for i in calendar]
    publish_status = [i.publish_status for i in calendar]
    quarter = [i.quarter for i in calendar]
    qualifier = [i.qualifier for i in calendar]
    region_id = [i.region_id for i in calendar]
    release_date = [i.release_date for i in calendar]
    ticker_id = [i.ticker_id for i in calendar]
    values = [i.values for i in calendar]
    year = [i.year for i in calendar]

    #access data for each earnings ticker
    ticker=[i.ticker for i in calendar]
    ticker = Ticker(ticker)
    change = ticker.change
    change_ratio = ticker.changeRatio
    close_price = ticker.close
    currency_code = ticker.currencyCode
    currency_id = ticker.currencyId
    derivative_support = ticker.derivativeSupport
    dis_exchange_code = ticker.disExchangeCode
    dis_symbol = ticker.disSymbol
    exchange_code = ticker.exchangeCode
    exchange_id = ticker.exchangeId
    fifty_two_week_high = ticker.fiftyTwoWkHigh
    fifty_two_week_low = ticker.fiftyTwoWkLow
    high_price = ticker.high
    low_price = ticker.low
    volume = ticker.volume
    vibrate_ratio = ticker.vibrateRatio
    symbol = ticker.symbol
    pe_ttm = ticker.peTtm


    #output from attributes

    print("release_id:", release_id)
    print("eps:", eps)
    print("earnings_release_id:", earnings_release_id)
    print("is_live:", is_live)
    print("last_release_date:", last_release_date)
    print("publish_status:", publish_status)
    print("quarter:", quarter)
    print("qualifier:", qualifier)
    print("region_id:", region_id)
    print("release_date:", release_date)
    print("ticker_id:", ticker_id)
    print("values:", values)
    print("year:", year)
    print("ticker:", ticker)
    print("change:", change)
    print("change_ratio:", change_ratio)
    print("close_price:", close_price)
    print("currency_code:", currency_code)
    print("currency_id:", currency_id)
    print("derivative_support:", derivative_support)
    print("dis_exchange_code:", dis_exchange_code)
    print("dis_symbol:", dis_symbol)
    print("exchange_code:", exchange_code)
    print("exchange_id:", exchange_id)
    print("fifty_two_week_high:", fifty_two_week_high)
    print("fifty_two_week_low:", fifty_two_week_low)
    print("high_price:", high_price)
    print("low_price:", low_price)
    print("volume:", volume)
    print("vibrate_ratio:", vibrate_ratio)
    print("symbol:", symbol)
    print("pe_ttm:", pe_ttm)

    # Creating a dictionary with attribute lists
    data = {
        'release_id': release_id,
        'eps': eps,
        'earnings_release_id': earnings_release_id,
        'is_live': is_live,
        'last_release_date': last_release_date,
        'publish_status': publish_status,
        'quarter': quarter,
        'qualifier': qualifier,
        'region_id': region_id,
        'release_date': release_date,
        'ticker_id': ticker_id,
        'values': values,
        'year': year,
        'ticker': ticker,
        'change': change,
        'change_ratio': change_ratio,
        'close_price': close_price,
        'currency_code': currency_code,
        'currency_id': currency_id,
        'derivative_support': derivative_support,
        'dis_exchange_code': dis_exchange_code,
        'dis_symbol': dis_symbol,
        'exchange_code': exchange_code,
        'exchange_id': exchange_id,
        'fifty_two_week_high': fifty_two_week_high,
        'fifty_two_week_low': fifty_two_week_low,
        'high_price': high_price,
        'low_price': low_price,
        'volume': volume,
        'vibrate_ratio': vibrate_ratio,
        'symbol': symbol,
        'pe_ttm': pe_ttm
    }

    # Define the directory path
    directory = 'files/earnings/'

    # Create the directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Define the file path
    filename = f'{directory}earnings_calendar.csv'
    # Creating a DataFrame
    df = pd.DataFrame(data)
    df.to_csv(filename)

asyncio.run(earnings_calendar(date=today_str))