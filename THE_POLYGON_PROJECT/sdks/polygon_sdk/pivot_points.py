from dataclasses import dataclass
from typing import List
from datetime import datetime
@dataclass
class PivotPointData:
    def __init__(self, timestamp, pivot_point, resistance1, resistance2, support1, support2):
        self.timestamp = timestamp
        self.pivot_point = pivot_point
        self.resistance1 = resistance1
        self.resistance2 = resistance2
        self.support1 = support1
        self.support2 = support2


def format_timestamp(timestamp: datetime) -> str:
    return timestamp.strftime("%Y/%m/%d %I:%M %p")


