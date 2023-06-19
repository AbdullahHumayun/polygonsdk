import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from cfg import today_str, thirty_days_ago_str,thirty_days_from_now_str
from sdks.stocksera_sdk.sdk import StockeraSDK

sdk = StockeraSDK()


earnings_calendar = sdk.earnings_calendar(date_from=thirty_days_ago_str, date_to=thirty_days_from_now_str)


# Accessing the latest attributes
date = earnings_calendar.date[0]
eps_act = earnings_calendar.eps_act[0]
eps_est = earnings_calendar.eps_est[0]
hour = earnings_calendar.hour[0]
mkt_cap = earnings_calendar.mkt_cap[0]
quarter = earnings_calendar.quarter[0]
revenue_act = earnings_calendar.revenue_act[0]
revenue_est = earnings_calendar.revenue_est[0]
ticker = earnings_calendar.ticker[0]
year = earnings_calendar.year[0]

# Print attribute values
print("Date:", date)
print("EPS (Actual):", eps_act)
print("EPS (Estimate):", eps_est)
print("Hour:", hour)
print("Market Cap:", mkt_cap)
print("Quarter:", quarter)
print("Revenue (Actual):", revenue_act)
print("Revenue (Estimate):", revenue_est)
print("Ticker:", ticker)
print("Year:", year)


df = pd.DataFrame(vars(earnings_calendar))


print(df)