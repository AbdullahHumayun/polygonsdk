from typing import Dict, Any
import pandas as pd
import asyncio
import requests
import aiohttp
from cfg import YOUR_API_KEY as API_KEY, today_str, seven_days_from_now_str
import json
class OptionSnapshotData:
    def __init__(self, data):
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                print(f"JSONDecodeError: Unable to parse JSON data: {data}")
                return

        for i in data:
            self.implied_volatility = i.get("implied_volatility", None)
            self.open_interest = i.get("open_interest")
            self.break_even_price = i.get("break_even_price")

            day = i.get('day')
            self.day_close = day.get("close")
            self.day_high = day.get("high")
            self.last_updated = day.get("last_updated")
            self.day_low = day.get("low")
            self.day_open = day.get("open")
            self.day_change_percent = day.get('change_percent')
            self.day_change = day.get('change')
            self.previous_close = day.get("previous_close")
            self.day_volume = day.get("volume")
            self.day_vwap = day.get("vwap")

            details = i.get('details')
            self.contract_type = details.get("contract_type")
            self.exercise_style = details.get("exercise_style")
            self.expiration_date = details.get("expiration_date")
            self.shares_per_contract = details.get("shares_per_contract")
            self.strike_price = details.get("strike_price")
            self.option_symbol = details.get("option_symbol")

            greeks = i.get('greeks')
            self.delta = greeks.get("delta")
            self.gamma = greeks.get("gamma")
            self.theta = greeks.get("theta")
            self.vega = greeks.get("vega")

            lastquote = i.get('last_quote')
            self.ask = lastquote.get("ask")
            self.ask_size = lastquote.get("ask_size")
            self.bid = lastquote.get("bid")
            self.bid_size = lastquote.get("bid_size")
            self.quote_last_updated = lastquote.get("last_updated")
            self.midpoint = lastquote.get("midpoint")

            lasttrade = i.get('last_trade')
            self.conditions = lasttrade.get("conditions")
            self.exchange = lasttrade.get("exchange")
            self.price = lasttrade.get("price")
            self.sip_timestamp = lasttrade.get("sip_timestamp")
            self.size = lasttrade.get("size")

            underlying = i.get('underlying_asset')
            self.change_to_break_even = underlying.get("change_to_break_even")
            self.underlying_last_updated = underlying.get("last_updated")
            self.underlying_price = underlying.get("price")
            self.underlying_ticker = underlying.get("ticker")
            self.data_dict = {
            "implied_volatility": [i.get("implied_volatility", None) for i in data],
            "open_interest": [i.get("open_interest") for i in data],
            "break_even_price": [i.get("break_even_price") for i in data],
            "day_close": [i.get('day').get("close") for i in data],
            "day_high": [i.get('day').get("high") for i in data],
            "last_updated": [i.get('day').get("last_updated") for i in data],
            "day_low": [i.get('day').get("low") for i in data],
            "day_open": [i.get('day').get("open") for i in data],
            "day_change_percent": [i.get('day').get("change_percent") for i in data],
            "day_change": [i.get('day').get("change") for i in data],
            "previous_close": [i.get('day').get("previous_close") for i in data],
            "day_volume": [i.get('day').get("volume") for i in data],
            "day_vwap": [i.get('day').get("vwap") for i in data],
            "contract_type": [i.get('details').get("contract_type") for i in data],
            "exercise_style": [i.get('details').get("exercise_style") for i in data],
            "expiration_date": [i.get('details').get("expiration_date") for i in data],
            "shares_per_contract": [i.get('details').get("shares_per_contract") for i in data],
            "strike_price": [i.get('details').get("strike_price") for i in data],
            "option_symbol": [i.get('details').get("ticker") for i in data],
            "delta": [i.get('greeks').get("delta") for i in data],
            "gamma": [i.get('greeks').get("gamma") for i in data],
            "theta": [i.get('greeks').get("theta") for i in data],
            "vega": [i.get('greeks').get("vega") for i in data],
            "ask": [i.get('last_quote').get("ask") for i in data],
            "ask_size": [i.get('last_quote').get("ask_size") for i in data],
            "bid": [i.get('last_quote').get("bid") for i in data],
            "bid_size": [i.get('last_quote').get("bid_size") for i in data],
            "quote_last_updated": [i.get('last_quote').get("last_updated") for i in data],
            "midpoint": [i.get('last_quote').get("midpoint") for i in data],
            "conditions": [i.get('last_trade').get("conditions") for i in data],
            "exchange": [i.get('last_trade').get("exchange") for i in data],
            "price": [i.get('last_trade').get("price") for i in data],
            "sip_timestamp": [i.get('last_trade').get("sip_timestamp") for i in data],
            "size": [i.get('last_trade').get("size") for i in data],
            "change_to_break_even": [i.get('underlying_asset').get("change_to_break_even") for i in data],
            "underlying_last_updated": [i.get('underlying_asset').get("last_updated") for i in data],
            "underlying_price": [i.get('underlying_asset').get("price") for i in data],
            "underlying_ticker": [i.get('underlying_asset').get("ticker") for i in data]
        }



    @classmethod
    def to_dict(self):
        return {slot: getattr(self, slot) for slot in self.__slots__}
    


