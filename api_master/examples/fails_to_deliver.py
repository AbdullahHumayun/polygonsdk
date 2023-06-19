import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from cfg import two_years_ago_str, today_str
from sdks.stocksera_sdk.sdk import StockeraSDK

sdk = StockeraSDK()


ftds = sdk.ftd(ticker="AAPL", from_date=two_years_ago_str, date_to=today_str)


ftd_amount = ftds.amount_ftd[0]
ftd_dollar_cost = ftds.dollar_cost[0]
ftd_date = ftds.date[0]
ftds_t35_settlement_date = ftds.t35_date[0]
ftd_ticker = ftds.ticker[0]#if no ticker is entered - this will be None


df = pd.DataFrame(vars(ftds))
df = df[::-1] #reverse the DF to get the latest values first
print(df)