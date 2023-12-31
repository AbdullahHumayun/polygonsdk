"""AUTOMATICALLY CREATE CHANNELS TO MONITOR
CONDITIONS AND DATA FROM POLYGON.IO
"""


import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

import requests

import requests
from time import sleep
import csv
import requests

from _discord import emojis as e


#EXAMPLE CHANNEL LIST - CREATES CHANNELS FOR YOU TO MONITOR IN REAL TIME

categories = [f"NEWS📰WORLD"] 
        
news_dict = { 
"TICKER NEWS": ["stocks📰", "penny📰stocks", "etfs📰", "market📰news", "corp📰news", "investing📰edu", "sector📰stocks", "investor📰rel", "earnings📰dividends", "legal📰info", "market📰regions", "news📰events", "market📰analysis", "crypto📰", "fed📰news", "fin📰services", "industry📰news", "econ📰indicators", "uncon📰invest", "product📰announce", "analyst📰ratings", "offers📰", "forex📰", "market📰sentiments"],
}


channels_dict = {
    'STOCK CONDITIONS': [f"Intermarket{e.broom}Sweep", f"SSR{e.blood}", f"OddLot{e.skull}Trade", f"Closing{e.cross}Prints", f"Derivative{e.building}Priced",
                         f"Opening{e.new}Prints", ""], 

    'STOCK EXCHANGES': [f"Nyse{e.building}Arca", f"Nyse{e.building}Floor", f"FINRA{e.building}ADF", f"Nasdaq{e.building}", 
                        f"Cboe{e.building}edga", f"Cboe{e.building}edgx", f"Cboe{e.building}BZX", f"Nyse{e.building}American",
                        f"Cboe{e.building}BYX", f"Investors{e.building}exchange", f"Members{e.building}Exchange", f"MIAX{e.building}Pearl",
                        f"Nasdaq{e.building}philly", f"Cta{e.building}authority"],

    'OPTION CONDITIONS': [f"Intermarket{e.broom}Sweeps", f"Reopening{e.open}Trade", f"canceled{e.cross}", f"LATE", f"reopening{e.open}Trade", 
                          f"single{e.leg}auction{e.broom}sweep", f"single{e.leg}auction", f"single{e.leg}cross{e.broom}", f"single{e.leg}cross",
                          f"single{e.leg}floor", f"multi{e.two}auto", f"multi{e.two}cross", f"multi{e.two}floor", f"multi{e.vs}single",
                          f"stock{e.chains}auction", f"options{e.cross}cross", f"floor{e.dna}trade", f"auction{e.vs}single", f"floor{e.vs}single",
                          f"multi{e.two}proprietary", f"multilateral{e.windy}compression", f"extended{e.dodo}hours"],

    'OPTION EXCHANGES': [f"NYSE{e.building}Options", f"Boston{e.building}Exchange", f"CBOE{e.building}", f"Nasdaq{e.building}global", 
                         f"ISE{e.building}", f"nasdaq{e.building}mrx", f"MIAX{e.building}",f"NYSE{e.building}arca", f"OPRA{e.building}", 
                         f"MIAX{e.building}PEARL", f"nasdaq{e.building}BX", f"nasdaq{e.building}philly", f"CBOE{e.building}BZX", 
                         f"CBOE{e.building}EDGX"],



    'SSR STOCKS': [f"SSR✅ACTIVATED", f"SSR{e.continued}CONTINUED", f"SSR{e.cross}DEACTIVATED"],

    "INDICATORS": [f"HALT{e.hand}VOLATILITY"],

    "QUOTE CONDITIONS": [f"Order{e.pour}Influx", f"Fast{e.cloud}Trading"],

    "STOCK FEEDS": [f"Large🐳Trades"],

    "OPTIONS FEEDS": [f"Large{e.broom}Sweeps"],

    "TECHNICAL ANALYSIS": [f"Oversold{e.greencircle}day", f"Overbought{e.redcircle}day", f"Oversold{e.greencircle}hour", 
                           f"Overbought{e.redcircle}hour", f"Oversold{e.greencircle}week", f"Overbought{e.redcircle}week"],

    "POPULAR TICKERS": [f"SPY", "META", "MSFT", "AAPL", "NVDA", "TSLA", "AMD", "CSCO", "TSM", "BABA", "SNAP"]}

    




#INSERT YOUR GUILD ID AT THE BOTTOM


""">>> IMPORTANT !

>>> Due to discord rate limiting - to create all of the channels automatically - it takes some time.
    
>>> You can lower the sleep time but you'll risk it skipping over a channel. 
    This script creates all of the ticker channels and webhook URLs you need for your server, and 
    saves them all to a CSV file for later use with the real-time websocket streaming.
"""

YOUR_GUILD_ID = 00000000000


def create_channels_and_webhooks(categories, channels_dict, guild_id):
    create_channel_url = f"https://discord.com/api/v9/guilds/{guild_id}/channels"
    headers = discord_headers
    ticker_webhook_dict = {}
    
    for category in news_dict:
        sleep(10)  # Adjust, but rate limit is very high here

        # Create category
        category_payload = {
            "name": category,
            "type": 4  # 4 is for category
        }
        category_response = requests.post(create_channel_url, json=category_payload, headers=headers)

        if category_response.status_code == 201:
            print(f"Category created: {category}")
            category_id = category_response.json()["id"]
            
            # For each channel under this category
            for ticker in news_dict[category]:
                sleep(10)  # Adjust, but rate limit is very high here

                # Create channel under the category
                channel_payload = {
                    "name": ticker,
                    "type": 0,  # 0 is for text channel, 2 is for voice channel
                    "parent_id": category_id  # Make this channel a child of the category
                }
                response = requests.post(create_channel_url, json=channel_payload, headers=headers)

                if response.status_code == 201:
                    print(f"Channel created for stock ticker: {ticker}")
                    channel_id = response.json()["id"]

                    # Create webhook for the channel
                    create_webhook_url = f"https://discord.com/api/v9/channels/{channel_id}/webhooks"
                    webhook_payload = {
                        "name": f"{ticker} webhook"
                    }

                    webhook_response = requests.post(create_webhook_url, json=webhook_payload, headers=headers)

                    if webhook_response.status_code == 200:
                        print(f"Webhook created for stock ticker: {ticker}")
                        webhook_name = webhook_response.json()["name"]
                        webhook_url = webhook_response.json()["url"]
                        ticker_webhook_dict[ticker] = {"name": webhook_name, "url": webhook_url}
                        print(f"Webhook details: Name - {webhook_name}, URL - {webhook_url}")  # Added for debug


        # Save the ticker_webhook_dict to a CSV file
        with open("files/discord/webhooks/ticker_webhooks.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Webhook Name", "Webhook URL"])
            for ticker, webhook_info in ticker_webhook_dict.items():
                writer.writerow([ticker, webhook_info["url"]])
    
    print("Ticker-webhook information saved to 'ticker_webhooks.csv'.")


create_channels_and_webhooks(categories, channels_dict, YOUR_GUILD_ID)  # Replace with your guild ID 
