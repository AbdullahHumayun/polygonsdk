
import statistics

from dataclasses import dataclass
from typing import Optional, List, Union, Tuple, Dict, Any




@dataclass
class AggregateResult:
    v: Optional[float] = None
    vw: Optional[float] = None
    o: Optional[float] = None
    c: Optional[float] = None
    h: Optional[float] = None
    l: Optional[float] = None
    t: Optional[int] = None
    n: Optional[int] = None
    otc: Optional[bool] = None

    @classmethod
    def from_dict(cls, data: dict):
        data['otc'] = data.get('otc', False)
        return cls(**data)

@dataclass
class AggregateResponse:
    results: list[AggregateResult]

    def get_average_close_price(self) -> Union[float, None]:
        if self.results:
            return statistics.mean([result.c for result in self.results if result.c is not None])
        return None

    def get_high_price(self) -> Union[float, None]:
        if self.results:
            high_prices = [result.h for result in self.results if result.h is not None]
            if high_prices:
                return max(high_prices)
        return None

    def get_low_price(self) -> Union[float, None]:
        if self.results:
            low_prices = [result.l for result in self.results if result.l is not None]
            if low_prices:
                return min(low_prices)
        return None
    

    def get_price_gaps(self) -> List[Tuple[AggregateResult, AggregateResult]]:
        gaps = []

        for i in range(1, len(self.results)):
            previous_bar = self.results[i - 1]
            current_bar = self.results[i]

            if previous_bar.h is None or previous_bar.l is None or current_bar.h is None or current_bar.l is None:
                continue  # Skip bars with missing data

            # Check for gap up
            if current_bar.l > previous_bar.h:
                gaps.append((previous_bar, current_bar))

            # Check for gap down
            elif current_bar.h < previous_bar.l:
                gaps.append((previous_bar, current_bar))

        return gaps
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'AggregateResult':
        results = data.get('results', [])
        results = [AggregateResult.from_dict(result) for result in results]

        return cls(
            adjusted=data.get('adjusted', False),
            next_url=data.get('next_url', None),
            queryCount=data.get('queryCount', 0),
            request_id=data.get('request_id', ""),
            results=results
        )
    
    @classmethod
    def from_list(cls, data_list):
        aggregate_responses = []

        for data in data_list:
            # The logic to create an AggregateResponse from a dict goes here
            aggregate_response = cls(
                adjusted=data.get('adjusted'),
                next_url=data.get('next_url'),
                queryCount=data.get('queryCount'),
                request_id=data.get('request_id'),
                results=[AggregateResult.from_dict(result) for result in data.get('results', [])],
            )
            aggregate_responses.append(aggregate_response)

        return aggregate_responses
    @classmethod
    def from_list(cls, data_list):
        aggregate_responses = []

        for data in data_list:
            # The logic to create an AggregateResponse from a dict goes here
            aggregate_response = cls(
                adjusted=data.get('adjusted'),
                next_url=data.get('next_url'),
                queryCount=data.get('queryCount'),
                request_id=data.get('request_id'),
                results=[AggregateResult.from_dict(result) for result in data.get('results', [])],
            )
            aggregate_responses.append(aggregate_response)

        return aggregate_responses