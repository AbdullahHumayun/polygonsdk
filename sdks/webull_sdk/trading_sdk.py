
import requests
from .webull_data import WebullStockData
import uuid
from webull_sdk.webull_sdk import AsyncWebullSDK
from cfg import webull_headers


access_tokens = { 
    "chuck": "dc_us_tech1.187afbd327c-2a29abe790af4fe5ad551282ca57deda",
    "cthehentz": "",
    "nikopotamus": "dc_us_tech1.187b4f6e6eb-5689996eba3b4c619ede69967d376c9b",
    "jdpartyhat": "dc_us_tech1.187bc5eaa24-0ff93b6087b44acd9888ae2358431c52",
    "captzilla": "dc_us_tech1.187bf310cc0-02ecc978670645cfb4d142d55a38ecfd",
    "ray": "dc_us_tech1.18731114684-37ee12ba60764adc8c6b7451652f58bb",
    "shane": "dc_us_tech1.187bb292115-4c6faf480ffc4a29901078740b6e837f",
    "wheresmoney": "",
    "cadoewen":"dc_us_tech1.187bb1edd0d-0d270c08c40a49a2a00dff424df5422b",


    

}

account_ids = { 
    "chuck": "11113932",
    "cthehentz": "11094459",
    "nikopotamus": "11113638",
    "jdpartyhat": "11113642",
    "captzilla": "11081884",
    "ray": "11113634",
    "shane": "11014218",
    "wheresmoney": "",
    "cadoewen":"11113963"
}

webull_headers = { 
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0', 'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.5', 'Content-Type': 'application/json', 'platform': 'web', 'hl': 'en', 'os': 'web', 'osv': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0', 'app': 'global', 'appid': 'webull-webapp', 'ver': '3.39.18', 'lzone': 'dc_core_r001', 'ph': 'MacOS Firefox', 'locale': 'eng', 'device-type': 'Web', 'access_token': f'{access_tokens}',
}



