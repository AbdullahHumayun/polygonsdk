import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sdks.stocksera_sdk.sdk import StockeraSDK
import pandas as pd


sdk = StockeraSDK()

#latest
jobless_claims = sdk.jobless_claims(days=200)
jobless_claims_date = jobless_claims.date[0]
jobless_claims_number = jobless_claims.number[0]
jobless_claims_percent_change = jobless_claims.percent_change[0]

df = pd.DataFrame(vars(jobless_claims))
df = df[::-1] #reverse order of DF to get latest value first
print(df)

