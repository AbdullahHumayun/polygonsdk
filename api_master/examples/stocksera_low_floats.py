import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from sdks.stocksera_sdk.sdk import StockeraSDK

sdk = StockeraSDK()


low_floats = sdk.low_float()

# Accessing the first attributes
company_name = low_floats.company_name[0]
exchange = low_floats.exchange[0]
floating_shares = low_floats.floating_shares[0]
industry = low_floats.industry[0]
market_cap = low_floats.market_cap[0]
one_day_change = low_floats.one_day_change[0]
outstanding_shares = low_floats.outstanding_shares[0]
previous_close = low_floats.previous_close[0]
Rank = low_floats.Rank[0]
ticker = low_floats.ticker[0]

# Print latest attribute values
print("Company Name:", company_name)
print("Exchange:", exchange)
print("Floating Shares:", floating_shares)
print("Industry:", industry)
print("Market Cap:", market_cap)
print("One-Day Change:", one_day_change)
print("Outstanding Shares:", outstanding_shares)
print("Previous Close:", previous_close)
print("Rank:", Rank)
print("Ticker:", ticker)


#print entire dataframe

df = pd.DataFrame(vars(low_floats))

print(df)