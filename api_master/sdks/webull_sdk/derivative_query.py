import pandas as pd

class QueryDerivatives:
    def __init__(self, option_data):
        self.open = option_data.get('open')
        self.high = option_data.get('high')
        self.low = option_data.get('low')
        self.strikePrice = option_data.get('strikePrice')
        self.isStdSettle = option_data.get('isStdSettle')
        self.preClose = option_data.get('preClose')
        self.openInterest = option_data.get('openInterest')
        self.volume = option_data.get('volume')
        self.latestPriceVol = option_data.get('latestPriceVol')
        self.delta = option_data.get('delta')
        self.vega = option_data.get('vega')
        self.impVol = option_data.get('impVol')
        self.gamma = option_data.get('gamma')
        self.theta = option_data.get('theta')
        self.rho = option_data.get('rho')
        self.close = option_data.get('close')
        self.change = option_data.get('change')
        self.changeRatio = option_data.get('changeRatio')
        self.expireDate = option_data.get('expireDate')
        self.tickerId = option_data.get('tickerId')
        self.belongTickerId = option_data.get('belongTickerId')
        self.openIntChange = option_data.get('openIntChange')
        self.activeLevel = option_data.get('activeLevel')
        self.cycle = option_data.get('cycle')
        self.weekly = option_data.get('weekly')
        self.executionType = option_data.get('executionType')
        self.direction = option_data.get('direction')
        self.derivativeStatus = option_data.get('derivativeStatus')
        self.currencyId = option_data.get('currencyId')
        self.regionId = option_data.get('regionId')
        self.exchangeId = option_data.get('exchangeId')
        self.symbol = option_data.get('symbol')
        self.unSymbol = option_data.get('unSymbol')
        self.askList = option_data.get('askList')
        self.bidList = option_data.get('bidList')
        self.quoteMultiplier = option_data.get('quoteMultiplier')
        self.quoteLotSize = option_data.get('quoteLotSize')
        self.tradeTime = option_data.get('tradeTime')
        self.timeZone = option_data.get('timeZone')
        self.tzName = option_data.get('tzName')
        self.tradeStatus = option_data.get('tradeStatus')
        self.tradeStamp = option_data.get('tradeStamp')


        self.data_dict = {
            'open': self.open,
            'high': self.high,
            'low': self.low,
            'strikePrice': self.strikePrice,
            'preClose': self.preClose,
            'openInterest': self.openInterest,
            'volume': self.volume,
            'latestPriceVol': self.latestPriceVol,
            'delta': self.delta,
            'vega': self.vega,
            'impVol': self.impVol,
            'gamma': self.gamma,
            'theta': self.theta,
            'rho': self.rho,
            'close': self.close,
            'change': self.change,
            'changeRatio': self.changeRatio,
            'expireDate': self.expireDate,
            'tickerId': self.tickerId,
            'belongTickerId': self.belongTickerId,
            'openIntChange': self.openIntChange,
            'activeLevel': self.activeLevel,
            'executionType': self.executionType,
            'direction': self.direction,
            'symbol': self.symbol,
            'unSymbol': self.unSymbol,
            'askList': self.askList,
            'bidList': self.bidList,
        }

        self.df = pd.DataFrame(self.data_dict)