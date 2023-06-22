import datetime
import pandas as pd

class StockLoans:
    def __init__(self, data):
        self.businessDate = [i['businessDate'] if i['businessDate'] is not None else None for i in data]
        self.newMarketLoanCount = [i['newMarketLoanCount'] if i['newMarketLoanCount'] is not None else None for i in data]
        self.totalMarketLoanVal = [i['totalMarketLoanVal'] if i['totalMarketLoanVal'] is not None else None for i in data]
        self.newBilateralLoanCount = [i['newBilateralLoanCount'] if i['newBilateralLoanCount'] is not None else None for i in data]
        self.totalBilateralLoanVal = [i['totalBilateralLoanVal'] if i['totalBilateralLoanVal'] is not None else None for i in data]
        
        self.data_dict = {
            'businessDate': self.businessDate,
            'newMarketLoanCount': self.newMarketLoanCount,
            'totalMarketLoanVal': self.totalMarketLoanVal,
            'newBilateralLoanCount': self.newBilateralLoanCount,
            'totalBilateralLoanVal': self.totalBilateralLoanVal
        }

        self.as_dataframe = pd.DataFrame(self.data_dict)
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


        self.data_dict = {
            'totalVolume': self.totalVolume,
            'optionsVolume': self.optionsVolume,
            'futuresVolume': self.futuresVolume,
            'fiftytwo_week_high': self.fiftytwo_week_high,
            'fiftytwo_week_low': self.fiftytwo_week_low,
            'monthlyDailyAverage': self.monthlyDailyAverage,
            'yearlyDailyAverage': self.yearlyDailyAverage,
            'trade_dates': self.trade_dates,
            'trade_volume': self.trade_volume
        }

        self.as_dataframe = pd.DataFrame(self.data_dict)