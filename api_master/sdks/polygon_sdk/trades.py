from dataclasses import dataclass, field
from typing import Optional, List
from datetime import datetime
from sdks.polygon_sdk.mapping_dicts import OPTIONS_EXCHANGES, option_condition_dict

@dataclass
class DataContainer:
    conditions: Optional[List[str]] = field(default_factory=list)
    exchange: Optional[str] = field(default=None)
    id: Optional[str] = field(default=None)
    participant_timestamp: Optional[str] = field(default=None)
    price: Optional[float] = field(default=None)
    sequence_number: Optional[int] = field(default=None)
    sip_timestamp: Optional[str] = field(default=None)
    size: Optional[int] = field(default=None)

    @classmethod
    def from_dict(cls, data_dict):
        conditions = [option_condition_dict.get(condition) for condition in data_dict.get('conditions', [])]
        exchange = OPTIONS_EXCHANGES.get(data_dict.get('exchange'))
        return cls(conditions=conditions, exchange=exchange, 
                   id=data_dict.get('id'), 
                   participant_timestamp=data_dict.get('participant_timestamp'), 
                   price=data_dict.get('price'), 
                   sequence_number=data_dict.get('sequence_number'), 
                   sip_timestamp=data_dict.get('sip_timestamp'), 
                   size=data_dict.get('size'))
    @staticmethod
    def _format_timestamp(timestamp):
        if timestamp:
            dt = datetime.fromtimestamp(timestamp / 1e9)  # convert from nanoseconds
            return dt.strftime("%Y-%m-%d")  # output format
        return None
    def __repr__(self):
        return (f"DataContainer(conditions={self.conditions}, exchange={self.exchange}, id={self.id}, "
                f"participant_timestamp={self.participant_timestamp}, price={self.price}, "
                f"sequence_number={self.sequence_number}, sip_timestamp={self.sip_timestamp}, "
                f"size={self.size})")