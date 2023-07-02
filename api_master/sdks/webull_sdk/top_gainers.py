import pandas as pd

class GainersData:
    def __init__(self, data):
        self.tickerId = [int(i['ticker']['tickerId']) if isinstance(i['ticker']['tickerId'], str) else i['ticker']['tickerId'] for i in data if 'ticker' in i and 'tickerId' in i['ticker']]
        
        self.exchangeId = [i['exchangeId'] for i in data if 'exchangeId' in i]
        self.type = [i['type'] for i in data if 'type' in i]
        self.secType = [i['secType'] for i in data if 'secType' in i]
        self.regionId = [i['regionId'] for i in data if 'regionId' in i]
        self.currencyId = [i['currencyId'] for i in data if 'currencyId' in i]
        self.currencyCode = [i['currencyCode'] for i in data if 'currencyCode' in i]
        self.name = [i['name'] for i in data if 'name' in i]
        self.symbol = [i['symbol'] for i in data if 'symbol' in i]
        self.disSymbol = [i['disSymbol'] for i in data if 'disSymbol' in i]
        self.disExchangeCode = [i['disExchangeCode'] for i in data if 'disExchangeCode' in i]
        self.exchangeCode = [i['exchangeCode'] for i in data if 'exchangeCode' in i]
        self.listStatus = [i['listStatus'] for i in data if 'listStatus' in i]
        self.template = [i['template'] for i in data if 'template' in i]
        self.derivativeSupport = [i['derivativeSupport'] for i in data if 'derivativeSupport' in i]
        self.isPTP = [i['isPTP'] for i in data if 'isPTP' in i]
        self.tradeTime = [i['tradeTime'] for i in data if 'tradeTime' in i]
        self.faTradeTime = [i['faTradeTime'] for i in data if 'faTradeTime' in i]
        self.status = [i['status'] for i in data if 'status' in i]
        self.close = [i['close'] for i in data if 'close' in i]
        self.change = [i['change'] for i in data if 'change' in i]
        self.changeRatio = [i['changeRatio'] for i in data if 'changeRatio' in i]
        self.marketValue = [i['marketValue'] for i in data if 'marketValue' in i]
        self.volume = [i['volume'] for i in data if 'volume' in i]
        self.turnoverRate = [i['turnoverRate'] for i in data if 'turnoverRate' in i]
        self.regionName = [i['regionName'] for i in data if 'regionName' in i]
        self.regionIsoCode = [i['regionIsoCode'] for i in data if 'regionIsoCode' in i]
        self.peTtm = [i['peTtm'] for i in data if 'peTtm' in i]
        self.preClose = [i['preClose'] for i in data if 'preClose' in i]
        self.fiftyTwoWkHigh = [i['fiftyTwoWkHigh'] for i in data if 'fiftyTwoWkHigh' in i]
        self.fiftyTwoWkLow = [i['fiftyTwoWkLow'] for i in data if 'fiftyTwoWkHigh' in i]
        self.open = [i['open'] for i in data if 'open' in i]
        self.high = [i['high'] for i in data if 'high' in i]
        self.low = [i['low'] for i in data if 'low' in i]


