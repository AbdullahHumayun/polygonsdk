class Indices:
    __slots__ = ['name', 'ticker']
    def __init__(self, results):
        self.name = [i.get('name', None) for i in results]
        self.ticker = [i.get('ticker', None) for i in results]



class IndicesData:
    __slots__ = ['session', 'change', 'change_percent', 'close', 'high', 'low', 'open', 'previous_close']
    def __init__(self, results):

        self.session = [i['session'] if i['session'] is not None else None for i in results]
        self.change = [i['change'] if i['change'] is not None else 0 for i in self.session]
        self.change_percent = [i['change_percent'] if i['change_percent'] is not None else 0 for i in self.session]
        self.close = [i['close'] if i['close'] is not None else 0 for i in self.session]
        self.high = [i['high'] if i['high'] is not None else 0 for i in self.session]
        self.low = [i['low'] if i['low'] is not None else 0 for i in self.session]
        self.open = [i['open'] if i['open'] is not None else 0 for i in self.session]
        self.previous_close = [i['previous_close'] if i['previous_close'] is not None else 0 for i in self.session]



