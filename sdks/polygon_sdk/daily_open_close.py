class DailyOpenClose:
    def __init__(self, response_data):
        self.after_hours = response_data.get("afterHours")
        self.close = response_data.get("close")
        self.date = response_data.get("from")
        self.high = response_data.get("high")
        self.low = response_data.get("low")
        self.open = response_data.get("open")
        self.pre_market = response_data.get("preMarket")
        self.status = response_data.get("status")
        self.symbol = response_data.get("symbol")
        self.volume = response_data.get("volume")

    def __str__(self):
        return f"DailyOpenClose({self.symbol}, {self.date})"

    def __repr__(self):
        return self.__str__()
    

