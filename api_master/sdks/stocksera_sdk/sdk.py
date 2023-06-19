



import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import stocksera
import pandas as pd
from cfg import today_str, thirty_days_from_now_str,thirty_days_ago_str, two_years_ago_str
from cfg import YOUR_STOCKSERA_KEY
from .models import NewsSentiment,Insiders,JimCramer,JoblessClaims,EarningsCalendar,FTD,LowFloat,House,TradingHalts,Inflation,IPOs,ShortInterest,LatestInsiderTradingSummary,MarketNews,MarketSummary,NewsSentiment,RetailSales,ReverseRepo,SECFillings,Senate,ShortVolume,StockTwits,Subreddit,DailyTreasury,WSBMentions,WSBOptions



client = stocksera.Client(YOUR_STOCKSERA_KEY)


class StockeraSDK:
    def __init__(self):

        self.client = client


    def jim_cramer(self, stock):
        data = JimCramer(client.jim_cramer(ticker=stock, segment="", call=""))
        if data:
            return data
        return None

    def jobless_claims(self, days=100):
        data = JoblessClaims(client.jobless_claims(days=days))
        if data:
            return data
        return None
    
    def IPO_calendar(self):
        data = IPOs(client.ipo_calendar())
        if data:
            return data
        return None

    def earnings_calendar(self, date_from=today_str, date_to=thirty_days_from_now_str):
        data = EarningsCalendar(client.earnings_calendar(date_from=date_from, date_to=date_to))
        if data:
            return data
        else:
            return None

    def ftd(self, ticker:str="", date_from=two_years_ago_str, date_to=today_str):
        data = FTD(client.ftd(ticker=ticker, date_from=date_from, date_to=date_to))
        
        if data:
            return data
        return None

    def low_float(self):
        data = LowFloat(client.low_float())
        if data:
            return data
        return []

    def market_news(self):
        data = MarketNews(client.market_news())
        if data:
            return data
        return []

    def house(self, name=str, ticker=str, state=str, date_from=today_str, date_to=thirty_days_from_now_str):
        data = House(client.house(name=name,ticker=ticker,state=state,date_from=date_from,date_to=date_to))
        if data:
            return data
        return None

    def trading_halts(self):
        data = TradingHalts(client.trading_halts())
        if data:
            return data
        return []

    def retail_sales(self):
        data = RetailSales(client.retail_sales())
        if data:
            return data
        return []

    def inflation(self):
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

    def reverse_repo(self, days):
        data = ReverseRepo(client.reverse_repo(days=days))
        if data:
            return data
        return []
    
    def latest_insider_summary(self):
        data = LatestInsiderTradingSummary(client.latest_insider_trading_summary())
        if data:
            return data
        return []


    def sec_fillings(self, stock):
        data = SECFillings(client.sec_fillings(stock))
        if data:
            return data
        return []

    ##TODO## -- FIX
    def senate(self, name=str,ticker=str, date_from=two_years_ago_str, date_to=today_str):
        data = client.senate(name=name, ticker=ticker, date_from=date_from, date_to=today_str)
        senate = data['senate']
        print(senate)
        if senate:
            return senate
        return None

    def short_volume(self, stock, date_from=thirty_days_ago_str, to_date=today_str):
        data = ShortVolume(client.short_volume(stock))
        if data:
            return data
        return []
    
    def short_interest(self):
        data = ShortInterest(client.short_interest())
        if data:
            return data
        return []

    def stocktwits(self, stock):
        data = StockTwits(client.stocktwits(stock))
        if data:
            return data
        return None

    def subreddit(self, stock):
        data = Subreddit(client.subreddit(stock))
        if data:
            return data
        return []

    def daily_treasury(self, days=100):
        data = DailyTreasury(client.daily_treasury(days=days))
        if data:
            return data
        return []

    def wsb_mentions(self, stock):
        data = WSBMentions(client.wsb_mentions(stock))
        if data:
            return data
        return None

    def wsb_options(self, days):
        data = WSBOptions(client.wsb_options(days=days))
        if data:
            return data
        return []
    

    def news_sentiment(self, ticker: str):
        data = NewsSentiment(client.news_sentiment(ticker))
        if data:
            return data
        return []

