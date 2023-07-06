
from typing import List
from api_master.cfg import YOUR_API_KEY

from utilities.webhook_urls import sector_hooks
import asyncio
from collections import defaultdict
from discord_webhook import AsyncDiscordWebhook, DiscordEmbed
from api_master.polygon_enhanced.polygon_enhanced import WebSocketClient
from master import MasterControl
from utilities.list_sets import TAPES, quote_conditions, indicators, subscriptions, market_sectors
from api_master.polygon_enhanced.polygon_enhanced.websocket.models import EquityAgg,EquityTrade,EquityQuote, Market
from datetime import datetime
import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="!", intents=disnake.Intents.all())
subs = ['LVS', 'MOS', 'AMD', 'UPS', 'GDX', 'BMY', 'RTX', 'NFLX', 'WFC', 'AFRM', 'XLF', 'RIG', 'VIX', 'ENPH', 'STNE', 'DNN', 'OSTK', 'XLK', 'SPWR', 'CARR', 'SIRI', 'EWU', 'MU', 'UUP', 'C', 'TNA', 'EWZ', 'MARA', 'SVXY', 'KO', 'UVIX', 'KHC', 'W', 'TLRY', 'PATH', 'SNDL', 'DOCN', 'SE', 'BYND', 'QCOM', 'SVIX', 'ON', 'FSLR', 'BEKE', 'ACB', 'ENVX', 'WMB', 'DIA', 'BTAI', 'UPRO', 'UPST', 'TMF', 'TQQQ', 'XOP', 'TZA', 'DM', 'WMT', 'META', 'ROKU', 'MCD', 'COP', 'ADBE', 'TSLA', 'UCO', 'KGC', 'BCS', 'BITF', 'NNDM', 'MSFT', 'BAC', 'NLY', 'NOK', 'WDC', 'SMH', 'V', 'GE', 'AMGN', 'DNA', 'EWG', 'COF', 'CLF', 'NEM', 'SOXS', 'TECK', 'BBD', 'AZN', 'QS', 'RIVN', 'HYG', 'PYPL', 'CLOV', 'IWM', 'DK', 'HUT', 'APLD', 'SLG', 'MMAT', 'WYNN', 'MELI', 'UVXY', 'SOFI', 'CCL', 'EBAY', 'INTC', 'NIO', 'GS', 'X', 'ETRN', 'PENN', 'XLP', 'MQ', 'AMC', 'M', 'GME', 'XSP', 'NET', 'SPXL', 'MRK', 'LQD', 'SLB', 'BVN', 'RIO', 'SIMO', 'DASH', 'SBSW', 'XPEV', 'ITB', 'JPM', 'EFA', 'PARA', 'USO', 'LI', 'UAL', 'CIM', 'EEM', 'CRWD', 'ONON', 'ETSY', 'PFE', 'PANW', 'HD', 'MVIS', 'ATVI', 'SPXS', 'RBLX', 'ABNB', 'AXP', 'ZIM', 'ORCL', 'RIOT', 'HTZ', 'FCX', 'XP', 'GOLD', 'EBIX', 'ABR', 'CRBU', 'AG', 'APA', 'CVX', 'BILI', 'MA', 'NCLH', 'IQ', 'MLCO', 'KWEB', 'DOW', 'PG', 'OPEN', 'LOW', 'CCJ', 'KOLD', 'PAAS', 'GOOGL', 'FXI', 'KMI', 'AI', 'PSNY', 'LRCX', 'COTY', 'QQQ', 'STLA', 'U', 'FSR', 'XLV', 'SPXU', 'USB', 'TSN', 'NEE', 'IEI', 'XRT', 'RUN', 'AGNC', 'MULN', 'HUM', 'CMCSA', 'EMB', 'CVS', 'PDD', 'BP', 'MO', 'CGC', 'BRK B', 'NU', 'RCL', 'RUT', 'MP', 'OKTA', 'TFC', 'CPNG', 'TMC', 'CROX', 'AAL', 'GNRC', 'TIP', 'DIS', 'MMM', 'MSTR', 'SPY', 'MPW', 'SCHW', 'CHPT', 'BITO', 'WBD', 'BBIO', 'CRM', 'MSOS', 'GSAT', 'TTD', 'MRVL', 'VXX', 'LEVI', 'TRUP', 'AUPH', 'SOXL', 'NKE', 'LLY', 'ZION', 'HOOD', 'AA', 'BABA', 'ALB', 'MRNA', 'UNG', 'CAT', 'HL', 'NVAX', 'MGM', 'BBBYQ', 'PEP', 'UBER', 'PCG', 'SGEN', 'PLUG', 'SU', 'SPLK', 'JWN', 'KR', 'KEY', 'HBI', 'FNGS', 'DAL', 'MDT', 'ARKK', 'LUMN', 'BMBL', 'BTU', 'FFIE', 'PAA', 'LABU', 'IBM', 'ABBV', 'SAVE', 'T', 'GLD', 'CMG', 'TGT', 'XLE', 'JD', 'JBLU', 'XHB', 'XBI', 'DKNG', 'AAP', 'SNOW', 'DB', 'LCID', 'SPX', 'COST', 'ABT', 'BX', 'FUBO', 'MDB', 'AEM', 'CSCO', 'CVNA', 'VFC', 'HAL', 'ASTS', 'NYCB', 'IEP', 'CZR', 'SBUX', 'F', 'JNJ', 'JOBY', 'SWN', 'TWLO', 'KRE', 'GENI', 'VZ', 'TEVA', 'PACW', 'LEN', 'SOUN', 'XOM', 'GOOG', 'TBT', 'PACB', 'DVN', 'BOIL', 'ACRS', 'DDOG', 'PBR', 'NDX', 'VALE', 'TELL', 'TSLL', 'GOEV', 'PLTR', 'MRO', 'TMUS', 'DPST', 'EPD', 'LULU', 'FIS', 'CLSK', 'BTG', 'GT', 'BUD', 'GIS', 'Z', 'BIDU', 'AAPL', 'NKLA', 'UNH', 'DUK', 'IEF', 'SHEL', 'CHWY', 'DD', 'EQT', 'JMIA', 'SPCE', 'WBA', 'UBS', 'EOSE', 'ZS', 'SQQQ', 'TDOC', 'CBL', 'AMAT', 'AMZN', 'HPQ', 'EWJ', 'GILD', 'FDX', 'BB', 'AR', 'LAZR', 'BA', 'ZM', 'FTCH', 'MANU', 'TLT', 'FCEL', 'ET', 'ALLY', 'IONQ', 'VBIV', 'LUV', 'NVDA', 'HZNP', 'SHOP', 'ISEE', 'MTCH', 'SLV', 'LYFT', 'VLO', 'PTON', 'TXN', 'MS', 'VOD', 'SNAP', 'SMCI', 'FUTU', 'OXY', 'JETS', 'DOCU', 'TSM', 'XLI', 'IYR', 'XLU', 'XLY', 'COIN', 'SQ', 'CVE', 'PINS', 'AVGO', 'GM', 'DISH']
import aiohttp
from asyncio import Queue
from pymongo import MongoClient
from api_master.polygon_enhanced.polygon_enhanced.websocket import WebSocketClient, WebSocketMessage
import traceback
client = MongoClient('mongodb://localhost:27017/')
db = client['fudstop']  # Replace with your database name
master = MasterControl()
subs = ','.join(subs)
print(subs)
# Initialize our queue and dictionary outside the function

