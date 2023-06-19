import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from sdks.stocksera_sdk.sdk import StockeraSDK

sdk = StockeraSDK()

sec_filings = sdk.sec_fillings(stock="AAPL")

#get the latest values first
filing_description = sec_filings.Description[0]
filing_url = sec_filings.filing_url[0]
filing = sec_filings.Filling[0]
filing_date = sec_filings.FillingDate[0]
filing_url = sec_filings.report_url[0]



df = pd.DataFrame(vars(sec_filings))

print(df) #seems to be out-dated
