import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sdks.stocksera_sdk.sdk import StockeraSDK
import pandas as pd


sdk = StockeraSDK()


treasury = sdk.daily_treasury(days=100)

#latest
treasury_amount_change = treasury.amount_change[0]
treasury_close_balance = treasury.close_balance[0]
treasury_open_balance = treasury.open_balance[0]
treasury_date = treasury.date[0]
treasury_moving_avg = treasury.moving_avg[0]

treasury_df = pd.DataFrame(vars(treasury))
treasury_df = treasury_df[::-1] #reverse order of DF to get latest value first
print(treasury_df)




