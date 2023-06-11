import mplfinance as mpf
import pandas as pd
import numpy as np
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
import io
import mplfinance as mpf

sdk = AsyncPolygonSDK(YOUR_API_KEY)
from cfg import YOUR_API_KEY, today_str

async def plot_chart(ticker, multiplier, timespan, to_date, from_date, limit):
    aggs = await sdk.get_aggregates(ticker=ticker, multiplier=multiplier, timespan=timespan,from_date=from_date, to_date=today_str, limit=limit)


    data = { 
        'Open': aggs.open,
        'High': aggs.high,
        'Low': aggs.low,
        'Close': aggs.close,
        'Time': aggs.timestamp,
        'Volume': aggs.volume
    }
    df = pd.DataFrame(data)
    df.index = pd.DatetimeIndex(df.index)

    if df.empty:
        print(f"The DataFrame is empty for {ticker}.")
        return None, None

    # Check for NaN values in the DataFrame
    if df.isna().any().any():
        print(f"The DataFrame contains NaN values for {ticker}.")
        df.fillna(0, inplace=True)

    df['EveningStar'] = np.nan



    
    
    # Define the style for the chart
    mc = mpf.make_marketcolors(up='g', down='r', edge='inherit', wick='inherit', volume='inherit')
    style = mpf.make_mpf_style(marketcolors=mc)

    # Add a scatterplot of the 'EveningStar' points
    apdict = [mpf.make_addplot(df['EveningStar'], type='scatter', markersize=50, marker='v', color='b')]

    try:
        fig, axes = mpf.plot(df, type='candle', style=style, title=f'Trend Reversal - {ticker} DAILY', volume=True,
                            addplot=apdict, returnfig=True)
    except ValueError as e:
        print(f"Failed to plot chart for {ticker} due to: {e}")
        return None, None

    # Save the figure
    filename = f"files/images/plots/bullish_star.png"
    fig.savefig(filename)

    # Read the image file in binary mode
    with open(filename, 'rb') as f:
        image_bytes = f.read()

    return io.BytesIO(image_bytes), filename
   
async def is_hanging_man(ticker):
    aggs = await sdk.get_aggregates(
        ticker, 1, "day", 
        from_date="2023-03-01", 
        to_date="2023-05-20", 
        order="desc", 
        limit=2
    )

    if aggs.close is not None and len(aggs.close) < 2 or len(aggs.open) < 2 or len(aggs.low) < 2 or len(aggs.high) < 1:
        print(f"Not enough data for {ticker}")
        return False       

    close_price = aggs.close[0]
    open_price = aggs.open[0]
    low_price = aggs.low[0]
    high_price = aggs.high[0]

    previous_close = aggs.close[1]

    body = abs(open_price - close_price)
    lower_wick = min(open_price, close_price) - low_price

    if previous_close < close_price and body <= lower_wick / 2 and high_price - max(open_price, close_price) <= body / 2:
        return True

    return False


async def is_spinning_top(ticker):
    aggs = await sdk.get_aggregates(
        ticker, 1, "day", 
        from_date="2023-03-01", 
        to_date="2023-05-20", 
        order="desc", 
        limit=1
    )

    if len(aggs.close) < 1 or len(aggs.open) < 1 or len(aggs.low) < 1 or len(aggs.high) < 1:
        print(f"Not enough data for {ticker}")
        return False       

    close_price = aggs.close[0]
    open_price = aggs.open[0]
    low_price = aggs.low[0]
    high_price = aggs.high[0]

    body = abs(open_price - close_price)
    total_range = high_price - low_price
    if total_range == 0:  # Check if total_range is zero
        return False
    if body / total_range < 0.33:
        return True

    return False

