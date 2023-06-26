from api_master.sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
import asyncio
from tabulate import tabulate
from api_master.cfg import YOUR_API_KEY
from api_master.sdks.polygon_sdk.universal_snapshot import UniversalOptionSnapshot, UniversalSnapshot
poly = AsyncPolygonSDK(YOUR_API_KEY)
import aiohttp
from api_master.sdks.polygon_sdk.option_snapshot import OptionSnapshotData
import csv
from api_master.cfg import two_days_from_now_str, today_str, thirty_days_from_now_str, fifteen_days_from_now_str
import pandas as pd
from api_master.sdks.fmp_sdk.sdk import fmpSDK
from api_master.sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
import disnake
from api_master.sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK

opts = PolygonOptionsSDK(YOUR_API_KEY)

fmp = fmpSDK()
import tabulate
import asyncio
import aiohttp
import pandas as pd
from tabulate import tabulate
async def get_option_data(ticker, price):
    async with aiohttp.ClientSession() as session:
        if price is not None:
            lower_strike = round(price * 0.95)
            upper_strike = round(price * 1.05)
            initial_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte={fifteen_days_from_now_str}&limit=250&apiKey={YOUR_API_KEY}"
            print(initial_url)
            async with session.get(initial_url) as resp:
                data = await resp.json()
                results = data['results']
                option_data = OptionSnapshotData(results)
                symbols = str(option_data.option_symbol).replace("'","").replace(']','').replace('[','').replace(' ','')
                print(symbols)

                if option_data is not None:
                    df = pd.DataFrame(option_data.data_dict).dropna(how="any").sort_values('implied_volatility', ascending=True)
                    if not df.empty:
                        df = df.iloc[[0]]
                        for _, row in df.iterrows():
                            strike = row['strike_price']
                            symbol = row['underlying_ticker']
                            iv = round(float(row['implied_volatility'])*100,5)
                            underlying_price = row['underlying_price']
                            expiry = row['expiration_date']
                            expiry = expiry[5:]
                            skew = "🔥" if strike <= underlying_price else "🟢"
                            skew_metric = strike - underlying_price
                            if skew_metric < -5 or skew_metric > 5:
                                return [symbol, strike, underlying_price, expiry, iv, skew, skew_metric]


asyncio.run(get_option_data(ticker="GME", price=20))