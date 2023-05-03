class WebullStockData:
    """A class representing stock data obtained from Webull.

    Attributes:
        web_name (str): The name of the stock.
        web_symb (str): The stock's symbol.
        web_exchange (str): The exchange code where the stock is traded.
        web_stock_close (float): The stock's closing price.
        last_earnings (str): The date of the stock's latest earnings report.
        web_stock_vol (int): The stock's trading volume.
        web_change_ratio (float): The stock's price change ratio.
        web_stock_open (float): The stock's opening price.
        web_stock_high (float): The stock's highest price.
        web_stock_low (float): The stock's lowest price.
        fifty_high (float): The stock's 52-week high price.
        avg_vol3m (float): The stock's average trading volume over the past 3 months.
        fifty_low (float): The stock's 52-week low price.
        avg_10d_vol (float): The stock's average trading volume over the past 10 days.
        outstanding_shares (int): The number of outstanding shares of the stock.
        total_shares (int): The total number of shares of the stock.
        estimated_earnings (str): The estimated date of the stock's next earnings report.
        web_vibrate_ratio (float): The stock's price fluctuation ratio.
    """
    def __init__(self, ticker):
        self.r = session.get(f"https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId={ticker}&includeSecu=1&includeQuote=1&more=1").json()


        self.web_name = self.r.get("name", None)
        self.web_symb = self.r.get("symbol", None)
        self.web_exchange = self.r.get("disExchangeCode", None)
        self.web_stock_close =self.r.get("close", None)
        self.last_earnings = self.r.get('latestEarningsDate',None)
        self.web_stock_vol =self.r.get("volume",None)
        self.web_change_ratio = self.r.get("changeRatio", None)
        self.web_stock_open =self.r.get("open",None)
        self.web_stock_high =self.r.get("high", None)
        self.web_stock_low =self.r.get("low", None)
        self.fifty_high = self.r.get("fiftyTwoWkHigh", None)
        self.avg_vol3m = self.r.get('avgVol3M')
        self.fifty_low = self.r.get("fiftyTwoWkLow", None)
        self.avg_10d_vol = self.r.get("avgVol10D", None)
        self.outstanding_shares = self.r.get('outstandingShares', None)
        self.total_shares = self.r.get('totalShares', None)
        try:
            self.estimated_earnings = self.r.get("nextEarningDay", None)
            self.web_vibrate_ratio = self.r.get('vibrateRatio', None)
        except KeyError:
            self.estimated_earnings = None
            self.web_vibrate_ratio = None

# Cache expiration time in seconds
class Analysis:
    def __init__(self, ticker):
        r = session.get(f"https://quotes-gw.webullfintech.com/api/information/securities/analysis?tickerId={ticker}").json()
        
        self.rating = r.get('rating', None)
        if self.rating:
            self.rating_suggestion = self.rating.get('ratingAnalysis', None)

            if 'ratingAnalysisTotals' in self.rating:
                self.rating_totals = self.rating['ratingAnalysisTotals']
            else:
                self.rating_totals = None

            rating_spread = self.rating.get('ratingSpread', None)
            if rating_spread:
                self.buy = rating_spread.get('buy', None)
                self.underperform = rating_spread.get('underPerform', None)
                self.strongbuy = rating_spread.get('strongBuy', None)
                self.sell = rating_spread.get('sell', None)
                self.hold = rating_spread.get('hold', None)
            else:
                self.buy = None
                self.underperform = None
                self.strongbuy = None
                self.sell = None
                self.hold = None
        else:
            self.rating_suggestion = None
            self.rating_totals = None
            self.buy = None
            self.underperform = None
            self.strongbuy = None
            self.sell = None
            self.hold = None



# Periodically remove expired entries from the cache

import requests
session = requests.session()


class WebullVolAnalysis:
    
    def __init__(self, ticker):
        
        if ticker is None:
            self.avePrice = None
            self.buyVolume = None
            self.sellVolume = None
            self.nVolume = None
            self.totalVolume = None
            return
        
        vol_anal_stock = f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/stat?count=10&tickerId={ticker}&type=0"
        response = session.get(vol_anal_stock).json()
        
        # Check if the response JSON contains the required keys
        if all(key in response for key in ('avePrice', 'buyVolume', 'sellVolume', 'nVolume', 'totalVolume')):
            self.avePrice = response.get('avePrice', None)
            self.buyVolume = response.get('buyVolume', None)
            self.sellVolume = response.get('sellVolume', None)
            self.nVolume = response.get('nVolume', None)
            self.totalVolume = response.get('totalVolume', None)
        else:
            # If the required keys are not present, set the attribute values to None
            self.avePrice = 0
            self.buyVolume = 0
            self.sellVolume = 0
            self.nVolume = 0
            self.totalVolume = 0