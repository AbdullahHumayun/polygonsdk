from dataclasses import dataclass
from typing import List




@dataclass
class Day:
    c: float
    h: float
    l: float
    o: float
    v: int
    vw: float

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


@dataclass
class LastQuote:
    P: float
    S: int
    p: float
    s: int
    t: int

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


@dataclass
class LastTrade:
    c: List[int]
    i: str
    p: float
    s: int
    t: int
    x: int

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


@dataclass
class Min:
    av: int
    c: float
    h: float
    l: float
    n: int
    o: float
    t: int
    v: int
    vw: float

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


@dataclass
class PrevDay:
    c: float
    h: float
    l: float
    o: float
    v: int
    vw: float

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


@dataclass
class TickerSnapshotResults:
    day: Day
    lastQuote: LastQuote
    lastTrade: LastTrade
    min: Min
    prevDay: PrevDay
    ticker: str
    todaysChange: float
    todaysChangePerc: float
    updated: int

    @classmethod
    def from_dict(cls, data):
        return cls(
            day=Day.from_dict(data['day']),
            lastQuote=LastQuote.from_dict(data['lastQuote']),
            lastTrade=LastTrade.from_dict(data['lastTrade']),
            min=Min.from_dict(data['min']),
            prevDay=PrevDay.from_dict(data['prevDay']),
            ticker=data['ticker'],
            todaysChange=data['todaysChange'],
            todaysChangePerc=data['todaysChangePerc'],
            updated=data['updated'],
        )