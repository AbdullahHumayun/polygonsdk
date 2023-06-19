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
        self.amount_ftd = [i['Failure to Deliver'] if i['Failure to Deliver'] is not None else None for i in data]

        self.t35_date = [i['T+35 Date'] if i['T+35 Date'] is not None else None for i in data]
        self.dollar_cost = [i['Amount (FTD x $)'] if i['Amount (FTD x $)'] is not None else None for i in data]



class House:
    def __init__(self, data):
        house = data['house']
        self.trans_date = [i['Transaction Date'] if 'Transaction Date' in i else None for i in house]
        self.owner = [i['Owner'] if 'Owner' in i else None for i in house]
        self.ticker = [i['Ticker'] if 'Ticker' in i else None for i in house]
        self.asset_desc = [i['Asset Description'] if 'Asset Description' in i else None for i in house]
        self.asset_type = [i['Asset Type'] if 'Asset Type' in i else None for i in house]
        self.type = [i['Type'] if 'Type' in i else None for i in house]
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


class IPOs:
    def __init__(self, data):
        self.date = [i['Date'] if 'Date' is not None else None for i in data]
        self.exchange = [i['Exchange'] if 'Exchange' is not None else None for i in data]
        self.expected_price = [i['Expected Price'] if 'Expected Price' is not None else None for i in data]
        self.mkt_cap = [i['Mkt Cap'] if 'Mkt Cap' is not None else None for i in data]
        self.name = [i['Name'] if 'Name' is not None else None for i in data]
        self.number_shares = [i['Number Shares'] if 'Number Shares' is not None else None for i in data]
        self.status = [i['Status'] if 'Status' is not None else None for i in data]
        self.symbol = [i['Symbol'] if 'Symbol' is not None else None for i in data]


class JimCramer:
    def __init__(self, data):
        self.ticker = [i['Ticker'] if 'Ticker' in i else None for i in data]
        self.date = [i['Date'] if 'Date' in i else None for i in data]
        self.segment = [i['Segment'] if 'Segment' in i else None for i in data]
        self.call = [i['Call'] if 'Call' in i else None for i in data]
        self.price = [i['Price'] if 'Price' in i else None for i in data]


class JoblessClaims:
    def __init__(self, data):
        self.date = [i['Date'] if 'Date' in i else None for i in data]
        self.number = [i['Number'] if 'Number' in i else None for i in data]
        self.percent_change = [i['Percent Change'] if 'Percent Change' in i else None for i in data]



class LowFloat:
    def __init__(self, data):
        self.Rank = [i['Rank'] if 'Rank' in i else None for i in data]
        self.ticker= [i['ticker'] if 'ticker' in i else None for i in data]
        self.company_name= [i['company_name'] if 'company_name' in i else None for i in data]
        self.exchange= [i['exchange'] if 'exchange' in i else None for i in data]
        self.previous_close= [i['previous_close'] if 'previous_close' in i else None for i in data]
        self.one_day_change= [i['one_day_change'] if 'one_day_change' in i else None for i in data]
        self.floating_shares= [i['floating_shares'] if 'floating_shares' in i else None for i in data]
        self.outstanding_shares= [i['outstanding_shares'] if 'outstanding_shares' in i else None for i in data]
        self.short_int= [i['short_int'] if 'short_int' in i else None for i in data]
        self.market_cap= [i['market_cap'] if 'market_cap' in i else None for i in data]
        self.industry= [i['industry'] if 'industry' in i else None for i in data]


class LatestInsiderTradingSummary:
    def __init__(self, data):
        self.ticker = [i['Ticker'] if 'Ticker' in i else None for i in data]
        self.amount = [i['Amount'] if 'Amount' in i else None for i in data]
        self.market_cap =[i['Market Cap'] if 'Market Cap' in i else None for i in data]
        self.percent_of_market_cap = [i['% of Mkt Cap'] if '% of Mkt Cap' in i else None for i in data]


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
        self.Date = [i['Date'] if 'Date' in i else None for i in data]
        self.Title = [i['Title'] if 'Title' in i else None for i in data]
        self.Link = [i['Link'] if 'Link' in i else None for i in data]
        self.Sentiment = [i['Sentiment'] if 'Sentiment' in i else None for i in data]

class RetailSales:
    def __init__(self, data):
        self.date = [i['Date'] if 'Date' in i else None for i in data]
        self.amount = [i['Amount'] if 'Amount' in i else None for i in data]
        self.percent_change = [i['Percent Change'] if 'Percent Change' in i else None for i in data]
        self.monthly_avg_cases = [i['monthly_avg_cases'] if 'monthly_avg_cases' in i else None for i in data]


