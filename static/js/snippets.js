window.snippets = {
  polygonSnippets: {
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
      `,

      "Polygon Ticker Logo": `
      from urllib.parse import unquote
      from cfg import YOUR_API_KEY
      import aiohttp

      async def get_polygon_logo(symbol):
          url = f'https://api.polygon.io/v3/reference/tickers/{symbol}?apiKey={YOUR_API_KEY}'
          async with aiohttp.ClientSession() as session:
              async with session.get(url) as response:
                  data = await response.json()
                  
                  if 'results' not in data:
                      # No results found
                      return None
                  
                  results = data['results']
                  branding = results.get('branding')

                  if branding and 'icon_url' in branding:
                      encoded_url = branding['icon_url']
                      decoded_url = unquote(encoded_url)
                      url_with_api_key = f"{decoded_url}?apiKey={YOUR_API_KEY}"
                      return url_with_api_key
            
            `
          },

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
      `,
    discordSnippets: {

    

      "Discord Bot - Setup Template": `

      import disnake
      from disnake.ext import commands
      from cfg import token #your bot's token
      # Create a DISNAKE bot instance
      # Set the intents from the developer portal.
      bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all())
      
      # Event: Bot is ready
      @bot.event
      async def on_ready():
          print(f"Bot is ready! Logged in as {bot.user}")
      
      # Command: Ping
      @bot.command()
      async def ping(ctx):
          await ctx.send("Pong!")
      
      # Run the bot
      bot.run(token)`,

      "Make News Embed":`
      from discord_webhook import DiscordEmbed, AsyncDiscordWebhook


      async def make_news_embed(webhook_url, image_url, title, description, name, icon_url, article_url, tickers, home_url, keywords, author):
          webhook = AsyncDiscordWebhook(webhook_url)
          embed = DiscordEmbed(title=title, description=f"{description}", url=article_url)
          embed.add_embed_field(name="Relevant tickers:", value=f"{tickers}", inline=False)
          embed.add_embed_field(name="News Keywords:", value=f"n{keywords}", inline=True)
          embed.add_embed_field(name="Publisher:", value=f"{name}")
          embed.add_embed_field(name=f"Author:", value=f"> **{author}**")
          embed.set_image(image_url)
          embed.set_footer(text="Data provided by Polygon.io", icon_url=icon_url)
          embed.set_author(name=author)
          embed.set_timestamp()
          webhook.add_embed(embed)
          await webhook.execute()
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
    `
    },
  webullSnippets: {
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
    `},

  StockMarketHelperFunctions: {
    "Human Readable Option Symbol": `
    
  import re
  def human_readable(string):
      \\"""Takes an option symbol and converts to a human readable format"""\\
      try:
          match = re.search(r'(\\w{1,5})(\\d{2})(\\d{2})(\\d{2})([CP])(\\d+)', string) #looks for the options symbol in O: format
          underlying_symbol, year, month, day, call_put, strike_price = match.groups()
      except TypeError:
          underlying_symbol = "AMC"
          year = "23"
          month = "02"
          day = "17"
          call_put = "CALL"
          strike_price = "380000"
      
      expiry_date = month + '/' + day + '/' + '20' + year
      if call_put == 'C':
          call_put = 'Call'
      else:
          call_put = 'Put'
      strike_price = "\${{:.2f}}".format(float(strike_price)/1000)
      return "{} {} {} Expiring {}".format(underlying_symbol, strike_price, call_put, expiry_date)
  `,

  "Original Form":` 
  import re
  def original_form(human_readable_list):
      \\"""Takes a human readable option symbol and converts back to original form."""\\
      match = re.search(r'^(\w{1,5}) \$(\d+\.\d{2}) (Call|Put) Expiring (\d{2})/(\d{2})/(\d{4})$', human_readable_list)
      underlying_symbol, strike_price, call_put, month,day,year = match.groups()
      strike_price = str(int(float(strike_price) * 1000)).zfill(8)
      year = year[-2:]
      call_put = 'C' if call_put == 'Call' else 'P'
      expiry_date = year[-2:] + month + day
      options_symbol = f"{underlying_symbol}{expiry_date}{call_put}{strike_price}"
      return options_symbol
  
  `
},
generalHelperFunctions: { 
"Calculate Sum":`
  def calculate_sum(a, b):
      """
      Calculates the sum of two numbers.
  
      Args:
          a (number): The first number.
          b (number): The second number.
  
      Returns:
          number: The sum of the two numbers.
      """
      return a + b`,
  
"Generate Random Number":`
  def generate_random_number(min, max):
      """
      Generates a random number within a given range.
  
      Args:
          min (number): The minimum value of the range.
          max (number): The maximum value of the range.
  
      Returns:
          number: A random number within the specified range.
      """
      import random
      return random.randint(min, max)`,
  "Capitalize String": `
  
  
  def capitalize_string(string):
      """
      Capitalizes the first letter of a string.
  
      Args:
          string (str): The input string.
  
      Returns:
          str: The input string with the first letter capitalized.
      """
      return string.capitalize()`,

  "Reverse String": `
  

  def reverse_string(string):
      """
      Reverses a given string.
  
      Args:
          string (str): The input string.
  
      Returns:
          str: The reversed string.
      """
      return string[::-1]`,

  "Format Date": `
  

  def format_date(date, format="%Y-%m-%d"):
      """
      Formats a date object into a string in the specified format.
  
      Args:
          date (datetime.date): The input date object.
          format (str, optional): The format string. Defaults to "%Y-%m-%d".
  
      Returns:
          str: The formatted date string.
      """
      return date.strftime(format)`,

  "Get File Extension":`

  def get_file_extension(file_name):
      """
      Retrieves the extension of a given file.
  
      Args:
          file_name (str): The name of the file.
  
      Returns:
          str: The file extension.
      """
      import os
      return os.path.splitext(file_name)[1][1:]`,

  "Is Palindrome":`
  
 
  def is_palindrome(string):
      """
      Checks if a given string is a palindrome.
  
      Args:
          string (str): The input string.
  
      Returns:
          bool: True if the string is a palindrome, False otherwise.
      """
      return string == string[::-1]`,

  "Count Vowels":`
  
 
  def count_vowels(string):
      """
      Counts the number of vowels in a given string.
  
      Args:
          string (str): The input string.
  
      Returns:
          int: The number of vowels in the string.
      """
      vowels = "aeiou"
      return sum(1 for char in string.lower() if char in vowels)`,
  "Calculate Factorial":`

  def calculate_factorial(n):
      """
      Calculates the factorial of a given number.
  
      Args:
          n (int): The input number.
  
      Returns:
          int: The factorial of the number.
      """
      if n == 0:
          return 1
      else:
          return n * calculate_factorial(n-1)`,

  "Is Prime Number":`
  

  def is_prime_number(number):
      """
      Checks if a given number is prime.
  
      Args:
          number (int): The input number.
  
      Returns:
          bool: True if the number is prime, False otherwise.
      """
      if number <= 1:
          return False
      for i in range(2, int(number**0.5) + 1):
          if number % i == 0:
              return False
      return True`,


  "Find Least Common Multiple":`
  
  
  def find_lcm(a, b):
      """
      Finds the least common multiple (LCM) of two numbers.
  
      Args:
          a (int): The first number.
          b (int): The second number.
  
      Returns:
          int: The LCM of the two numbers.
      """
      def calculate_gcd(x, y):
          """
          Calculates the greatest common divisor (GCD) of two numbers.
          """
          while y:
              x, y = y, x % y
          return x
  
      return abs(a * b) // calculate_gcd(a, b)`,

  "Calculate Average":`
  

  def calculate_average(numbers):
      """
      Calculates the average of a list of numbers.
  
      Args:
          numbers (list): The list of numbers.
  
      Returns:
          float: The average of the numbers.
      """
      return sum(numbers) / len(numbers)`,

  "Remove Duplicates from List":`
  

  def remove_duplicates(lst):
      """
      Removes duplicate elements from a list while preserving the order.
  
      Args:
          lst (list): The input list.
  
      Returns:
          list: The list with duplicate elements removed.
      """
      seen = set()
      return [x for x in lst if not (x in seen or seen.add(x))]`,

  "Is Anagram":`
  

  def is_anagram(str1, str2):
      """
      Checks if two strings are anagrams of each other.
  
      Args:
          str1 (str): The first string.
          str2 (str): The second string.
  
      Returns:
          bool: True if the strings are anagrams, False otherwise.
      """
      return sorted(str1.lower()) == sorted(str2.lower())`,

  "Find Median Number":`
  

  def find_median(numbers):
      """
      Finds the median of a list of numbers.
  
      Args:
          numbers (list): The list of numbers.
  
      Returns:
          float: The median of the numbers.
      """
      sorted_numbers = sorted(numbers)
      n = len(sorted_numbers)
      if n % 2 == 0:
          return (sorted_numbers[n//2 - 1] + sorted_numbers[n//2]) / 2
      else:
          return sorted_numbers[n//2]`,
  
  "Calculate Power":`
  def calculate_power(base, exponent):
      """
      Calculates the result of raising a base to a specified exponent.
  
      Args:
          base (number): The base number.
          exponent (number): The exponent.
  
      Returns:
          number: The result of the exponentiation.
      """
      return base ** exponent`,

  "Calculate Percentage":`
  

  def calculate_percentage(value, total):
      """
      Calculates the percentage of a value relative to a total.
  
      Args:
          value (number): The value.
          total (number): The total.
  
      Returns:
          float: The percentage.
      """
      return (value / total) * 100`,

  "Find Maximum Value":`
  

  def find_max(numbers):
      """
      Finds the maximum value in a list of numbers.
  
      Args:
          numbers (list): The list of numbers.
  
      Returns:
          number: The maximum value.
      """
      return max(numbers)`,
  
  "Find Minimum Value":`
  def find_min(numbers):
      """
      Finds the minimum value in a list of numbers.
  
      Args:
          numbers (list): The list of numbers.
  
      Returns:
          number: The minimum value.
      """
      return min(numbers)`,

  "Remove Whitespace":`
  def remove_whitespace(string):
      """
      Removes whitespace characters from a string.
  
      Args:
          string (str): The input string.
  
      Returns:
          str: The string without whitespace.
      """
      return string.replace(" ", "")`

}

};

