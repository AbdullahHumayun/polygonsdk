from dataclasses import dataclass
from typing import List
import pandas as pd
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


        self.data_dict = {

            'Timestamp': self.timestamp,
            'Pivot Point': self.pivot_point,
            'Resistance 1': self.resistance1,
            'Resistance 2': self.resistance2,
            'Support 1': self.support1,
            'Support 2': self.support2
        }

        self.df = pd.DataFrame(self.data_dict)

def format_timestamp(timestamp: datetime) -> str:
    return timestamp.strftime("%Y/%m/%d %I:%M %p")


