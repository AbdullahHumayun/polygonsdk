class OptionVolumeTotals:
    def __init__(self, entity):
        self.total_vol = entity["totalVolume"]
        self.optionsVol=entity["optionsVolume"]
        self.futures_vol=entity["futuresVolume"]
        self.fiftytwohigh =entity["fiftytwo_week_high"]
        self.fiftytwolow =entity["fiftytwo_week_low"]
        self.monthlydailyavg=entity["monthlyDailyAverage"]
        self.yearlydailyavg=entity["yearlyDailyAverage"]