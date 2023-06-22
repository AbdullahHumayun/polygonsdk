import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import stocksera
import pandas as pd
from typing import List, Optional

from cfg import today_str, thirty_days_from_now_str,thirty_days_ago_str, two_years_ago_str
from cfg import YOUR_STOCKSERA_KEY
from .models import NewsSentiment,Insiders,JimCramer,JoblessClaims,EarningsCalendar,FTD,LowFloat,House,TradingHalts,Inflation,IPOs,ShortInterest,LatestInsiderTradingSummary,MarketNews,MarketSummary,NewsSentiment,RetailSales,ReverseRepo,SECFillings,Senate,ShortVolume,StockTwits,Subreddit,DailyTreasury,WSBMentions,WSBOptions



client = stocksera.Client(YOUR_STOCKSERA_KEY)


class StockeraSDK:
    def __init__(self):

        self.client = client


    def jim_cramer(self, stock: str) -> Optional[JimCramer]:
        """Retrieve Jim Cramer data for a specific stock.

        Args:
            stock (str): Ticker symbol of the stock.

        Returns:
            Optional[JimCramer]: JimCramer data for the stock, or None if data is not available.
        """
        data = JimCramer(client.jim_cramer(ticker=stock, segment="", call=""))
        if data:
            return data
        return None

    def jobless_claims(self, days: int = 100) -> Optional[JoblessClaims]:
        """Retrieve jobless claims data for a specific number of days.

        Args:
            days (int, optional): Number of days to retrieve jobless claims data for. Defaults to 100.

        Returns:
            Optional[JoblessClaims]: Jobless claims data for the specified number of days, or None if data is not available.
        """
        data = JoblessClaims(client.jobless_claims(days=days))
        if data:
            return data
        return None
    
    def IPO_calendar(self) -> Optional[IPOs]:
        """Retrieve IPO calendar data.

        Returns:
            Optional[IPOs]: IPO calendar data, or None if data is not available.
        """
        data = IPOs(client.ipo_calendar())
        if data:
            return data
        return None

    def earnings_calendar(self, date_from: str = today_str, date_to: str = thirty_days_from_now_str) -> Optional[EarningsCalendar]:
        """Retrieve earnings calendar data for a specified date range.

        Args:
            date_from (str, optional): Start date of the date range. Defaults to today's date.
            date_to (str, optional): End date of the date range. Defaults to 30 days from now.

        Returns:
            Optional[EarningsCalendar]: Earnings calendar data for the specified date range, or None if data is not available.
        """
        data = EarningsCalendar(client.earnings_calendar(date_from=date_from, date_to=date_to))
        if data:
            return data
        else:
            return None

    def ftd(self, date_from: str = two_years_ago_str, date_to: str = today_str) -> Optional[FTD]:
        """Retrieve Failure to Deliver (FTD) data for a specified date range.

        Args:
            date_from (str, optional): Start date of the date range. Defaults to two years ago.
            date_to (str, optional): End date of the date range. Defaults to today's date.

        Returns:
            Optional[FTD]: Failure to Deliver (FTD) data for the specified date range, or None if data is not available.
        """
        data = FTD(client.ftd(date_from=date_from, date_to=date_to))
        if data:
            return data
        return None

    def low_float(self) -> List[LowFloat]:
        """Retrieve low float data.

        Returns:
            List[LowFloat]: List of low float data, or an empty list if data is not available.
        """
        data = LowFloat(client.low_float())
        if data:
            return data
        return []

    def market_news(self) -> List[MarketNews]:
        """Retrieve market news data.

        Returns:
            List[MarketNews]: List of market news data, or an empty list if data is not available.
        """
        data = MarketNews(client.market_news())
        if data:
            return data
        return []

    def house(self, name: str, ticker: str, state: str, date_from: str = today_str, date_to: str = thirty_days_from_now_str) -> Optional[House]:
        """Retrieve house data for a specific name, ticker, state, and date range.

        Args:
            name (str): Name of the house.
            ticker (str): Ticker symbol of the house.
            state (str): State of the house.
            date_from (str, optional): Start date of the date range. Defaults to today's date.
            date_to (str, optional): End date of the date range. Defaults to 30 days from now.

        Returns:
            Optional[House]: House data for the specified parameters, or None if data is not available.
        """
        data = House(client.house(name=name, ticker=ticker, state=state, date_from=date_from, date_to=date_to))
        if data:
            return data
        return None

    def trading_halts(self) -> List[TradingHalts]:
        """Retrieve trading halts data.

        Returns:
            List[TradingHalts]: List of trading halts data, or an empty list if data is not available.
        """
        data = TradingHalts(client.trading_halts())
        if data:
            return data
        return []

    def retail_sales(self) -> List[RetailSales]:
        """Retrieve retail sales data.

        Returns:
            List[RetailSales]: List of retail sales data, or an empty list if data is not available.
        """
        data = RetailSales(client.retail_sales())
        if data:
            return data
        return []

    def inflation(self) -> pd.DataFrame:
        """Retrieve inflation data.

        Returns:
            pd.DataFrame: DataFrame containing the inflation data.
        """
        data = client.inflation()
        years = list(data.keys())

        all_data = []
        for year in years:
            year_data = [year] + [data[year][month] for month in data[year]]
            all_data.append(year_data)

        df = pd.DataFrame(all_data)
        month_names = ['Year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Avg']
        df.columns = month_names
        return df

    def reverse_repo(self, days: int) -> List[ReverseRepo]:
        """Retrieve reverse repo data for a specific number of days.

        Args:
            days (int): Number of days to retrieve reverse repo data for.

        Returns:
            List[ReverseRepo]: List of reverse repo data for the specified number of days, or an empty list if data is not available.
        """
        data = ReverseRepo(client.reverse_repo(days=days))
        if data:
            return data
        return []
    
    def latest_insider_summary(self) -> Optional[LatestInsiderTradingSummary]:
        """Retrieve the latest insider trading summary data.

        Returns:
            Optional[LatestInsiderTradingSummary]: Latest insider trading summary data, or None if data is not available.
        """
        data = LatestInsiderTradingSummary(client.latest_insider_trading_summary())
        if data:
            return data
        return []

    def sec_fillings(self, stock: str) -> Optional[SECFillings]:
        """Retrieve SEC filings data for a specific stock.

        Args:
            stock (str): Ticker symbol of the stock.

        Returns:
            Optional[SECFillings]: SEC filings data for the stock, or None if data is not available.
        """
        data = SECFillings(client.sec_fillings(stock))
        if data:
            return data
        return []

    def senate(self, name: str, ticker: str, date_from: str = two_years_ago_str, date_to: str = today_str) -> Optional[Senate]:
        """Retrieve Senate data for a specific name, ticker, and date range.

        Args:
            name (str): Name of the senator.
            ticker (str): Ticker symbol associated with the senator.
            date_from (str, optional): Start date of the date range. Defaults to two years ago.
            date_to (str, optional): End date of the date range. Defaults to today's date.

        Returns:
            Optional[Senate]: Senate data for the specified parameters, or None if data is not available.
        """
        data = client.senate(name=name, ticker=ticker, date_from=date_from, date_to=date_to)
        senate = data['senate']
        if senate:
            return senate
        return None

    def short_volume(self, stock: str, date_from: str = thirty_days_ago_str, date_to: str = today_str) -> List[ShortVolume]:
        """Retrieve short volume data for a specific stock and date range.

        Args:
            stock (str): Ticker symbol of the stock.
            date_from (str, optional): Start date of the date range. Defaults to 30 days ago.
            date_to (str, optional): End date of the date range. Defaults to today's date.

        Returns:
            List[ShortVolume]: List of short volume data for the specified stock and date range, or an empty list if data is not available.
        """
        data = ShortVolume(client.short_volume(stock))
        if data:
            return data
        return []
    
    def short_interest(self) -> Optional[ShortInterest]:
        """Retrieve short interest data.

        Returns:
            Optional[ShortInterest]: Short interest data, or None if data is not available.
        """
        data = ShortInterest(client.short_interest())
        if data:
            return data
        return []

    def stocktwits(self, stock: str) -> Optional[StockTwits]:
        """Retrieve StockTwits data for a specific stock.

        Args:
            stock (str): Ticker symbol of the stock.

        Returns:
            Optional[StockTwits]: StockTwits data for the stock, or None if data is not available.
        """
        data = StockTwits(client.stocktwits(stock))
        if data:
            return data
        return None

    def subreddit(self, stock: str) -> List[Subreddit]:
        """Retrieve subreddit data for a specific stock.

        Args:
            stock (str): Ticker symbol of the stock.

        Returns:
            List[Subreddit]: List of subreddit data for the stock, or an empty list if data is not available.
        """
        data = Subreddit(client.subreddit(stock))
        if data:
            return data
        return []

    def daily_treasury(self, days: int = 100) -> List[DailyTreasury]:
        """Retrieve daily treasury data for a specific number of days.

        Args:
            days (int, optional): Number of days to retrieve daily treasury data for. Defaults to 100.

        Returns:
            List[DailyTreasury]: List of daily treasury data for the specified number of days, or an empty list if data is not available.
        """
        data = DailyTreasury(client.daily_treasury(days=days))
        if data:
            return data
        return []

    def wsb_mentions(self, stock: str) -> Optional[WSBMentions]:
        """Retrieve WSB mentions data for a specific stock.

        Args:
            stock (str): Ticker symbol of the stock.

        Returns:
            Optional[WSBMentions]: WSB mentions data for the stock, or None if data is not available.
        """
        data = WSBMentions(client.wsb_mentions(stock))
        if data:
            return data
        return None

    def wsb_options(self, days: int) -> List[WSBOptions]:
        """Retrieve WSB options data for a specific number of days.

        Args:
            days (int): Number of days to retrieve WSB options data for.

        Returns:
            List[WSBOptions]: List of WSB options data for the specified number of days, or an empty list if data is not available.
        """
        data = WSBOptions(client.wsb_options(days=days))
        if data:
            return data
        return []

    def news_sentiment(self, ticker: str) -> List[NewsSentiment]:
        """Retrieve news sentiment data for a specific stock.

        Args:
            ticker (str): Ticker symbol of the stock.

        Returns:
            List[NewsSentiment]: List of news sentiment data for the stock, or an empty list if data is not available.
        """
        data = NewsSentiment(client.news_sentiment(ticker))
        if data:
            return data
        return []