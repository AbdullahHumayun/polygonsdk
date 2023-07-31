import asyncio
import aiohttp
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from datetime import datetime
from urllib.parse import urlencode
from cfg import YOUR_API_KEY

import io


from dataclasses import dataclass
from typing import List, Tuple, Optional, Union
import datetime

import pandas as pd
import asyncio

@dataclass
class AggregatesData:
    c: Optional[float] = None
    h: Optional[float] = None
    l: Optional[float] = None
    op: Optional[float] = None
    n: Optional[int] = None
    a: Optional[int] = None
    o: Optional[float] = None
    t: Optional[int] = None
    v: Optional[int] = None
    vw: Optional[float] = None



@dataclass
class AggregatesResponse:
    adjusted: Optional[bool] = None
    next_url: Optional[str] = None
    queryCount: Optional[int] = None
    request_id: Optional[str] = None
    results: Optional[List[AggregatesData]] = None
    resultsCount: Optional[int] = None
    status: Optional[str] = None
    ticker: Optional[str] = None

    async def average_closing_price(self) -> float:
        await asyncio.sleep(0)  # simulate async I/O, e.g. database or API call
        total_closing_price = sum(result.c for result in self.results)
        return total_closing_price / self.resultsCount

    async def date_range(self) -> Tuple[datetime.datetime, datetime.datetime]:
        await asyncio.sleep(0)  # simulate async I/O, e.g. database or API call
        # t is timestamp in milliseconds, need to divide by 1000 to convert to seconds
        dates = [datetime.datetime.fromtimestamp(result.t / 1000) for result in self.results]
        return min(dates), max(dates)

    async def highest_and_lowest_closing_prices(self) -> Tuple[float, float]:
        await asyncio.sleep(0)  # simulate async I/O, e.g. database or API call
        closing_prices = [result.c for result in self.results]
        return max(closing_prices), min(closing_prices)

    async def total_volume(self) -> int:
        await asyncio.sleep(0)  # simulate async I/O, e.g. database or API call
        return sum(result.v for result in self.results)

    async def daily_price_change(self, timespan: str, return_df=False) -> Union[List[Tuple[str, float]], pd.DataFrame]:
        await asyncio.sleep(0)  # simulate async I/O, e.g. database or API call
        if timespan == 'minute':
            data = [(datetime.datetime.fromtimestamp(result.t / 1000).strftime('%H:%M:%S'), 
                    round((result.c - result.o) / result.o * 100, 2),
                    (result.o, result.c)) for result in self.results]
        elif timespan == 'hour':
            data = [(datetime.datetime.fromtimestamp(result.t / 1000).strftime('%Y-%m-%d %H:00:00'), 
                    round((result.c - result.o) / result.o * 100, 2),
                    (result.o, result.c)) for result in self.results]
        else:
            data = [(datetime.datetime.fromtimestamp(result.t / 1000).strftime('%Y-%m-%d'), 
                    round((result.c - result.o) / result.o * 100, 2),
                    (result.o, result.c)) for result in self.results]
                
        if return_df:
            df = pd.DataFrame(data, columns=['Date', f'{timespan.capitalize()} Price Change', 'Price Range'])
            return df
        else:
            return data

    async def daily_high_low_range(self) -> List[float]:
        await asyncio.sleep(0)  # simulate async I/O, e.g. database or API call
        return [result.h - result.l for result in self.results]

    async def vwap(self) -> float:
        await asyncio.sleep(0)  # simulate async I/O, e.g. database or API call
        total_vwap = sum(result.v * result.vw for result in self.results)
        total_volume = sum(result.v for result in self.results)
        return total_vwap / total_volume

    async def average_trading_volume(self) -> float:
        await asyncio.sleep(0)  # simulate async I/O, e.g. database or API call
        return sum(result.v for result in self.results) / self.resultsCount

    async def max_daily_price_change(self) -> float:
        await asyncio.sleep(0)  # simulate async I/O, e.g. database or API call
        price_changes = [(result.c - result.o) / result.o * 100 for result in self.results]
        return max(price_changes)
