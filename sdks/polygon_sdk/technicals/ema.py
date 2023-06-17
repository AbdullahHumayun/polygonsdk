class ExponentialMovingAverage:
    def __init__(self, values):
        self.value = [i['value'] if i['value'] is not None else None for i in values]
        self.timestamps = [i['timestamp'] if i['timestamp'] is not None else None for i in values]