import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio



from sdks.webull_sdk.webull_sdk import AsyncWebullSDK

sdk = AsyncWebullSDK()

async def stock_data(ticker="NVDA"):

    stock_data = await sdk.get_webull_stock_data(ticker)

    fiftyhigh = stock_data.fifty_high
    fiftylow = stock_data.fifty_low
    close = stock_data.web_stock_close
    high = stock_data.web_stock_high
    low = stock_data.web_stock_low
    open_ = stock_data.web_stock_open
    changeratio = round(float(stock_data.web_change_ratio) * 100, 2)
    vol = float(stock_data.web_stock_vol)
    vr = stock_data.web_vibrate_ratio

    outstanding_shares = stock_data.outstanding_shares
    total_shares = stock_data.total_shares

    avg_10day_volume = stock_data.avg_10d_vol
    avg_3month_volume = stock_data.avg_vol3m
    company_name = stock_data.web_name
    symbol = stock_data.web_symb

    print("fiftyhigh:", fiftyhigh)
    print("fiftylow:", fiftylow)
    print("close:", close)
    print("high:", high)
    print("low:", low)
    print("open:", open_)
    print("changeratio:", changeratio)
    print("vol:", vol)
    print("vr:", vr)
    print("outstanding_shares:", outstanding_shares)
    print("total_shares:", total_shares)
    print("avg_10day_volume:", avg_10day_volume)
    print("avg_3month_volume:", avg_3month_volume)
    print("company_name:", company_name)
    print("symbol:", symbol)


asyncio.run(stock_data(ticker="NVDA"))