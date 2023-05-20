class ETFHoldings:
    def __init__(self, datalist):



        self.name = datalist.get('name',None)
        self.changeRatio = datalist.get('changeRatio', None)
        self.shareNumber = datalist.get('shareNumber', None)
        self.ratio = datalist.get('ratio', None)


        tickerTuple = datalist.get('tickerTuple', None)
        self.tickerId = datalist.get('tickerId', None)
        self.etfname = datalist.get('name', None)
        self.symbol = datalist.get('symbol', None)