from typing import Optional, List
from dataclasses import dataclass


import datetime

@dataclass
class MACDData:
    @dataclass
    class Value:
        histogram: float
        signal: float
        timestamp: datetime.datetime
        value: float

    next_url: Optional[str]
    request_id: Optional[str]
    url: Optional[str]
    values: List[Value]
    status: str

    def __repr__(self):
        return (
            f"MACDData(next_url={self.next_url}, request_id={self.request_id}, "
            f"url={self.url}, values={self.values}, status={self.status})"
        )

    @classmethod
    def from_dict(cls, data_dict):
        next_url = data_dict.get("next_url")
        request_id = data_dict.get("request_id")
        url = data_dict.get("results", {}).get("underlying", {}).get("url")
        values = [
            cls.Value(
                histogram=value.get("histogram"),
                signal=value.get("signal"),
                timestamp=datetime.datetime.fromtimestamp(value.get("timestamp") / 1000.0),
                value=value.get("value")
            )
            for value in data_dict.get("results", {}).get("values", [])
        ]
        status = data_dict.get("status")

        return cls(next_url, request_id, url, values, status)