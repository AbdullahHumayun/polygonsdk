import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sdks.stocksera_sdk.sdk import StockeraSDK
import pandas as pd


sdk = StockeraSDK()


jim = sdk.jim_cramer(stock="TSLA")

#get latest call
jims_call = jim.call[0]
jim_date = jim.date[0]
jim_price_target = jim.price[0]
jim_segment = jim.segment[0]
jim_ticker = jim.ticker[0]

df = pd.DataFrame(vars(jim))

print(df) #seems outdated