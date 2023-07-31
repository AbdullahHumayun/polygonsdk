from dataclasses import dataclass
from typing import List, Optional, Dict

@dataclass
class TradeData:
    conditions: List[int]
    exchange: int
    id: str
    participant_timestamp: int
    price: float

    sequence_number: int
    sip_timestamp: int
    size: int
    tape: int
    trf_id: Optional[float] = None
    trf_timestamp: Optional[float] = None

@dataclass
class TradeResponse:
    next_url: Optional[str]
    request_id: str
    results: List[TradeData]
    status: str


    async def get_total_trade_volume(self) -> int:
        return sum(trade.size for trade in self.results)

    async def get_average_trade_price(self) -> float:
        total_price = sum(trade.price for trade in self.results)
        return total_price / len(self.results)

    async def get_unique_exchanges(self) -> List[int]:
        return list(set(trade.exchange for trade in self.results))

    async def get_trade_conditions(self) -> Dict[int, int]:
        condition_dict = {}
        for trade in self.results:
            for condition in trade.conditions:
                if condition in condition_dict:
                    condition_dict[condition] += 1
                else:
                    condition_dict[condition] = 1
        return condition_dict

    async def get_trade_sequence_range(self) -> int:
        sequence_numbers = [trade.sequence_number for trade in self.results]
        return max(sequence_numbers) - min(sequence_numbers)