class ReverseRepo:
    def __init__(self, data):
        self.date = [i['Date'] if 'Date' in i else None for i in data]
        self.amount = [i['Amount'] if 'Amount' in i else None for i in data]
        self.num_parties = [i['Num Parties'] if 'Num Parties' in i else None for i in data]
        self.average = [i['Average'] if 'Average' in i else None for i in data]
        self.moving_average = [i['Moving Average'] if 'Moving Average' in i else None for i in data]


class SECFillings:
    def __init__(self, data):
        self.Filling = [i['Filling'] if i['Filling'] is not None else None for i in data]
        self.Description = [i['Description'] if i['Description'] is not None else None for i in data]
        self.FillingDate = [i['Filling Date'] if 'Filling Date' in i else None for i in data]
        self.report_url = [i['report_url'] if 'report_url' in i else None for i in data]
        self.filing_url = [i['filing_url'] if 'filing_url' in i else None for i in data]


class Senate:

    def __init__(self, data):
        self.TransactionDate = [data.get('Transaction Date') for i in data]
        self.Owner = [data.get('Owner') if 'Owner' in i else None for i in data]
        self.Ticker = [i['Ticker'] if 'Ticker' in i else None for i in data]
        self.AssetDescription = [i['Asset Description'] if 'Asset Description' in i else None for i in data]
        self.AssetType = [data.get('Asset Type') if 'Asset Type' in i else None for i in data]
        self.Type = [data.get('Type') if 'Type' in i else None for i in data]
        self.Amount = [data.get('Amount') if 'Amount' in i else None for i in data]
        self.Senator = [data.get('Senator') if 'Senator' in i else None for i in data]
        self.Link = [data.get('Link') if 'Link' in i else None for i in data]
        self.DisclosureDate = [data.get('Disclosure Date') if 'Disclosure Date' in i else None for i in data]


class ShortInterest:
    def __init__(self, data):

        
        self.Rank = [i['Rank'] if 'Rank' in i else None for i in data]
        self.Ticker= [i['Ticker'] if 'Ticker' in i else None for i in data]
        self.Date=[i['Date'] if 'Date' in i else None for i in data]
        self.ShortInterest= [i['Short Interest'] if 'Short Interest' in i else None for i in data]
        self.AverageVolume= [i['Average Volume'] if 'Average Volume' in i else None for i in data]
        self.DaysToCover= [i['Days To Cover'] if 'Days To Cover' in i else None for i in data]
        self.FloatShort= [i['% Float Short'] if '% Float Short' in i else None for i in data]


class ShortVolume:
    def __init__(self, data):
        self.date = [i['Date'] if 'Date' in i else None for i in data]
        self.short_vol = [i.get('Short Vol', None) for i in data]
        self.short_exempt_vol = [i.get('Short Exempt Vol', None) for i in data]
        self.total_vol = [i.get('Total Vol', None) for i in data]
        self.percent_shorted = [i.get('% Shorted', None) for i in data]



class StockTwits:
    def __init__(self, data):
        self.rank = [i['rank'] if i['rank'] is not None else None for i in data]
        self.watchlist = [i['watchlist'] if 'watchlist' in i else None for i in data]
        self.date_updated = [i['date_updated'] if 'date_updated' in i else None for i in data]


class Subreddit:
    def __init__(self, data):
        self.Date = [i['Date'] if 'Date' in i else None for i in data]
        self.subreddit = [i['subreddit'] if 'subreddit' in i else None for i in data]
        self.Redditors = [i['Redditors'] if 'Redditors' in i else None for i in data]
        self.Active = [i['Active'] if 'Active' in i else None for i in data]
        self.percActive = [i['% Active'] if '% Active' in i else None for i in data]
        self.percGrowth = [i['% Growth'] if '% Growth' in i else None for i in data]
        self.percPriceChange = [i['% Price Change'] if '% Price Change' in i else None for i in data]


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


class Insiders:
    def __init__(self, data):


        self.Ticker = [i['Ticker'] if 'Ticker' in i else None for i in data]
        self.Name = [i['Name'] if 'Name' in i else None for i in data]
        self.Relationship = [i['Relationship'] if 'Relationship' in i else None for i in data]
        self.Date = [i['Date'] if 'Date' in i else None for i in data]
        self.Transaction = [i['Transaction'] if 'Transaction' in i else None for i in data]
        self.Cost = [i['Cost'] if 'Cost' in i else None for i in data]
        self.Shares = [i['Shares'] if 'Shares' in i else None for i in data]
        self.Value = [i['Value ($)'] if 'Value ($)' in i else None for i in data]
        self.SharesTotal= [i['#Shares Total'] if '#Shares Total' in i else None for i in data]
        self.DateFilled= [i['Date Filled'] if 'Date Filled' in i else None for i in data]