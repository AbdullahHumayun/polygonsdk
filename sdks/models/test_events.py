from typing import Optional, Union, List, NewType, Dict, Any
from .common import EventType
from dataclasses import dataclass
from datetime import datetime
import pandas as pd
from typing import Optional, Union, List, NewType, Dict, Any
from .common import EventType
from dataclasses import dataclass
from datetime import datetime
option_condition_dict = {
    201: 'Canceled',
    202: 'Late and Out Of Sequence',
    203: 'Last and Canceled',
    204: 'Late',
    205: 'Opening Trade and Canceled',
    206: 'Opening Trade, Late, and Out Of Sequence',
    207: 'Only Trade and Canceled',
    208: 'Opening Trade and Late',
    209: 'Automatic Execution',
    210: 'Reopening Trade',
    219: 'Intermarket Sweep Order',
    227: 'Single Leg Auction Non ISO',
    228: 'Single Leg Auction ISO',
    229: 'Single Leg Cross Non ISO',
    230: 'Single Leg Cross ISO',
    231: 'Single Leg Floor Trade',
    232: 'Multi Leg auto-electronic trade',
    233: 'Multi Leg Auction',
    234: 'Multi Leg Cross',
    235: 'Multi Leg floor trade',
    236: 'Multi Leg auto-electronic trade against single leg(s)',
    237: 'Stock Options Auction',
    238: 'Multi Leg Auction against single leg(s)',
    239: 'Multi Leg floor trade against single leg(s)',
    240: 'Stock Options auto-electronic trade',
    241: 'Stock Options Cross',
    242: 'Stock Options floor trade',
    243: 'Stock Options auto-electronic trade against single leg(s)',
    244: 'Stock Options Auction against single leg(s)',
    245: 'Stock Options floor trade against single leg(s)',
    246: 'Multi Leg Floor Trade of Proprietary Products',
    247: 'Multilateral Compression Trade of Proprietary Products',
    248: 'Extended Hours Trade',
}
CRYPTO_TRADE_CONDITIONS = {
    0: "Regular Trade",
    1: "Sell Side",
    2: "Buy Side",
}

OPTIONS_EXCHANGES = { 
    300:'NYSE American Options',
    301:'Boston Options Exchange',
    302:'Chicago Board Options Exchange',
    303:'MIAX Emerald, LLC',
    304:'Cboe EDGX Options',
    307:'Nasdaq Global Markets Exchange Group',
    308:'International Securities Exchange, LLC',
    309:'Nasdaq MRX Options Exchange',
    312:'MIAX International Securities Exchange, LLC',
    313:'NYSE Arca, Inc. - Options',
    314:'Options Price Reporting Authority',
    315:'MIAX Pearl, LLC - Options',
    316:'Nasdaq Options Market',
    319:'Nasdaq BX - Options',
    322:'Cboe C2 Options Exchange',
    323:'Nasdaq Philadelphia Exchange, LLC - Options',
    325:'Cboe BZX Options Exchange'}

STOCK_EXCHANGES = {
1:'NYSE American, LLC',
2:'Nasdaq OMX BX, Inc.',
3:'NYSE National, Inc.',
4:'FINRA NYSE TRF',
4:'FINRA Nasdaq TRF Carteret',
4:'FINRA Nasdaq TRF Chicago',
4:'FINRA Alternative Display Facility',
5:'Unlisted Trading Privileges',
6:'International Securities Exchange, LLC - Stocks',
7:'Cboe EDGA',
8:'Cboe EDGX',
9:'NYSE Chicago, Inc.',
10:'New York Stock Exchange',
11:'NYSE Arca, Inc.',
12:'Nasdaq',
13:'Consolidated Tape Association',
14:'Long-Term Stock Exchange',
15:'Investors Exchange',
16:'Cboe Stock Exchange',
17:'Nasdaq Philadelphia Exchange LLC',
18:'Cboe BYX',
19:'Cboe BZX',
20:'MIAX Pearl',
21:'Members Exchange',
62:'OTC Equity Security',    
 }

TAPES = {1: "NYSE", 2: "AMEX", 3: "Nasdaq"}

