
class TreausryBalance:
    def __init__(self, data):

        self.date = [i['Date'] if i ['Date'] is not None else None for i in data]
        self.close_blaance = [i['Close Balance'] if i ['Close Balance'] is not None else None for i in data]
        self.open_balance = [i['Open Balance'] if i ['Open Balance'] is not None else None for i in data]
        self.amount_change = [i['Amount Change'] if i ['Amount Change'] is not None else None for i in data]
        self.percent_change = [i['Percent Change'] if i ['Percent Change'] is not None else None for i in data]