class ShortInterest:
    def __init__(self, data):
        self.settlement = [i['settlementDate'] for i in data]
        self.short_int = [i['shortInterst'] for i in data]
        self.avg_volume = [i['avgDailyShareVolume'] for i in data]
        self.days_to_cover = [i['daysToCover'] for i in data]
