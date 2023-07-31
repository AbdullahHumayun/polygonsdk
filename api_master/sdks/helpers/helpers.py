import re
import pytz
from typing import List
from sdks.polygon_sdk.list_sets import stock_condition_dict, STOCK_EXCHANGES, stock_condition_desc_dict
from ssl import SSLError
from datetime import datetime, timedelta
import requests
from cfg import hex_colors
from cfg import YOUR_API_KEY, thirty_days_ago_str, today_str, YOUR_WEBULL_HEADERS as webull_headers
import aiohttp
import asyncio
import pandas as pd
from urllib.parse import urlencode
from sdks.datamaster import DataMaster
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from sdks.polygon_sdk.masterSDK import MasterSDK
now = datetime.now()
polygon = AsyncPolygonSDK(YOUR_API_KEY)
webull = AsyncWebullSDK()
master = MasterSDK()
import disnake
from disnake import ui
from discord_webhook import DiscordEmbed, AsyncDiscordWebhook

class Paginator(ui.View):
    def __init__(self, pages):
        super().__init__()
        self.pages = pages
        self.current_page = 0

    async def on_timeout(self) -> None:
        for button in self.children:
            button.disabled = True
        await self.message.edit(view=self)

    @ui.button(style=disnake.ButtonStyle.green, label="Previous", custom_id="on_prev")
    async def on_prev(self, button: ui.Button, interaction: disnake.AppCmdInter):
        if self.current_page == 0:
            return
        self.current_page -= 1
        await interaction.response.edit_message(embed=self.pages[self.current_page], view=self)

    @ui.button(style=disnake.ButtonStyle.green, label="Next",custom_id="on_next")
    async def on_next(self, button: ui.Button, interaction: disnake.AppCmdInter):
        if self.current_page == len(self.pages) - 1:
            return
        self.current_page += 1
        await interaction.response.edit_message(embed=self.pages[self.current_page], view=self)


class HelperResponse:
    def __init__(self, r=None):
        self.r = r

    @staticmethod
    def parse(data):
        if isinstance(data, dict):
            parsed_data = HelperResponse()
            for key, value in data.items():
                setattr(parsed_data, key, HelperResponse.parse(value))
            return parsed_data
        elif isinstance(data, list):
            parsed_data = []
            for item in data:
                parsed_item = HelperResponse.parse(item)
                parsed_data.append(parsed_item)
            return parsed_data
        else:
            return data
            
    def traverse(self, print_fn, depth=0):
        attr_names = [attr for attr in dir(self) if not attr.startswith('__') and not callable(getattr(self, attr)) and attr != 'r']
        for attr in attr_names:
            value = getattr(self, attr)
            if isinstance(value, HelperResponse):
                print_fn(f"{'  '*depth}{attr}:")
                value.traverse(print_fn, depth+1)
            elif isinstance(value, list) and all(isinstance(v, HelperResponse) for v in value):
                print_fn(f"{'  '*depth}{attr} (list):")
                for v in value:
                    v.traverse(print_fn, depth+1)
            else:
                print_fn(f"{'  '*depth}{attr}: {value}")

def chunked(data, size):
    return [data[i:i+size] for i in range(0, len(data), size)]


def parse(api_endpoint):
    """Parse a URL"""
    if not api_endpoint:
        print(f"Please provide a data URL.")
        return

    try:
        response = requests.get(api_endpoint)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
        return
    except requests.exceptions.RequestException as err:
        print(f"Error occurred: {err}")
        return

    try:
        data = response.json()
    except ValueError:
        print("No JSON object could be decoded from the response.")
        return

    response_obj = HelperResponse.parse(data)

    # Create an empty list to store the lines of the response
    response_lines = []
    response_obj.traverse(response_lines.append)

    # Concatenate the lines with newline characters to form a single string
    response_str = '\n'.join(response_lines)

    # Send the response in chunks of 2000 characters to avoid hitting the Discord character limit
    for i in range(0, len(response_str), 2000):
        chunk = response_str[i:i+2000]
        # If the chunk is cut off mid-line, move the last line to the next chunk
        if i + 2000 < len(response_str) and response_str[i+2000] != '\n':
            last_newline = chunk.rfind('\n')
            next_chunk = chunk[last_newline+1:]
            chunk = chunk[:last_newline]
            response_str = response_str[:i+2000] + next_chunk + response_str[i+2000:]
            print(f"```{chunk}```")


