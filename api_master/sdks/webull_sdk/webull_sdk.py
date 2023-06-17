from pathlib import Path
import sys

# Get the absolute path of the current file
current_file_path = Path(__file__).resolve()

# Get the absolute path of the 'cfg' module
cfg_module_path = current_file_path.parent.parent / 'cfg'

# Add the module path to sys.path
sys.path.append(str(cfg_module_path))



import aiohttp
from .derivative_query import QueryDerivatives
from typing import List, Optional
from aiohttp.client_exceptions import ContentTypeError
from .capitalflow import CapitalFlow
import aiohttp
from dateutil import parser
from .etf_holdings import ETFHoldings
from .calendar import EarningsCalendar
from .cost_distribution import CostDistribution
from .events import Event
from .top_gainers import Ticker
import pandas as pd
from .webull_data import Analysis, WebullStockData, WebullVolAnalysis
from .top_gainers import GainersData
from .etf_finder import ETFCommodity
from .top_options import BelongTicker, Values, Derivative, TickerValues
from typing import Dict,Union
from datetime import datetime, timedelta, timezone
from .financial_statement import FinancialStatement, CashFlow, BalanceSheet
from .news import NewsItem
from .shortinterest import ShortInterest
from api_master.cfg import today_str, thirty_days_ago_str
from .institutional_holdings import InstitutionHolding
now = datetime.now()
ninety_days_from_now = now + timedelta(days=90)
ninety_days = ninety_days_from_now.strftime("%Y-%m-%d")
seen_article_urls = set()
thresholds = {
    'current_ratio': 1.5,
    'quick_ratio': 1,
    'debt_to_equity_ratio': 2,
    'return_on_assets': 0.05,
    'return_on_equity': 0.15,
    'gross_profit_margin': 0.4,
    'operating_margin': 0.1,
    'net_profit_margin': 0.05,
    'dividend_payout_ratio': (0.3, 0.8),
    'revenue_growth': 0.1,
    'total_asset_turnover': 0.5,
    'inventory_turnover': 5,
    'days_sales_outstanding': 45,
    'debt_ratio': 0.6,
    'interest_coverage': 3,
    'price_to_earnings_ratio': 15,
    'price_to_sales_ratio': 2.5,
    'price_to_book_value': 3,
    'eps_growth': 0.1,
    'free_cash_flow_margin': 0.05,
    'score': 14,
}
class AsyncWebullSDK:
    def __init__(self, tickerId=None, symbol=None):
        self.tickerId = tickerId
        self._ticker = None
        self._values = None
        self._earning_release_id = None
        self._ticker_id = None
        self._region_id = None
        self._qualifier = None
        self._eps = None
        self._eps_estimate = None
        self._year = None
        self._quarter = None
        self._release_date = None
        self._is_live = None
        self._last_release_date = None
        self._publish_status = None
        self.tickerId = tickerId
        self.symbol = symbol
        self.base_url = "https://quotes-gw.webullfintech.com/api/"

    async def get_top_gainers_data(self, type: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://quotes-gw.webullfintech.com/api/bgw/market/topGainers?regionId=6&rankType={type}&pageIndex=1&pageSize=350") as response:
                data = await response.json()
                print(data)
                datas = data['data']
                top_gainers = [d['ticker'] for d in datas]
                results = GainersData(top_gainers)
                
            return results    


    async def fifty_two_high_and_lows(self):
        """Returns tickers near low/high or new low/high on the year."""
        rank_types = ['nearLow', 'nearHigh', 'newLow', 'newHigh']
        tickers = []
        for rank_type in rank_types:
            url=f"https://quotes-gw.webullfintech.com/api/wlas/ranking/52weeks?regionId=6&rankType={rank_type}&pageIndex=1&pageSize=350"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    datas = await response.json()
                    data = datas['data']
                    tickers += [i['ticker'] if 'ticker' in i else None for i in data]
        return Ticker(tickers)
    async def top_active_stocks(self):
        """Get the most active tickers by relative volume, turnover, range, and volume"""
        rank_types = ['rvol10d', 'volume', 'turnover', 'range']
        tickers = []
        for rank_type in rank_types:
            url = f"https://quotes-gw.webullfintech.com/api/wlas/ranking/topActive?regionId=6&rankType={rank_type}&pageIndex=1&pageSize=350"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    datas = await response.json()
                    data = datas['data']
                    tickers += [i['ticker'] if 'ticker' in i else None for i in data]
        return Ticker(tickers)
    async def top_options_chains(self):
        rank_types = ['volume', 'position', 'turnover', 'posIncrease', 'posDecrease', 'impVol']
        tickers = []
        for rank_type in rank_types:
            url = f"https://quotes-gw.webullfintech.com/api/wlas/option/rank/list?regionId=6&rankType={rank_type}&pageIndex=1&pageSize=350"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    response = await response.json()
                    data = response.get('data', None)
                    derivatives = [Derivative.from_dict(data.get("derivative", {})) for data in data]
                    values = [Values.from_dict(data.get("values", {})) for data in data]
                    belongticker = [BelongTicker.from_dict(data.get("belongTicker", {})) for data in data]

                    self.change = [i.change for i in belongticker]
                    self.changeRatio = [i.changeRatio for i in belongticker]
                    self.close = [i.close for i in belongticker]
                    self.symbol = [i.symbol for i in derivatives]
                    self.fiftyTwoWkHigh = [i.fiftyTwoWkHigh for i in belongticker]
                    self.fiftyTwoWkLow = [i.fiftyTwoWkLow for i in belongticker]
                    self.high = [i.high for i in belongticker]
                    self.low = [i.low for i in belongticker]
                    self.name = [i.name for i in belongticker]
                    self.marketValue = [i.marketValue for i in belongticker]
                    self.vibrateRatio = [i.vibrateRatio for i in belongticker]
                    self.volume = [i.volume for i in belongticker]
                    self.turnoverRate = [i.turnoverRate for i in belongticker]
                    self.disSymbol = [i.disSymbol for i in belongticker]
                    self.option_change = [i.change for i in derivatives]
                    self.option_change_ratio = [i.changeRatio for i in derivatives]
                    self.option_close = [i.close for i in derivatives]
                    self.strike = [i.strikePrice for i in derivatives]
                    self.direction = [i.direction for i in derivatives]
                    self.option_symbol = [i.symbol for i in derivatives]
                    self.underlying_symbol = [i.unSymbol for i in derivatives]
                    self.cycle = [i.cycle for i in derivatives]
                    self.expiry = [i.expireDate for i in derivatives]
                    self.belong_ticker_id = [i.belongTickerId for i in derivatives]
                    self.attributes_dict = {
                        "change": self.change,
                        "changeRatio": self.changeRatio,
                        "close": self.close,
                        "symbol": self.symbol,
                        "fiftyTwoWkHigh": self.fiftyTwoWkHigh,
                        "fiftyTwoWkLow": self.fiftyTwoWkLow,
                        "high": self.high,
                        "low": self.low,
                        "name": self.name,
                        "marketValue": self.marketValue,
                        "vibrateRatio": self.vibrateRatio,
                        "volume": self.volume,
                        "turnoverRate": self.turnoverRate,
                        "disSymbol": self.disSymbol,
                        "option_change": self.option_change,
                        "option_change_ratio": self.option_change_ratio,
                        "option_close": self.option_close,
                        "strike": self.strike,
                        "direction": self.direction,
                        "option_symbol": self.option_symbol,
                        "underlying_symbol": self.underlying_symbol,
                        "cycle": self.cycle,
                        "expiry": self.expiry,
                        "belong_ticker_id": self.belong_ticker_id}

                    self.df = pd.DataFrame(self.attributes_dict)

        return self.df, derivatives
                

    async def top_options_tickers(self, rank_type):
        """Rank Types: totalVolume / totalPosition / """
        url = f"https://quotes-gw.webullfintech.com/api/wlas/option/rank/list?regionId=6&rankType={rank_type}&pageIndex=1&pageSize=350"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response = await response.json()
                data = response.get('data', None)
                values = [TickerValues.from_dict(data.get("values", {})) for data in data]
                belongticker = [BelongTicker.from_dict(data.get("ticker", {})) for data in data]


                

                return values, belongticker, values

    async def fetch_ticker_id(self, keyword):
        url = f"{self.base_url}search/pc/tickers?keyword={keyword}&regionId=6&pageIndex=1&pageSize=1"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                r = await response.json()
                data = r.get('data', None)
                if data is not None:
                    try:
                        self.tickerId = data[0]['tickerId']
                        self.symbol = data[0]['symbol']
                    except IndexError:
                        pass
                else:
                    pass
                return self.tickerId, self.symbol
            

    async def cost_distribution(self, ticker, start_date=thirty_days_ago_str, end_date=today_str):
        async with aiohttp.ClientSession() as session:
            tickerid, _ = await self.fetch_ticker_id(ticker)
            url = f"https://quotes-gw.webullfintech.com/api/quotes/chip/query?tickerId={tickerid}&startDate={start_date}&endDate={end_date}"
            headers = {'Content-Type': 'application/json'}
            async with session.get(url,headers=headers) as response:
                try:
                    response_data = await response.json()
                    print(await response.text())
                    data = response_data['data']
                    cost_distribution = [CostDistribution(item) for item in data]
                    return cost_distribution
                except ContentTypeError as e:
                    print(f"Error: {e}\nResponse text: {await response.text()}")
                    return None



    async def economic_events(self,from_date=today_str, to_date=ninety_days_from_now):
        url = f"https://chartevents-reuters.tradingview.com/events?minImportance=1&from={from_date}&to={ninety_days}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response_data = await response.json()
                events_data = response_data['result']

                events = [Event(item) for item in events_data]

                data = {
                    "Actual": [event.actual if event.actual is not None else None for event in events],
                    "Comment": [event.comment for event in events],
                    "Country": [event.country for event in events],
                    "Currency": [event.currency for event in events],
                    "Date": [event.date for event in events],
                    "Time": [event.time for event in events],
                    "Forecast": [event.forecast if event.forecast is not None else None for event in events],
                    "ID": [event.id for event in events],
                    "Importance": [event.importance for event in events],
                    "Indicator": [event.indicator for event in events],
                    "Link": [event.link for event in events],
                    "Period": [event.period for event in events],
                    "Previous": [event.previous if event.previous is not None else None for event in events],
                    "Scale": [event.scale for event in events],
                    "Source": [event.source for event in events],
                    "Title": [event.title for event in events],
                    "Unit": [event.unit for event in events],
                }
                df = pd.DataFrame(data)
                return df


    async def get_etf_categories(self, type: str) -> Optional[List[ETFCommodity]]:
            """
            Retrieves a list of ETFs from the following types:
            >>> commodity
            >>> industry
            >>> index
            >>> other

            Args:
                type (str): The category type of ETFCommodity instances to retrieve. Must be one of "index", "industry", "commodity", or "other".

            Returns:
                Optional[List[ETFCommodity]]: A list of ETFCommodity instances containing ETF or commodity data. Returns None if an error occurs while fetching the data.
            """
            url = f"https://quotes-gw.webullfintech.com/api/wlas/etfinder/pcFinder?topNum=5&finderId=wlas.etfinder.{type}&nbboLevel=false"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()

                        tabs = data.get('tabs')
                        ticker_tuples = [t.get('tickerTupleList') for t in tabs]
                        if data:
                            etfs = []
                            for i, ticker_list in enumerate(ticker_tuples):
                                for ticker_data in ticker_list:
                                    etf = ETFCommodity(tabs[i], ticker_data)
                                    etfs.append(etf)      
                            return etfs
                    else:
                        print(f"Error fetching data: {response.status}")
                        return None

    async def get_earnings_calendar(self, date_str):
        url = f"{self.base_url}bgw/explore/calendar/earnings?regionId=6&pageIndex=1&pageSize=50&startDate={date_str}"
        async with aiohttp.ClientSession() as session:
           
            async with session.get(url) as response:
                data = await response.json()
                results = data['data']

                earnings_calendars = [EarningsCalendar(result) for result in results]
                return earnings_calendars
            

    async def get_balancesheet(self, ticker: str) -> List[BalanceSheet]:
        """
        Retrieves a list of BalanceSheet instances for a given stock ticker.

        Args:
            ticker (str): The ticker symbol of the stock to retrieve balance sheet statements for.

        Returns:
            List[BalanceSheet]: A list of BalanceSheet instances containing balance sheet statement data.
        """
        async with aiohttp.ClientSession() as session:
            tickerid, _ = await self.fetch_ticker_id(ticker)
            
            async with session.get(f"https://quotes-gw.webullfintech.com/api/information/financial/balancesheet?tickerId={tickerid}&type=102&fiscalPeriod=1,2,3,4&limit=50") as response:
                
                if response.status == 200:
                    r = await response.json()
                    try:
                        data = r['data']
                        balance_sheets = [BalanceSheet(statement) for statement in data]
                        return balance_sheets
                    except KeyError:
                        pass



    async def get_financial_statement(self, ticker: str) -> List[FinancialStatement]:

        """
        Retrieves a list of FinancialStatement instances for a given stock ticker.

        Args:
            ticker (str): The ticker symbol of the stock to retrieve financial statements for.

        Returns:
            List[FinancialStatement]: A list of FinancialStatement instances containing financial statement data.
        """
        async with aiohttp.ClientSession() as session:
            tickerid, _ = await self.fetch_ticker_id(ticker)
            async with session.get(f"https://quotes-gw.webullfintech.com/api/information/financial/incomestatement?tickerId={tickerid}&type=102&fiscalPeriod=1,2,3,4&limit=11") as resp:
                if resp.status == 200:
                    r = await resp.json()
                    try:
                        data = r['data']
                        financial_statements = [FinancialStatement(statement) for statement in data]
                        return financial_statements
                    except KeyError:
                        pass

    async def get_cash_flow(self, ticker):
        """
        Retrieves a list of CashFlow instances for a given stock ticker.

        Args:
            ticker (str): The ticker symbol of the stock to retrieve cash flow statements for.

        Returns:
            List[CashFlow]: A list of CashFlow instances containing cash flow statement data.
        """
        async with aiohttp.ClientSession() as session:
            tickerid, _ = await self.fetch_ticker_id(ticker)
            async with session.get(f"https://quotes-gw.webullfintech.com/api/information/financial/cashflow?tickerId={tickerid}&type=102&fiscalPeriod=1,2,3,4&limit=11") as resp:
                if resp.status == 200:
                    r = await resp.json()
                    try:
                        data = r['data']
                        financial_statements = [CashFlow(statement) for statement in data]
                        return financial_statements
                    except KeyError:
                        pass


    async def get_short_interest(self, ticker):
        """
        Get the short interest data for a given ticker ID.

        Args:
            ticker_id (int): The unique identifier for the stock ticker.

        Returns:
            ShortInterest: An instance of the ShortInterest class containing short interest data in the form of a List, or None if an error occurs.
        """
        async with aiohttp.ClientSession() as session:
            tickerid, _ = await self.fetch_ticker_id(ticker)
            async with session.get(f"https://quotes-gw.webullfintech.com/api/information/brief/shortInterest?tickerId={tickerid}") as resp:
                if resp.status != 200:
                    return None
                data = await resp.json()
                short_interest = ShortInterest(data)
                return short_interest


    async def get_institutional_holdings(self, ticker):
        """
        Retrieves institutional holdings for a given ticker.

        Args:
            ticker (str): The ticker symbol to retrieve holdings for.

        Returns:
            InstitutionHolding: An object representing the institutional holdings for the given ticker.
        """
        async with aiohttp.ClientSession() as session:
            tickerid, symbol = await self.fetch_ticker_id(ticker)
            async with session.get(f"https://quotes-gw.webullfintech.com/api/information/stock/getInstitutionalHolding?tickerId={tickerid}") as resp:
                if resp.status == 200:
                    r = await resp.json()
                    try:
                        holdings = InstitutionHolding(r)
                        return holdings
                    except KeyError:
                        print("Error parsing response")
                        return None
                    

        

    async def capital_flow(self, ticker):
        async with aiohttp.ClientSession() as session:
            tickerid, _ = await self.fetch_ticker_id(ticker)
            async with session.get(f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/ticker?tickerId={tickerid}&showHis=true") as response:
                r = await response.json()
                latest = r['latest']
                if latest is not None:
                    item = item = latest['item']
                    if item is not None:
                        return CapitalFlow(item)





    async def get_webull_stock_data(self, ticker):
        """Fetches and returns a `WebullStockData` object containing stock data for the specified ticker symbol.

        Args:
            ticker (str): The ticker symbol of the stock to fetch data for.

        Returns:
            A `WebullStockData` object containing the following attributes:
            >>> web_name (str): The name of the stock.
            >>> web_symb (str): The ticker symbol of the stock.
            >>> web_exchange (str): The stock exchange the stock is traded on.
            >>> web_stock_close (float): The most recent closing price of the stock.
            >>> last_earnings (str): The date of the company's last earnings report.
            >>> web_stock_vol (float): The current volume of shares traded.
            >>> web_change_ratio (float): The change in price of the stock as a percentage.
            >>> web_stock_open (float): The opening price of the stock for the current trading day.
            >>> web_stock_high (float): The highest price the stock has reached during the current trading day.
            >>> web_stock_low (float): The lowest price the stock has reached during the current trading day.
            >>> fifty_high (float): The highest price the stock has reached in the past 52 weeks.
            >>> avg_vol3m (float): The average volume of shares traded over the past 3 months.
            >>> fifty_low (float): The lowest price the stock has reached in the past 52 weeks.
            >>> avg_10d_vol (float): The average volume of shares traded over the past 10 days.
            >>> outstanding_shares (float): The number of outstanding shares of the stock.
            >>> total_shares (float): The total number of shares of the stock.
            >>> estimated_earnings (str): The date of the company's next earnings report (if available).
            >>> web_vibrate_ratio (float): The volatility of the stock.
        """

        tickerid, _ = await self.fetch_ticker_id(ticker)
        webull_stock_data = WebullStockData(tickerid)


        return webull_stock_data



    async def get_analysis_data(self, ticker):
        try:
            async with aiohttp.ClientSession() as session:
                tickerid, _ = await self.fetch_ticker_id(ticker)
                async with session.get(f"https://quotes-gw.webullfintech.com/api/information/securities/analysis?tickerId={tickerid}") as resp:
                    if resp.status == 200:
                        r = await resp.json()
                    else:
                        return None

                    # Store the fetched analysis data in the cache
                    analysis_data = Analysis(tickerid)

                    return analysis_data

        except Exception as e:
            print(f"Error getting analysis data for ticker {ticker}: {e}")
            return None
        

    async def get_webull_vol_analysis_data(self, ticker):
            tickerid, _ = await self.fetch_ticker_id(ticker)
            # If the ticker WebullVolAnalysis data is not in the cache or has expired, fetch it
            webull_vol_analysis_data = WebullVolAnalysis(tickerid)
            
        # Store the fetched WebullVolAnalysis data in the cache


            return webull_vol_analysis_data


    async def calculate_score(self,
        capital_expenditures,
        cash_from_financing_activities,
        cash_from_investing_activities,
        cash_from_operating_activities,
        net_change_in_cash,
        net_income,
        total_cash_dividends_paid
    ):
        score = 0
        
        if cash_from_operating_activities is not None and float(cash_from_operating_activities) > 0:
            score += 2

        if net_income is not None and cash_from_operating_activities is not None and float(cash_from_operating_activities) / float(net_income) > 1.2:
            score += 1

        if capital_expenditures is not None and cash_from_operating_activities is not None and float(cash_from_operating_activities) > 0 and float(capital_expenditures) / float(cash_from_operating_activities) < 0.5:
            score += 1

        if net_change_in_cash is not None and float(net_change_in_cash) > 0:
            score += 1

        if total_cash_dividends_paid is not None and net_income is not None and float(total_cash_dividends_paid) / float(net_income) < 0.5:
            score += 1

        if cash_from_financing_activities is not None and net_income is not None and float(net_income) != 0 and float(cash_from_financing_activities) / float(net_income) < 0:
            score += 1

        return {
            "capital_expenditures": capital_expenditures,
            "cash_from_financing_activities": cash_from_financing_activities,
            "cash_from_investing_activities": cash_from_investing_activities,
            "cash_from_operating_activities": cash_from_operating_activities,
            "net_change_in_cash": net_change_in_cash,
            "net_income": net_income,
            "total_cash_dividends_paid": total_cash_dividends_paid,
            "score": score
        }
    async def financial_score(self, ticker):
        score = 0
        ticker_id, _ = await self.fetch_ticker_id(ticker)

        marketprice = await self.get_webull_stock_data(ticker_id)
        market_price = marketprice.web_stock_close
        balance_sheet = await self.get_balancesheet(ticker_id)
        cashflow = await self.get_cash_flow(ticker_id)
        fin_statement = await self.get_financial_statement(ticker_id)

        # Calculate financial ratios and metrics
        ratios = await self.calculate_ratios(balance_sheet, fin_statement, cashflow, market_price)
        if ratios is not None:
        # Scoring based on the calculated ratios and metrics
            if ratios['current_ratio'] is not None and ratios['current_ratio'] > 2:
                score += 1
            if ratios['quick_ratio'] is not None and ratios['quick_ratio'] > 1:
                score += 1
            if ratios['debt_to_equity_ratio'] is not None and ratios['debt_to_equity_ratio'] < 0.5:
                score += 2
            if ratios['return_on_assets'] is not None and ratios['return_on_assets'] > 0.05:
                score += 2
            if ratios['return_on_equity'] is not None and ratios['return_on_equity'] > 0.15:
                score += 3
            if ratios['gross_profit_margin'] is not None and ratios['gross_profit_margin'] > 0.4:
                score += 2
            if ratios['operating_margin'] is not None and ratios['operating_margin'] > 0.1:
                score += 2
            if ratios['net_profit_margin'] is not None and ratios['net_profit_margin'] > 0.05:
                score += 3
            if ratios['dividend_payout_ratio'] is not None and 0.3 <= ratios['dividend_payout_ratio'] <= 0.6:
                score += 1
            if ratios['revenue_growth'] is not None and ratios['revenue_growth'] > 0.1:
                score += 2
            if ratios['total_asset_turnover'] is not None and ratios['total_asset_turnover'] > 0.7:
                score += 1
            if ratios['inventory_turnover'] is not None and ratios['inventory_turnover'] > 6:
                score += 1
            if ratios['days_sales_outstanding'] is not None and ratios['days_sales_outstanding'] < 45:
                score += 1
            if ratios['debt_ratio'] is not None and ratios['debt_ratio'] < 0.5:
                score += 2
            if ratios['interest_coverage'] is not None and ratios['interest_coverage'] > 3:
                score += 1
            for k, v in ratios.items():
                score_threshold = thresholds.get('score')
                if k == 'score':
                    if score_threshold is None:
                        check = ":white_check_mark:"
                    elif isinstance(score_threshold, tuple) and isinstance(v, float) and score_threshold[0] <= v <= score_threshold[1]:
                        check = ":white_check_mark:"
                    elif isinstance(score_threshold, (int, float)) and isinstance(v, float) and float(v) >= score_threshold:
                        check = ":white_check_mark:"
                    else:
                        check = ":x:"
                else:
                    check = ":white_check_mark:" if isinstance(v, float) and thresholds.get(k) and isinstance(thresholds[k], tuple) and thresholds[k][0] <= v <= thresholds[k][1] or isinstance(thresholds.get(k), (int, float)) and (isinstance(v, float) and thresholds.get(k) is not None and float(v) >= thresholds[k] or not isinstance(v, float) and thresholds.get(k, 0) == 0) else ":x:"

                return {**ratios, 'score': score}

    async def calculate_ratios(self, balance_sheet, fin_statement, cashflow, market_price):
        ratios = {}
        
        # Check if fin_statement and balance_sheet are not empty
        if fin_statement and balance_sheet:
            if balance_sheet and balance_sheet[0].totalCurrentAssets is not None and balance_sheet[0].totalCurrentLiabilities is not None and float(balance_sheet[0].totalCurrentLiabilities) > 0 and float(balance_sheet[0].totalCurrentAssets) > 0:
                current_ratio = float(balance_sheet[0].totalCurrentAssets) / float(balance_sheet[0].totalCurrentLiabilities)
            else:
                current_ratio = None

            if balance_sheet[0].totalCurrentAssets is not None and balance_sheet[0].totalInventory is not None and balance_sheet[0].totalCurrentLiabilities is not None:
                quick_ratio = (float(balance_sheet[0].totalCurrentAssets) - float(balance_sheet[0].totalInventory)) / float(balance_sheet[0].totalCurrentLiabilities)
            else:
                quick_ratio = None

            if balance_sheet[0].totalDebt is not None and balance_sheet[0].totalEquity is not None:
                debt_to_equity_ratio = float(balance_sheet[0].totalDebt) / float(balance_sheet[0].totalEquity)
            else:
                debt_to_equity_ratio = None

            if fin_statement[0].net_income is not None and balance_sheet[0].totalAssets is not None:
                if float(balance_sheet[0].totalAssets) != 0:
                    return_on_assets = float(fin_statement[0].net_income) / float(balance_sheet[0].totalAssets)
                else:
                    return_on_assets = None  # or any appropriate value to represent the case when total assets are zero
            else:
                return_on_assets = None

            if fin_statement[0].net_income is not None and balance_sheet[0].totalEquity is not None:
                return_on_equity = float(fin_statement[0].net_income) / float(balance_sheet[0].totalEquity)
            else:
                return_on_equity = None

            if fin_statement[0].total_revenue is not None and fin_statement[0].cost_of_revenue_total is not None and float(fin_statement[0].total_revenue) > 0:
                gross_profit_margin = (float(fin_statement[0].total_revenue) - float(fin_statement[0].cost_of_revenue_total)) / float(fin_statement[0].total_revenue)
            else:
                gross_profit_margin = None

            if fin_statement[0].total_revenue is not None and float(fin_statement[0].total_revenue) > 0:
                if fin_statement[0].operating_income is not None:
                    operating_margin = float(fin_statement[0].operating_income) / float(fin_statement[0].total_revenue)
                else:
                    operating_margin = None
            else:
                operating_margin = None

            if fin_statement[0].total_revenue is not None and fin_statement[0].net_income is not None and float(fin_statement[0].total_revenue) > 0:
                net_profit_margin = float(fin_statement[0].net_income) / float(fin_statement[0].total_revenue)
            else:
                net_profit_margin = None

            if cashflow and cashflow[0].total_cash_dividends_paid is not None and fin_statement[0].net_income is not None and float(fin_statement[0].net_income) > 0:
                dividend_payout_ratio = float(cashflow[0].total_cash_dividends_paid) / float(fin_statement[0].net_income)
            else:
                dividend_payout_ratio = None


            try:
                if cashflow is not None and cashflow[0].total_cash_dividends_paid is not None and fin_statement[0].net_income is not None and float(fin_statement[0].net_income) > 0:
                    dividend_payout_ratio = float(cashflow[0].total_cash_dividends_paid) / float(fin_statement[0].net_income)
                else:
                    dividend_payout_ratio = None
            except IndexError:
                # Handle the index error here
                dividend_payout_ratio = None

            # Revenue Growth - You will need data from the previous year's financial statement

            if len(fin_statement) > 1 and fin_statement[1].total_revenue is not None and float(fin_statement[1].total_revenue) > 0:
                revenue_growth = (float(fin_statement[0].total_revenue) - float(fin_statement[1].total_revenue)) / float(fin_statement[1].total_revenue)
            else:
                revenue_growth = None
                            
            if fin_statement[0].total_revenue is not None and balance_sheet[0].totalAssets is not None and float(balance_sheet[0].totalAssets) > 0 and float(fin_statement[0].total_revenue) > 0:
                total_asset_turnover = float(fin_statement[0].total_revenue) / float(balance_sheet[0].totalAssets)
            else:
                total_asset_turnover = None

            # Inventory Turnover
            try:
                if fin_statement[0].cost_of_revenue_total is not None and fin_statement[0].cost_of_revenue_total != 0 and balance_sheet[0].totalInventory is not None and balance_sheet[0].totalInventory != 0:
                    inventory_turnover = float(fin_statement[0].cost_of_revenue_total) / float(balance_sheet[0].totalInventory)
                else:
                    inventory_turnover = None
            except ZeroDivisionError:
                inventory_turnover = None

                        # Days Sales Outstanding (DSO)
            if fin_statement[0].total_revenue is not None and fin_statement[0].total_revenue != 0 and balance_sheet[0].totalReceivablesNet is not None and balance_sheet[0].totalReceivablesNet != 0 and float(fin_statement[0].total_revenue) != 0:
                days_sales_outstanding = (float(balance_sheet[0].totalReceivablesNet) / float(fin_statement[0].total_revenue)) * 365
            else:
                days_sales_outstanding = None
            # Debt Ratio
            if balance_sheet[0].totalDebt is not None and balance_sheet[0].totalAssets is not None and float(balance_sheet[0].totalDebt) > 0 and float(balance_sheet[0].totalAssets) > 0:
                debt_ratio = float(balance_sheet[0].totalDebt) / float(balance_sheet[0].totalAssets)
            else:
                debt_ratio = None

            # Interest Coverage Ratio
            if fin_statement[0].operating_income is not None and fin_statement[0].inter_expse_inc_net_oper is not None and float(fin_statement[0].inter_expse_inc_net_oper) > 0 and float(fin_statement[0].operating_income) > 0:
                interest_coverage = float(fin_statement[0].operating_income) / float(fin_statement[0].inter_expse_inc_net_oper)
            else:
                interest_coverage = None

            if fin_statement[0].diluted_eps_excl_extra_items is not None and market_price is not None and float(fin_statement[0].diluted_eps_excl_extra_items) > 0:
                price_to_earnings_ratio = float(market_price) / float(fin_statement[0].diluted_eps_excl_extra_items)
            else:
                price_to_earnings_ratio = None

            if (fin_statement[0].total_revenue is not None and 
                balance_sheet[0].totalCommonSharesOutstanding is not None and 
                market_price is not None and 
                float(balance_sheet[0].totalCommonSharesOutstanding) > 0 and
                float(fin_statement[0].total_revenue) != 0):
                price_to_sales_ratio = float(market_price) * float(balance_sheet[0].totalCommonSharesOutstanding) / float(fin_statement[0].total_revenue)
            else:
                price_to_sales_ratio = None

            if balance_sheet[0].totalEquity is not None and balance_sheet[0].totalCommonSharesOutstanding is not None and market_price is not None and float(balance_sheet[0].totalCommonSharesOutstanding) > 0:
                price_to_book_value = float(market_price) * float(balance_sheet[0].totalCommonSharesOutstanding) / float(balance_sheet[0].totalEquity)
            else:
                price_to_book_value = None

            if balance_sheet[0].totalReceivablesNet is not None and balance_sheet[0].totalInventory is not None and balance_sheet[0].accountsPayable is not None and fin_statement[0].cost_of_revenue_total is not None and fin_statement[0].total_revenue is not None and float(fin_statement[0].total_revenue) > 0:
                days_sales_outstanding = 365 * float(balance_sheet[0].totalReceivablesNet) / float(fin_statement[0].total_revenue)
                days_inventory_outstanding = 365 * float(balance_sheet[0].totalInventory) / float(fin_statement[0].cost_of_revenue_total)
                days_payable_outstanding = 365 * float(balance_sheet[0].accountsPayable) / float(fin_statement[0].cost_of_revenue_total)
                cash_conversion_cycle = days_sales_outstanding + float(days_inventory_outstanding) - float(days_payable_outstanding)
            else:
                cash_conversion_cycle = None
            if fin_statement[0].total_revenue is not None and balance_sheet[0].ppeTotalNet is not None and float(balance_sheet[0].ppeTotalNet) > 0:
                fixed_asset_turnover = float(fin_statement[0].total_revenue) / float(balance_sheet[0].ppeTotalNet)
            else:
                fixed_asset_turnover = None

            if fin_statement[0].total_revenue is not None and balance_sheet[0].totalAssets is not None and float(balance_sheet[0].totalAssets) > 0:
                asset_turnover = float(fin_statement[0].total_revenue) / float(balance_sheet[0].totalAssets)
            else:
                asset_turnover = None

            if fin_statement[0].operating_profit is not None and balance_sheet[0].totalDebt is not None and float(fin_statement[0].operating_profit) > 0:
                total_debt_to_ebitda = float(balance_sheet[0].totalDebt) / float(fin_statement[0].operating_profit)
            else:
                total_debt_to_ebitda = None

            return {
                'current_ratio': current_ratio,
                'quick_ratio': quick_ratio,
                'debt_to_equity_ratio': debt_to_equity_ratio,
                'return_on_assets': return_on_assets,
                'return_on_equity': return_on_equity,
                'gross_profit_margin': gross_profit_margin,
                'operating_margin': operating_margin,
                'net_profit_margin': net_profit_margin,
                'dividend_payout_ratio': dividend_payout_ratio,
                'revenue_growth': revenue_growth,
                'total_debt_to_ebitda': total_debt_to_ebitda,
                'interest_coverage': interest_coverage,
                'price_to_earnings_ratio': price_to_earnings_ratio,
                'price_to_sales_ratio': price_to_sales_ratio,
                'price_to_book_value': price_to_book_value,
                'cash_conversion_cycle': cash_conversion_cycle,
                'inventory_turnover': inventory_turnover,
                'fixed_asset_turnover': fixed_asset_turnover,
                'asset_turnover': asset_turnover,
                'debt_ratio': debt_ratio,
                'total_asset_turnover': total_asset_turnover,
                'days_sales_outstanding': days_sales_outstanding

            }

    async def get_etfs_for_ticker(self, ticker):
        async with aiohttp.ClientSession() as session:
            ticker_id, _ = await self.fetch_ticker_id(ticker)
            url = f"https://quotes-gw.webullfintech.com/api/information/company/queryEtfList?tickerId={ticker_id}&pageIndex=1&pageSize=350"
            async with session.get(url) as response:
                r = await response.json()
                datalist = r['dataList']
                etf_holdings = [ETFHoldings(i) for i in datalist]
                return etf_holdings

                



    async def get_webull_news(self, ticker, current_news_id: int = 0, page_size: int = 50, headers: dict = None) -> List[NewsItem]:
        async with aiohttp.ClientSession(headers="YOUR_WEBULL_HEADERS") as session:
            ticker_id, _ = await self.fetch_ticker_id(ticker)
            url = f"https://quotes-gw.webullfintech.com/api/information/news/tickerNews?tickerId={ticker_id}&currentNewsId={current_news_id}&pageSize={page_size}"
            async with session.get(url) as response:
                news_data = await response.json()
                return [NewsItem(news) for news in news_data]
    async def check_recent_news(self, ticker, webull_headers):

        ticker_id, _ = await self.fetch_ticker_id(ticker)
        news = await self.get_webull_news(ticker_id, headers=webull_headers)

        if not news:
            return None

        latest_news = news[0]
        news_time = parser.parse(latest_news.news_time)
        time_threshold = datetime.now(timezone.utc) - timedelta(minutes=90)

        if news_time >= time_threshold:
            return {
                'news_url': latest_news.news_url,
                'source_name': latest_news.source_name,
                'title': latest_news.title,
                'news_time': news_time
            }

        return None
    
    async def get_recent_news_for_tickers(self,ticker, webull_headers):
        ticker_id, _ = await self.fetch_ticker_id(ticker)
        recent_news_list = []
        recent_news = await self.check_recent_news(ticker_id, webull_headers)
        if recent_news is not None and recent_news['news_url'] not in seen_article_urls:
            seen_article_urls.add(recent_news['news_url'])
            recent_news_list.append(recent_news)

        return recent_news_list
    


    async def get_option_data(self, symbol):
        option_data_dict = {}
        url = f"https://quotes-gw.webullfintech.com/api/quote/option/quotes/queryBatch?derivativeIds={symbol}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                print(data)
                opt_data = [QueryDerivatives(i) for i in data]

        return opt_data