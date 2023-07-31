from dataclasses import dataclass
import pandas as pd
from typing import Dict, Any




class IndicesData:

    def __init__(self, results):

        session = [i['session'] if i['session'] is not None else None for i in results]

        self.name = [i['name'] if 'name' in i else None for i in results]
        self.ticker = [i['ticker'] if 'ticker' in i else None for i in results]
        self.change = [i['change'] if 'change' in i else None for i in session]
        self.change_percent = [i['change_percent'] if 'change_percent' in i else None for i in session]
        self.close = [i['close'] if 'close' in i else None for i in session]
        self.high = [i['high'] if 'high' in i else None for i in session]
        self.low = [i['low'] if 'low' in i else None for i in session]
        self.open = [i['open'] if 'open' in i else None for i in session]
        self.previous_close = [i['previous_close'] if 'previous_close' in i else None for i in session]

        self.data_dict = { 
            'name': self.name,
            'ticker': self.ticker,
            'change': self.change,
            'change_percent': self.change_percent,
            'open':self.open,
            'high':self.high,
            'low':self.low,
            'close':self.close,
            'previous_close': self.previous_close,

        }

        self.df = pd.DataFrame(self.data_dict).transpose()

    @classmethod
    def from_dict(cls, data: Dict[str, Any], **kwargs) -> 'IndicesData':
        return cls(**data)
    

 
    def to_dict(self):
        return self.data_dict

    def __iter__(self):
        yield from self.to_dict().items()




from typing import Optional, List, Any

@dataclass
class IndicesSession:
    # assuming these are the attributes; adjust as needed
    change: Optional[float] = None
    change_percent: Optional[float] = None
    close: Optional[float] = None
    high: Optional[float] = None
    low: Optional[float] = None
    open: Optional[float] = None
    previous_close: Optional[float] = None

    def to_dict(self):
        return {
            "change": self.change,
            "change_percent": self.change_percent,
            "close": self.close,
            "high": self.high,
            "low": self.low,
            "open": self.open,
            "previous_close": self.previous_close,
        }


    @classmethod
    def from_dict(cls, data: Dict[str, Any], **kwargs) -> 'IndicesSession':
        return cls(**data)
@dataclass
class IndicesResponse:
    session: IndicesSession = None
    value: Optional[float] = None
    name: Optional[str] = None
    ticker: Optional[str] = None

    def to_dict(self):
        return {
            "session": self.session.to_dict() if self.session else None,
            "value": self.value,
            "name": self.name,
            "ticker": self.ticker,
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'IndicesResponse':
        session_data = data.get('session', None)
        session = IndicesSession.from_dict(session_data) if session_data else None
        return cls(
            value=data.get('value', None),
            name=data.get('name', None),
            ticker=data.get('ticker', None),
            session=session,
        )
    
    def __iter__(self):
        yield from self.to_dict().items()