import pandas as pd


class DailyOpenClose:
    """
    Class representing daily open and close data for a symbol.
    """

    def __init__(self, response_data):
        """
        Initialize a DailyOpenClose object with response data.

        Args:
            response_data (dict): Response data containing open and close information.
        """
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


    
        self.data_dict = {
            "after_hours": self.after_hours,
            "close": self.close,
            "date": self.date,
            "high": self.high,
            "low": self.low,
            "open": self.open,
            "pre_market": self.pre_market,
            "status": self.status,
            "symbol": self.symbol,
            "volume": self.volume
        }

        self.df = pd.DataFrame(self.data_dict)
    def __str__(self):
        return f"DailyOpenClose({self.symbol}, {self.date})"

    def __repr__(self):
        return self.__str__()
    

