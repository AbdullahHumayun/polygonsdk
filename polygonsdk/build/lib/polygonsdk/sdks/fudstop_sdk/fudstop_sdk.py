import sys
import os

# Get the directory path of the polygonsdkmaster package
package_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(package_dir)

from datetime import datetime
import asyncio
from .option_vol_totals import OptionVolumeTotals
import pandas as pd
import aiohttp
from cfg import YOUR_NASDAQ_KEY
from io import StringIO

import csv
class fudstopSDK:
    def __init__(self):
        self.nasdaq = YOUR_NASDAQ_KEY


    async def option_market_totals(self):
        async with aiohttp.ClientSession() as session:
            url=f"https://marketdata.theocc.com/mdapi/volume-totals"
            async with session.get(url) as resp:
                data = await resp.json()
                entity = data['entity']
                totals = OptionVolumeTotals(entity)
                return totals
            


        
    async def get_occ_open_interest(self, report_date):
        url = "https://marketdata.theocc.com/daily-open-interest"
        params = {"reportDate": report_date, "format": "csv", "action": "download"}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status == 200:
                    # Read the response as a pandas DataFrame
                    content = await response.content.read()
                    df = pd.read_csv(StringIO(content.decode('utf-8')), skiprows=2)
                    df = df.rename(columns={
                        "": "Date",
                        "Unnamed: 0": "Equity Calls",
                        "Calls": "Equity Puts",
                        "Puts": "Equity Total",
                        "Total": "Index Calls",
                        "Calls.1": "Index Puts",
                        "Puts.1": "Index Total",
                        "Total.1": "Debt Calls",
                        "Calls.2": "Debt Puts",
                        "Puts.2": "Debt Total",
                        "Total.2": "Futures Total",
                        "Total.3": "OCC Total",
                    })

                    return df
                else:
                    return None
                


    async def get_iv_percentile(self, symbol):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://data.nasdaq.com/api/v3/datasets/QOR/{symbol}/data.json?api_key={YOUR_NASDAQ_KEY}") as response:
                d = await response.json()
                dataset = d['dataset_data']
                data = dataset['data']
                column_names = dataset['column_names']
                Date = column_names[0]
                values = data[0]
                Date = values[0]
                ivper30 = round(values[8] * 100, ndigits=2)
                ivper60 = round(values[11]* 100, ndigits=2)
                ivper90 = round(values[14]* 100, ndigits=2)
                ivper360 = round(values[17]* 100, ndigits=2)
                self.ivperavg = round((ivper30 + ivper60 + ivper90 + ivper360) / 4, ndigits=4)

        return self.ivperavg
    
