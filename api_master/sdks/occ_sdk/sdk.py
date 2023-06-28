import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import requests
import pandas as pd

from typing import Optional
from cfg import today_str
from .models import StockLoans, VolumeTotals
from datetime import datetime
class occSDK:
    def __init__(self):
        self.base_url = f"https://marketdata.theocc.com/mdapi/"



    def stock_loans(self, report_date: str = today_str, type: str = "daily") -> Optional[StockLoans]:
        """Retrieve stock loan data for a specific report date and type.

        Args:
            report_date (str): Report date in YYYY-MM-DD format. Defaults to today's date.
            type (str): Report type. Defaults to "daily".

        Returns:
            Optional[StockLoans]: Stock loan data for the specified report date and type, or None if data is not available.
        """
        r = requests.get(url=f"https://marketdata.theocc.com/mdapi/stock-loan?report_date={report_date}&report_type={type}").json()
        entity = r['entity']
        stockLoanResults = StockLoans(entity['stockLoanResults'] if entity.get('stockLoanResults') is not None else None)
        if stockLoanResults:
            return stockLoanResults
        else:
            return None

    def volume_totals(self) -> VolumeTotals:
        """Retrieve volume totals data.

        Returns:
            VolumeTotals: Volume totals data.
        """
        r = requests.get("https://marketdata.theocc.com/mdapi/volume-totals").json()
        entity = VolumeTotals(r['entity'])
        return entity