import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from menus.pagination import AlertMenus

import disnake

from disnake.ext import commands
intents=disnake.Intents.all()
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK

from cfg import YOUR_API_KEY, YOUR_DISCORD_BOT_TOKEN


polygon = AsyncPolygonSDK(YOUR_API_KEY)
poly_options = PolygonOptionsSDK(YOUR_API_KEY)
webull = AsyncWebullSDK()


class PersistentViewBot(commands.Bot):
    def __init__(self, command_prefix, intents, ticker=None, embeds=None):
        self.ticker = ticker
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.persistent_views_added = False
        self.embeds = embeds

    async def on_ready(self):
        if not self.persistent_views_added:
            view = AlertMenus(self.embeds)
            self.add_view(view)
            self.persistent_views_added = True

        print(f"Logged in as {self.user} (ID: {self.user.id})")


   






bot = PersistentViewBot(command_prefix=">>", intents=intents)






from sdks.stocksera_sdk.sdk import StockeraSDK
from cfg import stocksera_key, today_str, thirty_days_from_now_str, five_days_ago_str
import stocksera
import pandas as pd
import disnake
from tabulate import tabulate
sdk = StockeraSDK()
from cfg import poly_options, YOUR_STOCKSERA_KEY
import aiohttp
import asyncio
client = stocksera.Client(YOUR_STOCKSERA_KEY)


















async def get_price_data(ticker: str):
    if ticker.startswith('SPX') or ticker.startswith("VIX"):
        ticker = ticker.replace(f"{ticker}", f"I:{ticker}")
        url = f"https://api.polygon.io/v3/snapshot?ticker.any_of={ticker}&apiKey=Hu_4qFYQSp53uz4sZRX1vmiGyNvTbvxz"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return
                data = await resp.json()
                results = data['results'] if 'results' in data else None
                value = results[0]['value']
                return value
    else:
        ticker = ticker
        url = f"https://api.polygon.io/v3/snapshot?ticker.any_of={ticker}&apiKey=Hu_4qFYQSp53uz4sZRX1vmiGyNvTbvxz"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status != 200:
                    return
                data = await resp.json()
                results = data['results'] if 'results' in data else None
                price = results[0]['session']['close']
                return price
            

async def get_near_the_money(ticker,lower_strike, upper_strike, today_str):

    url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte={today_str}&limit=250&apiKey={poly_options}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                return
            data = await resp.json()
            results = data['results'] if data['results'] is not None else None
            details = [i['details'] if i['details'] is not None else None for i in results]
            ticker = [i['ticker'] if i['ticker'] is not None else None for i in details]
            output = ','.join(ticker)  # holds all the option symbols
            return output


async def find_lowest_iv(output):
    async with aiohttp.ClientSession() as session:
        url = f"https://api.polygon.io/v3/snapshot?ticker.any_of={output}&apiKey={poly_options}"
        async with session.get(url) as filtered_resp:
            if filtered_resp.status != 200:
                print(f"Error")
            else:
                response = await filtered_resp.json()
                if response is None:
                    print(f"Bad output: {output}")
                filtered_results = response['results'] if 'results' in response else None
                if filtered_results is not None:

                    call_data = []
                    put_data = []

                    for result in filtered_results:
                        contract_type = result.get('details').get('contract_type')
                        if contract_type == 'call':
                            call_data.append(result)
                        elif contract_type == 'put':
                            put_data.append(result)
                        else:
                            continue

                    underlying_price = [i.get('underlying_asset').get('underlying_price') for i in filtered_results]
                    underlying_price = underlying_price[0]


                    call_symbols = [i.get('ticker', None) for i in call_data]
                    call_ivs = [i.get('implied_volatility', None) for i in call_data]
                    call_strikes = [i.get('details').get('strike_price', None) for i in call_data]
                    call_expiry = [i.get('details').get('expiration_date', None) for i in call_data]
                    call_name = [i.get('name', None) for i in call_data]
                 
                    
                    put_symbols = [i.get('ticker', None) for i in put_data]
                    put_ivs = [i.get('implied_volatility', None) for i in put_data]
                    put_strikes = [i.get('details').get('strike_price', None) for i in put_data]
                    put_expiry = [i.get('details').get('expiration_date', None) for i in put_data]        
                    put_name = [i.get('name', None) for i in put_data]
               

                    call_dict = { 
                        'Symbol': call_symbols,
                        'Name': call_name,
                        'Strike': call_strikes,
                        'Expiry': call_expiry,
                        'IV': call_ivs
                    }


                    put_dict = { 
                        'Symbol': put_symbols,
                        'Name': put_name,
                        'Strike': put_strikes,
                        'Expiry': put_expiry,
                        'IV': put_ivs
                    }


                    call_df = pd.DataFrame(call_dict).sort_values('IV').dropna(how="any")

                    put_df = pd.DataFrame(put_dict).sort_values('IV').dropna(how="any")

                    

                    current_lowest_iv_symbol_call = call_df['Symbol'].iloc[0]
                    current_lowest_iv_strike_call = call_df['Strike'].iloc[0]
                    current_lowest_iv_name_call = call_df['Name'].iloc[0]
                    current_lowest_iv_expiry_call = call_df['Expiry'].iloc[0]
                    current_lowest_iv_value_call = call_df['IV'].iloc[0]

                    print(current_lowest_iv_value_call)

                    current_lowest_iv_symbol_put = put_df['Symbol'].iloc[0]
                    current_lowest_iv_strike_put = put_df['Strike'].iloc[0]
                    current_lowest_iv_name_put = put_df['Name'].iloc[0]
                    current_lowest_iv_expiry_put = put_df['Expiry'].iloc[0]
                    current_lowest_iv_value_put = put_df['IV'].iloc[0]


                    final_dict = { 

                        'call_symbol': current_lowest_iv_symbol_call,
                        'put_symbol': current_lowest_iv_symbol_put,
                        'call_strike': current_lowest_iv_strike_call,
                        'put_strike': current_lowest_iv_strike_put,
                        'call_name': current_lowest_iv_name_call,
                        'put_name': current_lowest_iv_name_put,
                        'call_iv': current_lowest_iv_value_call,
                        'put_iv': current_lowest_iv_value_put,
                        'call_expiry': current_lowest_iv_expiry_call,
                        'put_expiry': current_lowest_iv_expiry_put
                    }


                    return final_dict
async def main():
    ticker = "GME"
    price = await get_price_data(ticker=ticker)

    lower_strike = 0.95 * price
    upper_stike = 1.05 * price

    atm_options = await get_near_the_money(ticker=ticker,lower_strike=lower_strike,upper_strike=upper_stike, today_str="2023-06-23")
    while True:
        low_iv_data = await find_lowest_iv(atm_options)

asyncio.run(main())














extensions = []
cogs_directory = os.path.join(os.path.dirname(__file__), 'cogs')

for filename in os.listdir(cogs_directory):
    if filename.endswith('.py'):
        extension_name = filename[:-3]  # Remove the .py extension
        extensions.append(f'cogs.{extension_name}')

for extension in extensions:
    bot.load_extension(f'bot.{extension}')

bot.run(YOUR_DISCORD_BOT_TOKEN)