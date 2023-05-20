import requests
from cfg import discord_headers
import requests
from time import sleep
import csv
import requests
#EXAMPLE CHANNEL LIST - CREATES CHANNELS FOR YOU TO MONITOR IN REAL TIME


stock_tickers = ["SPY", "AAPL", "GOOGL", "TSLA", "AMD", "NVDA", "KRE", "NFLX", "AMZN", "PYPL"]  # Example stock tickers - channels / webhooks will be made here

#INSERT YOUR GUILD ID AT THE BOTTOM


""">>> IMPORTANT !

>>> Due to discord rate limiting - to create all of the channels automatically - it takes some time.
    
>>> You can lower the sleep time but you'll risk it skipping over a channel. 
    This script creates all of the ticker channels and webhook URLs you need for your server, and 
    saves them all to a CSV file for later use with the real-time websocket streaming.
"""




def create_channels_and_webhooks(stock_tickers, guild_id):
    create_channel_url = f"https://discord.com/api/v9/guilds/{guild_id}/channels"
    headers = discord_headers
    ticker_webhook_dict = {}
    
    for ticker in stock_tickers:
        sleep(15)  # Adjust, but rate limit is very high here
        # Create channel
        channel_payload = {
            "name": ticker,
            "type": 0  # 0 is for text channel, 2 is for voice channel
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
        with open("files/discord/webhooks/ticker_webhooks.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Webhook Name", "Webhook URL"])
            for ticker, webhook_info in ticker_webhook_dict.items():
                writer.writerow([ticker, webhook_info["url"]])
    
    print("Ticker-webhook information saved to 'ticker_webhooks.csv'.")


create_channels_and_webhooks(stock_tickers, 1108564784326123520)  # Replace with your guild ID