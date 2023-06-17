# Webull SDK Toolkit

The data in this program could change or stop working at any time due to endpoint name changes, 

attribute name changes, etc.

As of last week - Webull has released their OpenAPI for trading.

I would recommend checking it out at https://www.webull.com

All pricing data in this toolkit will be real-time granularity.

Useful functions inside of this SDK:

---

### Functions found herein:


## Table of Contents

1. [Analyze Capital Flow](#analyze-capital-flow)

2. [Calculate Ratios](#calculate-ratios)

3. [Calculate Score](#calculate-score)

4. [Check Recent News](#check-recent-news)

5. [Get Analysis Data](#get-analysis-data)

6. [Get Cash Flow](#get-cash-flow)

7. [Get Earnings Calendar](#get-earnings-calendar)

8. [Get ETF Categories](#get-etf-categories)

9. [Get Financial Statement](#get-financial-statement)

10. [Get Institutional Holdings](#get-institutional-holdings)

11. [Get Option Data](#get-option-data)

12. [Get Short Interest](#get-short-interest)

13. [Get Webull News](#get-webull-news)

14. [Get Webull Stock Data](#get-webull-stock-data)

15. [Get Webull Vol Analysis Data](#get-webull-vol-analysis-data)

16. [Top Options Chains](#top-options-chains)

17. [Top Options Tickers](#top-options-tickers)

## Analyze Capital Flow <a name="analyze-capital-flow"></a>

```python
import asyncio
from webull_sdk import AsyncWebullSDK

async def main():
    webull = AsyncWebullSDK()
    capital_flow = await webull.capital_flow("AAPL")
    print(capital_flow)

asyncio.run(main())
```

## Calculate Ratios <a name="calculate-ratios"></a>

```python
import asyncio
from webull_sdk import AsyncWebullSDK

async def main():
    webull = AsyncWebullSDK()
    balance_sheet = await webull.get_balancesheet("AAPL")
    fin_statement = await webull.get_financial_statement("AAPL")
    cashflow = await webull.get_cash_flow("AAPL")
    market_price = 150  # Example market price
    ratios = await webull.calculate_ratios(balance_sheet, fin_statement, cashflow, market_price)
    print(ratios)

asyncio.run(main())
```

## Calculate Score <a name="calculate-score"></a>

```python
import asyncio
from webull_sdk import AsyncWebullSDK

async def main():
    webull = AsyncWebullSDK()
    score = await webull.financial_score("AAPL")
    print(score)

asyncio.run(main())
```

## Check Recent News <a name="check-recent-news"></a>

```python
import asyncio
from webull_sdk import AsyncWebullSDK

async def main():
    webull = AsyncWebullSDK()
    recent_news = await webull.get_recent_news_for_tickers(["AAPL", "GOOGL", "TSLA"])
    print(recent_news)

asyncio.run(main())
```

## Get Analysis Data <a name="get-analysis-data"></a>

```python
import asyncio
from webull_sdk import AsyncWebullSDK

async def main():
    webull = AsyncWebullSDK()
    analysis_data = await webull.get_analysis_data("AAPL")
    print(analysis_data)

asyncio.run(main())
```

## Get Cash Flow <a name="get-cash-flow"></a>

```python
import asyncio
from webull_sdk import AsyncWebullSDK

async def main():
    webull = AsyncWebullSDK()
    cash_flow = await webull.get_cash_flow("AAPL")
    print(cash_flow)

asyncio.run(main())
```

## Get Earnings Calendar <a name="get-earnings-calendar"></a>

```python
import asyncio
from webull_sdk import AsyncWebullSDK

async def main():
    webull = AsyncWebullSDK()
    earnings_calendar = await webull.get_earnings_calendar("2022-02-10")
    print(earnings_calendar)

asyncio.run(main())
```

## Get ETF Categories <a name="get-etf-categories"></a>

```python
import asyncio
from webull_sdk import AsyncWebullSDK

async def main():
    webull = AsyncWebullSDK()
    etf_categories = await webull.get_etf_categories("commodity")
    print(etf_categories)

asyncio.run(main())
```

## Get Financial Statement <a name="get-financial-statement"></a>

```python
import asyncio
from webull_sdk import AsyncWebullSDK

async def main():
    webull = AsyncWebullSDK()
    financial_statement = await webull.get_financial_statement("AAPL")
    print(financial_statement)

asyncio.run(main())
```

## Get Institutional Holdings <a name="get-institutional-holdings"></a>

```python
import asyncio
from webull_sdk import AsyncWebullSDK

async def main():
    webull = AsyncWebullSDK()
    institutional_holdings = await webull.get_institutional_holdings("AAPL")
    print(institutional_holdings)

asyncio.run(main())
```

## Get Option Data <a name="get-option-data"></a>

```python
import asyncio
from webull_sdk import AsyncWebullSDK

async def main():
    webull = AsyncWebullSDK()
    option_data = await webull.get_option_data("AAPL")
    print(option_data)

asyncio.run(main())
```

## Get Short Interest <a name="get-short-interest"></a>

```python
import asyncio
from webull_sdk import AsyncWebullSDK

async def main():
    webull = AsyncWebullSDK()
    short_interest = await webull.get_short_interest("AAPL")
    print(short_interest)

asyncio.run(main())
```

## Get Webull News <a name="get-webull-news"></a>

```python
import asyncio
from webull_sdk import AsyncWebullSDK

async def main():
    webull = AsyncWebullSDK()
    webull_news = await webull.get_webull_news("AAPL")
    print(webull_news)

asyncio.run(main())
```

## Get Webull Stock Data <a name="get-webull-stock-data"></a>

```python
import asyncio
from webull_sdk import AsyncWebullSDK

async def main():
    webull = AsyncWebullSDK()
    webull_stock_data = await webull.get_webull_stock_data("AAPL")
    print(webull_stock_data)

asyncio.run(main())
```

## Get Webull Vol Analysis Data <a name="get-webull-vol-analysis-data"></a>

```python
import asyncio
from webull_sdk import AsyncWebullSDK

async def main():
    webull = AsyncWebullSDK()
    webull_vol_analysis_data = await webull.get_webull_vol_analysis_data("AAPL")
    print(webull_vol_analysis_data)

asyncio.run(main())
```


