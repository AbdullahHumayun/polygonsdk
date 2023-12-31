import pandas as pd

class ETFCommodity:
    def __init__(self, tabs_data, ticker_data):
        self.ticker_id = ticker_data.get('tickerId')
        self.exchange_id = ticker_data.get('exchangeId')
        self.type = ticker_data.get('type')
        self.sec_type = ticker_data.get('secType')
        self.region_id = ticker_data.get('regionId')
        self.currency_id = ticker_data.get('currencyId')
        self.currency_code = ticker_data.get('currencyCode')
        self.name = ticker_data.get('name')
        self.symbol = ticker_data.get('symbol')
        self.display_symbol = ticker_data.get('disSymbol')
        self.display_exchange_code = ticker_data.get('disExchangeCode')
        self.exchange_code = ticker_data.get('exchangeCode')
        self.list_status = ticker_data.get('listStatus')
        self.template = ticker_data.get('template')
        self.exchange_trade = ticker_data.get('exchangeTrade')
        self.derivative_support = ticker_data.get('derivativeSupport')
        self.is_ptp = ticker_data.get('isPTP')
        self.asset_type = ticker_data.get('assetType')
        self.trade_time = ticker_data.get('tradeTime')
        self.fa_trade_time = ticker_data.get('faTradeTime')
        self.status = ticker_data.get('status')
        self.close = ticker_data.get('close')
        self.change = ticker_data.get('change')
        self.change_ratio = ticker_data.get('changeRatio')
        self.volume = ticker_data.get('volume')
        self.net_asset = ticker_data.get('netAsset')
        self.total_asset = ticker_data.get('totalAsset')
        self.region_name = ticker_data.get('regionName')
        self.region_iso_code = ticker_data.get('regionIsoCode')
        self.pe_ttm = ticker_data.get('peTtm')
        self.pre_close = ticker_data.get('preClose')
        self.fifty_two_wk_high = ticker_data.get('fiftyTwoWkHigh')
        self.fifty_two_wk_low = ticker_data.get('fiftyTwoWkLow')
        self.open = ticker_data.get('open')
        self.high = ticker_data.get('high')
        self.low = ticker_data.get('low')
        self.vibrate_ratio = ticker_data.get('vibrateRatio')
        self.pchange = ticker_data.get('pchange')
        self.up_num = tabs_data.get('upNum')
        self.down_num = tabs_data.get('dowoNum')
        self.flat_num = tabs_data.get('flatNum')


        self.data_dict = {
        'name': self.name,
        'symbol': self.symbol,
        'close': self.close,
        'change': self.change,
        'change_ratio': self.change_ratio,
        'volume': self.volume,
        'net_asset': self.net_asset,
        'total_asset': self.total_asset,
        'pe_ttm': self.pe_ttm,
        'pre_close': self.pre_close,
        'fifty_two_wk_high': self.fifty_two_wk_high,
        'fifty_two_wk_low': self.fifty_two_wk_low,
        'open': self.open,
        'high': self.high,
        'low': self.low,
        'vibrate_ratio': self.vibrate_ratio,
        'pchange': self.pchange,
        'up_num': self.up_num,
        'down_num': self.down_num,
        'flat_num': self.flat_num

        }
        

        self.df = pd.DataFrame(self.data_dict)
    def __repr__(self):
        return f"<ETFObject: {self.name[0]} ({self.symbol[0]})>"
