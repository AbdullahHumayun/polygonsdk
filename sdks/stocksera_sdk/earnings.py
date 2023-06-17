
class Earnings:
    def __init__(self, data):


        self.date = [i['date'] if i['date'] is not None else None for i in data]
        self.hour = [i['hour'] if i['hour'] is not None else None for i in data]
        self.ticker = [i['ticker'] if i['ticker'] is not None else None for i in data]
        self.eps_est = [i['eps_est'] if i['eps_est'] is not None else None for i in data]
        self.eps_act = [i['eps_act'] if i['eps_act'] is not None else None for i in data]
        self.revenue_est = [i['revenue_est'] if i['revenue_est'] is not None else None for i in data]
        self.revenue_act = [i['revenue_act'] if i['revenue_act'] is not None else None for i in data]
        self.year = [i['year'] if i['year'] is not None else None for i in data]
        self.quarter = [i['quarter'] if i['quarter'] is not None else None for i in data]
        self.mkt_cap = [i['mkt_cap'] if i['mkt_cap'] is not None else None for i in data]