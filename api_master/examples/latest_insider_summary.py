import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from sdks.stocksera_sdk.sdk import StockeraSDK

sdk = StockeraSDK()


latest_insider_summary = sdk.latest_insider_summary()


#get latest values
dollar_amount = latest_insider_summary.amount[0]
market_cap = latest_insider_summary.market_cap[0]
percent_of_market_cap_transacted = latest_insider_summary.percent_of_market_cap[0]
ticker_traded = latest_insider_summary.ticker[0]


df = pd.DataFrame(vars(latest_insider_summary))

print(df)