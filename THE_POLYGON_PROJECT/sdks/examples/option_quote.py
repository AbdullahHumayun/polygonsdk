import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from datetime import datetime
import pandas as pd

from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from sdks.helpers.helpers import get_date_string

from cfg import YOUR_API_KEY

now = datetime.now()
sdk = PolygonOptionsSDK(YOUR_API_KEY)

async def main():
    """
    Main function to retrieve option quotes and save them to a CSV file.

    The date range for fetching option quotes can be adjusted by modifying the value of `num_days_ago`.
    A negative value represents days in the past, and a positive value represents days in the future.
    For example, `num_days_ago = -50` will fetch option quotes from 50 days ago until today.
    """

    # Specify the option details
    underlying_symbol = "SPY"
    expiration_date = "2023-05-15"
    option_type = 'C'
    strike_price = '417'

    # Generate the option symbol
    option_symbol = await sdk.generate_option_symbol(underlying_symbol, expiration_date, option_type, strike_price)

    # Specify the date range for fetching option quotes
    num_days_ago = get_date_string(-50)
    today_str = datetime.today().strftime('%Y-%m-%d')

    option_quote = await sdk.get_option_quote(option_symbol=option_symbol, order="desc", limit=50000, timestamp_lte=today_str, timestamp_gte=num_days_ago)

    # Create a DataFrame from the option quotes
    df = pd.DataFrame(option_quote.to_dict())


    csv_filename = f'files/options/quotes/{option_symbol[2:]}_{num_days_ago.replace("-", "")}.csv'
    df.to_csv(csv_filename)

asyncio.run(main())