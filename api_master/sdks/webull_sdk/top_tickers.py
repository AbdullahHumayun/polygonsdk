from typing import Dict, Optional
from dataclasses import dataclass

@dataclass
class Ticker:
    name: Optional[str]
    symbol: Optional[str]
    exchangeTrade: Optional[bool]
    derivativeSupport: Optional[int]
    close: Optional[str]
    change: Optional[str]
    changeRatio: Optional[str]
    volume: Optional[str]
    netAsset: Optional[str]
    totalAsset: Optional[str]
    peTtm: Optional[str]
    preClose: Optional[str]
    fiftyTwoWkHigh: Optional[str]
    fiftyTwoWkLow: Optional[str]
    open: Optional[str]
    high: Optional[str]
    low: Optional[str]
    vibrateRatio: Optional[str]

    @classmethod
    def from_dict(cls, data: Dict) -> 'Ticker':
        return cls(
            name=data.get('name'),
            symbol=data.get('symbol'),
            exchangeTrade=data.get('exchangeTrade'),
            derivativeSupport=data.get('derivativeSupport'),
            close=data.get('close'),
            change=data.get('change'),
            changeRatio=data.get('changeRatio'),
            volume=data.get('volume'),
            netAsset=data.get('netAsset'),
            totalAsset=data.get('totalAsset'),
            peTtm=data.get('peTtm'),
            preClose=data.get('preClose'),
            fiftyTwoWkHigh=data.get('fiftyTwoWkHigh'),
            fiftyTwoWkLow=data.get('fiftyTwoWkLow'),
            open=data.get('open'),
            high=data.get('high'),
            low=data.get('low'),
            vibrateRatio=data.get('vibrateRatio')
        )
        
@dataclass
class Values:
    dt: Optional[str]
    tickerId: Optional[int]
    volume: Optional[str]
    position: Optional[str]
    volumeCallPutRatio: Optional[str]
    positionCallPutRatio: Optional[str]
    price: Optional[str]
    changeRatio: Optional[str]
    change: Optional[str]

    @classmethod
    def from_dict(cls, data: Dict) -> 'Values':
        return cls(
            dt=data.get('dt'),
            tickerId=data.get('tickerId'),
            volume=data.get('volume'),
            position=data.get('position'),
            volumeCallPutRatio=data.get('volumeCallPutRatio'),
            positionCallPutRatio=data.get('positionCallPutRatio'),
            price=data.get('price'),
            changeRatio=data.get('changeRatio'),
            change=data.get('change')
        )

@dataclass
class TopTickers:
    ticker: Ticker
    values: Values

    @classmethod
    def from_dict(cls, data: Dict) -> 'TopTickers':
        ticker = Ticker.from_dict(data.get('ticker', {}))
        values = Values.from_dict(data.get('values', {}))
        return cls(ticker=ticker, values=values)