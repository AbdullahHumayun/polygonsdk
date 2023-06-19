import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from sdks.stocksera_sdk.sdk import StockeraSDK

sdk = StockeraSDK()


repo = sdk.reverse_repo(days=200)

#latest
repo_amount = repo.amount[0]
repo_average = repo.average[0]
repo_date = repo.date[0]
repo_moving_average = repo.moving_average[0]
num_parties = repo.num_parties[0]

df = pd.DataFrame(vars(repo))
df = df[::-1] #reverse order of DF to get latest value first
print(df)
