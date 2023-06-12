window.snippets = {
  restApiSnippets: {
    "Get All Stock Snapshots": `
      import asyncio
      from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
      from cfg import YOUR_API_KEY

      polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)

      filename = "files/stocks/all_snapshots.csv"

      async def get_all_ticker_data():
          \"\"\"Gets all snapshots market-wide and saves to CSV for further analysis / testing purposes.\"\"\"

          await polygonsdk.write_snapshots_to_csv()

          print(f"Data has been successfully saved to files/stocks/all_snapshots.csv.")

      asyncio.run(get_all_ticker_data())
    `,
    "Get All Crypto Snapshots": `
      import asyncio
      import pandas as pd
      from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
      from cfg import YOUR_API_KEY

      polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)

      async def get_all_crypto_data():
          \"\"\"Gets all crypto snapshots and saves to CSV for further analysis / testing purposes.\"\"\"

          crypto_snapshots = await polygonsdk.get_all_crypto_snapshots()
          df = pd.DataFrame(vars(crypto_snapshots))
          df.to_csv('files/crypto/all_crypto_snapshots.csv')

          print(f"Data has been successfully saved to files/crypto/all_crypto_snapshots.csv.")

      asyncio.run(get_all_crypto_data())
    `,
    "Get All Options Snapshots": `
      import asyncio
      from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
      from cfg import YOUR_API_KEY

      polyoptions = PolygonOptionsSDK(YOUR_API_KEY)

      async def get_all_options_data():
          \"\"\"Gets all options snapshots and saves to CSV for further analysis / testing purposes.\"\"\"

          contracts = await polyoptions.fetch_all_option_contracts(
              expiration_date_gte="2023-05-22",  # The expiration will be after today
              expiration_date_lte="2023-07-01",  # Select your desired date range
          )

          await polyoptions.get_snapshots(contracts, 'files/options/all_options_data.csv')

          print(f"Data has been successfully saved to files/options/all_options_data.csv.")

      asyncio.run(get_all_options_data())
    `,
    "Get All Indices Snapshots": `
      import asyncio

      from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
      from cfg import YOUR_API_KEY

      polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)

      async def get_all_indices_data():
          \"\"\"Gets all indices snapshots and saves to CSV for further analysis / testing purposes.\"\"\"

          await polygonsdk.write_indices_to_csv()

          print(f"Data has been successfully saved to files/indices/all_indices_snapshots.csv.")

      asyncio.run(get_all_indices_data())
    `,
    "Get All Forex Snapshots": `
      import asyncio
      import pandas as pd
      from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
      from cfg import YOUR_API_KEY

      polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)

      async def get_forex_data():
          \"\"\"Gets all forex snapshots and saves to CSV for further analysis / testing purposes.\"\"\"

          forex_snapshots = await polygonsdk.get_all_forex_snapshots()
          df = pd.DataFrame(vars(forex_snapshots))
          df.to_csv('files/forex/all_forex_snapshots.csv')

          print(f"Data has been successfully saved to files/forex/all_forex_snapshots.csv.")

      asyncio.run(get_forex_data())
    `
  },
  otherSnippets: {
    "Get All Webull Data": `
      import asyncio
      from examples.webull_data import Webull

      async def process_data():
          webull = Webull()
          await webull.fetch_data('AAPL')

      asyncio.run(process_data())
    `,
    "Run All Webull Functions": `
      from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
      import asyncio
      from cfg import today_str

      sdk = AsyncWebullSDK()

      async def main():
          ticker = "GME"

          capital_flow = await sdk.capital_flow(ticker)
          balance_sheet = await sdk.get_balancesheet(ticker)
          fin_statement = await sdk.get_financial_statement(ticker)
          cash_flow = await sdk.get_cash_flow(ticker)

          market_data = await sdk.get_webull_stock_data(ticker)
          price = market_data.web_stock_close

          financial_ratios = await sdk.calculate_ratios(
              balance_sheet, fin_statement, cash_flow, price
          )

          score = await sdk.calculate_score(
              capital_expenditures=cash_flow[0].capital_expenditures,
              cash_from_financing_activities=cash_flow[0].cash_from_financing_activities,
              cash_from_investing_activities=cash_flow[0].cash_from_investing_activities,
              cash_from_operating_activities=cash_flow[0].cash_from_operating_activities,
              net_change_in_cash=cash_flow[0].net_change_in_cash,
              total_cash_dividends_paid=cash_flow[0].total_cash_dividends_paid,
              net_income=cash_flow[0].net_income,
          )

          calendar = await sdk.get_earnings_calendar(today_str)
          tickers = [i.ticker for i in calendar]

          financial_score = await sdk.financial_score(ticker)

          analysts = await sdk.get_analysis_data(ticker)

          inst = await sdk.get_institutional_holdings(ticker)

          etfs = await sdk.get_etf_categories("commodity")  # Choose between commodity // industry // index // other

          shortint = await sdk.get_short_interest(ticker)

          vol_anal = await sdk.get_webull_vol_analysis_data(ticker)

      asyncio.run(main())
    `,
    "Real Time Discord Integration": `
      import sys
      import os

      sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

      from typing import List
      import random
      import asyncio
      from datetime import datetime
      from sdks.models.test_events import TestStocksEvent
      from sdks.polygon_sdk.mapping_dicts import STOCK_EXCHANGES
      from sdks.polygon_sdk.mapping_dicts import stock_condition_dict, option_condition_dict, OPTIONS_EXCHANGES
      import pandas as pd
      from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
      from cfg import YOUR_API_KEY
      from _discord.hooks.hook_dicts import stock_exchange_hooks
      from discord_webhook import AsyncDiscordWebhook, DiscordEmbed
      from asyncio import Queue
      from _discord.embeddings import Data

      sdk = AsyncPolygonSDK(YOUR_API_KEY)
      df = pd.read_csv('files/stocks/all_snapshots.csv')

      class MockDiscord(Data):
          def __init__(self, symbol=None):
              self.symbol = symbol
              self.last_exchange = None
              self.buyvol = None

          async def consume(self, queue: Queue):
              while True:
                  tasks = []
                  m = await queue.get()
                  self.ask = m.last_quote_ask_price
                  self.bid = m.last_quote_bid_price
                  self.bid_size = m.last_quote_bid_size
                  self.ask_size = m.last_quote_ask_size
                  self.snapshot_close = m.close
                  self.snapshot_low = m.low
                  self.snapshot_open = m.open
                  self.snapshot_high = m.high
                  self.today_change_percent = m.today_change_percent
                  self.today_change = m.today_change
                  self.snapshot_volume = m.volume
                  self.prev_volume = m.prev_volume
                  self.prev_vwap = m.prev_vwap
                  self.snapshot_vwap = m.vwap
                  self.snapshot_exchange = STOCK_EXCHANGES.get(m.last_exchange)
                  self.conditions = [
                      stock_condition_dict.get(condition, 'Unknown')
                      for condition in m.last_trade_conditions
                  ]
                  self.snapshot_size = m.last_size
                  self.snapshot_price = m.last_price
                  self.minute_close = m.min_close
                  self.minute_high = m.min_high
                  self.minute_low = m.min_low
                  self.minute_open = m.min_open
                  self.minute_volume = m.min_volume
                  self.minute_accumulated_volume = m.min_av
                  self.minute_vwap = m.min_vwap
                  self.prev_close = m.prev_close
                  self.prev_high = m.prev_high
                  self.prev_low = m.prev_low
                  self.prev_open = m.prev_open
                  self.prev_volume = m.prev_volume
                  await asyncio.sleep(5)
                  for name, webhook_url in stock_exchange_hooks.items():
                      exchange_hook = AsyncDiscordWebhook(webhook_url, content="<@375862240601047070>")
                      embed = DiscordEmbed(title=f"Exchange Feed - {self.snapshot_exchange}")
                      exchange_hook.add_embed(embed)
                      asyncio.create_task(self.send_webhook(exchange_hook))
                      await asyncio.sleep(2.5)

                  for name, webhook_url in OPTIONS_EXCHANGES.items():
                      exchange_hook = AsyncDiscordWebhook(webhook_url, content="<@375862240601047070>")
                      embed = DiscordEmbed(title=f"Exchange Feed - {self.snapshot_exchange}")
                      exchange_hook.add_embed(embed)
                      asyncio.create_task(self.send_webhook(exchange_hook))
                      await asyncio.sleep(2.5)

                  for name, webhook_url in option_condition_dict.items():
                      exchange_hook = AsyncDiscordWebhook(webhook_url, content="<@375862240601047070>")
                      embed = DiscordEmbed(title=f"Exchange Feed - {self.snapshot_exchange}")
                      exchange_hook.add_embed(embed)
                      asyncio.create_task(self.send_webhook(exchange_hook))
                      await asyncio.sleep(2.5)

          async def send_webhook(self, webhook):
              retries = 0
              while retries < 5:
                  await webhook.execute()
                  break

              retries += 1

      async def handle_msg(msgs: List[TestStocksEvent], queue: Queue):
          for m in msgs:
              await queue.put(m)

      async def send_messages(handler, queue):  # pass queue as an argument
          while True:
              # Select a random row from the DataFrame
              index = random.randint(0, len(df) - 1)
              row = df.iloc[index]

              # Create TestStocksEvent object from row data
              event = TestStocksEvent.from_row(row)

              # Call the handler with the message
              await handler([event], queue)
              await asyncio.sleep(0.01)

      async def main():
          data = MockDiscord()

          data_queue = Queue()

          num_workers = 15  # adjust this value based on your requirements
          sdk_tasks = [
              data.consume(data_queue) for _ in range(num_workers)
          ]

          sdk_tasks.append(asyncio.create_task(send_messages(handle_msg, data_queue)))

          await asyncio.gather(*sdk_tasks)  # include consume_task in gather()

      asyncio.run(main())
    `,
    "Latest Ticker News": `
      import asyncio

      from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
      from cfg import YOUR_API_KEY

      polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)
      ticker = "AAPL"

      async def news(ticker):
          \"\"\"Retrieve the latest news for a specific ticker and print the details.\"\"\"

          news = await polygonsdk.get_ticker_narrative(ticker)
          desc = [i.description for i in news]
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
    `
  }
};