from typing import List
from dataclasses import dataclass
from dataclasses import field


import requests




@dataclass
class Derivative:
    derivative: dict = None
    tickerId: str = None
    exchangeId: int = None
    regionId: int = None
    symbol: str = None
    unSymbol: str = None
    tickerType: int = None
    belongTickerId: str = None
    direction: str = None
    weekly: str = None
    quoteLotSize: int = None
    expireDate: str = None
    strikePrice: str = None
    price: float = None
    close: float = None
    change: float = None
    changeRatio: float = None
    template: str = None
    quoteMultiplier: int = None
    cycle: str = None
    
    def __init__(self, derivative: dict = None, tickerId: str = None, exchangeId: int = None, regionId: int = None, 
                 symbol: str = None, unSymbol: str = None, tickerType: int = None, belongTickerId: str = None, 
                 direction: str = None, weekly: str = None, quoteLotSize: int = None, expireDate: str = None, 
                 strikePrice: str = None, price: float = None, close: float = None, change: float = None, 
                 changeRatio: float = None, template: str = None, quoteMultiplier: int = None, cycle: str = None):
        
        self.derivative = derivative
        self.tickerId = tickerId
        self.exchangeId = exchangeId
        self.regionId = regionId
        self.symbol = symbol
        self.unSymbol = unSymbol
        self.tickerType = tickerType
        self.belongTickerId = belongTickerId
        self.direction = direction
        self.weekly = weekly
        self.quoteLotSize = quoteLotSize
        self.expireDate = expireDate
        self.strikePrice = strikePrice
        self.price = price
        self.close = close
        self.change = change
        self.changeRatio = changeRatio
        self.template = template
        self.quoteMultiplier = quoteMultiplier
        self.cycle = cycle

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            derivative=data.get('derivative'),
            tickerId=data.get('tickerId'),
            exchangeId=data.get('exchangeId'),
            regionId=data.get('regionId'),
            symbol=data.get('symbol'),
            unSymbol=data.get('unSymbol'),
            tickerType=data.get('tickerType'),
            belongTickerId=data.get('belongTickerId'),
            direction=data.get('direction'),
            weekly=data.get('weekly'),
            quoteLotSize=data.get('quoteLotSize'),
            expireDate=data.get('expireDate'),
            strikePrice=data.get('strikePrice'),
            price=data.get('price'),
            close=data.get('close'),
            change=data.get('change'),
            changeRatio=data.get('changeRatio'),
            template=data.get('template'),
            quoteMultiplier=data.get('quoteMultiplier'),
            cycle=data.get('cycle')
        )

