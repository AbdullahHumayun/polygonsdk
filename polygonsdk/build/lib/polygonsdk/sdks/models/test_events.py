import pandas as pd

from typing import Union, List, NewType, Dict, Any
from dataclasses import dataclass

from .maps import option_condition_dict, EQUITY_TRADE_CONDITIONS


@dataclass
class TestStocksEvent:
    """
    This class represents a simulated stock market event. It's designed to provide a detailed snapshot of a particular 
    stock's trading activity, encapsulating data like the stock's opening, closing, high, and low prices, as well as
    volume information and details about the last trade and quote.

    Attributes:
        symbol: The ticker symbol for the stock.
        close: The closing price of the stock.
        high: The highest traded price of the stock.
        low: The lowest traded price of the stock.
        open: The opening price of the stock.
        volume: The volume of shares traded.
        vwap: The volume-weighted average price of the stock.
        last_quote_ask_price: The last quoted ask price.
        last_quote_ask_size: The size of the last quoted ask.
        last_quote_bid_price: The last quoted bid price.
        last_quote_bid_size: The size of the last quoted bid.
        last_quote_timestamp: The timestamp of the last quote.
        last_trade_conditions: The conditions of the last trade.
        last_exchange: The exchange where the last trade occurred.
        last_price: The price of the last trade.
        last_size: The size of the last trade.
        last_id: The unique identifier of the last trade.
        last_trade_timestamp: The timestamp of the last trade.
        min_close: The minimum closing price.
        min_high: The minimum highest price.
        min_low: The minimum lowest price.
        min_open: The minimum opening price.
        min_volume: The minimum volume.
        min_av: The minimum average volume.
        min_vwap: The minimum volume-weighted average price.
        prev_vwap: The previous volume-weighted average price.
        prev_close: The previous closing price.
        prev_high: The previous highest price.
        prev_low: The previous lowest price.
        prev_open: The previous opening price.
        prev_volume: The previous volume.
        today_change_percent: The percentage change in price during the day.
        today_change: The change in price during the day.
    """
    symbol: str=None
    today_change_percent: float = None
    today_change: float = None
    open: float = None
    high: float = None
    low: float = None
    close: float = None
    volume: float = None
    vwap: float = None
    last_trade_conditions: List[Dict[int, str]] = None
    last_exchange: Dict[int, str] = None
    last_price: float = None
    last_size: float = None
    last_trade_timestamp: str=None
    last_quote_timestamp: str=None
    last_quote_bid: float = None
    last_quote_ask: float = None
    last_quote_ask_size: float = None
    last_quote_bid_size: float = None
    trade_id: int = None
    min_av: float = None
    min_volume: float = None
    min_open: float = None
    min_high: float = None
    min_low: float = None
    min_close: float = None
    min_vwap: float = None
    prev_open: float = None
    prev_high: float = None
    prev_low: float = None
    prev_close: float = None
    prev_volume: float = None
    prev_vwap: float = None

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
            trade_id = row['Last Trade ID'],
            last_quote_bid=row['Last Quote Bid Price'],
            last_quote_ask=row['Last Quote Ask Price'],
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
    """
    This class represents a simulated market event for options. It's primarily used during after-market hours to simulate 
    a websocket feed and process data quickly. The data encapsulated in each instance of this class typically include
    ticker information, break-even price, contract details, and various Greek values typically used in options trading.
    This class provides an efficient way to manage and manipulate these pieces of information.

    Attributes:
        ticker: The ticker symbol for the option.
        break_even_price: The price at which the option breaks even.
        contract_type: Type of the option contract - 'Call' or 'Put'.
        exercise_style: Style of the option contract - 'American' or 'European'.
        expiration_date: Expiration date of the option contract.
        shares_per_contract: Number of shares per option contract.
        strike_price: The price at which the option can be exercised.
        delta: The rate of change of the option price with respect to changes in the underlying asset's price.
        gamma: The rate of change of the delta with respect to changes in the underlying asset's price.
        theta: The rate of decrease in the option price with respect to time.
        vega: The rate of change of the option price with respect to changes in the underlying asset's volatility.
        implied_volatility: The option's implied volatility.
        ask: The asking price of the option.
        ask_size: The size of the ask order.
        bid: The bid price of the option.
        bid_size: The size of the bid order.
        last_updated: The timestamp of the last update.
        midpoint: The midpoint of the bid and ask prices.
        timeframe_quote: The timeframe of the quote.
        last_trade_conditions: The conditions of the last trade.
        last_trade_exchange: The exchange where the last trade occurred.
        last_trade_price: The price of the last trade.
        last_trade_sip_timestamp: The SIP timestamp of the last trade.
        last_trade_size: The size of the last trade.
        timeframe_trade: The timeframe of the trade.
        day_change: The change in price during the day.
        day_change_percent: The percentage change in price during the day.
        open_interest: The open interest of the option.
        day_close: The closing price of the day.
        day_high: The highest price of the day.
        day_last_updated: The timestamp of the last update of the day.
        day_low: The lowest price of the day.
        day_open: The opening price of the day.
        day_previous_close: The previous day's closing price.
        day_volume: The volume of the day.
        day_vwap: The volume-weighted average price of the day.
        change_to_break_even: The change needed to reach the break-even price.
        price: The current price of the option.
        underlying_ticker: The ticker of the underlying asset.

    """
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


