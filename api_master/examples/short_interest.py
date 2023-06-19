import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from sdks.stocksera_sdk.sdk import StockeraSDK

sdk = StockeraSDK()

short_int = sdk.short_interest() #view tickers with the highest short interest % of float


#access the first values
average_volume = short_int.AverageVolume[0]
short_interest_date = short_int.Date[0]
days_to_cover = short_int.DaysToCover[0]
short_percent_of_float = short_int.FloatShort[0]
short_interest_rank = short_int.Rank[0]
short_interest = short_int.ShortInterest[0]


#print the entire dataframe

df = pd.DataFrame(vars(short_int))
df = df[::1] #reverse the DF order so we get the latest values first

print(df) ##THIS DATA SEEMS TO BE OUT-DATED##