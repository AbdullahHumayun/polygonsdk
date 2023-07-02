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


# Webhook URLs
news_urls = {
    'MarketWatch': os.environ.get('MarketWatch'),
    'SeekingAlpha': os.environ.get('SeekingAlpha'),
    'ZacksInvestmentResearch': os.environ.get('ZacksInvestmentResearch'),
    'Investing.com': os.environ.get('Investing.com'),
    'PennyStock': os.environ.get('PennyStock'),
    'Benzinga': os.environ.get('Benzinga'),
    'GlobeNewswireInc': os.environ.get('GlobeNewswireInc'),
    'TheMotleyFool': os.environ.get('TheMotleyFool'),
}




# STOCK EXCHANGES
exchange_volume = {
    'large_volume': os.environ.get('large_volume'),
    'adf_trf': os.environ.get('adf_trf'),
    'cboe_byx': os.environ.get('cboe_byx'),
    'ltse': os.environ.get('ltse'),
    'cboe_bzx': os.environ.get('cboe_bzx'),
    'nyse': os.environ.get('nyse'),
    'nyse_arca': os.environ.get('nyse_arca'),
    'nasdaq': os.environ.get('nasdaq'),
    'miaxpearl': os.environ.get('miaxpearl'),
    'cta': os.environ.get('cta'),
    'ise': os.environ.get('ise'),
    'iex': os.environ.get('iex'),
    'memx': os.environ.get('memx'),
    'edgx': os.environ.get('edgx'),
    'edga': os.environ.get('edga'),
    'nasdaq_psx': os.environ.get('nasdaq_psx'),
    'nyse_amer': os.environ.get('nyse_amer'),
    'nat': os.environ.get('nat'),
    'utp': os.environ.get('utp'),
    'ssr': os.environ.get('ssr'),
    'icx': os.environ.get('icx'),
    'odd_lot': os.environ.get('odd_lot'),
    'intermarket': os.environ.get('intermarket'),
    'otc': os.environ.get('otc')
}


##CRYPTO##
lrc = os.environ.get('lrc')
ada = os.environ.get('ada')
eth = os.environ.get('eth')
gala = os.environ.get('gala')
ape = os.environ.get('ape')
nct = os.environ.get('nct')
xrp = os.environ.get('xrp')
jasmy = os.environ.get('jasmy')
ctsi = os.environ.get('ctsi')
hbar = os.environ.get('hbar')
hmt = os.environ.get('hmt')
sol = os.environ.get('sol')
usdt = os.environ.get('usdt')
xlm = os.environ.get('xlm')
btc = os.environ.get('btc')
xtz = os.environ.get('xtz')
bch = os.environ.get('bch')
imx = os.environ.get('imx')
doge = os.environ.get('doge')
luna = os.environ.get('luna')
shib = os.environ.get('shib')
fil = os.environ.get('fil')
ach = os.environ.get('ach')
etc = os.environ.get('etc')
xmr = os.environ.get('xmr')
ltc = os.environ.get('ltc')
mkr = os.environ.get('mkr')
algo = os.environ.get('algo')
atom = os.environ.get('atom')
ada2 = os.environ.get('ada2')
jet = os.environ.get('jet')
sand = os.environ.get('sand')
sutu = os.environ.get('sutu')
mana = os.environ.get('mana')
kava = os.environ.get('kava')
matic = os.environ.get('matic')
neo = os.environ.get('neo')
link = os.environ.get('link')
cgld = os.environ.get('cgld')
coti = os.environ.get('coti')
sushi = os.environ.get('sushi')
grt = os.environ.get('grt')
bnb = os.environ.get('bnb')
hnt = os.environ.get('hnt')
dot = os.environ.get('dot')
avax = os.environ.get('avax')
wbtc = os.environ.get('wbtc')
vet = os.environ.get('vet')
dash = os.environ.get('dash')
uni = os.environ.get('uni')
ftt = os.environ.get('ftt')
aave = os.environ.get('aave')
zec = os.environ.get('zec')
rndr = os.environ.get('rndr')
yfi = os.environ.get('yfi')
ren = os.environ.get('ren')
stx = os.environ.get('stx')
rose = os.environ.get('rose')
ogn = os.environ.get('ogn')
ankr = os.environ.get('ankr')
tru = os.environ.get('tru')
uma = os.environ.get('uma')
qnt = os.environ.get('qnt')
iota = os.environ.get('iota')
xyo = os.environ.get('xyo')
zrx = os.environ.get('zrx')
spell = os.environ.get('spell')
boson = os.environ.get('boson')
crv = os.environ.get('crv')
snt = os.environ.get('snt')
flow = os.environ.get('flow')
icp = os.environ.get('icp')
bat = os.environ.get('bat')
nexo = os.environ.get('nexo')
dai = os.environ.get('dai')
swftc = os.environ.get('swftc')
ocean = os.environ.get('ocean')
rari = os.environ.get('rari')
ust = os.environ.get('ust')
inj = os.environ.get('inj')
cro = os.environ.get('cro')
rep = os.environ.get('rep')
gtc = os.environ.get('gtc')
ksm = os.environ.get('ksm')
omg = os.environ.get('omg')


##FOREX##
usdcad = os.environ.get('usdcad')
usdjpy = os.environ.get('usdjpy')
usdhkd = os.environ.get('usdhkd')
usdcny = os.environ.get('usdcny')



##OPTION EXCHANGES##
nyse_amer_options = os.environ.get('nyse_amer_options')
TRADING_IDEAS = os.environ.get('TRADING_IDEAS')










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
