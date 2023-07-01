class RSI:

    def __init__(self, values):

        #self.timestamp = [i['timestamp'] if (i is not None and callable(i) and 'timestamp' in i) else None for i in values]
        if values is not None:
            self.rsi_value = [i['value'] if (i is not None and callable(i) and 'value' in i) else None for i in values]
