import pandas as pd


class UniversalSnapshot:
    def __init__(self, results):
        session = [i['session'] if i['session'] is not None else None for i in results]
        self.change = [i['change'] if 'change' in i else None for i in session]
        self.change_percent = [i['change_percent'] if 'change_percent' in i else None for i in session]
        self.early_trading_change = [i['early_trading_change'] if 'early_trading_change' in i else None for i in session]
        self.early_trading_change_percent = [i['early_trading_change_percent'] if 'early_trading_change_percent' in i else None for i in session]
        self.close = [i['close'] if 'close' in i else None for i in session]
        self.high = [i['high'] if 'high' in i else None for i in session]
        self.low = [i['low'] if 'low' in i else None for i in session]
        self.open = [i['open'] if 'open' in i else None for i in session]
        self.volume =[i['volume'] if 'volume' in i else None for i in session]
        self.prev_close = [i['previous_close'] if 'previous_close' in i else None for i in session]

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

        
        self.implied_volatility = [i['implied_volatility'] if 'implied_volatility' in i else None for i in results]
        self.open_interest = [i['open_interest'] if i['open_interest'] is not None else None for i in results]
        

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
        


        self.name = [i.get('name') for i in results]
        self.market_status = [i.get('market_status') for i in results]
        self.ticker = [i.get('ticker') for i in results]
        self.type = [i.get('type') for i in results]

        underlying_asset = [i['underlying_asset'] if i['underlying_asset'] is not None else None for i in results]
        self.change_to_breakeven = [i['change_to_break_even'] if 'change_to_break_even' in i else None for i in underlying_asset]
        self.underlying_ticker = [i['ticker'] if 'ticker' in i else None for i in underlying_asset]
        if self.underlying_ticker[0] == "I:SPX":

            self.underlying_price = [i['value'] if 'value' in i else None for i in underlying_asset]
        else:
            self.underlying_price = [i['price'] if 'price' in i else None for i in underlying_asset]





        self.data_dict = {
            'Change %': self.change_percent,
            'Early Trading Change': self.early_trading_change,
            'Early Trading Change Percent': self.early_trading_change_percent,
            'Close': self.close,
            'High': self.high,
            'Low': self.low,
            'Open': self.open,
            'Vol': self.volume,
            'Previous Close': self.prev_close,
            'C/P': self.contract_type,
            'Exercise Style': self.exercise_style,
            '🗓️': self.expiry,
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
            'Midpoint': self.midpoint,
            'Last Trade Sip Timestamp': self.sip_timestamp,
            'Last Trade Conditions': self.conditions,
            'Last Trade Price': self.trade_price,
            'Size': self.trade_size,
            'Last Trade Exchange': self.exchange,
            'OI': self.open_interest,
            '💲': self.underlying_price,
            'Sym': self.underlying_ticker,
            'Name': self.name,
            'Market Status': self.market_status,
            'Ticker': self.ticker,
            'Types': self.type,
        }
        self.df = pd.DataFrame(self.data_dict).sort_values('IV', ascending=False)

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
        self.break_even = [i['break_even_price'] if 'break_even_price' in i else None for i in results]
        self.implied_volatility = [i['implied_volatility'] if 'implied_volatility' in i else None for i in results] 
        self.open_interest = [i['open_interest'] if 'open_interest' in i else None for i in results]

        day = [i['day'] if i['day'] is not None else None for i in results]
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
            'mid': self.midpoint,
            'change_to_breakeven': self.change_to_breakeven,
            'price': self.underlying_price,
            'sym': self.underlying_ticker
        }

        self.df = pd.DataFrame(self.data_dict)
    def __repr__(self) -> str:
        return f"UniversalOptionSnapshot(break_even={self.break_even}, \
                implied_volatility={self.implied_volatility},\
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
