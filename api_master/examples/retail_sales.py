import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sdks.stocksera_sdk.sdk import StockeraSDK
import pandas as pd


sdk = StockeraSDK()


retail_sales = sdk.retail_sales()


amount = retail_sales.amount[0]
retail_sales_date = retail_sales.date[0]
monthly_avg_cases = retail_sales.monthly_avg_cases[0]
retail_sales_percent_change = retail_sales.percent_change[0]


df = pd.DataFrame(vars(retail_sales))
df = df[::-1] #reverse DF to get latest values first
print(df)

