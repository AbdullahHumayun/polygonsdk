import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from sdks.stocksera_sdk.sdk import StockeraSDK

sdk = StockeraSDK()

stocktwits = sdk.stocktwits(stock="GME")

#get first values
date_updated = stocktwits.date_updated[0]
stocktwits_rank = stocktwits.rank[0]
stocktwits_watchlists = stocktwits.watchlist[0]

df = pd.DataFrame(vars(stocktwits))
df = df[::-1] #reverse DF to get latest values first

print(df)