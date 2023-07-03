class RSI:
    def __init__(self, values):
        if values is not None and len(values) > 0:
            self.rsi_value = [i['value'] if 'value' in i else None for i in values]
        else:
            self.rsi_value = None