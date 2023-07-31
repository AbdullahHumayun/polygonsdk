from typing import List
from typing import List
class MACDData:
    def __init__(self, results):
        self.timestamps = [i['timestamp'] if 'timestamp' in i else None for i in results]
        self.macd = [i['value'] if 'value' in i else None for i in results]
        self.signal = [i['signal'] if 'signal' in i else None for i in results]
        self.histogram = [i['histogram'] if 'histogram' in i else None for i in results]


