import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sdks.occ_sdk.sdk import occSDK



sdk = occSDK()


x =sdk.volume_totals()


print(x.fiftytwo_week_low)
print(x.optionsVolume)
print(x.fiftytwo_week_high)
print(x.futuresVolume)
print(x.monthlyDailyAverage)
print(x.yearlyDailyAverage)
print(x.totalVolume)
daily_stats = list(zip(x.trade_dates, x.trade_volume))
print(daily_stats)