from datetime import datetime
import pandas as pd
class OptionAggs:
    def __init__(self, bar_data):
        self.open = bar_data.get("o")
        self.high = bar_data.get("h")
        self.low = bar_data.get("l")
        self.close = bar_data.get("c")
        self.volume = bar_data.get("v")
        self.vw = bar_data.get("vw")
        self.number_of_trades = bar_data.get("n")
        self.timestamp = self._convert_timestamp(bar_data.get("t"))

        self.data_dict = {
            'Timestamp': self.timestamp,
            'Open': self.open,
            'High': self.high,
            'Low': self.low,
            'Close': self.close,
            'Volume': self.volume,
            'VWAP': self.vw,
            'Number of Trades': self.number_of_trades
        }

        self.df = pd.DataFrame(self.data_dict)
    @staticmethod
    def _convert_timestamp(timestamp):
        dt = datetime.fromtimestamp(timestamp // 1000)
        return dt.strftime('%Y/%m/%d:%I:%M %p')
    
    
    def to_dict(self):
        return {
            'timestamp': self.timestamp,
            'open': self.open,
            'high': self.high,
            'low': self.low,
            'close': self.close,
            'volume': self.volume,
            'vw': self.vw,
            'number_of_trades': self.number_of_trades
        }
    def __str__(self):
        return f"OptionAggs(timestamp={self.timestamp}, open={self.open}, high={self.high}, low={self.low}, close={self.close}, volume={self.volume})"

    def __repr__(self):
        return self.__str__()
    
