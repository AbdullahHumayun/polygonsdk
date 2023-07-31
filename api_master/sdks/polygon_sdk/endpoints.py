from api_master.cfg import YOUR_API_KEY, thirty_days_from_now_str,thirty_days_ago_str,today_str,seven_days_from_now_str
import random

ticker="SPY"
option_ticker="SPY250321C00380000"
forex_ticker="EURUSD"
crypto_ticker="BTCUSD"
indices_ticker="SPX"

timespans = ["minute","day","hour","week","month","quarter","year"]
timespan = random.choice(timespans)
window = 14
sorts = ['asc', 'desc']
limits = ["5000", "50000", "250", "1000"]
adjusts = ['true','false']
date="2023-07-21"
start_dates= [f"{thirty_days_ago_str}", f"{thirty_days_from_now_str}", f"{today_str}", f"{seven_days_from_now_str}"]
includeOtc = ['true', 'false']
asset_classes = ['stocks', 'crypto', 'forex', 'indices', 'options']


aggregateBars=f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/{timespan}/{start_dates[1]}/{today_str}?adjusted=true&sort=asc&limit=50000&apiKey={YOUR_API_KEY}"
groupedDaily=f"https://api.polygon.io/v2/aggs/grouped/locale/us/market/stocks/{date}?adjusted={adjusts[0]}&include_otc={includeOtc[0]}&apiKey={YOUR_API_KEY}"
dailyOpenClose=f"https://api.polygon.io/v1/open-close/{ticker}/{date}?adjusted={adjusts[0]}&apiKey={YOUR_API_KEY}"
previousClose=f"https://api.polygon.io/v2/aggs/ticker/{ticker}/prev?adjusted={adjusts[0]}&apiKey={YOUR_API_KEY}"
trades=f"https://api.polygon.io/v3/trades/{ticker}?limit={limits[1]}&apiKey={YOUR_API_KEY}"
lastTrade=f"https://api.polygon.io/v2/last/trade/{ticker}?apiKey={YOUR_API_KEY}"
nbboQuotes=f"https://api.polygon.io/v3/quotes/{ticker}?limit={limits[1]}&apiKey={YOUR_API_KEY}"
lastQuote=f"https://api.polygon.io/v2/last/nbbo/{ticker}?apiKey={YOUR_API_KEY}"
universalSnapshot=f"https://api.polygon.io/v3/snapshot?ticker.any_of={ticker},O:{option_ticker},C:{forex_ticker},X:{crypto_ticker},I:{indices_ticker}&order={sorts[0]}&limit={limits[2]}&apiKey={YOUR_API_KEY}"
sma=f"https://api.polygon.io/v1/indicators/sma/{ticker}?timespan={timespan}&adjusted={adjusts[0]}&window={window}&series_type=close&expand_underlying=true&order={sorts[1]}&limit={limits[0]}&apiKey={YOUR_API_KEY}"
ema=f"https://api.polygon.io/v1/indicators/ema/{ticker}?timespan={timespan}&adjusted={adjusts[0]}&window={window}&series_type=close&expand_underlying=true&order={sorts[1]}&limit={limits[0]}&apiKey={YOUR_API_KEY}"
macd=f"https://api.polygon.io/v1/indicators/macd/{ticker}?timespan={timespan}&adjusted={adjusts[0]}&short_window=12&long_window=26&signal_window=9&series_type=close&expand_underlying=true&order={sorts[1]}&limit={limits[0]}&apiKey={YOUR_API_KEY}"
rsi=f"https://api.polygon.io/v1/indicators/rsi/{ticker}?timespan={timespan}&adjusted={adjusts[0]}&window={window}&series_type=close&expand_underlying=true&order={sorts[1]}&limit={limits[0]}&apiKey={YOUR_API_KEY}"
tickerTypes=f"https://api.polygon.io/v3/reference/tickers?active=true&apiKey={YOUR_API_KEY}"
tickerDetails=f"https://api.polygon.io/v3/reference/tickers/{ticker}?apiKey={YOUR_API_KEY}"
tickerNews=f"https://api.polygon.io/v2/reference/news?ticker={ticker}&limit={limits[3]}&apiKey={YOUR_API_KEY}"
dividends=f"https://api.polygon.io/v3/reference/dividends?apiKey={YOUR_API_KEY}"
stock_financials=f"https://api.polygon.io/vX/reference/financials?ticker={ticker}&apiKey={YOUR_API_KEY}"
conditions=f"https://api.polygon.io/v3/reference/conditions?asset_class={asset_classes[0]}&apiKey={YOUR_API_KEY}"

