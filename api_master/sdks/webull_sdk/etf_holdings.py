import pandas as pd

class ETFHoldings:
    def __init__(self, datalist):



        self.name = datalist.get('name',None)
        self.changeRatio = datalist.get('changeRatio', None)
        self.shareNumber = datalist.get('shareNumber', None)
        self.ratio = datalist.get('ratio', None)


        self.tickerTuple = datalist.get('tickerTuple', None)
        self.tickerId = datalist.get('tickerId', None)
        self.etfname = datalist.get('name', None)
        self.symbol = datalist.get('symbol', None)



        self.data_dict = { 
            'Name': self.name,
            'ChangeRatio': self.changeRatio,
            'ShareNumber': self.shareNumber,
            'Ratio': self.ratio,
            'Ticker ID': self.tickerId,
            'ETF Name': self.etfname,
            'Symbol': self.symbol
        }


        self.df = pd.DataFrame(self.data_dict)