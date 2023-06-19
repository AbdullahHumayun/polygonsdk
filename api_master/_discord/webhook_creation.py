"""AUTOMATICALLY CREATE CHANNELS TO MONITOR
CONDITIONS AND DATA FROM POLYGON.IO
"""


import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))


import requests
from cfg import discord_headers
import requests
from time import sleep
import csv
import requests

from _discord import emojis as e


#EXAMPLE CHANNEL LIST - CREATES CHANNELS FOR YOU TO MONITOR IN REAL TIME

categories = [f"STOCK CONDITIONS",
              f"OPTION CONDITIONS",
              f"OPTION EXCHANGES" 
              f"SSR STOCKS", 
              f"INDICATORS", 
              "STOCK EXCHANGES", 
              f"QUOTE CONDITIONS", 
              "POPULAR TICKERS",
              "TICKER NEWS",
              "TECHNICAL ANALYSIS",
              "STOCK FEEDS",
              "OPTIONS FEEDS"] 
        

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

    "TICKER NEWS": [f"trading{e.world}ideas", f"price{e.world}target", f"large{e.world}cap",
                     f"up{e.world}grades", f"down{e.world}grades", f"analyst{e.world}ratings", 
                     f"small{e.world}cap", f"ipo{e.world}center", f"financing{e.world}agreements",
                     f"conference{e.world}webcast", f"law{e.world}legal", f"company{e.world}announce", f"earnings{e.world}news", f"partnerships{e.world}",
                     f"movers{e.world}", f"crypto{e.world}", f"top{e.world}stories", f"global{e.world}government", f"european{e.world}news",
                     f"etfs{e.world}", f"calendar{e.world}events", f"regulatory{e.world}filings", f"insider{e.world}trades", f"tech{e.world}", f"rumors{e.world}"],

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




def create_channels_and_webhooks(categories, channels_dict, guild_id):
    create_channel_url = f"https://discord.com/api/v9/guilds/{guild_id}/channels"
    headers = discord_headers
    ticker_webhook_dict = {}
    
    for category in categories:
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
            for ticker in channels_dict[category]:
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
