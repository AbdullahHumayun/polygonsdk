
import aiohttp
from api_master.sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK

from collections import defaultdict
from api_master.sdks.polygon_sdk.universal_snapshot import UniversalOptionSnapshot,UniversalSnapshot
import asyncio
import pandas as pd
from api_master.sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
import numpy as np
from tabulate import tabulate
from api_master.cfg import YOUR_API_KEY, today_str, thirty_days_from_now_str, two_years_from_now_str
opts = PolygonOptionsSDK(YOUR_API_KEY)
poly = AsyncPolygonSDK(YOUR_API_KEY)

ticker="GME"
async def main(tickers:str):
    table_data = []

    for ticker in tickers:
        atm_calls, atm_puts = await opts.get_near_the_money_options(ticker)
        if ticker.startswith("SPX"):
            price = await poly.get_index_price(ticker)
        else:
            price = await poly.get_stock_price(ticker)

        first_row_volume_calls = atm_calls.iloc[0]['Vol']
        first_row_volume_puts = atm_puts.iloc[0]['Vol']
        first_row_oi_calls = atm_calls.iloc[0]['OI']
        first_row_oi_puts = atm_puts.iloc[0]['OI']
        first_row_iv_puts = atm_puts.iloc[0]['IV']
        first_row_iv_calls = atm_calls.iloc[0]['IV']

        first_row_exp_calls = atm_calls.iloc[0]['🗓️']
        first_row_exp_puts = atm_puts.iloc[0]['🗓️']
        first_row_skew_calls = atm_calls.iloc[0]['Skew']
        first_row_skew_puts = atm_puts.iloc[0]['Skew']

        data_dict = {
            'Ticker': ticker,
            'Call Vol': first_row_volume_calls,
            'Call OI': first_row_oi_calls,
            'Call Skew': first_row_skew_calls,
            'Price': price,
            'Put Skew': first_row_skew_puts,
            'Put OI': first_row_oi_puts,
            'Put Vol': first_row_volume_puts,
        }

        table_data.append(data_dict)

    df = pd.DataFrame(table_data)
    table = tabulate(df, headers='keys', tablefmt='fancy')
    print(table)

tickers = ['SPX','AMD','NVDA']

# asyncio.run(main(tickers=tickers))