from dataclasses import dataclass
from typing import Optional

class Address:
    address1: Optional[str] = None
    city: Optional[str] = None
    postal_code: Optional[str] = None
    state: Optional[str] = None

class Branding:
    icon_url: Optional[str] = None
    logo_url: Optional[str] = None


class CompanyResults:
    request_id: str
    address: Optional[Address] = None
    branding: Optional[Branding] = None
    status: Optional[str] = None
    active: float
    address: Optional[Address] = None
    branding: Optional[Branding] = None
    cik: Optional[str] = None
    composite_figi: Optional[str] = None
    description: Optional[str] = None
    homepage_url: Optional[str] = None
    list_date: Optional[str] = None
    locale: Optional[str] = None
    market: Optional[str] = None
    market_cap: Optional[float] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None
    primary_exchange: Optional[str] = None
    round_lot: Optional[str] = None
    share_class_figi: Optional[str] = None
    share_class_shares_outstanding: Optional[float] = None
    sic_code: Optional[str] = None
    sic_description: Optional[str] = None
    ticker: Optional[str] = None
    ticker_root: Optional[str] = None
    total_employees: Optional[str] = None
    type: Optional[str] = None
    weighted_shares_outstanding: Optional[float] = None


class CompanyInfo:
    request_id: str
    address: Optional[Address] = None
    branding: Optional[Branding] = None
    status: Optional[str] = None

