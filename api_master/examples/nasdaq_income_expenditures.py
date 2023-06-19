"""DOWNLOADS INCOME EXPENDITURE DATA"""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



from sdks.nasdaq_sdk.sdk import Nasdaq


nasdaq = Nasdaq()

income_expenditures = nasdaq.income_expenditures()
print(income_expenditures)