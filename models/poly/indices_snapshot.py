from dataclasses import dataclass
from typing import Optional

@dataclass
class Session:
    change: float
    change_percent: float
    close: float
    high: float
    low: float
    open: float
    previous_close: float

    @classmethod
    def from_dict(cls, data):
        return cls(**data)


@dataclass
class IndicesSnapshotResult:
    last_updated: int
    market_status: str
    name: str
    session: Session
    ticker: str
    timeframe: str
    type: str
    value: float
    error: Optional[str] = None
    message: Optional[str] = None

    @classmethod
    def from_dict(cls, data):
        session_data = data.get('session')
        session = Session.from_dict(session_data) if session_data is not None else None

        return cls(
            last_updated=data['last_updated'],
            market_status=data['market_status'],
            name=data['name'],
            session=session,
            ticker=data['ticker'],
            timeframe=data['timeframe'],
            type=data['type'],
            value=data['value'],
            error=data.get('error'),
            message=data.get('message'),
        )