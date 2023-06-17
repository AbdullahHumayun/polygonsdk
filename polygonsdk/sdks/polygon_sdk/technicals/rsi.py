class RSI:

    def __init__(self, values):

        self.timestamp = [i['timestamp'] if i['timestamp'] is not None else None for i in values]
        self.rsi_value = [i['value'] if i['value'] is not None else None for i in values]
