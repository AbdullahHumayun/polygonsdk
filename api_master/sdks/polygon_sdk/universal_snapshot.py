import pandas as pd
from datetime import datetime

indices_list = ["SPX", "SPXW", "NDX", "VIX", "VVIX"]

class UniversalSnapshot:
    def __init__(self, results):
        session = [i['session'] if i is not None and 'session' in i else None for i in results]
        self.change = [i['change'] if i is not None and 'change' in i else None for i in session]
        self.change_percent = [i['change_percent'] if i is not None and 'change_percent' in i else None for i in session]
        self.early_trading_change = [i['early_trading_change'] if i is not None and 'early_trading_change' in i else None for i in session]
        self.early_trading_change_percent = [i['early_trading_change_percent'] if i is not None and 'early_trading_change_percent' in i else None for i in session]
        self.close = [i['close'] if i is not None and 'close' in i else None for i in session]
        self.high = [i['high'] if i is not None and 'high' in i else None for i in session]
        self.low = [i['low'] if i is not None and 'low' in i else None for i in session]
        self.open = [i['open'] if i is not None and 'open' in i else None for i in session]
        self.volume =[i['volume'] if i is not None and 'volume' in i else None for i in session]
        self.prev_close = [i['previous_close'] if i is not None and 'previous_close' in i else None for i in session]

        details = [i['details'] if i is not None and 'details' in i else None for i in results]
        self.strike = [i['strike_price'] if i is not None and 'strike_price' in i else None for i in details]
        self.expiry = [i['expiration_date'] if i is not None and 'expiration_date' in i else None for i in details]
        self.contract_type = [i['contract_type'] if i is not None and 'contract_type' in i else None for i in details]
        self.exercise_style = [i['exercise_style'] if i is not None and 'exercise_style' in i else None for i in details]
        self.ticker = [i['ticker'] if i is not None and 'ticker' in i else None for i in details]

        greeks = [i['greeks'] if i is not None and 'greeks' in i else None for i in results]
        self.theta = [i['theta'] if i is not None and 'theta' in i else None for i in greeks]
        self.delta = [i['delta'] if i is not None and 'delta' in i else None for i in greeks]
        self.gamma = [i['gamma'] if i is not None and 'gamma' in i else None for i in greeks]
        self.vega = [i['vega'] if i is not None and 'vega' in i else None for i in greeks]

        
        self.implied_volatility = [i['implied_volatility'] if i is not None and 'implied_volatility' in i else None for i in results]
        self.open_interest = [i['open_interest'] if i is not None and 'open_interest' in i else None for i in results]

        last_trade = [i['last_trade'] if i is not None and 'last_trade' in i else None for i in results]
        self.sip_timestamp = [i['sip_timestamp'] if i is not None and 'sip_timestamp' in i else None for i in last_trade]
        self.conditions = [i['conditions'] if i is not None and 'conditions' in i else None for i in last_trade]
        self.trade_price = [i['price'] if i is not None and 'price' in i else None for i in last_trade]
        self.trade_size = [i['size'] if i is not None and 'size' in i else None for i in last_trade]
        self.exchange = [i['exchange'] if i is not None and 'exchange' in i else None for i in last_trade]

        last_quote = [i['last_quote'] if i is not None and 'last_quote' in i else None for i in results]
        self.ask = [i['ask'] if i is not None and 'ask' in i else None for i in last_quote]
        self.bid = [i['bid'] if i is not None and 'bid' in i else None for i in last_quote]
        self.bid_size = [i['bid_size'] if i is not None and 'bid_size' in i else None for i in last_quote]
        self.ask_size = [i['ask_size'] if i is not None and 'ask_size' in i else None for i in last_quote]
        self.midpoint = [i['midpoint'] if i is not None and 'midpoint' in i else None for i in last_quote]

        self.name = [i.get('name') if i is not None else None for i in results]
        self.market_status = [i.get('market_status') if i is not None else None for i in results]
        self.ticker = [i.get('ticker') if i is not None else None for i in results]
        self.type = [i.get('type') if i is not None else None for i in results]

        underlying_asset = [i['underlying_asset'] if i is not None and 'underlying_asset' in i else None for i in results]
        self.change_to_breakeven = [i['change_to_break_even'] if i is not None and 'change_to_break_even' in i else None for i in underlying_asset]
        self.underlying_ticker = [i['ticker'] if i is not None and 'ticker' in i else None for i in underlying_asset]
        if self.underlying_ticker in indices_list:
            self.underlying_price = [i['value'] if i is not None and 'value' in i else None for i in underlying_asset]
        else:
            self.underlying_price = [i['price'] if i is not None and 'price' in i else None for i in underlying_asset]





        self.data_dict = {
            'Change %': self.change_percent,
            'Close': self.close,
            'High': self.high,
            'Low': self.low,
            'Open': self.open,
            'Vol': self.volume,
            'Prev Close': self.prev_close,
            'C/P': self.contract_type,
            'Style': self.exercise_style,
            'Exp': self.expiry,
            'Skew': self.strike,
            'Strike': self.strike,
            'Delta': self.delta,
            'Gamma': self.gamma,
            'Theta': self.theta,
            'Vega': self.vega,
            'IV': self.implied_volatility,
            'Ask': self.ask,
            'Ask Size': self.ask_size,
            'Bid': self.bid,
            'Bid Size': self.bid_size,
            'Mid': self.midpoint,
            'Timestamp': self.sip_timestamp,
            'Conditions': self.conditions,
            'Trade Price': self.trade_price,
            'Size': self.trade_size,
            'Exchange': self.exchange,
            'OI': self.open_interest,
            'Price': self.underlying_price,
            'Sym': self.underlying_ticker,
            'Name': self.name,
            'Ticker': self.ticker,
            'Types': self.type,
        }



        self.skew_dict = { 
            'C/P': self.contract_type,
            'iv': self.implied_volatility,
            'exp': self.expiry,
            'vol': self.volume,
            'oi': self.open_interest,
            'strike': self.strike,
}
        self.df = pd.DataFrame(self.data_dict)

        self.skew_df = pd.DataFrame(self.skew_dict)

    def __getitem__(self, index):
        return self.df[index]

    def __setitem__(self, index, value):
        self.df[index] = value
    def __iter__(self):
        # If df is a DataFrame, it's already iterable (over its column labels)
        # To iterate over rows, use itertuples or iterrows
        self.iter = self.df.itertuples()
        return self

    def __next__(self):
        # Just return the next value from the DataFrame iterator
        try:
            return next(self.iter)
        except StopIteration:
            # When there are no more rows, stop iteration
            raise StopIteration
