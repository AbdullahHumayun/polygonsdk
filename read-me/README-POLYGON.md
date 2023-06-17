# polygonsdk

POLYGON.IO TOOL-KIT for real time market analysis

# Welcome to new-age market data analysis.

![Example Discord](https://i.imgur.com/ZnBtMy6.gif)

(view discord readme to set-up discord feeds)


## Table of Contents

1. [Introduction](#introduction)

2. [Simulated Markets](#simulated-markets)

3. [Stock Functions](#stock-functions)

4. [Options Functions](#options-functions)

5. [Indices Functions](#indices-functions)

6. [Forex Functions](#forex-functions)

7. [Crypto Functions](#crypto-functions)

8. [EXAMPLES](#examples)

## 1. Introduction <a name="introduction"></a>


Financial markets and the tools available to retail as a whole have been evolving rapidly over the last two years. The quality of data and the ability to find an edge has never been more prevalent - and this tool-kit is designed to do just that.

Polygon.io offers real-time websocket clusters that exceed any other API I've used - and I've used everything from CBOE Livevol to CBOE Hanweck, Nasdaq Datalink, BlackBox Stocks, etc. This by far has the most leverage for true real-time market analysis that can be combined with a multitude of other sources to create a unique view into the ever-changing financial markets.

This is the non-discord specific readme file designed to guide you through the process of utilizing this program. I intend to fully automate the discord side of this program - including Discord server and corresponding webhook creation.

## What you need

1. You'll need to go to https://www.polygon.io and select the package that suits your needs. Polygon offers a free tier for tinkering, as well as higher-grade tiers with real-time data. If you decide to go with anything other than the free version - you can use code FUDSTOP at checkout to recieve a discount on your purchase). Whether you're an options trader, stock trader, crypto trader, index trader, or forex trader - polygon offers it all with various package levels making the data affordable for most people - including a free tier. I've been using their service personally for quite awhile, and am familiar with all data-clusters. 

2. The real-time data is recommended if you plan on using the data for your personal intra-day market analysis. Analyzing markets in this fashion creates a huge advantage - speaking from personal experience. I'm passionate about market finance as well as the data within it, and actively trade options utilizing their options socket. The other tiers offer value as well so it really depends on your own personal needs. This repo is my attempt to show the level of analysis that can be accomplished with this service.

3. I will be updating this as time progresses in an attempt to keep the code clean and organized.

4. If you have any questions - don't hesitate to reach out. I work with financial data every single day, and have no issue helping someone who's stuck.

5. This program contains a custom-made WebullSDK that can change or become unavailable at any time - so please keep this in mind. As long as the code is attainable - I will keep it updated and maintained as needed.

### In case you missed it - you can use the code FUDSTOP at checkout to recieve a discount on your overall purchase.


## Getting Started


#### 1. Download the zip file / clone the repository.

#### 2. Once downloaded - extract to a new folder, and then open the folder in your text editor of choice. (Visual Studio will be shown for demonstration)

#### 3. Install the necessary dependencies:

```
pip install -r requirements.txt
```


### 4. Copy your API key from https://www.polygon.io by clicking the "Dashboard" in the upper right corner and going to the Api Keys section.
    After you copy your key, paste it into the **cfg.py** in-between the quotations for the **YOUR_API_KEY** attribute.

![Example Screenshot](https://i.ibb.co/K6pbkpK/replaceme.png)

#### 5. Get market-wide data for your subscription feed that you went with.

        Inside of the get_data folder - you will find 5 files corresponding to each of the different subscriptions polygon offers. Pick the one(s)
        you want, and simply run the code to recieve a fresh spreadsheet of data for that market.

## If you went with the STOCKS data:

   To get started with capturing market-wide data to analyze further - select the "get_all_tickers.py" and run the file.
   This will save a CSV file with all of the up-to-date market data for stocks that we can utilize for simulated market testing during
   non-market hours. Weekends are some of the best times to analyze markets as the data freezes for a full 48 hours to allow thorough analysis.


## If you went with the INDICES data:

  To gather all up-to-date indices snapshots, simply select the "get_all_indices_data.py" file and run it - and you'll now have a CSV file under 'files/indices' to utilize.
  
  
## If you went with the OPTIONS data:

  To gather all up-to-date options data (recommended to specify by expiration date and/or strike here - as this can take a significant amount of time due to the vast amount of options), select the
  'get_all_options_data.py' file and run it. Depending on your computer - you can adjust the "MAX_SIMULTANEOUS_REQUESTS" to control how fast or slow you gather the options based on your personal
  computer. You can adjust this in the **sdks/polygon_sdk/options_market/async_options_sdk.py** file.
   
 When you run the file - it may take awhile - and you'll see the terminal begin to print out data confirming that you are collecting the option snapshots:

![Options Part1](https://i.ibb.co/257qG2d/options-part1.png")

After this first portion is complete - you'll then see the data being parsed and stored into the appropriate CSV file moving at a much faster rate in the terminal.

![Options Part2](https://i.ibb.co/3WYHr1D/options-par2.png)


Once this process completes - you can now view the file in **files/options/all_options_data.csv** 

You have collected all options market-wide to analyze how you wish.


## If you went with the FOREX/CRYPTO data:

  To gather all of the up-to-date forex data, simply run the **get_latest_forex_data.py** file and view the spreadsheet saved in **files/forex/all_forex_snapshots.py**.

  To gather all of the up-to-date crypto data, simply run the **get_latest_crypto_data.py** file and view the spreadsheet saved in **files/crypto/all_crypto_snapshots.py**.
  
  
  

---
A confirmation message should print when the csv files complete:

![Confirmation Example](https://i.ibb.co/2gXX1hq/datasaved.png)
### Now you should have up-to-date market data across all subscriptions and across all tickers for each data-type.
You can find the csv files in their respective folders within the **files** parent folder.


--- 

This tutorial should be plug and play - meanining the only code you should have to add is your API key - and the rest should be able to get you started fairly easily!


## 2. Simulated Markets <a name="simulated-markets"></a>


---
### Creating Simulated Markets with up-to-date data (for stocks and option use when markets are closed)
---

### Run the simulated markets inside the simulated_markets folder.

    
    Ensure they work - and view the speed at which you can expect to utilize the real-time websocket clusters.

    You can easily add / manipulate the attributes and bring in other functions from the built-in SDKS as you wish.

    More examples for this will be added in the near future.

    The majority of the functions are able to be used with dot-notation, making it very easy to pick and choose
    the attributes you wish to analyze either in real-time or as needed.

    Easily build applications and systems to monitor financial markets with this tool-set! I will be 

    providing several examples of how to do this.

![Dot notation - Attributes 1](https://i.ibb.co/LNr5YQv/dot-notation.png)

![Dot notation - Attributes 2](https://i.ibb.co/RDcLYXW/dot-notation2.png)

![Dot notation - Attributes 3](https://i.ibb.co/kxTPWF6/dot-notation3.png)

You can easily define them like so to customize your terminal output for analysis:

![Example 1- Attributes](https://i.ibb.co/gjFLNfV/example1.png)

This will output the following when running the script:

![Example 2 - Script](https://i.ibb.co/1vHNTcs/example21.png)


From here - you can basically get as creative as you want. You can bring in additional functions from the SDKs - which I will provide examples for soon.

Here's a more refined approach to identify specific conditions:


Add this code above the 'handle_msg' function:


``````
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY
polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)
``````




Then modify the handle_msg function as follows:

``````
    async def handle_msg(msgs: List[TestStocksEvent]):
    file_name = 'files/stocks/met_conditions.txt'
    for m in msgs:
        # Define the attributes
        symbol = m.symbol
        price = m.last_price
        last_trade_size = float(m.last_size)
        volume = float(m.volume)
        previous_volume = float(m.prev_volume)

        # Check the conditions
        if volume > (previous_volume * 1.5) and price <= 25 and last_trade_size >= 10000:
            # Append the symbol to the text file
            with open(file_name, 'a') as file:
                file.write(symbol + '\n')
``````


This handle_msg function processes a list of TestStocksEvent objects, which represent stock events. For each stock event, it extracts the relevant attributes such as symbol, price, last_trade_size, volume, and previous_volume.

It then checks if the following conditions are met:

The current volume is more than 1.5 times the previous volume.
The price is less than or equal to 25.
The last trade size is greater than or equal to 10,000.


Get creative with it. This is just a minor example. Lots more to cover.


### Simulated Options Market

Open the **mock_options_market.py** file after you have successfully gathered your options data from **get_latest_options_data.py**.

Run the script to begin processing the data.


## 3. Stock Functions <a name="stock-functions"></a>


### 1. Stock Aggregates
    USE CASE:
    
    1. Historical Analysis: Analyze historical stock data by fetching aggregated information such as open, high, low, close prices, and volume for a specific stock ticker over a specified time span. 

    2. Trading Strategy Development: Use the function to access aggregated data for backtesting trading strategies, studying price patterns, and analyzing volume trends.

    3. Market Research and Visualization: Utilize the aggregated data for market research, generating charts, and visualizing stock price trends and volume patterns.

    4. Data Analysis and Machine Learning: Incorporate the aggregated data into data analysis and machine learning workflows for tasks like stock market prediction, feature engineering, and model building.


    Usage:
    ```python
        """
        Retrieve aggregate data for a given stock ticker.

        :param stock_ticker: The stock ticker symbol as a string.
        :param multiplier: The multiplier for the timespan as an integer.
        :param timespan: The timespan as a string (e.g., "minute", "hour", "day", "week", "month", "quarter", "year").
        :param from_date: The start date for the data as a string in YYYY-MM-DD format.
        :param to_date: The end date for the data as a string in YYYY-MM-DD format.
        :param order: The order in which to display the results.
        :param limit: The limit of aggregates to gather. Adjust based on time needs.
        :return: An instance of AggregatesData containing the aggregate data.
        """
        ```
    
``````python
import pandas as pd

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY, five_days_ago_str, today_str

polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)
#ticker="META"

async def stock_aggregates(ticker):

    stock_aggregates_data = await polygonsdk.get_aggregates(

        ticker=ticker,
        multiplier=1,
        timespan="day",
        from_date=five_days_ago_str, 
        to_date=today_str, 
        order="desc"

        )
    
    open = stock_aggregates_data.open
    close = stock_aggregates_data.close
    high = stock_aggregates_data.high
    low = stock_aggregates_data.low
    volume = stock_aggregates_data.volume
    vwap = stock_aggregates_data.volume_weighted_average
    timestamp = await polygonsdk.format_timestamps_list(stock_aggregates_data.timestamp)

    # Display the retrieved data
    print(f"Open Prices: {open}")
    print(f"Close Prices: {close}")
    print(f"High Prices: {high}")
    print(f"Low Prices: {low}")
    print(f"Volume: {volume}")
    print(f"VWAP: {vwap}")
    print(f"Timestamps: {timestamp}")



    df = pd.DataFrame(stock_aggregates_data.results)
    df[timestamp] = pd.to_datetime(df['t'], unit='ms')
    df.to_csv(f'files/stocks/{ticker}_aggregates.csv')


asyncio.run(main())

#output in ASCENDING order by time (for charting):

#Open Prices: [20.46, 20.16, 20.45, 20.69, 20.83]
#Close Prices: [20.51, 20.24, 20.76, 20.88, 20.69]
#High Prices: [20.99, 20.65, 20.96, 21.16, 20.98]
#Low Prices: [20.0904, 20.1204, 20.38, 20.51, 20.23]
#Volume: [2402799.0, 1522674.0, 2139945.0, 1652512.0, 2006061.0]
#VWAP: [20.6108, 20.3216, 20.7405, 20.8441, 20.5956]
#Timestamps: ['2023/05/07 11:00 PM', '2023/05/08 11:00 PM', '2023/05/09 11:00 PM', '2023/05/10 11:00 PM', '2023/05/11 11:00 PM'] 

#output in DESCENDING order by time (for conditional checks):

#Open Prices: [20.83, 20.69, 20.45, 20.16, 20.46]
#Close Prices: [20.69, 20.88, 20.76, 20.24, 20.51]
#High Prices: [20.98, 21.16, 20.96, 20.65, 20.99]
#Low Prices: [20.23, 20.51, 20.38, 20.1204, 20.0904]
#Volume: [2006061.0, 1652512.0, 2139945.0, 1522674.0, 2402799.0]
#VWAP: [20.5956, 20.8441, 20.7405, 20.3216, 20.6108]
#Timestamps: ['2023/05/11 11:00 PM', '2023/05/10 11:00 PM', '2023/05/09 11:00 PM', '2023/05/08 11:00 PM', '2023/05/07 11:00 PM']
``````
#Dataframe output:

|  GME  | Open  | Close | High  | Low    | Volume     | VWAP    | Timestamps  |
|-------|-------|-------|-------|--------|------------|---------|-------------|
| Day 1 | 20.83 | 20.69 | 20.98 | 20.23  | 2006061.0  | 20.5956 | 2023/05/11  |
| Day 2 | 20.69 | 20.88 | 21.16 | 20.51  | 1652512.0  | 20.8441 | 2023/05/10  |
| Day 3 | 20.45 | 20.76 | 20.96 | 20.38  | 2139945.0  | 20.7405 | 2023/05/09  |
| Day 4 | 20.16 | 20.24 | 20.65 | 20.1204| 1522674.0  | 20.3216 | 2023/05/08  |
| Day 5 | 20.46 | 20.51 | 20.99 | 20.0904| 2402799.0  | 20.6108 | 2023/05/07  |




### 2. Relative Strength Index:

   Usage: Retrieve RSI data with up to 50,000 datapoints with customizable window.
   Default window: 14
   
   Timespans: minute, hour, day, week, month, quarter, year

```python

import asyncio

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY

polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)

#ticker="META"
async def rsi(ticker):


    rsi_data = await polygonsdk.get_rsi(ticker=ticker, timespan="hour", adjusted=True, window=14, limit=500)
    print(rsi_data) #returns a list of RSI values


asyncio.run(rsi())
```


### 3. Moving Average Convergence / Divergence Indicator (MACD):

 Usage: Retrieve MACD data, signal data, and histogram data with up to 50,000 datapoints with customizable windows.
 Default windows: 
                short window: 12
                long window: 26
                signal window: 9

 Timespans: minute, day, hour, week, month, quarter, year

   
```python

import asyncio

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY

polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)

async def macd(ticker):


    macd, histogram, signal = await polygonsdk.get_macd(ticker,timespan="day",adjusted=True,short_window=12,long_window=26,signal_window=9,series_type="close")

    print(f"MAC-D DATA: {macd}")
    print()
    print(f"MAC-D HISTOGRAM DATA: {histogram}")
    print()
    print(f"MAC-D SIGNAL DATA: {signal}")
asyncio.run(macd())
```

### 4. Simple Moving Average (SMA)

   Usage: Return the SMA values for a given timespan for a ticker with up to 50,000 datapoints with customizable windows.
   Windows: If you want the 50/21 MAs - use windows 50 and 21 respectively.
   Timespans: minute, day, hour, week, month, quarter, year
   
   Returns the latest value, underlying VWAP price, value_trend, and historic_values.
   
```python

import asyncio

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY

polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)


async def simple_moving_average(ticker):

    sma_50, vwap, sma50_trend, sma50_historic = await polygonsdk.get_simple_moving_average(ticker=ticker,timespan="minute",adjusted=True,window=50, limit=500) #for 50 MA

    sma_21, vwap, sma21_trend, sma21_historic = await polygonsdk.get_simple_moving_average(ticker=ticker,timespan="minute",adjusted=True,window=21, limit=500) #for 21 MA

    print(f"SMA 50 TREND: {sma50_trend}")
    print()
    print(f"SMA 50 HISTORIC: {sma50_historic}")
    print()
    print(f"SMA 21 HISTORIC: {sma21_historic}")
    print()
    print(f"LATEST SMA21: {sma_21} on the")
    print(f"LATEST SMA50: {sma_50}")
    print(f"VWAP PRICE for {ticker}: ${vwap}")
    print(f"SMA 21 TREND: {sma21_trend}")


await asyncio.run(simple_moving_average())
```
   
### 5. Exponential Moving Average (EMA)

   Usage: Return the EMA values for a given timespan for a ticker with up to 50,000 datapoints with customizable windows.
   Windows: If you want the 50/21 EMAs - use windows 50 and 21 respectively.
   Timespans: minute, day, hour, week, month, quarter, year

   Returns the latest value, underlying VWAP price, value_trend, and historic_values.

```python

import asyncio

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY

polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)


async def exponential_moving_average(ticker):

    ema_50, vwap, ema50_trend, ema50_historic = await polygonsdk.get_exponential_moving_average(ticker=ticker,timespan="minute",adjusted=True,window=50, limit=500) #for 50 EMA

    ema_21, vwap, ema21_trend, ema21_historic = await polygonsdk.get_exponential_moving_average(ticker=ticker,timespan="minute",adjusted=True,window=21, limit=500) #for 21 EMA

    print(f"EMA 50 TREND: {ema50_trend}")
    print()
    print(f"EMA 50 HISTORIC: {ema50_historic}")
    print()
    print()
    print(f"EMA 21 HISTORIC: {ema21_historic}")
    print()
    print(f"LATEST EMA21: {ema_21}")
    print(f"LATEST EMA50: {ema_50}")
    print(f"VWAP PRICE for {ticker}: ${vwap}")
    print(f"EMA 21 TREND: {ema21_trend}")

await asyncio.run(exponential_moving_average())
```

### 6. Support and Resistance Levels
   Usage: Plot support / resistance across any timeframe using aggregates data.
   
   Choose a multiplier and a timespan and a date-range to gather the support / resistance
   data.
   
   A multiplier of 26 and a timespan of 'day' would mean you're looking for support / resistance
   on the 26 day timeframe.
   
   
   A multiplier of 25 and a timespan of 'minute' would mean you're looking for support / resistance
   on the 25 minute timeframe.
   
   Returns: support and resistance levels for the ticker.
   
```python
import asyncio

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY, five_days_ago_str, today_str

polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)
ticker="GME"

async def support_resistance(ticker):

    support, resistance = await polygonsdk.get_support_resistance_levels(stock_ticker="GME",multiplier=30,timespan='minute',from_date=five_days_ago_str,to_date=today_str)
    print(support)
    print(resistance)
asyncio.run(support_resistance(ticker))
```
  
  When plotted:
  
  ![Support Resistance Example 30 minute](https://i.ibb.co/4TRQctL/support-resistance.png)
  
  
### 7. Latest Ticker News:

   Usage: Retrieve the latest ticker narrative for a stock, or list of ticker narratives.

   Returns publisher information, published time, mentioned tickers, keywords, a description, image,
   and title.


```python
import asyncio

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY

polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)
ticker="AAPL"

async def news(ticker):

    news = await polygonsdk.get_ticker_narrative(ticker)
    desc=[i.description for i in news]
    news_keywords = [i.keywords for i in news]
    mentioned_tickers = [i.tickers for i in news]
    published = [i.pub_time for i in news]
    news_url = [i.news_url for i in news]
    publisher_homepage = [i.homepage_url for i in news]
    news_image = [i.image_url for i in news]
    publisher_logo = [i.logo_url for i in news]
    publisher_name = [i.name for i in news]
    title = [i.title for i in news]

    print(f"Latest News for {ticker[0]}:")
    print()
    print(f"Title: {title[0]}")
    print()
    print(f"Description: {desc[0]}")
    print()
    print(f"Source URL: {news_url[0]}")
    print(f"Published: {published[0]}")
    print(f"Publisher: {publisher_name[0]}")
    print(f"Publisher Website: {publisher_homepage[0]}")
    print(f"Publisher Logo: {publisher_logo[0]}")
    print(f"News Image: {news_image[0]}")
    print()
    print(f"News Keywords: {news_keywords[0]}")
    print(f"Tickers Mentioned: {mentioned_tickers[0]}")

asyncio.run(news(ticker))

#output:

#Title: What's Fueling Meta's 92% Share-Price Jump This Year?

#Description: Investor optimism -- fueled by Meta's efficiency -- is pushing the stock higher.

#Source URL: None
#Published: 2023-05-13T13:51:00Z
#Publisher: The Motley Fool
#Publisher Website: https://www.fool.com/
#Publisher Logo: https://s3.polygon.io/public/assets/news/logos/themotleyfool.svg       
#News Image: https://g.foolcdn.com/editorial/images/732077/pressing-the-facebook-like-button.jpg

#News Keywords: ['investing']
#Tickers Mentioned: ['META']
```


### 8. Check for bullish MACD cross and oversold RSI on the specified timespan:

```python

import asyncio

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.polygon_sdk.technical_conditions import check_macd_condition,check_rsi_condition

from cfg import YOUR_API_KEY

polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)
ticker="AAPL"

async def _(ticker):
    macd, histogram, signal = await polygonsdk.get_macd(ticker, timespan="hour")

    rsi = await polygonsdk.get_rsi(ticker, timespan="hour")


    rsi = rsi[0] # get the latest value

    histogram = histogram[::1] # get the histogram

    macd_check = check_macd_condition(macd) #checks for iminent bullish MACD cross
    rsi_check = check_rsi_condition(rsi) #checks for oversold RSI (30 or less)

    print(macd_check, rsi_check)

asyncio.run(_(ticker))
```


### 9. Get Pivot Points
Find support / resistance 1 and 2 + the pivot points for any ticker:

```python

import asyncio 

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK

from cfg import YOUR_API_KEY

poly = AsyncPolygonSDK(YOUR_API_KEY)
async def pivot_point():



    _ = await poly.get_pivot_points("GME", 1, "day", from_date="2023-05-01", to_date="2023-05-16")
    print(f"RESISTANCE: ${_.resistance1} ${ _.resistance2}")
    print(f"PIVOT POINT: ${_.pivot_point}")
    print(f"SUPPORT: ${_.support1} ${_.support2}")

    

asyncio.run(pivot_point())
```

### Get the ROC (Rate of Change)

1. **Trend Reversals**: ROC can be used to identify potential trend reversals by looking for a divergence between the ROC and the price. If the price is making higher highs while the ROC is making lower highs, it could indicate a bearish reversal. Conversely, if the price is making lower lows while the ROC is making higher lows, it could signal a bullish reversal.

2. **Overbought/Oversold Conditions**: ROC can help identify overbought or oversold conditions in the market. When the ROC is at an extreme high, it suggests that the security may be overbought and due for a price correction. Conversely, when the ROC is at an extreme low, it indicates that the security may be oversold and could be due for a price rebound.

3. **Price Movements**: ROC measures the strength of price movements. A rising ROC indicates increasing momentum, suggesting that the security's price is moving higher at an accelerating rate. Conversely, a falling ROC indicates decreasing momentum, suggesting that the security's price is moving lower at a decelerating rate.

```python

import asyncio


from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY, today_str

poly = AsyncPolygonSDK(YOUR_API_KEY)
ticker = "MSFT"

async def main():

    roc = await poly.get_rate_of_change(ticker, "day", 1, from_date="2023-04-01", to_date=today_str, window=10)
    print(roc)

asyncio.run(main())
```

### BOLLINGER BANDS:

Get the bollinger bands for a ticker:


```python


import asyncio

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY, today_str

poly = AsyncPolygonSDK(YOUR_API_KEY)
ticker = "NVDA"

async def main():

    x = await poly.get_bollinger_bands(symbol="GME",multiplier=1, timespan="hour", from_date="2023-01-01", to_date=today_str, window=20, num_std_dev=2)
    for i in x:
        print(i)

asyncio.run(main())
```
## 4. Options Functions <a name="options-functions"></a>


### Generating a Symbol to use for other functions

>>> Sometimes, you'll want to easily get an options symbol to use for processing trades, aggregates,
or other data.

You can easily generate an option symbol utilzing the built-in **generate_option_symbol** 
function within the PolygonOptionsSDK:

```python
"""YOUR MAIN FILE TO CONDUCT MARKET ANALYSIS"""

import asyncio

from cfg import YOUR_API_KEY

from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK

polyoptions = PolygonOptionsSDK(YOUR_API_KEY)


underlying_symbol = "F"
expiration_date = "2023-05-19"
option_type = "C"
strike_price = 11.5

async def get_option_symbol():

    option_symbol = await polyoptions.generate_option_symbol(
        underlying_symbol=underlying_symbol, 
        expiration_date=expiration_date, 
        option_type=option_type, 
        strike_price=strike_price)
    print(option_symbol)
    



# Run the main function
asyncio.run(get_option_symbol())
```


### GET OPTION QUOTES

This function provides example of how to generate an option symbol
using the SDK to then easily call additional functions.

Using options quotes as an example - you can easily specify your
date range, and immediately have quotes for a specified contract
saved to a CSV file for further analysis:

```python

import asyncio
from datetime import datetime
import pandas as pd

from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from sdks.polygon_sdk.helpers.helpers import get_date_string

from cfg import YOUR_API_KEY

now = datetime.now()
sdk = PolygonOptionsSDK(YOUR_API_KEY)

async def main():
    """
    Main function to retrieve option quotes and save them to a CSV file.

    The date range for fetching option quotes can be adjusted by modifying the value of `num_days_ago`.
    A negative value represents days in the past, and a positive value represents days in the future.
    For example, `num_days_ago = -50` will fetch option quotes from 50 days ago until today.
    """

    # Specify the option details
    underlying_symbol = "SPY"
    expiration_date = "2023-05-15"
    option_type = 'C'
    strike_price = '417'

    # Generate the option symbol
    option_symbol = await sdk.generate_option_symbol(underlying_symbol, expiration_date, option_type, strike_price)

    # Specify the date range for fetching option quotes
    num_days_ago = get_date_string(-50)
    today_str = datetime.today().strftime('%Y-%m-%d')

    option_quote = await sdk.get_option_quote(option_symbol=option_symbol, order="desc", limit=50000, timestamp_lte=today_str, timestamp_gte=num_days_ago)

    # Create a DataFrame from the option quotes
    df = pd.DataFrame(option_quote.to_dict())


    csv_filename = f'files/options/quotes/{option_symbol[2:]}_{num_days_ago.replace("-", "")}.csv'
    df.to_csv(csv_filename)

asyncio.run(main())
```

After running the file above, found in the **options_examples** folder, you'll have
the CSV file saved at which point you can load into excel:

![Excel Example](https://i.ibb.co/M5LCBy5/optquote.png)

Then - depending on your excel version - simply click

'Analyze Data' after highlighting it all, and you

get instant visualization of that option.

For example, to visualize the frequency of the ask price,
you hit *analyze data* at the top right of Excel, and then
look through the auto-generated data charts to find frequency
of ask price, or the price traders are buying this particular 
option for most often:

![Excel Chart](https://i.ibb.co/S0tzJyc/EXAMPLEOPTIONQUOTE.png)


### GET OPTION TRADES

```python

import asyncio

import pandas as pd

from cfg import YOUR_API_KEY

from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK

polyoptions = PolygonOptionsSDK(YOUR_API_KEY)
poly = AsyncPolygonSDK(YOUR_API_KEY)

underlying_symbol = "F"
expiration_date = "2023-05-19"
option_type = "C"
strike_price = 11.5

async def get_trades():


    #in order to use the trades function - you'll first need the symbol:
    
    option_symbol = await polyoptions.generate_option_symbol(underlying_symbol=underlying_symbol, expiration_date=expiration_date, option_type=option_type, strike_price=strike_price)
    print(option_symbol) #symbol used for further analysis below


    opt_trades = await polyoptions.get_option_trades(symbol=option_symbol, limit=100)
    
    condition_name = [i.conditions for i in opt_trades]
    price = [i.price for i in opt_trades]
    size=  [i.size for i in opt_trades]
    sip_timestamp = [i.sip_timestamp for i in opt_trades]
    exchange = [i.exchange for i in opt_trades]

    df = pd.DataFrame({
        'Condition': condition_name,
        'Price': price,
        'Size': size,
        'Sip Timestamp': sip_timestamp,
        'Exchange': exchange
    })


    df.to_csv(f'files/options/trades/{underlying_symbol}{option_type}{strike_price}_trades.csv')

    print(condition_name)

#asyncio.run(get_trades())


#COPY THIS CODE TO ROOT FOLDER
```


### Get all option chains for any ticker, store data as csv file:

```python
import asyncio
import pandas as pd

from cfg import YOUR_API_KEY

from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK


webull = AsyncWebullSDK()
poly = AsyncPolygonSDK(YOUR_API_KEY)
polyoptions = PolygonOptionsSDK(YOUR_API_KEY)

ticker="GME"
async def fetch_entire_chain():
    all_options = await polyoptions.get_option_chain_all(ticker)



    # Create a DataFrame from the dictionary
    df = pd.DataFrame([option.to_dict() for option in all_options])
    # Save the DataFrame to a CSV file
    df.to_csv(f'files/options/ticker_chains/all_{ticker}_chains.csv', index=False)

# Run the main function
asyncio.run(fetch_entire_chain())
```



# EXAMPLES  <a name="examples"></a>

With so many metrics to work with - you can scan for specific criteria
for your specific research or trading needs. This is an example using fresh options snapshot data.

Here's an example script that checks for specific IV ranges, a tight bid/ask spread
for liquidity, a specific bid-ask range, unusual volume (OI > VOL).

There are so many possibilities here for testing / analysis.

---

## 1 - OPTIONS MARKET SCANNER

In this example script - you are scanning for specific option criteria - and when the criteria is met -
the matching option Symbol is saved to CSV file in the **files** folder:

```python
import sys
import os


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from typing import List
from asyncio import Queue
import random
import csv
import asyncio
import pandas as pd
from sdks.helpers.helpers import human_readable
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from sdks.models.test_events import TestOptionsEvent, option_condition_dict, OPTIONS_EXCHANGES

from sdks.helpers.helpers import extract_underlying_symbol
from simulated_markets.helpers import write_to_csv
from cfg import YOUR_API_KEY
from cachetools import TTLCache
sdk = PolygonOptionsSDK(YOUR_API_KEY)
df = pd.read_csv('files/options/all_options_data.csv') #you get this file from the get_data folder - run 'get_all_options_data.py'

async def handle_msg(queue: asyncio.Queue, msgs: List[TestOptionsEvent]):
    tasks = []
    for m in msgs:
        option_symbol = m.ticker
        underlying_ticker = m.underlying_ticker
        tasks.append(queue.put((option_symbol, underlying_ticker)))
        await process_snapshot(option_symbol, underlying_ticker)

    await asyncio.gather(*[task for task in tasks if task is not None])

snapshot_cache = TTLCache(maxsize=2000, ttl=60)
# Bounded semaphore to limit concurrent tasks1
semaphore = asyncio.BoundedSemaphore(40)
async def send_messages(handler):
    while True:
        # Select a random row from the DataFrame
        index = random.randint(0, len(df) - 1)
        row = df.iloc[index]

        # Create TestOptionsEvent object from row data
        event = TestOptionsEvent.from_row(row)

        # Print the created TestOptionsEvent object


        await handler([event])


async def process_snapshot(option_symbol: str, underlying_ticker):

    async with semaphore:

        snapshot = await sdk.get_option_contract_snapshot(underlying_asset=underlying_ticker, option_contract=option_symbol)




        # Option Symbol Details
        option_symbol = snapshot.option_symbol
        strike_price = snapshot.strike_price
        contract_type = snapshot.contract_type
        expiration_date = snapshot.expiration_date
        break_even_price = snapshot.break_even_price

        # Day Information
 
        day_change_percent = snapshot.day_change_percent
        day_volume = snapshot.day_volume
        day_vwap = snapshot.day_vwap


        # Greeks and Volatility
        delta = snapshot.delta
        implied_volatility = snapshot.implied_volatility
        open_interest = snapshot.open_interest

        # Quote Data
        ask = snapshot.ask
        ask_size = snapshot.ask_size
        bid = snapshot.bid
        bid_size = snapshot.bid_size

        # Trade Information
        conditions = snapshot.conditions
        underlying_price = snapshot.underlying_price

        results = []

        print(f"Snapshot Processed for {human_readable(option_symbol)}")
        # Check if the option meets the below criteria
        if (implied_volatility is not None 
            and implied_volatility <= 0.53 
            and implied_volatility >= 0.22
            and underlying_price >= 5 
            and bid >= 0.07 
            and ask <= 2.00
            and abs(bid - ask) <= 0.03
            and bid_size is not None
            and ask_size is not None
            and day_volume is not None
            and open_interest is not None
            and day_volume > (open_interest * 2)):
            
 
                
            results.append({"Underlying": underlying_ticker, "Strike Price": strike_price, "Contract Type": contract_type, "Expiration Date": expiration_date, "Day Volume": day_volume, "Day VWAP": day_vwap, "Open Interest": open_interest, "Delta": delta, "Day Change Percent": day_change_percent, "Implied Volatility": implied_volatility, "Underlying Price": underlying_price, "Break Even Price": break_even_price})

        # Save the results to a CSV file
        for result in results:
            write_to_csv(result)



async def worker(queue: asyncio.Queue):
    while True:
        option_symbol, symbol = await queue.get()
        await process_snapshot(option_symbol, symbol)
        queue.task_done()


async def main():
    # Create a queue to pass symbols between handle_msg and workers
    queue = asyncio.Queue()

    # Create a fixed number of worker tasks
    num_workers = 4
    worker_tasks = [asyncio.create_task(worker(queue)) for _ in range(num_workers)]

    await send_messages(lambda msgs: handle_msg(queue, msgs))

    # Cancel the worker tasks
    for task in worker_tasks:
        task.cancel()

    # Wait for the worker tasks to finish
    await asyncio.gather(*worker_tasks, return_exceptions=True)




asyncio.run(main())
```

The above example uses a bounded sephamore / queue logic to increase performance.

Cacheing can also be implemented to further enhance performance.




### 2 - GAP FINDER WITH FILLED TIMESTAMPS

This function allows you to incorporate gap-finding logic into your strategy:

```python

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
import asyncio
from cfg import YOUR_API_KEY

sdk = AsyncPolygonSDK(YOUR_API_KEY)
async def main():


    aggs = await sdk.get_aggregates("SPY", 60, "minute", from_date="2023-01-01", to_date = "2023-05-16",limit = 2000)
    close = aggs.close
    open = aggs.open
    high = aggs.high
    low = aggs.low
    time = aggs.timestamp
    _ = await sdk.find_gaps(open, high, low, close, time)
    print(_)



asyncio.run(main())
```

OUTPUT:

| Type   | Dates      | Indices | Gap Low | Gap High | Filled Timestamp   |
|--------|------------|---------|---------|----------|--------------------|
| Gap-up | 2023-01-04 | 16      | 381.11  | 382.0    | 2023-01-04 04:00:00 |
| Gap-up | 2023-01-05 | 33      | 383.6   | 383.59   | 2023-01-05 07:00:00 |
| Gap-up | 2023-01-09 | 64      | 387.83  | 388.37   | 2023-01-09 14:00:00 |
| Gap-up | 2023-01-10 | 80      | 387.66  | 386.91   | 2023-01-10 07:00:00 |
| Gap-up | 2023-01-18 | 160     | 396.86  | 397.77   | 2023-01-18 04:00:00 |
| Gap-up | 2023-01-26 | 256     | 401.08  | 400.73   | 2023-01-26 09:00:00 |
| Gap-up | 2023-02-02 | 336     | 412.44  | 412.24   | 2023-02-02 05:00:00 |
| Gap-up | 2023-02-06 | 383     | 410.65  | 410.54   | 2023-02-07 03:00:00 |
| Gap-up | 2023-02-08 | 402     | 414.32  | 413.56   | 2023-02-08 06:00:00 |
| Gap-up | 2023-02-09 | 416     | 411.43  | 413.02   | 2023-02-09 07:00:00 |
| Gap-up | 2023-02-09 | 417     | 414.65  | 414.21   | 2023-02-09 05:00:00 |
| Gap-up | 2023-02-10 | 432     | 407.35  | 405.85   | 2023-02-10 09:00:00 |


![Gaps Output](https://i.ibb.co/smpqhKY/gaps.png)