class Ticker:
    def __init__(self, ticker):
        self.tickerId = [i['tickerId'] if 'tickerId' in i else None for i in ticker]
        self.exchangeId = [i['exchangeId'] if 'exchangeId' in i else None for i in ticker]
        self.type = [i['type'] if 'type' in i else None for i in ticker]
        self.secType = [i['secType'] if 'secType' in i else None for i in ticker]
        self.regionId = [i['regionId'] if 'regionId' in i else None for i in ticker]
        self.currencyId = [i['currencyId'] if 'currencyId' in i else None for i in ticker]
        self.currencyCode = [i['currencyCode'] if 'currencyCode' in i else None for i in ticker]
        self.name = [i['name'] if 'name' in i else None for i in ticker]
        self.symbol = [i['symbol'] if 'symbol' in i else None for i in ticker]
        self.disSymbol = [i['disSymbol'] if 'disSymbol' in i else None for i in ticker]
        self.disExchangeCode = [i['disExchangeCode'] if 'disExchangeCode' in i else None for i in ticker]
        self.exchangeCode = [i['exchangeCode'] if 'exchangeCode' in i else None for i in ticker]
        self.listStatus = [i['listStatus'] if 'listStatus' in i else None for i in ticker]
        self.template = [i['template'] if 'template' in i else None for i in ticker]
        self.derivativeSupport = [i['derivativeSupport'] if 'derivativeSupport' in i else None for i in ticker]
        self.isPTP = [i['isPTP'] if 'isPTP' in i else None for i in ticker]
        self.tradeTime = [i['tradeTime'] if 'tradeTime' in i else None for i in ticker]
        self.faTradeTime = [i['faTradeTime'] if 'faTradeTime' in i else None for i in ticker]
        self.status = [i['status'] if 'status' in i else None for i in ticker]
        self.close = [i['close'] if 'close' in i else None for i in ticker]
        self.change = [i['change'] if 'change' in i else None for i in ticker]
        self.changeRatio = [i['changeRatio'] if 'changeRatio' in i else None for i in ticker]
        self.marketValue = [i['marketValue'] if 'marketValue' in i else None for i in ticker]
        self.volume = [i['volume'] if 'volume' in i else None for i in ticker]
        self.regionName = [i['regionName'] if 'regionName' in i else None for i in ticker]
        self.regionIsoCode = [i['regionIsoCode'] if 'regionIsoCode' in i else None for i in ticker]
        self.peTtm = [i['peTtm'] if 'peTtm' in i else None for i in ticker]
        self.preClose = [i['preClose'] if 'preClose' in i else None for i in ticker]
        self.fiftyTwoWkHigh = [i['fiftyTwoWkHigh'] if 'fiftyTwoWkHigh' in i else None for i in ticker]
        self.fiftyTwoWkLow = [i['fiftyTwoWkLow'] if 'fiftyTwoWkLow' in i else None for i in ticker]
        self.open = [i['open'] if 'open' in i else None for i in ticker]
        self.high = [i['high'] if 'high' in i else None for i in ticker]
        self.low = [i['low'] if 'low' in i else None for i in ticker]
        self.vibrateRatio = [i['vibrateRatio'] if 'vibrateRatio' in i else None for i in ticker]
        self.pchange = [i['pchange'] if 'pchange' in i else None for i in ticker]
        self.pchRatio = [i['pchRatio'] if 'pchRatio' in i else None for i in ticker]
        self.pprice = [i['pprice'] if 'pprice' in i else None for i in ticker]
        self.data_dict = {
            'tickerId': self.tickerId,
            'exchangeId': self.exchangeId,
            'type': self.type,
            'secType': self.secType,
            'regionId': self.regionId,
            'currencyId': self.currencyId,
            'currencyCode': self.currencyCode,
            'name': self.name,
            'symbol': self.symbol,
            'disSymbol': self.disSymbol,
            'disExchangeCode': self.disExchangeCode,
            'exchangeCode': self.exchangeCode,
            'listStatus': self.listStatus,
            'template': self.template,
            'derivativeSupport': self.derivativeSupport,
            'isPTP': self.isPTP,
            'tradeTime': self.tradeTime,
            'faTradeTime': self.faTradeTime,
            'status': self.status,
            'close': self.close,
            'change': self.change,
            'changeRatio': self.changeRatio,
            'marketValue': self.marketValue,
            'volume': self.volume,
            'regionName': self.regionName,
            'regionIsoCode': self.regionIsoCode,
            'peTtm': self.peTtm,
            'preClose': self.preClose,
            'fiftyTwoWkHigh': self.fiftyTwoWkHigh,
            'fiftyTwoWkLow': self.fiftyTwoWkLow,
            'open': self.open,
            'high': self.high,
            'low': self.low,
            'vibrateRatio': self.vibrateRatio,
            'pchange': self.pchange,
            'pchRatio': self.pchRatio,
            'pprice': self.pprice
        }

        self.df = pd.DataFrame(self.data_dict)

