import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
import pandas as pd

from cfg import YOUR_API_KEY
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK

polyoptions = PolygonOptionsSDK(YOUR_API_KEY)
poly = AsyncPolygonSDK(YOUR_API_KEY)

async def get_trades():
    """
    Retrieve option trades for a specific option symbol and save them to a CSV file.

    This function retrieves option trades using the PolygonOptionsSDK and saves the trades
    to a CSV file for further analysis.

    Ensure that you have set the appropriate values for the following variables before running the function:
    - underlying_symbol: The underlying symbol of the option.
    - expiration_date: The expiration date of the option.
    - option_type: The type of the option (C for Call, P for Put).
    - strike_price: The strike price of the option.
    """

    underlying_symbol = "F"
    expiration_date = "2023-05-19"
    option_type = "C"
    strike_price = 11.5

    # Generate the option symbol
    option_symbol = await polyoptions.generate_option_symbol(underlying_symbol=underlying_symbol,
                                                             expiration_date=expiration_date,
                                                             option_type=option_type,
                                                             strike_price=strike_price)
    print(option_symbol)  # Symbol used for further analysis below

    # Retrieve option trades
    opt_trades = await polyoptions.get_option_trades(symbol=option_symbol, limit=100)

    # Extract relevant information from option trades
    condition_name = [i.conditions for i in opt_trades]
    price = [i.price for i in opt_trades]
    size = [i.size for i in opt_trades]
    sip_timestamp = [i.sip_timestamp for i in opt_trades]
    exchange = [i.exchange for i in opt_trades]

    # Create a DataFrame from the option trades
    df = pd.DataFrame({
        'Condition': condition_name,
        'Price': price,
        'Size': size,
        'Sip Timestamp': sip_timestamp,
        'Exchange': exchange
    })

    # Save the DataFrame to a CSV file
    csv_filename = f'files/options/trades/{underlying_symbol}{option_type}{strike_price}_trades.csv'
    df.to_csv(csv_filename)

   

asyncio.run(get_trades())