import requests
from tabulate import tabulate
import asyncio
import aiohttp
import pandas as pd

from cfg import YOUR_API_KEY as API_KEY, today_str

class OptionSnapshotData:


    def __init__(self, data):

        self.implied_volatility = [i['implied_volatility'] if 'implied_volatility' in i else None for i in data]

        self.open_interest  = [i['open_interest'] if 'open_interest' in i else None for i in data]
        self.break_even_price = [i['break_even_price'] if 'break_even_price' in i else None for i in data]

        day = [i['day'] if i['day'] is not None else None for i in data]
        self.day_close = [i['close'] if 'close' in i else None for i in day]
        self.day_high= [i['high'] if 'high' in i else None for i in day]
        self.last_updated = [i['last_updated'] if 'last_updated' in i else None for i in day]
        self.day_low= [i['low'] if 'low' in i else None for i in day]
        self.day_open= [i['open'] if 'open' in i else None for i in day]
        self.day_change_percent = [i['change_percent'] if 'day_change_percent' in i else None for i in day]
        self.day_change = [i['change'] if 'change' in i else None for i in day]
        self.previous_close= [i['previous_close'] if 'previous_close' in i else None for i in day]
        self.day_volume= [i['volume'] if 'volume' in i else None for i in day]
        self.day_vwap = [i['vwap'] if 'vwap' in i else None for i in day]
        

        details  = [i['details'] if 'details' in i else None for i in data]
        self.contract_type = [i['contract_type'] if 'contract_type' in i else None for i in details]
        self.exercise_style= [i['exercise_style'] if 'exercise_style' in i else None for i in details]
        self.expiration_date = [i['expiration_date'] if 'expiration_date' in i else None for i in details]
        self.shares_per_contract = [i['shares_per_contract'] if 'shares_per_contract' in i else None for i in details]
        self.strike_price= [i['strike_price'] if 'strike_price' in i else None for i in details]
        self.option_symbol = [i['option_symbol'] if 'option_symbol' in i else None for i in details]

        greeks = [i['greeks'] if 'details' in i else None for i in data]
        self.delta = [i['delta'] if 'delta' in i else None for i in greeks]
        self.gamma  = [i['gamma'] if 'gamma' in i else None for i in greeks]
        self.theta  = [i['theta'] if 'theta' in i else None for i in greeks]
        self.vega  = [i['vega'] if 'vega' in i else None for i in greeks]
        

        lastquote = [i['last_quote'] if i['last_quote'] is not None else None for i in data]
        self.ask = [i['ask'] if 'ask' in i else None for i in lastquote]
        self.ask_size= [i['ask_size'] if 'ask_size' in i else None for i in lastquote]
        self.bid = [i['bid'] if 'bid' in i else None for i in lastquote]
        self.bid_size = [i['bid_size'] if 'bid_size' in i else None for i in lastquote]
        self.quote_last_updated = [i['last_updated'] if 'last_updated' in i else None for i in lastquote]
        self.midpoint= [i['midpoint'] if 'midpoint' in i else None for i in lastquote]

        lasttrade = [i['last_trade'] if 'last_trade' in i else None for i in data]
        self.conditions = [i['conditions'] if 'conditions' in i else None for i in lasttrade]
        self.exchange = [i['exchange'] if 'exchange' in i else None for i in lasttrade]
        self.price  = [i['price'] if 'price' in i else None for i in lasttrade]
        self.sip_timestamp  = [i['sip_timestamp'] if 'sip_timestamp' in i else None for i in lasttrade]
        self.size  = [i['size'] if 'size' in i else None for i in lasttrade]

        underlying  = [i['underlying_asset'] if i['underlying_asset'] is not None else None for i in data]
        self.change_to_break_even = [i['change_to_break_even'] if 'change_to_break_even' in i else None for i in underlying]
        self.underlying_last_updated = [i['last_updated'] if 'last_updated' in i else None for i in underlying]
        self.underlying_price  = [i['price'] if 'price' in i else None for i in underlying]
        self.underlying_ticker  = [i['ticker'] if 'ticker' in i else None for i in underlying]



    


async def get_price(session, ticker):
    if ticker.startswith('SPX'):
        ticker = ticker.replace(f"{ticker}", f"I:{ticker}")
        url = f"https://api.polygon.io/v3/snapshot?ticker.any_of={ticker}&apiKey={API_KEY}"
        async with session.get(url) as resp:
            data = await resp.json()
            results = data['results'] if data['results'] is not None else None
            if results is None:
                print(f"Error - results from price request.")
            value = results[0]['value']
            return value
    
    elif ticker.startswith('VIX'):
        ticker = ticker.replace(f"{ticker}", f"I:{ticker}")
        url = f"https://api.polygon.io/v3/snapshot?ticker.any_of={ticker}&apiKey={API_KEY}"
        async with session.get(url) as resp:
            data = await resp.json()
            results = data['results'] if data['results'] is not None else None
            if results is None:
                print(f"Error - results from price request.")
            value = results[0]['value']
            return value
    else:
        url = f"https://api.polygon.io/v3/snapshot?ticker.any_of={ticker}&apiKey={API_KEY}"
        async with session.get(url) as resp:
            data = await resp.json()
            results = data['results'] if data['results'] is not None else None
            if results is None:
                print(f"Error - results from price request.")
            value = results[0]['session']['close']
            return value

async def fetch_prices(tickers):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for ticker in tickers:
            tasks.append(get_price(session, ticker))
        return await asyncio.gather(*tasks)

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


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def get_near_the_money_options2(session,ticker: str, lower_strike, upper_strike):
    initial_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte=2023-07-21&limit=250&apiKey={API_KEY}"

    async with aiohttp.ClientSession() as session:
        atm_options = await fetch(session, initial_url)
        results = atm_options['results']

        while 'next_url' in atm_options:
            next_url = atm_options['next_url']
            atm_options = await fetch(session, next_url + f"&apiKey={API_KEY}")
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
    