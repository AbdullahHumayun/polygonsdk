"""DOWNLOADS INFLATION DATA"""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



from sdks.nasdaq_sdk.sdk import Nasdaq


nasdaq = Nasdaq()

sp500_data = nasdaq.sp500()
print(sp500_data)