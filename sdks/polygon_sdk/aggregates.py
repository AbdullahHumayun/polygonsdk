class AggregatesData:
    def __init__(self, response_data):
        self.adjusted = response_data.get("adjusted")
        self.next_url = response_data.get("next_url")
        self.ticker = response_data.get("ticker")
        self.query_count = response_data.get("queryCount")
        self.request_id = response_data.get("request_id")
        self.results = response_data.get("results")

        if self.results is None:
            self.close = []
            self.high = []
            self.low = []
            self.n = []
            self.open = []
            self.timestamp = []
            self.volume = []
            self.volume_weighted_average = []
        else:
            self.close = [i['c'] for i in self.results]
            self.high = [i['h'] for i in self.results]
            self.low = [i['l'] for i in self.results]
            self.n = [i['n'] for i in self.results]
            self.open = [i['o'] for i in self.results]
            self.timestamp = [i['t'] for i in self.results]
            self.volume = [i['v'] for i in self.results]
            self.volume_weighted_average = [i['vw'] for i in self.results]

    def __str__(self):
        return f"AggregatesData({self.ticker})"

    def __repr__(self):
        return self.__str__()