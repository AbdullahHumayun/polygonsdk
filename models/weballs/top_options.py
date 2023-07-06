from dataclasses import dataclass
from typing import List, Optional, Dict, Any

@dataclass
class Derivative:
    tickerId: int
    exchangeId: int
    regionId: int
    symbol: str
    unSymbol: str
    tickerType: int
    belongTickerId: int
    direction: str
    weekly: int
    quoteLotSize: int
    expireDate: str
    strikePrice: str
    trdStatus: str
    price: str
    close: str
    change: str
    changeRatio: str
    template: str
    quoteMultiplier: int
    cycle: int
    expirationType: Optional[str] = None

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


@dataclass
class BelongTicker:
    name: Optional[str] = None
    symbol: Optional[str] = None
    disSymbol: Optional[str] = None
    derivativeSupport: Optional[int] = None
    status: Optional[str] = None
    close: Optional[str] = None
    change: Optional[str] = None
    changeRatio: Optional[str] = None
    volume: Optional[str] = None
    tickerId: Optional[str] = None
    fiftyTwoWkHigh: Optional[str] = None
    fiftyTwoWkLow: Optional[str] = None
    open: Optional[str] = None
    high: Optional[str] = None
    low: Optional[str] = None
    vibrateRatio: Optional[str] = None
    pprice: Optional[str] = None
    pchange: Optional[str] = None
    pchRatio: Optional[str] = None
    exchangeTrade: Optional[str] = None
    netAsset: Optional[str] = None
    totalAsset: Optional[str] = None
    marketValue: Optional[str] = None
    turnoverRate: Optional[str] = None
    peTtm: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'BelongTicker':
        filtered_data = {key: data[key] for key in cls.__annotations__.keys() if key in data}
        return cls(**filtered_data)

@dataclass
class Values:
    dt: str
    tickerId: int
    volume: str
    position: str
    price: str
    changeRatio: str
    change: str
    belongTickerId: int
    middlePrice: str
    turnover: Optional[str] = None
    positionChange: Optional[str] = None
    implVol: Optional[str] = None

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


@dataclass
class WebullTopOptions:
    derivative: Derivative
    belongTicker: BelongTicker
    values: Values

    @classmethod
    def from_dict(cls, data):
        return cls(
            derivative=Derivative.from_dict(data.get('derivative', {})),
            belongTicker=BelongTicker.from_dict(data.get('belongTicker', {})),
            values=Values.from_dict(data.get('values', {}))
        )