async def get_near_the_money_options(ticker: str, lower_strike, upper_strike):
    if ticker.startswith('SPX'):
        ticker = ticker.replace(f"{ticker}", f"I:{ticker}")
        initial_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte=2023-06-30&limit=250&apiKey={API_KEY}"

        ticker = ticker.replace(f"{ticker}", f"I:{ticker}")
        atm_options = requests.get(initial_url).json()
        results = atm_options['results']
        ticker = [i.get('details').get('ticker') for i in results]

        while 'next_url' in atm_options:
            next_url = atm_options['next_url']
            r = requests.get(next_url + f"&apiKey={API_KEY}")
            atm_options = r.json()
            results.extend(atm_options['results'])

        # Now you have all the results in the `results` list
        # You can process them in chunks of 250 if needed
        chunk_size = 250
        chunks = []
        for i in range(0, len(results), chunk_size):
            chunk = results[i:i+chunk_size]
            symbol = [i.get('details').get('ticker') for i in chunk]
            chunks.append(symbol)

        # Construct URLs for each chunk
        base_url = "https://api.polygon.io/v3/snapshot?ticker.any_of={}&apiKey={}"
        urls = []
        for chunk in chunks:
            # Flatten the chunk list
            
            # Join the tickers into a comma-separated string
            ticker_string = ",".join(chunk)
            
            # Construct the URL
            url = base_url.format(ticker_string, API_KEY)
            
            urls.append(url)

        return urls



async def get_near_the_money_options2(ticker: str, lower_strike, upper_strike):
    initial_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte=2023-07-21&limit=250&apiKey={API_KEY}"

    async with aiohttp.ClientSession() as session:
        async with session.get(initial_url) as resp:
            atm_options = await resp.json()
            results = atm_options['results']

            while 'next_url' in atm_options:
                next_url = atm_options['next_url']
                async with session.get(next_url + f"&apiKey={API_KEY}") as resp2:
                    results = await resp2.json()

                    results.extend(atm_options['results'])

        data = OptionSnapshotData(results)
        df = pd.DataFrame(vars(data))
        df['expiration_date'] = pd.to_datetime(df['expiration_date']).dt.strftime("%m-%d")

        # Sort by nearest expiry and lowest implied volatility
        df.sort_values(['expiration_date', 'implied_volatility'], ascending=[True, True], inplace=True)

        lowest_iv_row = df.iloc[0]

        return lowest_iv_row




async def find_lowest_iv(output):
    async with aiohttp.ClientSession() as session:
        url = f"{output}&apiKey={API_KEY}"
        final_dicts_call = []
        final_dicts_put = []
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
                        'IV': call_ivs,

                    }

                    put_dict = {
                        'Symbol': put_symbols,
                        'Name': put_name,
                        'Strike': put_strikes,
                        'Expiry': put_expiry,
                        'IV': put_ivs,

                    }

                    call_df = pd.DataFrame(call_dict).sort_values('IV').dropna(how="any")
                    put_df = pd.DataFrame(put_dict).sort_values('IV').dropna(how="any")
                    call_df.to_csv('iv_monitor_calls.csv')
                    put_df.to_csv('iv_monitor_puts.csv')
                    def get_lowest_iv(group):
                        return group.sort_values('IV').iloc[0]

                    grouped_call_df = call_df.groupby('Expiry').apply(get_lowest_iv)
                    grouped_put_df = put_df.groupby('Expiry').apply(get_lowest_iv)
                    #print(grouped_call_df)
        
                    #print(grouped_put_df)
                    for index, row in grouped_call_df.iterrows():
                        current_dict = {
                            'symbol': row['Symbol'],
                            'name': row['Name'],
                            'strike': row['Strike'],
                            'expiry': index,  # level 0 index is 'Expiry'
                            'iv': row['IV'],

                        }
                        final_dicts_call.append(current_dict)

                
                    for index, row in grouped_put_df.iterrows():
                        current_dict = {
                            'symbol': row['Symbol'],
                            'name': row['Name'],
                            'strike': row['Strike'],
                            'expiry': index,  # level 0 index is 'Expiry'
                            'iv': row['IV'],

                        }
                        final_dicts_put.append(current_dict)
                        
        return final_dicts_call, final_dicts_put 
    


    def to_dict(self):
        return {slot: getattr(self, slot) for slot in self.__slots__}
    

    