EQUITY_TRADE_CONDITIONS = {
    1: 'Acquisition',
    2: 'Average Price Trade',
    3: 'Automatic Execution',
    4: 'Bunched Trade',
    5: 'Bunched Sold Trade',
    6: 'CAP Election',
    7: 'Cash Sale',
    8: 'Closing Prints',
    9: 'Cross Trade',
    10: 'Derivatively Priced',
    11: 'Distribution',
    12: 'Form T/Extended Hours',
    13: 'Extended Hours (Sold Out Of Sequence)',
    14: 'Intermarket Sweep',
    15: 'Market Center Official Close',
    16: 'Market Center Official Open',
    17: 'Market Center Opening Trade',
    18: 'Market Center Reopening Trade',
    19: 'Market Center Closing Trade',
    20: 'Next Day',
    21: 'Price Variation Trade',
    22: 'Prior Reference Price',
    23: 'Rule 155 Trade (AMEX)',
    24: 'Rule 127 (NYSE Only)',
    25: 'Opening Prints',
    27: 'Stopped Stock (Regular Trade)',
    28: 'Re-Opening Prints',
    29: 'Seller',
    30: 'Sold Last',
    31: 'Sold Last and Stopped Stock',
    32: 'Sold (Out Of Sequence)',
    33: 'Sold (Out of Sequence) and Stopped Stock',
    34: 'Split Trade',
    35: 'Stock Option',
    36: 'Yellow Flag Regular Trade',
    37: 'Odd Lot Trade',
    38: 'Corrected Consolidated Close (per listing market)',
    41: 'Trade Thru Exempt',
    52: 'Contingent Trade',
    53: 'Qualified Contingent Trade',
    55: 'Opening Reopening Trade Detail',
    57: 'Short Sale Restriction Activated',
    58: 'Short Sale Restriction Continued',
    59: 'Short Sale Restriction Deactivated',
    60: 'Short Sale Restriction In Effect',
    62: 'Financial Status - Bankrupt',
    63: 'Financial Status - Deficient',
    64: 'Financial Status - Delinquent',
    65: 'Financial Status - Bankrupt and Deficient',
    66: 'Financial Status - Bankrupt and Delinquent',
    67: 'Financial Status - Deficient and Delinquent',
    68: 'Financial Status - Deficienft, Delinquent, and Bankrupt',
    69: 'Financial Status - Liquidation',
    70: 'Financial Status - Creations Suspended',
    71: 'Financial Status - Redemptions Suspended'}

EXCHANGE_MAPPING = {
    1: 'Coinbase',
    2: 'Bitfinex',
    6: 'Bitstamp',
    23: 'Kraken',
}


@dataclass
class TestStocksEvent:
    symbol: str
    close: float
    high: float
    low: float
    open: float
    volume: float
    vwap: float
    last_quote_ask_price: float
    last_quote_ask_size: int
    last_quote_bid_price: float
    last_quote_bid_size: int
    last_quote_timestamp: str
    last_trade_conditions: str

    last_exchange: str
    last_price: float
    last_size: int
    last_id: int
    last_trade_timestamp: str
    min_close: float
    min_high: float
    min_low: float
    min_open: float
    min_volume: float
    min_av: float
    min_vwap: float
    prev_vwap: float
    prev_close: float
    prev_high: float
    prev_low: float
    prev_open: float
    prev_volume: float
    today_change_percent: float
    today_change: float

    @classmethod
    def from_row(cls, row):
        return cls(
            symbol=row['Symbol'],
            today_change_percent=row['Change Percent'],
            today_change=row['Change'],
            open=row['Day Open'],
            close=row['Day Close'],
            high=row['Day High'],
            low=row['Day Low'],
            volume=row['Day Volume'],
            vwap=row['Day VWAP'],
            last_trade_conditions=EQUITY_TRADE_CONDITIONS.get(row["Last Trade Conditions"] if pd.notna(row["Last Trade Conditions"]) else ""),

            last_exchange=row['Last Trade Exchange'],
            last_price=row['Last Trade Price'],
            last_size=row['Last Trade Size'],
            last_trade_timestamp=row['Last Trade Timestamp'],
            last_id = row['Last Trade ID'],
            last_quote_bid_price=row['Last Quote Bid Price'],
            last_quote_ask_price=row['Last Quote Ask Price'],
            last_quote_ask_size=row['Last Quote Ask Size'],
            last_quote_bid_size=row['Last Quote Bid Size'],
            last_quote_timestamp=row['Last Quote Timestamp'],
            
            min_av = row['Minute Data Accumulated Volume'],
            min_volume=row['Minute Data Volume'],
            min_close=row['Minute Data Close'],
            min_open=row['Minute Data Open'],
            min_high=row['Minute Data High'],
            min_low=row['Minute Data Low'],
            min_vwap=row['Minute Data VWAP'],
            prev_open=row['Prev Day Open'],
            prev_close=row['Prev Day Close'],
            prev_high=row['Prev Day High'],
            prev_low=row['Prev Day Low'],
            prev_volume=row['Prev Day Volume'],
            prev_vwap=row['Prev Day VWAP'],

        )
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TestStocksEvent':
        return cls(**data)

