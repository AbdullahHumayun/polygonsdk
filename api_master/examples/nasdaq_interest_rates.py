"""DOWNLOADS INCOME EXPENDITURE DATA"""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



from sdks.nasdaq_sdk.sdk import Nasdaq


nasdaq = Nasdaq()

interest_rates = nasdaq.interest_rates()
print(interest_rates)