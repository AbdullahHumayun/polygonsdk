import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from cfg import today_str
from sdks.stocksera_sdk.sdk import StockeraSDK

sdk = StockeraSDK()

short_vol = sdk.short_volume(stock="GME", date_from="2020-12-30", to_date=today_str)


#get the latest values
short_date = short_vol.date[0]
short_percent = short_vol.percent_shorted[0]
short_exempt_vol = short_vol.short_exempt_vol[0]
total_volume = short_vol.total_vol[0]

#print the dataframe of all results

df = pd.DataFrame(vars(short_vol))
print(df)