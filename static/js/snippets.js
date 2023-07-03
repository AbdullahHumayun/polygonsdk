window.snippets = {

  BotTutorial: { 
    "SCRIPT: Create Project Folders":`

    #Windows - copy/paste this into your CMD \
    #to create the file structure...


    #change "PROJECT_FOLDER" to the name you want


    mkdir PROJECT_FOLDER && type nul > PROJECT_FOLDER\main.py && type nul > PROJECT_FOLDER\config.py && mkdir PROJECT_FOLDER\MYBOT && type nul > PROJECT_FOLDER\MYBOT\bot.py && mkdir PROJECT_FOLDER\COGS && type nul > PROJECT_FOLDER\COGS\general.py && type nul > PROJECT_FOLDER\COGS\gpt4.py && echo Project folder and files created successfully.
    
    `,

    "Lesson 1 - Bot Start-up & Commands":` 

#file: main.py

import disnake #almost identical to discord.py
from disnake.ext import commands

#get token from https://discord.com/developers/applications
from config import token 

intents = disnake.Intents.all()
command_prefix = ">>"



class MyBot(commands.Bot):
    def __init__(self, command_prefix, intents=intents):
        super().__init__(command_prefix, intents=intents)

    async def on_ready(self):
        print(f"Bot is ready! Logged in as {self.user.name}")

    async def on_message(self, message):
        if message.author == self.user:
            return

        await self.process_commands(message)



bot = MyBot(intents=intents, command_prefix=command_prefix)





bot.load_extensions("cogs")
bot.run(token)
    `,
    "Lesson 2 - Command Cogs":`


# file: cogs/general.py

import disnake
from disnake.ext import commands
from disnake import Embed


bot = commands.Bot(command_prefix=">>", intents=disnake.Intents.all())

    
class General(commands.Cog):
def __init__(self, bot):
    self.bot = bot


    @commands.slash_command()
    async def general(self, interaction):
        pass



    @bot.command()
    async def goodbye(ctx: commands.Context):
        
        """Says goodbye in chat."""
        embed = Embed(
            title="Goodbye!",
            description="Farewell! See you next time.",
            color= disnake.Colour.dark_purple(),
            url="https://ww.google.com"
        )

        # Add sequential fields!@
        for i in range(1, 26):
            embed.add_field(name=f"Field Name {i}", value=f"Field Value {i}")

        await ctx.send(embed=embed)

    @general.sub_command()
    async def hello(interaction: disnake.ApplicationCommandInteraction):
        """Says hello in chat."""
        embed = Embed(
            title="Hello!",
            description="Hello! How are you?",
            color= disnake.Colour.dark_teal(),
            url="https://ww.google.com"
        )

        # Add sequential fields
        for i in range(1, 26):
            embed.add_field(name=f"Field Name {i}", value=f"Field Value {i}")

        await interaction.send(embed=embed)  


def setup(bot: commands.Bot):
    bot.add_cog(General(bot))
    print(f"General commands have been loaded!")
    
    `,

  "Bonus Lesson - Add GPT4 To Discord":`

#file: cogs/gpt4.py

from disnake.ext import commands
import disnake
import asyncio
import openai
from config import openaikey

bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all())
openai.api_key = openaikey
class GPT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def gpt4(self, ctx: commands.Context, prompt: str):
        """Talk with CHATGPT. Call the command once and then reply as normal."""
        messages = [
            {"role": "user", "content": f"Use all of the data and come up with a solution. Pay close attention to the option IV versus the current price. You have the nearest option symbols to the money along with all corresponding data to make these determinations."}
        ]
        conversation_history = {}
        conversation_id = str(ctx.author.id)
        prompt = prompt
        # Retrieve the conversation history from the dictionary
        history = conversation_history.get(conversation_id, [])

        while True:
            # Add the new prompt to the conversation history
            history.append({"role": "user", "content": prompt})

            # Create the messages list including system message and conversation history
            messages = [
                {"role": "system", "content": "You will help me save as much time as possible on this project for creating an sdk.'"},
                {"role": "assistant", "content": "Absolutely! Let me know when I can help you save time."},
            ]
            messages.extend(history)

            # Generate a response based on the full conversation history
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            message_content = completion.choices[0].message.content

            # Store the updated conversation history in the dictionary
            conversation_history[conversation_id] = history

            embed = disnake.Embed(title="Chat with GPT4", description=f"> {message_content}")
            embed.add_field(name="YOUR PROMPT:", value=f"You asked: {prompt}")

            # Send the response to the user
            await ctx.send(embed=embed)
            print(message_content)
            # Check if the user wants to stop the conversation
            if prompt.lower() == "stop":
                await ctx.send("Conversation ended.")
                break

            # Wait for the user's next message
            def check(m):
                return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

            try:
                user_message = await self.bot.wait_for("message", check=check, timeout=60)
            except asyncio.TimeoutError:
                await ctx.send("Conversation timed out. Please start a new conversation.")
                break

            prompt = user_message.content


def setup(bot: commands.Bot):
    bot.add_cog(GPT(bot))
    print(f"GPT commands have been loaded!")
  
  `,

  },

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
          ,

        "Generate Option Symbol":`
        
        import asyncio

        from cfg import YOUR_API_KEY
        from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
    
        polyoptions = PolygonOptionsSDK(YOUR_API_KEY)
        
        underlying_symbol = "F"
        expiration_date = "2023-05-19"
        option_type = "C"
        strike_price = 11.5
        
        async def get_option_symbol() -> None:
            """
            Retrieves the option symbol using the Polygon Options SDK.
            """
            option_symbol = await polyoptions.generate_option_symbol(
                underlying_symbol=underlying_symbol,
                expiration_date=expiration_date,
                option_type=option_type,
                strike_price=strike_price
            )
            print(option_symbol)
        
        
        # Run the main function
        asyncio.run(get_option_symbol())
        `,


        "Get Entire Option Chain":`
        import asyncio
        import pandas as pd
        
        from cfg import YOUR_API_KEY
        
        from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
        from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
        from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
        
        
        webull = AsyncWebullSDK()
        poly = AsyncPolygonSDK(YOUR_API_KEY)
        polyoptions = PolygonOptionsSDK(YOUR_API_KEY)
        
        
        ticker = "GME"
        
        
        async def fetch_entire_chain() -> None:
            """
            Fetches the entire option chain for a given ticker and saves it to a CSV file.
            """
            all_options = await polyoptions.get_option_chain_all(ticker)
        
            # Create a DataFrame from the dictionary
            df = pd.DataFrame([option.to_dict() for option in all_options])
        
            # Save the DataFrame to a CSV file
            df.to_csv(f'files/options/ticker_chains/all_{ticker}_chains.csv', index=False)
        
        
        # Run the main function
        asyncio.run(fetch_entire_chain())        
`,
        "Get Option Quote":`
        import asyncio
        from datetime import datetime
        import pandas as pd
        
        from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
        from sdks.helpers.helpers import get_date_string
        
        from cfg import YOUR_API_KEY
        
        now = datetime.now()
        sdk = PolygonOptionsSDK(YOUR_API_KEY)
        
        async def main():
            """
            Main function to retrieve option quotes and save them to a CSV file.
        
            The date range for fetching option quotes can be adjusted by modifying the value of 'num_days_ago'.
            A negative value represents days in the past, and a positive value represents days in the future.
            For example, 'num_days_ago' = -50 will fetch option quotes from 50 days ago until today.
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
        `,

        "Get Option Trades":`
        import asyncio
        import pandas as pd
        
        from cfg import YOUR_API_KEY
        from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
        from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
        
        polyoptions = PolygonOptionsSDK(YOUR_API_KEY)
        poly = AsyncPolygonSDK(YOUR_API_KEY)
        
        async def get_trades():
            """
            Retrieve option trades for a specific option symbol and save them to a CSV file.
        
            This function retrieves option trades using the PolygonOptionsSDK and saves the trades
            to a CSV file for further analysis.
        
            Ensure that you have set the appropriate values for the following variables before running the function:
            - underlying_symbol: The underlying symbol of the option.
            - expiration_date: The expiration date of the option.
            - option_type: The type of the option (C for Call, P for Put).
            - strike_price: The strike price of the option.
            """
        
            underlying_symbol = "F"
            expiration_date = "2023-05-19"
            option_type = "C"
            strike_price = 11.5
        
            # Generate the option symbol
            option_symbol = await polyoptions.generate_option_symbol(underlying_symbol=underlying_symbol,
                                                                     expiration_date=expiration_date,
                                                                     option_type=option_type,
                                                                     strike_price=strike_price)
            print(option_symbol)  # Symbol used for further analysis below
        
            # Retrieve option trades
            opt_trades = await polyoptions.get_option_trades(symbol=option_symbol, limit=100)
        
            # Extract relevant information from option trades
            condition_name = [i.conditions for i in opt_trades]
            price = [i.price for i in opt_trades]
            size = [i.size for i in opt_trades]
            sip_timestamp = [i.sip_timestamp for i in opt_trades]
            exchange = [i.exchange for i in opt_trades]
        
            # Create a DataFrame from the option trades
            df = pd.DataFrame({
                'Condition': condition_name,
                'Price': price,
                'Size': size,
                'Sip Timestamp': sip_timestamp,
                'Exchange': exchange
            })
        
            # Save the DataFrame to a CSV file
            csv_filename = f'files/options/trades/{underlying_symbol}{option_type}{strike_price}_trades.csv'
            df.to_csv(csv_filename)
        
           
        
        asyncio.run(get_trades())        
`,

        "Plot Option Aggregates":`
        
        import asyncio
        import pandas as pd
        import matplotlib.pyplot as plt
        import mplfinance as mpf
        from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
        from cfg import YOUR_API_KEY
        poly = PolygonOptionsSDK(YOUR_API_KEY)
        
        
        underlying_symbol="SPY"
        expiration_date="2023-05-22"
        option_type="C"
        strike_price="400"
        multiplier=1
        timespan="hour"
        from_date="2023-01-01"
        to_date="2023-05-22"
        order="desc"
        limit=100
        
        async def main():
        
            ticker = await poly.generate_option_symbol(underlying_symbol,expiration_date,option_type,strike_price)
            print(ticker)
            aggs = await poly.get_aggregate_bars(ticker, multiplier, timespan, from_date, to_date,adjusted=True, limit=100)
            print(aggs)
            close = [i.close for i in aggs]
            high = [i.close for i in aggs]
            low = [i.close for i in aggs]
            open = [i.close for i in aggs]
            timestamp = [i.close for i in aggs]
            volume = [i.volume for i in aggs]
            vwap = [i.vw for i in aggs]
            num_trades = [i.number_of_trades for i in aggs]
            
            data = {
                'Open': open,
                'High': high,
                'Low': low,
                'Close': close,
                'Time': timestamp,
                'Volume': volume
            }
            print(data)
            df = pd.DataFrame(data)
        
            # Convert timestamp to datetime and set it as index
            df['Time'] = pd.to_datetime(df['Time'], unit='ms')
            df.set_index('Time', inplace=True)
            df.sort_index(inplace=True)
            # Rename columns to match mplfinance requirements
            df.rename(columns={'Open': 'open', 'High': 'high', 'Low': 'low', 'Close': 'close', 'Volume': 'volume'}, inplace=True)
        
            # Plot the candlestick chart using mplfinance
            mpf.plot(df, type='candle', style='mike', title=f'{ticker} - {multiplier} {timespan}', ylabel='Price ($)', volume=True)
        
        asyncio.run(main())
        
        `,
        "Real Time Options Scanner":`
        from typing import List
        from asyncio import Queue
        import random
        import csv
        import asyncio
        import pandas as pd
        from sdks.helpers.helpers import human_readable
        from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
        from sdks.models.test_events import TestOptionsEvent
        
        
        from examples.helpers import write_to_csv
        from cfg import YOUR_API_KEY
        from cachetools import TTLCache
        sdk = PolygonOptionsSDK(YOUR_API_KEY)
        queue = asyncio.Queue()
        
         # generate get this file automatically runnning "get_all_options_data.py"
        df = pd.read_csv('files/options/all_options_data.csv')
        
        
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
                # Select a random row from the DataFrame
                index = random.randint(0, len(df) - 1)
                row = df.iloc[index]
        
                # Create TestOptionsEvent object from row data
                event = TestOptionsEvent.from_row(row)
        
                # Print the created TestOptionsEvent object
        
        
                await handler([event])
        
        
        async def process_snapshot(option_symbol: str, underlying_ticker: str) -> None:
            """
            Process the snapshot data for an option contract and perform analysis.
        
            Args:
                option_symbol: The symbol of the option contract.
                underlying_ticker: The symbol of the underlying asset.
            """
        
            # Acquire the semaphore
            async with semaphore:
        
                snapshot = await sdk.get_option_contract_snapshot(underlying_asset=underlying_ticker, option_contract=option_symbol)
        
                # Retrieve the RSI value from the cache
        
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
        
                # Check if the option meets specific criteria for analysis
                if (implied_volatility is not None
                    and implied_volatility <= 0.53
                    and implied_volatility >= 0.22
                    and underlying_price >= 5
                    and bid >= 0.07
                    and ask <= 2.00
                    and abs(bid - ask) <= 0.03
                    and bid_size is not None
                    and ask_size is not None
                    and bid_size > (ask_size * 10)
                    and day_volume is not None
                    and open_interest is not None
                    and day_volume > (open_interest * 2)):
                    
                    results.append(
                        {
                            "Underlying": underlying_ticker,
                            "Strike Price": strike_price,
                            "Contract Type": contract_type,
                            "Expiration Date": expiration_date,
                            "Day Volume": day_volume,
                            "Day VWAP": day_vwap,
                            "Open Interest": open_interest,
                            "Delta": delta,
                            "Day Change Percent": day_change_percent,
                            "Implied Volatility": implied_volatility,
                            "Underlying Price": underlying_price,
                            "Break Even Price": break_even_price,
                        }
                    )
        
                # Save the results to a CSV file
                for result in results:
                    write_to_csv(result)
        
        
        async def worker(queue: asyncio.Queue) -> None:
            """
            Worker function to process messages from the queue.
        
            Args:
                queue: The asyncio queue containing the option symbols and underlying tickers.
            """
            while True:
                option_symbol, symbol = await queue.get()
                await process_snapshot(option_symbol, symbol)
                queue.task_done()
        
        
        async def main() -> None:
            """
            Main function to coordinate the processing of option snapshots using multiple workers.
            """
            # Create a queue to pass symbols between handle_msg and workers
            queue = asyncio.Queue()
        
            # Create a fixed number of worker tasks
            num_workers = 32
            worker_tasks = [asyncio.create_task(worker(queue)) for _ in range(num_workers)]
        
            await send_messages(lambda msgs: handle_msg(queue, msgs))
        
            # Cancel the worker tasks
            for task in worker_tasks:
                task.cancel()
        
            # Wait for the worker tasks to finish
            await asyncio.gather(*worker_tasks, return_exceptions=True)
        
        
        asyncio.run(main())
        `,
        

        "Latest Ticker News": `
        import asyncio
    
        from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
        from cfg import YOUR_API_KEY
    
        polygonsdk = AsyncPolygonSDK(YOUR_API_KEY)
        ticker = "AAPL"
    
        async def news(ticker):
            """Retrieve the latest news for a specific ticker and print the details."""
    
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
      `,},
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
      return string.replace(" ", "")`,



},
    apiMasterSnippets: { 
    "Webull - Analyst Ratings":` 

    from api_master.examples.webull_analyst_ratings import analyst_ratings

    import asyncio
    
    
    #run one ticker
    ticker="NVDA"
    async def main():
    
        await analyst_ratings(ticker=ticker)
    
    
    
    asyncio.run(main())
    
    
    #run multiple tickers
    tickers = ["NVDA","AMD","GME","AMC","WMT"]
    
    async def multi_main():
    
        for ticker in tickers:
            await analyst_ratings(ticker)
    
    
    asyncio.run(multi_main())
    
    `,

    "Webull - Balance Sheet":`
    from api_master.examples.webull_balance_sheet import balance_sheet

    import asyncio
    
    
    #run one ticker
    ticker="TSLA"
    async def main():
    
        await balance_sheet(ticker=ticker)
    
    
    
    asyncio.run(main())
    
    
    #run multiple tickers
    tickers = ["TSLA","AMD","GME","AMC","WMT"]
    
    async def multi_main():
    
        for ticker in tickers:
            await balance_sheet(ticker)
    
    
    asyncio.run(multi_main())`,

    "Webull - Financial Statement":`
    from api_master.examples.webull_financial_statement import financial_statement

    import asyncio
    
    
    #run one ticker
    ticker="AMZN"
    async def main():
    
        await financial_statement(ticker=ticker)
    
    
    
    asyncio.run(main())
    
    
    #run multiple tickers
    tickers = ["TSLA","AMD","GME","AMC","WMT"]
    
    async def multi_main():
    
        for ticker in tickers:
            await financial_statement(ticker)
    
    
    asyncio.run(multi_main())
    
    `,

    "Webull - Cash Flow":` 
    from api_master.examples.webull_cash_flow import cash_flow

    import asyncio


    #run one ticker
    ticker="AMD"
    async def main():

        await cash_flow(ticker=ticker)



    asyncio.run(main())


    #run multiple tickers
    tickers = ["TSLA","AMD","GME","AMC","WMT"]

    async def multi_main():

        for ticker in tickers:
            await cash_flow(ticker)


    asyncio.run(multi_main())
    
    `,
    "Webull - Short Interest":`
    
    from api_master.examples.webull_short_interest import short_interest

    import asyncio
    
    
    #run one ticker
    ticker="AMD"
    async def main():
    
        await short_interest(ticker=ticker)
    
    
    
    asyncio.run(main())
    
    
    #run multiple tickers
    tickers = ["TSLA","AMD","GME","AMC","WMT"]
    
    async def multi_main():
    
        for ticker in tickers:
            await short_interest(ticker)
    
    
    asyncio.run(multi_main())

    `,

    "Webull - Institutional Ownership": `
    
    from api_master.examples.webull_institutions import institutional_ownership

    import asyncio


    #run one ticker
    ticker="AMD"
    async def main():

        await institutional_ownership(ticker=ticker)



    asyncio.run(main())


    #run multiple tickers
    tickers = ["TSLA","AMD","GME","AMC","WMT"]

    async def multi_main():

        for ticker in tickers:
            await institutional_ownership(ticker)


    asyncio.run(multi_main())
    
    `,

    "Webull - Stock Data": `
    from api_master.examples.webull_stock_data import stock_data

    import asyncio
    
    
    #run one ticker
    ticker="AMD"
    async def main():
    
        await stock_data(ticker=ticker)
    
    
    
    asyncio.run(main())
    
    
    #run multiple tickers
    tickers = ["TSLA","AMD","GME","AMC","WMT"]
    
    async def multi_main():
    
        for ticker in tickers:
            await stock_data(ticker)
    
    
    asyncio.run(multi_main())
    
    `,

    "Webull - Cost Distribution": `
    from api_master.examples.webull_cost_distribution import cost_distribution

    import asyncio
    
    
    #run one ticker
    ticker="AMD"
    async def main():
    
        await cost_distribution(ticker=ticker)
    
    
    
    asyncio.run(main())
    
    
    #run multiple tickers
    tickers = ["TSLA","AMD","GME","AMC","WMT"]
    
    async def multi_main():
    
        for ticker in tickers:
            await cost_distribution(ticker)
    
    
    asyncio.run(multi_main())
    
    `,

    "Webull - Volume Analysis": `
    
    from api_master.examples.webull_volume_analysis import volume_analysis

    import asyncio


    #run one ticker
    ticker="AMD"
    async def main():

        await volume_analysis(ticker=ticker)



    asyncio.run(main())


    #run multiple tickers
    tickers = ["TSLA","AMD","GME","AMC","WMT"]

    async def multi_main():

        for ticker in tickers:
            await volume_analysis(ticker)


    asyncio.run(multi_main())
    
`,
    "Webull - Earnings Calendar": `
    
    from api_master.examples.webull_earnings_calendar import earnings_calendar

    import asyncio
    
    
    #run one ticker
    
    async def main():
    
        await earnings_calendar(date="2023-07-30")
    
    
    
    asyncio.run(main())
    `




}


}

