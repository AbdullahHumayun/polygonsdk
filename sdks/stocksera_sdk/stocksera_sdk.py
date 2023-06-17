import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import stocksera

from cfg import YOUR_STOCKSERA_KEY
from cfg import today_str
from cfg import thirty_days_from_now_str


from .borrowed import BorrowedShares
from .treasury import TreausryBalance
from .earnings import Earnings
import pandas as pd


symbol = "NVDA"

class StockseraSDK:
    def __init__(self):
        self.client = stocksera.Client(YOUR_STOCKSERA_KEY)

        

    def borrowed_shares(self, symbol):
        borrowed_shares_data = BorrowedShares(self.client.borrowed_shares(symbol))

        return borrowed_shares_data
    

    def treasury_balance(self, days: int = 100):

        treasury_balance_data = TreausryBalance(self.client.daily_treasury(days))

        return treasury_balance_data
    

    def upcoming_earnings(self, from_date=today_str, to_date=thirty_days_from_now_str):

        upcoming_earnings_data = Earnings(self.client.earnings_calendar(date_from=today_str,date_to=thirty_days_from_now_str))
        return upcoming_earnings_data



