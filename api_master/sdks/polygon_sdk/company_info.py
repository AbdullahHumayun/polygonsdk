import pandas as pd

class CompanyInfo:
    def __init__(self, results):
        self.cik = results.get("cik", None)
        self.composite_figi = results.get("composite_figi", None)
        self.currency_name = results.get("currency_name", None)
        self.description = results.get("description", None)
        self.homepage_url = results.get("homepage_url", None)
        self.list_date = results.get("list_date", None)
        self.locale = results.get("locale", None)
        self.market = results.get("market", None)
        self.market_cap = results.get("market_cap", None)
        self.name = results.get("name", None)
        self.phone_number = results.get("phone_number", None)
        self.primary_exchange = results.get("primary_exchange", None)
        self.round_lot = results.get("round_lot", None)
        self.share_class_figi = results.get("share_class_figi", None)
        self.share_class_shares_outstanding = results.get("share_class_shares_outstanding", None)
        self.sic_code = results.get("sic_code", None)
        self.sic_description = results.get("sic_description", None)
        self.ticker = results.get("ticker", None)


     
