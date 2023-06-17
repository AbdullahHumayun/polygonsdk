from typing import Dict, Any

class OptionSnapshotData:
    __slots__ = ['option_symbol', 'strike_price', 'contract_type', 'expiration_date', 'exercise_style', 'shares_per_contract', 'break_even_price',
                 'day_close', 'day_change_percent', 'day_change', 'day_high', 'day_low', 'day_open', 'day_volume', 'day_vwap', 'last_updated', 'previous_close', 
                 'delta', 'gamma', 'theta', 'vega', 'implied_volatility', 'open_interest',
                 'ask', 'ask_size', 'bid', 'bid_size', 'quote_last_updated', 'midpoint',
                 'conditions', 'exchange', 'price', 'sip_timestamp', 'size',
                 'change_to_break_even', 'underlying_last_updated', 'underlying_price', 'underlying_ticker',]

    def __init__(self, data):

        self.implied_volatility = data.get("implied_volatility")
        self.open_interest = data.get("open_interest")
        self.break_even_price = data.get("break_even_price")

        day = data.get('day')
        self.day_close = day.get("close")
        self.day_high = day.get("high")
        self.last_updated = day.get("last_updated")
        self.day_low = day.get("low")
        self.day_open = day.get("open")
        self.day_change_percent = day.get('change_percent')
        self.day_change = day.get('change')
        self.previous_close = day.get("previous_close")
        self.day_volume = day.get("volume")
        self.day_vwap = day.get("vwap")
        

        details = data.get('details')
        self.contract_type = details.get("contract_type")
        self.exercise_style = details.get("exercise_style")
        self.expiration_date = details.get("expiration_date")
        self.shares_per_contract = details.get("shares_per_contract")
        self.strike_price = details.get("strike_price")
        self.option_symbol = details.get("ticker")

        greeks = data.get('greeks')
        self.delta = greeks.get("delta")
        self.gamma = greeks.get("gamma")
        self.theta = greeks.get("theta")
        self.vega = greeks.get("vega")
        

        lastquote = data.get('last_quote')
        self.ask = lastquote.get("ask")
        self.ask_size = lastquote.get("ask_size")
        self.bid = lastquote.get("bid")
        self.bid_size = lastquote.get("bid_size")
        self.quote_last_updated = lastquote.get("last_updated")
        self.midpoint = lastquote.get("midpoint")

        lasttrade = data.get('last_trade')
        self.conditions = lasttrade.get("conditions")
        self.exchange = lasttrade.get("exchange")
        self.price = lasttrade.get("price")
        self.sip_timestamp = lasttrade.get("sip_timestamp")
        self.size = lasttrade.get("size")

        underlying = data.get('underlying_asset')
        self.change_to_break_even = underlying.get("change_to_break_even")
        self.underlying_last_updated = underlying.get("last_updated")
        self.underlying_price = underlying.get("price")
        self.underlying_ticker = underlying.get("ticker")
    def to_dict(self):
        return {slot: getattr(self, slot) for slot in self.__slots__}