async def is_bullish_hammer(ticker):
    """
    Checks if the latest candlestick forms a Bullish Hammer.
    The `candles` input is a list of dict with each dict containing the
    'open', 'close', 'high', 'low' prices of a period.
    """
    aggs = await sdk.get_aggregates(

    ticker, 1, "day", 
    from_date="2023-03-01", 
    to_date="2023-05-20", 
    order="desc", 
    limit=100

                )
            
    if len(aggs.close) <= 1 or len(aggs.open) <1 or len(aggs.low) <1 or len(aggs.high) <1:
        print(f"No")
        return False       
    close_prices = aggs.close[0]
    open_prices = aggs.open[0]
    low_prices = aggs.low[0]
    high_prices = aggs.high[0]
    ticker = aggs.ticker[0]


    # Calculate the body and wicks of the candlestick
    body = abs(open_prices - close_prices)
    upper_wick = high_prices - max(open_prices, close_prices)
    lower_wick = min(open_prices, close_prices) - low_prices

    # Check the conditions for a Bullish Hammer:
    # 1. The body is on the upper third part of the candlestick.
    # 2. There is little or no upper wick.
    # 3. The lower wick is at least twice the length of the body.
    if body <= lower_wick / 2 and upper_wick <= body / 2:
        return True
    else:
        return False

async def morning_star(ticker):
    aggs = await sdk.get_aggregates(

    ticker, 1, "day", 
    from_date="2023-03-01", 
    to_date="2023-05-20", 
    order="desc", 
    limit=100

                )
            
    if aggs is None:
        return False
    close_prices = aggs.close
    open_prices = aggs.open
    low_prices = aggs.low
    high_prices = aggs.high
    ticker = aggs.ticker
    if len(close_prices) < 3 or len(open_prices) < 3 or len(high_prices) < 3 or len(low_prices) < 3:
        return False

    # Get the data for the last three candles
    first_open = open_prices[0]
    first_close = close_prices[0]


    second_close = close_prices[1]
    second_high = high_prices[1]
    third_open = open_prices[2]
    third_close = close_prices[2]






    if first_open > second_close and first_open > second_high and \
    second_high < third_close and third_close > third_open and \
    first_close > first_open:
        return True
    else:
        return False
    
async def is_bullish_engulfing(ticker):
    aggs = await sdk.get_aggregates(
        ticker, 1, "day", 
        from_date="2023-03-01", 
        to_date="2023-05-20", 
        order="desc", 
        limit=2
    )

    if len(aggs.close) < 2 or len(aggs.open) < 2:
        print(f"Not enough data for {ticker}")
        return False       

    close_price = aggs.close[0]
    open_price = aggs.open[0]

    previous_close = aggs.close[1]
    previous_open = aggs.open[1]

    if close_price > previous_open and open_price < previous_close:
        return True

    return False


async def is_bearish_engulfing(ticker):
    aggs = await sdk.get_aggregates(
        ticker, 1, "day", 
        from_date="2023-03-01", 
        to_date="2023-05-20", 
        order="desc", 
        limit=2
    )

    if len(aggs.close) < 2 or len(aggs.open) < 2:
        print(f"Not enough data for {ticker}")
        return False       

    close_price = aggs.close[0]
    open_price = aggs.open[0]

    previous_close = aggs.close[1]
    previous_open = aggs.open[1]

    if open_price > previous_close and close_price < previous_open:
        return True

    return False

async def evening_star(ticker):
    aggs = await sdk.get_aggregates(
        ticker, 1, "day", 
        from_date="2023-03-01", 
        to_date="2023-05-20", 
        order="desc", 
        limit=100
    )

    close_prices = aggs.close
    open_prices = aggs.open
    low_prices = aggs.low
    high_prices = aggs.high
    ticker = aggs.ticker
    
    if len(close_prices) < 3 or len(open_prices) < 3 or len(high_prices) < 3 or len(low_prices) < 3:
        return False

    # Get the data for the last three candles
    first_open = open_prices[0]
    first_close = close_prices[0]

    second_open = open_prices[1]
    second_close = close_prices[1]

    third_open = open_prices[2]
    third_close = close_prices[2]

    # Evening Star conditions:
    # 1. First candle is a long bullish candle
    # 2. Second candle is a small body that gaps up from the first candle
    # 3. Third candle is a bearish candle that closes below the midpoint of the first candle's body
    if (first_open < first_close and 
        second_open > first_close and second_close > first_close and 
        third_open < second_close and third_close < second_close and
        third_close < (first_open + first_close) / 2):
        return True
    else:
        return False
