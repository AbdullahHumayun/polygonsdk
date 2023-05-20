
class CostDistribution:
    def __init__(self, data):
        self.tickerId = data['tickerId']
        self.avgCost = data['avgCost']
        self.closeProfitRatio = data['closeProfitRatio']
        self.chip90Start = data['chip90Start']
        self.chip90End = data['chip90End']
        self.chip90Ratio = data['chip90Ratio']
        self.chip70Start = data['chip70Start']
        self.chip70End = data['chip70End']
        self.chip70Ratio = data['chip70Ratio']
        self.close = data['close']
        self.totalShares = data['totalShares']
        self.distributions = data['distributions']
        self.tradeStamp = data['tradeStamp']

    def __str__(self):
        return f"CostDistribution(tickerId={self.tickerId}, avgCost={self.avgCost}, closeProfitRatio={self.closeProfitRatio}, chip90Start={self.chip90Start}, chip90End={self.chip90End}, chip90Ratio={self.chip90Ratio}, chip70Start={self.chip70Start}, chip70End={self.chip70End}, chip70Ratio={self.chip70Ratio}, close={self.close}, totalShares={self.totalShares}, distributions={self.distributions}, tradeStamp={self.tradeStamp})"

    def __repr__(self):
        return self.__str__()
