"""DOWNLOADS ECONOMIC INDICATOR  DATA"""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



from sdks.nasdaq_sdk.sdk import Nasdaq


nasdaq = Nasdaq()

economic_indicators = nasdaq.economic_indicators()
print(economic_indicators)