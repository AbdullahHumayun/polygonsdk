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
YOUR_RAPIDAPI_KEY = os.environ.get('YOUR_RAPIDAPI_KEY')

# Access the Discord headers
discord_headers = {
    'Authorization': os.getenv('DISCORD_AUTHORIZATION'),
    'User-Agent': os.getenv('DISCORD_USER_AGENT'),
    'Accept': os.getenv('DISCORD_ACCEPT'),
    'Content-Type': os.getenv('DISCORD_CONTENT_TYPE')
}


# Date and Time - import these to easily create date parameters for different functions such as option aggregates, stock aggregates.
today = datetime.today().date()  # Current date
now = datetime.now()  # Current date and time
today_str = datetime.now().strftime('%Y-%m-%d')
five_days_ago_str = (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d')
two_days_from_now_str = (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
five_days_from_now_str = (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d')
thirty_days_ago_str = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
thirty_days_str = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')
seven_days_from_now_str = (datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
fifteen_days_from_now_str = (datetime.now() + timedelta(days=15)).strftime('%Y-%m-%d')
two_years_ago_str = (datetime.now() - timedelta(days=730)).strftime('%Y-%m-%d')
two_years_from_now_str = (datetime.now() + timedelta(days=730)).strftime('%Y-%m-%d')
thirty_days_from_now_str = (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')
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
