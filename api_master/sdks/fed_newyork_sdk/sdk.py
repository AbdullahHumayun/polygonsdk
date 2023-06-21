
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import requests
from cfg import today_str

import json
import pandas as pd
from models import AuctionResult, FXSwaps, TimeSeries, AsOfDates, TimeSeriesData, SecuredReferenceRates, UnsecuredReferenceRates

session = requests.session()



class FedNewyork:
    def __init__(self):
        self.base_url = "https://markets.newyorkfed.org/api/"


    def agency_mbs_search(self, start_date="2023-01-01", end_date=today_str):
        """Search for AMBS operations out of the Federal Reserve of New York"""

        r = session.get(self.base_url + f"ambs/all/results/summary/search.json?startDate={start_date}&endDate={today_str}").json()
        ambs = r['ambs']
        auctions = ambs['auctions']
        if auctions is not None:
            data = AuctionResult(auctions)
            return data
        else:
            return None
    

    def agency_mbs_count(self, number=10):
        """Return AMBS transactions by count."""
        r = session.get(self.base_url + f"ambs/all/results/details/last/{number}.json").json()
        ambs = r['ambs']
        auctions = ambs['auctions']
        if auctions is not None:
            data = AuctionResult(auctions)
            return data
        else:
            return None
        

    def liquidity_swaps_latest(self):
        """Get the latest central bank liquidity swap data."""
        r = session.get(self.base_url + f"fxs/all/latest.json").json()
        fxSwaps = r['fxSwaps']
        operations = fxSwaps['operations']
        if operations is not None:
            data = FXSwaps(operations)
            return data
        else:
            return "No recent data found."
        
    def liquidity_swaps_count(self, number=50):
        """Get the latest central bank liquidity swap data."""
        r = session.get(self.base_url + f"fxs/usdollar/last/{number}.json").json()
        fxSwaps = r['fxSwaps']
        operations = fxSwaps['operations']
        if operations is not None:
            data = FXSwaps(operations)
            return data
        else:
            return "No recent data found."
        

    def liquidity_swaps_search(self, start_date = "2023-01-01", end_date = today_str, type="trade", counterparties='japan,europe'):
        """Search for liquidity swaps between a custom date range.
        
        Arguments:
          >>> start_date: a date in YYYY-MM-DD format to start from
          >>> end_date: a date in YYYY-MM-DD to end on. defaults to today.
          >>> type: type of information to return. trade or maturity.
          >>> counterparties: list of counterparties. default: europe, japan
        """

        

        r = session.get(self.base_url + f"fxs/all/search.json?startDate={start_date}&endDate={end_date}&dateType={type}&counterparties={counterparties}").json()
        fxSwaps = r['fxSwaps']
        operations = fxSwaps['operations']
        if operations is not None:
            data = FXSwaps(operations)
            return data
        else:
            return None
        

    def get_fed_counterparties(self):
        """Returns the current counterparties to the Federal Reserve."""
        r = session.get(self.base_url + "fxs/list/counterparties.json").json()
        fxSwaps = r['fxSwaps']
        counterparties = fxSwaps['counterparties']
        if counterparties is not None:
            return counterparties


    def get_as_of_dates(self):
        """Returns a list of dates to query the FED API with."""
        r = session.get("https://markets.newyorkfed.org/api/pd/list/asof.json").json()
        pdd = r['pd']
        as_of_dates = pdd['asofdates']
        if as_of_dates is not None:
            data = AsOfDates(as_of_dates)
            return data
        else:
            return None
        
    def get_timeseries(self):
            """Returns the timeseries data to query the FED API"""

            r = requests.get("https://markets.newyorkfed.org/api/pd/list/timeseries.json").json()
            pdd = r['pd']
            timeseries = pdd['timeseries']
            if timeseries is not None:
                data = TimeSeries(timeseries)

                
                return data
            else:
                return None


    def get_timeseries_data(self, timeseries):
        """Use timeseries codes to query the FED API."""
        
        timeseries_data = requests.get(f"https://markets.newyorkfed.org/api/pd/get/{timeseries}.json").json()
        pdd = timeseries_data['pd']
        timeseries = pdd['timeseries']
        if timeseries is not None:
            data = TimeSeriesData(timeseries)
            return data
        else:
            return None
    
    def secured_rates(self):
        """Returns all unsecured central bank rates globally.
        
        Arguments:
        >>> rate_type: secured or unsecured
        """
        r = session.get(f"https://markets.newyorkfed.org/api/rates/secured/all/latest.json").json()
        refrates = r['refRates']

        if refrates is not None:
            data = SecuredReferenceRates(refrates)
            return data
        else:
            return None
        
    def unsecured_rates(self):
        """Returns all unsecured central bank rates globally.
        
        Arguments:
        >>> rate_type: secured or unsecured
        """
        r = session.get(f"https://markets.newyorkfed.org/api/rates/unsecured/all/latest.json").json()
        refrates = r['refRates']

        if refrates is not None:
            data = UnsecuredReferenceRates(refrates)
            return data
        else:
            return None


