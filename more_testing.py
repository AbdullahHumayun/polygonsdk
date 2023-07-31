from discord_webhook import DiscordWebhook, DiscordEmbed
from api_master.sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from api_master.sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from api_master.sdks.polygon_sdk.masterSDK import MasterSDK
from api_master.cfg import YOUR_API_KEY, today_str
import matplotlib.pyplot as plt
from io import BytesIO
polygon = AsyncPolygonSDK(YOUR_API_KEY)
opts = PolygonOptionsSDK(YOUR_API_KEY)
master = MasterSDK()
import pandas as pd
import matplotlib.dates as mdates
# Finding the peak and trough for the "Close" price
import pandas as pd
import matplotlib.pyplot as plt
from discord_webhook import DiscordWebhook, DiscordEmbed
import numpy as np

async def main():
    ticker = "AMC"

    data2 = await polygon.get_all_rsi(ticker, timespan="hour", timestamp_greater_than="2023-07-01", timestamp_less_than=today_str)
    aggs = await polygon.get_all_aggregates(ticker, 1, timespan="hour", from_date="2023-07-01", to_date=today_str)

    # Create DataFrames for aggregates
    df_aggs = pd.DataFrame({
        'Close': aggs.close,
        'High': aggs.high,
        'Open': aggs.open,
        'Low': aggs.low,
        'Volume': aggs.volume,
        'Timestamp': aggs.timestamp
    })
    df_rsi = pd.DataFrame({'RSI': data2.rsi_value}, index=data2.timestamp)

    # Merge the DataFrames on the timestamp
    merged_df = pd.merge(df_aggs, df_rsi, left_index=True, right_index=True, how='outer')
    merged_df['Timestamp'] = pd.to_datetime(merged_df['Timestamp'], unit='s')
    # Handle NaN if needed
    merged_df.fillna(method='ffill', inplace=True)
    merged_df.to_csv(f'merged_df_{ticker}.csv')
    print(merged_df)

    peak = merged_df['Close'].max()
    trough = merged_df['Close'].min()
    fibonacci_levels = [0, 0.236, 0.382, 0.5, 0.618, 1]

    plt.style.use('dark_background')
    plt.figure(figsize=(20, 10))  # Increase figure size
    plt.plot(merged_df['Timestamp'], merged_df['Close'], label='Close Price', color='lightblue', linewidth=2)
    plt.title(f'Fibonacci Retracement Levels for {ticker}', fontsize=16)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Price', fontsize=14)

    for level in fibonacci_levels:
        price_level = trough + (peak - trough) * level
        color = 'gold' if level == 0.618 else 'grey'
        linestyle = '-' if level == 0.618 else '--'
        plt.axhline(price_level, color=color, linestyle=linestyle, alpha=0.7)
        plt.text(merged_df['Timestamp'].iloc[-1], price_level, f'{level * 100:.1f}%', fontsize=10, color=color)

    plt.grid(True, color='grey', linestyle='--', alpha=0.5)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.xticks(rotation=45)
    plt.legend(loc='upper left')

    filename = f'chart.png'
    plt.tight_layout()
    plt.savefig(filename)
    print(f"Chart saved as {filename}")

    # URL of your Discord webhook
    webhook_url = 'https://discord.com/api/webhooks/1064077864330338424/ESvYk9hOKpwQrVWeStbCJRQ7HZL-kNCxwmoZ5pt8ASHQbHFYN4xB4zteBNCnKiiPCVFj'

    # Creating a webhook instance
    webhook = DiscordWebhook(url=webhook_url)

    # Creating an embed with a title
    embed = DiscordEmbed(title="Chart")
    embed.set_image(url="attachment://CHART_GOES_HERE.png")

    # Reading the file and adding it as an attachment
    with open(filename, 'rb') as file:
        webhook.add_file(file=file.read(), filename="CHART_GOES_HERE.png")

    # Adding the embed to the webhook
    webhook.add_embed(embed)

    # Executing the webhook to send the message
    webhook.execute()
async def send_to_discord():
    
    filename = 'chart_AMC.png'

    # URL of your Discord webhook
    webhook_url = 'https://discord.com/api/webhooks/1064077864330338424/ESvYk9hOKpwQrVWeStbCJRQ7HZL-kNCxwmoZ5pt8ASHQbHFYN4xB4zteBNCnKiiPCVFj'

    # Creating a webhook instance
    webhook = DiscordWebhook(url=webhook_url)

    # Creating an embed with a title
    embed = DiscordEmbed(title="Chart")
    embed.set_image(url="attachment://CHART_GOES_HERE.png")

    # Reading the file and adding it as an attachment
    with open(filename, 'rb') as file:
        webhook.add_file(file=file.read(), filename="CHART_GOES_HERE.png")

    # Adding the embed to the webhook
    webhook.add_embed(embed)

    # Executing the webhook to send the message
    webhook.execute()
    print("Chart sent to Discord")


import asyncio


asyncio.run(send_to_discord())