class TradingWebullSDK:

    def __init__(self, username=None, tickerId=None):
        self.tickerId = tickerId
        self.base_url = "https://quotes-gw.webullfintech.com/api/"
        self.base_trading_url = "https://act.webullfintech.com/webull-paper-center/api/paper/1/acc/"
        self.access_token = access_tokens.get(username)
        self.account_id = account_ids.get(username)
        self.username = username
        self.webull_headers = { 
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0', 
            'Accept': '*/*', 
            'Accept-Encoding': 'gzip, deflate', 
            'Accept-Language': 'en-US,en;q=0.5', 
            'Content-Type': 'application/json', 
            'platform': 'web', 
            'hl': 'en', 
            'os': 'web', 
            'osv': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:99.0) Gecko/20100101 Firefox/99.0', 
            'app': 'global', 
            'appid': 'webull-webapp', 
            'ver': '3.39.18', 
            'lzone': 'dc_core_r001', 
            'ph': 'MacOS Firefox', 
            'locale': 'eng', 
            'device-type': 'Web', 
            'access_token': self.access_token,
        }

    def fetch_ticker_id(self, keyword):
        url = f"{self.base_url}search/pc/tickers?keyword={keyword}&regionId=6&pageIndex=1&pageSize=1"
        r = requests.get(url).json()
        data = r.get('data', None)
        if data is not None:
            try:
                self.tickerId = data[0]['tickerId']
                self.symbol = data[0]['symbol']
            except IndexError:
                pass
        else:
            pass
        return self.tickerId, self.symbol
    def reset(self, username):
        account_id = account_ids.get(username)
        access_token = access_tokens.get(username)

        if not account_id or not access_token:
            raise ValueError(f"Invalid username: {username}")

        webull_headers["access_token"] = access_token

        url = f"https://act.webullfintech.com/webull-paper-center/api/paper/1/acc/reset/{account_id}/10000000"
        r = requests.post(url, headers=webull_headers).json()
        return r
    
    def get_account_info(self):
        webull_headers["access_token"] = access_tokens
        account_info = requests.post(f"https://act.webullfintech.com/webull-paper-center/api/paper/1/acc/{self.account_id}", headers=self.webull_headers).json()
        self.total_pl = account_info['totalProfitLoss']
        self.total_pl_rate = account_info['totalProfitLossRate']
        self.base_url = account_info['actBaseUrl']
        self.act_id = account_info['accountId']
        self.account_value = account_info['netLiquidation']
        self.account_stats = account_info['accountMembers']
        self.positions = account_info['positions']
    def place_order(self, username, keyword, quantity, price, order_type):
        ticker_id, _ = self.fetch_ticker_id(keyword)
        if not ticker_id:
            raise ValueError(f"Invalid keyword: {keyword}")

        account_id = account_ids.get(username)
        access_token = access_tokens.get(username)

        if not account_id or not access_token:
            raise ValueError(f"Invalid username: {username}")

        webull_headers["access_token"] = access_token

        data = {
            'action': "BUY" if quantity > 0 else "SELL",
            'comboType': 'NORMAL',
            'orderType': order_type,
            'outsideRegularTradingHour': True,
            'quantity': abs(quantity),
            'lmtPrice': price,
            'serialId': str(uuid.uuid4()),
            'tickerId': ticker_id,
            'timeInForce': "GTC"
        }

        r = requests.post(f"{self.base_trading_url}{account_id}/orderop/place/{ticker_id}", json=data, headers=webull_headers).json()
        return r
    def take_profit_cut_losses(self):
        r2 = requests.get(f"https://act.webullfintech.com/webull-paper-center/api/paper/1/acc/{account_ids}", headers=webull_headers).json()
        print(r2)
        # (The rest of the code remains the same)
        accountId = r2['accountId']
        currency = r2['currency']
        currencyId = r2['currencyId']
        netLiquidation = r2['netLiquidation']
        accountMembers = r2['accountMembers']
        accounts = r2['accounts']
        openOrders = r2['openOrders']

        positions = r2['positions']
        totalProfitLoss = r2['totalProfitLoss']
        totalProfitLossRate = r2['totalProfitLossRate']
        actBaseUrl = r2['actBaseUrl']


        id = [i.get('id') for i in positions]
        accountId = [i.get('accountId') for i in positions]
        paperId = [i.get('paperId') for i in positions]
        ticker = [i.get('ticker') for i in positions]
        status = [i.get('status') for i in positions]
        position = [i.get('position') for i in positions]
        cost = [i.get('cost') for i in positions]
        costPrice = [i.get('costPrice') for i in positions]
        lastPrice = [i.get('lastPrice') for i in positions]
        marketValue = [i.get('marketValue') for i in positions]
        unrealizedProfitLoss = [i.get('unrealizedProfitLoss') for i in positions]
        unrealizedProfitLossRate = [i.get('unrealizedProfitLossRate') for i in positions]
        tickerType = [i.get('tickerType') for i in positions]
        optionType = [i.get('optionType') for i in positions]
        optionExpireDate = [i.get('optionExpireDate') for i in positions]
        optionContractMultiplier = [i.get('optionContractMultiplier') for i in positions]
        optionExercisePrice = [i.get('optionExercisePrice') for i in positions]
        belongTickerId = [i.get('belongTickerId') for i in positions]

        dissymbol = [i.get('disSymbol') for i in ticker]
        symbol = [i.get('symbol') for i in ticker]

        positions = [pos for pos in positions if len(pos['ticker']['symbol']) <= 5]
        return positions

    
    def get_webull_stock_data(self, ticker):


        # Check if the ticker WebullStockData is available in the cache

        # If the ticker WebullStockData is not in the cache or has expired, fetch it
        webull_stock_data = WebullStockData(ticker)
        # Store the fetched WebullStockData in the cache


        return webull_stock_data
    
    def get_price(self, ticker):
        if ticker is not None:
            r = requests.get(f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=1&tickerId={ticker}&includeSecu=1&delay=0&more=1").json()
            data = r['data']
            price = data[0]['price']
            return price
        else:
            print(f"No Ticker")

