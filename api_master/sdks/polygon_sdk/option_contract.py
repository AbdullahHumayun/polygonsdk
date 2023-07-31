import aiohttp
from typing import Optional, Dict
from typing import List
from datetime import datetime
from dataclasses import dataclass, field
from cfg import YOUR_API_KEY

from sdks.polygon_sdk.mapping_dicts import OPTIONS_EXCHANGES, option_condition_dict

@dataclass
class Day:
    change: Optional[float] = None
    change_percent: Optional[float] = None
    close: Optional[float] = None
    high: Optional[float] = None
    last_updated: Optional[int] = None
    low: Optional[float] = None
    open: Optional[float] = None
    previous_close: Optional[float] = None
    volume: Optional[int] = None
    vwap: Optional[float] = None
    def __repr__(self):
        fields = [f"{k}={v}" for k, v in self.__dict__.items() if v is not None]
        return f"{self.__class__.__name__}({', '.join(fields)})"
@dataclass
class Details:
    contract_type: str
    exercise_style: str
    expiration_date: str
    shares_per_contract: int
    strike_price: float
    ticker: str
    def __repr__(self):
        fields = [f"{k}={v}" for k, v in self.__dict__.items() if v is not None]
        return f"{self.__class__.__name__}({', '.join(fields)})"
@dataclass
class Greeks:
    delta: Optional[float] = None
    gamma: Optional[float] = None
    theta: Optional[float] = None
    vega: Optional[float] = None
    implied_volatility: Optional[float] = None

    def __repr__(self):
        fields = [f"{k}={v}" for k, v in self.__dict__.items() if v is not None]
        return f"{self.__class__.__name__}({', '.join(fields)})"
@dataclass
class LastQuote:
    ask: float
    ask_size: int
    bid: float
    bid_size: int
    last_updated: int
    midpoint: float
    timeframe: str
    def __repr__(self):
        fields = [f"{k}={v}" for k, v in self.__dict__.items() if v is not None]
        return f"{self.__class__.__name__}({', '.join(fields)})"
@dataclass
class LastTrade:
    conditions: List[int]
    exchange: int
    price: float
    sip_timestamp: int
    size: int
    timeframe: str

    conditions_str: List[str] = field(init=False)
    exchange_str: str = field(init=False)
    sip_timestamp_str: str = field(init=False)

    def __post_init__(self):
        self.conditions_str = self.get_conditions()
        self.exchange_str = self.get_exchange()
        self.sip_timestamp_str = self.get_human_readable_timestamp()
    def __repr__(self):
        fields = [f"{k}={v}" for k, v in self.__dict__.items() if v is not None]
        return f"{self.__class__.__name__}({', '.join(fields)})"

    def get_conditions(self):
        if self.conditions is None:
            return None
        conditions_str = [option_condition_dict.get(c, f"Unknown condition: {c}") for c in self.conditions]

        return conditions_str
    def get_exchange(self):
        return OPTIONS_EXCHANGES.get(self.exchange, f"Unknown exchange: {self.exchange}")

    def get_human_readable_timestamp(self):
        # Assume that the timestamp is in nanoseconds
        timestamp_in_seconds = self.sip_timestamp / 1e9
        dt_object = datetime.fromtimestamp(timestamp_in_seconds)
        return dt_object.strftime("%Y-%m-%d %H:%M:%S")
    @classmethod
    def from_dict(cls, data: Dict):
        data["conditions"] = [cls.get_conditions(condition) for condition in data["conditions"]]
        data["exchange"] = cls.get_exchange(data["exchange"])
        data["sip_timestamp"] = cls.get_human_readable_timestamp(data["sip_timestamp"])
        return cls(**data)
@dataclass
class UnderlyingAsset:
    change_to_break_even: Optional[float] = None
    last_updated: Optional[int] = None
    price: Optional[float] = None
    ticker: Optional[str] = None
    timeframe: Optional[str] = None
    value: Optional[float] = None
    def __repr__(self):
        fields = [f"{k}={v}" for k, v in self.__dict__.items() if v is not None]
        return f"Greeks({', '.join(fields)})"
@dataclass
class OptionContract:
    
    day: Optional[Day]
    details: Details
    greeks: Greeks
    last_quote: LastQuote
    last_trade: LastTrade
    open_interest: int
    underlying_asset: UnderlyingAsset
    break_even_price: Optional[float] = None
    
    @staticmethod
    async def fetch_option_data(option_symbol: str, underlying_ticker: str):
        url = f"https://api.polygon.io/v3/snapshot/options/{underlying_ticker}/{option_symbol}?apiKey={YOUR_API_KEY}"

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                data = await resp.json()

        results = data['results']

        # Create the class instances
        day = Day(**results['day'])
        details = Details(**results['details'])
        greeks = Greeks(**results['greeks']) if 'greeks' in results else None
        last_quote = LastQuote(**results['last_quote'])
        last_trade = LastTrade(**results['last_trade'])
        underlying_asset = UnderlyingAsset(**results['underlying_asset'])

        return OptionContract(results['break_even_price'] if 'break_even_price' in results else None, day, details, greeks,
                            last_quote, last_trade, results['open_interest'], underlying_asset)
            
    def __repr__(self):
        fields = [f"{k}={v}" for k, v in self.__dict__.items() if v is not None]
        return f"{self.__class__.__name__}({', '.join(fields)})"