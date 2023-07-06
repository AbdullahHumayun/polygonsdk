from dataclasses import dataclass
from typing import List, Optional, Iterator
from datetime import datetime

@dataclass
class RSIValue:
    timestamp: str
    value: str

    @classmethod
    def from_dict(cls, data: dict) -> 'RSIValue':
        timestamp = datetime.fromtimestamp(data['timestamp'] / 1000)
        value = data['value']
        return cls(timestamp=timestamp, value=value)

    def __iter__(self) -> Iterator:
        yield self.timestamp
        yield self.value


@dataclass
class RSIResults:
    status: str
    request_id: str
    next_url: str
    results: dict
    values: List[RSIValue]
    value: Optional[float] = None
    timestamp: Optional[float] = None

    def __iter__(self):
        yield from self.values

    @classmethod
    def from_dict(cls, data: dict) -> 'RSIResults':
        status = data.get('status', None)
        request_id = data.get('request_id', None)
        next_url = data.get('next_url', None)
        results = data.get('results', None)
        values_data = data.get('results', {}).get('values', [])
        values = [RSIValue.from_dict(item) for item in values_data]
        if values:
            value = values[0].value
            timestamp = values[0].timestamp
        else:
            value = None
            timestamp = None
        return cls(status=status, request_id=request_id, next_url=next_url, results=results, values=values, value=value, timestamp=timestamp)