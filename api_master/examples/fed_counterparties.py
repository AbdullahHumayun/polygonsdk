import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from cfg import today_str
from sdks.fed_newyork_sdk.sdk import FedNewyork
import pandas as pd



sdk = FedNewyork()


sdk = FedNewyork()


x = sdk.get_fed_counterparties()

print(x)

#output:

# ['Banco de Mexico', 'Bank of Canada', 
# 'Bank of England', 'Bank of Japan', 
# 'Bank of Korea', 'Danmarks Nationalbank', 
# 'European Central Bank', 'Monetary Authority of Singapore', 
# 'Norges Bank', 'Reserve Bank of Australia', 'Swiss National Bank']