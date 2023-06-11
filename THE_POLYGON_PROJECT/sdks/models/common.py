from enum import Enum


class Feed(Enum):
    Delayed = "delayed.polygon.io"
    RealTime = "socket.polygon.io"
    Nasdaq = "nasdaqfeed.polygon.io"
    PolyFeed = "polyfeed.polygon.io"
    PolyFeedPlus = "polyfeedplus.polygon.io"
    StarterFeed = "starterfeed.polygon.io"


class Market(Enum):
    Stocks = "stocks"
    Options = "options"
    Forex = "forex"
    Crypto = "crypto"
    Indices = "indices"


class EventType(Enum):
    TestOptionsEvent = "TO"
    TestStocksEvent = "TS"
