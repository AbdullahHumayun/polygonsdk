import datetime

class StockLoans:
    def __init__(self, data):
        self.businessDate = [i['businessDate'] if i['businessDate'] is not None else None for i in data]
        self.newMarketLoanCount = [i['newMarketLoanCount'] if i['newMarketLoanCount'] is not None else None for i in data]
        self.totalMarketLoanVal = [i['totalMarketLoanVal'] if i['totalMarketLoanVal'] is not None else None for i in data]
        self.newBilateralLoanCount = [i['newBilateralLoanCount'] if i['newBilateralLoanCount'] is not None else None for i in data]
        self.totalBilateralLoanVal = [i['totalBilateralLoanVal'] if i['totalBilateralLoanVal'] is not None else None for i in data]



class VolumeTotals:
    def __init__(self, data):
        self.totalVolume = float(data['totalVolume'])
        self.optionsVolume = float(data['optionsVolume'])
        self.futuresVolume = float(data['futuresVolume'])
        self.fiftytwo_week_high = float(data['fiftytwo_week_high'])
        self.fiftytwo_week_low = float(data['fiftytwo_week_low'])
        self.monthlyDailyAverage = float(data['monthlyDailyAverage'])
        self.yearlyDailyAverage = float(data['yearlyDailyAverage'])
        weekly_volume = data['weekly_volume']
        trade_date = [i['trade_date'] if i['trade_date'] is not None else None for i in weekly_volume]
        self.trade_dates = [datetime.datetime.fromtimestamp(timestamp / 1000).strftime("%Y-%m-%d") for timestamp in trade_date]
        self.trade_volume = [i['trade_volume'] if i['trade_volume'] is not None else None for i in weekly_volume]
