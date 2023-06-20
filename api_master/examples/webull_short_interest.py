import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
import pandas as pd


from sdks.webull_sdk.webull_sdk import AsyncWebullSDK

sdk = AsyncWebullSDK()


async def short_interest(ticker="AMC"):



    #short interest data - latest
    short_int_data = await sdk.get_short_interest(ticker)
    avg_volume = float(short_int_data.avg_volume[0]) #get avg volume trend
    short_interest = float(short_int_data.short_int[0])
    settlement_date = short_int_data.settlement[0]
    dtc = short_int_data.days_to_cover[0]


    print(f"Avg Vol: {avg_volume}")
    print(f"Shares Short: {short_interest:,}")
    print(f"Settlement Date: {settlement_date}")
    print(f"Days to Cover: {dtc}")


    #short interest data - historic


    data_dict = { 

        'Average Volume': short_int_data.avg_volume,
        'Short Interest': short_int_data.short_int,
        'Settlement Date': short_int_data.settlement,
        'Days to Cover': short_int_data.days_to_cover
    }


    df = pd.DataFrame(data_dict)

    filename= f'files/short_interest/{ticker}_short_interest.csv'

    df.to_csv(filename)
asyncio.run(short_interest(ticker="AMC"))