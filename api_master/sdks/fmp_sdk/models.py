class PriceTarget:
    def __init__(self, data):
        self.symbol = [i['symbol'] if 'symbol' in i else None for i in data]
        self.pub_date = [i['publishedDate'] if 'publishedDate' in i else None for i in data]
        self.news_url = [i['newsURL'] if 'newsURL' in i else None for i in data]
        self.news_title = [i['newsTitle'] if 'newsTitle' in i else None for i in data]
        self.analyst_name = [i['analystName'] if 'analystName' in i else None for i in data]
        self.target = [i['priceTarget'] if 'priceTarget' in i else None for i in data]
        self.adjusted_target = [i['adjPriceTarget'] if 'adjPriceTarget' in i else None for i in data]
        self.price_when_posted = [i['priceWhenPosted'] if 'priceWhenPosted' in i else None for i in data]
        self.news_publisher = [i['newsPublisher'] if 'newsPublisher' in i else None for i in data]
        self.newsbase_url = [i['newsBaseURL'] if 'newsBaseURL' in i else None for i in data]
        self.analyst_company = [i['analystCompany'] if 'analystCompany' in i else None for i in data]



class CountryRiskPremium:
    def __init__(self, data):
        self.country = [i['country'] if 'country' in i else None for i in data]
        self.continent = [i['continent'] if 'continent' in i else None for i in data]
        self.totalEquityRiskPremium = [i['totalEquityRiskPremium'] if 'totalEquityRiskPremium' in i else None for i in data]
        self.countryRiskPremium = [i['countryRiskPremium'] if 'countryRiskPremium' in i else None for i in data]