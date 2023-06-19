import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import requests
import pandas as pd

from cfg import today_str
from .models import StockLoans, VolumeTotals
from datetime import datetime
class occSDK:
    def __init__(self):
        self.base_url = f"https://marketdata.theocc.com/mdapi/"



    def stock_loans(self, report_date: str = today_str, type: str="daily"):
        r = requests.get(url=f"https://marketdata.theocc.com/mdapi/stock-loan?report_date={report_date}&report_type={type}").json()
        entity = r['entity'] if r['entity'] is not None else None
        stockLoanResults = StockLoans(entity['stockLoanResults'] if entity['stockLoanResults'] is not None else None)
        if stockLoanResults:
            return stockLoanResults
        else:
            return None
        

    def volume_totals(self):
        r = requests.get("https://marketdata.theocc.com/mdapi/volume-totals").json()
        entity = VolumeTotals(r['entity'])

        return entity
    