@dataclass
class BelongTicker:
    belongTicker: dict = field(default_factory=dict)
    tickerId: str = None
    exchangeId: int = None
    type: int = None
    secType: int = None
    regionId: int = None
    currencyId: int = None
    currencyCode: str = None
    name: str = None
    symbol: str = None
    disSymbol: str = None
    disExchangeCode: str = None
    exchangeCode: str = None
    listStatus: int = None
    template: str = None
    derivativeSupport: bool = None
    tradeTime: str = None
    faTradeTime: str = None
    status: int = None
    close: float = None
    change: float = None
    changeRatio: float = None
    marketValue: float = None
    volume: float = None
    turnoverRate: float = None
    regionName: str = None
    regionIsoCode: str = None
    peTtm: float = None
    preClose: float = None
    fiftyTwoWkHigh: float = None
    fiftyTwoWkLow: float = None
    open: float = None
    high: float = None
    low: float = None
    vibrateRatio: float = None
    pprice: float = None
    pchange: float = None
    pchRatio: float = None

    def __init__(self, belongTicker, tickerId, exchangeId, type, secType, regionId, currencyId, currencyCode, name, symbol, disSymbol, disExchangeCode, exchangeCode, listStatus, template, derivativeSupport, tradeTime, faTradeTime, status, close, change, changeRatio, marketValue, volume, turnoverRate, regionName, regionIsoCode, peTtm, preClose, fiftyTwoWkHigh, fiftyTwoWkLow, open, high, low, vibrateRatio, pprice, pchange, pchRatio):
        self.belongTicker = belongTicker
        self.tickerId = tickerId
        self.exchangeId = exchangeId
        self.type = type
        self.secType = secType
        self.regionId = regionId
        self.currencyId = currencyId
        self.currencyCode = currencyCode
        self.name = name
        self.symbol = symbol
        self.disSymbol = disSymbol
        self.disExchangeCode = disExchangeCode
        self.exchangeCode = exchangeCode
        self.listStatus = listStatus
        self.template = template
        self.derivativeSupport = derivativeSupport
        self.tradeTime = tradeTime
        self.faTradeTime = faTradeTime
        self.status = status
        self.close = close
        self.change = change
        self.changeRatio = changeRatio
        self.marketValue = marketValue
        self.volume = volume
        self.turnoverRate = turnoverRate
        self.regionName = regionName
        self.regionIsoCode = regionIsoCode
        self.peTtm = peTtm
        self.preClose = preClose
        self.fiftyTwoWkHigh = fiftyTwoWkHigh
        self.fiftyTwoWkLow = fiftyTwoWkLow
        self.open = open
        self.high = high
        self.low = low
        self.vibrateRatio = vibrateRatio
        self.pprice = pprice
        self.pchage = pchange
        self.pchRatio = pchRatio
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            belongTicker=data.get('belongTicker', {}),
            tickerId=data.get('tickerId'),
            exchangeId=data.get('exchangeId'),
            type=data.get('type'),
            secType=data.get('secType'),
            regionId=data.get('regionId'),
            currencyId=data.get('currencyId'),
            currencyCode=data.get('currencyCode'),
            name=data.get('name'),
            symbol=data.get('symbol'),
            disSymbol=data.get('disSymbol'),
            disExchangeCode=data.get('disExchangeCode'),
            exchangeCode=data.get('exchangeCode'),
            listStatus=data.get('listStatus'),
            template=data.get('template'),
            derivativeSupport=data.get('derivativeSupport'),
            tradeTime=data.get('tradeTime'),
            faTradeTime=data.get('faTradeTime'),
            status=data.get('status'),
            close=data.get('close'),
            change=data.get('change'),
            changeRatio=data.get('changeRatio'),
            marketValue=data.get('marketValue'),
            volume=data.get('volume'),
            turnoverRate=data.get('turnoverRate'),
            regionName=data.get('regionName'),
            regionIsoCode=data.get('regionIsoCode'),
            peTtm=data.get('peTtm'),
            preClose=data.get('preClose'),
            fiftyTwoWkHigh=data.get('fiftyTwoWkHigh'),
            fiftyTwoWkLow=data.get('fiftyTwoWkLow'),
            open=data.get('open'),
            high=data.get('high'),
            low=data.get('low'),
            vibrateRatio=data.get('vibrateRatio'),
            pprice=data.get('pprice'),
            pchange=data.get('pchange'),
            pchRatio=data.get('pchRatio')
        )

@dataclass
class Values:
    tickerId: str = None
    exchangeId: str = None
    regionId: int = None
    symbol: str = None
    unSymbol: str = None
    tickerType: str = None
    belongTickerId: str = None
    direction: str = None
    weekly: bool = None
    quoteLotSize: int = None
    expireDate: int = None
    strikePrice: float = None
    price: float = None
    close: float = None
    change: float = None
    changeRatio: float = None
    template: str = None
    quoteMultiplier: int = None
    cycle: str = None
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            tickerId=data.get('tickerId'),
            exchangeId=data.get('exchangeId'),
            regionId=data.get('regionId'),
            symbol=data.get('symbol'),
            unSymbol=data.get('unSymbol'),
            tickerType=data.get('tickerType'),
            belongTickerId=data.get('belongTickerId'),
            direction=data.get('direction'),
            weekly=data.get('weekly'),
            quoteLotSize=data.get('quoteLotSize'),
            expireDate=data.get('expireDate'),
            strikePrice=data.get('strikePrice'),
            price=data.get('price'),
            close=data.get('close'),
            change=data.get('change'),
            changeRatio=data.get('changeRatio'),
            template=data.get('template'),
            quoteMultiplier=data.get('quoteMultiplier'),
            cycle=data.get('cycle'),

        )



class TopOptionsVolumeTickers:
    def __init__(self):
        r = requests.get("https://quotes-gw.webullfintech.com/api/wlas/option/rank/list?regionId=6&rankType=totalVolume&pageIndex=1&pageSize=250").json()
        self.data = r['data']
        self.process_data()

    def process_data(self):
        self.ticker_data = []
        for item in self.data:
            ticker = item['ticker']
            values = item['values']

            ticker_dict = {
                'name': ticker.get('name'),
                'symbol': ticker.get('symbol'),
                'disExchangeCode': ticker.get('disExchangeCode'),
                'close': ticker.get('close'),
                'changeRatio': round(float(ticker.get('changeRatio', 0)) * 100, 2) if ticker.get('changeRatio') is not None else None,
                'volume': float(ticker.get('volume')) if ticker.get('volume') is not None else "NA",
                'netAsset': ticker.get('netAsset'),
                'totalAsset': ticker.get('totalAsset'),
                'fiftyTwoWkHigh': ticker.get('fiftyTwoWkHigh'),
                'fiftyTwoWkLow': ticker.get('fiftyTwoWkLow'),
                'open': ticker.get('open'),
                'high': ticker.get('high'),
                'low': ticker.get('low'),
                'vibrateRatio': ticker.get('vibrateRatio'),
                'opt_vol': values.get('volume'),
                'opt_oi': values.get('position'),
                'volumecallputratio': values.get('volumeCallPutRatio'),
                'positioncallputratio': values.get('positionCallPutRatio'),
                'price': values.get('price'),
                'change_ratio': round(float(values.get('changeRatio', 0)) * 100, 2) if values.get('changeRatio') is not None else None
            }

            self.ticker_data.append(ticker_dict)
    def is_ticker_in_top_list(self, input_ticker):
        for ticker in self.ticker_data:
            if ticker['symbol'] == input_ticker:
                return ticker
        return None

    


