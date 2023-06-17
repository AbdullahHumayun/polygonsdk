from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class ForexSnapshot:

    ticker: list
    change: list
    change_percent: list
    day_open: list
    day_high: list
    day_low: list
    day_close: list
    day_volume: list
    day_vwap: list
    ask: list
    bid: list
    timestamp: list
    exchange: list
    min_open: list
    min_high: list
    min_low: list
    min_close: list
    min_volume: list
    prev_open: list
    prev_high: list
    prev_low: list
    prev_close: list
    prev_volume: list
    prev_vwap: list

    def __init__(self, tickers):

        self.ticker = [i['ticker'] if i['ticker'] is not None else None for i in tickers]
        self.change = [i['todaysChange'] if i['todaysChange'] is not None else None for i in tickers]
        self.change_percent = [i['todaysChangePerc'] if i['todaysChangePerc'] is not None else None for i in tickers]
        day = [i['day'] if i['day'] is not None else None for i in tickers]
        self.day_open = [i['o'] if i['o'] is not None else None for i in day]
        self.day_high = [i['h'] if i['h'] is not None else None for i in day]
        self.day_low = [i['l'] if i['l'] is not None else None for i in day]
        self.day_close = [i['c'] if i['c'] is not None else None for i in day]
        self.day_volume = [i['v'] if i['v'] is not None else None for i in day]
        self.day_vwap = [i['vw'] if i['vw'] is not None else None for i in day]
        last_quote = [i['lastQuote'] if i['lastQuote'] is not None else None for i in tickers]
        self.ask = [i['a'] if i['a'] is not None else None for i in last_quote]
        self.bid = [i['b'] if i['b'] is not None else None for i in last_quote]
        self.timestamp = [i['t'] if i['t'] is not None else None for i in last_quote]
        self.exchange = [i['x'] if i['x'] is not None else None for i in last_quote]
        minute_data = [i['min'] if i['min'] is not None else None for i in tickers]
        self.min_open = [i['o'] if i['o'] is not None else None for i in minute_data]
        self.min_high = [i['h'] if i['h'] is not None else None for i in minute_data]
        self.min_low = [i['l'] if i['l'] is not None else None for i in minute_data]
        self.min_close = [i['c'] if i['c'] is not None else None for i in minute_data]
        self.min_volume = [i['v'] if i['v'] is not None else None for i in minute_data]
        prev_day_data = [i['prevDay'] if i['prevDay'] is not None else None for i in tickers]
        self.prev_open = [i['o'] if i['o'] is not None else None for i in prev_day_data]
        self.prev_high = [i['h'] if i['h'] is not None else None for i in prev_day_data]
        self.prev_low = [i['l'] if i['l'] is not None else None for i in prev_day_data]
        self.prev_close = [i['c'] if i['c'] is not None else None for i in prev_day_data]
        self.prev_volume = [i['v'] if i['v'] is not None else None for i in prev_day_data]
        self.prev_vwap = [i['vw'] if i['vw'] is not None else None for i in prev_day_data]

    def to_dict(self) -> Dict[str, Any]:
        return {slot: getattr(self, slot) for slot in self.__slots__}
@dataclass
class CryptoSnapshot:

    ticker: list
    change: list
    change_percent: list
    day_open: list
    day_high: list
    day_low: list
    day_close: list
    day_volume: list
    day_vwap: list
    last_trade_conditions: list
    last_trade_id: list
    last_trade_price: list
    last_trade_size: list
    last_trade_exchange: list
    last_trade_timestamp: list
    min_open: list
    min_high: list
    min_low: list
    min_close: list
    min_volume: list
    prev_open: list
    prev_high: list
    prev_low: list
    prev_close: list
    prev_volume: list
    prev_vwap: list

    def __init__(self, tickers):
        self.ticker = [i['ticker'] if i['ticker'] is not None else None for i in tickers]
        self.change = [i['todaysChange'] if i['todaysChange'] is not None else None for i in tickers]
        self.change_percent = [i['todaysChangePerc'] if i['todaysChangePerc'] is not None else None for i in tickers]
        day = [i['day'] if i['day'] is not None else None for i in tickers]
        self.day_open = [i['o'] if i['o'] is not None else None for i in day]
        self.day_high = [i['h'] if i['h'] is not None else None for i in day]
        self.day_low = [i['l'] if i['l'] is not None else None for i in day]
        self.day_close = [i['c'] if i['c'] is not None else None for i in day]
        self.day_volume = [i['v'] if i['v'] is not None else None for i in day]
        self.day_vwap = [i['vw'] if i['vw'] is not None else None for i in day]
        last_trade = [i['lastTrade'] if i['lastTrade'] is not None else None for i in tickers]
        self.last_trade_conditions = [last_trade.get('c', None) if last_trade is not None else None for last_trade in last_trade]
        self.last_trade_id = [i['i'] if 'i' in i and i['i'] is not None else None for i in last_trade]
        self.last_trade_price = [i['p'] if 'p' in i and i['p'] is not None else None for i in last_trade]
        self.last_trade_size = [i['s'] if 's' in i and i['s'] is not None else None for i in last_trade]
        self.last_trade_exchange = [i['x'] if 'x' in i and i['x'] is not None else None for i in last_trade]
        self.last_trade_timestamp = [i['t'] if 't' in i and i['t'] is not None else None for i in last_trade]
        minute_data = [i['min'] if i['min'] is not None else None for i in tickers]
        self.min_open = [i['o'] if i['o'] is not None else None for i in minute_data]
        self.min_high = [i['h'] if i['h'] is not None else None for i in minute_data]
        self.min_low = [i['l'] if i['l'] is not None else None for i in minute_data]
        self.min_close = [i['c'] if i['c'] is not None else None for i in minute_data]
        self.min_volume = [i['v'] if i['v'] is not None else None for i in minute_data]
        prev_day_data = [i['prevDay'] if i['prevDay'] is not None else None for i in tickers]
        self.prev_open = [i['o'] if i['o'] is not None else None for i in prev_day_data]
        self.prev_high = [i['h'] if i['h'] is not None else None for i in prev_day_data]
        self.prev_low = [i['l'] if i['l'] is not None else None for i in prev_day_data]
        self.prev_close = [i['c'] if i['c'] is not None else None for i in prev_day_data]
        self.prev_volume = [i['v'] if i['v'] is not None else None for i in prev_day_data]
        self.prev_vwap = [i['vw'] if i['vw'] is not None else None for i in prev_day_data]

    def to_dict(self) -> Dict[str, Any]:
        return {slot: getattr(self, slot) for slot in self.__slots__}