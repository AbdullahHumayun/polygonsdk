"""
Configuration File
-----------------

This configuration file contains various settings and variables used in the program.

"""
from datetime import datetime, timedelta

# API Keys
YOUR_API_KEY = "YOUR POLYGON API KEY GOES HERE" ##polygon.io APIKEY. If you don't have one - you can sign up here: https://www.polygon.io | Use code FUDSTOP at checkout for an exclusive discount on their real-time APIs.
YOUR_OPENAI_KEY = "" ##openAI key for integrating chatGPT into discord.
YOUR_NASDAQ_KEY = "" ##nasdaq datalink key for using the nasdaq functions (iv_percentile)
YOUR_WEBULL_HEADERS = "" ##headers needed to access the webull functions (news)
YOUR_STOCKSERA_KEY = "YOUR_STOCKSERA_KEY"
discord_headers = {
    'Authorization': f'YOUR DISCORD AUTH TOKEN HERE',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36', #replace with your user-agent if needed
    'Accept': 'application/json',
    'Content-Type': "application/json"
}

# Date and Time - import these to easily create date parameters for different functions such as option aggregates, stock aggregates.
today = datetime.today().date()  # Current date
now = datetime.now()  # Current date and time
today_str = today.strftime('%Y-%m-%d')  # Current date as string
five_days_ago = now - timedelta(days=5)  # Five days ago from current date and time
five_days_ago_str = five_days_ago.strftime('%Y-%m-%d')  # Five days ago as string
two_days_from_now = now + timedelta(days=2)  # Two days from now
two_days_from_now_str = two_days_from_now.strftime('%Y-%m-%d')  # Two days from now as string
five_days_from_now = now + timedelta(days=5)  # Five days from now
five_days_from_now_str = five_days_from_now.strftime('%Y-%m-%d')  # Five days from now as string
thirty_days_ago = now - timedelta(days=30)  # Thirty days ago from current date and time
thirty_days_ago_str = thirty_days_ago.strftime("%Y-%m-%d")  # Thirty days ago as string
thirty_days = now + timedelta(days=30)  # Thirty days ago from current date and time
thirty_days_from_now_str = thirty_days.strftime("%Y-%m-%d")  # Thirty days ago as string

# Hex Colors for discord embeds
hex_colors = {
    'black': '000000',
    'white': 'FFFFFF',
    'red': 'FF0000',
    'green': '00FF00',
    'blue': '0000FF',
    'yellow': 'FFFF00',
    'cyan': '00FFFF',
    'magenta': 'FF00FF',
    'gray': '808080',
    'silver': 'C0C0C0',
    'maroon': '800000',
    'olive': '808000',
    'purple': '800080',
    'teal': '008080',
    'navy': '000080',
    'fuchsia': 'FF0080',
    'lime': '00FF80',
    'aqua': '00FFFF',
    'orange': 'FFA500',
    'pink': 'FFC0CB',
    'lavender': 'E6E6FA',
    'sky blue': '87CEEB',
    'forest green': '228B22',
    'dark slate gray': '2F4F4F',
    'chocolate': 'D2691E',
    'goldenrod': 'DAA520',
    'deep pink': 'FF1493',
    'tomato': 'FF6347',
    'dark orchid': '9932CC',
    'steel blue': '4682B4'
}