class UniversalOptionSnapshot:
    def __init__(self, results):
        self.break_even = [i['break_even_price'] if 'break_even_price' is not None and 'break_even_price' in i else None for i in results]
        self.implied_volatility = [i['implied_volatility'] if 'implied_volatility' in i else None for i in results] 
        self.open_interest = [i['open_interest'] if 'open_interest' in i else None for i in results]

        day = [i['day'] if 'day' is not None else None for i in results]
        self.volume = [i['volume'] if 'volume' in i  else None for i in day]
        self.high = [i['high'] if 'high' in i else None for i in day]
        self.low = [i['low'] if 'low' in i else None for i in day]
        self.vwap = [i['vwap'] if 'vwap' in i else None for i in day]
        self.open = [i['open'] if 'open' in i else None for i in day]
        self.close = [i['close'] if 'close' in i else None for i in day]




        details = [i['details'] for i in results]
        self.strike = [i['strike_price'] if 'strike_price' in i else None for i in details]
        self.expiry = [i['expiration_date'] if 'expiration_date' in i else None for i in details]
        self.contract_type = [i['contract_type'] if 'contract_type' in i else None for i in details]
        self.exercise_style = [i['exercise_style'] if 'exercise_style' in i else None for i in details]
        self.ticker = [i['ticker'] if 'ticker' in i else None for i in details]

        greeks = [i['greeks'] if i['greeks'] is not None else None for i in results]
        self.theta = [i['theta'] if 'theta' in i else None for i in greeks]
        self.delta = [i['delta'] if 'delta' in i else None for i in greeks]
        self.gamma = [i['gamma'] if 'gamma' in i else None for i in greeks]
        self.vega = [i['vega'] if 'vega' in i else None for i in greeks]


        last_trade = [i['last_trade'] if i['last_trade'] is not None else None for i in results]
        self.sip_timestamp = [i['sip_timestamp'] if 'sip_timestamp' in i else None for i in last_trade]
        self.conditions = [i['conditions'] if 'conditions' in i else None for i in last_trade]
        self.trade_price = [i['price'] if 'price' in i else None for i in last_trade]
        self.trade_size = [i['size'] if 'size' in i else None for i in last_trade]
        self.exchange = [i['exchange'] if 'exchange' in i else None for i in last_trade]

        last_quote = [i['last_quote'] if i['last_quote'] is not None else None for i in results]
        self.ask = [i['ask'] if 'ask' in i else None for i in last_quote]
        self.bid = [i['bid'] if 'bid' in i else None for i in last_quote]
        self.bid_size = [i['bid_size'] if 'bid_size' in i else None for i in last_quote]
        self.ask_size = [i['ask_size'] if 'ask_size' in i else None for i in last_quote]
        self.midpoint = [i['midpoint'] if 'midpoint' in i else None for i in last_quote]


        underlying_asset = [i['underlying_asset'] if i['underlying_asset'] is not None else None for i in results]
        self.change_to_breakeven = [i['change_to_break_even'] if 'change_to_break_even' in i else None for i in underlying_asset]
        self.underlying_price = [i['price'] if 'price' in i else None for i in underlying_asset]
        self.underlying_ticker = [i['ticker'] if 'ticker' in i else None for i in underlying_asset]

        self.data_dict = {
            'strike': self.strike,
            'exp': self.expiry,
            'C/P': self.contract_type,
            'exercise_style': self.exercise_style,
            'ticker': self.ticker,
            'theta': self.theta,
            'delta': self.delta,
            'gamma': self.gamma,
            'vega': self.vega,
            'timestamp': self.sip_timestamp,
            'OI': self.open_interest,
            'open': self.open,
            'high': self.high,
            'low': self.low,
            'close': self.close,
            'vwap':self.vwap,
            'conditions': self.conditions,
            'price': self.trade_price,
            'Size': self.trade_size,
            'exchange': self.exchange,
            'ask': self.ask,
            'bid': self.bid,
            'IV': self.implied_volatility,
            'bid_size': self.bid_size,
            'ask_size': self.ask_size,
            'vol': self.volume,
            'entryCost': self.midpoint,
            'change_to_breakeven': self.change_to_breakeven,
            'price': self.underlying_price,
            'sym': self.underlying_ticker
        }


        # Create DataFrame from data_dict
        self.df = pd.DataFrame(self.data_dict)
    def __repr__(self) -> str:
        return f"UniversalOptionSnapshot(break_even={self.break_even}, \
                implied_volatility={self.implied_volatility},\
                open_interest ={self.open_interest}, \
                change={self.exchange}, \
                expiry={self.expiry}, \
                ticker={self.ticker} \
                contract_type={self.contract_type}, \
                exercise_style={self.exercise_style}, \
                theta={self.theta}, \
                delta={self.delta}, \
                gamma={self.gamma}, \
                vega={self.vega}, \
                sip_timestamp={self.sip_timestamp}, \
                conditions={self.conditions}, \
                trade_price={self.trade_price}, \
                trade_size={self.trade_size}, \
                exchange={self.exchange}, \
                ask={self.ask}, \
                bid={self.bid}, \
                bid_size={self.bid_size}, \
                ask_size={self.ask_size}, \
                midpoint={self.midpoint}, \
                change_to_breakeven={self.change_to_breakeven}, \
                underlying_price={self.underlying_price}, \
                underlying_ticker={self.underlying_ticker})"
    
    def __getitem__(self, index):
        return self.df[index]

    def __setitem__(self, index, value):
        self.df[index] = value
    def __iter__(self):
        # If df is a DataFrame, it's already iterable (over its column labels)
        # To iterate over rows, use itertuples or iterrows
        self.iter = self.df.itertuples()
        return self

    def __next__(self):
        # Just return the next value from the DataFrame iterator
        try:
            return next(self.iter)
        except StopIteration:
            # When there are no more rows, stop iteration
            raise StopIteration

