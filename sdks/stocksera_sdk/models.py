"""STOCKSERA MODELS"""


class DailyTreasury:
    def __init__(self, data):
        self.date = [i.get('Date') if i.get('Date') is not None else None for i in data]
        self.close_balance = [i.get('Close Balance') if i.get('Close Balance') is not None else None for i in data]
        self.open_balance = [i.get('Open Balance') if i.get('Open Balance') is not None else None for i in data]
        self.amount_change = [i.get('Amount Change') if i.get('Amount Change') is not None else None for i in data]
        self.percent_change = [i.get('Percent Change') if i.get('Percent Change') is not None else None for i in data]
        self.moving_avg = [i.get('Moving Avg') if i.get('Moving Avg') is not None else None for i in data]


class EarningsCalendar:
    def __init__(self, data):
        self.date = [i['date'] if i['date'] is not None else None for i in data]
        self.hour = [i['hour'] if i['hour'] is not None else None for i in data]
        self.ticker = [i['ticker'] if i['ticker'] is not None else None for i in data]
        self.eps_est = [i['eps_est'] if i['eps_est'] is not None else None for i in data]
        self.eps_act  = [i['eps_act'] if i['eps_act'] is not None else None for i in data]
        self.revenue_est = [i['revenue_est'] if i['revenue_est'] is not None else None for i in data]
        self.revenue_act = [i['revenue_act'] if i['revenue_act'] is not None else None for i in data]
        self.year = [i['year'] if i['year'] is not None else None for i in data]
        self.quarter = [i['quarter'] if i['quarter'] is not None else None for i in data]
        self.mkt_cap = [i['mkt_cap'] if i['mkt_cap'] is not None else None for i in data]


class FTD:
    def __init__(self, data):
        print(data)
        self.date = [i['Date'] if i['Date'] is not None else None for i in data]
        try:
            self.ticker = [i['Ticker'] if i['Ticker'] is not None else None for i in data]
        except KeyError:
            self.ticker = "N/A"
        self.price = [i['Price'] if i['Price'] is not None else None for i in data]
        self.amount_ftd = [i['FTD'] if i['FTD'] is not None else None for i in data]

        self.t35_date = [i['T+35 Date'] if i['T+35 Date'] is not None else None for i in data]
        self.dollar_cost = [i['FTD x $'] if i['FTD x $'] is not None else None for i in data]



class House:
    def __init__(self, data):
        house = data['house'] if 'house' in data else None
        self.trans_date = [i['Transaction Date'] if 'Transaction Date' in i else None for i in house]
        self.owner = [i['Owner'] if 'Owner' in i else None for i in house]
        self.ticker = [i['Ticker'] if 'Ticker' in i else None for i in house]
        self.asset_desc = [i['Asset Description'] if 'Asset Description' in i else None for i in house]
        self.asset_type = [i['Asset Type'] if 'Asset Type' in i else None for i in house]
        self.type = [i['Type'] if 'Type' is not None else None for i in house]
        self.amount = [i['Amount'] if 'Amount' in i else None for i in house]
        self.rep = [i['Representative'] if 'Representative' in i else None for i in house]
        self.link = [i['Link'] if 'Link' in i else None for i in house]
        self.disclosure_date = [i['Disclosure Date'] if 'Disclosure Date' in i else None for i in house]
        self.district=[i['District'] if 'District' in i else None for i in house]
        self.capital_gains_over_200k = [i['Cap Gains Over 200USD'] if 'Cap Gains Over 200USD' in i else None for i in house]


class Inflation:
    def __init__(self, data):
        self.shares = data.get('shares')
        self.value = data.get('value')
        self.shares_total = data.get('shares_total')


class IPOCalendar:
    def __init__(self, data):
        self.date = data.get('date')
        self.symbol = data.get('symbol')
        self.name = data.get('name')
        self.expected_price = data.get('expected_price')
        self.number_shares = data.get('number_shares')
        self.mkt_cap = data.get('mkt_cap')
        self.status = data.get('status')
        self.exchange = data.get('exchange')


class JimCramer:
    def __init__(self, data):
        self.ticker = data.get('ticker')
        self.date = data.get('date')
        self.segment = data.get('segment')
        self.call = data.get('call')
        self.price = data.get('price')


class JoblessClaims:
    def __init__(self, data):
        self.date = [i['Date'] if 'Date' in i else None for i in data]
        self.number = [i['Date'] if 'Date' in i else None for i in data]
        self.percent_change = [i['Date'] if 'Date' in i else None for i in data]



