
from typing import Optional
from dataclasses import dataclass

@dataclass
class Dividend:
    cash_amount: float
    declaration_date: str
    dividend_type: str
    ex_dividend_date: str
    frequency: int
    pay_date: str
    record_date: str
    ticker: str
    currency: Optional[str] = None
    

@dataclass
class Condition:
    id: int
    name: str
    type: str
    description: str

    def __str__(self):
        return f"Condition(id={self.id}, name='{self.name}', type='{self.type}', description='{self.description}')"

    @classmethod
    def from_json(cls, json_data: dict):
        return cls(
            id=json_data['id'],
            name=json_data['name'],
            type=json_data['type'],
            description=json_data['description'],
        )
    