class CallsOrPuts:
    def __init__(self, data):
        self.cfi = [i['cfi'] if 'cfi' in i else None for i in data]
        self.contract_type = [i['contract_type'] if 'contract_type' in i else None for i in data]
        self.exercise_style = [i['exercise_style'] if 'exercise_style' in i else None for i in data]
        self.expiration_date = [i['expiration_date'] if 'expiration_date' in i else None for i in data]
        self.primary_exchange = [i['primary_exchange'] if 'primary_exchange' in i else None for i in data]
        self.shares_per_contract = [i['shares_per_contract'] if 'shares_per_contract' in i else None for i in data]
        self.strike_price = [i['strike_price'] if 'strike_price' in i else None for i in data]
        self.ticker = [i['ticker'] if 'ticker' in i else None for i in data]
        self.underlying_ticker = [i['underlying_ticker'] if 'underlying_ticker' in i else None for i in data]


        self.data_dict = { 
            'ticker': self.ticker,
            'strike': self.strike_price,
            'expiry': self.expiration_date

        }


        self.df = pd.DataFrame(self.data_dict).sort_values(by='expiry')

class MultipleUniversalOptionSnapshot:
    def __init__(self, results):
        self.break_even = results.get('break_even_price', None)
        print(self.break_even)
        self.implied_volatility = results.get('implied_volatility', None)
        self.open_interest = results.get('open_interest', None)

        day = results.get('day', None)
        self.volume = day.get('volume', None)
        self.high = day.get('high', None)
        self.low = day.get('low', None)
        self.vwap = day.get('vwap', None)
        self.open = day.get('open', None)
        self.close = day.get('close', None)




        details = results.get('details', None)
        self.strike = details.get('strike_price', None)
        self.expiry =  details.get('expiration_date', None)
        self.contract_type =  details.get('contract_type', None)
        self.exercise_style =  details.get('exercise_style', None)
        self.ticker =  details.get('ticker', None)

        greeks = results.get('greeks', None)
        self.theta = greeks.get('theta', None)
        self.delta = greeks.get('delta', None)
        self.gamma = greeks.get('gamma', None)
        self.vega = greeks.get('vega', None)


        last_trade = results.get('last_trade', None)
        self.sip_timestamp = last_trade.get('sip_timestamp', None)
        self.conditions = last_trade.get('conditions', None)
        self.trade_price = last_trade.get('price', None)
        self.trade_size = last_trade.get('size', None)
        self.exchange = last_trade.get('exchange', None)

        last_quote = results.get('last_quote', None)
        self.ask = last_quote.get('ask', None)
        self.bid = last_quote.get('bid', None)
        self.bid_size = last_quote.get('bid_size', None)
        self.ask_size = last_quote.get('ask_size', None)
        self.midpoint = last_quote.get('midpoint', None)


        underlying_asset = results.get('underlying_asset', None)
        self.change_to_breakeven = underlying_asset.get('change_to_breakeven', None)
        self.underlying_price = underlying_asset.get('underlying_price', None)
        self.underlying_ticker = underlying_asset.get('underlying_ticker', None)

        self.data_dict = {
            'strike': self.strike,
            'exp': self.expiry,
            'type': self.contract_type,
            'exercise_style': self.exercise_style,
            'ticker': self.ticker,
            'theta': self.theta,
            'delta': self.delta,
            'gamma': self.gamma,
            'vega': self.vega,
            'sip_timestamp': self.sip_timestamp,
            'open': self.open,
            'high': self.high,
            'low': self.low,
            'close': self.close,
            'vwap':self.vwap,
            'conditions': self.conditions,
            'price': self.trade_price,
            'Size': self.trade_size,
            'exchange': self.exchange,
            'ask': self.ask,
            'bid': self.bid,
            'IV': self.implied_volatility,
            'bid_size': self.bid_size,
            'ask_size': self.ask_size,
            'vol': self.volume,
            'entryCost': self.midpoint,
            'change_to_breakeven': self.change_to_breakeven,
            'price': self.underlying_price,
            'sym': self.underlying_ticker
        }

        self.df = pd.DataFrame(self.data_dict)