import stocksera
from cfg import YOUR_STOCKSERA_KEY,today_str, thirty_days_from_now_str

from .models import JimCramer,JoblessClaims,EarningsCalendar,FTD,LowFloat,House,TradingHalts,Inflation,IPOCalendar,ShortInterest,LatestInsiderTradingSummary,MarketNews,MarketSummary,NewsSentiment,RetailSales,ReverseRepo,SECFillings,Senate,ShortVolume,StockTwits,Subreddit,DailyTreasury,WSBMentions,WSBOptions



client = stocksera.Client(YOUR_STOCKSERA_KEY)


class StockSeraSDK:
    def __init__(self):

        self.client = client


    def jim_cramer(self, stock):
        data = client.jim_cramer(ticker=stock, segment="", call="")
        if data:
            return JimCramer(data)
        return None

    def jobless_claims(self):
        data = client.jobless_claims()
        if data:
            return JoblessClaims(data)
        return None

    def earnings_calendar(self, date_from=today_str, date_to=thirty_days_from_now_str):
        data = EarningsCalendar(client.earnings_calendar(date_from=date_from, date_to=date_to))
        if data:
            return data
        else:
            return None

    def ftd(self, from_date=today_str, date_to=thirty_days_from_now_str):
        data = FTD(client.ftd(date_from=from_date, date_to=date_to))
        if data:
            return data
        return None

    def low_float(self):
        data = LowFloat(client.low_float)
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

    def inflation(self):
        data = Inflation(client.inflation())
        if data:
            return data
        return None

    def ipo_calendar(self):
        data = IPOCalendar(client.ipo_calendar())
        if data:
            return data
        return []

    def short_interest(self):
        data = ShortInterest(client.short_interest())
        if data:
            return data
        return []

    def latest_insider_trading_summary(self):
        data = LatestInsiderTradingSummary(client.latest_insider_trading_summary())
        if data:
            return data
        return []

    def market_news(self):
        data = MarketNews(client.market_news())
        if data:
            return data
        return []

    def market_summary(self, market_type):
        data = client.market_summary(market_type=market_type)
        if data:
            return MarketSummary(data)
        return None

    def news_sentiment(self, stock):
        data = NewsSentiment(client.news_sentiment(stock))
        if data:
            return data
        return []

    def retail_sales(self):
        data = RetailSales(client.retail_sales())
        if data:
            return data
        return []

    def reverse_repo(self, days):
        data = ReverseRepo(client.reverse_repo(days=days))
        if data:
            return data
        return []

    def sec_fillings(self, stock):
        data = SECFillings(client.sec_fillings(stock))
        if data:
            return data
        return []

    def senate(self, stock):
        data = client.senate(stock)
        if data:
            return Senate(data)
        return None

    def short_volume(self, stock):
        data = ShortVolume(client.short_volume(stock))
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

    def daily_treasury(self, days):
        data = client.daily_treasury(days=days)
        if data:
            return DailyTreasury(data)
        return []

    def wsb_mentions(self, stock):
        data = client.wsb_mentions(stock)
        if data:
            return WSBMentions(data)
        return None

    def wsb_options(self, days):
        data = WSBOptions(client.wsb_options(days=days))
        if data:
            return data
        return []
