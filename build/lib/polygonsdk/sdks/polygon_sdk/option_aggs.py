from datetime import datetime

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

    @staticmethod
    def _convert_timestamp(timestamp):
        dt = datetime.fromtimestamp(timestamp // 1000)
        return dt.strftime('%Y/%m/%d:%I:%M %p')

    def __str__(self):
        return f"OptionAggs(timestamp={self.timestamp}, open={self.open}, high={self.high}, low={self.low}, close={self.close}, volume={self.volume})"

    def __repr__(self):
        return self.__str__()