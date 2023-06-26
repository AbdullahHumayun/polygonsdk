import re
import pytz
from typing import List
from datetime import datetime, timedelta
from polygon.exceptions import BadResponse
from cfg import YOUR_API_KEY
import aiohttp
import asyncio
import pandas as pd
from urllib.parse import urlencode
now = datetime.now()
def format_timestamp(timestamp: datetime) -> str:
    return timestamp.strftime("%Y/%m/%d")


def human_readable(string):
    try:
        match = re.search(r'(\w{1,5})(\d{2})(\d{2})(\d{2})([CP])(\d+)', string) #looks for the options symbol in O: format
        underlying_symbol, year, month, day, call_put, strike_price = match.groups()
    except TypeError:
        underlying_symbol = f"AMC"
        year = "23"
        month = "02"
        day = "17"
        call_put = "CALL"
        strike_price = "380000"
    
    expiry_date = month + '/' + day + '/' + '20' + year
    if call_put == 'C':
        call_put = 'Call'
    else:
        call_put = 'Put'
    strike_price = '${:.2f}'.format(float(strike_price)/1000)
    return "{} {} {} Expiring {}".format(underlying_symbol, strike_price, call_put, expiry_date)


def get_checkmark(k, v, thresholds):
    if k == 'score':
        if v is not None and v >= thresholds['score']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'current_ratio':
        if v is not None and v >= thresholds['current_ratio']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'quick_ratio':
        if v is not None and v >= thresholds['quick_ratio']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'debt_to_equity_ratio':
        if v is not None and v <= thresholds['debt_to_equity_ratio']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'return_on_assets':
        if v is not None and v >= thresholds['return_on_assets']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'return_on_equity':
        if v is not None and v >= thresholds['return_on_equity']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'gross_profit_margin':
        if v is not None and v >= thresholds['gross_profit_margin']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'operating_margin':
        if v is not None and v >= thresholds['operating_margin']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'net_profit_margin':
        if v is not None and v >= thresholds['net_profit_margin']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'dividend_payout_ratio':
        if v is not None and v >= thresholds['dividend_payout_ratio'][0] and v <= thresholds['dividend_payout_ratio'][1]:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'revenue_growth':
        if v is not None and v >= thresholds['revenue_growth']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'total_asset_turnover':
        if v is not None and v >= thresholds['total_asset_turnover']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'inventory_turnover':
        if v is not None and v >= thresholds['inventory_turnover']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'days_sales_outstanding':
        if v is not None and v <= thresholds['days_sales_outstanding']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'debt_ratio':
        if v is not None and v <= thresholds['debt_ratio']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'interest_coverage':
        if v is not None and v >= thresholds['interest_coverage']:
            return ":white_check_mark:"
        else:
            return ":x:"
    else:
        return ":x:"


def validate_date_format(date_string):
    date_pattern = re.compile(r"\d{4}-\d{2}-\d{2}")
    return bool(date_pattern.fullmatch(date_string))


def convert_to_date(num_days: int):
    """Outputs a date string in the format:
    >>> YYYY-MM-DD e.g. 2023-04-21

    Args:
    
    >>> num days: integer - the numbers of days 
    forward or backwards

    """
    
    time = now + timedelta(days=num_days)
    date_string = time.strftime("%Y-%m-%d")
    return date_string

def format_date(input_str):
    # Parse the input string as a datetime object
    input_datetime = datetime.fromisoformat(input_str.replace("Z", "+00:00"))

    # Convert the datetime object to Eastern Time
    utc_timezone = pytz.timezone("UTC")
    eastern_timezone = pytz.timezone("US/Eastern")
    input_datetime = input_datetime.astimezone(utc_timezone)
    eastern_datetime = input_datetime.astimezone(eastern_timezone)

    # Format the output string
    output_str = eastern_datetime.strftime("%Y-%m-%d at %I:%M%p %Z")
    return output_str



def get_date_string(days):
    date = datetime.now() + timedelta(days=days)
    return date.strftime('%Y-%m-%d')


async def extract_underlying_symbol(symb):



    try:
        match = re.search(r'O:(\w{1,5})(\d{2})(\d{2})(\d{2})([CP])(\d+)', symb)
        underlying_symbol, year, month, day, call_put, strike_price = match.groups() 
    except BadResponse:
        return "N/A"
    except AttributeError:
        return "M/A"
    
    return underlying_symbol


async def fetch_url(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            data = await response.json()
            return data
        else:
            print(f"Error: {response.status}")
            return None

# Fetch all URLs
async def paginate():
    all_results = []
    next_urls = [f"https://api.polygon.io/v3/snapshot?type=options&order=asc&ticker.lt=SPY&ticker.gt=I:SPX&limit=250&apiKey={YOUR_API_KEY}"]
    async with aiohttp.ClientSession() as session:
        while next_urls:
            tasks = [fetch_url(session, url) for url in next_urls]
            responses = await asyncio.gather(*tasks, return_exceptions=True)

            next_urls = []
            for response in responses:
                if isinstance(response, Exception):
                    print(f"Error: {response}")
                else:
                    if "results" in response:
                        print(response['results'][0]['ticker'])
                        all_results.extend(response["results"])
                        next_url = response.get("next_url")
                        if next_url:
                            next_url += f'&{urlencode({"apiKey": YOUR_API_KEY})}'
                            next_urls.append(next_url)
    df = pd.DataFrame(all_results)
    df.to_csv('testing_it.csv')
    return all_results









# import aiohttp
# async def main():
#     ticker_symbols = ['AAPL', 'GOOGL', 'MSFT']  # Assuming you have a list of ticker symbols

#     async with aiohttp.ClientSession() as session:
#         price_tasks = [poly.get_stock_price(ticker) for ticker in tickers]
#         prices = await asyncio.gather(*price_tasks)
#         ticker_prices = dict(zip(tickers, prices))  # Assuming no None prices

#         # Now get option data concurrently
#         option_data_tasks = [get_option_data(ticker, ticker_prices[ticker], session) for ticker in tickers]
#         results = await asyncio.gather(*option_data_tasks)
#         # Filter out None results and add valid results to data_list
#         data_list = [result for result in results if result is not None]

#         data_list = sorted(data_list, key=lambda x: x[6], reverse=True)
#         print(data_list)

# if __name__ == "__main__":
#     asyncio.run(main())