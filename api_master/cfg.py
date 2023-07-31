
from datetime import datetime, timedelta


from dotenv import dotenv_values

config =dotenv_values()


import os

# API Keys
YOUR_API_KEY =""  ##polygon.io APIKEY. If you don't have one - you can sign up here:
#                                              https://www.polygon.io | Use code FUDSTOP at checkout for an exclusive discount on their real-time APIs.
YOUR_OPENAI_KEY =os.environ.get('YOUR_OPENAI_KEY') ##openAI key for integrating chatGPT into discord.
YOUR_NASDAQ_KEY =os.environ.get('YOUR_NASDAQ_KEY') ##nasdaq datalink key for using the nasdaq functions (iv_percentile)
YOUR_WEBULL_HEADERS ={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=""0.5', 'Content-Type': 'application/json', 'platform': 'web', 'hl': 'en', 'os': 'web', 'osv': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0', 'app': 'global', 'appid': 'webull-webapp', 'ver': '3.39.18', 'lzone': 'dc_core_r001', 'ph': 'MacOS Firefox', 'locale': 'eng',
}

YOUR_IEX_CLOUD_KEY =os.environ.get('YOUR_IEX_CLOUD_KEY')
YOUR_STOCKSERA_KEY =os.environ.get('YOUR_STOCKSERA_KEY') #https://stocksera.pythonanywhere.com/accounts/developers/
YOUR_FINNHUB_KEY =os.environ.get('YOUR_FINNHUB_KEY') #https://finnhub.io/
YOUR_FMP_KEY =os.environ.get('YOUR_FMP_KEY') #https://site.financialmodelingprep.com/developer/docs/
YOUR_FRED_API_KEY =os.environ.get('YOUR_FRED_API_KEY') #https://fred.stlouisfed.org/docs/api/fred/
YOUR_DISCORD_BOT_TOKEN =os.environ.get('YOUR_DISCORD_BOT_TOKEN')#https://discord.com/developers/docs/intro
YOUR_RAPIDAPI_KEY =os.environ.get('YOUR_RAPIDAPI_KEY')




# Access the Discord headers
discord_headers ={
    'Authorization': os.getenv('DISCORD_AUTHORIZATION'),
    'User-Agent': os.getenv('DISCORD_USER_AGENT'),
    'Accept': os.getenv('DISCORD_ACCEPT'),
    'Content-Type': os.getenv('DISCORD_CONTENT_TYPE')
}


