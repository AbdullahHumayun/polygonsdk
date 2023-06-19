"""DOWNLOADS INFLATION DATA"""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sdks.occ_sdk.sdk import occSDK
import pandas as pd


x = occSDK()


datas = x.stock_loans(report_date="2023-06-12", type="daily")


#get the latest values
business_date = datas.businessDate[0]
bilateral_loan_count = datas.newBilateralLoanCount[0]
new_market_loans = datas.newMarketLoanCount[0]
total_bilateral_loan_volume = datas.totalBilateralLoanVal[0]
total_market_loan_volume = datas.totalMarketLoanVal[0]


df = pd.DataFrame(vars(datas)) # get all values

df.to_csv('files/occ/stock_loans.csv')