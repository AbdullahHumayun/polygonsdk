import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from sdks.stocksera_sdk.sdk import StockeraSDK

sdk = StockeraSDK()


news_sentiment = sdk.news_sentiment(ticker="MSFT")

#latest
news_date = news_sentiment.Date[0]
news_sentiment_link = news_sentiment.Link[0]
news_sentiment_title = news_sentiment.Title[0]
news_sentiment_result = news_sentiment.Sentiment[0]

df = pd.DataFrame(vars(news_sentiment))

print(df)