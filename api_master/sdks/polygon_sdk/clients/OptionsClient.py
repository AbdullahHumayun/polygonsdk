from dataclasses import dataclass, asdict
from dataclasses_json import dataclass_json
from collections import defaultdict
from typing import List, Any, Dict, Optional, Tuple
import pandas as pd

@dataclass_json
@dataclass
class Day:
    change: float
    change_percent: float
    close: float
    high: float
    last_updated: int
    low: float
    open: float
    previous_close: float
    volume: int
    vwap: float

@dataclass_json
@dataclass
class Details:
    contract_type: str
    exercise_style: str
    expiration_date: str
    shares_per_contract: int
    strike_price: float
    ticker: str

@dataclass_json
@dataclass
class Greeks:
    delta: float
    gamma: float
    theta: float
    vega: float

@dataclass_json
@dataclass
class LastQuote:
    ask: float
    ask_size: int
    bid: float
    bid_size: int
    last_updated: int
    midpoint: float

@dataclass_json
@dataclass
class LastTrade:
    conditions: List[int]
    exchange: int
    price: float
    sip_timestamp: int
    size: int
    timeframe: str

@dataclass_json
@dataclass
class UnderlyingAsset:
    change_to_break_even: float
    last_updated: int
    price: float
    ticker: str

@dataclass_json
@dataclass
class Result:
    break_even_price: float
    day: Day
    details: Details
    greeks: Greeks
    implied_volatility: float
    last_quote: LastQuote
    last_trade: LastTrade
    open_interest: int
    underlying_asset: UnderlyingAsset

@dataclass_json
@dataclass
class ApiResponse:
    request_id: str
    results: List[Result]
    status: str



    async def group_by_expiration_date(results: List[Result]) -> Dict[str, List[Result]]:
        groups = defaultdict(list)
        for result in results:
            groups[result.details.expiration_date].append(result)
        return groups
    


    async def create_dataframes(groups: Dict[str, List[Result]]) -> Dict[str, pd.DataFrame]:
        dataframes = {}
        for expiration_date, results in groups.items():
            # Convert the list of Result instances to a list of dictionaries
            data = [asdict(result) for result in results]
            # Create a DataFrame for this group
            df = pd.json_normalize(data)
            dataframes[expiration_date] = df
        return dataframes