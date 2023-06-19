import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from sdks.stocksera_sdk.sdk import StockeraSDK


sdk = StockeraSDK()


news = sdk.market_news()

#latest
news_date = news.Date[0]
news_section = news.Section[0]
news_source = news.Source[0]
news_title = news.Title[0]

df = pd.DataFrame(vars(news))

print(df)