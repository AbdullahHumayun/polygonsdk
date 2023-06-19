import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sdks.stocksera_sdk.sdk import StockeraSDK
import pandas as pd


sdk = StockeraSDK()


ipos = sdk.IPO_calendar()

# Accessing the latest IPO
date = ipos.date[0]
exchange = ipos.exchange[0]
expected_price = ipos.expected_price[0]
mkt_cap = ipos.mkt_cap[0]
name = ipos.name[0]
number_shares = ipos.number_shares[0]
status = ipos.status[0]
symbol = ipos.symbol[0]

# Print attribute values
print("Date:", date)
print("Exchange:", exchange)
print("Expected Price:", expected_price)
print("Market Cap:", mkt_cap)
print("Name:", name)
print("Number of Shares:", number_shares)
print("Status:", status)
print("Symbol:", symbol)


df = pd.DataFrame(vars(ipos))

print(df)