def format_timestamp(timestamp: datetime) -> str:
    return timestamp.strftime("%Y/%m/%d")


def human_readable(string):
    try:
        match = re.search(r'(\w{1,5})(\d{2})(\d{2})(\d{2})([CP])(\d+)', string) #looks for the options symbol in O: format
        underlying_symbol, year, month, day, call_put, strike_price = match.groups()
    except TypeError:
        underlying_symbol = f"AMC"
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
    strike_price = '${:.2f}'.format(float(strike_price)/1000)
    return "{} {} {} Expiring {}".format(underlying_symbol, strike_price, call_put, expiry_date)


def get_checkmark(k, v, thresholds):
    if k == 'score':
        if v is not None and v >= thresholds['score']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'current_ratio':
        if v is not None and v >= thresholds['current_ratio']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'quick_ratio':
        if v is not None and v >= thresholds['quick_ratio']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'debt_to_equity_ratio':
        if v is not None and v <= thresholds['debt_to_equity_ratio']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'return_on_assets':
        if v is not None and v >= thresholds['return_on_assets']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'return_on_equity':
        if v is not None and v >= thresholds['return_on_equity']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'gross_profit_margin':
        if v is not None and v >= thresholds['gross_profit_margin']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'operating_margin':
        if v is not None and v >= thresholds['operating_margin']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'net_profit_margin':
        if v is not None and v >= thresholds['net_profit_margin']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'dividend_payout_ratio':
        if v is not None and v >= thresholds['dividend_payout_ratio'][0] and v <= thresholds['dividend_payout_ratio'][1]:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'revenue_growth':
        if v is not None and v >= thresholds['revenue_growth']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'total_asset_turnover':
        if v is not None and v >= thresholds['total_asset_turnover']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'inventory_turnover':
        if v is not None and v >= thresholds['inventory_turnover']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'days_sales_outstanding':
        if v is not None and v <= thresholds['days_sales_outstanding']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'debt_ratio':
        if v is not None and v <= thresholds['debt_ratio']:
            return ":white_check_mark:"
        else:
            return ":x:"
    elif k == 'interest_coverage':
        if v is not None and v >= thresholds['interest_coverage']:
            return ":white_check_mark:"
        else:
            return ":x:"
    else:
        return ":x:"


def validate_date_format(date_string):
    date_pattern = re.compile(r"\d{4}-\d{2}-\d{2}")
    return bool(date_pattern.fullmatch(date_string))


def convert_to_date(num_days: int):
    """Outputs a date string in the format:
    >>> YYYY-MM-DD e.g. 2023-04-21

    Args:
    
    >>> num days: integer - the numbers of days 
    forward or backwards

    """
    
    time = now + timedelta(days=num_days)
    date_string = time.strftime("%Y-%m-%d")
    return date_string

def format_date(input_str):
    # Parse the input string as a datetime object
    input_datetime = datetime.fromisoformat(input_str.replace("Z", "+00:00"))

    # Convert the datetime object to Eastern Time
    utc_timezone = pytz.timezone("UTC")
    eastern_timezone = pytz.timezone("US/Eastern")
    input_datetime = input_datetime.astimezone(utc_timezone)
    eastern_datetime = input_datetime.astimezone(eastern_timezone)

    # Format the output string
    output_str = eastern_datetime.strftime("%Y-%m-%d at %I:%M%p %Z")
    return output_str



def get_date_string(days):
    date = datetime.now() + timedelta(days=days)
    return date.strftime('%Y-%m-%d')


async def extract_underlying_symbol(symb):



    try:
        match = re.search(r'O:(\w{1,5})(\d{2})(\d{2})(\d{2})([CP])(\d+)', symb)
        underlying_symbol, year, month, day, call_put, strike_price = match.groups() 

    except AttributeError:
        return "M/A"
    
    return underlying_symbol


