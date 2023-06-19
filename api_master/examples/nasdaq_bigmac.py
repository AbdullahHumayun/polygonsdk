"""DOWNLOADS BIG-MAC DATA"""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))



from sdks.nasdaq_sdk.sdk import Nasdaq

nasdaq = Nasdaq()



nasdaqSDK = Nasdaq()

bm = nasdaqSDK.bigmac()
print(bm) #saves all dataframes for all countries to files/nasdaq/bigmac