# Webhook URLs
news_urls ={
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
exchange_volume ={
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
lrc =os.environ.get('lrc')
ada =os.environ.get('ada')
eth ="" 
gala =os.environ.get('gala')
ape =os.environ.get('ape')
nct =os.environ.get('nct')
xrp ="" 
jasmy ="" 
ctsi =os.environ.get('ctsi')
hbar =os.environ.get('hbar')
hmt =os.environ.get('hmt')
sol =os.environ.get('sol')
usdt =os.environ.get('usdt')
xlm =os.environ.get('xlm')
btc ="" 
xtz =os.environ.get('xtz')
bch =os.environ.get('bch')
imx =os.environ.get('imx')
doge =os.environ.get('doge')
luna =os.environ.get('luna')
shib =os.environ.get('shib')
fil =os.environ.get('fil')
ach =os.environ.get('ach')
etc =os.environ.get('etc')
xmr =os.environ.get('xmr')
ltc =os.environ.get('ltc')
mkr =os.environ.get('mkr')
algo =os.environ.get('algo')
atom =os.environ.get('atom')
ada2 =os.environ.get('ada2')
jet =os.environ.get('jet')
sand =os.environ.get('sand')
sutu =os.environ.get('sutu')
mana =os.environ.get('mana')
kava =os.environ.get('kava')
matic =os.environ.get('matic')
neo =os.environ.get('neo')
link =os.environ.get('link')
cgld =os.environ.get('cgld')
coti =os.environ.get('coti')
sushi =os.environ.get('sushi')
grt =os.environ.get('grt')
bnb =os.environ.get('bnb')
hnt =os.environ.get('hnt')
dot =os.environ.get('dot')
avax =os.environ.get('avax')
wbtc =os.environ.get('wbtc')
vet =os.environ.get('vet')
dash =os.environ.get('dash')
uni =os.environ.get('uni')
ftt =os.environ.get('ftt')
aave =os.environ.get('aave')
zec =os.environ.get('zec')
rndr =os.environ.get('rndr')
yfi =os.environ.get('yfi')
ren =os.environ.get('ren')
stx =os.environ.get('stx')
rose =os.environ.get('rose')
ogn =os.environ.get('ogn')
ankr =os.environ.get('ankr')
tru =os.environ.get('tru')
uma =os.environ.get('uma')
qnt =os.environ.get('qnt')
iota =os.environ.get('iota')
xyo =os.environ.get('xyo')
zrx =os.environ.get('zrx')
spell =os.environ.get('spell')
boson =os.environ.get('boson')
crv =os.environ.get('crv')
snt =os.environ.get('snt')
flow =os.environ.get('flow')
icp =os.environ.get('icp')
bat =os.environ.get('bat')
nexo =os.environ.get('nexo')
dai =os.environ.get('dai')
swftc =os.environ.get('swftc')
ocean =os.environ.get('ocean')
rari =os.environ.get('rari')
ust =os.environ.get('ust')
inj =os.environ.get('inj')
cro =os.environ.get('cro')
rep =os.environ.get('rep')
gtc =os.environ.get('gtc')
ksm =os.environ.get('ksm')
omg =os.environ.get('omg')


##FOREX##
usdcad =os.environ.get('usdcad')
usdjpy =os.environ.get('usdjpy')
usdhkd =os.environ.get('usdhkd')
usdcny =os.environ.get('usdcny')



##OPTION EXCHANGES##
nyse_amer_options =os.environ.get('nyse_amer_options')
TRADING_IDEAS =os.environ.get('TRADING_IDEAS')






zero_dte=""



# Date and Time - import these to easily create date parameters for different functions such as option aggregates, stock aggregates.
today =datetime.today().date()  # Current date
now =datetime.now()  # Current date and time
today_str =datetime.now().strftime('%Y-%m-%d')
today_str_yymmdd =datetime.now().strftime('%y%m%d')
five_days_ago_str =datetime.now() - timedelta(days=5).strftime('%Y-%m-%d')
yesterday =datetime.now() - timedelta(days=1).strftime('%Y-%m-%d')
two_days_from_now_str =datetime.now() + timedelta(days=2).strftime('%Y-%m-%d')
five_days_from_now_str =datetime.now() + timedelta(days=5).strftime('%Y-%m-%d')
thirty_days_ago_str =datetime.now() - timedelta(days=30).strftime('%Y-%m-%d')
thirty_days_str =datetime.now() + timedelta(days=30).strftime('%Y-%m-%d')
seven_days_from_now_str =datetime.now() + timedelta(days=7).strftime('%Y-%m-%d')
eight_days_from_now_str =datetime.now() + timedelta(days=8).strftime('%Y-%m-%d')
fifteen_days_from_now_str =datetime.now() + timedelta(days=15).strftime('%Y-%m-%d')
two_years_ago_str =datetime.now() - timedelta(days=730).strftime('%Y-%m-%d')
two_years_from_now_str =datetime.now() + timedelta(days=730).strftime('%Y-%m-%d')
thirty_days_from_now_str =datetime.now() + timedelta(days=30).strftime('%Y-%m-%d')
# Hex Colors for discord embeds
hex_colors ={
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


MARKETWATCH_WEBHOOK =os.environ.get()
SEEKINGALPHA_WEBHOOK =os.environ.get()
ZACKSINVESTMENTRESEARCH_WEBHOOK =os.environ.get()
INVESTINGCOM_WEBHOOK =os.environ.get()
PENNYSTOCK_WEBHOOK =os.environ.get()
BENZINGA_WEBHOOK =os.environ.get()
GLOBENEWSWIREINC_WEBHOOK =os.environ.get()
THEMOTLEYFOOL_WEBHOOK =os.environ.get()
EQUITYMARKETNEWS_WEBHOOK =os.environ.get()
ANALYSISADVICE_WEBHOOK =os.environ.get()
SPECIFICMARKETS_WEBHOOK =os.environ.get()
CORPACTIONGOVERNANCE_WEBHOOK =os.environ.get()
PRODUCTPARTNERSHIPS_WEBHOOK =os.environ.get()
CORPFINANCE_WEBHOOK =os.environ.get()
EVENTS_WEBHOOK =os.environ.get()
REGULATORYLEGAL_WEBHOOK =os.environ.get()
HEALTHCLINICAL_WEBHOOK =os.environ.get()
GENERAL_WEBHOOK =os.environ.get()

#INDICATORS
SHORT_APPENDAGE=""
LONG_APPENDAGE=""

indicatorsDictionary ={

    'NBBO_BB_BO_LONG_APPENDAGE':"",
    'NBBO_BB_BO_SHORT_APPENDAGE':"",
    'NBBO_QUOTE_IS_NBBO':"",
    'RETAIL_INTEREST_ON_BID NYSE Retail interest fact sheet':'https://discord.com/api/webhooks/1130548108590325802/aq_4yRmVvgtM2n34IJrKZOnt1nPOhjaFnp4tgQCzLzlB7vmRl08vOEEX6uyipQsKrbuP',
    'RETAIL_INTEREST_ON_ASK NYSE Retail interest fact sheet': 'https://discord.com/api/webhooks/1130553122868174968/qRG20N3P6CY0VKjTkFWolVC_ngBJOk6d4_x7aTppP9CNXoleadjzKv-CqqUL5W17pDgU',
    'RETAIL_INTEREST_ON_BID_AND_ASK NYSE Retail interest fact sheet':"",
    'Short Sales Restriction in Effect':"",
    'Deficient, Delinquent, and Bankrupt':"",
    'Deficient - Below listing requirements': 'https://discord.com/api/webhooks/1134233736402186260/E89gpF0_5fb-C9nKKpg1FQprxpR8o_xQhjA9x4WIWmUCreEsmEiY8POcIrPlGAl8SM-v',
    'Delinquent - Late filing':"",
}



#STOCK CONDITIONS
CLOSING_PRINTS=""
ODD_LOT=""
SSR=""
INTERMARKET_SWEEPS=""
DERIVATIVELY=""
OPENING_PRINTS=""
NEXT_DAY=""
SLOW_ASK=""
CORRECTED_CLOSE=""
DEFICIENT=""
PRIOR_REFERENCE=""
CROSS_TRADE=""
OPENING_TRADE=""
OFFICIAL_CLOSE=""
RETAIL_INTEREST_BID=""
RETAIL_INTEREST_ASK=""
RETAIL_INTEREST_BID_AND_ASK=""
ORDER_INFLUX=""
REDEMPTION_SUSPENSION=""
SIP_GENERATED_FLAG ="" 
TRADE_THRU_EXEMPT=""
FORM_T=""


stockQuoteIndicatorsDictionary ={
   "":"",
   "":"",
   "":"",
   "":"",
    'Redemptions Suspended': ""
}


stockQuoteConditionsDictionary ={
    'SIP Generated': SIP_GENERATED_FLAG,
    'Slow Ask': SLOW_ASK,
    'Order Influx': ORDER_INFLUX,
    'Intermarket Sweep': 'https://discord.com/api/webhooks/1126246935188226068/iJb0_KQtjfjL0dFk6RfP6zEJS_aPGpJwDKzBR9wBVSxXX_KwGWhJNHxOwTZ6dPn-eS3k',

}

stockConditionsDictionary ={
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
    'Average Price Trade':"",
    'Qualified Contingent Trade':"",
    'Contingent Trade':"",
    'Last and Canceled': 'https://discord.com/api/webhooks/1133441647133339648/724efDyG_n0fkwndtvdTVf2G3s6vtutpAVmwFoPKukC-dNU5ADPfueExfiSO45hsaiX9',
    'Form T': 'https://discord.com/api/webhooks/1130652456162955394/yERSk8ERxiERVGpCOloI_Zwqois4O0zj_MEpayKHm0-TBWf_2JpkxE8j2RJjbcsZzoQM',

}

FINRA_ADF=""
NYSE=""
CBOE_BZX=""
NASDAQ=""
NYSE_AMERICAN=""
NYSE_ARCA=""
OTC=""
IEX=""
MEMX=""
CBOE_EDGX=""
CBOE_EDGA=""
CBOE_BYX=""
MIAX_PEARL=""


stockExchangeDescriptionDictionary ={
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
    'NYSE National, Inc.': 'NYSE National — a fully electronic market that combines the high performance of NYSE Pillar technology with a “taker/maker” fee schedule — aims to deliver greater choice to investors.',
    'Nasdaq Philadelphia Exchange LLC': ""
}

stockExchangeDictionary ={
   "":NYSE_ARCA,
   "":NYSE,
   "":FINRA_ADF,
   "":NASDAQ,
   "":CBOE_EDGA,
   "":CBOE_EDGX,
   "":CBOE_BZX,
   "":NYSE_AMERICAN,
   "":CBOE_BYX,
   "":IEX,
   "":MEMX,
   "":MIAX_PEARL,
}

#STOCK EXCHANGES

FINRA_ADF=""
NYSE=""
CBOE_BZX=""
NASDAQ=""
NYSE_AMERICAN=""
NYSE_ARCA=""
OTC=""
IEX=""
MEMX=""
CBOE_EDGX=""
CBOE_EDGA=""
CBOE_BYX=""
MIAX_PEARL=""


stock_exchange_hooks ={
   "":NYSE_ARCA,
   "":NYSE,
   "":FINRA_ADF,
   "":NASDAQ,
   "":CBOE_EDGA,
   "":CBOE_EDGX,
   "":CBOE_BZX,
   "":NYSE_AMERICAN,
   "":CBOE_BYX,
   "":IEX,
   "":MEMX,
   "":MIAX_PEARL,


}

#OPTIONS EXCHANGES
MIAX=""
ISE=""
CBOE=""
MIAX_EMERALD=""
MIAX_PEARL_OPTIONS=""
NASDAQ_BX=""
NASDAQ_GLOBAL=""
BOSTON_EXCHANGE=""
CBOE_BZX_OPTIONS=""
NASDAQ_MRX=""
ARCA_OPTIONS=""
NYSE_AMERICAN_OPTIONS=""
OPRA=""
NASDAQ_PHILLY_OPTIONS=""
NASDAQ_OPTIONS=""
CBOE_EDGX_OPTIONS=""
CBOE_C2=""


options_exchange_hooks ={
    'NYSE American Options': NYSE_AMERICAN_OPTIONS,
    'Boston Options Exchange': BOSTON_EXCHANGE,
    'Chicago Board Options Exchange': CBOE,
    'MIAX Emerald, LLC': MIAX_EMERALD,
    'Cboe EDGX Options': CBOE_EDGX_OPTIONS,
    'Nasdaq Global Markets Exchange Group': NASDAQ_GLOBAL,
    'International Securities Exchange, LLC': ISE,
    'Nasdaq MRX Options Exchange': NASDAQ_MRX,
    'MIAX International Securities Exchange, LLC': MIAX,
    'NYSE Arca, Inc. - Options': ARCA_OPTIONS,
    'Options Price Reporting Authority': OPRA,
    'MIAX Pearl, LLC - Options': MIAX_PEARL_OPTIONS,
    'Nasdaq BX - Options': NASDAQ_BX,
    'Nasdaq Philadelphia Exchange, LLC - Options': NASDAQ_PHILLY_OPTIONS,
    'Cboe BZX Options Exchange': CBOE_BZX_OPTIONS,
    'MIAX Pearl, LLC': MIAX_PEARL_OPTIONS,
    'Cboe EDGX': CBOE_EDGX_OPTIONS,
    'Cboe C2 Options Exchange': CBOE_C2,
    'Nasdaq Options Market': NASDAQ_OPTIONS,
    
}


optionsExchangeDescriptionDictionary ={
    'NYSE American Options':"",
    'Boston Options Exchange':"",
    'Chicago Board Options Exchange':"",
    'MIAX Emerald, LLC':"",
    'Cboe EDGX Options':"",
    'Nasdaq Global Markets Exchange Group':"",
    'International Securities Exchange, LLC':"",
    'Nasdaq MRX Options Exchange':"",
    'MIAX International Securities Exchange, LLC':"",
    'NYSE Arca, Inc. - Options':"",
    'Options Price Reporting Authority':"",
    'MIAX Pearl, LLC - Options':"",
    'Nasdaq BX - Options':"",
    'Nasdaq Philadelphia Exchange, LLC - Options':"",
    'Cboe BZX Options Exchange':"",
    'MIAX Pearl, LLC':"",
    'Cboe EDGX':"",
    'Cboe C2 Options Exchange':"" 
}



##SECTORS

consumer_cyclical=os.environ.get('consumer_cyclical')
consumer_defensive=os.environ.get('consumer_defensive')
real_estate=os.environ.get('real_estate')
healthcare=os.environ.get('healthcare')
industrials=os.environ.get('industrials')
etfs=os.environ.get('etfs')
basic_materials=os.environ.get('basic_materials')
utilities=os.environ.get('utilities')
energy=os.environ.get('energy')
communication_services=os.environ.get('communication')
financial_services=os.environ.get('financial_services')
technology=os.environ.get('technology')
sectorDescriptions ={
    'consumer_cyclical': "",
    'consumer_defensive': "",
    'real_estate': "",
    'healthcare': "",
    'industrials': "",
    'etfs': "",
    'basic_materials': "",
    'utilities': "",
    'energy': "",
    'communication_services': "",
    'financial_services': "",
    'technology': ""
}

#OPTIONS EXCHANGES
MIAX=os.environ.get('MIAX')
ISE =os.environ.get('ISE')
CBOE =os.environ.get('CBOE')
MIAX_EMERALD =os.environ.get('MIAX_EMERALD')
NASDAQ_BX =os.environ.get('NASDAQ_BX')
NASDAQ_GLOBAL =os.environ.get('NASDAQ_GLOBAL')
MIAX_PEARL_OPTIONS =os.environ.get('MIAX_PEARL_OPTIONS')
BOSTON_EXCHANGE =os.environ.get('BOSTON_EXCHANGE')
CBOE_BZX_OPTIONS =os.environ.get('CBOE_BZX_OPTIONS')
NASDAQ_MRX =os.environ.get('NASDAQ_MRX')
ARCA_OPTIONS =os.environ.get('ARCA_OPTIONS')
NYSE_AMERICAN_OPTIONS=os.environ.get('NYSE_AMERICAN_OPTIONS')
OPRA=os.environ.get('OPRA')
NASDAQ_PHILLY_OPTIONS =os.environ.get('NASDAQ_PHILLY_OPTIONS')
NASDAQ_OPTIONS =os.environ.get('NASDAQ_OPTIONS')
CBOE_EDGX_OPTIONS =os.environ.get('CBOE_EDGX_OPTIONS')
CBOE_C2 =os.environ.get('CBOE_C2')


#trades
vol_10kplus=""
vol5k_to10k=""
vol500_to1k=""
vol1k_to5k=""



#vol_analysis

accumulation=""
fire_sale=""
earnings_today=""



#options conditions
optionConditionsDict ={
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",
   "":"",'Only Trade and Canceled':'https://discord.com/api/webhooks/1133451710782775356/MsZXdqT7SsMzETgg7QBEwLOm9HHLD8VRU26xKeB58NZ0d_r1ULx_0KlHI6RNdLpbiLAg',
    'Canceled': "",
    'Multi Leg Floor Trade of Proprietary Products':"" 
}
#conditionals
near_52_high=""
near_52_low=""
new_52_low=""
new_52_high=""
earnings_week=""
above_avg_volume=""
below_avg_volume=""
squeeze_potential=""


#option volume
optvol_5k10k=""
optvol_100kplus=""
optvol_50to100k=""
optvol_20to50k=""
optvol_10kto20k=""

spx100calls=""
spx100puts=""
spycalls=""
spyputs=""

#skews

skew1=""
skew2=""
skew3=""


#tickers

spx=""
spy=""
coin=""
bidu=""
ual=""
tgt=""

konviction=""
konviction_squeeze=""
discord_headers ={
    'Authorization': 'YOUR TOKEN HERE',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'Accept': 'application/json',
}
sector_hooks ={
   "":consumer_cyclical,
   "":consumer_defensive,
   "":real_estate,
   "":healthcare,
   "":industrials,
   "":etfs,
   "":basic_materials,
   "":utilities,
   "":energy,
   "":communication_services,
   "":financial_services,
   "":technology
}

keyword_webhooks ={
    'https://discord.com/api/webhooks/1130687106902130728/xhW4uJI4lkK867SQA8AmQ2_iC3zQQg5s-BG3GixXhsmUgtviG5nknoLJbU6g8WhiSgXe': ['Broad U.S. Equity ETFs', 'Sector ETFs', 'Large Cap', 'Mid Cap', 'Small Cap', 'Equities', 'Bonds', 'REIT', 'Analyst Recommendations', 'Insider Trades', 'Analyst Color', 'Futures', 'Penny Stocks'],
    'https://discord.com/api/webhooks/1130687152611667998/GVx5K72SWOdXAYI-mxkq76o0VIEKuQEix70otYYLZ1jw_c3YQHE3b4N04EBS8eqd3xC4': ['How to make money with penny stocks', 'Top Penny Stocks 2022', 'Top Penny Stocks 2023', 'Insider trading penny stocks', 'Penny stock news', 'Trading Penny Stocks', 'Penny stocks to buy', 'Penny Stock Basics', 'Penny stocks to watch', 'Penny Stocks', 'Definition of penny stocks', 'What are penny stocks', 'Penny stocks to buy now', 'Best penny stocks to watch', 'Best penny stocks', 'Penny stocks', 'Penny stock', 'Penny Stock News', 'Penny Stocks Robinhood', 'List of penny stocks', 'Penny stocks on robinhood', 'Penny Stocks Watch List', 'Making money with penny stocks', 'Trading penny stocks'],
    'https://discord.com/api/webhooks/1130687198237298739/DrsKnTQUWuwI3-QRlOG0WBvfvf383VaMk8ULgDTg1Z_OHvSHdn2U2YPT_XW0suWVZRJk': ['Emerging Market ETFs', 'Specialty ETFs', 'New ETFs', 'Currency ETFs', 'ETFs'],
    'https://discord.com/api/webhooks/1130687244005543997/I5ZZco2lGISFswliMaOAjQ6zAfsYdF07hlUtE3DhbKIeOBQI0_jivnLXfWqt2TLhERJa': ['Markets', 'Movers', 'Intraday Update', 'Stock Market News'],
    'https://discord.com/api/webhooks/1130687289350160455/mlQNVZNzWBtI05qOkesO-WNyfNCLfEDFvo1GFlSIGaii0EYzvpd98gXzacgKL7V-kVE3': ['Directors and Officers', 'Partnerships', 'Company Announcement', 'Corporate Action', 'M&A', 'Media', 'Mergers and Acquisitions', 'Movers & Shakers', 'Financing Agreements', 'Joint Venture', 'Business Contracts'],
    'https://discord.com/api/webhooks/1130687334472495265/1f-WPhLqes9VYAmZPMceHB7Q4ADBHvfaFTMKZiRtMiKZUzTkr_6zwpp4u6wSuFjCbnV9': ['Education', 'Guidance', 'Advisory', 'Economic Research and Reports', 'Trading Ideas'],
    'https://discord.com/api/webhooks/1130687381201223680/eoORUfGWzQU_fkcr1Nv2FXtZePMq3ZPnxVQpK7DosqEkbN36Q_f97hGo2mGgcZ9JQP-n': ['Cannabis', 'Biotech', 'Biotech penny stocks', 'Gaming', 'Health Care', 'Tech'],
    'https://discord.com/api/webhooks/1130687426399055892/Rs69dW9nX1HHZyFSN727Z0866RSnOMiPiRlqhGiOOKwcjCzew-RlQMc5yyQ-pLvRbM_N': ['Conference Calls/ Webcasts', 'Earningscall-transcripts', 'Annual Meetings & Shareholder Rights'],
    'https://discord.com/api/webhooks/1130687472423145493/XfC8WJIrFAr_sKabGVDBjejf_8mcV0BonycpFgGec22GY8WCoVIWGyeohLUg67s9OjD7': ['Dividends', 'Earnings', 'Dividend Reports and Estimates', 'Earnings Releases and Operating Results'],
    'https://discord.com/api/webhooks/1130687518757634148/m60wEMJmpmDZDQ5q-SQ7Rt5kEgZ3MTdmLFObE8ZNAopDrmv5n3FZh_uy6o28VxLj5sQP': ['Regulatory information', 'Law & Legal Issues', 'Regulations', 'Legal'],
    'https://discord.com/api/webhooks/1130687564345516083/Ic9rEt2EzZFoKKTAqA_sHd0IZb3JKbZq95NF0Kw4AIYbES6qfVY5ZQQ82TvGqyzRIZ2W': ['Asia', 'Eurozone', 'Emerging Markets', 'Global'],
    'https://discord.com/api/webhooks/1130687610084401252/GR5_M17LJqGDSLoPT4geMErppFckQxpQl1rxB_2kfvZoGPh6MY_HyoAt7YGQeh13_QPZ': ['News', 'Events', 'Top Stories', 'Press releases'],
    'https://discord.com/api/webhooks/1130687656053973002/jEF2nmx9ZtrpEeh14hqhMj8SyQxnScVPMIUfUDZi9TvliQyQjH1hC6QXYlKdO6Tc_kP1': ['Short Ideas', 'Options', 'Technical Analysis', 'Long Ideas', 'Technicals'],
    'https://discord.com/api/webhooks/1130687701436346388/J_KJM7FZ4dzqbbHNhWIspjfvQb-eKppj8YVvRlg71YUxgy7wi6nkQWI-TykJEQT7sWzC': ['Cryptocurrency','Forex'],
    'https://discord.com/api/webhooks/1130687746890006598/pp0yjFAOQ7icFj5W7AhQBUL6bL7XTUnCsyoHXbzHaI0w09nMKDzVSmprkWHrm7nZRzEG': ['Federal Reserve', 'Government News', 'Government'],
    'https://discord.com/api/webhooks/1130687792087826462/wspD4U5L-uyQi-94Oap3OxBaskIlrqcvYjOziroM2SGO44UFbUxfJlbbmg61IXf_GL1s': ['Retail Sales', 'Small Business', 'Banking'],
    'https://discord.com/api/webhooks/1130687838233571430/sdPN18uJxlZpfC4FKVf7QTwwwVnU9Paqa9JJ6NjHEkemZyy5f-jFZSTJXUQsRT61koVB': ['Travel', 'Entertainment', 'Health', 'Real Estate'],
    'https://discord.com/api/webhooks/1130687884710658121/2OCHYnw3sybRQVuxbAlOq0InbgKi1olG71imiCCu4hQSStw3lb-ET1kDwPnR8rTXUUjq': ['Econ #s', 'Economics', 'Macro Economic Events'],
    'https://discord.com/api/webhooks/1130687930508255385/KIvWYbLhURnpUwqLM_WENtuymhBPghaQML96F_uGrmlCKyJCLx6J07Uu60ng4Y3Ggl2t': ['Psychedelics', 'Environmental, Social, and Governance Criteria'],
    'https://discord.com/api/webhooks/1130687976905654313/s7LkV0BMQgOjQEf-s9bfY8t0ucdpEfLREPtDT3ajfkTJi6MTCiQEqwdTh6ODpleQRcvA': ['Product / Services Announcement'],
    'https://discord.com/api/webhooks/1130688028566884422/RAGHU_KNc660cV_ZFH5ABVmkJl3AuiXHVf8Lb8IjuxfgPDBqEzDof25Ll8Tac1XqcFrx': ['Initiation', 'Reiteration', 'Upgrades', 'Downgrades', 'Price Target', 'Analyst Ratings'],
    'https://discord.com/api/webhooks/1130688074351910972/1hCMMcPoJ6EU-0BoayPYf0nsfZj9k-hZU6r8e1MKaT-_6DV8lKBFokIJuaP2Z2tieiLe': ['Offerings'],
    'https://discord.com/api/webhooks/1130688171491987566/rVs7hPxYZBKjc34anra6XdSELzIQJO7FPca5yQBEkY0dGGJm6DzxQzkfuFHw5Aer85dl': ['Success Stories', 'Short Sellers', 'Market Activity', 'Unusual options activity', 'Signals']
}



keyword_categories ={
    'stocks': ['Broad U.S. Equity ETFs', 'Sector ETFs', 'Large Cap', 'Mid Cap', 'Small Cap', 'Equities', 'Bonds', 'REIT', 'Analyst Recommendations', 'Insider Trades', 'Analyst Color', 'Futures', 'Penny Stocks'],
    'penny_stocks': ['How to make money with penny stocks', 'Top Penny Stocks 2022', 'Top Penny Stocks 2023', 'Insider trading penny stocks', 'Penny stock news', 'Trading Penny Stocks', 'Penny stocks to buy', 'Penny Stock Basics', 'Penny stocks to watch', 'Penny Stocks', 'Definition of penny stocks', 'What are penny stocks', 'Penny stocks to buy now', 'Best penny stocks to watch', 'Best penny stocks', 'Penny stocks', 'Penny stock', 'Penny Stock News', 'Penny Stocks Robinhood', 'List of penny stocks', 'Penny stocks on robinhood', 'Penny Stocks Watch List', 'Making money with penny stocks', 'Trading penny stocks'],
    'etfs': ['Emerging Market ETFs', 'Specialty ETFs', 'New ETFs', 'Currency ETFs', 'ETFs'],
    'market_news': ['Markets', 'Movers', 'Intraday Update', 'Stock Market News'],
    'corp_news': ['Directors and Officers', 'Partnerships', 'Company Announcement', 'Corporate Action', 'M&A', 'Media', 'Mergers and Acquisitions', 'Movers & Shakers', 'Financing Agreements', 'Joint Venture', 'Business Contracts'],
    'investing_edu': ['Education', 'Guidance', 'Advisory', 'Economic Research and Reports', 'Trading Ideas'],
    'sector_stocks': ['Cannabis', 'Biotech', 'Biotech penny stocks', 'Gaming', 'Health Care', 'Tech'],
    'investor_rel': ['Conference Calls/ Webcasts', 'Earningscall-transcripts', 'Annual Meetings & Shareholder Rights'],
    'earnings_dividends': ['Dividends', 'Earnings', 'Dividend Reports and Estimates', 'Earnings Releases and Operating Results'],
    'legal_info': ['Regulatory information', 'Law & Legal Issues', 'Regulations', 'Legal'],
    'market_regions': ['Asia', 'Eurozone', 'Emerging Markets', 'Global'],
    'news_events': ['News', 'Events', 'Top Stories', 'Press releases'],
    'market_analysis': ['Short Ideas', 'Options', 'Technical Analysis', 'Long Ideas', 'Technicals'],
    'crypto_forex': ['Cryptocurrency','Forex'],
    'fed_news': ['Federal Reserve', 'Government News', 'Government'],
    'fin_services': ['Retail Sales', 'Small Business', 'Banking'],
    'industry_news': ['Travel', 'Entertainment', 'Health', 'Real Estate'],
    'econ_indicators': ['Econ #s', 'Economics', 'Macro Economic Events'],
    'uncon_invest': ['Psychedelics', 'Environmental, Social, and Governance Criteria'],
    'product_announce': ['Product / Services Announcement'],
    'analyst_ratings': ['Initiation', 'Reiteration', 'Upgrades', 'Downgrades', 'Price Target', 'Analyst Ratings'],
    'offers': ['Offerings'],
    'market_sentiments': ['Success Stories', 'Short Sellers', 'Market Activity', 'Unusual options activity', 'Signals'],
}


conditions_to_check =['Odd Lot Trade', 'Form T', 'Intermarket Sweep',  
                                    'Market Center Official Close', 'Corrected Consolidated Close (per listing market)',
                                    'Trade Thru Exempt', 'SSR in Effect'
                                    ]

exchanges_to_check =['NYSE Arca, Inc.', 'NYSE American, LLC', 'New York Stock Exchange', 'Cboe EDGX', 'Nasdaq', 
                      'FINRA Alternative Display Facility', 'Cboe BZX', 'Members Exchange', 'Investors Exchange', 
                      'NYSE American, LLC']




# keywords_to_check =['Broad U.S. Equity ETFs','corp_news', 'Cryptocurrency', 'how to make money with penny stocks', 'Conference Calls/ Webcasts', 'Directors and Officers', 'Analyst Recommendations', 'Top Penny Stocks 2022', 'Markets', 'Sector ETFs', 'Movers', 'Partnerships', 'top penny stocks', 'investing', 'insider trading penny stocks', 'Large Cap', 'Short Ideas', 'penny stock news', 'Emerging Market ETFs', 'Trading Penny Stocks', , 'Tax Issues/Accounting', 'penny stocks to buy', 'Mid Cap', 'Education', 'Penny Stock Basics', 'Dividends', 'Regulatory information', 'Options', 'Company Announcement', 'Cannabis', 'penny stocks to watch', 'Corporate Action', 'Federal Reserve', 'Law & Legal Issues', 'After-Hours Center', 'M&A', 'Media', 'Mergers and Acquisitions', 'Movers & Shakers', 'Bonds', 'Financing Agreements', 'earningscall-transcripts', 'Clinical Study', 'ETFs', 'Treasuries', 'Retail Sales', 'Interview', 'Trading Ideas', 'Penny Stocks', 'definition of penny stocks', 'Calendar of Events', 'Small Cap', 'Econ #s', 'Guidance', 'Small Business', 'Top Penny Stocks 2023', 'what are penny stocks', 'Equities', 'Asia', 'News', 'Events', 'Gaming', 'Technical Analysis', 'biotech penny stocks', 'Eurozone', 'Biotech', 'Pre-Market Outlook', 'Insider Trades', 'Exclusives', 'Travel', 'penny stocks to buy now', 'best penny stocks to watch', 'Psychedelics', 'Earnings', 'Entertainment', 'Top Stories', 'Health Care', 'Economics', 'Health', 'European Regulatory News', 'Forex', 'Success Stories', 'Short Sellers', 'Commodities', 'Government News', 'Initiation', 'Reiteration', 'Politics', 'best penny stocks', 'Press releases', 'Offerings', 'penny stocks', 'Emerging Markets', 'Specialty ETFs', 'Analyst Color', 'Stock Market News', 'Intraday Update', 'REIT', 'Legal', 'Management statements', 'Penny Stocks Robinhood', 'list of penny stocks', 'Joint Venture', 'Dividend Reports and Estimates', 'New ETFs', 'Advisory', 'Economic Research and Reports', 'Global', 'are penny stocks worth it', 'Futures', 'unusual options activity', 'Signals', 'Regulations', 'Real Estate', 'Environmental, Social, and Governance Criteria', 'Tech', 'Featured', 'Business Contracts', 'Other News', 'Upgrades', 'Government', 'Earnings Releases and Operating Results', 'penny stocks on robinhood', 'Analyst Ratings', 'Currency ETFs', 'penny stock', 'Penny Stock News', 'Product / Services Announcement', 'Price Target', 'Downgrades', 'Annual Meetings & Shareholder Rights', 'Penny Stocks Watch List', 'Macro Economic Events', 'making money with penny stocks', 'Long Ideas', 'General', 'trading penny stocks', 'Technicals', 'Previews']

from discord_webhook import AsyncDiscordWebhook
content=""
filecoin_indices_hook=AsyncDiscordWebhook("YOUR_WEBHOOK_URL", content="")
china_indices_hook=AsyncDiscordWebhook("YOUR_WEBHOOK_URL", content="")
volatility_indices_hook=AsyncDiscordWebhook("YOUR_WEBHOOK_URL", content="")
skew_indices_hook=AsyncDiscordWebhook("YOUR_WEBHOOK_URL", content="")
cloud_indices_hook=AsyncDiscordWebhook("YOUR_WEBHOOK_URL", content="")
spx_dispersion_hook=AsyncDiscordWebhook("YOUR_WEBHOOK_URL", content="")
benchmark_indices_hook=AsyncDiscordWebhook("YOUR_WEBHOOK_URL", content="")
futures_indices_hook=AsyncDiscordWebhook("YOUR_WEBHOOK_URL", content="")
short_indices_hook=AsyncDiscordWebhook("YOUR_WEBHOOK_URL", content="")
us_dollar_hook=AsyncDiscordWebhook("YOUR_WEBHOOK_URL", content="")
basic_materials_hook=AsyncDiscordWebhook("YOUR_WEBHOOK_URL", content="")
technology_hook=AsyncDiscordWebhook("YOUR_WEBHOOK_URL", content="")
industrials_hook=AsyncDiscordWebhook("YOUR_WEBHOOK_URL", content="")


##INDICES
china_indices=""['NASDAQ China Utilities TR Index', 'Nasdaq China Consumer Discretionary NTR Index', 'NASDAQ China Large Mid Cap TR Index', 'NASDAQ China Small Cap Index', 'Nasdaq Overseas China New Economy Top 50 HKD TR', 'NASDAQ Golden Dragon China Total Return Index', 'NASDAQ Golden Dragon China Net Total Return Index', 'Dow Jones BRIC China 15 Index (EUR)', 'Nasdaq China Consumer Staples Large Mid Cap NTR Index', 'NASDAQ AlphaDEX China TR Index', 'NASDAQ China Health Care Index', 'Nasdaq China Basic Materials Large Mid Cap Index', 'NASDAQ China Small Cap TR Index', 'NASDAQ China Mid Cap Index', 'NASDAQ China Health Care NTR Index', 'NASDAQ China Utilities Large Mid Cap NTR Index', 'Nasdaq China Consumer Staples NTR Index', 'NASDAQ China Financials Large Mid Cap NTR Index', 'Nasdaq China Consumer Discretionary Large Mid Cap NTR Index', 'Nasdaq China Real Estate Large Mid Cap TR Index', 'NASDAQ China Financials Large Mid Cap TR Index', 'Nasdaq China Basic Materials NTR Index', 'Nasdaq China Financials Large Mid Cap Index', 'Nasdaq China Real Estate Index', 'NASDAQ Global plus China A Shares Index', 'Nasdaq China Energy NTR Index', 'NASDAQ China Utilities Large Mid Cap TR Index', 'Nasdaq China Industrials Large Mid Cap NTR Index', 'NASDAQ China Financials Index', 'Nasdaq China Health Care Large Mid Cap Index', 'Dow Jones BRIC China 15 Index (USD)', 'NASDAQ China Utilities NTR Index', 'Nasdaq China Basic Materials TR Index', 'NASDAQ China Index', 'Nasdaq China Real Estate Large Mid Cap NTR Index', 'NASDAQ China Utilities TR Index', 'Nasdaq China Consumer Discretionary NTR Index', 'NASDAQ China Large Mid Cap TR Index', 'NASDAQ China Small Cap Index', 'Nasdaq Overseas China New Economy Top 50 HKD TR', 'NASDAQ Golden Dragon China Total Return Index', 'NASDAQ Golden Dragon China Net Total Return Index', 'Dow Jones BRIC China 15 Index (EUR)', 'Nasdaq China Consumer Staples Large Mid Cap NTR Index', 'NASDAQ AlphaDEX China TR Index', 'NASDAQ China Health Care Index', 'Nasdaq China Basic Materials Large Mid Cap Index', 'NASDAQ China Small Cap TR Index', 'NASDAQ China Mid Cap Index', 'NASDAQ China Health Care NTR Index', 'NASDAQ China Utilities Large Mid Cap NTR Index', 'Nasdaq China Consumer Staples NTR Index', 'NASDAQ China Financials Large Mid Cap NTR Index', 'Nasdaq China Consumer Discretionary Large Mid Cap NTR Index', 'Nasdaq China Real Estate Large Mid Cap TR Index', 'NASDAQ China Financials Large Mid Cap TR Index', 'Nasdaq China Basic Materials NTR Index', 'Nasdaq China Financials Large Mid Cap Index', 'Nasdaq China Real Estate Index', 'NASDAQ Global plus China A Shares Index', 'Nasdaq China Energy NTR Index', 'NASDAQ China Utilities Large Mid Cap TR Index', 'Nasdaq China Industrials Large Mid Cap NTR Index', 'NASDAQ China Financials Index', 'Nasdaq China Health Care Large Mid Cap Index', 'Dow Jones BRIC China 15 Index (USD)', 'NASDAQ China Utilities NTR Index', 'Nasdaq China Basic Materials TR Index', 'NASDAQ China Index', 'Nasdaq China Real Estate Large Mid Cap NTR Index'],
volatility_indices=""['Cboe 3-Month Realized Volatility Index', 'Nasdaq US Low Volatility Dividend Achievers KRW Net Total Return Index', 'Nasdaq Nordea SmartBeta Momentum Volatility Eurozo', 'Nasdaq US Low Volatility Dividend Achievers KRW Total Return Index', 'NASDAQ Nordea SmartBeta Momentum Volatility Swe PR', 'Nasdaq 100 5% Target Volatility Index', 'NASDAQ Nordea SmartBeta Dividend Volatility Swe TR', 'Volatility NASDAQ - 100', 'Cboe S&P 500 Managed Volatility BuyWrite Index', 'DWA Emerging Market Momentum & Low Volatility TR', 'CBOE S&P 500 9-Day Volatility Index', 'VIX Component Volatility Index', 'DWA Switzerland Momentum & Low Volatility TR', 'Cboe Volatility Index', 'Realized Volatility Index', 'Cboe EuroCurrency Volatility Index', 'Cboe 6-Month Realized Volatility Index', 'Cboe DJIA Volatility Index', 'Cboe S&P 500 One-Year Volatility Index', 'Cboe NASDAQ-100 Volatility Index', 'CBOE S&P 500 Far-Term 9-Day Volatility Index', 'Cboe S&P 500 Market-Neutral Volatility Risk Premia Optimized Index', 'Cboe EFA ETF Volatility Index', 'Cboe Realized Volatility Index', 'Nasdaq Factor Laggard US Low Volatility NTR Index', 'Nasdaq Factor Laggard US Low Volatility Index', 'Nasdaq Factor Laggard US Low Volatility TR Index', 'Cboe 12-Month Realized Volatility Index', 'Cboe Volatility Index Options Settlement Price', 'DWA Developed Market Momentum & Low Volatility', 'DWA Emerging Market Momentum & Low Volatility NTR', 'CBOE S&P 500 6-Month Volatility Index', 'Nasdaq Victory US Multi-Factor Min Volatility TR', 'Cboe Crude Oil ETF Volatility Index', 'Cboe Gold ETF Volatility Index', 'NASDAQ Nordea SmartBeta Momentum Volatility Swe TR', 'Nasdaq US Low Volatility Dividend Achievers KRW Index', 'DWA Emerging Market Momentum & Low Volatility', 'Cboe Emerging Markets Volatility Index', 'CBOE S&P 500 Near-Term 9-Day Volatility Index', 'Cboe Brazil ETF Volatility Index', 'Nasdaq Nordea SmartBeta Volatility TR Index', 'Nasdaq Factor Family US Low Volatility TR Index', 'Defined Risk Volatility Income', 'Nasdaq Nordea SmartBeta Volatility PR Inde', 'DWA Switzerland Momentum & Low Volatility', 'Cboe Russell 2000 Volatility Index', 'Nasdaq Factor Family US Low Volatility NTR Index', 'Cboe S&P 500 3 Month Volatility Index', 'Nasdaq US Low Volatility Dividend Achievers Index', 'Cboe S&P 500 Volatility Managed PutWrite Index', 'DWA Developed Market Momentum & Low Volatility TR', 'Nasdaq-100 Volatility Index Final Settlement Price', 'Nasdaq US Low Volatility Dividend Achievers Total Return Index', 'Nasdaq Victory US Multi-Factor Minimum Volatility', 'Cboe Low Volatility Index', 'NASDAQ Nordea SmartBeta Dividend Volatility Swe PR', 'Dorsey Wright Momentum Plus Low Volatility Index', 'Nasdaq-100 Volatility Index VOLQ', 'Nasdaq Victory US Multi-Factor Mini Volatility NTR', 'CBOE Standard Monthly Only 30-day Volatility Index', 'DWA Switzerland Momentum & Low Volatility NTR', 'DWA Developed Market Momentum & Low Volatility NTR', 'Cboe Volatility Index Settlement Value', 'Nasdaq Factor Family US Low Volatility Index'],
skew_indices=""['Cboe SKEW Index', 'Cboe SMILE Index']
spx_dispersion_indices=""['Mini SPX Index (AM Settlement)', 'SPX Theta Weighted Dispersion', 'SPX Vega Weighted Dispersion', 'SPX Gamma Weighted Dispersion']
cloud=""['Nasdaq CTA International Cloud Computing Index', 'ISE CTA Cloud Computing Net Total Return Index', 'BVP Nasdaq Emerging Cloud TR Index', 'ISE CTA Cloud Computing Total Return Index', 'Nasdaq CTA International Cloud Computing Total Return Index', 'BVP Nasdaq Emerging Cloud Index', 'Nasdaq CTA International Cloud Computing Net Total Return Index', 'BVP Nasdaq Emerging Cloud NTR Index']
benchmark=""['Nasdaq US Benchmark Paints and Coatings Index', 'Nasdaq US Benchmark Mortgage REITs: Diversified TR Index', 'Nasdaq US Benchmark Technology Hardware and Equipment TR Index', 'Nasdaq US Benchmark Media Index', 'Nasdaq US Benchmark Retail TR Index', 'Nasdaq US Benchmark Diversified Materials Index', 'Nasdaq US Benchmark Casinos and Gambling Index', 'Nasdaq US Benchmark Software Index', 'NASDAQ US Benchmark TR Index', 'Nasdaq US Benchmark Alternative Electricity Index', 'OMX Stockholm Benchmark Cap_GI', 'Nasdaq US Benchmark Trucking Index', 'Nasdaq US Benchmark Delivery Services Index', 'Nasdaq US Benchmark Pharmaceuticals and Biotechnology Index', 'Nasdaq US Benchmark Footwear TR Index', 'Nasdaq US Benchmark Machinery: Specialty NTR Index', 'Nasdaq US Benchmark Auto Parts TR Index', 'Nasdaq US Benchmark Machinery: Construction and Handling NTR Index', 'Nasdaq US Benchmark Travel and Leisure NTR Index', 'Nasdaq US Benchmark Education Services TR Index', 'Nasdaq US Benchmark Infrastructure REITs NTR Index', 'Nasdaq US Benchmark Electronic Equipment: Control and Filter Index', 'Nasdaq US Benchmark Paper TR Index', 'Nasdaq US Benchmark Electronic Equipment: Other Index', 'Nasdaq US Benchmark Chemicals: Diversified TR Index', 'Nasdaq US Benchmark Diversified REITs NTR Index', 'Nasdaq US Benchmark Containers and Packaging TR Index', 'Nasdaq US Benchmark Auto Parts NTR Index', 'OMX_Baltic_Benchmark_GI', 'Nasdaq US Benchmark Consumer Lending TR Index', 'Nasdaq US Benchmark Auto Parts Index', 'Nasdaq US Benchmark Home Construction NTR Index', 'Nasdaq US Benchmark Industrial Materials NTR Index', 'Nasdaq US Benchmark Industrial Transportation Index', 'Nasdaq US Benchmark Real Estate Investment Trusts NTR Index', 'Nasdaq US Benchmark Financial Services Index', 'Nasdaq US Benchmark Apparel Retailers TR Index', 'Nasdaq US Benchmark Media Agencies NTR Index', 'Nasdaq US Benchmark Retail NTR Index', 'Nasdaq US Benchmark Health Care Management Services Index', 'Nasdaq US Benchmark Tobacco TR Index', 'Nasdaq US Benchmark Medical Equipment and Services NTR Index', 'Nasdaq US Benchmark Consumer Electronics TR Index', 'Nasdaq US Benchmark Diversified Materials TR Index', 'Nasdaq US Benchmark Food Products NTR Index', 'Nasdaq US Benchmark Hotels and Motels TR Index', 'OMX Stockholm Benchmark ESG Responsible Index', 'Nasdaq US Benchmark Consumer Services: Misc. Index', 'Nasdaq US Benchmark Retail Index', 'Nasdaq US Benchmark Integrated Oil and Gas Index', 'Nasdaq US Benchmark Beverages NTR Index', 'Nasdaq US Benchmark Footwear NTR Index', 'Nasdaq US Benchmark Chemicals Index', 'Nasdaq US Benchmark Reinsurance TR Index', 'Nasdaq US Benchmark Real Estate Investment and Services Index', 'Nasdaq US Benchmark Gas Distribution Index', 'Nasdaq US Benchmark Railroads TR Index', 'Nasdaq US Benchmark Cable Television Services NTR Index', 'Nasdaq US Benchmark Financial Services NTR Index', 'Nasdaq US Benchmark Residential REITs NTR Index', 'Nasdaq US Benchmark Multi-utilities TR Index', 'Nasdaq US Benchmark Food Products TR Index', 'Nasdaq US Benchmark Automobiles Index', 'Nasdaq US Benchmark Consumer Discretionary NTR Index', 'Nasdaq US Benchmark Business Training and Employment Agencies TR Index', 'Nasdaq US Benchmark Building: Climate Control NTR Index', 'Nasdaq US Benchmark Engineering and Contracting Services Index', 'Nasdaq US Benchmark Real Estate Services Index', 'Nasdaq US Benchmark Financials Index', 'Nasdaq US Benchmark Radio and TV Broadcasters Index', 'Nasdaq US Benchmark Metal Fabricating TR Index', 'Nasdaq US Benchmark Financials TR Index', 'Nasdaq US Benchmark Clothing and Accessories NTR Index', 'OMX Helsinki Benchmark_PI', 'Nasdaq US Benchmark Household Equipment and Products TR Index', 'Nasdaq US Benchmark Hotel and Lodging REITs NTR Index', 'Nasdaq US Benchmark Waste and Disposal Services Index', 'Nasdaq US Benchmark Technology Hardware and Equipment NTR Index', 'Nasdaq US Benchmark Alternative Electricity TR Index', 'Nasdaq US Benchmark Energy TR Index', 'Nasdaq US Benchmark Apparel Retailers Index', 'Nasdaq US Benchmark Toys TR Index', 'Nasdaq US Benchmark Electrical Components NTR Index', 'Nasdaq US Benchmark Real Estate Holding and Development Index', 'Nasdaq US Benchmark Gas, Water and Multi-utilities TR Index', 'Nasdaq US Benchmark Aerospace Index', 'Nasdaq US Benchmark Waste and Disposal Services TR Index', 'Nasdaq US Benchmark Paints and Coatings NTR Index', 'Nasdaq US Benchmark Soft Drinks NTR Index', 'Nasdaq US Benchmark Education Services NTR Index', 'Nasdaq US Benchmark Industrial Support Services NTR Index', 'Nasdaq US Benchmark Industrial Support Services Index', 'Nasdaq US Benchmark Toys NTR Index', 'Nasdaq US Benchmark Forms and Bulk Printing Services Index', 'Nasdaq US Benchmark Restaurants and Bars TR Index', 'Nasdaq US Benchmark Specialty Retailers Index', 'Nasdaq US Benchmark Commercial Vehicle-Equipment Leasing Index', 'OMX Stockholm Benchmark Cap_NI', 'OMX_Baltic_Benchmark_PI', 'Nasdaq US Benchmark Medical Equipment and Services TR Index', 'Nasdaq US Benchmark Restaurants and Bars NTR Index', 'Nasdaq US Benchmark Finance and Credit Services TR Index', 'Nasdaq US Benchmark Consumer Products and Services Index', 'Nasdaq US Benchmark Health Care Facilities Index', 'Nasdaq US Benchmark Drug Retailers Index', 'Nasdaq US Benchmark Telecommunications Equipment Index', 'Nasdaq US Benchmark Multi-utilities NTR Index', 'Nasdaq US Benchmark Biotechnology Index', 'Nasdaq US Benchmark Publishing Index', 'Nasdaq US Benchmark Telecommunications Equipment TR Index', 'Nasdaq US Benchmark Health Care Providers NTR Index', 'Nasdaq US Benchmark Oil Refining and Marketing Index', 'Nasdaq US Benchmark Mortgage REITs: Residential NTR Index', 'Nasdaq US Benchmark Coal NTR Index', 'OMX Copenhagen Benchmark Cap_PI', 'Nasdaq US Benchmark Distillers and Vintners Index', 'Nasdaq US Benchmark Investment Services Index', 'Nasdaq US Benchmark Footwear Index', 'Nasdaq US Benchmark Health Care NTR Index', 'Nasdaq US Benchmark Software NTR Index', 'OMX Stockholm Benchmark ESG Responsible Capped Net Index', 'Nasdaq US Benchmark Machinery: Agricultural NTR Index', 'Nasdaq US Benchmark Oil, Gas and Coal NTR Index', 'Nasdaq US Benchmark Software and Computer Services Index', 'Nasdaq US Benchmark Real Estate Services NTR Index', 'Nasdaq US Benchmark Electronic Equipment: Gauges and Meters Index', 'Nasdaq US Benchmark Home Construction TR Index', 'Nasdaq US Benchmark Consumer Services TR Index', 'Nasdaq US Benchmark Health Care Management Services NTR Index', 'OMX Copenhagen Benchmark Cap_GI', 'Nasdaq US Benchmark Electronic Equipment: Other TR Index', 'Nasdaq US Benchmark Consumer Electronics NTR Index', 'Nasdaq US Benchmark Health Care Facilities NTR Index', 'Nasdaq US Benchmark Containers and Packaging Index', 'Nasdaq US Benchmark Personal Goods NTR Index', 'Nasdaq US Benchmark Automobiles TR Index', 'Nasdaq US Benchmark Mortgage Finance Index', 'Nasdaq US Benchmark Telecommunications Services NTR Index', 'Nasdaq US Benchmark Nondurable Household Products NTR Index', 'Nasdaq US Benchmark Production Technology Equipment NTR Index', 'Nasdaq US Benchmark Health Care REITs NTR Index', 'Nasdaq US Benchmark Hotels and Motels Index', 'Nasdaq US Benchmark Other Specialty REITs TR Index', 'Nasdaq US Benchmark Aerospace and Defense NTR Index', 'Nasdaq US Benchmark Electricity NTR Index', 'Nasdaq US Benchmark Retailers Index', 'Nasdaq US Benchmark Full Line Insurance NTR Index', 'Nasdaq US Benchmark Life Insurance TR Index', 'Nasdaq US Benchmark Gold Mining NTR Index', 'Nasdaq US Benchmark Other Specialty REITs Index', 'Nasdaq US Benchmark Home Improvement Retailers TR Index', 'Nasdaq US Benchmark General Mining TR Index', 'Nasdaq US Benchmark Gas Distribution TR Index', 'Nasdaq US Benchmark Entertainment NTR Index', 'Nasdaq US Benchmark Health Care TR Index', 'Nasdaq US Benchmark Automobiles and Parts Index', 'Nasdaq US Benchmark Renewable Energy Equipment Index', 'Nasdaq US Benchmark Specialty Retailers TR Index', 'Nasdaq US Benchmark Consumer Digital Services NTR Index', 'Nasdaq US Benchmark Electricity TR Index', 'Nasdaq US Benchmark Security Services NTR Index', 'Nasdaq US Benchmark Transaction Processing Services NTR Index', 'Nasdaq US Benchmark Industrial Metals and Mining TR Index', 'Nasdaq US Benchmark Specialty Retailers NTR Index', 'Nasdaq US Benchmark Business Training and Employment Agencies Index', 'Nasdaq US Benchmark Health Care Management Services TR Index', 'Nasdaq US Benchmark Office REITs NTR Index', 'Nasdaq US Benchmark Other Specialty REITs NTR Index', 'Nasdaq US Benchmark Basic Resources Index', 'Nasdaq US Benchmark Commercial Vehicle-Equipment Leasing NTR Index', 'Nasdaq US Benchmark Nondurable Household Products Index', 'Nasdaq US Benchmark Health Care REITs Index', 'Nasdaq US Benchmark Property and Casualty Insurance NTR Index', 'OMX Helsinki Benchmark CAP_PI', 'Nasdaq US Benchmark Gold Mining TR Index', 'Nasdaq US Benchmark Paper Index', 'OMX Stockholm Benchmark ESG Responsible Net Index', 'Nasdaq US Benchmark Real Estate NTR Index', 'Nasdaq US Benchmark Asset Managers and Custodians Index', 'Nasdaq US Benchmark']
futures=""['Cboe 1st Month VIX Futures 15 Mins EOD Ind TWAP Value', 'Cboe 1st VIX Futures 15min Indicative TWAP Midpoint Value', 'Cboe VIX Jan Futures 4pm EST Mark Index', 'Cboe 2nd VIX Futures 15min Indicative TWAP Midpoint Value', 'Long VIX Futures Index', 'Dow Jones Industrial Average Futures Index (USD) TR', 'Dow Jones Industrial Average Futures 2X Inverse Daily Index (USD) TR', 'Cboe 8th VIX Futures Mid-Morning Indicative TWAP Value', 'Cboe VIX May Futures 4 pm EST Mark Index', '2x Long VIX Futures ETF January Intraday Indicative Value', 'Dow Jones Industrial Average Futures 2X Leveraged Daily Index (USD) TR', 'Cboe 2nd VIX Futures Mid-Morning 3hour Ind TWAP Value', 'Cboe VIX Feb Futures 4pm EST Mark Index', 'Cboe VIX Oct Futures 4 pm EST Mark Index', 'Cboe VIX Nov Futures 4 pm EST Mark Index', 'Cboe VIX Mar Futures 4 pm EST Mark Index', 'Cboe 2nd VIX Futures 15min Indicative TWAP Ask Value', 'Short VIX Futures Index', 'ProShares Short VIX Short-Term Futures ETF', 'Cboe VIX Sep Futures 4 pm EST Mark Index', 'Cboe 2nd VIX Futures Mid-Morning Indicative TWAP Value', 'Cboe 6th VIX Futures Mid-Morning Indicative TWAP Value', 'Cboe 1st VIX Futures Mid-Morning Indicative TWAP Value', 'Cboe 5th VIX Futures Mid-Morning Indicative TWAP Value', 'Mid-morning TWAP value of Cboe 2nd VIX Futures', 'Dynamic Short VIX Futures Index', 'Dynamic Long VIX Futures Index', 'Cboe VIX Apr Futures 4 pm EST Mark Index', 'ProShares VIX Short-Term Futures ETF', 'ProShares VIX Mid-Term Futures ETF', 'Cboe VIX Jun Futures 4 pm EST Mark Index', 'Cboe VIX Dec Futures 4 pm EST Mark Index', 'Mid-morning TWAP value of Cboe 1st VIX Futures', 'ProShares Ultra VIX Short-Term Futures ETF', 'Cboe VIX Jul Futures 4 pm EST Mark Index', 'S&P 500 VIX Futures Enhanced Roll Index ER', 'Cboe 3rd VIX Futures TAS Ask Price Index', 'Cboe 1st VIX Futures TAS Ask Price Index', 'Cboe 4th VIX Futures Mid-Morning Indicative TWAP Value', '-1x Short VIX Futures ETF - Intraday Indicative Value', 'Cboe 2nd Month VIX Futures 15 Mins EOD Ind TWAP Value', 'Cboe VX Futures 3rd Near-Term Month Indicative Daily Settlement Value', 'Cboe 2nd VIX Futures TAS Bid Price Index', 'Mid-morning TWAP value of Cboe 9th VIX Futures', 'S&P 500 Dynamic VIX Futures Index ER', 'Cboe 1st VIX Futures 15min Indicative TWAP Ask Value', 'Cboe 3rd VIX Futures Mid-Morning Indicative TWAP Value', 'Cboe 3rd VIX Futures TAS Bid Price Index', 'Cboe 1st VIX Futures 15min Indicative TWAP Bid Value', 'Cboe 2nd VIX Futures 15min Indicative TWAP Bid Value', 'Cboe 1st VIX Futures Mid-Morning 3hour Ind TWAP Value', 'Cboe 3rd VIX Futures Mid-Morning 15 Minute Indicative TWAP Value', 'Cboe VX Futures 1st Near-Term Month Indicative Daily Settlement Value', 'Cboe 3rd VIX Futures Mid-Morning 3 Hour Indicative TWAP Value', 'S&P 500 Dynamic VIX Futures Index TR', 'Cboe VX Futures 2nd Near-Term Month Indicative Daily Settlement Value', 'Cboe 1st VIX Futures TAS Bid Price Index', 'Dow Jones Industrial Average Futures Inverse Daily Index (USD) TR']
short_indices=""['Dow Jones U.S. Thematic Short Size Index', 'VelocityShares Daily 2x VIX Short-Term ETN Intraday Indicative Value', 'Dynamic Short VIX Futures Index', 'Nasdaq Short Duration Diversified Income TR Index', 'NASDAQ-100 2x Short Net Total Return Index', 'Cboe Short-Term Interest Rate Index', 'Cboe S&P 500 4% OTM Short Strangle Index (with KRW 3 month Certificate of Deposit)', 'Dow Jones U.S. Thematic Short Quality Total Return Index', 'NASDAQ-100 2x Short Total Return Index', 'Touchstone Ultra Short Income ETF', 'Dow Jones U.S. Thematic Short Size Total Return Index', 'NASDAQ-100 2x Short Index', 'Dow Jones U.S. Short Relative Value Total Return Index', 'Dow Jones U.S. Select Short-Term REIT Index NTR', 'Dow Jones U.S. Thematic Short Quality Index', 'Dow Jones U.S. Short Relative Value Index', 'NASDAQ-100 1x Short Total Return Index', 'NASDAQ-100 1x Short Net Total Return Index', 'Short VIX Futures Index', 'ProShares Short VIX Short-Term Futures ETF', 'ProShares Short Bitcoin Strategy ETF', 'NASDAQ-100 1x Short Index', 'ProShares VIX Short-Term Futures ETF', 'VelocityShares VIX Short-Term ETN Intraday Indicative Value', '-1x Short VIX Futures ETF - Intraday Indicative Value', 'ProShares Ultra VIX Short-Term Futures ETF']
us_dollar=""['Cboe 15 Augur / US Dollar RealPrice Index', 'Cboe 100 Zcash / US Dollar RealPrice Index', 'Cboe 25K Ripple / US Dollar RealPrice Index', 'Cboe 2000 OMG / US Dollar RealPrice Index', 'Cboe 100 Solana / US Dollar RealPrice Index', 'Bitcoin Cash vs US Dollar', 'Cboe 100 Tezos / US Dollar RealPrice Index', 'Cboe 2500 Chainlink / US Dollar RealPrice Index', 'Cboe 5000 Waves / US Dollar RealPrice Index', 'Cboe 40 Eos / US Dollar RealPrice Index', 'Cboe 25K Cardano / US Dollar RealPrice Index', 'Bitcoin vs US Dollar', 'Cboe 250 Augur / US Dollar RealPrice Index', 'Cboe 25 QTUM / US Dollar RealPrice Index', 'Cboe 2000 Ethereum Classic / US Dollar RealPrice Index', 'Cboe 1000 QTUM / US Dollar RealPrice Index', 'Cboe 500 Bancor / US Dollar RealPrice Index', 'Cboe 500 Basic Attention Token / US Dollar RealPrice Index', 'Cboe 100K Cardano / US Dollar RealPrice Index', 'Cboe 25K Orchid / US Dollar RealPrice Index', 'Cboe 100 Filecoin / US Dollar RealPrice Index', 'Cboe 400 Eos / US Dollar RealPrice Index', 'Cboe 20 Zcash / US Dollar RealPrice Index', 'Cboe 25K Polygon / US Dollar RealPrice Index', 'Cboe 1000 Polygon / US Dollar RealPrice Index', 'Cboe 300 Cosmos / US Dollar RealPrice Index', 'Cboe 1000 Orchid / US Dollar RealPrice Index', 'Cboe 50 Dash / US Dollar RealPrice Index', 'Cboe 5 Dash / US Dollar RealPrice Index', 'Cboe 50 Bancor / US Dollar RealPrice Index', 'Cboe 25 Aave / US Dollar RealPrice Index', 'Cboe 1000 Uniswap / US Dollar RealPrice Index', 'Cboe 100 QTUM / US Dollar RealPrice Index', 'Cboe 200 Tezos / US Dollar RealPrice Index', 'Cboe 400 Aave / US Dollar RealPrice Index', 'Cboe 2000 Stellar / US Dollar RealPrice Index', 'Cboe 400 Binance Coin / US Dollar RealPrice Index', 'Cboe 5000 Filecoin / US Dollar RealPrice Index', 'Cboe 2000 Bancor / US Dollar RealPrice Index', 'Cboe 9000 Stellar / US Dollar RealPrice Index', 'Cboe 50 Tezos / US Dollar RealPrice Index', 'Cboe 5000 Orchid / US Dollar RealPrice Index', 'Cboe 1000 Filecoin / US Dollar RealPrice Index', 'Cboe 20K Waves / US Dollar RealPrice Index', 'Cboe 100 Algorand / US Dollar RealPrice Index', 'Cboe 75 Cosmos / US Dollar RealPrice Index', 'Cboe 500 Kyber Network / US Dollar RealPrice Index', 'Cboe 5 Maker / US Dollar RealPrice Index', 'Cboe 500 Filecoin / US Dollar RealPrice Index', 'Cboe 3000 0x / US Dollar RealPrice Index', 'Cboe 2000 Kyber Network / US Dollar RealPrice Index', 'Cboe 10 Eos / US Dollar RealPrice Index', 'Cboe 50 Maker / US Dollar RealPrice Index', 'Cboe 10K Decentraland / US Dollar RealPrice Index', 'Cboe 5 Binance Coin / US Dollar RealPrice Index', 'Cboe 75 Tezos / US Dollar RealPrice Index', 'Cboe 10 Zcash / US Dollar RealPrice Index', 'Cboe 500 OMG / US Dollar RealPrice Index', 'Cboe 3000 Decentraland / US Dollar RealPrice Index', 'Cboe 100 OMG / US Dollar RealPrice Index', 'Cboe 5000 Chainlink / US Dollar RealPrice Index', 'Cboe 500 Stellar / US Dollar RealPrice Index', 'Cboe 2000 QTUM / US Dollar RealPrice Index', 'Cboe 20 Dash / US Dollar RealPrice Index', 'Cboe 100 Ethereum Classic / US Dollar RealPrice Index', 'Cboe 100 Basic Attention Token / US Dollar RealPrice Index', 'Cboe 200K 0x / US Dollar RealPrice Index', 'Cboe 25 OMG / US Dollar RealPrice Index', 'Cboe 200K Ripple / US Dollar RealPrice Index', 'Cboe 500 QTUM / US Dollar RealPrice Index', 'Cboe 10 Maker / US Dollar RealPrice Index', 'Cboe 50K Cardano / US Dollar RealPrice Index', 'Litecoin vs US Dollar', 'Cboe 100 Dash / US Dollar RealPrice Index', 'Cboe 500 Decentraland / US Dollar RealPrice Index', 'Cboe 5000 Solana / US Dollar RealPrice Index', 'Cboe 2500 Solana / US Dollar RealPrice Index', 'Cboe 500K Dogecoin / US Dollar RealPrice Index', 'Cboe 100K Ripple / US Dollar RealPrice Index', 'Ether vs US Dollar', 'Cboe 150 Cosmos / US Dollar RealPrice Index', 'Cboe 5000 Algorand / US Dollar RealPrice Index', 'Cboe 100 Binance Coin / US Dollar RealPrice Index', 'Cboe 100 Aave / US Dollar RealPrice Index', 'Cboe 100 Eos / US Dollar RealPrice Index', 'Cboe 800 Eos / US Dollar RealPrice Index', 'Cboe 500 Solana / US Dollar RealPrice Index', 'Cboe 50 Uniswap / US Dollar RealPrice Index', 'Cboe 250 Ethereum Classic / US Dollar RealPrice Index', 'Cboe 250 Uniswap / US Dollar RealPrice Index', 'Cboe 1000 OMG / US Dollar RealPrice Index', 'Cboe 5 Zcash / US Dollar RealPrice Index', 'Cboe 250 Waves / US Dollar RealPrice Index', 'Cboe 100K Polygon / US Dollar RealPrice Index', 'Cboe 5000 Uniswap / US Dollar RealPrice Index', 'Cboe 10K Cardano / US Dollar RealPrice Index', 'Cboe 2 Maker / US Dollar RealPrice Index', 'Cboe 50 Aave / US Dollar RealPrice Index', 'Cboe 1000 0x / US Dollar RealPrice Index', 'Cboe 200K Dogecoin / US Dollar RealPrice Index', 'Cboe 5000 Cardano / US Dollar RealPrice Index', 'Cboe 10K 0x / US Dollar RealPrice Index', 'Cboe 200 Bancor / US Dollar RealPrice Index', 'Cboe 500 Ethereum Classic / US Dollar RealPrice Index', 'Cboe 50K Polygon / US Dollar RealPrice Index', 'Cboe 1000 Kyber Network / US Dollar RealPrice Index', 'Cboe 10 Aave / US Dollar RealPrice Index', 'Cboe 200 Basic Attention Token / US Dollar RealPrice Index', 'Cboe 1250 Decentraland / US Dollar RealPrice Index', 'Cboe 25 Maker / US Dollar RealPrice Index']
basic_materials_indices=""['Nasdaq EM Europe Basic Materials NTR Index', 'Nasdaq Norway Basic Materials NTR Index', 
                         'Nasdaq Korea Basic Materials Large Mid Cap NTR Index', 'Nasdaq China Basic Materials NTR Index', 
                         'Nasdaq Netherlands Basic Materials TR Index', 'Nasdaq Canada Basic Materials Large Mid Cap NTR Index', 
                         'Nasdaq Korea Basic Materials TR Index', 'Nasdaq Sweden Basic Materials Large Mid Cap NTR Index', 
                         'Nasdaq India Basic Materials NTR Index', 'Nasdaq Netherlands Basic Materials Large Mid Cap NTR Index', 
                         'Nasdaq Finland Basic Materials TR Index', 'Nasdaq ASPA Basic Materials Large Mid Cap NTR Index', 
                         'Nasdaq India Basic Materials Large Mid Cap Index', 'Nasdaq US Small Cap Basic Materials Index', 
                         'Nasdaq Taiwan Basic Materials TR Index', 'Nasdaq Brazil Basic Materials Large Mid Cap NTR Index', 
                         'Dow Jones Islamic Market Basic Materials Total Return Index', 'Nasdaq Singapore Basic Materials TR Index', 
                         'Nasdaq Developed Markets Basic Materials NTR Index', 'Nasdaq N America Basic Materials Large Mid Cap Index', 
                         'Nasdaq DM Europe Basic Materials Large Mid Cap Index', 'Nasdaq China Basic Materials Large Mid Cap NTR Index', 
                         'Nasdaq Finland Basic Materials Index', 'Nasdaq Norway Basic Materials Index', 
                         'Nasdaq Taiwan Basic Materials Large Mid Cap Index', 'Nasdaq ASPA Basic Materials Large Mid Cap Index', 
                         'Nasdaq Asia Basic Materials Large Mid Cap Index', 'Nasdaq South Africa Basic Materials NTR Index', 
                         'Nasdaq EM Asia Basic Materials Large Mid Cap TR Index', 'Nasdaq Asia Basic Materials Large Mid Cap NTR Index', 
                         'Nasdaq North America Basic Materials TR Index', 'Nasdaq Indonesia Basic Materials Large Mid Cap TR Index', 
                         'Nasdaq DM Europe Basic Materials Large Mid Cap NTR Index', 'Nasdaq Asia Basic Materials TR Index', 
                         'N Basic Materials EUR GI', 'Nasdaq US Benchmark Basic Materials TR Index', 'Nasdaq EM Europe Basic Materials Index', 
                         'Nasdaq Spain Basic Materials TR Index', 'Nasdaq Japan Basic Materials Index', 'Nasdaq US Mid Cap Basic Materials Index', 
                         'Nasdaq South Africa Basic Materials TR Index', 'Nasdaq China Basic Materials Large Mid Cap Index', 
                         'Nasdaq Taiwan Basic Materials Index', 'Nasdaq Australia Basic Materials NTR Index', 'Nasdaq EMEA Basic Materials Index', 
                         'Nasdaq Netherlands Basic Materials Index', 'Nasdaq South Africa Basic Materials Large Mid Cap Index', 
                         'Nasdaq Finland Basic Materials NTR Index', 'Nasdaq DM Asia Basic Materials Large Mid Cap Index', 
                         'Nasdaq Eurozone Basic Materials NTR Index', 'Nasdaq Latin America Basic Materials Large Mid Cap Index', 
                         'Nasdaq EM MEA Basic Materials Large Mid Cap TR Index', 'Nasdaq DM ASPA Basic Materials TR Index', 
                         'Nasdaq United Kingdom Basic Materials Large Mid Cap Index', 'Nasdaq US Benchmark Basic Materials Index', 
                         'Nasdaq South Africa Basic Materials Large Mid Cap NTR Index', 'Nasdaq BRIC Basic Materials Large Mid Cap Index', 
                         'Nasdaq US Small Cap Basic Materials TR Index', 'Nasdaq DM Asia Basic Materials Large Mid Cap TR Index', 
                         'Nasdaq Australia Basic Materials Large Mid Cap TR Index', 'Dow Jones U.S. Basic Materials Index', 
                         'Nasdaq Developed Markets Basic Materials Large Mid Cap NTR Index', 'Nasdaq Mexico Basic Materials Large Mid Cap Index', 
                         'Nasdaq US Large Cap Basic Materials Index', 'Nasdaq EM Asia Basic Materials Large Mid Cap Index', 
                         'CRSP US Basic Materials Total Return Index', 'Nasdaq BRIC Basic Materials Large Mid Cap TR Index', 
                         'Nasdaq South Africa Basic Materials Large Mid Cap TR Index', 'Nasdaq US Large Cap Basic Materials TR Index', 
                         'Nasdaq Asia Basic Materials Index', 'Nasdaq Singapore Basic Materials NTR Index', 'Nasdaq DM Asia Basic Materials Index', 
                         'Nasdaq Turkey Basic Materials NTR Index', 'Nasdaq MEA Basic Materials Index', 'Nasdaq Germany Basic Materials NTR Index', 
                         'Dow Jones Global Basic Materials Index', 'Nasdaq Sweden Basic Materials Large Mid Cap Index', 
                         'Nasdaq Eurozone Basic Materials Large Mid Cap TR Index', 'Nasdaq Sweden Basic Materials Index', 
                         'Nasdaq Global Basic Materials TR Index', 'Nasdaq Turkey Basic Materials TR Index', 'Nasdaq Indonesia Basic Materials NTR Index', 'Nasdaq Netherlands Basic Materials Large Mid Cap Index', 'Nasdaq Taiwan Basic Materials Large Mid Cap TR Index', 'Nasdaq United Kingdom Basic Materials Large Mid Cap TR Index', 'Nasdaq Brazil Basic Materials Large Mid Cap TR Index', 'Nasdaq US Benchmark Basic Materials NTR Index', 'Nasdaq US Mid Cap Basic Materials TR Index', 'Nasdaq MEA Basic Materials TR Index', 'Nasdaq North America Basic Materials NTR Index', 'Nasdaq DM MEA Basic Materials TR Index', 'Nasdaq China Basic Materials TR Index', 'Nasdaq Eurozone Basic Materials Large Mid Cap NTR Index', 'Nasdaq Emerging Markets Basic Materials Large Mid Cap NTR Index', 'Nasdaq Belgium Basic Materials TR Index', 'Nasdaq Europe Basic Materials Index', 'Nasdaq Netherlands Basic Materials Large Mid Cap TR Index', 'Nasdaq Australia Basic Materials TR Index', 'Nasdaq DM Europe Basic Materials Index', 'Nasdaq Israel Basic Materials NTR Index', 'OMX Helsinki Basic Materials GI', 'Nasdaq Malaysia Basic Materials NTR Index', 'Nasdaq ASPA Basic Materials Large Mid Cap TR Index', 'Nasdaq EM Asia Basic Materials NTR Index', 'Nasdaq Japan Basic Materials TR Index', 'Nasdaq DM ASPA Basic Materials Large Mid Cap NTR Index', 'Nasdaq China Basic Materials Large Mid Cap TR Index', 'NASDAQ DM Ex US Basic Materials NTR Index', 'Nasdaq Singapore Basic Materials Index', 'Nasdaq Indonesia Basic Materials Large Mid Cap NTR Index', 'Nasdaq Eurozone Basic Materials TR Index', 'Nasdaq EM MEA Basic Materials Large Mid Cap NTR Index', 'Nasdaq Taiwan Basic Materials Large Mid Cap NTR Index', 'Nasdaq Japan Basic Materials Large Mid Cap TR Index', 'Nasdaq Philippines Basic Materials TR Index', 'Nasdaq Israel Basic Materials TR Index', 'Nasdaq Sweden Basic Materials NTR Index', 'Nasdaq Australia Basic Materials Large Mid Cap NTR Index', 'Nasdaq BRIC Basic Materials Large Mid Cap NTR Index', 'First North Basic Materials GI', 'Nasdaq Canada Basic Materials TR Index', 'Nasdaq Europe Basic Materials Large Mid Cap NTR Index', 'Nasdaq Mexico Basic Materials Index', 'Nasdaq Asia Basic Materials NTR Index', 'Nasdaq India Basic Materials TR Index', 'Nasdaq United Kingdom Basic Materials Index', 'Nasdaq United Kingdom Basic Materials Large Mid Cap NTR Index', 'Nasdaq Sweden Basic Materials TR Index', 'Nasdaq Europe Basic Materials Large Mid Cap TR Index', 'Nasdaq Brazil Basic Materials NTR Index', 'Nasdaq EM Europe Basic Materials Large Mid Cap TR Index', 'Nasdaq Netherlands Basic Materials NTR Index', 'Nasdaq Europe Basic Materials NTR Index', 'Nasdaq Emerging Markets Basic Materials TR Index', 'OMX Stockholm Basic Materials GI', 'Nasdaq Australia Basic Materials Index', 'Nasdaq Thailand Basic Materials NTR Index', 'Nasdaq Switzerland Basic Materials Index', 'Nasdaq Canada Basic Materials Index', 'Nasdaq Canada Basic Materials Large Mid Cap Index', 'Nasdaq DM ASPA Basic Materials Index', 'Nasdaq Latin America Basic Materials TR Index', 'Nasdaq Latin America Basic Materials Index', 'First North Basic Materials PI', 'Nasdaq Brazil Basic Materials TR Index', 'Nasdaq DM Asia Basic Materials NTR Index', 'Nasdaq Global Basic Materials NTR Index', 'N Basic Materials EUR PI', 'Nasdaq EMEA Basic Materials Large Mid Cap Index', 'Nasdaq France Basic Materials TR Index', 'Nasdaq Global Basic Materials Large Mid Cap NTR Index', 
                         'Nasdaq MEA Basic Materials Large Mid Cap NTR Index', 'Nasdaq Asia Basic Materials Large Mid Cap TR Index', 'Nasdaq Korea Basic Materials NTR Index', 'Dow Jones Americas Basic Materials Index', 'Nasdaq EM MEA Basic Materials Large Mid Cap Index', 'Dow Jones Islamic Market Basic Materials Index', 'Nasdaq EMEA Basic Materials NTR Index', 'Dow Jones Europe ex-U.K. Basic Materials Index', 'Nasdaq Canada Basic Materials NTR Index', 'Nasdaq DM Europe Basic Materials TR Index', 'Nasdaq US Basic Materials Large Mid Cap Index', 'Nasdaq DM Asia Basic Materials Large Mid Cap NTR Index', 'Nasdaq DM Asia Basic Materials TR Index', 'Nasdaq US Basic Materials Large Mid Cap NTR Index', 'Nasdaq US Mid Cap Basic Materials NTR Index', 'Nasdaq Switzerland Basic Materials NTR Index', 'Nasdaq DM Europe Basic Materials Large Mid Cap TR Index', 'Nasdaq Brazil Basic Materials Large Mid Cap Index', 'Nasdaq India Basic Materials Index', 'Nasdaq EMEA Basic Materials Large Mid Cap NTR Index', 'Dorsey Wright Basic Materials Tech Leaders', 'Nasdaq Poland Basic Materials NTR Index', 'Nasdaq DM ASPA Basic Materials Large Mid Cap Index', 'Nasdaq Developed Markets Basic Materials Index', 'Nasdaq Indonesia Basic Materials TR Index', 'Nasdaq Germany Basic Materials Large Mid Cap Index', 'OMX Helsinki Basic Materials PI', 'Nasdaq Mexico Basic Materials NTR Index', 'Nasdaq Australia Basic Materials Large Mid Cap Index', 'Nasdaq Indonesia Basic Materials Large Mid Cap Index', 'Nasdaq BRIC Basic Materials NTR Index', 'Nasdaq EM Asia Basic Materials Index', 'Nasdaq Malaysia Basic Materials Index', 'Nasdaq Emerging Markets Basic Materials Index', 'Nasdaq DM MEA Basic Materials NTR Index', 'Nasdaq ASPA Basic Materials NTR Index', 'Nasdaq DM ASPA Basic Materials NTR Index', 'Nasdaq Global Basic Materials Index', 'NASDAQ DM Ex US Basic Materials TR Index', 'Nasdaq Malaysia Basic Materials TR Index', 'Nasdaq DM Europe Basic Materials NTR Index', 'Nasdaq Germany Basic Materials Large Mid Cap NTR Index', 'Nasdaq Latin America Basic Materials NTR Index', 'Nasdaq Turkey Basic Materials Index', 'Nasdaq France Basic Materials Index', 'Nasdaq Developed Markets Basic Materials Large Mid Cap TR Index', 'Nasdaq Emerging Markets Basic Materials Large Mid Cap Index', 'Nasdaq MEA Basic Materials Large Mid Cap TR Index', 'Nasdaq Europe Basic Materials TR Index', 'Nasdaq Europe Basic Materials Large Mid Cap Index', 'Nasdaq EM Europe Basic Materials Large Mid Cap NTR Index', 'Nasdaq Japan Basic Materials NTR Index', 'Dow Jones U.S. Basic Materials Total Stock Market Index', 'Nasdaq Developed Markets Basic Materials TR Index', 'Nasdaq Philippines Basic Materials NTR Index', 'Dow Jones Europe Basic Materials Index', 'Nasdaq Hong Kong Basic Materials Index', 'Nasdaq US Basic Materials Large Mid Cap TR Index', 'Nasdaq ASPA Basic Materials Index', 'Nasdaq Mexico Basic Materials Large Mid Cap NTR Index', 'Nasdaq DM MEA Basic Materials Index', 'Nasdaq Thailand Basic Materials Index', 'Dow Jones Global ex-U.S. Basic Materials Index', 'Nasdaq Poland Basic Materials TR Index', 'Nasdaq Germany Basic Materials TR Index', 'Nasdaq Eurozone Basic Materials Index', 'CRSP US Basic Materials Index', 'Nasdaq Brazil Basic Materials Index', 'Nasdaq ASPA Basic Materials TR Index', 'Nasdaq India Basic Materials Large Mid Cap NTR Index', 'Nasdaq Developed Markets Basic Materials Large Mid Cap Index', 'Nasdaq Global Basic Materials Large Mid Cap TR Index', 'Nasdaq North America Basic Materials Index', 'Nasdaq Germany Basic Materials Index', 'Nasdaq Hong Kong Basic Materials NTR Index', 'Nasdaq Hong Kong Basic Materials TR Index', 'NASDAQ DM Ex US Basic Materials Index', 'Nasdaq BRIC Basic Materials TR Index', 'Nasdaq South Africa Basic Materials Index', 'Dorsey Wright Basic Materials Tech Leaders TR', 'Nasdaq BRIC Basic Materials Index', 'OMX Stockholm Basic Materials PI', 'Nasdaq EMEA Basic Materials TR Index', 'Nasdaq EM Europe Basic Materials TR Index', 'Nasdaq MEA Basic Materials Large Mid Cap Index', 'Nasdaq EMEA Basic Materials Large Mid Cap TR Index', 'Nasdaq Japan Basic Materials Large Mid Cap NTR Index', 'Nasdaq Poland Basic Materials Index', 'Nasdaq Sweden Basic Materials Large Mid Cap TR Index', 'Nasdaq Belgium Basic Materials NTR Index', 'Nasdaq France Basic Materials NTR Index', 'OMX Baltic Basic Materials GI', 'Nasdaq Mexico Basic Materials TR Index', 'Nasdaq Norway Basic Materials TR Index', 'Nasdaq Eurozone Basic Materials Large Mid Cap Index', 'Nasdaq Philippines Basic Materials Index', 'Nasdaq Korea Basic Materials Index', 'Nasdaq Global Basic Materials Large Mid Cap Index', 'Nasdaq EM MEA Basic Materials TR Index', 'Nasdaq Spain Basic Materials NTR Index', 'Nasdaq Germany Basic Materials Large Mid Cap TR Index', 'Nasdaq United Kingdom Basic Materials NTR Index', 'OMX Baltic Basic Materials PI', 'Nasdaq N America Basic Materials Large Mid Cap NTR Index', 'Nasdaq DM ASPA Basic Materials Large Mid Cap TR Index', 'Nasdaq Israel Basic Materials Index', 'Nasdaq Japan Basic Materials Large Mid Cap Index', 'Nasdaq Mexico Basic Materials Large Mid Cap TR Index', 'Nasdaq India Basic Materials Large Mid Cap TR Index', 'Nasdaq EM Asia Basic Materials Large Mid Cap NTR Index', 'Nasdaq Indonesia Basic Materials Index', 'Nasdaq EM Europe Basic Materials Large Mid Cap Index', 'Nasdaq Korea Basic Materials Large Mid Cap Index', 'Nasdaq Switzerland Basic Materials TR Index', 'Nasdaq N America Basic Materials Large Mid Cap TR Index', 'Nasdaq Latin America Basic Materials Large Mid Cap TR Index', 'Nasdaq EM Asia Basic Materials TR Index', 'Nasdaq United Kingdom Basic Materials TR Index', 'Nasdaq Taiwan Basic Materials NTR Index', 'Dow Jones U.S. Basic Materials Total Return Index', 'Nasdaq Emerging Markets Basic Materials NTR Index', 'Nasdaq US Large Cap Basic Materials NTR Index', 'Nasdaq Latin America Basic Materials Large Mid Cap NTR Index', 'Nasdaq Thailand Basic Materials TR Index', 'Nasdaq Canada Basic Materials Large Mid Cap TR Index', 'Nasdaq MEA Basic Materials NTR Index', 'Nasdaq Spain Basic Materials Index', 'Nasdaq Emerging Markets Basic Materials Large Mid Cap TR Index', 'Nasdaq US Small Cap Basic Materials NTR Index', 'Nasdaq China Basic Materials Index', 'Nasdaq EM MEA Basic Materials NTR Index', 'Nasdaq Korea Basic Materials Large Mid Cap TR Index', 'Nasdaq EM MEA Basic Materials Index', 'Nasdaq Belgium Basic Materials Index']
technology_indices=""['KBW Nasdaq Financial Technology TR Index', 'NASDAQ OMX China Technology', 'Nasdaq US Benchmark Technology Index', 'Nasdaq China Technology Large Mid Cap TR Index', 'Nasdaq US Small Cap Technology Hardware and Equipment NTR Index', 'Nasdaq China Technology Large Mid Cap Index', 'Nasdaq Emerging Markets Technology Large Mid Cap Index', 'OMX Iceland Technology GI', 'Nasdaq Netherlands Technology Large Mid Cap NTR Index', 'Nasdaq China Technology Index', 'Nasdaq US Large Cap Technology Index', 'Nasdaq CTA Global Climate Technology Index', 'Strategic Technology & Ecommerce Real Estate Net Total Return GBP Index', 'Nasdaq US Mid Cap Technology Hardware and Equipment Index', 'Nasdaq Small Cap Production Technology Equipment TR Index', 'Dow Jones U.S. Technology Hardware & Equipment Total Stock Market Index', 'Nasdaq EMEA Technology Large Mid Cap Index', 'Strategic Technology & Ecommerce Real Estate Total Return GBP Index', 'Dow Jones U.S. Technology Total Return Index', 'Nasdaq MEA Technology Index', 'Strategic Technology & Ecommerce Real Estate Total Return EUR Index', 'Nasdaq Switzerland Technology TR Index', 'Nasdaq Japan Technology Large Mid Cap TR Index', 'Nasdaq Israel Technology NTR Index', 'Dow Jones Technology Titans 30 Total Return Index', 'Nasdaq South Africa Technology TR Index', 'Nasdaq CTA Global Climate Technology Total Return Index', 'Nasdaq Hong Kong Technology NTR Index', 'Nasdaq Germany Technology Large Mid Cap NTR Index', 'Nasdaq Developed Markets Technology Index', 'Nasdaq US Benchmark Technology NTR Index', 'Nasdaq Canada Technology NTR Index', 'Nasdaq Korea Technology Large Mid Cap Index', 'Nasdaq Korea Technology TR Index', 'Nasdaq CTA Global Climate Technology Net Total Return Index', 'Nasdaq Italy Technology NTR Index', 'Nasdaq US Large Cap Technology TR Index', 'OMX Copenhagen Technology Hardware and Equipment GI', 'NASDAQ Technology Dividend TR Index', 'Nasdaq MEA Technology TR Index', 'OMX Helsinki Technology Hardware and Equipment GI', 'Nasdaq BRIC Technology NTR Index', 'Dow Jones Islamic Market Technology Index', 'NASDAQ-100 Technology Sector Market-Cap Weighted T', 'Nasdaq Europe Technology Large Mid Cap Index', 'Nasdaq Asia Technology NTR Index', 'Dow Jones U.S. Technology Index Capped (USD) TR', 'Nasdaq Canada Technology Large Mid Cap TR Index', 'Nasdaq Taiwan Technology NTR Index', 'Strategic Technology & Ecommerce Real Estate Net Total Return CAD Index', 'OMX Helsinki Technology GI', 'Nasdaq Singapore Technology Index', 'Nasdaq Malaysia Technology Index', 'Nasdaq US Small Cap Technology TR Index', 'Nasdaq India Technology Large Mid Cap Index', 'KBW Nasdaq Financial Technology Index', 'CRSP US Technology TR Index', 'Nasdaq Thailand Technology TR Index', 'Nasdaq Asia Technology Large Mid Cap Index', 'Nasdaq Small Cap Production Technology Equipment Index', 'Nasdaq US Benchmark Technology Hardware and Equipment TR Index', 'Nasdaq CTA Latin American Technology Innovators Net Total Return Index', 'Strategic Technology & Ecommerce Real Estate CAD Index', 'Nasdaq India Technology Index', 'Nasdaq US Large Cap Technology Hardware and Equipment Index', 'Nasdaq Germany Technology TR Index', 'Nasdaq BRIC Technology TR Index', 'NASDAQ-100 Technology Sector Market-Cap Weighted Index', 'Dow Jones U.S. Technology Total Stock Market Index', 'Nasdaq Mid Cap Production Technology Equipment TR Index', 'Nasdaq EMEA Technology TR Index', 'Nasdaq DM ASPA Technology Large Mid Cap NTR Index', 'Technology Select Sector Settlement Index', 'Dow Jones Americas Technology Index', 'Dow Jones Technology Titans 30 Index', 'Nasdaq Emerging Markets Technology TR Index', 'Nasdaq India Technology TR Index', 'Nasdaq Emerging Markets Technology Large Mid Cap TR Index', 'Strategic Technology & Ecommerce Real Estate Index', 'Nasdaq Global Technology NTR Index', 'Nasdaq N America Technology Large Mid Cap TR Index', 'Nasdaq Developed Markets Technology NTR Index', 'Nasdaq China Technology TR Index', 'Nasdaq North America Technology Index', 'NASDAQ-100 Technology Sector Total Return', 'Nasdaq Switzerland Technology Index', 'Nasdaq Taiwan Technology Large Mid Cap NTR Index', 'Nasdaq Norway Technology NTR Index', 'Nasdaq Eurozone Technology NTR Index', 'NASDAQ-100 Technology Sector', 'Nasdaq North America Technology NTR Index', 'Dow Jones U.S. Technology Capped Index (USD)', 'Nasdaq Singapore Technology NTR Index', 'Nasdaq Thailand Technology Index', 'Nasdaq EM Asia Technology Large Mid Cap NTR Index', 'Nasdaq France Technology TR Index', 'Strategic Technology & Ecommerce Real Estate Net Total Return JPY Index', 'NASDAQ-100 Technology Sector Synthetic Dividend 2%', 'Nasdaq US Mid Cap Technology TR Index', 'Nasdaq US Technology Large Mid Cap Index', 'OMX Copenhagen Technology Hardware and Equipment PI', 'N Technology EUR GI', 'Nasdaq Germany Technology Large Mid Cap Index', 'NASDAQ DM Ex US Technology NTR Index', 'Dow Jones U.S. Large-Cap Technology Index', 'Nasdaq ASPA Technology Large Mid Cap Index', 'Nasdaq DM Asia Technology Large Mid Cap TR Index', 'CRSP US Technology Index', 'Nasdaq CTA Latin American Technology Innovators Total Return BRL Index', 'Nasdaq EMEA Technology NTR Index', 'Nasdaq DM Europe Technology Large Mid Cap Index', 'Nasdaq DM ASPA Technology Large Mid Cap TR Index', 'Nasdaq EM Asia Technology Large Mid Cap Index', 'NASDAQ DM Ex US Technology TR Index', 'Nasdaq India Technology Large Mid Cap TR Index', 'OMX Helsinki Technology Hardware and Equipment PI', 'Nasdaq Asia Technology Large Mid Cap TR Index', 'Nasdaq Eurozone Technology Large Mid Cap NTR Index', 'Nasdaq DM Europe Technology Large Mid Cap TR Index', 'Nasdaq Global Technology Large Mid Cap TR Index', 'Nasdaq Korea Technology Large Mid Cap TR Index', 'Nasdaq DM MEA Technology Index', 'Nasdaq Asia Technology TR Index', 'Nasdaq Singapore Technology TR Index', 'Nasdaq United Kingdom Technology NTR Index', 'Nasdaq Eurozone Technology Large Mid Cap TR Index', 'OMX Baltic Technology GI', 'Nasdaq Taiwan Technology Index', 'Dow Jones Technology Titans 30 Index (EUR)', 'Nasdaq Global Technology Index', 'Nasdaq US Mid Cap Technology NTR Index', 'Nasdaq Japan Technology NTR Index', 'NASDAQ OMX China Technology Net Total Return', 'Nasdaq US Mid Cap Technology Index', 'Nasdaq Australia Technology TR Index', 'Nasdaq DM ASPA Technology NTR Index', 'Nasdaq CTA Latin American Technology Innovators BRL Index', 
                    'Nasdaq US Production Technology Equipment Large Mid Cap Index', 'Nasdaq US Small Cap Technology NTR Index', 'OMX Stockholm Technology Hardware and Equipment GI', 'Strategic Technology & Ecommerce Real Estate GBP Index', 'Nasdaq BRIC Technology Large Mid Cap Index', 'Nasdaq CTA Latin American Technology Innovators Net Total Return BRL Index', 'Nasdaq US Technology Large Mid Cap TR Index', 'Nasdaq Korea Technology Index', 'NASDAQ Technology Dividend Index', 'Nasdaq Norway Technology TR Index', 'Nasdaq US Mid Cap Technology Hardware and Equipment TR Index', 'Nasdaq US Large Cap Technology NTR Index', 'Nasdaq Australia Technology Index', 'Strategic Technology & Ecommerce Real Estate JPY Index', 'OMX Baltic Technology PI', 'Nasdaq Taiwan Technology Large Mid Cap Index', 'Nasdaq ASPA Technology NTR Index', 'Nasdaq Developed Markets Technology Large Mid Cap Index', 'Nasdaq US Production Technology Equipment Large Mid Cap NTR Index', 'Nasdaq DM MEA Technology NTR Index', 'Nasdaq Eurozone Technology TR Index', 'Strategic Technology & Ecommerce Real Estate EUR Index', 'Nasdaq South Africa Technology Index', 'Nasdaq DM Europe Technology Large Mid Cap NTR Index', 'OMX Helsinki Technology PI', 'Strategic Technology & Ecommerce Real Estate Total Return CAD Index', 'Nasdaq Netherlands Technology NTR Index', 'Nasdaq EM Asia Technology NTR Index', 'Nasdaq EMEA Technology Index', 'Nasdaq India Technology Large Mid Cap NTR Index', 'Nasdaq DM ASPA Technology Index', 'Nasdaq US Benchmark Technology TR Index', 'KBW Nasdaq Financial Technology NNR 70 Index', 'Nasdaq US Large Cap Technology Hardware and Equipment NTR Index', 'Nasdaq Netherlands Technology Large Mid Cap Index', 'Nasdaq ASPA Technology Large Mid Cap NTR Index', 'Nasdaq US Benchmark Production Technology Equipment NTR Index', 'NASDAQ DM Ex US Technology Index', 'Nasdaq DM Asia Technology NTR Index', 'Nasdaq Emerging Markets Technology Large Mid Cap NTR Index', 'Technology Select Sector Index', 'Strategic Technology & Ecommerce Real Estate Net Total Return Index', 'Strategic Technology & Ecommerce Real Estate Net Total Return AUD Index', 'Nasdaq Developed Markets Technology Large Mid Cap NTR Index', 'OMX Iceland Technology PI', 'Nasdaq Canada Technology Index', 'Nasdaq United Kingdom Technology Large Mid Cap NTR Index', 'Nasdaq US Small Cap Technology Index', 'Nasdaq United Kingdom Technology Index', 'Nasdaq United Kingdom Technology Large Mid Cap Index', 'Nasdaq DM Europe Technology Index', 'Nasdaq France Technology NTR Index', 'Nasdaq US Benchmark Technology Hardware and Equipment NTR Index', 'Nasdaq Canada Technology Large Mid Cap NTR Index', 'Dow Jones Europe ex-U.K. Technology Index', 'Nasdaq DM ASPA Technology TR Index', 'Nasdaq DM MEA Technology TR Index', 'NASDAQ-100 Technology Sector Net Total Return', 'Nasdaq Developed Markets Technology TR Index', 'NASDAQ-100 Technology Sector Market-Cap Weighted Notional Net Total Return Index', 'Nasdaq Eurozone Technology Large Mid Cap Index', 'Nasdaq BRIC Technology Large Mid Cap NTR Index', 'Nasdaq Switzerland Technology NTR Index', 'Nasdaq Israel Technology TR Index', 'Nasdaq Korea Technology Large Mid Cap NTR Index', 'Nasdaq EM MEA Technology NTR Index', 'Nasdaq BRIC Technology Index', 'Dorsey Wright Technology Tech Leaders TR', 'Nasdaq Germany Technology Large Mid Cap TR Index', 'Nasdaq Norway Technology Index', 'Nasdaq DM ASPA Technology Large Mid Cap Index', 'Nasdaq Europe Technology TR Index', 'Nasdaq Developed Markets Technology Large Mid Cap TR Index', 'Nasdaq Malaysia Technology TR Index', 
                    'Nasdaq Asia Technology Index', 'Nasdaq Australia Technology NTR Index', 'Nasdaq Korea Technology NTR Index', 'Nasdaq South Africa Technology NTR Index', 'Nasdaq Netherlands Technology Large Mid Cap TR Index', 'Nasdaq Japan Technology Large Mid Cap Index', 'Nasdaq US Technology Hardware and Equipment Large Mid Cap NTR Index', 'Nasdaq Germany Technology NTR Index', 'Nasdaq India Technology NTR Index', 'N Technology EUR PI', 'Nasdaq Europe Technology NTR Index', 'Strategic Technology & Ecommerce Real Estate Total Return Index', 'Nasdaq Taiwan Technology TR Index', 'Nasdaq Canada Technology Large Mid Cap Index', 'Nasdaq CTA Latin American Technology Innovators Total Return Index', 'OMX Stockholm Technology PI', 'Nasdaq EMEA Technology Large Mid Cap NTR Index', 'Nasdaq Emerging Markets Technology Index', 'Nasdaq US Small Cap Technology Hardware and Equipment Index', 'Nasdaq US Small Cap Technology Hardware and Equipment TR Index', 'Nasdaq CTA Latin American Technology Innovators Index', 'Nasdaq EM Asia Technology Large Mid Cap TR Index', 'Strategic Technology & Ecommerce Real Estate Net Total Return EUR Index', 'Nasdaq Israel Technology Index', 'Nasdaq Eurozone Technology Index', 'Nasdaq Taiwan Technology Large Mid Cap TR Index', 'Nasdaq Europe Technology Index', 'Nasdaq Small Cap Production Technology Equipment NTR Index', 'Nasdaq Germany Technology Index', 'First North Technology PI', 'OMX Copenhagen Technology PI', 'Nasdaq US Technology Hardware and Equipment Large Mid Cap TR Index', 'Nasdaq US Technology Hardware and Equipment Large Mid Cap Index', 'NASDAQ OMX China Technology Total Return', 'Nasdaq China Technology NTR Index', 'Nasdaq US Technology Large Mid Cap NTR Index', 'Nasdaq Europe Technology Large Mid Cap NTR Index', 'Nasdaq Europe Technology Large Mid Cap TR Index', 'Nasdaq China Technology Large Mid Cap NTR Index', 'Nasdaq EM MEA Technology TR Index', 'Nasdaq N America Technology Large Mid Cap NTR Index', 'Nasdaq Global Technology TR Index', 'Dow Jones Global ex-U.S. Technology Index', 'Nasdaq BRIC Technology Large Mid Cap TR Index', 'Nasdaq EM MEA Technology Index', 'Nasdaq France Technology Index', 'Nasdaq Asia Technology Large Mid Cap NTR Index', 'Nasdaq DM Asia Technology Large Mid Cap NTR Index', 'Strategic Technology & Ecommerce Real Estate Total Return JPY Index', 'Nasdaq US Benchmark Technology Hardware and Equipment Index', 'Nasdaq Emerging Markets Technology NTR Index', 'Nasdaq North America Technology TR Index', 'Nasdaq US Benchmark Production Technology Equipment TR Index', 'Nasdaq Thailand Technology NTR Index', 'Nasdaq United Kingdom Technology Large Mid Cap TR Index']


##crypto exchanges
KRAKEN=""
COINBASE=""
BITFINEX=""
BITSTAMP=""

exchange_webhooks ={
    'NYSE Arca, Inc.': NYSE_ARCA,
    'NYSE American, LLC': NYSE_AMERICAN,
    'New York Stock Exchange': NYSE,
    'Cboe BZX': CBOE_BZX,
    'Cboe EDGX': CBOE_EDGX,
    'Members Exchange': MEMX,
    'Investors Exchange': IEX,
    'Nasdaq': NASDAQ,
    'FINRA Alternative Display Facility': FINRA_ADF,

}





#condition webhook dict
condition_webhooks ={
    'Odd Lot Trade': ODD_LOT,
    'Form T': FORM_T,
    'Intermarket Sweep Order': INTERMARKET_SWEEPS,
    'Market Center Official Close': OFFICIAL_CLOSE,
    'Corrected Consolidated Close (per listing market)': CORRECTED_CLOSE,
    'Trade Thru Exempt': TRADE_THRU_EXEMPT,
    'SSR In Effect': SSR,

}

technicals_webhooks ={
    'OVERBOUGHT_1MIN':"",
    'OVERSOLD_1MIN':"",
    'OVERBOUGHT_1HOUR':"",
    'OVERSOLD_1HOUR':"",
    'OVERBOUGHT_DAY':"",
    'OVERSOLD_DAY':"",
    'OVERBOUGHT_WEEK':"",
    'OVERSOLD_WEEK':"",
    'SUPER_OVERBOUGHT':"",
    'SUPER_OVERSOLD': ""
}
#technicals
OVERBOUGHT_1MIN=""
OVERSOLD_1MIN=""
OVERBOUGHT_1HOUR ="" 
OVERSOLD_1HOUR ="" 
OVERBOUGHT_DAY ="" 
OVERSOLD_DAY ="" 
OVERBOUGHT_WEEK=""
OVERSOLD_WEEK=""
SUPER_OVERBOUGHT=""
SUPER_OVERSOLD=""


VWAP_DIFFERENTIAL=""
upside_scalps=""
downside_scalps=""
downside_day=""
upside_day=""
nobody_profit=""
everyone_profit ="" 
bullish_crossover=""
bearish_crossover ="" 
consumer_cyclical_hook=""

number_one=""


#STOCK CONDITIONS
CLOSING_PRINTS=""
ODD_LOT=""
SSR=""
INTERMARKET_SWEEPS=""
DERIVATIVELY=""
OPENING_PRINTS=""
NEXT_DAY=""
SLOW_ASK=""
CORRECTED_CLOSE=""
DEFICIENT=""
PRIOR_REFERENCE=""
CROSS_TRADE=""
OPENING_TRADE=""
OFFICIAL_CLOSE=""
RETAIL_INTEREST_BID=""
RETAIL_INTEREST_ASK=""
RETAIL_INTEREST_BID_AND_ASK=""
ORDER_INFLUX=""
REDEMPTION_SUSPENSION=""
SIP_GENERATED_FLAG ="" 
TRADE_THRU_EXEMPT=""
FORM_T=""

UNUSUAL_OPTIONS ="" 

option_sweeps=""
single_auction_non_iso=""
multileg_floor_trade=""
multileg_auction=""
multileg_auto=""
multi_vs_single=""
multiauto_vs_single=""
options_floor_trade=""
multi_cross=""
options_auto_trade=""
options_cross=""