async def fetch_url(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            data = await response.json()
            return data
        else:
            print(f"Error: {response.status}")
            return None

# Fetch all URLs
async def paginate():
    all_results = []
    next_urls = [f"https://api.polygon.io/v3/snapshot?type=options&order=asc&ticker.lt=SPY&ticker.gt=I:SPX&limit=250&apiKey={YOUR_API_KEY}"]
    async with aiohttp.ClientSession() as session:
        while next_urls:
            tasks = [fetch_url(session, url) for url in next_urls]
            responses = await asyncio.gather(*tasks, return_exceptions=True)

            next_urls = []
            for response in responses:
                if isinstance(response, Exception):
                    print(f"Error: {response}")
                else:
                    if "results" in response:
                        print(response['results'][0]['ticker'])
                        all_results.extend(response["results"])
                        next_url = response.get("next_url")
                        if next_url:
                            next_url += f'&{urlencode({"apiKey": YOUR_API_KEY})}'
                            next_urls.append(next_url)
    df = pd.DataFrame(all_results)
    df.to_csv('testing_it.csv')
    return all_results





from sdks.polygon_sdk.list_sets import etfs_list



# import aiohttp
# async def main():
#     ticker_symbols = ['AAPL', 'GOOGL', 'MSFT']  # Assuming you have a list of ticker symbols

#     async with aiohttp.ClientSession() as session:
#         price_tasks = [poly.get_stock_price(ticker) for ticker in tickers]
#         prices = await asyncio.gather(*price_tasks)
#         ticker_prices = dict(zip(tickers, prices))  # Assuming no None prices

#         # Now get option data concurrently
#         option_data_tasks = [get_option_data(ticker, ticker_prices[ticker], session) for ticker in tickers]
#         results = await asyncio.gather(*option_data_tasks)
#         # Filter out None results and add valid results to data_list
#         data_list = [result for result in results if result is not None]

#         data_list = sorted(data_list, key=lambda x: x[6], reverse=True)
#         print(data_list)

# if __name__ == "__main__":
#     asyncio.run(main())


def chunk_list(input_list, chunk_size):
    """Yield successive n-sized chunks from a list."""
    for i in range(0, len(input_list), chunk_size):
        yield input_list[i:i + chunk_size]

from cfg import konviction

async def stream_embed(symbol, embed: DiscordEmbed, webhook_url):
    webhook = AsyncDiscordWebhook(webhook_url, content=f"<@375862240601047070>")
    data_task = webull.get_webull_stock_data(symbol)
    latest_news_task = webull.get_webull_news(symbol, headers=webull_headers)
    vol_analysis_task = webull.get_webull_vol_analysis_data(symbol)
    short_int_task = webull.get_short_interest(symbol)
    snapshot_task = polygon.get_stock_snapshot(symbol)
    logo_task = polygon.get_polygon_logo(symbol)
    cost_dist_task = webull.cost_distribution(symbol)

    data, latest_news, vol_analysis, short_int, snapshot, logo, cost_dist = await asyncio.gather(
        data_task, latest_news_task, vol_analysis_task, short_int_task, snapshot_task, logo_task, cost_dist_task
    )

    if latest_news is not None and len(latest_news) > 0:
        news_url = latest_news[0].news_url
        news_title = latest_news[0].title
        news_source = latest_news[0].source_name
        embed.add_embed_field(
            name=f"Latest News:",
            value=f"> **{news_title}**\n> **{news_url}**\n> *Source:* **{news_source}**",
            inline=False
        )

    if short_int is None:
        short_int = 0
    if vol_analysis is None:
        return
    buyvol = float(vol_analysis.buyVolume)
    sellvol = float(vol_analysis.sellVolume)
    nvol = float(vol_analysis.nVolume)
    tvol = float(vol_analysis.totalVolume)
    try:
        buyPct = (buyvol / tvol) * 100
        nPct = (nvol / tvol) * 100
        sellPct = (sellvol / tvol) * 100
    except ZeroDivisionError:
        pass

    short_interest = [float(item) for item in short_int.short_int]
    total_shares = float(data.total_shares) if data.total_shares is not None and symbol not in etfs_list else None
    try:
        short_interest = short_interest[0]
    except IndexError:
        short_interest = 0
    if total_shares is not None and symbol not in etfs_list:
        short_percentage_of_float = (short_interest / total_shares) * 100
    else:
        short_percentage_of_float = None
        print("Total shares information is not available.")

    avg10dvol = data.avg_10d_vol
    avg3mvol = data.avg_vol3m
    fifty_high = data.fifty_high
    fifty_low = data.fifty_low
    next_er = data.last_earnings
    out_shares = float(data.outstanding_shares) if data.outstanding_shares is not None else "N/A"
    total_shares = float(data.total_shares) if data.total_shares is not None else "N/A"
    changep = data.web_change_ratio
    close = data.web_stock_close
    name = data.web_name
    high = data.web_stock_high
    open_ = data.web_stock_open
    low = data.web_stock_low
    vol = data.web_stock_vol

    if 'ETF' not in data.web_name:
  
        cost_dist = await webull.cost_distribution(symbol)

        if cost_dist is not None and len(cost_dist) > 0:
            profit_ratio = cost_dist[0].closeProfitRatio
            avg_cost = cost_dist[0].avgCost

            if profit_ratio is not None:
                profit_ratio = round(float(profit_ratio) * 100, 2)
                embed.add_embed_field(
                    name=f"Average Cost:",
                    value=f"> *Across all players - the average cost basis is:*\n> **${avg_cost}**"
                )
                embed.add_embed_field(
                    name=f"% Profiting:",
                    value=f"> **{profit_ratio}%** *of shareholders are currently profiting.*"
                )

    if snapshot and snapshot.prev_day is not None and snapshot.last_trade is not None and snapshot.stock_last_quote is not None and snapshot.today_changep is not None:
        pchange_percent = ((snapshot.prev_day.close - snapshot.prev_day.open) / snapshot.prev_day.open) * 100
    embed.add_embed_field(
        name=f"Day Stats:",
        value=f"> Open: **${open_}**\n> High: **${high}**\n> Last: **${close}**\n> Low: **${low}**\n\n> Change: **{round(float(changep) * 100, 2)}%**"
    )
    if snapshot is not None:
        logo = await polygon.get_polygon_logo(symbol)
        conditions = []
        conds = snapshot.last_trade.conditions
        if conds is not None:
            for condition in conds:
                condition = stock_condition_dict.get(condition)
                conditions.append(condition)

        exchange = STOCK_EXCHANGES.get(snapshot.last_trade.trade_exchange)
        embed.add_embed_field(
            name=f"Previous Day Stats:",
            value=f"> pOpen: **${snapshot.prev_day.open}**\n"
                  f"> pHigh: **${snapshot.prev_day.high}**\n"
                  f"> pLow: **${snapshot.prev_day.low}**\n"
                  f"> pClose: **${snapshot.prev_day.close}**\n"
                  f"> pVol: **{float(snapshot.prev_day.volume):,}**\n"
                  f"> pVWAP: **${snapshot.prev_day.vwap}**"
        )
        embed.add_embed_field(
            name=f"Last Trade:",
            value=f"> Size: **{snapshot.last_trade.trade_size}**\n"
                  f"> Price: **${snapshot.last_trade.trade_price}**\n"
                  f"> Exchange: **{exchange}**\n"
                  f"> Condition(s): **{conditions}**"
        )
        embed.add_embed_field(
            name=f"Last Quote:",
            value=f"> Bidsize: **{float(snapshot.stock_last_quote.bid_size):,}**\n"
                  f"> Asksize: **{float(snapshot.stock_last_quote.ask_size):,}**\n\n"
                  f"> Bid: **${snapshot.stock_last_quote.bid_price}**\n"
                  f"> Ask: **${snapshot.stock_last_quote.ask_price}**"
        )
        if logo and logo is not None:
            embed.set_thumbnail(logo)

    if avg10dvol is not None:
        embed.add_embed_field(
            name=f"Volume:",
            value=f"> Today: **{float(vol):,}**\n"
                  f"> 10d AVG: **{(float(avg10dvol)):,}**\n"
                  f"> 3mo AVG: **{float(avg3mvol):,}**"
        )
    embed.add_embed_field(
        name=f"Vol Analysis:",
        value=f"> 🟢  Buy: **{round(buyPct, 2):,}%**\n"
              f"> ⚪ Neut: **{round(nPct, 2):,}%**\n"
              f"> 🔴 Sell: **{round(sellPct, 2):,}%**",
        inline=True
    )
    embed.add_embed_field(
        name=f"52week Stats:",
        value=f"> High: **{fifty_high}**\n"
              f"> Current: **${close}**\n"
              f"> Low: **{fifty_low}**"
    )

    if short_percentage_of_float is not None:
        embed.add_embed_field(
            name=f"Short Interest:",
            value=f"> **{round(short_percentage_of_float, 2)}%** *of the float is shorted.*"
        )

    embed.set_timestamp()
    webhook.add_embed(embed)

    # Send the webhook
    try:
        await webhook.execute()
    except SSLError:
        pass

async def build_stock_condition_embed(symbol, webhook_url, data):
    webhook = AsyncDiscordWebhook(webhook_url, content=f"<@375862240601047070>",rate_limit_retry=True)
    embed = DiscordEmbed(title=f"Stock Condition - {data['stockConditions']}")
    if data['stockConditions'] is not None:
        embed.description = f"```py\n{symbol} was just traded with the condition of {data['stockConditions']}```"
        embed.color = hex_colors['orange']
        embed.set_thumbnail(await polygon.get_polygon_logo(symbol))
        embed.set_footer(text=f"{symbol} | Data Provided by Polygon.io")
        webhook.add_embed(embed)
        await webhook.execute()




async def build_sector_embed(symbol, webhook_url, embed: DiscordEmbed):
    webhook = AsyncDiscordWebhook(webhook_url, content=f"<@375862240601047070>",rate_limit_retry=True)

    #rsi_snapshot = await polygon.rsi_snapshot(ticker=symbol)


    #print(rsi_snapshot)
    embed.set_thumbnail(await polygon.get_polygon_logo(symbol))
    embed.set_footer(text=f"{symbol} | Data Provided by Polygon.io")
    #embed.add_embed_field(name=f"RSI Snapshot:", value=f"```py\n{rsi_snapshot}```", inline=False)
    embed.set_timestamp()
    webhook.add_embed(embed)
    await webhook.execute()


async def build_exchange_embed(symbol, webhook_url, embed: DiscordEmbed):
    webhook = AsyncDiscordWebhook(webhook_url, content=f"<@375862240601047070>")

   #rsi_snapshot = await polygon.rsi_snapshot(ticker=symbol)
   # print(rsi_snapshot)
    embed.set_thumbnail(await polygon.get_polygon_logo(symbol))
    embed.set_footer(text=f"{symbol} | Data Provided by Polygon.io")
    #embed.add_embed_field(name=f"RSI Snapshot:", value=f"```py\n{rsi_snapshot}```", inline=False)
    embed.set_timestamp()
    webhook.add_embed(embed)
    await webhook.execute()

async def build_embed(symbol, embed: DiscordEmbed, webhook_url):
    webhook = AsyncDiscordWebhook(webhook_url, content=f"<@375862240601047070>",rate_limit_retry=True)
    data_task = webull.get_webull_stock_data(symbol)
    latest_news_task = webull.get_webull_news(symbol, headers=webull_headers)
    vol_analysis_task = webull.get_webull_vol_analysis_data(symbol)
    short_int_task = webull.get_short_interest(symbol)
    snapshot_task = polygon.get_stock_snapshot(symbol)
    logo_task = polygon.get_polygon_logo(symbol)
    cost_dist_task = webull.cost_distribution(symbol)

    data, latest_news, vol_analysis, short_int, snapshot, logo, cost_dist = await asyncio.gather(
        data_task, latest_news_task, vol_analysis_task, short_int_task, snapshot_task, logo_task, cost_dist_task
    )

    if latest_news is not None and len(latest_news) > 0:
        news_url = latest_news[0].news_url
        news_title = latest_news[0].title
        news_source = latest_news[0].source_name
        embed.add_embed_field(
            name=f"Latest News:",
            value=f"> **{news_title}**\n> **{news_url}**\n> *Source:* **{news_source}**",
            inline=False
        )

    if short_int is None:
        short_int = 0
    if vol_analysis is None:
        return
    buyvol = float(vol_analysis.buyVolume)
    sellvol = float(vol_analysis.sellVolume)
    nvol = float(vol_analysis.nVolume)
    tvol = float(vol_analysis.totalVolume)
    try:
        buyPct = (buyvol / tvol) * 100
        nPct = (nvol / tvol) * 100
        sellPct = (sellvol / tvol) * 100
    except ZeroDivisionError:
        pass

    short_interest = [float(item) for item in short_int.short_int]
    total_shares = float(data.total_shares) if data.total_shares is not None and symbol not in etfs_list else None
    try:
        short_interest = short_interest[0]
    except IndexError:
        short_interest = 0
    if total_shares is not None and symbol not in etfs_list:
        short_percentage_of_float = (short_interest / total_shares) * 100
    else:
        short_percentage_of_float = None
        print("Total shares information is not available.")

    avg10dvol = data.avg_10d_vol
    avg3mvol = data.avg_vol3m
    fifty_high = data.fifty_high
    fifty_low = data.fifty_low
    next_er = data.last_earnings
    out_shares = float(data.outstanding_shares) if data.outstanding_shares is not None else "N/A"
    total_shares = float(data.total_shares) if data.total_shares is not None else "N/A"
    changep = data.web_change_ratio
    close = data.web_stock_close
    name = data.web_name
    high = data.web_stock_high
    open_ = data.web_stock_open
    low = data.web_stock_low
    vol = data.web_stock_vol

    if 'ETF' not in data.web_name:
  
        cost_dist = await webull.cost_distribution(symbol)

        if cost_dist is not None and len(cost_dist) > 0:
            profit_ratio = cost_dist[0].closeProfitRatio
            avg_cost = cost_dist[0].avgCost

            if profit_ratio is not None:
                profit_ratio = round(float(profit_ratio) * 100, 2)
                embed.add_embed_field(
                    name=f"Average Cost:",
                    value=f"> *Across all players - the average cost basis is:*\n> **${avg_cost}**"
                )
                embed.add_embed_field(
                    name=f"% Profiting:",
                    value=f"> **{profit_ratio}%** *of shareholders are currently profiting.*"
                )

    if snapshot and snapshot.prev_day is not None and snapshot.last_trade is not None and snapshot.stock_last_quote is not None and snapshot.today_changep is not None:
        pchange_percent = ((snapshot.prev_day.close - snapshot.prev_day.open) / snapshot.prev_day.open) * 100
    embed.add_embed_field(
        name=f"Day Stats:",
        value=f"> Open: **${open_}**\n> High: **${high}**\n> Last: **${close}**\n> Low: **${low}**\n\n> Change: **{round(float(changep) * 100, 2)}%**"
    )
    if snapshot is not None:
        logo = await polygon.get_polygon_logo(symbol)
        conditions = []
        conds = snapshot.last_trade.conditions
        if conds is not None:
            for condition in conds:
                condition = stock_condition_dict.get(condition)
                conditions.append(condition)

        exchange = STOCK_EXCHANGES.get(snapshot.last_trade.trade_exchange)
        embed.add_embed_field(
            name=f"Previous Day Stats:",
            value=f"> pOpen: **${snapshot.prev_day.open}**\n"
                  f"> pHigh: **${snapshot.prev_day.high}**\n"
                  f"> pLow: **${snapshot.prev_day.low}**\n"
                  f"> pClose: **${snapshot.prev_day.close}**\n"
                  f"> pVol: **{float(snapshot.prev_day.volume):,}**\n"
                  f"> pVWAP: **${snapshot.prev_day.vwap}**"
        )
        embed.add_embed_field(
            name=f"Last Trade:",
            value=f"> Size: **{snapshot.last_trade.trade_size}**\n"
                  f"> Price: **${snapshot.last_trade.trade_price}**\n"
                  f"> Exchange: **{exchange}**\n"
                  f"> Condition(s): **{conditions}**"
        )
        embed.add_embed_field(
            name=f"Last Quote:",
            value=f"> Bidsize: **{float(snapshot.stock_last_quote.bid_size):,}**\n"
                  f"> Asksize: **{float(snapshot.stock_last_quote.ask_size):,}**\n\n"
                  f"> Bid: **${snapshot.stock_last_quote.bid_price}**\n"
                  f"> Ask: **${snapshot.stock_last_quote.ask_price}**"
        )
        if logo and logo is not None:
            embed.set_thumbnail(logo)

    if avg10dvol is not None:
        embed.add_embed_field(
            name=f"Volume:",
            value=f"> Today: **{float(vol):,}**\n"
                  f"> 10d AVG: **{(float(avg10dvol)):,}**\n"
                  f"> 3mo AVG: **{float(avg3mvol):,}**"
        )
    embed.add_embed_field(
        name=f"Vol Analysis:",
        value=f"> 🟢  Buy: **{round(buyPct, 2):,}%**\n"
              f"> ⚪ Neut: **{round(nPct, 2):,}%**\n"
              f"> 🔴 Sell: **{round(sellPct, 2):,}%**",
        inline=True
    )
    embed.add_embed_field(
        name=f"52week Stats:",
        value=f"> High: **{fifty_high}**\n"
              f"> Current: **${close}**\n"
              f"> Low: **{fifty_low}**"
    )

    if short_percentage_of_float is not None:
        embed.add_embed_field(
            name=f"Short Interest:",
            value=f"> **{round(short_percentage_of_float, 2)}%** *of the float is shorted.*"
        )

    embed.set_timestamp()
    webhook.add_embed(embed)

    # Send the webhook
    try:
        await webhook.execute()
    except SSLError:
        pass


def create_discord_embed(title, description, color, fields=None):
    embed = DiscordEmbed(title=title, description=description, color=color)
    if fields:
        for field in fields:
            embed.add_embed_field(name=field['name'], value=field['value'])
    return embed


async def build_option_embed(ticker, embed: DiscordEmbed, webhook_url):
    symbol_task = extract_underlying_symbol(ticker)
    option_snap_task = master.get_universal_snapshot(ticker)
    logo_task = polygon.get_polygon_logo(symbol_task)
    profit_task = webull.cost_distribution(symbol_task)
    short_int_task = webull.get_short_interest(symbol_task)
    latest_news_task = webull.get_webull_news(symbol_task, headers=webull_headers)
    vol_analysis_task = webull.get_webull_vol_analysis_data(symbol_task)

    symbol, option_snap, logo, profit, short_int, latest_news, vol_analysis = await asyncio.gather(
        symbol_task, option_snap_task, logo_task, profit_task, short_int_task, latest_news_task, vol_analysis_task
    )

    if latest_news is not None and len(latest_news) > 0:
        news_url = latest_news[0].news_url
        news_title = latest_news[0].title
    else:
        news_url = None
        news_title = None
    if profit is None:
        return

    if short_int is None:
        short_int = 0
    if vol_analysis is None:
        return
    buyvol = float(vol_analysis.buyVolume)
    sellvol = float(vol_analysis.sellVolume)
    nvol = float(vol_analysis.nVolume)
    tvol = float(vol_analysis.totalVolume) if vol_analysis and vol_analysis.totalVolume > 0 else None
    if buyvol is not None and nvol is not None and sellvol is not None and tvol is not None:
        buyPct = (buyvol / tvol) * 100
        nPct = (nvol / tvol) * 100
        sellPct = (sellvol / tvol) * 100
    else:
        buyPct = "--"
        sellPct = "--"
        nPct = "--"
    profit_ratio = [i.closeProfitRatio if i.closeProfitRatio is not None else "N/A" for i in profit]
    avg_cost = [i.avgCost for i in profit]
    short_interest = [float(item) for item in short_int.short_int]

    try:
        short_interest = short_interest[0]
    except IndexError:
        short_interest = 0

    if avg_cost is not None and len(avg_cost) > 0:
        avg_cost = avg_cost[0]
    else:
        avg_cost = None

    if profit_ratio is not None and len(profit_ratio) > 0:
        profit_ratio = round(float(profit_ratio[0]) * 100, 2)
    else:
        profit_ratio = None

    webhook = AsyncDiscordWebhook(webhook_url, content=f"<@375862240601047070>")

    embed.add_embed_field(name=f"{symbol}", value=f"```py\n{symbol}```", inline=False)
    try:
        embed.add_embed_field(
            name=f"Option Stats:",
            value=f"> Open: **${option_snap.open[0]}**\n"
                  f"> High: **${option_snap.high[0]}**\n"
                  f"> Last: **${option_snap.close[0]}**\n"
                  f"> Low: **${option_snap.low[0]}**\n\n"
                  f"> Change: **{round(float(option_snap.change_percent[0]) * 100, 2)}%**"
        )
    except TypeError:
        pass
    if option_snap.delta is not None and option_snap.theta is not None and option_snap.vega is not None and option_snap.gamma is not None:
        # Check if the values are not None before converting to float
        delta_value = round(float(option_snap.delta[0]), 2) if option_snap.delta[0] is not None else None
        gamma_value = round(float(option_snap.gamma[0]), 2) if option_snap.gamma[0] is not None else None
        vega_value = round(float(option_snap.vega[0]), 2) if option_snap.vega[0] is not None else None
        theta_value = round(float(option_snap.theta[0]), 2) if option_snap.theta[0] is not None else None
        iv_value = round(float(option_snap.implied_volatility[0]) * 100, 2) if option_snap.implied_volatility[0] is not None else None
        try:
            # Add the embed field with the updated values
            embed.add_embed_field(
                name="Option Greeks:",
                value=f"> Delta: **{round(float(delta_value),2)}**\n"
                    f"> Gamma: **{round(float(gamma_value),2)}**\n"
                    f"> Vega: **{round(float(vega_value),2)}**\n"
                    f"> Theta: **{round(float(theta_value),2)}**\n"
                    f"> IV: **{round(float(iv_value),2)}**"
            )
        except TypeError:

            embed.add_embed_field(
                name="Option Greeks:",
                value=f"Some greek data not available."
            )
    if option_snap.volume is not None and option_snap.volume[0] is not None and option_snap.open_interest is not None and option_snap.open_interest[0] is not None:
        embed.add_embed_field(
            name=f"OI vs Vol:",
            value=f"> OI: **{float(option_snap.open_interest[0]):,}**\n"
                  f"> VOL: **{float(option_snap.volume[0]):,}**"
        )
    if sellPct is not None and buyPct is not None and tvol is not None:
        embed.add_embed_field(
            name=f"Underlying Volume Analysis:",
            value=f"> 🟩 Buy: **{round(buyPct, 2):,}%**\n"
                  f"> ⬜ Neut: **{round(nPct, 2):,}%**\n"
                  f"> 🟥 Sell: **{round(sellPct, 2):,}%**",
            inline=True
        )
    embed.add_embed_field(
        name=f"Average Cost:",
        value=f"> *Across all players - the average cost basis is:*\n"
              f"> **${avg_cost}**"
    )
    embed.add_embed_field(
        name=f"% Profiting:",
        value=f"> **{profit_ratio}%** *of shareholders are currently profiting.*"
    )

    if latest_news is not None and len(latest_news) > 0:
        embed.add_embed_field(
            name=f"Latest News:",
            value=f"> **{news_title}**\n"
                  f"> **{news_url}**\n"
                  f"> *Source:* **{latest_news[0].source_name}**",
            inline=False
        )
    embed.set_timestamp()

    embed.set_thumbnail(logo)

    webhook.add_embed(embed)

    # Send the webhook
    try:
        await webhook.execute()
    except SSLError:
        pass