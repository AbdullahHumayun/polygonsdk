from sdks.stocksera_sdk.models import ShortVolume,ShortInterest, Senate
from sdks.stocksera_sdk.sdk import StockeraSDK, YOUR_STOCKSERA_KEY

import stocksera
client = stocksera.Client(YOUR_STOCKSERA_KEY)
stockseraSDK = StockeraSDK()


import pandas as pd



wsb_options = stockseraSDK.wsb_options(days=100)


#get the latest values
wsb_calls = wsb_options.calls[0]
wsb_puts = wsb_options.puts[0]
wsb_ticker = wsb_options.ticker[0]
wsb_ratio = wsb_options.ratio[0]

df = pd.DataFrame(vars(wsb_options))

print(df)