@dataclass
class TestOptionsEvent:
    ticker: str
    break_even_price: float
    contract_type: str
    exercise_style: str
    expiration_date: str
    shares_per_contract: float
    strike_price: float
    delta: float
    gamma: float
    theta: float
    vega: float
    implied_volatility: float
    ask: float
    ask_size: int
    bid: float
    bid_size: int
    last_updated: str
    midpoint: float
    timeframe_quote: str
    last_trade_conditions: list
    last_trade_exchange: str
    last_trade_price: float
    last_trade_sip_timestamp: str
    last_trade_size: int
    timeframe_trade: str
    day_change: float
    day_change_percent: float
    open_interest: float
    day_close: float
    day_high: float
    day_last_updated: str
    day_low: float
    day_open: float
    day_previous_close: float
    day_volume: int
    day_vwap: float
    change_to_break_even: float
    price: float
    underlying_ticker: str
    @property
    def last_trade_condition_name(self) -> str:
        return option_condition_dict.get(self.last_trade_conditions, "Unknown")
    @classmethod
    def from_row(cls, row) -> 'TestOptionsEvent':
        last_trade_conditions = row["last_trade_conditions"] if pd.notna(row["last_trade_conditions"]) else None
        last_trade_exchange=row["last_trade_exchange"] if pd.notna(row["last_trade_exchange"]) else ""

        if last_trade_conditions:
            last_trade_conditions = int(last_trade_conditions.strip('[]'))
        return cls(
            ticker=row["ticker"] if pd.notna(row["ticker"]) else "",
            break_even_price=row["break_even_price"] if pd.notna(row["break_even_price"]) else 0,
            contract_type=row["contract_type"] if pd.notna(row["contract_type"]) else "",
            exercise_style=row["exercise_style"] if pd.notna(row["exercise_style"]) else "",
            expiration_date=row["expiration_date"] if pd.notna(row["expiration_date"]) else "",
            shares_per_contract=row["shares_per_contract"] if pd.notna(row["shares_per_contract"]) else 0,
            strike_price=row["strike_price"] if pd.notna(row["strike_price"]) else 0,
            delta=row["delta"] if pd.notna(row["delta"]) else 0,
            gamma=row["gamma"] if pd.notna(row["gamma"]) else 0,
            theta=row["theta"] if pd.notna(row["theta"]) else 0,
            vega=row["vega"] if pd.notna(row["vega"]) else 0,
            implied_volatility=row["implied_volatility"] if pd.notna(row["implied_volatility"]) else 0,
            open_interest = row["open_interest"] if pd.notna(row["open_interest"]) else 0,
            ask=row["ask"] if pd.notna(row["ask"]) else 0,
            ask_size=row["ask_size"] if pd.notna(row["ask_size"]) else 0,
            bid=row["bid"] if pd.notna(row["bid"]) else 0,
            bid_size=row["bid_size"] if pd.notna(row["bid_size"]) else 0,
            last_updated=row["last_updated"] if pd.notna(row["last_updated"]) else "",
            midpoint=row["midpoint"] if pd.notna(row["midpoint"]) else 0,
            timeframe_quote=row["timeframe_quote"] if pd.notna(row["timeframe_quote"]) else "",
            last_trade_conditions=last_trade_conditions,
            last_trade_exchange=last_trade_exchange,
            last_trade_price=row["last_trade_price"] if pd.notna(row["last_trade_price"]) else 0,
            last_trade_sip_timestamp=row["last_trade_sip_timestamp"] if pd.notna(row["last_trade_sip_timestamp"]) else "",
            last_trade_size=row["last_trade_size"] if pd.notna(row["last_trade_size"]) else 0,
            timeframe_trade=row["timeframe_trade"] if pd.notna(row["timeframe_trade"]) else "",
            day_change=row["day_change"] if pd.notna(row["day_change"]) else 0,
            day_change_percent=row["day_change_percent"] if pd.notna(row["day_change_percent"]) else 0,
            day_close=row["day_close"] if pd.notna(row["day_close"]) else 0,
            day_high=row["day_high"] if pd.notna(row['day_high']) else 0,
            day_last_updated=row["day_last_updated"] if pd.notna(row["day_last_updated"]) else "",
            day_low=row["day_low"] if pd.notna(row['day_low']) else 0,
            day_open=row["day_open"] if pd.notna(row['day_open']) else 0,
            day_previous_close=row["day_previous_close"] if pd.notna(row['day_previous_close']) else 0,
            day_volume=row["day_volume"] if pd.notna(row['day_volume']) else 0,
            day_vwap=row["day_vwap"] if pd.notna(row['day_vwap']) else 0,
            change_to_break_even=row["change_to_break_even"] if pd.notna(row['change_to_break_even']) else 0,
            price=row["price"] if pd.notna(row['price']) else 0,
            underlying_ticker=row["underlying_ticker"] if pd.notna(row['underlying_ticker']) else 0)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'TestOptionsEvent':
        return cls(**data)



TestMessage = NewType(
    "TestMessage",
    List[
        Union[
            TestStocksEvent,
            TestOptionsEvent,
        ]
    ],
)