class LowFloat:
    def __init__(self, data):
        self.rank = data.get('rank')
        self.ticker = data.get('ticker')
        self.company_name = data.get('company_name')
        self.exchange = data.get('exchange')
        self.previous_close = data.get('previous_close')
        self.one_day_change = data.get('one_day_change')
        self.floating_shares = data.get('floating_shares')
        self.outstanding_shares = data.get('outstanding_shares')
        self.short_int = data.get('short_int')
        self.market_cap = data.get('market_cap')
        self.industry = data.get('industry')


class LatestInsiderTradingSummary:
    def __init__(self, data):
        self.ticker = data.get('ticker')
        self.amount = data.get('amount')
        self.market_cap = data.get('market_cap')
        self.percent_of_market_cap = data.get('percent_of_market_cap')


class MarketNews:
    def __init__(self, data):
        self.Date = [i['Date'] if i['Date'] is not None else None for i in data]
        self.Title = [i['Title'] if i['Title'] is not None else None for i in data]
        self.Source = [i['Source'] if i['Source'] is not None else None for i in data]
        self.URL = [i['URL'] if i['URL'] is not None else None for i in data]
        self.Section = [i['Section'] if i['Section'] is not None else None for i in data]


class MarketSummary:
    def __init__(self, data):
        self.snp500 = data.get('snp500')


class NewsSentiment:
    def __init__(self, data):
        self.date = data.get('date')
        self.title = data.get('title')
        self.link = data.get('link')
        self.sentiment = data.get('sentiment')


class RetailSales:
    def __init__(self, data):
        self.date = data.get('date')
        self.amount = data.get('amount')
        self.percent_change = data.get('percent_change')
        self.monthly_avg_cases = data.get('monthly_avg_cases')


class ReverseRepo:
    def __init__(self, data):
        self.date = data.get('date')
        self.amount = data.get('amount')
        self.num_parties = data.get('num_parties')
        self.average = data.get('average')
        self.moving_avg = data.get('moving_avg')


class SECFillings:
    def __init__(self, data):
        self.Filling = [i['Filling'] if i['Filling'] is not None else None for i in data]
        self.Description = [i['Description'] if i['Description'] is not None else None for i in data]
        self.FillingDate = [i['Filling Date'] if i['Filling Date'] is not None else None for i in data]
        self.report_url = [i['report_url'] if i['report_url'] is not None else None for i in data]
        self.filing_url = [i['filing_url'] if i['filing_url'] is not None else None for i in data]


class Senate:
    def __init__(self, data):
        self.senate = data.get('senate')
        self.names_available = data.get('names_available')


class ShortInterest:
    def __init__(self, data):
        self.rank = data.get('rank')
        self.ticker = data.get('ticker')
        self.date = data.get('date')
        self.short_interest = data.get('short_interest')
        self.average_volume = data.get('average_volume')
        self.days_to_cover = data.get('days_to_cover')
        self.percent_float_short = data.get('percent_float_short')


class ShortVolume:
    def __init__(self, data):
        self.date = data.get('date')
        self.short_vol = data.get('short_vol')
        self.short_exempt_vol = data.get('short_exempt_vol')
        self.total_vol = data.get('total_vol')
        self.percent_shorted = data.get('percent_shorted')
        self.close = data.get('close')


class StockTwits:
    def __init__(self, data):
        self.rank = data.get('rank')
        self.watchlist = data.get('watchlist')
        self.date_updated = data.get('date_updated')


class Subreddit:
    def __init__(self, data):
        self.date = data.get('date')
        self.subreddit = data.get('subreddit')
        self.redditors = data.get('redditors')
        self.active = data.get('active')
        self.percent_active = data.get('percent_active')
        self.percent_growth = data.get('percent_growth')
        self.percent_price_change = data.get('percent_price_change')


class TradingHalts:
    def __init__(self, data):
        self.halt_date = data.get('halt_date')
        self.halt_time = data.get('halt_time')
        self.ticker = data.get('ticker')
        self.exchange = data.get('exchange')
        self.reason = data.get('reason')
        self.resume_date = data.get('resume_date')
        self.resume_time = data.get('resume_time')


class WSBMentions:
    def __init__(self, data):
        self.mentions = data.get('mentions')


class WSBOptions:
    def __init__(self, data):
        self.ticker = data.get('ticker')
        self.calls = data.get('calls')
        self.puts = data.get('puts')
        self.ratio = data.get('ratio')