data_dict = defaultdict(lambda: {"agg": None, "trade": None, "quote": None})
import sqlite3

# Connect to the SQLite database
# If the database does not exist, it will be created
conn = sqlite3.connect('stock_data.db')

cursor = conn.cursor()
c = WebSocketClient(subscriptions=["A.*, T.*"], api_key=YOUR_API_KEY, market=Market.Stocks)
# Create table - EquityTrades
cursor.execute('''
    CREATE TABLE IF NOT EXISTS EquityTrades
    (symbol TEXT, price REAL, size INTEGER, conditions TEXT, exchange TEXT)
''')

# Create table - EquityAggs
cursor.execute('''
    CREATE TABLE IF NOT EXISTS EquityAggs
    (symbol TEXT, official_open REAL, last_price REAL, total_volume INTEGER, volume INTEGER, day_vwap REAL, average_size REAL)
''')

async def handle_msg(msgs: WebSocketMessage, cursor, inter=None):

    for m in msgs:
  
        if m.symbol in subs:
            message_data = {}

            if isinstance(m, EquityTrade):
                message_data['type'] = 'EquityTrade'
                message_data['symbol'] = m.symbol
                message_data['price'] = m.price
                message_data['size'] = m.size
                message_data['conditions'] = m.conditions
                message_data['exchange'] = m.exchange
                conditions_str = ', '.join(m.conditions)
                conn.execute("INSERT INTO EquityTrades VALUES (?, ?, ?, ?, ?)", (m.symbol, m.price, m.size, conditions_str, m.exchange))
                if m.size >= 100:
                    # Determine the sector of the traded ticker
                    sector = None
                    for sector_name, symbols in market_sectors.items():
                        if m.symbol in symbols:
                            sector = sector_name
                            break

                    if sector:
                        # Get the webhook URL for the sector
                        webhook_url = sector_hooks.get(sector)

                        if webhook_url:
                            # Create the webhook object
                            webhook = AsyncDiscordWebhook(webhook_url, content="<@375862240601047070>")

                            # Create the embed message
                            embed = DiscordEmbed(title=f"Last Trade: {m.symbol}",
                                                description=f"> Trade: **{m.size}** shares **${m.price}**\n\n> Conditions: **{m.conditions}**\n\n> Exchange: **{m.exchange}**")
                            webhook.add_embed(embed)

                            # Send the webhook message to the corresponding sector channel
                            await webhook.execute()
                            print(f"EXECUTED WEBHOOK")

                    else:
                        print(f"No sector found for ticker: {m.symbol}")
            elif isinstance(m, EquityAgg):
                message_data['type'] = 'EquityAgg'
                message_data['symbol'] = m.symbol
                message_data['official_open'] = m.official_open_price
                message_data['last_price'] = m.close
                message_data['total_volume'] = m.accumulated_volume
                message_data['volume'] = m.volume
                message_data['day_vwap'] = m.aggregate_vwap
                message_data['average_size'] = m.average_size
                conn.execute("INSERT INTO EquityAggs VALUES (?, ?, ?, ?, ?, ?, ?)", (m.symbol, m.official_open_price, m.close, m.accumulated_volume, m.volume, m.aggregate_vwap, m.average_size))
                conn.commit()



                rsi = await master.fetch_rsi(m.symbol)
                if rsi.value is not None and rsi.value <= 30:
                    color = disnake.Colour.dark_green()
                    embed = disnake.Embed(title=f"Aggregates: {m.symbol}", description=f"> VWAP: **{m.vwap}**\n> Aggregate VWAP: **${m.aggregate_vwap}**\n\n> Total VOL: **{m.accumulated_volume}**\n> Trade Vol: **{m.volume}**\n> RSI: **{round(rsi.value,ndigits=5)}**", color=color)
                    
                    #await inter.edit_original_message(f"{m.symbol} is oversold on the 1min - rsi: {rsi.value}",embed=embed)
   
                    
                elif rsi.value is not None and rsi.value >= 70:
                    color = disnake.Colour.dark_red()
                    embed = disnake.Embed(title=f"Aggregates: {m.symbol}", description=f"> VWAP: **{m.vwap}**\n> Aggregate VWAP: **${m.aggregate_vwap}**\n\n> Total VOL: **{m.accumulated_volume}**\n> Trade Vol: **{m.volume}**\n> RSI: **{round(rsi.value,ndigits=5)}**", color=color)
   
                    #await inter.edit_original_message(f"{m.symbol} is overbought on the 1min - rsi: {rsi.value}",embed=embed)
           
              
            
            return message_data






# @bot.slash_command()
async def main():
    """Start streaming options"""
    await c.connect(lambda msgs: handle_msg(msgs, conn, cursor))

    # Here we move the printing and closing connection part into another function
    async def print_and_close():
        # Query all rows in the EquityTrades table
        cursor.execute("SELECT * FROM EquityTrades")
        equity_trades_rows = cursor.fetchall()

        print('EquityTrades data:')
        for row in equity_trades_rows:
            print(row)

        # Query all rows in the EquityAggs table
        cursor.execute("SELECT * FROM EquityAggs")
        equity_aggs_rows = cursor.fetchall()

        print('EquityAggs data:')
        for row in equity_aggs_rows:
            print(row)

        # Close the cursor and connection
        cursor.close()
        conn.close()

asyncio.run(main())
