"""
Configuration File
-----------------

This configuration file contains various settings and variables used in the program.

"""
from datetime import datetime, timedelta

import os

# API Keys
YOUR_API_KEY = os.environ.get('YOUR_API_KEY') ##polygon.io APIKEY. If you don't have one - you can sign up here:
#                                              https://www.polygon.io | Use code FUDSTOP at checkout for an exclusive discount on their real-time APIs.
YOUR_OPENAI_KEY = os.environ.get('YOUR_OPENAI_KEY') ##openAI key for integrating chatGPT into discord.
YOUR_NASDAQ_KEY = os.environ.get('YOUR_NASDAQ_KEY') ##nasdaq datalink key for using the nasdaq functions (iv_percentile)
YOUR_WEBULL_HEADERS = os.environ.get('YOUR_WEBULL_HEADERS') ##headers needed to access the webull functions (news)
YOUR_IEX_CLOUD_KEY = os.environ.get('YOUR_IEX_CLOUD_KEY')
YOUR_STOCKSERA_KEY = os.environ.get('YOUR_STOCKSERA_KEY') #https://stocksera.pythonanywhere.com/accounts/developers/
YOUR_FINNHUB_KEY = os.environ.get('YOUR_FINNHUB_KEY') #https://finnhub.io/
YOUR_FMP_KEY = os.environ.get('YOUR_FMP_KEY') #https://site.financialmodelingprep.com/developer/docs/
YOUR_FRED_API_KEY = os.environ.get('YOUR_FRED_API_KEY') #https://fred.stlouisfed.org/docs/api/fred/
YOUR_DISCORD_BOT_TOKEN = os.environ.get('YOUR_DISCORD_BOT_TOKEN')#https://discord.com/developers/docs/intro




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
two_years_ago = now - timedelta(days=730)  # Thirty days ago from current date and time
two_years_ago_str = two_years_ago.strftime("%Y-%m-%d")  # Thirty days ago as string
two_years_from_now = now + timedelta(days=730)  # Thirty days ago from current date and time
two_years_from_now_str = two_years_from_now.strftime("%Y-%m-%d")  # Thirty days ago as string

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