class TopOptionsPositionTickers:
    def __init__(self):
        r = requests.get("https://quotes-gw.webullfintech.com/api/wlas/option/rank/list?regionId=6&rankType=totalPosition&pageIndex=1&pageSize=250").json()
        self.data = r['data']
        self.process_data()

    def process_data(self):
        self.ticker_data = []
        for item in self.data:
            ticker = item['ticker']
            values = item['values']

            ticker_dict = {
                'name': ticker.get('name'),
                'symbol': ticker.get('symbol'),
                'disExchangeCode': ticker.get('disExchangeCode'),
                'close': ticker.get('close'),
                'changeRatio': round(float(ticker.get('changeRatio', 0)) * 100, 2) if ticker.get('changeRatio') is not None else None,
                'volume': float(ticker.get('volume')) if ticker.get('volume') is not None else "NA",
                'netAsset': ticker.get('netAsset'),
                'totalAsset': ticker.get('totalAsset'),
                'fiftyTwoWkHigh': ticker.get('fiftyTwoWkHigh'),
                'fiftyTwoWkLow': ticker.get('fiftyTwoWkLow'),
                'open': ticker.get('open'),
                'high': ticker.get('high'),
                'low': ticker.get('low'),
                'vibrateRatio': ticker.get('vibrateRatio'),
                'opt_vol': values.get('volume'),
                'opt_oi': values.get('position'),
                'volumecallputratio': values.get('volumeCallPutRatio'),
                'positioncallputratio': values.get('positionCallPutRatio'),
                'price': values.get('price'),
                'change_ratio': round(float(values.get('changeRatio', 0)) * 100, 2) if values.get('changeRatio') is not None else None
            }

            self.ticker_data.append(ticker_dict)
    def is_ticker_in_top_list(self, input_ticker):
        for ticker in self.ticker_data:
            if ticker['symbol'] == input_ticker:
                return ticker
        return None
    



class TopOptionsImpVolTickers:
    def __init__(self):
        r = requests.get("https://quotes-gw.webullfintech.com/api/wlas/option/rank/list?regionId=6&rankType=impVol&pageIndex=1&pageSize=250").json()
        self.data = r['data']
        self.process_data()

    def process_data(self):
        self.ticker_data = []
        for item in self.data:
            ticker = item['ticker']
            values = item['values']

            ticker_dict = {
                'name': ticker.get('name'),
                'symbol': ticker.get('symbol'),
                'disExchangeCode': ticker.get('disExchangeCode'),
                'close': ticker.get('close'),
                'changeRatio': round(float(ticker.get('changeRatio', 0)) * 100, 2) if ticker.get('changeRatio') is not None else None,
                'volume': float(ticker.get('volume')) if ticker.get('volume') is not None else "NA",
                'netAsset': ticker.get('netAsset'),
                'totalAsset': ticker.get('totalAsset'),
                'fiftyTwoWkHigh': ticker.get('fiftyTwoWkHigh'),
                'fiftyTwoWkLow': ticker.get('fiftyTwoWkLow'),
                'open': ticker.get('open'),
                'high': ticker.get('high'),
                'low': ticker.get('low'),
                'vibrateRatio': ticker.get('vibrateRatio'),
                'opt_imp_vol': values.get('impVol'),
                'opt_hist_vol': values.get('histVol'),
                'ivBid': values.get('ivBid'),
                'ivMid': values.get('ivMid'),
                'ivAsk': values.get('ivAsk'),
                'price': values.get('price'),
                'change_ratio': round(float(values.get('changeRatio', 0)) * 100, 2) if values.get('changeRatio') is not None else None
            }

            self.ticker_data.append(ticker_dict)
            
    def is_ticker_in_top_list(self, input_ticker):
        for ticker in self.ticker_data:
            if ticker['symbol'] == input_ticker:
                return ticker
        return None