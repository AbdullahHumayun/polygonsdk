from typing import List
class MACDData:
    def __init__(self, timestamps, macd, signal, histogram):
        self.timestamps = timestamps
        self.macd = macd
        self.signal = signal
        self.histogram = histogram


