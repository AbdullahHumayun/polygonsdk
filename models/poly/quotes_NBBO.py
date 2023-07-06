from dataclasses import dataclass
from datetime import datetime

from utilities.list_sets import quote_conditions

@dataclass
class QuotesNBBO:
    next_url: str
    request_id: str
    results: list

    @classmethod
    def from_dict(cls, data_dict):
        next_url = data_dict.get("next_url")
        request_id = data_dict.get("request_id")
        results = []

        for result in data_dict.get("results", []):
            ask_exchange = result.get("ask_exchange")
            ask_price = result.get("ask_price")
            ask_size = result.get("ask_size")
            bid_exchange = result.get("bid_exchange")
            bid_price = result.get("bid_price")
            bid_size = result.get("bid_size")
            conditions = result.get("conditions")
            participant_timestamp = datetime.fromtimestamp(result.get("participant_timestamp") / 10**9)
            sequence_number = result.get("sequence_number")
            sip_timestamp = datetime.fromtimestamp(result.get("sip_timestamp") / 10**9)
            tape = result.get("tape")

            quotes_nbbo = QuotesNBBOItem(
                ask_exchange=ask_exchange,
                ask_price=ask_price,
                ask_size=ask_size,
                bid_exchange=bid_exchange,
                bid_price=bid_price,
                bid_size=bid_size,
                conditions=conditions,
                participant_timestamp=participant_timestamp,
                sequence_number=sequence_number,
                sip_timestamp=sip_timestamp,
                tape=tape
            )
            results.append(quotes_nbbo)

        return cls(next_url=next_url, request_id=request_id, results=results)


from dataclasses import dataclass
from datetime import datetime

from dataclasses import dataclass
from datetime import datetime

@dataclass
class QuotesNBBOItem:
    ask_exchange: int
    ask_price: float
    ask_size: int
    bid_exchange: int
    bid_price: float
    bid_size: int
    conditions: list
    participant_timestamp: datetime
    sequence_number: int
    sip_timestamp: datetime
    tape: int

    @classmethod
    def from_dict(cls, data_dict):
        ask_exchange = data_dict.get("ask_exchange")
        ask_price = data_dict.get("ask_price")
        ask_size = data_dict.get("ask_size")
        bid_exchange = data_dict.get("bid_exchange")
        bid_price = data_dict.get("bid_price")
        bid_size = data_dict.get("bid_size")
        conditions = data_dict.get("conditions")
        participant_timestamp = datetime.fromtimestamp(data_dict.get("participant_timestamp") / 1000000000)
        sequence_number = data_dict.get("sequence_number")
        sip_timestamp = datetime.fromtimestamp(data_dict.get("sip_timestamp") / 1000000000)
        tape = data_dict.get("tape")

        conditions = [quote_conditions.get(condition) for condition in conditions]

        return cls(
            ask_exchange, ask_price, ask_size, bid_exchange, bid_price, bid_size, conditions,
            participant_timestamp, sequence_number, sip_timestamp, tape
        )