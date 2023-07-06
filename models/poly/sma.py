from typing import Optional, List
from dataclasses import dataclass

import datetime

@dataclass
class SMAResults:
    @dataclass
    class Value:
        timestamp: str
        value: str

    next_url: Optional[str]
    request_id: Optional[str]
    aggregates: List[dict]
    url: Optional[str]
    values: List[Value]
    status: str

    def __repr__(self):
        return (
            f"SMAData(next_url={self.next_url}, request_id={self.request_id}, "
            f"aggregates={self.aggregates}, url={self.url}, values={self.values}, "
            f"status={self.status})"
        )

    @classmethod
    def from_dict(cls, data_dict):
        next_url = data_dict.get("next_url")
        request_id = data_dict.get("request_id")
        aggregates = [
            {
                "c": agg.get("c"),
                "h": agg.get("h"),
                "l": agg.get("l"),
                "n": agg.get("n"),
                "o": agg.get("o"),
                "t": agg.get("t"),
                "v": agg.get("v"),
                "vw": agg.get("vw")
            }
            for agg in data_dict.get("results", {}).get("underlying", {}).get("aggregates", [])
        ]
        url = data_dict.get("results", {}).get("underlying", {}).get("url")
        values = [
            {
                "timestamp": datetime.datetime.fromtimestamp(value.get("timestamp") / 1000.0).strftime("%Y-%m-%d"),
                "value": value.get("value")
            }
            for value in data_dict.get("results", {}).get("values", [])
        ]
        status = data_dict.get("status")

        return cls(next_url, request_id, aggregates, url, values, status)