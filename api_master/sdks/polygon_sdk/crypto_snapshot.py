from dataclasses import dataclass
from typing import List, Optional

@dataclass
class SessionCrypto:
    c: float
    h: float
    l: float
    o: float
    v: float
    vw: float
    n: Optional[int] = None
    t: Optional[int] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'SessionCrypto':
        return cls(
            c=data['c'],
            h=data['h'],
            l=data['l'],
            o=data['o'],
            v=data['v'],
            vw=data['vw'],
            n=data.get('n'),
            t=data.get('t')
        )


@dataclass
class LastTradeCrypto:
    conditions: List[int]
    i: str
    p: float
    s: float
    t: int
    x: int

    @classmethod
    def from_dict(cls, data: dict) -> 'LastTradeCrypto':
        return cls(
            conditions=data['c'],
            i=data['i'],
            p=data['p'],
            s=data['s'],
            t=data['t'],
            x=data['x']
        )


@dataclass
class CryptoSnapshotResult:
    day: SessionCrypto
    lastTrade: LastTradeCrypto
    min: SessionCrypto
    prevDay: SessionCrypto
    ticker: str
    todaysChange: float
    todaysChangePerc: float
    updated: int

    @classmethod
    def from_dict(cls, data: dict) -> 'CryptoSnapshotResult':
        return cls(
            day=SessionCrypto.from_dict(data['day']),
            lastTrade=LastTradeCrypto.from_dict(data['lastTrade']),
            min=SessionCrypto.from_dict(data['min']),
            prevDay=SessionCrypto.from_dict(data['prevDay']),
            ticker=data['ticker'],
            todaysChange=data['todaysChange'],
            todaysChangePerc=data['todaysChangePerc'],
            updated=data['updated']
        )