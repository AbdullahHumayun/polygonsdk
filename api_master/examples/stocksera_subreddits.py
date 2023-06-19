import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from sdks.stocksera_sdk.sdk import StockeraSDK

sdk = StockeraSDK()

subreddits = sdk.subreddit(stock="GME")

#get the first values
active_users = subreddits.Active[0]
subreddit_date = subreddits.Date[0]
percent_active = subreddits.percActive[0]
subreddit_growth = subreddits.percGrowth[0]
subreddit_influence_price_change = subreddits.percPriceChange[0]

df = pd.DataFrame(vars(subreddits))
df = df[::-1] #reverse the DF to get the latest values first
print(df)