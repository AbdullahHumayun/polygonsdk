# import disnake

# import requests


# from utils.webull_tickers import ticker_list
# import re
# from .citedoptions import RepoCitedDrop,RepoCitedDrop2,RepoCitedViewStart
# from selenium import webdriver
# from views.learnviews import OFRViewStart
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from views.learnviews import DataMenu
# from markets import LosersViewStart,GainersViewStart,ActiveViewStart,HighShortsViewStart,LowFloatDropdown,ForexViewStart,ETFsViewStart,FTDViewStart
# import stocksera
# from cfg import YOUR_STOCKSERA_KEY
# from tooloptions import DTCCViewStart,NYSEViewStart,CBOEViewStart
# from commandoptions import WebullCmdViewStart,StreamCmdViewStart,LearnCmdViewStart,DDCmdViewStart,OptionCmdViewStart,EconomyCmdViewStart,EarningsCmdViewStart,ChartingCmdViewStart,StockCmdViewStart,FlowCmdViewStart,DPSCmdViewStart
# from _discord.views.menus import AlertMenus
# from views.learnviews import FUDSTOPMenu
# from views.learnviews import TotalOIViewStart,TotalTurnoverViewStart,TotalVolumeViewStart,TopIVViewStart,TopOIDownViewStart,TopOIUpViewStart,TopOIViewStart,TopVolumeViewStart
# from views.learnviews import TechDropdown,TechDropdown2
# from app.app import RepoCitedDrop,RepoCitedDrop2,RepoCitedViewStart,RepoDataStart
# from citedoptions import RepoCitedViewStart
# from views.learnviews  import FedDataStart,FINRADataStart,InflationDataStart,MMFDataStart,RepoDataStart,HKEXDataStart,TreasuryDataStart,EconomicDataStart,BlockchainDataStart
# from app.fudstop import BotCmdMenu
# client = stocksera.Client(api_key=YOUR_STOCKSERA_KEY)
# from requests.exceptions import HTTPError
# from app.app import RepoDataStart, FedDataStart, TreasuryDataStart, HKEXDataStart,FINRADataStart,InflationDataStart
# from dataembeds import EconomicEmbed,FINRADataEmbed,BTCDataEmbed,FedDataEmbed,HKEXDataEmbed,MMFDataEmbed,InflationDataEmbed,TreasuryDataEmbed,RepoDataEmbed
# import csv

# from typing import List
# from datetime import datetime
# from urllib.parse import urlencode

# from datetime import datetime
# import requests
# from urllib.parse import urlencode
# class OptionSnapshotData:
#     class DayData:
#         def __init__(self, day_data):
#             self.close = day_data.get("close")
#             self.high = day_data.get("high")
#             self.last_updated = day_data.get("last_updated")
#             self.low = day_data.get("low")
#             self.open = day_data.get("open")
#             self.previous_close = day_data.get("previous_close")
#             self.volume = day_data.get("volume")
#             self.vwap = day_data.get("vwap")

#     class DetailsData:
#         def __init__(self, details_data):
#             self.contract_type = details_data.get("contract_type")
#             self.exercise_style = details_data.get("exercise_style")
#             self.expiration_date = details_data.get("expiration_date")
#             self.shares_per_contract = details_data.get("shares_per_contract")
#             self.strike_price = details_data.get("strike_price")
#             self.ticker = details_data.get("ticker")

#     class GreeksData:
#         def __init__(self, greeks_data):
#             self.delta = greeks_data.get("delta")
#             self.gamma = greeks_data.get("gamma")
#             self.theta = greeks_data.get("theta")
#             self.vega = greeks_data.get("vega")
#             self.implied_volatility = greeks_data.get("implied_volatility")

#     class LastQuoteData:
#         def __init__(self, last_quote_data):
#             self.ask = last_quote_data.get("ask")
#             self.ask_size = last_quote_data.get("ask_size")
#             self.bid = last_quote_data.get("bid")
#             self.bid_size = last_quote_data.get("bid_size")
#             self.last_updated = last_quote_data.get("last_updated")
#             self.midpoint = last_quote_data.get("midpoint")
#             self.timeframe = last_quote_data.get("timeframe")

#     class LastTradeData:
#         def __init__(self, last_trade_data):
#             self.conditions = last_trade_data.get("conditions")
#             self.exchange = last_trade_data.get("exchange")
#             self.price = last_trade_data.get("price")
#             self.sip_timestamp = last_trade_data.get("sip_timestamp")
#             self.size = last_trade_data.get("size")
#             self.timeframe = last_trade_data.get("timeframe")

#     class UnderlyingAssetData:
#         def __init__(self, underlying_asset_data):
#             self.change_to_break_even = underlying_asset_data.get("change_to_break_even")
#             self.last_updated = underlying_asset_data.get("last_updated")
#             self.price = underlying_asset_data.get("price")
#             self.ticker = underlying_asset_data.get("ticker")
#             self.timeframe = underlying_asset_data.get("timeframe")

#     def __init__(self, data):
#         self.break_even_price = data.get("break_even_price")
#         self.change = data.get("change")
#         self.change_percent = data.get("change_percent")
#         self.day = OptionSnapshotData.DayData(data.get("day", {}))
#         self.details = OptionSnapshotData.DetailsData(data.get("details", {}))
#         self.greeks = OptionSnapshotData.GreeksData(data.get("greeks", {}))
#         self.last_quote = OptionSnapshotData.LastQuoteData(data.get("last_quote", {}))
#         self.last_trade = OptionSnapshotData.LastTradeData(data.get("last_trade", {}))
#         self.open_interest = data.get("open_interest")
#         self.implied_volatility = data.get("implied_volatility")
#         self.underlying_asset = OptionSnapshotData.UnderlyingAssetData(data.get("underlying_asset", {}))
# class OptionTrade:
#     def __init__(self, trade_data, conditions_map):
#         self.exchange = trade_data.get("exchange")
#         self.participant_timestamp = trade_data.get("participant_timestamp")
#         self.price = trade_data.get("price")
#         self.sip_timestamp = trade_data.get("sip_timestamp")
#         self.size = trade_data.get("size")
#         self.conditions = [conditions_map.get(cond) for cond in trade_data.get("conditions", [])]

#     def __str__(self):
#         return f"Trade(price={self.price}, size={self.size}, timestamp={self.sip_timestamp}, conditions={self.conditions})"

#     def __repr__(self):
#         return self.__str__()
# class OptionAggs:
#     def __init__(self, bar_data):
#         self.open = bar_data.get("o")
#         self.high = bar_data.get("h")
#         self.low = bar_data.get("l")
#         self.close = bar_data.get("c")
#         self.volume = bar_data.get("v")
#         self.vw = bar_data.get("vw")
#         self.number_of_trades = bar_data.get("n")
#         self.timestamp = self._convert_timestamp(bar_data.get("t"))

#     @staticmethod
#     def _convert_timestamp(timestamp):
#         dt = datetime.fromtimestamp(timestamp // 1000)
#         return dt.strftime('%Y/%m/%d:%I:%M %p')

#     def __str__(self):
#         return f"OptionAggs(timestamp={self.timestamp}, open={self.open}, high={self.high}, low={self.low}, close={self.close}, volume={self.volume})"

#     def __repr__(self):
#         return self.__str__()
# class PolygonOptionsSDK:
#     """
#     A Python SDK for interacting with the Polygon.io Stock Options API.
    
#     Usage:
#     polygon_options_sdk = PolygonOptionsSDK(api_key="<your_api_key>")
#     """

#     def __init__(self, api_key):
#         """
#         Initialize the PolygonOptionsSDK with your API key.
        
#         :param api_key: Your Polygon.io API key as a string.
#         """
#         self.api_key = api_key
#         self.base_url = "https://api.polygon.io"
#         self.exchanges_map = {}  # Add this line to define the exchanges_map attribute
#         self.session = requests.Session()

#     def _request(self, endpoint, params=None):
#         if params is None:
#             params = {}
#         params["apiKey"] = self.api_key
#         url = f"{self.base_url}{endpoint}"
#         try:
#             response = requests.get(url, params=params)
#             response.raise_for_status()
#         except HTTPError as http_err:
#             print(f"An HTTP error occurred: {http_err}")
#             return None
#         except Exception as err:
#             print(f"An error occurred: {err}")
#             return None

#         try:
#             return response.json()
#         except Exception as err:
#             print(f"Error decoding JSON response: {err}")
#             return None
        

#     def get_option_conditions(self):
#         """
#         Get stock conditions data from the Polygon.io API.
        
#         :return: A dictionary with condition IDs as keys and condition names as values.
#         """
#         url = f"https://api.polygon.io/v3/reference/conditions?asset_class=options&limit=1000&apiKey={self.api_key}"
#         response = requests.get(url)
#         stock_conditions = {}

#         if response.status_code == 200:
#             data = response.json()
#             conditions_data = data['results']

#             for condition in conditions_data:
#                 condition_id = condition['id']
#                 condition_name = condition['name']
#                 stock_conditions[condition_id] = condition_name
#         else:
#             print(f"Error: {response.status_code}")

#         return stock_conditions


#     def get_exchanges(self, asset_class=None, locale=None):
#         endpoint = "/v3/reference/exchanges"
#         params = {}

#         if asset_class:
#             params["asset_class"] = asset_class
#         if locale:
#             params["locale"] = locale

#         exchanges_data = self._request(endpoint, params=params)

#         return exchanges_data

#     def generate_option_symbol(self, underlying_symbol, expiration_date, option_type, strike_price):
#         """
#         Generate an option symbol for a given underlying symbol, expiration date, option type, and strike price.

#         :param underlying_symbol: The symbol of the underlying stock or ETF.
#         :param expiration_date: The expiration date of the option in the format 'YYYY-MM-DD'.
#         :param option_type: The option type, 'C' for call or 'P' for put.
#         :param strike_price: The strike price of the option as an integer.
#         :return: The generated option symbol as a string.
#         """
#         # Convert the expiration date to the format 'YYMMDD'
#         expiration_date_obj = datetime.strptime(expiration_date, "%Y-%m-%d")
#         expiration_date_formatted = expiration_date_obj.strftime("%y%m%d")

#         # Convert the strike price to the required format
#         formatted_strike = f"{strike_price:05}000"

#         return f"O:{underlying_symbol}{expiration_date_formatted}{option_type}{formatted_strike}"

#     def _request_all_pages(self, initial_url, params=None, data_parser=None):
#         if params is None:
#             params = {}
#         params["apiKey"] = self.api_key

#         all_results = []
#         next_url = initial_url

#         while next_url:
#             try:
#                 response = requests.get(next_url, params=params)
#                 response.raise_for_status()
#                 data = response.json()

#                 if "results" in data:
#                     results = data["results"]
#                     if data_parser:
#                         results = [data_parser(item) for item in results]
#                     all_results.extend(results)

#                 next_url = data.get("next_url")
#                 if next_url:
#                     # Append the API key to the next_url
#                     next_url += f'&{urlencode({"apiKey": self.api_key})}'
#                     params = {}  # Clear params for next_url since it contains the required params

#             except HTTPError as http_err:
#                 print(f"An HTTP error occurred: {http_err}")
#                 break
#             except Exception as err:
#                 print(f"An error occurred: {err}")
#                 break

#         return all_results



#     def get_aggregate_bars(self, options_ticker, multiplier, timespan, start_date, end_date, adjusted=True, sort="asc", limit=120) -> List[OptionAggs]:
#         """
#         Get aggregate bars for an option contract over a given date range in custom time window sizes.

#         :param options_ticker: The ticker symbol of the options contract.
#         :param multiplier: The size of the timespan multiplier.
#         :param timespan: The size of the time window.
#         :param start_date: The start of the aggregate time window. Either a date with the format YYYY-MM-DD or a millisecond timestamp.
#         :param end_date: The end of the aggregate time window. Either a date with the format YYYY-MM-DD or a millisecond timestamp.
#         :param adjusted: Whether or not the results are adjusted for splits. By default, results are adjusted.
#         :param sort: Sort the results by timestamp. "asc" will return results in ascending order (oldest at the top), "desc" will return results in descending order (newest at the top).
#         :param limit: Limits the number of base aggregates queried to create the aggregate results. Max 50000 and Default 5000.
#         :return: A JSON object containing the results.
#         """
#         endpoint = f"/v2/aggs/ticker/{options_ticker}/range/{multiplier}/{timespan}/{start_date}/{end_date}"
#         params = {
#             "adjusted": adjusted,
#             "sort": sort,
#             "limit": limit
#         }

#         initial_url = f"{self.base_url}{endpoint}"
#         all_bars = self._request_all_pages(initial_url, params)
#         return all_bars
        




#     def get_daily_open_close(self, options_ticker, date, adjusted=True):
#         """
#         Get the open, close, and after-hours prices of an options contract on a certain date.

#         :param options_ticker: The ticker symbol of the options contract.
#         :param date: The date of the requested open/close in the format YYYY-MM-DD.
#         :param adjusted: Whether or not the results are adjusted for splits. Default is True.
#         :return: A dictionary containing the response data.
#         """
#         endpoint = f"/v1/open-close/{options_ticker}/{date}"
#         params = {"adjusted": adjusted}
#         return self._request(endpoint, params)

#     def get_previous_close(self, options_ticker, adjusted=True):
#         """
#         Get the previous day's open, high, low, and close (OHLC) for the specified options contract.

#         :param options_ticker: The ticker symbol of the options contract.
#         :param adjusted: Whether or not the results are adjusted for splits. Default is True.
#         :return: A dictionary containing the response data.
#         """
#         endpoint = f"/v2/aggs/ticker/{options_ticker}/prev"
#         params = {"adjusted": adjusted}
#         return self._request(endpoint, params)
    


#     def get_trades(self, options_ticker, timestamp=None, order=None, limit=None, sort=None):
#         """
#         Get trades for an options ticker symbol in a given time range.

#         :param options_ticker: The options ticker symbol to get trades for.
#         :param timestamp: Query by trade timestamp. Either a date with the format YYYY-MM-DD or a nanosecond timestamp.
#         :param order: Order results based on the sort field.
#         :param limit: Limit the number of results returned, default is 10 and max is 50000.
#         :param sort: Sort field used for ordering.
#         :return: A list of Trade objects containing the response data.
#         """
#         endpoint = f"/v3/trades/{options_ticker}"
#         params = {}
#         if timestamp:
#             params["timestamp"] = timestamp
#         if order:
#             params["order"] = order
#         if limit:
#             params["limit"] = limit
#         if sort:
#             params["sort"] = sort

#         initial_url = f"{self.base_url}{endpoint}"
#         all_trades = self._request_all_pages(initial_url, params=params, data_parser=lambda trade_data: OptionTrade(trade_data, self.conditions_map))
#         return all_trades
          
#     def get_last_trade(self, options_ticker):
#         """
#         Get the most recent trade for a given options contract.

#         :param options_ticker: The ticker symbol of the options contract.
#         :return: A dictionary containing the response data.
#         """
#         endpoint = f"/v2/last/trade/{options_ticker}"
#         return self._request(endpoint)

#     def get_options_quotes(self, options_ticker, timestamp=None, order=None, limit=None, sort=None):
#         """
#         Get quotes for an options ticker symbol in a given time range.
        
#         :param api_key: str, API key to access Polygon.io API
#         :param options_ticker: str, The ticker symbol to get quotes for
#         :param timestamp: str, optional, Query by timestamp (date format YYYY-MM-DD or a nanosecond timestamp)
#         :param order: str, optional, Order results based on the sort field
#         :param limit: int, optional, Limit the number of results returned (default is 10, max is 50000)
#         :param sort: str, optional, Sort field used for ordering
#         :return: dict, JSON response containing quote data
#         """
#         endpoint = f"/v3/quotes/{options_ticker}"
#         params = {}
#         if timestamp:
#             params += f"&timestamp={timestamp}"
#         if order:
#             params += f"&order={order}"
#         if limit:
#             params += f"&limit={limit}"
#         if sort:
#             params += f"&sort={sort}"

#         return self._request(endpoint)
    

#     def get_option_contract_snapshot(self, underlying_asset, option_contract):
#         """
#         Get the snapshot of an option contract for a stock equity.

#         :param underlying_asset: The underlying ticker symbol of the option contract.
#         :param option_contract: The option contract identifier.
#         :return: A JSON object containing the option contract snapshot data.
#         """
#         endpoint = f"/v3/snapshot/options/{underlying_asset}/{option_contract}"
#         return self._request(endpoint)
    

#     def get_option_chain(self, underlying_asset, strike_price=None, expiration_date=None, contract_type=None, order=None, limit=10, sort=None):
#         """
#         Get the snapshot of all options contracts for an underlying ticker.

#         :param underlying_asset: The underlying ticker symbol of the option contract.
#         :param strike_price: Query by strike price of a contract.
#         :param expiration_date: Query by contract expiration with date format YYYY-MM-DD.
#         :param contract_type: Query by the type of contract.
#         :param order: Order results based on the sort field.
#         :param limit: Limit the number of results returned, default is 10 and max is 250.
#         :param sort: Sort field used for ordering.
#         :return: A JSON object containing the option chain data.
#         """
#         endpoint = f"/v3/snapshot/options/{underlying_asset}"
#         params = {
#             "strike_price": strike_price,
#             "expiration_date": expiration_date,
#             "contract_type": contract_type,
#             "order": order,
#             "limit": limit,
#             "sort": sort
#         }

#         # Remove parameters with None values
#         params = {k: v for k, v in params.items() if v is not None}
#         return self._request(endpoint)

#     def get_option_chain_all(self, underlying_asset, strike_price=None, expiration_date=None, contract_type=None, order=None, limit=250, sort=None) -> List[OptionSnapshotData]:
#         """
#         Get all options contracts for an underlying ticker across all pages.

#         :param underlying_asset: The underlying ticker symbol of the option contract.
#         :param strike_price: Query by strike price of a contract.
#         :param expiration_date: Query by contract expiration with date format YYYY-MM-DD.
#         :param contract_type: Query by the type of contract.
#         :param order: Order results based on the sort field.
#         :param limit: Limit the number of results returned, default is 10 and max is 250.
#         :param sort: Sort field used for ordering.
#         :return: A list containing all option chain data across all pages.
#         """
#         endpoint = f"{self.base_url}/v3/snapshot/options/{underlying_asset}"
#         params = {
#             "strike_price": strike_price,
#             "expiration_date": expiration_date,
#             "contract_type": contract_type,
#             "order": order,
#             "limit": limit,
#             "sort": sort,
#             "apiKey": self.api_key
#         }
#         response_data = self._request_all_pages(endpoint, params=params)
#         option_data = [OptionSnapshotData(data) for data in response_data]
#         return option_data


# class TechnicalEmbed(disnake.Embed):
#     def __init__(self):
#         super().__init__(title=f"{emojis.uptrend} Technical Signals {emojis.uptrend}",
#         description="```py\nThis section of the app allows you to choose a technical indicator, and will display implications for the selected indicator, as well as a live example! Select the technical signals you want from the two drop-down menus below.```", color=disnake.Colour.dark_gold())

#         self.add_field(name="Return to Main", value=f"{emojis.downarrow}")
#         self.set_footer(text="Implemented by FUDstop.")

# from _discord import emojis

# class CommandsStart(disnake.ui.View):
#     def __init__(self):
        
#         super().__init__(timeout=None)

#         self.add_item(BotCmdMenu())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey,emoji=f"{emojis.bandaid}", custom_id="command1button1",row=0,disabled=True)#data
#     async def command1button1(self, button: disnake.ui.Button, inter: disnake.AppCmdInter, message=disnake.Message):
#         await inter.response.edit_message(LitStart(), embed=MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.webullcmd}", custom_id="command1button2",row=0,disabled=False)#webull
#     async def command1button2(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):



#         await inter.response.edit_message(view=WebullCmdViewStart(), embed=WebullCmdViewStart().embed)
        


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.clockspin}", custom_id="command1button3",row=0,disabled=False)#stream
#     async def command1button3(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=StreamCmdViewStart(), embed=CommandsEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.optioncmd}", custom_id="command1button4",row=0,disabled=False)#options
#     async def command1button4(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=OptionCmdViewStart(), embed=CommandsEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.toprightarrow}", custom_id="command1button5",row=0,disabled=False)#data
#     async def command1button5(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.portal}", custom_id="command1button6",row=1,disabled=False)#dp commands
#     async def command1button6(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        
#         await inter.response.edit_message(view=DPSCmdViewStart(), embed=CommandsEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="command1button7",row=1,disabled=True)
#     async def command1button7(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.pinkrocket}", custom_id="command1button8", disabled=False,row=1)#stockcmds
#     async def command1button8(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=StockCmdViewStart(), embed=CommandsEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="command1button9",row=1,disabled=True)
#     async def command1button9(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.learncmd}", custom_id="command1button10",row=1,disabled=False)
#     async def command1button10(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LearnCmdViewStart(), embed=CommandsEmbed())


    

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.glowstick}", custom_id="command1button16",row=3,disabled=False)#chart
#     async def command1button16(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=ChartingCmdViewStart(), embed=CommandsEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="command1button17",row=3,disabled=True)
#     async def command1button17(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.eye}", custom_id="command1button18",disabled=False,row=3)#DOWNARROW
#     async def downarrow(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=DDCmdViewStart(), embed=CommandsEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="command1button19",row=3,disabled=True)#data
#     async def command1button19(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.flowcmd}", custom_id="command1button20",row=3,disabled=False)#magicwand
#     async def command1button20(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=FlowCmdViewStart(), embed=CommandsEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="command1button21",row=4,disabled=True)#data
#     async def command1button21(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.earnings}", custom_id="command1button22",row=4,disabled=False)#pins
#     async def command1button22(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=EarningsCmdViewStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.economy}", custom_id="command1button23",row=4,disabled=False)#alert
#     async def command1button23(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=EconomyCmdViewStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.question}", custom_id="command1button24",row=4,disabled=True)#sectorrotation
#     async def command1button24(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="command1button25",row=4,disabled=True)#data
#     async def linkbutton25(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())


#     async def on_button_click(message: disnake.Message):

#         await message.add_reaction(emoji=emojis.balloons)

# class ToolsEmbed(disnake.Embed):
#     def __init__(self):
#         super().__init__(title=f"<a:_:1043679047617622078> Tools",description="```py\nIn this section you will find very useful information from links to applications, to helpful websites - to RSS feeds and SEC filings - as well as calculators and strategy optimizers. . and much```", color=disnake.Colour.dark_orange())


#         self.add_field(name=f"{emojis.dtcc}", value="```py\nDepository Trust Clearing Corporation```")
#         self.add_field(name=f"{emojis.sec}", value="```py\nSecurities and Exchange Commission```")
#         self.add_field(name=f"{emojis.finrawhite}", value="```py\nFINRA```")
#         self.add_field(name=f"{emojis.nyse}", value="```py\nThe New York Stock Exchange```")
#         self.add_field(name=f"{emojis.fed}", value="```py\nThe Federal Reserve Bank of the United States```")
#         self.add_field(name=f"<:_:1046522659736932403>", value="```py\nOptions Clearing Corporation```")
#         self.add_field(name=f"<:_:1046522227790716968>", value="```py\nCollege Board Options Exchange```", inline=False)
#         self.add_field(name=f"{emojis.cboe}", value="```py\nCollege Board Options Exchange```", inline=False)
#         self.add_field(name=f"{emojis.confirmed}", value="```py\nReturn to main.```",inline=False)




# class CoreDrop(disnake.ui.Select):
#     def __init__(self):
#         super().__init__(
#             placeholder="🇨 🇴 🇷 🇪  🇸 🇨 🇷 🇪 🇪 🇳 🇪 🇷 🇸",
#             min_values=1,
#             max_values=1,
#             custom_id="fuckyoulmfao",
#             options = [ 
#                 disnake.SelectOption(label="🇨  🇦  🇱  🇱 🇸", value=1, description="Scans for Earnings within 7 days, RSI over 70, Non-Healthcare - and price above $5.", emoji="<a:_:1044503960842670150>"),
#                 disnake.SelectOption(label="🇵 🇺 🇹 🇸",value=2,description="Scans for Earnings within 7 days, RSI over 70, Non-Healthcare - and price above $5.", emoji="<a:_:1044504251805745182>")
                
#             ]
#         )


#     async def callback(self, interaction: disnake.MessageCommandInteraction):
#         if self.values[0] == "1":
#             await interaction.send("```py\nlogin: fudstoptrading@charliesindex.com || password: ||fudstoppers#23||``` Updates daily around 7-8 PM CST. https://www.alphaquery.com/stock-screener/600010229?run=1", ephemeral=True)
#         elif self.values[0] =="2":
#             await interaction.send("```py\nlogin: fudstoptrading@charliesindex.com || password: ||fudstoppers#23||``` Updates daily around 7-8 PM CST. https://www.alphaquery.com/stock-screener/600010229?run=1", ephemeral=True)



# class MainEmbedAPP(disnake.Embed):
#     def __init__(self):
#         super().__init__(
#             title=f"{emojis.fudstop} FUDSTOP Application 2.0 Online",
#             description="```py\nThis is the FUDSTOP Application 2.0.``````py\nWithin this APP, you can click the buttons on the main page to get anything you need related to markets. From cited works to datasets, core play screener and bot-command help, as well as a server menu and YouTube videos - simply click what you need! Use the legend below to identify each category:```",
#             color=disnake.Colour.dark_orange()
#         )

#         self.add_field(name=f"{emojis.tradertools}", value=f"```py\nTrading Tools```",inline=True)
#         self.add_field(name=f"{emojis.book}", value=f"```py\nCited Works```",inline=True)
#         self.add_field(name=f"{emojis.confirmed}", value=f"```py\nServer Slash Commands```",inline=True)
        
#         self.add_field(name=f"{emojis.uptrend}", value=f"```py\nLive Technical Signals```",inline=True)
#         self.add_field(name=f"{emojis.worldwide}", value="```py\nFUDstop Server Menu```")
#         self.add_field(name=f"{emojis.links}",value="```py\nLinks```",inline=True)
#         self.add_field(name=f"{emojis.fudstop}", value="```py\nCore Logic```",inline=True)
#         self.add_field(name=f"{emojis.video}", value="```py\nVideos```", inline=True)
#         self.add_field(name=f"{emojis.alert}", value="```py\nTradyTics Play Alerts!```", inline=True)
#         self.add_field(name=f"{emojis.confirmed}", value="```py\nDiscord Help```", inline=True)
#         self.add_field(name=f"{emojis.question}", value="```py\nAPP Tutorial```", inline=True)
#         self.add_field(name=f"{emojis.purpleslash}", value="```py\nSp500 Live Data```", inline=True)
#         self.add_field(name=f"{emojis.confirmed}", value="```py\nFinished With an Area```", inline=True)
#         self.set_footer(text="NOTE - THIS DATA IS LIVE AND UPDATES EVERY TIME THE BUTTONS ARE CLICKED")
#         self.set_author(name="FUDstop Trading",icon_url="https://cdn.discordcom/icons/888488311927242753/a_2f3b77412430093a08a85639ce33045f.gif?size=40")


# class CoreEmbed(disnake.Embed):
#     def __init__(self):
#         super().__init__(
#             title=f"{emojis.fudstop} FUDSTOP Application 2.0 Online",
#             description="```py\nThis is the FUDSTOP Application 2.0.``````py\nWithin this APP, you can click the buttons on the main page to get anything you need related to markets. From cited works to datasets, core play screener and bot-command help, as well as a server menu and YouTube videos - simply click what you need! Use the legend below to identify each category:```",
#             color=disnake.Colour.dark_orange()
#         )

#         self.add_field(name=f"{emojis.confirmed}", value=f"```py\n To the main page.```",inline=True)
#         self.add_field(name="<a:_:1044504251805745182>", value=f"```py\nCheck Put Screener. Login information will be printed.```",inline=True)
#         self.add_field(name="<a:_:1044503960842670150>", value=f"```py\nCheck Call Screener. Login information will be printed.```",inline=True)
#         self.set_author(name="FUDstop Trading",icon_url="https://cdn.discordcom/icons/888488311927242753/a_2f3b77412430093a08a85639ce33045f.gif?size=40")
#         self.add_field(name="Legend:", value="```py\nCore Criteria:```<a:_:1043676146899877958> <a:_:1044765851506716673>  <a:_:1044765841192931388> <a:_:1044765824960974938> <a:_:1044766617810259988>")


# class LinksStartView(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)

    
#         self.select = disnake.ui.Select( 
#             placeholder =f"L I N K S",
#             min_values=1,
#             max_values=1,
#             custom_id="linksdrop",
#             options = [ 
#                 disnake.SelectOption(label=f"..",emoji=f"{emojis.links}"),
#                 disnake.SelectOption(label=f"...", emoji=f"{emojis.links}"),
#                 disnake.SelectOption(label=f"....",emoji=f"{emojis.links}"),
#                 disnake.SelectOption(label=f".....",emoji=f"{emojis.links}"),
#                 disnake.SelectOption(label=f"......",emoji=f"{emojis.links}"),
#                 disnake.SelectOption(label=f".......",emoji=f"{emojis.links}"),

#                 disnake.SelectOption(label=f"-",emoji=f"{emojis.links}"),
#                 disnake.SelectOption(label=f"--",emoji=f"{emojis.links}"),
#                 disnake.SelectOption(label=f"---",emoji=f"{emojis.links}"),
#                 disnake.SelectOption(label=f"----",emoji=f"{emojis.links}"),
#                 disnake.SelectOption(label=f"-----",emoji=f"{emojis.links}"),
#                 disnake.SelectOption(label=f"------",emoji=f"{emojis.links}"),
#                 disnake.SelectOption(label=f"-------",emoji=f"{emojis.links}"),
                

#             ]
#         )
#         self.embed = disnake.Embed(title=f"{emojis.links} Useful Links {emojis.links}", description=f"```py\nThis is your one stop shop for all of your market needs when it comes to URLs. Find links in here you've never heard of - or have been looking for.\n\nView the legend below for navigating the app:```", color=disnake.Colour.dark_purple())
#         self.add_item(self.select)
#         self.select.callback = lambda interaction: interaction.response.edit_message(view=LinksStartView(), embed = LinksStartView().embed)
#         self.embed = disnake.Embed(title=f"{emojis.links} Useful Links {emojis.links}", description=f"```py\nHere is a list of very useful links that can be used for a variety of different purposes. Whether its' to check futures, forex, crypto, markets - order flow, market volume, options volume, futures volume, technical indicators, options strategies, analysis tools, data visualization, and much much more - these links are reliable and trusted sources for your needed information.```", color=disnake.Colour.dark_orange())
#         self.embed.add_field(name=f"{emojis.pink1}", value=f"```py\nLegend:\n\n{emojis.pink1}``` ``Data Visualization``\n{emojis.pink2} ``Agency Filings and Important Info``\n{emojis.pink3} ``Calculators, tools, and resources.``\n{emojis.pink4} ``Courses / Market Knowledge.``\n{emojis.pink5} ``Cited Works and Critical Policy``")
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,emoji=f"{emojis.coolchart}", custom_id="links1button1",row=0,disabled=True)#data
#     async def links1button1(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LinksStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="links1button2",row=0,disabled=False)#tools
#     async def links1button2(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LinksStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.fail}", custom_id="links1button3",row=0,disabled=False)#check
#     async def links1button3(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(),embed=MarketsEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="links1button4",row=0,disabled=True)#citedworks
#     async def links1button4(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LinksStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="links1button5",row=0,disabled=True)#data
#     async def links1button5(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LinksStartView())




    

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="links1button16",disabled=False)
#     async def links1button16(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LinksStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="links1button17",disabled=True)
#     async def links1button17(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LinksStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="links1button18",disabled=True)#DOWNARROW
#     async def downarrow(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="links1button19",disabled=True)#data
#     async def links1button19(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LinksStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="links1button20",disabled=False)#magicwand
#     async def links1button20(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LinksStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji=f"{emojis.pink1}", custom_id="links1button21",disabled=True)#data
#     async def links1button21(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LinksStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji=f"{emojis.pink2}", custom_id="links1button22",disabled=False)#pins
#     async def links1button22(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LinksStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji=f"{emojis.pink3}", custom_id="links1button23",disabled=False)#alert
#     async def links1button23(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LinksStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji=f"{emojis.pink4}", custom_id="links1button24",disabled=False)#sectorrotation
#     async def links1button24(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LinksStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji=f"{emojis.pink5}", custom_id="links1button25",disabled=True)#data
#     async def linkbutton25(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LinksStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.ll}", custom_id="links12button21",disabled=True)#data
#     async def links1button221(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LinksStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.li}", custom_id="links12button22",disabled=True)#pins
#     async def links1button222(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LinksStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.ln}", custom_id="links1bu2tton23",disabled=True)#alert
#     async def links1button223(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LinksStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.lk}", custom_id="links21button24",disabled=True)#sectorrotation
#     async def links1button224(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LinksStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.ls}", custom_id="lin2ks1button25",disabled=True)#data
#     async def linkbutton225(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LinksStartView())


# class CommandsEmbed(disnake.Embed):
#     def __init__(self):
#         super().__init__(
#             title=f"{emojis.fudstop} FUDSTOP Application 2.0 Online",
#             description="```py\nThis is the FUDSTOP Application 2.0.``````py\nWithin this APP, you can click the buttons on the main page to get anything you need related to markets. From cited works to datasets, core play screener and bot-command help, as well as a server menu and YouTube videos - simply click what you need! Use the legend below to identify each category:```",
#             color=disnake.Colour.dark_orange(), url="https://www.fudstop.io")
        
#         self.add_field(name="<a:_:1042676749357555794>", value="```py\n/webull\nCommands using Webull's API! Features data from CBOE hanweck.```")
#         self.add_field(name=f"{emojis.optioncmd}", value="```py\n/Returns options related data and charts.```")
#         self.add_field(name=f"<a:_:1044503531878621195>",value="```py\n/dp\n\nCommands for dark-pool data such as biggest prints, weekly prints, day summary, and much more.```")
#         self.add_field(name="<a:_:1043013214180483112>", value="```py\n/stock\n\nGather ticker data for specific stocks - such as orderflow, leverage, liquidity, earnings crush, and much more.```")
#         self.add_field(name="<a:_:1043015881631993856>", value="```py\n/learn\n\nCommands used to learn several topics from discord to markets.```")
#         self.add_field(name="<a:_:1043016260415410206>", value="```py\n/c\n\n Command used to call stock charts to Discord.```")
#         self.add_field(name="<a:_:1043016260415410206>", value="```py\n/dd\n\nDue diligence commands from Open BB Bot.```")
#         self.add_field(name="<a:_:1043016503710208030>",value="```py\n/flow\n\nThese commands are for visualizing flow data for options.```")
#         self.add_field(name="<a:_:1043016743246901339>", value="```py\n/earnings\n\nCommands used for earnings related data.```")
#         self.add_field(name="<a:_:1043016869797441607>", value="```py\n/economy & /econ\n\nCommands related to economic information / data.```")
#         self.add_field(name="<a:_:1043022403393040414>", value="```py\n/analysis\n\nAnalyze markets, situations, and trends.```")
#         self.add_field(name="<a:_:1043024795404599438>", value="```py\n/jasmy\n\nJasmycoin related commands!```")
#         self.add_field(name="<a:_:1043017902191808523>", value="```py\n/stream\n\nCommands that return real-time data.```")
#         self.set_footer(text="Select a command set from the dropdown list to have the entire set printed to chat. Then, click the command to use it.")

# class AlertsEmbed(disnake.Embed):
#     def __init__(self):
#         super().__init__( 
#              title="tt🚀TradyTics Realtime Alerts",
#              description=f"```py\nPlay at your own risk. Very good return rates and play-calling. Definitely set notifications here to recieve the play alerts as soon as possible. The most lucrative alerts are the Bulls-eye alerts, social spike, and Stock Breakouts in my experience.```",
#              color=disnake.Colour.dark_red())



#         self.add_field(name="Navigation Code:",value="```py\ntt```")
#         self.add_field(name="tt<a:_:1043277380459962558>", value="<#1016369913759285338>")
#         self.add_field(name="tt<a:_:1043277380459962558>", value="<#1016369933187301416>")
#         self.add_field(name="tt<a:_:1043277380459962558>", value="<#1016369947829600297>")
#         self.add_field(name="tt<a:_:1043277380459962558>", value="<#1016369960810979388>")
#         self.add_field(name="tt<a:_:1043277380459962558>", value="<#1016369974945775666>")
#         self.add_field(name="tt<a:_:1043277380459962558>", value="<#1016369975864348673>")
#         self.add_field(name="tt<a:_:1043277380459962558>", value="<#1016369984768852090>")
#         self.add_field(name="tt<a:_:1043277380459962558>", value="<#1016369985867743394>")
#         self.add_field(name="tt<a:_:1043277380459962558>", value="<#1016372139802234991>")
#         self.add_field(name="tt<a:_:1043277380459962558>", value="<#1016372323051388999>")
#         self.add_field(name="tt<a:_:1043277380459962558>", value="<#1016372517251850360>")
#         self.add_field(name=f"{emojis.alert}", value="<#1016372151596630016>")
#         self.add_field(name="Navigation Code:",value="```py\ntt```")
#         self.set_footer(text="These can provide for some easy profit opportunities. Play at your own risk. Set notifications.")
        

# class NotificationsView(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, label="🇳 🇪 🇼 🇸", emoji=f"{emojis.worldwide}", custom_id="newsview1")
#     async def newsnotifs(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.defer(with_message=True, ephemeral=False)
#         self.add_item(FUDSTOPMenu())
#         em = disnake.Embed(title=f"{emojis.worldwide} News Area {emojis.worldwide}", description=f"```py\nSector monitoring for stock market industries. Each section contains dark pool feeds, quant alerts, unusual options alerts, regulation SHO alerts, and dark pool feeds real-time.```",color=disnake.Colour.random())
#         em.add_field(name="nw🌐After Hours", value="<#1041148553852112976>")
#         em.add_field(name="nw🌐Analyst Ratings", value="<#1015660065119797328>")
#         em.add_field(name="nw🌐Biotech", value="<#1041148250088030278>")
#         em.add_field(name="nw🌐Bonds", value="<#1041148248473210921>")
#         em.add_field(name="nw🌐Buybacks", value="<#1041146194455429171>")
#         em.add_field(name="nw🌐Cannabis", value="<#1041148025688567848>")
#         em.add_field(name="nw🌐Commodities", value="<#1015660043284258856>")
#         em.add_field(name="nw🌐Crypto", value="<#1015664808101695488")
#         em.add_field(name="nw🌐Dividends", value="<#1041148749948387328>")
#         em.add_field(name="nw🌐Downgrades", value="<#1041148750342664313>")
#         em.add_field(name="nw🌐Earnings", value="<#1015666153915424908>")
#         em.add_field(name="nw🌐Emerging Markets", value="<#1015666701389529228>")
#         em.add_field(name="nw🌐ETFs", value="<#1015660085353123910>")
#         em.add_field(name="nw🌐Fintech", value="<#1041150848329322586>")
#         em.add_field(name="nw🌐Forex", value="<#1041150847284936764>")
#         em.add_field(name="nw🌐Futures", value="<#1041150874715697182>")
#         em.add_field(name="nw🌐Gaming", value="<#1015666000814940220>")
#         em.add_field(name="nw🌐General", value="<#1015664603079921784>")
#         em.add_field(name="nw🌐Global", value="<#1015666000814940220>")
#         em.add_field(name="nw🌐Government", value="<#1015665876118294528>")
#         em.add_field(name="nw🌐Hedge Funds", value="<#1015664577754701825>")
#         em.add_field(name="nw🌐Intraday Updates", value="<#1015663450296430672>")
#         em.add_field(name="nw🌐Movers", value="<#1015662803304067193>")
#         em.add_field(name="nw🌐Trading Ideas", value="<#1015660106261737523>")
            
#         await inter.edit_original_message(embed=em)
#         await inter.send("```py\nClick this command and type 'nw' to see the list. There are more channels than listed here.``` </navigate channels:1034275861865705476>")  

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, label="🇵 🇱 🇦 🇾 🚀 🇦 🇱 🇪 🇷 🇹 🇸", custom_id="ttalerts")
#     async def ttnotifs(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.defer(with_message=True, ephemeral=False)
#         em = disnake.Embed(title="Play 🚀 Alerts", description="```py\nIf interested in having real-time play opportunities streeamlined to you intra-day - then it may be wise to set notifications for the Trady Tics section of discord.``` ```py\nThis section auto-posts play opportunities and can provide some lucrative opportunities. Make sure to always assess each play before entering, and trade these at your own risk as they are not apart of FUDSTOP's core logic process.```", color=disnake.Colour.dark_gold(), url="https://www.fudstop.io")
#         em.add_field(name="tt🚀News", value="<#1016372151596630016>")
        
#         em.add_field(name="tt🚀Options Sweeps", value="<#1016369913759285338>")
        
#         em.add_field(name="tt🚀Golden Sweeps", value="<#1016369933187301416>")
        
#         em.add_field(name="tt🚀Trady Flow", value="<#1016369947829600297>")
        
#         em.add_field(name="tt🚀Bullseye Alerts", value="<#1016369960810979388>")
        
            
#         em.add_field(name="tt🚀Scalps", value="<#1016369974945775666>")
        
            
#         em.add_field(name="tt🚀Social Spike", value="<#1016369975864348673>")
        
#         em.add_field(name="tt🚀Insider Trades", value="<#1016369984768852090>")
        
        
#         em.add_field(name="tt🚀Stock Breakouts", value="<#1016369985867743394>")
        
            
#         em.add_field(name="tt🚀Analyst Upgrades", value="<#1016372139802234991>")
        
            
#         em.add_field(name="tt🚀Crypto Breakouts", value="<#1016372323051388999>")
 
#         em.add_field(name="tt🚀Crypto Signals", value="<#1016372517251850360>")
#         em.add_field(name="Navigation Code:",value="```py\ntt```")
#         await inter.edit_original_message(embed=em, view=self)
#         await inter.send("```py\nClick this to launch the command. Then type 'tt' to view these channels!```</navigate channels:1034275861865705476>")



#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, label="🇷 🇸 🇸 🔊 🇫 🇪 🇪 🇩 🇸",custom_id="rssfeeds")
#     async def rssnotifs(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.defer(with_message=True, ephemeral=False)
#         self.add_item(FUDSTOPMenu())
#         em = disnake.Embed(title="🇷 🇸 🇸 🔊🇫 🇪 🇪 🇩 🇸", description="```py\nNever miss an important government or SEC filing again! Stay up to date with important developments by setting up notifications for these very critical Agency filings.```", color=disnake.Colour.dark_gold(), url="https://www.fudstop.io")
#         em.add_field(name="rss🔊Bonds", value="<#1019359742549823508>")
#         em.add_field(name="rss🔊Econ Library",value="<#1019361403032834128>") 
#         em.add_field(name="rss🔊FINRA Filings",value="<#1019360302250332301>")
#         em.add_field(name="rss🔊SEC Filings",value="<#1019360339856470146>")
#         em.add_field(name="rss🔊DTCC Filings",value="<#1028667813168173167>")
#         em.add_field(name="rss🔊NSCC Filings",value="<#1028668345702166698>")  
#         em.add_field(name="Navigation Code:",value="```py\nrss```")
#         await inter.edit_original_message(embed=em, view=self)
#         await inter.send("```py\nClick this to launch the command. Then type 'rss' to view these channels!```</navigate channels:1034275861865705476>")



#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, label="🇦 🇺 🇹 🇴  🇭 🇪 🇦 🇹 🇲 🇦 🇵 🇸", emoji="🔥",custom_id="heatmaps")
#     async def rssnotifs(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.defer(with_message=True, ephemeral=False)
#         self.add_item(FUDSTOPMenu())
#         em = disnake.Embed(title="🇦 🇺 🇹 🇴 🔥 🇭 🇪 🇦 🇹 🇲 🇦 🇵 🇸", description="```py\nSetup notifications for these channels to recieve auto-heatmaps for the specified index. These will post once per hour and provide a great intra-day check-up on markets if busy at work.```", color=disnake.Colour.fuchsia(), url="https://www.fudstop.io")
#         em.add_field(name="map🗾SP500", value="<#1035270377414336662>")
#         em.add_field(name="map🗾Crypto", value="<#1035270668901699584>")
#         em.add_field(name="map🗾NASDAQ 100", value="<#1035270694990262302>")
#         em.add_field(name="map🗾DOW 30", value="<#1035270719338201088>")
#         em.add_field(name="map🗾Russell 2000", value="<#1035270870320562267>")
#         em.add_field(name="map🗾Russell 1000", value="<#1035270806479056946>")
#         em.add_field(name="map🗾Market-Wide", value="<#1035270941208498186>")


 
#         em.add_field(name="Navigation Code:",value="```py\nmap```")
#         await inter.send("```py\nClick this to launch the command. Then type 'map' to view these channels!```</navigate channels:1042947625663610933>")


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, label="🇸 🇴 🇨 🇮 🇦 🇱",emoji="🔎",custom_id="socialmedia3")
#     async def socialmedia(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.defer(with_message=True, ephemeral=False)
#         self.add_item(FUDSTOPMenu())
#         em = disnake.Embed(title="🇸 🇴 🇨 🇮 🇦 🇱 🔎", description="```py\nSick of Twitter and Reddit? Participate from above by setting notifications for these channels. If you would like me to add someone you don't see on this list, or a subreddit you don't see - reach out and I can add it.```", color=disnake.Colour.dark_orange(), url="https://www.fudstop.io")
#         em.add_field(name="rr🧧FUDstop", value="<#1041143356690026567>")
#         em.add_field(name="rr🧧superstonk", value="<#1041143356690026567>")
#         em.add_field(name="rr🧧amcstock", value="<#1041143356690026567>")
#         em.add_field(name="rr🧧finance", value="<#1041143356690026567>")
#         em.add_field(name="rr🧧wallstreetbets", value="<#1041143356690026567>")
#         em.add_field(name="rr🧧stocks", value="<#1041143356690026567>")
#         em.add_field(name="tw🪢shilly'svids", value="<#1041143936988762122>")
#         em.add_field(name="tw🪢Ortex", value="<#1015879298940416071>")
#         em.add_field(name="tw🪢Gary Gensler", value="<#1041144288429473862>")
#         em.add_field(name="tw🪢FX Hedge", value="<#1041144342422749224>")
#         em.add_field(name="tw🪢Ryan Cohen", value="<#1041144801388679259>")
#         em.add_field(name="tw🪢Adam Aron", value="<#1041144840840290384>")
#         em.add_field(name="tw🪢Boss Blunts", value="<#1041144202228142152>")

#         em.add_field(name="Navigation Code:",value="```py\nrr for reddit | tw for twitter```")
#         await inter.edit_original_message(embed=em, view=self)
#         await inter.send("```py\nClick this to launch the command. Then type 'rr' for reddit or 'tw' for twitter to view these channels!```</navigate channels:1034275861865705476>", ephemeral=False)
    


#         self.embed = disnake.Embed(title=f"Alpha Menu", description=f"```py\nThis is the Alpha Menu. Click the data you want below.```", color=disnake.Colour.gold())
# class CoreStart(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)


    
#     @disnake.ui.button(style=disnake.ButtonStyle.red,emoji=f"{emojis.movingchart}", custom_id="core1button1",disabled=True,row=0)#datachart
#     async def core1button1(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = CoreEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.tools}", custom_id="core1button2",row=0,disabled=True)#tools
#     async def core1button2(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = CoreEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.confirmed}", custom_id="core1button3",row=0,disabled=False)#servermenu
#     async def menu(self, button: disnake.ui.Button, inter: disnake.AppCmdInter,ticker=str):
#         await inter.response.edit_message(view=LitStart(), embed=MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.book}", custom_id="core1button4",row=0,disabled=True)#citedworks
#     async def core1button4(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = CoreEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.movingchart}", custom_id="core1button5",disabled=True,row=0)#datachart
#     async def core1button5(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = CoreEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.lc}", custom_id="core1button6",row=1,disabled=True)#botcommands
#     async def core1button6(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=None, embed = CoreEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.lo}", custom_id="core1button7",disabled=True,row=1)#datachart
#     async def core1button7(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = CoreEmbed())
#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.uparrow}", custom_id="core1buttoaen9",disabled=True,row=1)#datachart
#     async def core1button8(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = CoreEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.letr}", custom_id="core1button10",disabled=True,row=1)#datachart
#     async def core1button9(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         pass



#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.le}", custom_id="core1button112",row=1,disabled=True)#news
#     async def core1button10(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = CoreEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.greencheck}", custom_id="core1button11",row=2,disabled=False)#links
#     async def core1button11(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         pass

#     @disnake.ui.button(style=disnake.ButtonStyle.red,emoji=f"{emojis.leftarrow}",custom_id="corecalls",row=2, disabled=True)
#     async def callscr342eener(self, button: disnake.ui.Button,interaction: disnake.MessageCommandInteraction):

#         await interaction.response.edit_message(view=CoreStart(), embed = CoreEmbed())

    
#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji=f"{emojis.fudstop}", custom_id="core1button13",row=2, disabled=True)#fudstop core
#     async def core1button13(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=CoreStart(), embed = CoreEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.red,emoji=f"{emojis.rightarrow}",custom_id="coreputds",row=2, disabled=True)
#     async def calls2342creener(self, button: disnake.ui.Button,interaction: disnake.MessageCommandInteraction):
#         await interaction.response.edit_message(view=AppStart(), embed = CoreEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.redcheck}", custom_id="core1button15",row=2,disabled=False)#puts
#     async def core1button15(self, button: disnake.ui.Button, interaction: disnake.AppCmdInter):

#         r2 = requests.get("https://www.alphaquery.com/service/run-screen?a=c7cff4986cfa6b7757c51e1c8b6f63c1c2fe66f052c6fd2741dfcea30c5cc1f4&screen=[{%22columnName%22:%22sector%22,%22operator%22:%22is%20not%22,%22value%22:%22Healthcare%22,%22valueType%22:%22%22,%22unit%22:%22%22},{%22columnName%22:%22rsi_14%22,%22operator%22:%22is%20greater%20than%22,%22value%22:%2270%22,%22valueType%22:%22number%22,%22unit%22:%22%22},{%22columnName%22:%22days_since_report_date_qr0%22,%22operator%22:%22is%20less%20than%22,%22value%22:%2210%22,%22valueType%22:%22number%22,%22unit%22:%22%22}]")

#         data2 = r2.json()


#         results2 = data2[
#             'resultsHtml'
#             ]
#         tag2 = "div"
#         reg_str2 = "<" + tag2 + ">(.*?)</" + tag2 + ">"
#         # regex to extract required strings
#         res2 = re.findall(
#             reg_str2, 
#             results2
#             )


#         for i in range(0,len(res2)):
#             try:
#                 put1 = res2[0:4]
#                 put2 = res2[5:9]
#                 put3 = res2[10:14]
#                 put4 = res2[15:19]
#                 put5 = res2[20:24]
#                 put6 = res2[25:29]
#                 put7 = res2[30:34]
#                 put8 = res2[35:39]
#                 put9 = res2[40:44]
#                 put10 = res2[45:49]
#             except IndexError:
#                 put1 = None
#                 put2 = "N/A"
#                 put3 = "N/A"
#                 put4 = "N/A"
#                 put5 = "N/A"
#                 put6 = "N/A"
#                 put7 = "N/A"
#                 put8 = "N/A"
#                 put9 = "N/A"
#                 put10 = "N/A"
#         item1 = put1
#         item2 = put2
#         item3 = put3
#         item4 = put4
#         item5 = put5
#         item6 = put6
#         item7 = put7
#         item8 = put8
#         item9 = put9
#         item10 = put10


#         items1 =  "\n".join(item1)
#         items2 =  "\n".join(item2)
#         items3 =  "\n".join(item3)
#         items4 =  "\n".join(item4)
#         items5 =  "\n".join(item5)
#         items6 =  "\n".join(item6)
#         items7 =  "\n".join(item7)
#         items8 =  "\n".join(item8)
#         items9 =  "\n".join(item9)
#         items10 = "\n".join(item10)

#         em2 = disnake.Embed(title=f"{emojis.redcheck}Core Puts{emojis.redcheck}", description=f"```py\nNote: This only displays the first 10 results (if any).\n\nPlease be responsible and verify that these plays fit all core criteria. Just because a ticker hits the screener does not automatically make it a core play. Click the link up top to be taken to the screener.```", color=disnake.Colour.dark_red(), url="https://www.alphaquery.com/stock-screener/600010229?run=1")
#         em2.add_field(name=f"Put#{emojis.pink1}{emojis.pink0}", value=f"```py\n{items1}```")
#         em2.add_field(name=f"Put#{emojis.pink9}", value=f"```py\n{items2}```")
#         em2.add_field(name=f"Put#{emojis.pink8}", value=f"```py\n{items3}```")
#         em2.add_field(name=f"Put#{emojis.pink7}", value=f"```py\n{items4}```")
#         em2.add_field(name=f"Put#{emojis.pink6}", value=f"```py\n{items5}```")
#         em2.add_field(name=f"Put#{emojis.pink5}", value=f"```py\n{items6}```")
#         em2.add_field(name=f"Put#{emojis.pink4}", value=f"```py\n{items7}```")
#         em2.add_field(name=f"Put#{emojis.pink3}", value=f"```py\n{items8}```")
#         em2.add_field(name=f"Put#{emojis.pink2}", value=f"```py\n{items9}```")
#         em2.add_field(name=f"Put#{emojis.pink1}", value=f"```py\n{items10}```", inline=False)

#         await interaction.response.edit_message(embed=em2, view=CoreStart())
#         await interaction.send("```py\nlogin: fudstoptrading@charliesindex.com || password: ||fudstoppers#23||``` Updates daily around 7-8 PM CST. https://www.alphaquery.com/stock-screener/600010229?run=1", ephemeral=False) 
        
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji="<a:_:1044890887680962591>", custom_id="core1button16",row=3,disabled=True)#videos
#     async def core1button16(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = CoreEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji="<a:_:1044647118352166994>", custom_id="core1button17",disabled=True,row=3)#datachart
#     async def core1button17(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = CoreEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey,emoji="<a:_:1044890977128685639>",custom_id="core1button18", row=3,disabled=True)
#     async def core1button18(self,button: disnake.ui.Button, interaction: disnake.MessageCommandInteraction):
#         await interaction.response.edit_message(view=self, embed=CoreEmbed())
       
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji="<a:_:1044647277437915277>", custom_id="core1button19",disabled=True,row=3)#datachart
#     async def core1button19(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = CoreEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji="<a:_:1044890936724951060>", custom_id="core1button20",row=3,disabled=True)#magicwand
#     async def core1button20(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = CoreEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji="<a:_:1043676146899877958>", custom_id="criteria1")
#     async def criteria1(self, button: disnake.ui.Button, interaction: disnake.MessageCommandInteraction):
#         embed = disnake.Embed(title="Criteria <a:_:1043676146899877958>", description="```py\nThe first criteria is to ensure that Earnings have just occured - and there exists a gap on the daily chart.```")
#         embed.add_field(name="Note:", value="```py\nI USE WEBULL FOR ALL OF MY TRADING NEEDS.``` ```py\nIf you aren't able to chart gaps because of the lack of the feature in your brokerage app - use horizontal lines.``` ```py\nFor Webull - to turn on the gaps - right click the chart and go to settings --> show gaps: five.\n\nOnly currently available for desktop.```")
#         embed.add_field(name="NOTE:", value="```py\nTHIS IS NOT A GAP FILL STRATEGY.``` ```py\n While gaps are the main criteria - WE DO NOT PLAY GAP FILLS. This will almost certainly cause losses for you. The strategy is to exploit the RSI - not the gap fill. More times than not - the gap actually never fills but rather acts as SUPPORT (downside gap) or RESISTANCE (upside gap).```")
#         embed.set_image(url="https://media.discordnet/attachments/896207280117264434/1043292492839268442/criteria1.png")
#         await interaction.response.send_message(embed=embed,ephemeral=False)
#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji="<a:_:1044765851506716673>", custom_id="criteria2")
#     async def criteria2(self, button: disnake.ui.Button, interaction: disnake.MessageCommandInteraction):
#         embed = disnake.Embed(title="Criteria <a:_:1044765851506716673>", description="```py\nThe second criteria to look for is an oversold or overbought RSI.(above 70 or below 30)``` ```py\nIn the current market state - there is no liquidity and it's being held captive in the repo. This is EXACTLY why we see gaps occur on earnings - because it remains one of the few moments in markets where the industry isn't sure of what's to come. This can be exploited as the gaps created are often OVER-REACTIONARY and exploitable by nature.```")
#         await interaction.response.send_message(embed=embed, ephemeral=False)

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji="<a:_:1044765841192931388>", custom_id="criteria3")
#     async def criteria3(self, button: disnake.ui.Button, interaction: disnake.MessageCommandInteraction):
#         embed = disnake.Embed(title="Criteria <a:_:1044765841192931388>", description="```py\nThe third criteria is to ensure that the MACD banana is curling, or is 'ripe'. Whenever the MACD starts to flatten = lucrative buying opportunity. This criterion should be considered a must for beginniners, but can be foregone once enough experience is acquired to understand core.```")
#         embed.add_field(name="NOTE:", value="```py\nPUT PLAYS TAKE LONGER TO PAN OUT THAN CALL PLAYS MORE TIMES THAN NOT.``` ```py\nIt's important to have patience here. Many of you are only used to trading high volatile, super active stocks - so after a day of trading sideways you're ready to give up on the trade. TRUST THE PROCESS. PAYTIENCE.```")
#         embed.set_image(url="https://media.discordnet/attachments/896207280117264434/1043297497499582594/macd.png")
#         await interaction.response.send_message(embed=embed, ephemeral=False)
#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji="<a:_:1044765824960974938>", custom_id="criteria4")
#     async def criteria4(self, button: disnake.ui.Button, interaction: disnake.MessageCommandInteraction):
#         embed = disnake.Embed(title="Criteria <a:_:1044765824960974938>", description="```py\nCriteria #4 is to always ensure that the IV is low. By running the``` </iv percentile:1042947626217246750> and </iv rank:1042947626217246750> commands.")
#         embed.add_field(name="IV Rank", value="```py\nOne method for rating the current IV is to rank it relative to its historical low/high range. For example, if the past year of IV measurements has ranged from a low of 20 to a high of 50, a current IV of 35 would be halfway between the low and high, producing an IV Rank of 50%. If the current IV were 44, then it would be 4/5 of the way from 20 to 50, resulting in an IV Rank of 80%. ```")
#         embed.add_field(name="IV Percentile", value="```py\n Another method for rating the current IV is to rank it relative to all IV measurements over the historical term. For example, if half of the past year’s measurements of IV have been lower than the current IV, then the current IV Percentile would be 50%. If only 20% of the measurements were below the current IV, then the IV Percentile would be 20%. This approach effectively accounts for the density of historical measurements```")
#         embed.set_image(url="https://media.discordnet/attachments/896207280117264434/1043297751934443681/image.png?width=1058&height=671")
#         await interaction.response.send_message(embed=embed,ephemeral=False)


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji="<a:_:1044766617810259988>", custom_id="criteria5")
#     async def criteria5(self, button: disnake.ui.Button, interaction: disnake.MessageCommandInteraction):
#         embed = disnake.Embed(title="Criteria <a:_:1043215878516379758>", description="```py\nCriteria #5 is your exit.``` ```py\nIf new: YOUR EXIT = IF YOU ARE PUSHED OUT OF THE MONEY.``` ```py\nFor example - if you buy a call at strike ITM at $60, and the price falls below $60 and holds - EXIT and move on - this is best practice when first starting out.```")
#         embed.add_field(name="Exit Strategy:", value="```py\nPlease don't ask anyone when you should sell. Only you can answer that question.```")
#         embed.add_field(name="NOTE:",value="```py\n HAVE PATIENCE. These are monthly options - not weekly or daily. Align your psychology with the correct timeframe.```")
#         await interaction.response.send_message(embed=embed,ephemeral=False)


# class DiscordHelpMenu(disnake.ui.Select):
#     def __init__(self):
#         super().__init__(
#             placeholder="🇩 🇮 🇸 🇨 🇴 🇷 🇩  🇭 🇪 🇱 🇵",
#             min_values=1,
#             max_values=1,
#             custom_id="discordhelpdrop",
#             options=[

#             disnake.SelectOption(label="Saving Messages as Threads",description="Learn how to quickly save messages as Threads.", emoji="<a:_:1043216082644766811>"),
#             disnake.SelectOption(label="Utilizing Discord Search",description="Our discord search feature is one of the most useful tools in this entire Discord.", emoji="<a:_:1043216082644766811>"),
#             disnake.SelectOption(label="Turning on Developer Mode",description="It is **absolutely essential that you turn on developer mode.", emoji="<a:_:1043216082644766811>"),
#             disnake.SelectOption(label="The Hashtag Navigation System",description="Learn how to navigate in discord using the channel keys.", emoji="<a:_:1043216082644766811>"),
#             disnake.SelectOption(label="Optimizing Your Discord Layout",description="In discord - you can mute the channels you don't want to hear info from", emoji="<a:_:1043216082644766811>"),
#             disnake.SelectOption(label="How to Query Every Ticker in the Market",description="A tutorial on how to query all tickers with Alphaquery.", emoji="<a:_:1043216082644766811>"),
#             disnake.SelectOption(label="Navigation and Researching",description="Discord tricks regarding navigation within discord and researching.", emoji="<a:_:1043216082644766811>"),
#             disnake.SelectOption(label="How to Read Open Interest & Volume",description="Learn to read OI and Volume.", emoji="<a:_:1043216082644766811>"),
#             disnake.SelectOption(label="Spy Charting",description="Learn how to chart for SUPPORT and RESISTANCE by using gaps.", emoji="<a:_:1043216082644766811>"),
#             disnake.SelectOption(label="Alphaquery Tutorial",description="Learn how to use Alphaquery", emoji="<a:_:1043216082644766811>"),
#             disnake.SelectOption(label="Desktop Notifications Example",description="Desktop notifications makes it easy to monitor markets during the day.", emoji="<a:_:1043216082644766811>"),
#             disnake.SelectOption(label="Query Every Ticker in the Market by RSI",description="Learn to use Alphaquery for giant RSI queries.```", emoji="<a:_:1043216082644766811>")])
#     async def callback(self,interaction:disnake.MessageCommandInteraction):
#         if  self.values[0] == "Saving Messages as Threads":
#             await interaction.send("https://youtu.be/neWYeYpfpxY", ephemeral=False)

#         elif self.values[0] == "Utilizing Discord Search":
#             await interaction.send("https://youtu.be/3CkRmT2SMNk", ephemeral=False)

#         elif self.values[0] == "Turning on Developer Mode":
#             await interaction.send("https://youtu.be/b52p7V4QTaM", ephemeral=False)

#         elif self.values[0] == "The Hashtag Navigation System":
#             await interaction.send("https://youtu.be/scRK6rZ_HWY", ephemeral=False)


#         elif self.values[0] == "Optimizing Your Discord Layout":
#             await interaction.send("https://youtu.be/xvlTy_GG10Y", ephemeral=False)


#         elif self.values[0] == "How to Query Every Ticker in the Market":
#             await interaction.send("https://youtu.be/HLG-ol7bAkA", ephemeral=False)


#         elif self.values[0] == "Navigation and Researching":
#             await interaction.send("https://youtu.be/sHthg4RKMRY", ephemeral=False)


#         elif self.values[0] == "How to Read Open Interest & Volume":
#             await interaction.send("https://youtu.be/7laLsbo3-K8", ephemeral=False)


#         elif self.values[0] == "Spy Charting":
#             await interaction.send("https://youtu.be/Gucc9fkphbo", ephemeral=False)

#         elif self.values[0] == "Alphaquery Tutorial":
#             await interaction.send("https://youtu.be/J-GfKWFSWuk", ephemeral=False)


#         elif self.values[0] == "Desktop Notifications Example":
#             await interaction.send("https://youtu.be/zPG_hoQXAto", ephemeral=False)
        
#         elif self.values[0] == "Query Every Ticker in the Market by RSI":
#             await interaction.send("https://youtu.be/2_Jb42gtz7I", ephemeral=False)


# class AppStart(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)




#     @disnake.ui.button(style=disnake.ButtonStyle.blurple,emoji=f"{emojis.movingchart}", custom_id="page1button1",disabled=True,row=0)#datachart
#     async def page1button1(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.tools}", custom_id="page1button2",row=0,disabled=True)#tools
#     async def page1button2(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.confirmed}", custom_id="page1button3",row=0,disabled=True)#servermenu
#     async def menu(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=MenuStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.book}", custom_id="page1button4",row=0,disabled=True)#citedworks
#     async def page1button4(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="page1button5",disabled=True)#datachart
#     async def page1button5(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.confirmed}", custom_id="page1button6",row=1,disabled=True)#botcommands
#     async def page1button6(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(embed = MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="page1button7",disabled=True,row=1)#datachart
#     async def page1button7(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.uparrow}", custom_id="page1button8", disabled=True,row=1)#arrow
#     async def page1button8(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="page1button9",disabled=True,row=1)#datachart
#     async def page1button9(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.worldwide}", custom_id="page1button10",row=1,disabled=True)#news
#     async def page1button10(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.links}", custom_id="page1button11",row=2,disabled=True)#links
#     async def page1button11(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.leftarrow}", custom_id="page1button12", disabled=True,row=2) #arrowleft
#     async def page1button12(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji="<a:_:1044512918466727986>", custom_id="page1button13",row=2)#fudstop core
#     async def page1button13(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=CoreStart(), embed = CoreEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.rightarrow}", custom_id="page1button14", disabled=True,row=2)#arrowright
#     async def page1button14(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji="<a:_:1042806896555474974>", custom_id="page1button15",row=2,disabled=True)#diamond
#     async def page1button15(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.video}", custom_id="page1button16",row=3,disabled=True)#videos
#     async def page1button16(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="page1button17",disabled=True,row=3)#datachart
#     async def page1button17(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.exit}", custom_id="page1button18",disabled=True,row=3)#arrow
#     async def page1button18(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="page1button19",disabled=True,row=3)#datachart
#     async def page1button19(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.confirmed}", custom_id="page1button20",row=3,disabled=True)#magicwand
#     async def page1button20(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="page1button21",disabled=True,row=4)#datachart
#     async def page1button21(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.question}", custom_id="page1button22",row=4,disabled=True)#pins
#     async def page1button22(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.alert}", custom_id="page1button23",row=4,disabled=True)#alert!
#     async def page1button23(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.purpleslash}", custom_id="page1button24",row=4,disabled=True)
#     async def page1button24(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="page1button25",disabled=True,row=4)#datachart
#     async def linkbutton25(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart(), embed = MainEmbedAPP())


# class LitStart(disnake.ui.View):
#     def __init__(self):

#         super().__init__(timeout=None)


        
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="lit1button1",row=0,disabled=True)#botcommands
#     async def lit1button1(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=None)
        


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple,emoji=f"{emojis.tools}", custom_id="lit1button2",disabled=False,row=0)#datachart
#     async def lit1button2(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=ToolsViewStart(), embed =ToolsEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.uparrow}", custom_id="lit1butto3",row=0,disabled=False)#data
#     async def mengre(self,button: disnake.ui.Button,inter:disnake.AppCmdInter):
        

#         await inter.response.edit_message(view=DataViewStart(), embed=DataViewStart().embed)
        



#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.book}", custom_id="lit1button4",disabled=False,row=0)#datachart
#     async def lit1button3(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         embed = disnake.Embed(title=f"{emojis.lc}{emojis.li}{emojis.lt}{emojis.le}{emojis.ld}", description=f"```py\nBrowse several topics of Cited Works to learn Financial Markets from the Leaders of the Industry.```", color=disnake.Colour.dark_gold())
#         embed.add_field(name=f"{emojis.fed}", value=f"```py\nCited works and publications from the Federal Reserve Bank of New York.```")
#         await inter.response.edit_message(view=CitedWorksViewStart(), embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="lit1button5",row=0,disabled=True)#news
#     async def lit1button10(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=MenuStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.confirmed}", custom_id="lit1button6",row=1,disabled=False)#botcommands
#     async def lit1button4(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=CommandsStart(), embed = CommandsEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="lit1button7",disabled=True,row=1)#datachart
#     async def lit1button5(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=None)

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.uptrend}", custom_id="lit1button8",row=1,disabled=False)#data
#     async def menu(self,button: disnake.ui.Button,inter:disnake.AppCmdInter):
        

#         await inter.response.edit_message(view=TAStart(), embed=TechnicalEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="lit1button9",disabled=True,row=1)#datachart
#     async def lit1button9(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=None)

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.worldwide}", custom_id="lit1button10",row=1,disabled=False)#news
#     async def lit1buttonx(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=MenuStart(), embed = MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.leftarrow}", custom_id="lit1button11", disabled=True,row=2) #arrowleft
#     async def lit1buttonxx(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=None)

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.links}", custom_id="lit1button12",row=2,disabled=False)#links
#     async def lit1button11(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LinksStartView(), embed = MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji=f"{emojis.fudstop}", custom_id="pager1button13",row=2)#fudstop core
#     async def lit1button13(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=CoreStart(), embed = CoreEmbed())

    
#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.stock}", custom_id="lit1button14",row=2,disabled=True)#diamond
#     async def lit1button15(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=None)
    
#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.rightarrow}", custom_id="lit1button15", disabled=False,row=2)#marketdata
#     async def lit1button14(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=MarketsView(), embed = MarketsEmbed())



#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.video}", custom_id="lit1button16",row=3,disabled=False)#videos
#     async def lit1button16(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView(), embed = MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="lit1button17",disabled=True,row=3)#datachart
#     async def lit1button17(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=None)

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.alert}", custom_id="lit1button18",row=3,disabled=False)#alert!
#     async def lit1button23(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AlertStart(), embed = MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="lit1button19",disabled=True,row=3)#datachart
#     async def lit1button19(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=None)


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.confirmed}", custom_id="lit1button20",row=3,disabled=False)#magicwand
#     async def lit1button20(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=DiscordStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="lit1button21",disabled=True,row=4)#datachart
#     async def lit1button21(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=None)

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.question}", custom_id="lit1button22",row=4,disabled=False)#pins
#     async def lit1button22(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=HelpStart(), embed = HelpEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.downarrow}", custom_id="lit1button23",disabled=False,row=4)#exit
#     async def lit1buttox(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AgencyViewStart(), embed=AgencyViewStart().embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.purpleslash}", custom_id="lit1button24",row=4,disabled=False)
#     async def lit1button24(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=StockPage1(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="lit1button25",disabled=True,row=4)#datachart
#     async def linkbutton25(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=None)


# class AgencyViewStart(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)

#         self.embed = disnake.Embed(title=f"{emojis.la}{emojis.lg}{emojis.le}{emojis.ln}{emojis.lc}{emojis.li}{emojis.le}{emojis.ls}", description=f"```py\nIn this section of Book-Market - you can find datasets from Agencies around the Industry.```", color=disnake.Colour.dark_blue())
#         self.embed.add_field(name=f"{emojis.confirmed}", value=f"```py\nReturn to Main.```")


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.confirmed}", custom_id="agency1button1",row=0,disabled=True)#botcommands
#     async def agency1button1(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AgencyViewStart(), embed=AgencyViewStart().embed)


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple,emoji=f"{emojis.coolchart}", custom_id="agency1button2",disabled=False,row=0)#datachart
#     async def agency1button2(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AgencyViewStart(), embed=AgencyViewStart().embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji=f"{emojis.confirmed}", custom_id="agency1butto3",row=0,disabled=True)#data
#     async def mengre(self,button: disnake.ui.Button,inter:disnake.AppCmdInter):
        

#         await inter.response.edit_message(view=DataViewStart(), embed=DataViewStart().embed)


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.coolchart}", custom_id="agency1button4",disabled=False,row=0)#datachart
#     async def agency1button3(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         embed = disnake.Embed(title=f"{emojis.lc}{emojis.li}{emojis.lt}{emojis.le}{emojis.ld}", description=f"```py\nBrowse several topics of Cited Works to learn Financial Markets from the Leaders of the Industry.```", color=disnake.Colour.dark_gold())
#         embed.add_field(name=f"{emojis.fed}", value=f"```py\nCited works and publications from the Federal Reserve Bank of New York.```")
#         await inter.response.edit_message(view=AgencyViewStart(), embed=AgencyViewStart().embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.confirmed}", custom_id="agency1button5",row=0,disabled=True)#news
#     async def agency1button10(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AgencyViewStart(), embed=AgencyViewStart().embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.coolchart}", custom_id="agency1button6",row=1,disabled=False)#botcommands
#     async def agency1button4(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AgencyViewStart(), embed=AgencyViewStart().embed)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.confirmed}", custom_id="agency1button7",disabled=True,row=1)#datachart
#     async def agency1button5(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=None)

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.coolchart}", custom_id="agency1button8",row=1,disabled=False)#data
#     async def menu(self,button: disnake.ui.Button,inter:disnake.AppCmdInter):
        

#         await inter.response.edit_message(view=AgencyViewStart(), embed=AgencyViewStart().embed)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.confirmed}", custom_id="agency1button9",disabled=True,row=1)#datachart
#     async def agency1button9(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=None)

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.coolchart}", custom_id="agency1button10",row=1,disabled=False)#news
#     async def agency1buttonx(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AgencyViewStart(), embed=AgencyViewStart().embed)


#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji=f"{emojis.confirmed}", custom_id="agency1button11", disabled=True,row=2) #arrowleft
#     async def agency1buttonxx(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=None)

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.confirmed}", custom_id="agency1button12",row=2,disabled=False)#links
#     async def agency1button11(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=OFRViewStart(), embed=OFRViewStart().embed)


#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.confirmed}", custom_id="agecy13button13",row=2)#fudstop core
#     async def agency1button13(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed=MainEmbedAPP())

    
#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.coolchart}", custom_id="agency1button14",row=2,disabled=True)#diamond
#     async def agency1button15(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=None)
    
#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji=f"{emojis.confirmed}", custom_id="agency1button15", disabled=True,row=2)#marketdata
#     async def agency1button14(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AgencyViewStart(), embed=AgencyViewStart().embed)



#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.coolchart}", custom_id="agency1button16",row=3,disabled=False)#videos
#     async def agency1button16(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView(), embed = MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.confirmed}", custom_id="agency1button17",disabled=True,row=3)#datachart
#     async def agency1button17(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=None)

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.coolchart}", custom_id="agency1button18",row=3,disabled=False)#alert!
#     async def agency1button23(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AlertStart(), embed = MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.confirmed}", custom_id="agency1button19",disabled=True,row=3)#datachart
#     async def agency1button19(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=None)


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.coolchart}", custom_id="agency1button20",row=3,disabled=False)#magicwand
#     async def agency1button20(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AgencyViewStart(), embed=AgencyViewStart().embed)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.confirmed}", custom_id="agency1button21",disabled=True,row=4)#datachart
#     async def agency1button21(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=None)

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.coolchart}", custom_id="agency1button22",row=4,disabled=False)#pins
#     async def agency1button22(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AgencyViewStart(), embed=AgencyViewStart().embed)


#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji=f"{emojis.confirmed}", custom_id="agency1button23",disabled=True,row=4)#exit
#     async def agency1buttox(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AgencyViewStart(), embed=AgencyViewStart().embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.coolchart}", custom_id="agency1button24",row=4,disabled=False)
#     async def agency1button24(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AgencyViewStart(), embed=AgencyViewStart().embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="agency1button25",disabled=True,row=4)#datachart
#     async def linkbutton25(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=None)


# class VideoSelect(disnake.ui.Select):
#     def __init__(self):
#         super().__init__( 
#             placeholder="🇸 🇺 🇧 🇯 🇪 🇨 🇹 ⬇️ 🇱 🇮 🇸 🇹",
#             min_values=1,
#             max_values=1,
#             custom_id="lfwet34he5r",
#             options = [ 
#                 disnake.SelectOption(label=f"FUDSTOP and Discord Videos", description="Nasdaq history and filings.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"National Securities Clearing Corp.", description="Filings, documents, history out of the NSCC.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"Depository Trust Clearing Corp.", description="Filings, documents, DRS, history cited works, papers, and more from the DTCC.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"FINRA", description="FINRA History and Filings.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"Securities and Exchange Commission", description="Important SEC Filings, history.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"Members Exchange", description="Learn about MEMX.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"The New York Stock Exchange", description="Learn about the NYSE via filings and histroy.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"THe Options Clearing Corporation", description="Learn how the OCC shapes the options markets.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"Reddit and Social Media", description="Social Media Psyop Warfare & Other Topics", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"Personal/Opinion", description="Nasdaq history and filings.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"AMC/GME Related", description="Nasdaq history and filings.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"History", description="Nasdaq history and filings.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"Trading and Psychology", description="Nasdaq history and filings.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"FUDSTOP and Discord Videos", description="Nasdaq history and filings.", emoji=f"{emojis.video}"),])
            
#     async def callback(self,interaction:disnake.MessageCommandInteraction):
#         if self.values == "FUDSTOP and Discord Videos":
#             pass
            


# class VideoStartView(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple,emoji=f"{emojis.balloons}", custom_id="video1button1",disabled=False,row=0)#datachart
#     async def video1button1(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         embed = disnake.Embed(title="Appls")
#         embed.set_image(url="https://i5.walmartimages.com/asr/bf2ec88a-2f36-41f2-93d3-c3161772733d_1.cdc913433c6acc6bf9201dc1fa86bac9.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF")
#         await inter.response.edit_message(view=VideoStart2View(),embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.uptrend}", custom_id="video1button2",row=0,disabled=True)#$
#     async def video1button2(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())
    


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.balloons}", custom_id="video1button3", disabled=False,row=0)#arrow
#     async def video1button8(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStart2View())


#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.uptrend}", custom_id="video1button4",row=0,disabled=True)#citedworks
#     async def video1button4(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())





#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.uptrend}", custom_id="video1button20",row=3,disabled=True)#magicwand
#     async def video1button20(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.balloons}", custom_id="video1button21",disabled=False,row=4)#datachart
#     async def video1button21(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStart2View())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.uptrend}", custom_id="video1button22",row=4,disabled=True)#pins
#     async def video1button22(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.balloons}", custom_id="video1button23",disabled=False,row=4)#exit
#     async def video1button18(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStart2View())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.uptrend}", custom_id="video1button24",row=4,disabled=True)
#     async def video1button24(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.balloons}", custom_id="video1button25",disabled=False,row=4)#datachart
#     async def linkbutton25(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStart2View())



# class VideoStart2View(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)


#         self.select = disnake.ui.Select(
#             placeholder="🇸 🇺 🇧 🇯 🇪 🇨 🇹 ⬇️ 🇱 🇮 🇸 🇹",
#             min_values=1,
#             max_values=1,
#             custom_id="lfwet34he5r",
#             options = [ 
#                 disnake.SelectOption(label=f"National Securities Clearing Corp.", description="Filings, documents, history out of the NSCC.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"Depository Trust Clearing Corp.", description="Filings, documents, DRS, history cited works, papers, and more from the DTCC.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"FINRA", description="FINRA History and Filings.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"Securities and Exchange Commission", description="Important SEC Filings, history.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"Members Exchange", description="Learn about MEMX.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"The New York Stock Exchange", description="Learn about the NYSE via filings and histroy.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"THe Options Clearing Corporation", description="Learn how the OCC shapes the options markets.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"Reddit and Social Media", description="Social Media Psyop Warfare & Other Topics", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"NASDAQ", description="Nasdaq history and filings.", emoji=f"{emojis.video}"),
#             ]
#         )

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,emoji=f"{emojis.alert}", custom_id="video1button1",disabled=True,row=0)#datachart
#     async def video1button1(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         embed = disnake.Embed(title="Appls")
#         embed.set_image(url="https://i5.walmartimages.com/asr/bf2ec88a-2f36-41f2-93d3-c3161772733d_1.cdc913433c6acc6bf9201dc1fa86bac9.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF")
#         await inter.response.edit_message(view=VideoStartView(),embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.alert}", custom_id="video20button2",row=0,disabled=True)#$
#     async def video20button2(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())
    


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.alert}", custom_id="video20button3", disabled=True,row=0)#arrow
#     async def video20button8(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.alert}", custom_id="video20button4",row=0,disabled=True)#citedworks
#     async def video20button4(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.alert}", custom_id="video20button5",disabled=True)#datachart
#     async def video20button5(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.alert}", custom_id="video20button6",row=1,disabled=True)#botcommands
#     async def video20button6(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.alert}", custom_id="video20button7",disabled=True,row=1)#datachart
#     async def video20button7(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.movers}", custom_id="video20button8",row=1,disabled=True)#data
#     async def menu(self,button: disnake.ui.Button,inter:disnake.AppCmdInter):
        

#         await inter.response.edit_message(view=VideoStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.alert}", custom_id="video20button9",disabled=True,row=1)#datachart
#     async def video20button9(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.alert}", custom_id="video20button10",row=1,disabled=True)#news
#     async def video20button10(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.alert}", custom_id="video20button11", disabled=True,row=2) #arrowleft
#     async def video20button12(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.movers}", custom_id="video20button12",row=2,disabled=False)#links
#     async def video20button11(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.alert}", custom_id="pager1button13",row=2)#fudstop core
#     async def video20button13(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())

    
#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.stock}", custom_id="video20button14",row=2,disabled=False)#diamond
#     async def video20button15(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStart3View())
    
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.alert}", custom_id="video20button15", disabled=True,row=2)#marketdata
#     async def video20button14(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())



#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.alert}", custom_id="video20button16",row=3,disabled=True)#videos
#     async def video20button16(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.alert}", custom_id="video20button17",disabled=True,row=3)#datachart
#     async def video20button17(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.movers}", custom_id="video20button18",row=3,disabled=True)#alert!
#     async def video20button23(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.alert}", custom_id="video20button19",disabled=True,row=3)#datachart
#     async def video20button19(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.alert}", custom_id="video20button20",row=3,disabled=True)#magicwand
#     async def video20button20(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.alert}", custom_id="video20button21",disabled=True,row=4)#datachart
#     async def video20button21(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.alert}", custom_id="video20button22",row=4,disabled=True)#pins
#     async def video20button22(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.alert}", custom_id="video20button23",disabled=True,row=4)#exit
#     async def video20button18(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.alert}", custom_id="video20button24",row=4,disabled=True)
#     async def video20button24(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.alert}", custom_id="video20button25",disabled=True,row=4)#datachart
#     async def linkbutton25(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())


# class VideoStart3View(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)


#         self.select = disnake.ui.Select(
#             placeholder="🇸 🇺 🇧 🇯 🇪 🇨 🇹 ⬇️ 🇱 🇮 🇸 🇹",
#             min_values=1,
#             max_values=1,
#             custom_id="lfwet34he5r",
#             options = [ 
#                 disnake.SelectOption(label=f"National Securities Clearing Corp.", description="Filings, documents, history out of the NSCC.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"Depository Trust Clearing Corp.", description="Filings, documents, DRS, history cited works, papers, and more from the DTCC.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"FINRA", description="FINRA History and Filings.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"Securities and Exchange Commission", description="Important SEC Filings, history.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"Members Exchange", description="Learn about MEMX.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"The New York Stock Exchange", description="Learn about the NYSE via filings and histroy.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"THe Options Clearing Corporation", description="Learn how the OCC shapes the options markets.", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"Reddit and Social Media", description="Social Media Psyop Warfare & Other Topics", emoji=f"{emojis.video}"),
#                 disnake.SelectOption(label=f"NASDAQ", description="Nasdaq history and filings.", emoji=f"{emojis.video}"),
#             ]
#         )

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,emoji=f"{emojis.boom}", custom_id="video1button1",disabled=True,row=0)#datachart
#     async def video1button1(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         embed = disnake.Embed(title="Appls")
#         embed.set_image(url="https://i5.walmartimages.com/asr/bf2ec88a-2f36-41f2-93d3-c3161772733d_1.cdc913433c6acc6bf9201dc1fa86bac9.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF")
#         await inter.response.edit_message(view=VideoStartView(),embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.boom}", custom_id="video20button2",row=0,disabled=True)#$
#     async def video20button2(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())
    


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.boom}", custom_id="video20button3", disabled=True,row=0)#arrow
#     async def video20button8(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.boom}", custom_id="video20button4",row=0,disabled=True)#citedworks
#     async def video20button4(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.boom}", custom_id="video20button5",disabled=True)#datachart
#     async def video20button5(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.boom}", custom_id="video20button6",row=1,disabled=True)#botcommands
#     async def video20button6(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.eye}", custom_id="video20button7",disabled=False,row=1)#datachart
#     async def video20button7(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         self.video20button9.emoji = f"{emojis.movers}"
#         self.video20button23.emoji = f"{emojis.blackmouth}"
#         await inter.response.edit_message(view=self)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.boom}", custom_id="video20button8",row=1,disabled=True)#data
#     async def menu(self,button: disnake.ui.Button,inter:disnake.AppCmdInter):
        

#         await inter.response.edit_message(view=VideoStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.eye}", custom_id="video20button9",disabled=False,row=1)#datachart
#     async def video20button9(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         self.video20button9.emoji = f"{emojis.eye}"
#         self.video20button23.emoji = f"{emojis.mouth}"
#         await inter.response.edit_message(view=VideoStart3View())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.boom}", custom_id="video20button10",row=1,disabled=True)#news
#     async def video20button10(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStart3View())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.boom}", custom_id="video20button11", disabled=True,row=2) #arrowleft
#     async def video20button12(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStart3View())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.boom}", custom_id="video20button12",row=2,disabled=True)#links
#     async def video20button11(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStart3View())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.nose}", custom_id="pager1button13",row=2, disabled=True)#fudstop core
#     async def video20button13(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStart3View())

    
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.boom}", custom_id="video20button14",row=2,disabled=True)#diamond
#     async def video20button15(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStart3View())
    
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.boom}", custom_id="video20button15", disabled=True,row=2)#marketdata
#     async def video20button14(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStart3View())



#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.boom}", custom_id="video20button16",row=3,disabled=True)#videos
#     async def video20button16(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.boom}", custom_id="video20button17",disabled=True,row=3)#datachart
#     async def video20button17(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.mouth}", custom_id="video20button18",row=3,disabled=False)#boom!
#     async def video20button23(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):

#         await inter.response.edit_message(
#        ".\n :eye_nazar: :eye_nazar: "
#         "👃 "
#       "👄",view=VideoStart3View())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.boom}", custom_id="video20button19",disabled=True,row=3)#datachart
#     async def video20button19(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.boom}", custom_id="video20button20",row=3,disabled=True)#magicwand
#     async def video20button20(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.boom}", custom_id="video20button21",disabled=True,row=4)#datachart
#     async def video20button21(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.boom}", custom_id="video20button22",row=4,disabled=True)#pins
#     async def video20button22(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStart3View())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.boom}", custom_id="video20button23",disabled=True,row=4)#exit
#     async def video20button18(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.boom}", custom_id="video20button24",row=4,disabled=True)
#     async def video20button24(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.boom}", custom_id="video20button25",disabled=True,row=4)#datachart
#     async def linkbutton25(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=VideoStartView())

# class DiscordStart(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)

#         self.add_item(DiscordHelpMenu())
#     @disnake.ui.button(style=disnake.ButtonStyle.blurple,emoji=f"{emojis.movingchart}", custom_id="discord1button1",row=0, disabled=True)#data
#     async def discord1button1(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.tools}", custom_id="discord1button2",row=0, disabled=True)#tools
#     async def discord1button2(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.confirmed}", custom_id="discord1button3",row=0, disabled=True)#check
#     async def discord1button3(self, bug: str, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.book}", custom_id="discord1button4",row=0, disabled=True)#citedworks
#     async def discord1button4(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="discord1button5",row=0, disabled=True)#data
#     async def discord1button5(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.confirmed}", custom_id="discord1button6",row=1, disabled=True)#botcommands
#     async def discord1button6(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=None)


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="discord1button7",row=1, disabled=True)
#     async def discord1button7(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.uparrow}", custom_id="discord1button8", disabled=False,row=1)
#     async def discord1button8(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="discord1button9",row=1, disabled=True)
#     async def discord1button9(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.worldwide}", custom_id="discord1button10",row=1, disabled=True)
#     async def discord1button10(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


    

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.video}", custom_id="discord1button16",row=3, disabled=True)
#     async def discord1button16(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="discord1button17",row=3, disabled=True)
#     async def discord1button17(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.exit}", custom_id="discord1button18",disabled=True,row=3)#DOWNARROW
#     async def downarrow(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="discord1button19",row=3, disabled=True)#data
#     async def discord1button19(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji=f"{emojis.confirmed}", custom_id="discord1button20",row=3, disabled=False)#magicwand
#     async def discord1button20(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="discord1button21",row=4, disabled=True)#data
#     async def discord1button21(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.question}", custom_id="discord1button22",row=4, disabled=True)#pins
#     async def discord1button22(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.alert}", custom_id="discord1button23",row=4, disabled=True)#alert
#     async def discord1button23(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.purpleslash}", custom_id="discord1button24",row=4, disabled=True)#sectorrotation
#     async def discord1button24(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="discord1button25",row=4, disabled=True)#data
#     async def linkbutton25(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


# class MenuStart(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)


#         self.add_item(FUDSTOPMenu())

       

    
#     @disnake.ui.button(style=disnake.ButtonStyle.blurple,emoji=f"{emojis.movingchart}", custom_id="menu1button1",row=0, disabled=True)#data
#     async def menu1button1(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.tools}", custom_id="menu1button2",row=0, disabled=True)#tools
#     async def menu1button2(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.confirmed}", custom_id="menu1button3",row=0, disabled=True)#check
#     async def menu1button3(self, bug: str, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.book}", custom_id="menu1button4",row=0, disabled=True)#citedworks
#     async def menu1button4(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="menu1button5",row=0, disabled=True)#data
#     async def menu1button5(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.confirmed}", custom_id="menu1button6",row=1, disabled=True)#botcommands
#     async def menu1button6(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=None)


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="menu1button7",row=1, disabled=True)
#     async def menu1button7(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.uparrow}", custom_id="menu1button8", disabled=False,row=1)
#     async def menu1button8(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="menu1button9",row=1, disabled=True)
#     async def menu1button9(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.worldwide}", custom_id="menu1button10",row=1, disabled=False)
#     async def menu1button10(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


    

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.video}", custom_id="menu1button16",row=3, disabled=True)
#     async def menu1button16(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="menu1button17",row=3, disabled=True)
#     async def menu1button17(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.downarrow}", custom_id="menu1button18",disabled=True,row=3)#DOWNARROW
#     async def downarrow(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="menu1button19",row=3, disabled=True)#data
#     async def menu1button19(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.confirmed}", custom_id="menu1button20",row=3, disabled=True)#magicwand
#     async def menu1button20(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="menu1button21",row=4, disabled=True)#data
#     async def menu1button21(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.question}", custom_id="menu1button22",row=4, disabled=True)#pins
#     async def menu1button22(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.alert}", custom_id="menu1button23",row=4, disabled=True)#alert
#     async def menu1button23(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.purpleslash}", custom_id="menu1button24",row=4, disabled=True)#sectorrotation
#     async def menu1button24(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="menu1button25",row=4, disabled=True)#data
#     async def linkbutton25(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())



# class AlertStart(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)




       
    

#     @disnake.ui.button(style=disnake.ButtonStyle.red,emoji=f"{emojis.movingchart}", custom_id="alert1button1",disabled=True,row=0)#datachart
#     async def alert1button1(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = AlertsEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.tools}", custom_id="alert1button2",row=0,disabled=True)#tools
#     async def alert1button2(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = AlertsEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.confirmed}", custom_id="alert1button3",row=0,disabled=True)#servermenu
#     async def menu(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=MenuStart(), embed = AlertsEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.book}", custom_id="alert1button4",row=0,disabled=True)#citedworks
#     async def alert1button4(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = AlertsEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.movingchart}", custom_id="alert1button5",disabled=True)#datachart
#     async def alert1button5(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = AlertsEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.confirmed}", custom_id="alert1button6",row=1,disabled=True)#botcommands
#     async def alert1button6(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(embed = AlertsEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.movingchart}", custom_id="alert1button7",disabled=True,row=1)#datachart
#     async def alert1button7(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = AlertsEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji=f"{emojis.downarrow}", custom_id="alert1button8", disabled=True,row=1)#arrowup
#     async def alert1button8(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = AlertsEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.movingchart}", custom_id="alert1button9",disabled=True,row=1)#datachart
#     async def alert1button9(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = AlertsEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.worldwide}", custom_id="alert1button10",row=1,disabled=True)#news
#     async def alert1button10(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = AlertsEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.links}", custom_id="alert1button11",row=2,disabled=True)#links
#     async def alert1button11(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = AlertsEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji=f"{emojis.rightarrow}", custom_id="alert1button12", disabled=True,row=2) #arrowleft
#     async def alert1button12(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = AlertsEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.rssfeeds}", custom_id="pager1button13",row=2)#fudstop core
#     async def alert1button13(self,button: disnake.ui.Button, inter: disnake.AppCmdInter):
        

#         embeds = [
#          disnake.Embed(title="Real-Time<a:_:1043215920484581447>Play Alerts", description="```py\nThe real time alerts provided by trady-tics can be a very good way to earn some easy money. \n\n WHEN TRADING THE ALERTS: GO IN THE MONEY. They often recommend OTM strikes - but I have found with experience that if you play these alerts ITM, you'll see a much higher success rate.```", color=disnake.Colour.random()),
#          disnake.Embed(title="Analyst<a:_:1043215920484581447>Upgrades", description="```py\nWHEN TRADING THE ALERTS: **GO IN THE MONEY**. They often recommend OTM strikes - but I have found with experience that if you play these alerts ITM, you'll see a much higher success rate.```", color=disnake.Colour.random()),
#          disnake.Embed(title="Bullseye<a:_:1043215920484581447>Alerts", description="```py\n\n WHEN TRADING THE ALERTS: **GO IN THE MONEY**. They often recommend OTM strikes - but I have found with experience that if you play these alerts ITM, you'll see a much higher success rate.```", color=disnake.Colour.random()),
#          disnake.Embed(title="Crypto<a:_:1043215920484581447>Alerts", description="```py\n\n WHEN TRADING THE ALERTS: **GO IN THE MONEY**. They often recommend OTM strikes - but I have found with experience that if you play these alerts ITM, you'll see a much higher success rate.```", color=disnake.Colour.random()),
#          disnake.Embed(title="Important<a:_:1043215920484581447>News", description="```py\n\n WHEN TRADING THE ALERTS: **GO IN THE MONEY**. They often recommend OTM strikes - but I have found with experience that if you play these alerts ITM, you'll see a much higher success rate.```", color=disnake.Colour.random()),
#          disnake.Embed(title="Insider<a:_:1043215920484581447>Trades", description="```py\n\n WHEN TRADING THE ALERTS: **GO IN THE MONEY**. They often recommend OTM strikes - but I have found with experience that if you play these alerts ITM, you'll see a much higher success rate.```", color=disnake.Colour.random()),
#          disnake.Embed(title="Options<a:_:1043215920484581447>Sweeps", description="```py\n\n WHEN TRADING THE ALERTS: **GO IN THE MONEY**. They often recommend OTM strikes - but I have found with experience that if you play these alerts ITM, you'll see a much higher success rate.```", color=disnake.Colour.random()),
#          disnake.Embed(title="Scalps<a:_:1043215920484581447>", description="```py\n\n WHEN TRADING THE ALERTS: **GO IN THE MONEY**. They often recommend OTM strikes - but I have found with experience that if you play these alerts ITM, you'll see a much higher success rate.```", color=disnake.Colour.random()),
#          disnake.Embed(title="Social<a:_:1043215920484581447>Spike", description="```py\n\n WHEN TRADING THE ALERTS: **GO IN THE MONEY**. They often recommend OTM strikes - but I have found with experience that if you play these alerts ITM, you'll see a much higher success rate.```", color=disnake.Colour.random()),
#          disnake.Embed(title="Stock<a:_:1043215920484581447>Breakouts", description="```py\n\n WHEN TRADING THE ALERTS: **GO IN THE MONEY**. They often recommend OTM strikes - but I have found with experience that if you play these alerts ITM, you'll see a much higher success rate.```", color=disnake.Colour.random()),
#          disnake.Embed(title="Trady<a:_:1043215920484581447>Flow", description="```py\n WHEN TRADING THE ALERTS: **GO IN THE MONEY**. They often recommend OTM strikes - but I have found with experience that if you play these alerts ITM, you'll see a much higher success rate.```", color=disnake.Colour.random()),]

#         options = [
#          disnake.SelectOption(label="AnalystUpgrades",value=1, description="If you play these alerts ITM, you'll see a much higher success rate.", emoji=f"{emojis.rssfeeds}"),
#          disnake.SelectOption(label="BullseyeAlerts",value=2, description="THE BEST ALERT BY FAR", emoji=f"{emojis.rssfeeds}"),
#          disnake.SelectOption(label="CryptoAlerts",value=3, description="WHEN TRADING THE ALERTS: ITM, you'll see a much higher success rate.", emoji=f"{emojis.rssfeeds}"),
#          disnake.SelectOption(label="ImportantNews",value=4, description="Important News Updates from TradyTics", emoji=f"{emojis.rssfeeds}"),
#          disnake.SelectOption(label="InsiderTrades",value=5, description="Insider Trades", emoji=f"{emojis.rssfeeds}"),
#          disnake.SelectOption(label="OptionsSweeps",value=6, description="WHEN TRADING THE ALERTS: ITM, you'll see a much higher success rate.", emoji=f"{emojis.rssfeeds}"),
#          disnake.SelectOption(label="Scalps",value=7, description="If you play these alerts ITM, you'll see a much higher success rate.", emoji=f"{emojis.rssfeeds}"),
#          disnake.SelectOption(label="SocialSpike",value=8, description="ALSO A GREAT ALERT FOR SOCIAL SENTIMENT!", emoji=f"{emojis.rssfeeds}"),
#          disnake.SelectOption(label="StockBreakouts",value=9, description="\nIf you play these alerts ITM, you'll see a much higher success rate.", emoji=f"{emojis.rssfeeds}"),
#          disnake.SelectOption(label="TradyFlow",value=10, description="If you play these alerts ITM, you'll see a much higher success rate.", emoji=f"{emojis.rssfeeds}"),]

#         await inter.response.edit_message(view=LitStart())
#         await inter.send(embed=AlertsEmbed(), view=AlertMenus(embeds,options), ephemeral=False)

#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji=f"{emojis.leftarrow}", custom_id="alert1button14", disabled=True,row=2)#arrowright
#     async def alert1button14(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = AlertsEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji="<a:_:1042806896555474974>", custom_id="alert1button15",row=2,disabled=True)#diamond
#     async def alert1button15(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = AlertsEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.video}", custom_id="alert1button16",row=3,disabled=True)#videos
#     async def alert1button16(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = AlertsEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.movingchart}", custom_id="alert1button17",disabled=True,row=3)#datachart
#     async def alert1button17(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = AlertsEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji=f"{emojis.uparrow}", custom_id="alert1button18",disabled=True,row=3)#arrowdown
#     async def alert1button18(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = AlertsEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.movingchart}", custom_id="alert1button19",disabled=True,row=3)#datachart
#     async def alert1button19(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = AlertsEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.confirmed}", custom_id="alert1button20",row=3,disabled=True)#magicwand
#     async def alert1button20(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = AlertsEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.movingchart}", custom_id="alert1button21",disabled=True,row=4)#datachart
#     async def alert1button21(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = AlertsEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji=f"{emojis.question}", custom_id="alert1button22",row=4,disabled=False)#pins
#     async def alert1button22(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=HelpStart(), embed=HelpStart().embed)


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.alert}", custom_id="alert1button23",row=4,disabled=True)#alert!
#     async def alert1button23(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AlertStart(), embed = AlertsEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.purpleslash}", custom_id="alert1button24",row=4,disabled=True)
#     async def alert1button24(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = AlertsEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.movingchart}", custom_id="alert1button25",disabled=True,row=4)#datachart
#     async def linkbutton25(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())


# class HelpEmbed(disnake.Embed):
#     def __init__(self):
#         super().__init__(title=f"{emojis.lf}{emojis.lu}{emojis.ld}{emojis.ls}{emojis.lt}{emojis.lo}{emojis.lp}", description=f"```py\nTutorial!\n\nAll information gathered from this command is from the industry, government agencies, or cited sources. This is designed to be an all-in-one resource tool for all of your market needs.```", color=disnake.Colour.dark_gold())

#         self.add_field(name=f"Start Tutorial:", value=f"```py\nYou'll be interacting with Drop-down menus and buttons and the design has been intuitively set-up. Buttons that are not lit-up is by design to not overload the user. To start - click the only available button below to begin the tutorial.```")

# class HelpStart(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)




#         self.embed = disnake.Embed(title=f"{emojis.question} Need Help? {emojis.question}", description=f"```py\nWith so many areas of finance to learn - I've struggled with figuring out a way to constantly keep everyone in the loop as far as market finance, current events, FUD vs NON FUD, news analysis, core logic, discord help, discord commands, discord settings - etc - it's A LOT.\nThat being said - this is the solution.```", color=disnake.Colour.dark_red())
#         self.embed.add_field(name="Arrows", value="```py\nThe arrow buttons are for switching between sections of the  All of this is live and real-time data and will update every time content is accessed.```",inline=False)
#         self.embed.add_field(name="Buttons", value=f"```py\nButtons will be displayed intuitively. If arrows aren't lit-up - that's by design to prevent over crowding the user's vision. Buttons will initially display Blurple, and will change to red when accessed.``` ```py\nTry it on this page by clicking``` {emojis.greenfire}. ```py\nThen - click the``` {emojis.confirmed} ```py\nicon to return to where you started.```",inline=False)
#         self.embed.set_footer(text=f"Implemented by FUDstop.")
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,emoji=f"{emojis.lh}", custom_id="helpnbutton1",row=0, disabled=True)#data
#     async def helpnbutton1(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.le}", custom_id="helpnbutton2",row=0, disabled=True)#tools
#     async def helpnbutton2(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.ll}", custom_id="helpnbutton3",row=0, disabled=True)#check
#     async def helpnbutton3(self, bug: str, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.lp}", custom_id="helpnbutton4",row=0, disabled=True)#citedworks
#     async def helpnbutton4(self, button: disnake.ui.Button, inter: disnake.AppCommandInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="helpnbutton5",row=0, disabled=True)#data
#     async def helpnbutton5(self, button: disnake.ui.Button, inter: disnake.AppCommandInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.lm}", custom_id="helpnbutton6",row=1, disabled=True)#botcommands
#     async def helpnbutton6(self, button: disnake.ui.Button, inter: disnake.AppCommandInter):
#         await inter.response.edit_message(view=None)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.le}", custom_id="helpnbutton7",row=1, disabled=True)
#     async def helpnbutton7(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.ln}", custom_id="helpnbutton8", disabled=True,row=1)
#     async def helpnbutton8(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.lu}", custom_id="helpnbutton9",row=1, disabled=True)
#     async def helpnbutton9(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="helpnbutton10",row=1, disabled=True)
#     async def helpnbutton10(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())



#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="helpnbutton11",row=2, disabled=True)#botcommands
#     async def helpnbutton11(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=None)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="helpnbutton12",row=2, disabled=True)
#     async def helpnbutton12(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="helpnbutton13", disabled=True,row=2)
#     async def helpnbutton13(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         self.helpnbutton13.disabled = True
#         self.helpnbutton18.disabled=False
#         self.helpnbutton15.style = disnake.ButtonStyle.green
#         self.helpnbutton18.emoji = f"{emojis.important}"
#         self.helpnbutton18.style = disnake.ButtonStyle.green

#         await inter.response.edit_message(view=self)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="helpnbutton14",row=2, disabled=True)
#     async def helpnbutton14(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.rightarrow}", custom_id="helpnbutton15",row=2, disabled=False)
#     async def helpnbutton15(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         self.embed.clear_fields()
       
#         self.helpnbutton15.emoji= f"{emojis.movingchart}"
#         self.helpnbutton15.disabled=True
#         self.linkbutton25.disabled=False
#         self.linkbutton25.emoji= f"{emojis.greenfire}"
#         await inter.response.edit_message(view=self,embed=HelpStart().embed)


    

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.download}", custom_id="helpnbutton16",row=3, disabled=True)
#     async def helpnbutton16(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):

#         self.add_item(BotCmdMenu())
#         embed = disnake.Embed(title=f"Dropdown Menus", description=f"```py\nWhile navigating the APP - you can utilize the drop-down menus for very convenient referencing for mobile users. The rich-embedded content is perfect for quick analysis of plays or if trying to learn bot commands.```", color=disnake.Colour.dark_orange())
#         embed.add_field(name=f"{emojis.downtrend_arrow}", value="```py\nClick the drop-down menu here to see an example.```")
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.download}", custom_id="helpnbutton17",row=3, disabled=True)
#     async def helpnbutton17(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.download}", custom_id="helpnbutton18",disabled=True,row=3)#DOWNARROW
#     async def helpnbutton18(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         self.remove_item(self.helpnbutton21)
#         self.remove_item(self.helpnbutton22)
#         self.remove_item(self.helpnbutton23)
#         self.remove_item(self.helpnbutton24)
#         self.remove_item(self.linkbutton25)
#         self.remove_item(self.helpnbutton16)
#         self.remove_item(self.helpnbutton17)
#         self.remove_item(self.helpnbutton18)
#         self.remove_item(self.helpnbutton19)
#         self.remove_item(self.helpnbutton20)
#         self.add_item(BotCmdMenu())
#         self.add_item(HighShortsViewStart().select)
#         embed = disnake.Embed(title=f"Dropdown Menus", description=f"```py\nWhile navigating the APP - you can utilize the drop-down menus for very convenient referencing for mobile users. The rich-embedded content is perfect for quick analysis of plays or if trying to learn bot commands.```", color=disnake.Colour.dark_orange())
#         embed.add_field(name=f"{emojis.downarrow}", value="```py\nClick the drop-down menu here to see an example of what the command menu as well as what a data menu for options looks like. You can select any bot commands to have the full list printed to discord.```")
#         embed.add_field(name=f"{emojis.fail}", value="```py\nReturn to main menu.```")
#         embed.add_field(name=f"{emojis.rightarrow}", value="```py\nStart Tutorial Over.```")
#         self.helpnbutton5.disabled=False
#         self.helpnbutton15.disabled=False
#         self.helpnbutton5.emoji = f"{emojis.fail}"
#         self.helpnbutton5.callback = lambda interaction: interaction.response.edit_message(view=LitStart(), embed=MainEmbedAPP())
#         self.helpnbutton15.callback = lambda interaction: interaction.response.edit_message(view=HelpStart(), embed=HelpEmbed())
#         await inter.response.edit_message(view=self, embed=embed)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.download}", custom_id="helpnbutton19",row=3, disabled=True)#data
#     async def helpnbutton19(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.download}", custom_id="helpnbutton20",row=3, disabled=True)#magicwand
#     async def helpnbutton20(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.download}", custom_id="helpnbutton21",row=4, disabled=True)#data
#     async def helpnbutton21(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.download}", custom_id="helpnbutton22",row=4, disabled=True)#pins
#     async def helpnbutton22(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.download}", custom_id="helpnbutton23",row=4, disabled=True)#alert
#     async def helpnbutton23(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.download}", custom_id="helpnbutton24",row=4, disabled=True)#sectorrotation
#     async def helpnbutton24(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.download}", custom_id="helpnbutton25",row=4, disabled=True)#data
#     async def linkbutton25(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         embed = disnake.Embed(title=f"{emojis.confirmed}", description=f"```py\nbuttons will return you back to main pages.```")
#         embed.add_field(name="Let me know your feedback!", value=f"```py\nThis should be a very beneficial tool. All feedback is welcome.``` ** Click the** {emojis.important} **emoji for an example drop-down menu tutorial.**")
#         self.linkbutton25.disabled=True

#         self.helpnbutton13.disabled = False

#         self.helpnbutton15.emoji = f"{emojis.rightarrow}"
#         self.helpnbutton13.emoji = f"{emojis.confirmed}"
#         self.helpnbutton13.style = disnake.ButtonStyle.blurple
#         await inter.response.edit_message(view=self,embed=embed)



# class ToolsDrop(disnake.ui.Select):
#     def __init__(self):
#         super().__init__( 

#         placeholder="Trader Tools",
#         min_values=1,
#         max_values=1,
#         custom_id="toolsdrop",
#         options = [ 
#         disnake.SelectOption(label="Black Scholes Calculator",value=1, description="Learn how to price your options contracts by using the Black Scholes Calculator", emoji=f"{emojis.tools}"),
#         disnake.SelectOption(label="Difference Checker",value=2,description="Want to compare documents side by side? See what's changed by utilizing the Difference Checker.", emoji=f"{emojis.tools}"),
#         disnake.SelectOption(label="Gitmind Mind Maps",value=3,description="Down a rabbit hole? Use Gitmind to make custom mind-maps.", emoji=f"{emojis.tools}"),
#         disnake.SelectOption(label="Market Maker Signals",value=4,description="Learn the market maker signals which happen on the level 2 order book.", emoji=f"{emojis.tools}"),
#         disnake.SelectOption(label="Mention Map",value=5,description="Mention Map allows you to see connections based on retweets / mentions.",emoji=f"{emojis.tools}"),
#         disnake.SelectOption(label="Option Strategy Creator",value=6,description="This is an amazing tool that helps you build option strategies and view the P/L charts.", emoji=f"{emojis.tools}"),
#         disnake.SelectOption(label="Options Profit Calculator",value=7, description="Use this tool to help guage your potential profit for a trade.", emoji=f"{emojis.tools}"),
#         disnake.SelectOption(label="SEC Interactive FTD Chart", value=8, description="Use this chart to visualize FTDs as they are released from SEC.GOV.", emoji=f"{emojis.tools}"),
#         disnake.SelectOption(label="Social Blade",value=9,description="Social Blade is a great tool to see YouTubers and Twitter Personalities' ad revenue.", emoji=f"{emojis.tools}"),
#         disnake.SelectOption(label="Social Grep",value=10, description="Scrape and Export Reddit Data from any subreddit to guage psyop levels.", emoji=f"{emojis.tools}"),
#         disnake.SelectOption(label="Subreddit Stats",value=11, description="Compare subreddits, view top comments, posts, and guage authenticity with this tool.", emoji=f"{emojis.tools}"),])


#     async def callback(self, interaction: disnake.MessageCommandInteraction):
#         if self.values[0] == "1":
#             await interaction.send("https://www.optionseducation.org/toolsoptionquotes/optionscalculator", ephemeral=False)
#         elif self.values[0] == "2":
#             await interaction.send("https://www.diffchecker.com/", ephemeral=False)
#         elif self.values[0] == "3":
#             await interaction.send("https://gitmind.com/", ephemeral=False)
#         elif self.values[0] == "4":
#             await interaction.send("https://otc.financial/list-of-market-maker-signals/#:~:text=Market%20maker%20signals%20are%20the,of%20a%20company's%20share%20price", ephemeral=False)
#         elif self.values[0] == "5":
#             await interaction.send("https://mentionmcom/", ephemeral=False)

#         elif self.values[0] == "6":
#             await interaction.send("https://optioncreator.com/", ephemeral=False)
#         elif self.values[0] == "7":
#             await interaction.send("https://www.optionsprofitcalculator.com/", ephemeral=False)
#         elif self.values[0] == "8":
#             await interaction.send("https://sec.report/fails.php?", ephemeral=False)
#         elif self.values[0] == "9":
#             await interaction.send("https://www.socialblade.com", ephemeral=False)
#         elif self.values[0] == "10":
#             await interaction.send("https://www.socialgrep.com:", ephemeral=False)
#         elif self.values[0] == "11":
#             await interaction.send("https://www.subredditstats.com)", ephemeral=False)


# class ToolsViewStart(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)


#         self.embed = disnake.Embed(title=f"{emojis.tools} Useful Tools {emojis.tools}", description="```py\nThese tools will help in a variety of different ways. Simply select what you need.```", color=disnake.Colour.dark_gold())


#         self.add_item(ToolsDrop())
#     @disnake.ui.button(style=disnake.ButtonStyle.blurple,emoji=f"{emojis.dtcc}", custom_id="tools1button1",disabled=False,row=0)#datachart
#     async def tools1button1(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):


#         await inter.response.edit_message(view=DTCCViewStart(), embed=ToolsEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.uptrend}", custom_id="tools1button2",row=0,disabled=True)#1
#     async def tools1button2(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.sec}", custom_id="tools1button3",row=0,disabled=False)#2
#     async def menu(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=ToolsViewStart(), embed=ToolsViewStart().embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.uptrend}", custom_id="tools1button4",row=0,disabled=True)#3
#     async def tools1button4(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.finrawhite}", custom_id="tools1button5",disabled=False, row=0)#datachart
#     async def tools1button5(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=ToolsViewStart(), embed=ToolsViewStart().embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.uptrend}", custom_id="tools1button6",row=1,disabled=True)#4
#     async def tools1button6(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = ToolsEmbed)


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.nyse}", custom_id="tools1button7",disabled=False,row=1)#datachart
#     async def tools1button7(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=NYSEViewStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji=f"{emojis.confirmed}", custom_id="tools1button8", disabled=False,row=1)#arrowup
#     async def tools1button8(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.fed}", custom_id="tools1button9",disabled=False,row=1)#datachart
#     async def tools1button9(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.uptrend}", custom_id="tools1button10",row=1,disabled=True)#5
#     async def tools1button10(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.occ}", custom_id="tools1button11",row=3,disabled=False)#6
#     async def tools1button11(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=ToolsViewStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="tools1button12", disabled=True,row=3) #arrowleft
#     async def tools1button12(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.stock}", custom_id="pager1button13",row=3, disabled=False)#fudstop core
#     async def tools1button13(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        

#         await inter.response.edit_message(view=OFRViewStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="tools1button14", disabled=True,row=3)#arrowright
#     async def tools1button14(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji="<:_:1046522227790716968>", custom_id="tools1button15",row=3,disabled=False)#7
#     async def tools1button15(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=CBOEViewStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.lt}", custom_id="tools1button16",row=4,disabled=True)#8
#     async def tools1button16(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.lo}", custom_id="tools1button17",disabled=True,row=4)#datachart
#     async def tools1button17(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.lo}", custom_id="tools1button18",disabled=True,row=4)#arrowdown
#     async def tools1button18(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.ll}", custom_id="tools1button19",disabled=True,row=4)#datachart
#     async def tools1button19(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.ls}", custom_id="tools1button20",row=4,disabled=True)#9
#     async def tools1button20(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())





# class TAStart(disnake.ui.View):
#     def __init__(self):
#         super().__init__(
#             timeout=None
#         )


#         self.add_item(TechDropdown())
#         self.add_item(TechDropdown2())



#     @disnake.ui.button(style=disnake.ButtonStyle.blurple,emoji=f"{emojis.movingchart}", custom_id="ta1button1",row=0,disabled=True)#data
#     async def ta1button1(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.tools}", custom_id="ta1button2",row=0,disabled=True)#tools
#     async def ta1button2(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.confirmed}", custom_id="ta1button3",row=0,disabled=True)#check
#     async def ta1button3(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji=f"{emojis.book}", custom_id="ta1button4",row=0,disabled=True)#citedworks
#     async def ta1button4(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=self)
#         await inter.send("You're already in on this section, dad!")

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="ta1button5",row=0,disabled=True)#data
#     async def ta1button5(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())

    


    

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.video}", custom_id="ta1button11",row=3,disabled=True)
#     async def ta1button16(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="ta1button12",row=3,disabled=True)
#     async def ta1button17(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji=f"{emojis.downarrow}", custom_id="ta1button13",disabled=False,row=3)#DOWNARROW
#     async def downarrow(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed=MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="ta1button14",row=3,disabled=True)#data
#     async def ta1button19(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.confirmed}", custom_id="ta1button15",row=3,disabled=True)#magicwand
#     async def ta1button20(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="ta1button21",row=4,disabled=True)#data
#     async def ta1button21(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.question}", custom_id="ta1button22",row=4,disabled=True)#pins
#     async def ta1button22(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.alert}", custom_id="ta1button23",row=4,disabled=True)#alert
#     async def ta1button23(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AlertStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.purpleslash}", custom_id="ta1button24",row=4,disabled=True)#sectorrotation
#     async def ta1button24(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movingchart}", custom_id="ta1button25",row=4,disabled=True)#data
#     async def linkbutton25(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())


# class MarketsEmbed(disnake.Embed):
#     def __init__(self):
#         super().__init__(title=f"<a:_:1043679047617622078> Tools",description="```py\nThis is the market data section. View today's top gainers / losers / forex gainers /etf gainers / top movers / high shorts with low float / high FTDs, and more.```", color=disnake.Colour.dark_orange())

#         self.add_field(name=f"{emojis.greenfire}",value="```py\nTop Gainers```")
#         self.add_field(name=f"{emojis.redfire}",value="```py\nTop Losers```")
#         self.add_field(name=f"{emojis.btcemoji}",value="```py\nCrypto Markets```")
#         self.add_field(name=f"{emojis.economy}",value="```py\nForex```")
#         self.add_field(name=f"{emojis.movers}",value="```py\nTop Movers```")
#         self.add_field(name=f"{emojis.chains}",value="```py\nTop ETFs```")
#         self.add_field(name=f"{emojis.lightboltneon}",value="```py\nTop Options```")
#         self.add_field(name=f"{emojis.pants}",value="```py\nHigh Shorts```")
#         self.add_field(name=f"{emojis.clockspin}",value="```py\nHigh FTDs```")
#         self.add_field(name=f"{emojis.float}",value="```py\nLow Float```")
#         self.add_field(name=f"{emojis.downarrow}", value="```py\nReturn to Main```", inline=False)

#         self.set_footer(text="Implemented by FUDstop")

    
# class FTDsEmbed(disnake.Embed):
#     def __init__(self):
#         super().__init__( 
#             title=f"{emojis.clockspin} Fails to Deliver with T+35 Dates {emojis.clockspin}", description=f"```py\nView the top tickers with the highest amounts of Failures to Deliver. Each result will have a T-35 settlement date. These can provide for some lucrative opportunities. For example - AMC showed up on this list just before its' last run!```",
#             color = disnake.Colour.dark_teal(),

#         )

#         self.add_field(name=f"{emojis.downarrow}", value="```py\nReturn to main page.```")
#         self.add_field(name=f"{emojis.uparrow}", value="```py\nReturn to market data page.```")



    
# class ForexEmbed(disnake.Embed):
#     def __init__(self):
#         super().__init__( 
#             title=f"{emojis.economy} Live forex! {emojis.economy}", description=f"```py\nView real-time forex!```",
#             color = disnake.Colour.dark_gold(),

#         )

#         self.add_field(name=f"{emojis.confirmed}", value="```py\nReturn to main page.```")
#         self.add_field(name=f"{emojis.downarrow}", value="```py\nReturn to market data page.```")


# class TopOptionsViewStart(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)


    
#         self.select = disnake.ui.Select(  
#         placeholder="🇴 🇵 🇹 🇮 🇴 🇳 🇸  ⬇️  🇲 🇪 🇳 🇺",
#         min_values=1,
#         max_values=1,
#         custom_id="topoptionsdropview",
#         options = [ 
#             disnake.SelectOption(label="Top Total Overall Open Interest", description="View the top 25 tickers with the most open contracts.", emoji=f"{emojis.crown}"),
#             disnake.SelectOption(label="Top Total Overall Volume", description="View the top 25 tickers with the most overall volume across all options.", emoji=f"{emojis.uptrend}"),
#             disnake.SelectOption(label="Top Open Interest Contracts", description="View the top 25 contracts currently trading with the most open interest.", emoji=f"{emojis.madbear}"),
#             disnake.SelectOption(label="Top Volume Contracts", description="View the top 25 contracts currently trading with the highest volume.", emoji=f"{emojis.moneytower}"),
#             disnake.SelectOption(label="Top Open Interest Increase", description="View the top 25 contracts with the most Open Interest increase.", emoji=f"{emojis.shield}"),
#             disnake.SelectOption(label="Top Open Interest Decrease", description="View the top 25 contracts with the most Open Interest decrease.", emoji=f"{emojis.sword}"),
#             disnake.SelectOption(label="Top Implied Volatility", description="View the top 25 contracts with the highest implied volatility.", emoji=f"{emojis.needle}"),
#             disnake.SelectOption(label="Top Turnover", description="View the top 25 contracts that have traded hands today.", emoji=f"{emojis.turnover}"),
#             disnake.SelectOption(label="Return to Main Menu",emoji=f"{emojis.turnover}"),

#         ]
#     )
#         self.add_item(self.select)
#         self.select.callback = lambda interaction: interaction.response.edit_message(view=TopOptionsViewStart())
#     @disnake.ui.button(style=disnake.ButtonStyle.blurple,emoji=f"{emojis.uptrend}", custom_id="topopts1button1",disabled=False,row=0)#datachart
#     async def topopts1button1(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=TotalVolumeViewStart(), embed=TotalVolumeViewStart().embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="topopts1button2",row=0,disabled=True)#ftds
#     async def topopts1button2(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(embed = GainersViewStart().embed, view=GainersViewStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.confirmed}", custom_id="topopts1button3", disabled=False,row=0)#arrow
#     async def topopts1button8(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(embed=MarketsEmbed(), view=MarketsView())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="topopts1button4",row=0,disabled=True)#toplosers
#     async def topopts1button4(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LosersViewStart(), embed=LosersViewStart().embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.crown}", custom_id="topopts1button5",disabled=False)#datachart
#     async def topopts1button5(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=TotalOIViewStart(), embed = TotalOIViewStart().embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="topopts1button6",row=1,disabled=True)#ye
#     async def topopts1button6(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=CryptoViewStart(),embed= CryptoEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.needle}", custom_id="topopts1button7",disabled=False,row=1)#datachart
#     async def topopts1button7(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=TopIVViewStart(), embed=TopIVViewStart().em)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="topopts1button8",row=1,disabled=True)#data
#     async def menu(self,button: disnake.ui.Button,inter:disnake.AppCmdInter):
        

#         await inter.response.edit_message(embed=ActiveViewStart().embed, view=ActiveViewStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.turnover}", custom_id="topopts1button9",disabled=False,row=1)#datachart
#     async def topopts1button9(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=TotalTurnoverViewStart(), embed=TotalTurnoverViewStart().embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="topopts1button10",row=1,disabled=True)#news
#     async def topopts1button10(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=ForexViewStart(), embed = ForexEmbed())


  


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.madbear}", custom_id="topopts1button16",row=3,disabled=False)#topETFs
#     async def topopts1button16(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=TopOIViewStart(), embed=TopOIViewStart().em)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="topopts1button17",disabled=True,row=3)#datachart
#     async def topopts1button17(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.lightboltneon}", custom_id="topopts1button18",row=3,disabled=True)#alert!
#     async def topopts1button23(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(embed =TotalOIViewStart().embed, view=TotalOIViewStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="topopts1button19",disabled=True,row=3)#datachart
#     async def topopts1button19(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.moneytower}", custom_id="topopts1button20",row=3,disabled=False)#forrex
#     async def topopts1button20(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=TopVolumeViewStart(), embed=TopVolumeViewStart().em)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="topopts1button21",disabled=True,row=4)#datachart
#     async def topopts1button21(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.sword}", custom_id="topopts1button22",row=4,disabled=False)#pins
#     async def topopts1button22(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=TopOIDownViewStart(), embed=TopOIDownViewStart().em)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="topopts1button23",disabled=True,row=4)#arrow
#     async def topopts1button18(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=MarketsView(), embed = MarketsEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.shield}", custom_id="topopts1button24",row=4,disabled=False)
#     async def topopts1button24(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=TopOIUpViewStart(), embed=TopOIUpViewStart().em)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.download}", custom_id="topopts1button25",disabled=True,row=4)#datachart
#     async def linkbutton25(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=MarketsView())


# class MarketsDrop(disnake.ui.Select):
#     def __init__(self):
#         super().__init__( 
#             placeholder="🇩 🇦 🇹 🇦  🗾 🇲 🇪 🇳 🇺",
#             min_values=1,
#             max_values=1,
#             custom_id="marketsdropper",
#             options = [ 
#                 disnake.SelectOption(label="Top Gainers", description="View top gainers on the day. Updates every time the button is clicked.", emoji=f"{emojis.greenfire}"),
#                 disnake.SelectOption(label="Top Losers", description="View top gainers on the day. Updates every time the button is clicked.", emoji=f"{emojis.redfire}"),
#                 disnake.SelectOption(label="Crypto Markets", description="View several cryptocurrencies that update each time button is clicked.", emoji=f"{emojis.btcemoji}"),
#                 disnake.SelectOption(label="Forex Market", description="View the forex markets in real time.", emoji=f"{emojis.economy}"),
#                 disnake.SelectOption(label="Top Movers", description="View the most active tickers on the day.", emoji=f"{emojis.movers}"),
#                 disnake.SelectOption(label="Top ETFs", description="View the top ETFs on the day.", emoji=f"{emojis.chains}"),
#                 disnake.SelectOption(label="Top Options", description="View top Open interest change / highest volume / most active contracts & more.", emoji=f"{emojis.lightboltneon}"),
#                 disnake.SelectOption(label="High Shorts", description="View tickers with high levels of short interest.", emoji=f"{emojis.pants}"),
#                 disnake.SelectOption(label="High FTDs", description="View tickers with high FTDs + the T35 settlement dates.", emoji=f"{emojis.clockspin}"),
#                 disnake.SelectOption(label="Low Float", description="View tickers with the lowest free floats.", emoji=f"{emojis.float}"),

#             ]
#         )

#     async def callback(self, interaction:disnake.MessageCommandInteraction):
#         if self.values[0] == "Top Gainers":
#             await interaction.response.edit_message(view=GainersViewStart(), embed=GainersViewStart().embed)
#         elif self.values[0] == "Top Losers":
#             await interaction.response.edit_message(view=LosersViewStart(), embed=LosersViewStart().embed)
#         elif self.values[0] == "Crypto Markets":
#             await interaction.response.edit_message(view=CryptoViewStart(), embed=CryptoEmbed())

#         elif self.values[0] == "Forex Markets":
#             await interaction.response.edit_message(view=ForexViewStart(),  embed=ForexEmbed())

#         elif self.values[0] == "Top Movers":
#             await interaction.response.edit_message(view=ActiveViewStart(), embed=ActiveViewStart().embed)

#         elif self.values[0] == "Top ETFs":
#             await interaction.response.edit_message(view=ETFsViewStart(), embed=ETFsViewStart().embed)



#         elif self.values[0] == "Top Options":
#             await interaction.response.edit_message(view=TopOptionsViewStart())



#         elif self.values[0] == "High FTDs":
#             await interaction.response.edit_message(view=FTDViewStart())

#         elif self.values[0] == "High Shorts":
#             await interaction.response.edit_message(view=HighShortsViewStart())

#         elif self.values[0] == "Low Float":
#             await interaction.response.edit_message(view=LowFloatDropdown())


# class MarketsView(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)

#         self.add_item(MarketsDrop())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey,emoji=f"{emojis.movingchart}", custom_id="markets1button1",disabled=True,row=0)#datachart
#     async def markets1button1(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.greenfire}", custom_id="markets1button2",row=0,disabled=False)#ftds
#     async def markets1button2(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=GainersViewStart(), embed = MarketsEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji=f"{emojis.downarrow}", custom_id="markets1button3", disabled=False,row=0)#arrow
#     async def markets1button8(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.redfire}", custom_id="markets1button4",row=0,disabled=False)#toplosers
#     async def markets1button4(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LosersViewStart(), embed=LosersViewStart().embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="markets1button5",disabled=True)#datachart
#     async def markets1button5(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.btcemoji}", custom_id="markets1button6",row=1,disabled=False)#ye
#     async def markets1button6(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=CryptoViewStart(), embed=CryptoEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="markets1button7",disabled=True,row=1)#datachart
#     async def markets1button7(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.movers}", custom_id="markets1button8",row=1,disabled=False)#data
#     async def menu(self,button: disnake.ui.Button,inter:disnake.AppCmdInter):
        

#         await inter.response.edit_message(view=ActiveViewStart(), embed=ActiveViewStart().embed)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="markets1button9",disabled=True,row=1)#datachart
#     async def markets1button9(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.economy}", custom_id="markets1button10",row=1,disabled=False)#news
#     async def markets1button10(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=ForexViewStart(), embed = ForexEmbed())


  


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.chains}", custom_id="markets1button16",row=3,disabled=False)#topETFs
#     async def markets1button16(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=ETFsViewStart(), embed=ETFsViewStart().embed)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="markets1button17",disabled=True,row=3)#datachart
#     async def markets1button17(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.lightboltneon}", custom_id="markets1button18",row=3,disabled=False)#alert!
#     async def markets1button23(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=TopOptionsViewStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="markets1button19",disabled=True,row=3)#datachart
#     async def markets1button19(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.pants}", custom_id="markets1button20",row=3,disabled=False)#forrex
#     async def markets1button20(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=HighShortsViewStart(), embed=HighShortsViewStart().embed)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="markets1button21",disabled=True,row=4)#datachart
#     async def markets1button21(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.clockspin}", custom_id="markets1button22",row=4,disabled=False)#pins
#     async def markets1button22(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=FTDViewStart(), embed = FTDsEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji=f"{emojis.uparrow}", custom_id="markets1button23",disabled=True,row=4)#arrow
#     async def markets1button18(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed = MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.float}", custom_id="markets1button24",row=4,disabled=False)
#     async def markets1button24(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LowFloatDropdown(), embed = LowFloatDropdown().embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="markets1button25",disabled=True,row=4)#datachart
#     async def linkbutton25(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=MarketsView())


# class CryptoEmbed(disnake.Embed):
#     def __init__(self):
#         super().__init__( 
#             title=f"{emojis.btcemoji} Live forex! {emojis.btcemoji}", description=f"```You are now viewing over 40 crypto coins. Selecting each button will update the coin's price to the current, real-time price.``` To switch between pages - use the {emojis.leftarrow} amd {emojis.rightarrow} buttons. To return to the market menu - select the {emojis.confirmed} button.```",
#             color = disnake.Colour.dark_gold(),

#         )

#         self.add_field(name=f"{emojis.leftarrow}", value="```py\nPrevious Page.```")
#         self.add_field(name=f"{emojis.rightarrow}", value="```py\nNext Page.```")
#         self.add_field(name=f"{emojis.confirmed}", value="```py\nReturn to the main market menu.```")

# class CryptoViewStart(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="sfm", label="sfm", emoji="<a:_:1043215920484581447>")
#     async def sfmusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         r = requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950191481&includeSecu=1&includeQuote=1&more=1").json()
#         changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#         high = r['high']
#         low = r['low']
#         price = r['close']
#         sym = r['symbol']
#         name = r['name']
#         embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```")
#         embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#         embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#         embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#         embed.add_field(name=f"Navigation:", value=f"```py\nPrevious Page:``` {emojis.leftarrow} ```py\nNext Page:``` {emojis.rightarrow} ```py\nReturn to Market Menu:``` {emojis.confirmed}", inline=False)
#         await interaction.response.edit_message(embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="xrp", emoji="<a:_:1043215920484581447>")
#     async def xrpusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         r = requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=925409426&includeSecu=1&includeQuote=1&more=1").json()
#         changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#         high = r['high']
#         low = r['low']
#         price = r['close']
#         sym = r['symbol']
#         name = r['name']
#         embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```")
#         embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#         embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#         embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#         embed.add_field(name=f"Navigation:", value=f"```py\nPrevious Page:``` {emojis.leftarrow} ```py\nNext Page:``` {emojis.rightarrow} ```py\nReturn to Market Menu:``` {emojis.confirmed}", inline=False)
#         await interaction.response.edit_message(embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="dot",label="dot", emoji="<a:_:1043215920484581447>")
#     async def dotusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         r = requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950185126&includeSecu=1&includeQuote=1&more=1").json()
#         changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#         high = r['high']
#         low = r['low']
#         price = r['close']
#         sym = r['symbol']
#         name = r['name']
#         embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```")
#         embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#         embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#         embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#         embed.add_field(name=f"Navigation:", value=f"```py\nPrevious Page:``` {emojis.leftarrow} ```py\nNext Page:``` {emojis.rightarrow} ```py\nReturn to Market Menu:``` {emojis.confirmed}", inline=False)
        
#         await interaction.response.edit_message(embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="vet",label="vet", emoji="<a:_:1043215920484581447>")
#     async def vetusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         r = requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950110798&includeSecu=1&includeQuote=1&more=1").json()
#         changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#         high = r['high']
#         low = r['low']
#         price = r['close']
#         sym = r['symbol']
#         name = r['name']
#         embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```")
#         embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#         embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#         embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#         embed.add_field(name=f"Navigation:", value=f"```py\nPrevious Page:``` {emojis.leftarrow} ```py\nNext Page:``` {emojis.rightarrow} ```py\nReturn to Market Menu:``` {emojis.confirmed}", inline=False)
#         await interaction.response.edit_message(embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="theta",label="theta", emoji="<a:_:1043215920484581447>")
#     async def thetausd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         r = requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950187863&includeSecu=1&includeQuote=1&more=1").json()

#         changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#         high = r['high']
#         low = r['low']
#         price = r['close']
#         sym = r['symbol']
#         name = r['name']
#         embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```")
#         embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#         embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#         embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#         embed.add_field(name=f"Navigation:", value=f"```py\nPrevious Page:``` {emojis.leftarrow} ```py\nNext Page:``` {emojis.rightarrow} ```py\nReturn to Market Menu:``` {emojis.confirmed}", inline=False)
#         await interaction.response.edit_message(embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="ksm",label="smu", emoji="<a:_:1043215920484581447>")
#     async def ksmusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         r = requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950185130&includeSecu=1&includeQuote=1&more=1").json()
#         changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#         high = r['high']
#         low = r['low']
#         price = r['close']
#         sym = r['symbol']
#         name = r['name']
#         embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```")
#         embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#         embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#         embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#         embed.add_field(name=f"Navigation:", value=f"```py\nPrevious Page:``` {emojis.leftarrow} ```py\nNext Page:``` {emojis.rightarrow} ```py\nReturn to Market Menu:``` {emojis.confirmed}", inline=False)
#         await interaction.response.edit_message(embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="xmr",label="xmr", emoji="<a:_:1043215920484581447>")
#     async def xmrusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         r = requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=925409430&includeSecu=1&includeQuote=1&more=1").json()
#         changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#         high = r['high']
#         low = r['low']
#         price = r['close']
#         sym = r['symbol']
#         name = r['name']
#         embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```")
#         embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#         embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#         embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#         embed.add_field(name=f"Navigation:", value=f"```py\nPrevious Page:``` {emojis.leftarrow} ```py\nNext Page:``` {emojis.rightarrow} ```py\nReturn to Market Menu:``` {emojis.confirmed}", inline=False)
#         await interaction.response.edit_message(embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="hbar",label="hbr", emoji="<a:_:1043215920484581447>")
#     async def hbarusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         r = requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950187866&includeSecu=1&includeQuote=1&more=1").json()
#         changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#         high = r['high']
#         low = r['low']
#         price = r['close']
#         sym = r['symbol']
#         name = r['name']
#         embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```")
#         embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#         embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#         embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#         embed.add_field(name=f"Navigation:", value=f"```py\nPrevious Page:``` {emojis.leftarrow} ```py\nNext Page:``` {emojis.rightarrow} ```py\nReturn to Market Menu:``` {emojis.confirmed}", inline=False)
#         await interaction.response.edit_message(embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="movr",label="movr", emoji="<a:_:1043215920484581447>")
#     async def movrusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         r = requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950187984&includeSecu=1&includeQuote=1&more=1").json()
#         changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#         high = r['high']
#         low = r['low']
#         price = r['close']
#         sym = r['symbol']
#         name = r['name']
#         embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```")
#         embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#         embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#         embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#         embed.add_field(name=f"Navigation:", value=f"```py\nPrevious Page:``` {emojis.leftarrow} ```py\nNext Page:``` {emojis.rightarrow} ```py\nReturn to Market Menu:``` {emojis.confirmed}", inline=False)
#         await interaction.response.edit_message(embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="flow",label="flow", emoji="<a:_:1043215920484581447>")
#     async def flowusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         r = requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950187868&includeSecu=1&includeQuote=1&more=1").json()
#         changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#         high = r['high']
#         low = r['low']
#         price = r['close']
#         sym = r['symbol']
#         name = r['name']
#         embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```")
#         embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#         embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#         embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#         embed.add_field(name=f"Navigation:", value=f"```py\nPrevious Page:``` {emojis.leftarrow} ```py\nNext Page:``` {emojis.rightarrow} ```py\nReturn to Market Menu:``` {emojis.confirmed}", inline=False)
#         await interaction.response.edit_message(embed=embed)
    
    
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="dag",label="dag", emoji="<a:_:1043215920484581447>")
#     async def dagusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         r = requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950187870&includeSecu=1&includeQuote=1&more=1").json()
#         changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#         high = r['high']
#         low = r['low']
#         price = r['close']
#         sym = r['symbol']
#         name = r['name']
#         embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```")
#         embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#         embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#         embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#         embed.add_field(name=f"Navigation:", value=f"```py\nPrevious Page:``` {emojis.leftarrow} ```py\nNext Page:``` {emojis.rightarrow} ```py\nReturn to Market Menu:``` {emojis.confirmed}", inline=False)
#         await interaction.response.edit_message(embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="kar",label="kar", emoji="<a:_:1043215920484581447>")
#     async def karusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         r = requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950187985&includeSecu=1&includeQuote=1&more=1").json()
#         changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#         high = r['high']
#         low = r['low']
#         price = r['close']
#         sym = r['symbol']
#         name = r['name']
#         embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```")
#         embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#         embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#         embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#         embed.add_field(name=f"Navigation:", value=f"```py\nPrevious Page:``` {emojis.leftarrow} ```py\nNext Page:``` {emojis.rightarrow} ```py\nReturn to Market Menu:``` {emojis.confirmed}", inline=False)
#         await interaction.response.edit_message(embed=embed)
    

    
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="dpi",label="dpi", emoji="<a:_:1043215920484581447>")
#     async def dpiusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         r = requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950187872&includeSecu=1&includeQuote=1&more=1").json()
#         changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#         high = r['high']
#         low = r['low']
#         price = r['close']
#         sym = r['symbol']
#         name = r['name']
#         embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```")
#         embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#         embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#         embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#         embed.add_field(name=f"Navigation:", value=f"```py\nPrevious Page:``` {emojis.leftarrow} ```py\nNext Page:``` {emojis.rightarrow} ```py\nReturn to Market Menu:``` {emojis.confirmed}", inline=False)
#         await interaction.response.edit_message(embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="mvi",label="mvi", emoji="<a:_:1043215920484581447>")
#     async def mviusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         r = requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950187873&includeSecu=1&includeQuote=1&more=1").json()
#         changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#         high = r['high']
#         low = r['low']
#         price = r['close']
#         sym = r['symbol']
#         name = r['name']
#         embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```")
#         embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#         embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#         embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#         embed.add_field(name=f"Navigation:", value=f"```py\nPrevious Page:``` {emojis.leftarrow} ```py\nNext Page:``` {emojis.rightarrow} ```py\nReturn to Market Menu:``` {emojis.confirmed}", inline=False)
#         await interaction.response.edit_message(embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="icp",label="icp", emoji="<a:_:1043215920484581447>")
#     async def icpusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         r = requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950192673&includeSecu=1&includeQuote=1&more=1").json()
#         changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#         high = r['high']
#         low = r['low']
#         price = r['close']
#         sym = r['symbol']
#         name = r['name']
#         embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```")
#         embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#         embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#         embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#         embed.add_field(name=f"Navigation:", value=f"```py\nPrevious Page:``` {emojis.leftarrow} ```py\nNext Page:``` {emojis.rightarrow} ```py\nReturn to Market Menu:``` {emojis.confirmed}", inline=False)
#         await interaction.response.edit_message(embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="fil",label="fil", emoji="<a:_:1043215920484581447>")
#     async def filusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         r = requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950192672&includeSecu=1&includeQuote=1&more=1").json()
#         changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#         high = r['high']
#         low = r['low']
#         price = r['close']
#         sym = r['symbol']
#         name = r['name']
#         embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```")
#         embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#         embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#         embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#         embed.add_field(name=f"Navigation:", value=f"```py\nPrevious Page:``` {emojis.leftarrow} ```py\nNext Page:``` {emojis.rightarrow} ```py\nReturn to Market Menu:``` {emojis.confirmed}", inline=False)
#         await interaction.response.edit_message(embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="amp",label="amp", emoji="<a:_:1043215920484581447>")
#     async def ampusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         r = requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950192671&includeSecu=1&includeQuote=1&more=1").json()
#         changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#         high = r['high']
#         low = r['low']
#         price = r['close']
#         sym = r['symbol']
#         name = r['name']
#         embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```")
#         embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#         embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#         embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#         embed.add_field(name=f"Navigation:", value=f"```py\nPrevious Page:``` {emojis.leftarrow} ```py\nNext Page:``` {emojis.rightarrow} ```py\nReturn to Market Menu:``` {emojis.confirmed}", inline=False)
#         await interaction.response.edit_message(embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="mkr",label="mkr", emoji="<a:_:1043215920484581447>")
#     async def mkrusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         r = requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950192468&includeSecu=1&includeQuote=1&more=1").json()
#         changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#         high = r['high']
#         low = r['low']
#         price = r['close']
#         sym = r['symbol']
#         name = r['name']
#         embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```")
#         embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#         embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#         embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#         embed.add_field(name=f"Navigation:", value=f"```py\nPrevious Page:``` {emojis.leftarrow} ```py\nNext Page:``` {emojis.rightarrow} ```py\nReturn to Market Menu:``` {emojis.confirmed}", inline=False)
#         await interaction.response.edit_message(embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="enj",label="enj", emoji="<a:_:1043215920484581447>")
#     async def enjusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         r = requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950192467&includeSecu=1&includeQuote=1&more=1").json()
#         changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#         high = r['high']
#         low = r['low']
#         price = r['close']
#         sym = r['symbol']
#         name = r['name']
#         embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```")
#         embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#         embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#         embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#         embed.add_field(name=f"Navigation:", value=f"```py\nPrevious Page:``` {emojis.leftarrow} ```py\nNext Page:``` {emojis.rightarrow} ```py\nReturn to Market Menu:``` {emojis.confirmed}", inline=False)
#         await interaction.response.edit_message(embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="comp",label="comp", emoji="<a:_:1043215920484581447>")
#     async def compusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         r = requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950192466&includeSecu=1&includeQuote=1&more=1").json()
#         changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#         high = r['high']
#         low = r['low']
#         price = r['close']
#         sym = r['symbol']
#         name = r['name']
#         embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```")
#         embed.add_field(name=f"Navigation:", value=f"```py\nPrevious Page:``` {emojis.leftarrow} ```py\nNext Page:``` {emojis.rightarrow} ```py\nReturn to Market Menu:``` {emojis.confirmed}", inline=False)
#         embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#         embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#         embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#         await interaction.response.edit_message(embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="bnt",label="bnt", emoji="<a:_:1043215920484581447>")
#     async def bntusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         r = requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950192465&includeSecu=1&includeQuote=1&more=1").json()
#         changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#         high = r['high']
#         low = r['low']
#         price = r['close']
#         sym = r['symbol']
#         name = r['name']
#         embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```")
#         embed.add_field(name=f"Navigation:", value=f"```py\nPrevious Page:``` {emojis.leftarrow} ```py\nNext Page:``` {emojis.rightarrow} ```py\nReturn to Market Menu:``` {emojis.confirmed}", inline=False)
#         embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#         embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#         embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#         await interaction.response.edit_message(embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="gala",label="gala", emoji="<a:_:1043215920484581447>")
#     async def galausd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         r = requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950192381&includeSecu=1&includeQuote=1&more=1").json()
#         changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#         high = r['high']
#         low = r['low']
#         price = r['close']
#         sym = r['symbol']
#         name = r['name']
#         embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```")
#         embed.add_field(name=f"Navigation:", value=f"```py\nPrevious Page:``` {emojis.leftarrow} ```py\nNext Page:``` {emojis.rightarrow} ```py\nReturn to Market Menu:``` {emojis.confirmed}", inline=False)
#         embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#         embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#         embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#         await interaction.response.edit_message(embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="snx",label="snx", emoji="<a:_:1043215920484581447>")
#     async def snxusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):

#         r = requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950192380&includeSecu=1&includeQuote=1&more=1").json()
#         changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#         high = r['high']
#         low = r['low']
#         price = r['close']
#         sym = r['symbol']
#         name = r['name']
#         embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```")
#         embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#         embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#         embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#         embed.add_field(name=f"Navigation:", value=f"```py\nPrevious Page:``` {emojis.leftarrow} ```py\nNext Page:``` {emojis.rightarrow} ```py\nReturn to Market Menu:``` {emojis.confirmed}", inline=False)
#         await interaction.response.edit_message(embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple,emoji=f"{emojis.confirmed}",custom_id="cryptonexter",disabled=False)
#     async def crypohome(self, button: disnake.ui.Button,interaction: disnake.MessageCommandInteraction):
#         await interaction.response.edit_message(view=LitStart(), embed=MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.red,emoji=f"{emojis.rightarrow}",custom_id="cryptwefonexter",disabled=False)
#     async def cryptoright(self, button: disnake.ui.Button,interaction: disnake.MessageCommandInteraction):
#         await interaction.response.edit_message(view=PageTwoView())



# class PageTwoView(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="chz",label="chz", emoji="<a:_:1043215920484581447>")
#     async def chzusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=925409426&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageTwoView())              
#             if counter == 35:
#                 break
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="yfi",label="yfi", emoji="<a:_:1043215920484581447>")
#     async def yfiusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950191914&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageTwoView())              
#             if counter == 35:
#                 break
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="cro",label="cro", emoji="<a:_:1043215920484581447>")
#     async def crousd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950191913&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageTwoView())              
#             if counter == 35:
#                 break
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="one",label="one", emoji="<a:_:1043215920484581447>")
#     async def oneusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950191912&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageTwoView())              
#             if counter == 35:
#                 break
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="aave",label="aave", emoji="<a:_:1043215920484581447>")
#     async def aaveusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950191808&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageTwoView())              
#             if counter == 35:
#                 break
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="usdc",label="usdc", emoji="<a:_:1043215920484581447>")
#     async def usdcusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950191754&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageTwoView())              
#             if counter == 35:
#                 break
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="xtz",label="xtz", emoji="<a:_:1043215920484581447>")
#     async def xtzusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950191753&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageTwoView())              
#             if counter == 35:
#                 break
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="lrc",label="lrc", emoji="<a:_:1043215920484581447>")
#     async def lrcusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950191531&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageTwoView())              
#             if counter == 35:
#                 break
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="crv", label="crv",emoji="<a:_:1043215920484581447>")
#     async def crvusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950191530&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageTwoView())              
#             if counter == 35:
#                 break
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="ren",label="ren", emoji="<a:_:1043215920484581447>")
#     async def renusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950190032&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageTwoView())              
#             if counter == 35:
#                 break

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="lnuc",label="lunc",emoji="<a:_:1043215920484581447>")
#     async def luncusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950189898&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageTwoView())              
#             if counter == 35:
#                 break

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="sushi",label="sushi", emoji="<a:_:1043215920484581447>")
#     async def sushiusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r= requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950189897&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageTwoView())              
#             if counter == 35:
#                 break

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="avax",label="avax", emoji="<a:_:1043215920484581447>")
#     async def avaxusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950189896&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageTwoView())
#             if counter == 35:
#                 await interaction.delete_original_response()
#                 break
            

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="matic",label="matic", emoji="<a:_:1043215920484581447>")
#     async def maticusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950189895&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageTwoView())
#             if counter == 35:
#                 break

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="algo", label="algo",emoji="<a:_:1043215920484581447>")
#     async def algousd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950188293&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageTwoView())
#             if counter == 35:
#                 break

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="uni",label="uni", emoji="<a:_:1043215920484581447>")
#     async def uniusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950188155&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageTwoView())
#             if counter == 35:
#                 break

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="link",label="link", emoji="<a:_:1043215920484581447>")
#     async def linkusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950188154&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageTwoView())
#             if counter == 35:
#                 break

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="bat", label="bat",emoji="<a:_:1043215920484581447>")
#     async def batusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950188153&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageTwoView())
#             if counter == 35:
#                 break

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="zec",label="zec", emoji="<a:_:1043215920484581447>")
#     async def zecusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950181635&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageTwoView())
#             if counter == 35:
#                 break

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="xml",label="xml", emoji="<a:_:1043215920484581447>")
#     async def xlmusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950181553&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageTwoView())
#             if counter == 35:
#                 break

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="dash",label="dash", emoji="<a:_:1043215920484581447>")
#     async def dashusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950181555&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageTwoView())
#             if counter == 35:
#                 break 

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="etc",label="etc", emoji="<a:_:1043215920484581447>")
#     async def etcusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950184636&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageTwoView())
#             if counter == 30:
#                 break

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="bch",label="bch", emoji="<a:_:1043215920484581447>")
#     async def bchusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950160803&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageTwoView())
#             if counter == 35:
#                     break

#     @disnake.ui.button(style=disnake.ButtonStyle.red,emoji=f"{emojis.leftarrow}",custom_id="cryptwefonexter",disabled=False)
#     async def cryptoleft(self, button: disnake.ui.Button,interaction: disnake.MessageCommandInteraction):
#         await interaction.response.edit_message(view=CryptoViewStart())    
    
    
#     @disnake.ui.button(style=disnake.ButtonStyle.red,emoji=f"{emojis.rightarrow}",custom_id="cryptwefonexter",disabled=False)
#     async def cryptoright(self, button: disnake.ui.Button,interaction: disnake.MessageCommandInteraction):
#         await interaction.response.edit_message(view=PageThreeView())



# class PageThreeView(disnake.ui.View):#add left and right arrows
#     def __init__(self):
#         super().__init__(timeout=None)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="ltc",label="ltc", emoji="<a:_:1043215920484581447>")
#     async def ltcusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950160801&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageThreeView())
#             if counter == 35:
#                     break

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="grt",label="grt", emoji="<a:_:1043215920484581447>")
#     async def grtusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950190669&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageThreeView())
#             if counter == 35:
#                     break

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="ftm",label="ftm", emoji="<a:_:1043215920484581447>")
#     async def ftmusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950190668&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageThreeView())
#             if counter == 35:
#                     break

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="mana",label="mana", emoji="<a:_:1043215920484581447>")
#     async def manausd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950190667&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)

#             await interaction.response.edit_message(embed=embed, view=PageThreeView())
#             if counter == 35:
#                     break
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="atom",label="atom", emoji="<a:_:1043215920484581447>")
#     async def atomusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950190666&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageThreeView())
#             if counter == 35:
#                     break

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="sol", label="sol",emoji="<a:_:1043215920484581447>")
#     async def solusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950190134&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageThreeView())
#             if counter == 35:
#                     break

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="ape", label="ape",emoji="<a:_:1043215920484581447>")

#     async def apeusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950192228&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageThreeView())
#             if counter == 35:
#                     break

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="eth",label="eth", emoji="<a:_:1043215920484581447>")
#     async def ethusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950160804&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageThreeView())
#             if counter == 35:
#                     break

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="ada",label="ada", emoji="<a:_:1043215920484581447>")
#     async def adausd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950185924&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)

#             await interaction.response.edit_message(embed=embed, view=PageThreeView())
#             if counter == 35:
#                     break

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="shib",label="shib", emoji="<a:_:1043215920484581447>")
#     async def shibusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950187162&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
#             await interaction.response.edit_message(embed=embed, view=PageThreeView())
#             if counter == 35:
#                     break

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="doge",label="doge", emoji="<a:_:1043215920484581447>")
#     async def dogeusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950181551&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
            
#             await interaction.response.edit_message(embed=embed, view=PageThreeView())
#             if counter == 35:
#                     break




#     @disnake.ui.button(style=disnake.ButtonStyle.grey, custom_id="btc",label="btc", emoji="<a:_:1043215920484581447>")
#     async def btcusd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
        
        
#         counter = 0
#         while True:
#             counter = counter + 1
#             r=requests.get(url="https://quotes-gw.webullfintech.com/api/stock/tickerRealTime/getQuote?tickerId=950181551&includeSecu=1&includeQuote=1&more=1").json()
#             changeratio = round(float(r["changeRatio"])*100, ndigits=2)
#             high = r['high']
#             low = r['low']
#             price = r['close']
#             sym = r['symbol']
#             name = r['name']
#             embed = disnake.Embed(title=f"{name} | {sym}", description=f"```py\nPrice: {price}```", color=disnake.Colour.random())
#             embed.add_field(name=f"Low:", value=f"```py\n${low}```",inline=True)
#             embed.add_field(name=f"High:", value=f"```py\n${high}```",inline=True)
#             embed.add_field(name=f"Change on Day:", value=f"```py\n{changeratio}%```",inline=True)
            
    
#             await interaction.response.edit_message(embed=embed, view=PageThreeView())
#             if counter == 35:
#                     break


# class MonitorStart(disnake.ui.View):#add left and right arrows
#     def __init__(self):
#         super().__init__(timeout=None)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,emoji=f"{emojis.lh}", custom_id="monitor1button1",row=0, disabled=True)#data
#     async def monitor1button1(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.le}", custom_id="monitor1button2",row=0, disabled=True)#tools
#     async def monitor1button2(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.ll}", custom_id="monitor1button3",row=0, disabled=True)#check
#     async def monitor1button3(self, bug: str, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.lp}", custom_id="monitor1button4",row=0, disabled=True)#citedworks
#     async def monitor1button4(self, button: disnake.ui.Button, inter: disnake.AppCommandInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="monitor1button5",row=0, disabled=True)#data
#     async def monitor1button5(self, button: disnake.ui.Button, inter: disnake.AppCommandInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.lm}", custom_id="monitor1button6",row=1, disabled=True)#botcommands
#     async def monitor1button6(self, button: disnake.ui.Button, inter: disnake.AppCommandInter):
#         await inter.response.edit_message(view=None)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.le}", custom_id="monitor1button7",row=1, disabled=True)
#     async def monitor1button7(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.ln}", custom_id="monitor1button8", disabled=True,row=1)
#     async def monitor1button8(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.lu}", custom_id="monitor1button9",row=1, disabled=True)
#     async def monitor1button9(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="monitor1button10",row=1, disabled=True)
#     async def monitor1button10(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())



#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="monitor1button11",row=2, disabled=True)#botcommands
#     async def monitor1button11(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=None)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="monitor1button12",row=2, disabled=True)
#     async def monitor1button12(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="monitor1button13", disabled=True,row=2)
#     async def monitor1button13(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         self.monitor1button13.disabled = True
#         self.monitor1button18.disabled=False
#         self.monitor1button15.style = disnake.ButtonStyle.green
#         self.monitor1button18.emoji = f"{emojis.important}"
#         self.monitor1button18.style = disnake.ButtonStyle.green

#         await inter.response.edit_message(view=self)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.movingchart}", custom_id="monitor1button14",row=2, disabled=True)
#     async def monitor1button14(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.rightarrow}", custom_id="monitor1button15",row=2, disabled=False)
#     async def monitor1button15(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):

#         self.monitor1button15.emoji= f"{emojis.movingchart}"
#         self.monitor1button15.disabled=True
#         self.linkbutton25.disabled=False
#         self.linkbutton25.emoji= f"{emojis.greenfire}"
#         await inter.response.edit_message(view=self,embed=HelpStart().embed)


    

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.download}", custom_id="monitor1button16",row=3, disabled=True)
#     async def monitor1button16(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):

#         self.add_item(BotCmdMenu())
#         embed = disnake.Embed(title=f"Dropdown Menus", description=f"```py\nWhile navigating the APP - you can utilize the drop-down menus for very convenient referencing for mobile users. The rich-embedded content is perfect for quick analysis of plays or if trying to learn bot commands.```", color=disnake.Colour.dark_orange())
#         embed.add_field(name=f"{emojis.downtrend_arrow}", value="```py\nClick the drop-down menu here to see an example.```")
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.download}", custom_id="monitor1button17",row=3, disabled=True)
#     async def monitor1button17(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.download}", custom_id="monitor1button18",disabled=True,row=3)#DOWNARROW
#     async def monitor1button18(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         self.remove_item(self.monitor1button21)
#         self.remove_item(self.monitor1button22)
#         self.remove_item(self.monitor1button23)
#         self.remove_item(self.monitor1button24)
#         self.remove_item(self.linkbutton25)
#         self.remove_item(self.monitor1button16)
#         self.remove_item(self.monitor1button17)
#         self.remove_item(self.monitor1button18)
#         self.remove_item(self.monitor1button19)
#         self.remove_item(self.monitor1button20)
#         self.add_item(BotCmdMenu())
#         self.add_item(HighShortsViewStart().select)
#         embed = disnake.Embed(title=f"Dropdown Menus", description=f"```py\nWhile navigating the APP - you can utilize the drop-down menus for very convenient referencing for mobile users. The rich-embedded content is perfect for quick analysis of plays or if trying to learn bot commands.```", color=disnake.Colour.dark_orange())
#         embed.add_field(name=f"{emojis.downarrow}", value="```py\nClick the drop-down menu here to see an example of what the command menu as well as what a data menu for options looks like. You can select any bot commands to have the full list printed to discord.```")
#         embed.add_field(name=f"{emojis.fail}", value="```py\nReturn to main menu.```")
#         embed.add_field(name=f"{emojis.rightarrow}", value="```py\nStart Tutorial Over.```")
#         self.monitor1button5.disabled=False
#         self.monitor1button15.disabled=False
#         self.monitor1button5.emoji = f"{emojis.fail}"
#         self.monitor1button5.callback = lambda interaction: interaction.response.edit_message(view=LitStart(), embed=MainEmbedAPP())
#         self.monitor1button15.callback = lambda interaction: interaction.response.edit_message(view=HelpStart(), embed=HelpEmbed())
#         await inter.response.edit_message(view=self, embed=embed)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.download}", custom_id="monitro9",row=3, disabled=True)#data
#     async def monitor1button19(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.download}", custom_id="monitor1button20",row=3, disabled=True)#magicwand
#     async def monitor1button20(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.download}", custom_id="monitor1button21",row=4, disabled=True)#data
#     async def monitor1button21(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.download}", custom_id="monitor1button22",row=4, disabled=True)#pins
#     async def monitor1button22(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.download}", custom_id="monitor1button23",row=4, disabled=True)#alert
#     async def monitor1button23(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.download}", custom_id="monitor1button24",row=4, disabled=True)#sectorrotation
#     async def monitor1button24(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=AppStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.download}", custom_id="monitor1button25",row=4, disabled=True)#data
#     async def linkbutton25(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         embed = disnake.Embed(title=f"{emojis.confirmed}", description=f"```py\nbuttons will return you back to main pages.```")
#         embed.add_field(name="Let me know your feedback!", value=f"```py\nThis should be a very beneficial tool. All feedback is welcome.``` ** Click the** {emojis.important} **emoji for an example drop-down menu tutorial.**")
#         self.linkbutton25.disabled=True

#         self.monitor1button13.disabled = False

#         self.monitor1button15.emoji = f"{emojis.rightarrow}"
#         self.monitor1button13.emoji = f"{emojis.confirmed}"
#         self.monitor1button13.style = disnake.ButtonStyle.blurple
#         await inter.response.edit_message(view=self,embed=embed)



# class StockPage1(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)





#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.confirmed}",custom_id="topag2r434e334t")
#     async def page2rig4ht(self, button: disnake.ui.Button, interaction: disnake.MessageCommandInteraction):
#         await interaction.response.edit_message(view=LitStart(), embed=MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"{emojis.rightarrow}",custom_id="topag234e3as34t")
#     async def pager2right(self, button: disnake.ui.Button, interaction: disnake.MessageCommandInteraction):
#         await interaction.response.edit_message(view=StockPage3())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,label="AAPL",custom_id="AAPL",emoji="<a:_:1043679142576656475>")
#     async def aapl(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["AAPL"]
#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange infor for {self.sym}", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="MSFT",label="MSFT",emoji="<a:_:1043679142576656475>")
#     async def msft(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["MSFT"]
#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")

#         counter = 0
#         await interaction.response.defer(with_message=True)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange infor for {self.sym}", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 35:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="AMZN",label="AMZN",emoji="<a:_:1043679142576656475>")
#     async def amzn(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["AMZN"]

#         counter = 0
#         await interaction.response.defer(with_message=True)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange infor for {self.sym}", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 35:
#                 break
#         await interaction.response.edit_message(view=self,embed=em)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="GOOGL",label="GOOGL",emoji="<a:_:1043679142576656475>")
#     async def googl(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):

#         self.ids = ticker_list["GOOGL"]
#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange infor for {self.sym}", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 35:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="BRK.B",label="BRK.B",emoji="<a:_:1043679142576656475>")

#     async def brkb(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["BRK-B"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange infor for {self.sym}", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 35:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="GOOG",label="GOOG",emoji="<a:_:1043679142576656475>")

#     async def goog(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["GOOG"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange infor for {self.sym}", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="TSLA",label="TSLA",emoji="<a:_:1043679142576656475>")

#     async def tsla(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["TSLA"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange infor for {self.sym}", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)
#         await interaction.response.edit_message(view=self,embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="UNH",label="UNH",emoji="<a:_:1043679142576656475>")

#     async def unh(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):

#         self.ids = ticker_list["UNH"]
#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for UNH", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange infor for {self.sym}", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="XOM",label="XOM",emoji="<a:_:1043679142576656475>")
#     async def xom(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):

#         self.ids = ticker_list["XOM"]
#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for XOM", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange infor for {self.sym}", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="JNJ",label="JNJ",emoji="<a:_:1043679142576656475>")
#     async def jnj(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["JNJ"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for JNJ", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange infor for {self.sym}", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="NVDA",label="NVDA",emoji="<a:_:1043679142576656475>")
#     async def nvda(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["NVDA"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         await interaction.response.defer(with_message=True, ephemeral=False)
#         counter = 0
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for NVDA", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
            
#             if counter == 50:
#                 break
#         await interaction.edit_original_message(embed = em)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="JPM",label="JPM",emoji="<a:_:1043679142576656475>")
#     async def jpm(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["JPM"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for JPM", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="V",label="V",emoji="<a:_:1043679142576656475>")
#     async def v(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["V"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for V", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="PG",label="PG",emoji="<a:_:1043679142576656475>")
#     async def ph(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["PG"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for PG", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="CVX",label="CVX",emoji="<a:_:1043679142576656475>")
#     async def cvx(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["CVX"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for CVX", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="HD",label="HD",emoji="<a:_:1043679142576656475>")
#     async def hd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["HD"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for HD", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="MA",label="MA",emoji="<a:_:1043679142576656475>")
#     async def ma(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["MA"]
#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for MA", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="LLY",label="LLY",emoji="<a:_:1043679142576656475>")
#     async def lly(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["LLY"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for {self.sym}", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)
        

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="PFE",label="PFE",emoji="<a:_:1043679142576656475>")
#     async def pfe(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["PFE"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for PFE", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="ABBV",label="ABBV",emoji="<a:_:1043679142576656475>")
#     async def abbv(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["ABBV"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for ABBV", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="MRK",label="MRK",emoji="<a:_:1043679142576656475>")
#     async def mrk(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["MRK"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for MRK", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)
    

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="META",label="META",emoji="<a:_:1043679142576656475>")
#     async def meta(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["META"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         counter = 0
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for META", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

# class StockPage2(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji="<a:_:1042677512284680321>",custom_id="topage22t2344")
#     async def page1left(self, button: disnake.ui.Button, interaction: disnake.MessageCommandInteraction):
#         await interaction.response.edit_message(view=StockPage1())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.confirmed}",custom_id="toptyetage222344t")
#     async def page2right35(self, button: disnake.ui.Button, interaction: disnake.MessageCommandInteraction):
#         await interaction.response.edit_message(view=LitStart(), embed=MainEmbedAPP())
#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji="<a:_:1043216013208064050>",custom_id="topage222344t")
#     async def page2right(self, button: disnake.ui.Button, interaction: disnake.MessageCommandInteraction):
#         await interaction.response.edit_message(view=StockPage3())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="PEP",label="PEP",emoji="<a:_:1043679142576656475>")
#     async def pep(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["PEP"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for PEP", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="KO",label="KO",emoji="<a:_:1043679142576656475>")

#     async def ko(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["KO"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for KO", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="COST",label="COST",emoji="<a:_:1043679142576656475>")

#     async def cost(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["COST"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for COST", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="WMT",label="WMT",emoji="<a:_:1043679142576656475>")

#     async def wmt(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["WMT"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for WMT", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)



#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="AVGO",label="AVGO",emoji="<a:_:1043679142576656475>")

#     async def avgo(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["AVGO"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for AVGO", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="MCD",label="MCD",emoji="<a:_:1043679142576656475>")

#     async def mcd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["MCD"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for MCD", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="CSCO",label="CSCO",emoji="<a:_:1043679142576656475>")

#     async def csco(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["CSCO"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for CSCO", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="ACN",label="ACN",emoji="<a:_:1043679142576656475>")

#     async def can(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["ACN"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for ACN", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="ABT",label="ABT",emoji="<a:_:1043679142576656475>")

#     async def abt(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["ABT"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for ABT", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="WFC",label="WFC",emoji="<a:_:1043679142576656475>")

#     async def wfc(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["WFC"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for WFC", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="DHR",label="DHR",emoji="<a:_:1043679142576656475>")

#     async def dhr(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["DHR"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for DHR", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="COP",label="COP",emoji="<a:_:1043679142576656475>")

#     async def cop(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["COP"]
#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for COP", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="DIS",label="DIS",emoji="<a:_:1043679142576656475>")

#     async def dis(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["DIS"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for DIS", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="LIN",label="LIN",emoji="<a:_:1043679142576656475>")

#     async def lin(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["LIN"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for LIN", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="BMY",label="BMY",emoji="<a:_:1043679142576656475>")

#     async def bmy(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["BMY"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for BMY", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="NEE",label="NEE",emoji="<a:_:1043679142576656475>")

#     async def nee(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["NEE"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for NEE", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="TXN",label="TXN",emoji="<a:_:1043679142576656475>")

#     async def txn(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["TXN"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for TXN", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="VZ",label="VZ",emoji="<a:_:1043679142576656475>")

#     async def vz(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["VZ"]
#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for VZ", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="ADBE",label="ADBE",emoji="<a:_:1043679142576656475>")

#     async def adbe(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["ADBE"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for ADBE", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="AMGN",label="AMGN",emoji="<a:_:1043679142576656475>")

#     async def amgn(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["AMGN"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for AMGN", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="CMCSA",label="CMCSA",emoji="<a:_:1043679142576656475>")

#     async def cmcsa(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["CMCSA"]
#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for CMCSA", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

# class StockPage3(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji="<a:_:1042677512284680321>",custom_id="topage113t4")
#     async def page1left(self, button: disnake.ui.Button, interaction: disnake.MessageCommandInteraction):
#         await interaction.response.edit_message(view=StockPage2())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.confirmed}",custom_id="topage1re2124t")
#     async def page2rcct(self, button: disnake.ui.Button, interaction: disnake.MessageCommandInteraction):
#         await interaction.response.edit_message(view=LitStart(), embed=MainEmbedAPP())
    
#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji="<a:_:1043216013208064050>",custom_id="topage12124t")
#     async def page2right(self, button: disnake.ui.Button, interaction: disnake.MessageCommandInteraction):
#         await interaction.response.edit_message(view=StockPage4())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="PM",label="PM",emoji="<a:_:1043679142576656475>")

#     async def pm(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["PM"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for PM", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="HON",label="HON",emoji="<a:_:1043679142576656475>")

#     async def hon(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["HON"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for HON", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="RTX",label="RTX",emoji="<a:_:1043679142576656475>")
#     async def rtx(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["RTX"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for RTX", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="QCOM",label="QCOM",emoji="<a:_:1043679142576656475>")

#     async def qcom(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["QCOM"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for QCOM", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="T",label="T",emoji="<a:_:1043679142576656475>")

#     async def t(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["T"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for T", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="LOW",label="LOW",emoji="<a:_:1043679142576656475>")

#     async def low(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["LOW"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for LOW", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="NKE",label="NKE",emoji="<a:_:1043679142576656475>")

#     async def nke(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["NKE"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for NKE", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="IBM",label="IBM",emoji="<a:_:1043679142576656475>")

#     async def ibm(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["IBM"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for IBM", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="NFLX",label="NFLX",emoji="<a:_:1043679142576656475>")

#     async def nflx(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["NFLX"]
#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         await interaction.response.edit_message(view=self,embed=embed)

#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for NFLX", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

        
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="UNP",label="UNP",emoji="<a:_:1043679142576656475>")

#     async def unp(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["UNP"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for UNP", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="GS",label="GS",emoji="<a:_:1043679142576656475>")

#     async def gs(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["GS"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for GS", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="UPS",label="UPS",emoji="<a:_:1043679142576656475>")

#     async def ups(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["UPS"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for UPS", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="CVS",label="CVS",emoji="<a:_:1043679142576656475>")

#     async def cvs(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["CVS"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for CVS", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="INTC",label="INTC",emoji="<a:_:1043679142576656475>")

#     async def intc(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["INTC"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for INTC", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="CE",label="CAT",emoji="<a:_:1043679142576656475>")

#     async def cat(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["CAT"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for CAT", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="ORCL",label="ORCL",emoji="<a:_:1043679142576656475>")

#     async def orcl(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["ORCL"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for ORCL", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="AMD",label="AMD",emoji="<a:_:1043679142576656475>")

#     async def amd(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["AMD"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for AMD", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="MS",label="MS",emoji="<a:_:1043679142576656475>")

#     async def ms(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["MS"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for MS", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="SCHW",label="SCHW",emoji="<a:_:1043679142576656475>")

#     async def schw(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["SCHW"]
#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for SCHW", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="SPGI",label="SPGI",emoji="<a:_:1043679142576656475>")

#     async def spgi(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["SPGI"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for SPGI", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="DE",label="DE",emoji="<a:_:1043679142576656475>")

#     async def de(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["DE"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for DE", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="ELV",label="ELV",emoji="<a:_:1043679142576656475>")

#     async def elv(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["ELV"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for ELV", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)
# class StockPage4(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)


#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji="<a:_:1042677512284680321>",custom_id="towef3rww2t4")
#     async def page1left(self, button: disnake.ui.Button, interaction: disnake.MessageCommandInteraction):
#         await interaction.response.edit_message(view=StockPage3())
    
#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.confirmed}",custom_id="top34542qq355t4")
#     async def page4home(self, button: disnake.ui.Button, interaction: disnake.MessageCommandInteraction):
#         await interaction.response.edit_message(view=LitStart(), embed=MainEmbedAPP())

#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji="<a:_:1043216013208064050>",custom_id="topwefagefwwee44t")
#     async def page2right(self, button: disnake.ui.Button, interaction: disnake.MessageCommandInteraction):
#         await interaction.response.edit_message(view=StockPage5())
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="LMT",label="LMT",emoji="<a:_:1043679142576656475>")

#     async def lmt(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["LMT"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for LMT", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="SBUX",label="SBUX",emoji="<a:_:1043679142576656475>")

#     async def sbux(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["SBUX"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for SBUX", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="BLK",label="BLK",emoji="<a:_:1043679142576656475>")

#     async def blk(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["BLK"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for BLK", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="INTU",label="INTU",emoji="<a:_:1043679142576656475>")

#     async def intu(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["INTU"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for INTU", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="MDT",label="MDT",emoji="<a:_:1043679142576656475>")

#     async def mdt(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["MDT"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for MDT", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="ADP",label="ADP",emoji="<a:_:1043679142576656475>")

#     async def adp(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["ADP"]
#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for ADP", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="GILD",label="GILD",emoji="<a:_:1043679142576656475>")

#     async def gild(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["GILD"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for GILD", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="PLD",label="PLD",emoji="<a:_:1043679142576656475>")

#     async def pld(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["PLD"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for PLD", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="AMT",label="AMT",emoji="<a:_:1043679142576656475>")

#     async def amt(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["AMT"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for AMD", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="PYPL",label="PYPL",emoji="<a:_:1043679142576656475>")

#     async def pypl(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["PYPL"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for PYPL", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="BA",label="BA",emoji="<a:_:1043679142576656475>")

#     async def ba(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["BA"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for BA", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="CI",label="CI",emoji="<a:_:1043679142576656475>")

#     async def ci(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["CI"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for CI", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="C",label="C",emoji="<a:_:1043679142576656475>")

#     async def c(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["C"]
#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for C", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="GE",label="GE",emoji="<a:_:1043679142576656475>")

#     async def ge(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["GE"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for GE", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="ISRG",label="ISRG",emoji="<a:_:1043679142576656475>")

#     async def isrg(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["ISRG"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()

#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for ISRG", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="TJX",label="TJX",emoji="<a:_:1043679142576656475>")

#     async def tjx(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["TJX"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for TJX", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="AMAT",label="AMAT",emoji="<a:_:1043679142576656475>")

#     async def amat(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["AMAT"]
#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for AMAT", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="AXP",label="AXP",emoji="<a:_:1043679142576656475>")

#     async def axp(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["AXP"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for AXP", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)
#     # @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="TMUS",label="TMUS",emoji="<a:_:1043679142576656475>")

#     # async def tmus(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#     #     self.ids = ticker_list["TMUS"]
#     #     self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#     #     self.close = self.r[0]['close']
#     #     self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#     #     self.sym = self.r[0]['disSymbol']
#     #     embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#     #     counter = 0
#     #     await interaction.response.defer(with_message=True,ephemeral=False)
#     #     while True:
#     #         counter = counter + 1
#     #         r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#     #         d= r.json()
#     #         data = d['data']
#     #         index1 = data[0]
#     #         time = index1['tradeTime']
#     #         price = index1['price']
#     #         volume = index1['volume']
#     #         trdbs = index1['trdBs']
#     #         trdex = index1['trdEx']
#     #         em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for TMUS", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#     #         em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#     #         await interaction.edit_original_message(embed = em)
#     #         if counter == 50:
#     #             break
#     #     await interaction.response.edit_message(view=self,embed=embed)



#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="MDLZ",label="MDLZ",emoji="<a:_:1043679142576656475>")

#     async def mdlz(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["MDLZ"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for MDLZ", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="CB",label="CB",emoji="<a:_:1043679142576656475>")

#     async def cb(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["CB"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for CB", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

# class StockPage5(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)


#     @disnake.ui.button(style=disnake.ButtonStyle.red, emoji="<a:_:1042677512284680321>",custom_id="top34542355t4")
#     async def page1left(self, button: disnake.ui.Button, interaction: disnake.MessageCommandInteraction):
#         await interaction.response.edit_message(view=StockPage4())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.confirmed}",custom_id="top34542qq355t4")
#     async def page4home(self, button: disnake.ui.Button, interaction: disnake.MessageCommandInteraction):
#         await interaction.response.edit_message(view=LitStart(), embed=MainEmbedAPP())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="BAC",label="BAC",emoji="<a:_:1043679142576656475>")
#     async def bac(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["BAC"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for BAC", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="CRM",label="CRM",emoji="<a:_:1043679142576656475>")

#     async def crm(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["CRM"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for CRM", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="EOG",label="EOG",emoji="<a:_:1043679142576656475>")

#     async def eog(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["EOG"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for EOG", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)




#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="TMO",label="TMO",emoji="<a:_:1043679142576656475>")

#     async def tmo(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["TMO"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for TMO", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="ADI",label="ADI",emoji="<a:_:1043679142576656475>")

#     async def adi(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["ADI"]
#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for ADI", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="MMC",label="MMC",emoji="<a:_:1043679142576656475>")

#     async def mmc(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["MMC"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for MMC", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="NOW",label="NOW",emoji="<a:_:1043679142576656475>")

#     async def now(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["NOW"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for NOW", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="VRTX",label="VRTX",emoji="<a:_:1043679142576656475>")

#     async def vrtx(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["VRTX"]
#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for VRTX", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="REGN",label="REGN",emoji="<a:_:1043679142576656475>")

#     async def regn(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["REGN"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         await interaction.response.edit_message(view=self,embed=embed)       
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for REGN", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="MO",label="MO",emoji="<a:_:1043679142576656475>")

#     async def mo(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["MO"]
#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for MO", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="BKNG",label="BKNG",emoji="<a:_:1043679142576656475>")

#     async def bkng(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["BKNG"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for BKNG", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="NOC",label="NOC",emoji="<a:_:1043679142576656475>")

#     async def noc(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["NOC"]

#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for NOC", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="TGT",label="TGT",emoji="<a:_:1043679142576656475>")

#     async def tgt(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["TGT"]
#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for TGT", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,custom_id="PGR",label="PGR",emoji="<a:_:1043679142576656475>")
#     async def pgr(self, button: disnake.ui.Button, interaction: disnake.ApplicationCommandInteraction):
#         self.ids = ticker_list["PGR"]
#         self.r= requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={self.ids}%20%20%20%20%20&includeSecu=1&delay=0&more=1").json()
#         self.close = self.r[0]['close']
#         self.vol= round(float(self.r[0]['volume'])*0.000001,ndigits=2)
#         self.sym = self.r[0]['disSymbol']
#         embed = disnake.Embed(title=f"Stats for {self.sym}", description=f"```py\nCurrent Price: ${self.close} | Current Volume: {self.vol} million.```")
#         counter = 0
#         await interaction.response.defer(with_message=True,ephemeral=False)
#         while True:
#             counter = counter + 1
#             r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={self.ids}")
#             d= r.json()
#             data = d['data']
#             index1 = data[0]
#             time = index1['tradeTime']
#             price = index1['price']
#             volume = index1['volume']
#             trdbs = index1['trdBs']
#             trdex = index1['trdEx']
#             em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for PGR", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
#             em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
#             await interaction.edit_original_message(embed = em)
#             if counter == 50:
#                 break
#         await interaction.response.edit_message(view=self,embed=embed)



# class DataViewStart(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)

#         self.add_item(DataMenu())
#         self.embed= disnake.Embed(title=f"{emojis.ld}{emojis.la}{emojis.lt}{emojis.la} {emojis.lm}{emojis.le}{emojis.ln}{emojis.lu}", description=f"```py\nClick the corresponding emoji, or select from the dropdown list the datasets that you would like to browse. All datasets are updated daily / weekly / monthly depending on the data being retrieved.```", color=disnake.Colour.dark_gold())
#         self.embed.add_field(name=f"{emojis.moneygun}", value=f"```py\nMoney Market Fund Datasets that show the exposure to the FED REPO as well as Bilateral repo transactions.```")
#         self.embed.add_field(name=f"{emojis.balloons}", value=f"```py\nInflation data from around the globe. With inflation being the FED's key focus - this is an important dataset to monitor.```")
#         self.embed.add_field(name=f"{emojis.repo}", value=f"```py\nView several repo datasets. Includes treasuries sold/bought - agency securities sold/bought, and mortgage backed securities sold/bought during the overnight, repo, and reverse repo operations.```")
#         self.embed.add_field(name=f"{emojis.pinkcrystal}", value=f"```py\nFINRA Datasets - Includes alternative trading system data and over the counter data.```")
#         self.embed.add_field(name=f"{emojis.hammering}", value=f"```py\nUS Unemployment Data. The FED wants unemployment to rise to help slow the economy. Important data to keep an eye on.```")
#         self.embed.add_field(name=f"{emojis.btcemoji}", value=f"```py\nBlockchain datasets. Several to choose from.```")
#         self.embed.add_field(name=f"{emojis.datas}", value=f"```py\nOrganisation for Economic Co-operation and Development data from around the world.```")
#         self.embed.add_field(name=f"{emojis.china}", value=f"````py\nView data out of the HKEX exchange.```")
#         self.embed.add_field(name=f"{emojis.redline}", value="```py\nView Systematic Internalizer data out of Europe regulated by ESMA.```"),
#         self.embed.add_field(name=f"{emojis.fed}", value="```py\nFederal Reserve Bank of New York Datasets - includes securities lending, SOMA holdings, and historic ON RRP repo data.```"),
#         self.embed.add_field(name=f"{emojis.treasury}", value="```py\nTreasury auction data, bond datasets.```"),
#         self.embed.set_footer(text="Implemented by FUDstop.")
#     @disnake.ui.button(style=disnake.ButtonStyle.grey,emoji=f"{emojis.coolchart}", custom_id="databutton1",row=0, disabled=True)#data
#     async def databutton1(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.moneygun}", custom_id="databutton2",row=0, disabled=False)#tools
#     async def databutton2(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=MMFDataStart(), embed=MMFDataEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="databutton3",row=0, disabled=True)#check
#     async def databutton3(self, bug: str, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed=MainEmbedAPP())
    
    
#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.balloons}", custom_id="databutton4",row=0, disabled=False)#citedworks
#     async def databutton4(self, button: disnake.ui.Button, inter: disnake.AppCommandInter):
#         self.embed= disnake.Embed(title=f"{emojis.li}{emojis.ln}{emojis.lf}{emojis.ll}{emojis.la}{emojis.lt}{emojis.li}{emojis.lo}{emojis.ln}", description=f"```py\nYou are viewing Inflation Datasets.```{emojis.balloons} Select one from the dropdown to view it.", color=disnake.Colour.dark_blue())
#         self.embed.add_field(name=f"{emojis.confirmed}", value=f"```py\nReturn```")
#         await inter.response.edit_message(view=InflationDataStart(), embed=InflationDataEmbed)

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="databutton5",row=0, disabled=True)#data
#     async def databutton5(self, button: disnake.ui.Button, inter: disnake.AppCommandInter):
#         await inter.response.edit_message(view=FedDataStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.repo}", custom_id="databutton6",row=1, disabled=False)#botcommands
#     async def databutton6(self, button: disnake.ui.Button, inter: disnake.AppCommandInter):
#         await inter.response.edit_message(view=RepoDataStart(), embed=RepoDataEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="databutton7",row=1, disabled=True)
#     async def databutton7(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.pinkcrystal}", custom_id="databutton8", disabled=False,row=1)
#     async def databutton8(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):

#         await inter.response.edit_message(view=FINRADataStart(), embed=FINRADataEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="databutton9",row=1, disabled=True)
#     async def databutton9(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.hammering}", custom_id="databutton10",row=1, disabled=False)
#     async def databutton10(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         self.embed= disnake.Embed(title=f"{emojis.le}{emojis.lc}{emojis.lo}{emojis.ln}{emojis.lo}{emojis.lm}{emojis.li}{emojis.lc}", description=f"```py\nYou are viewing Economic Datasets.```{emojis.pinkcrystal} Select one from the dropdown to view it.", color=disnake.Colour.dark_blue())
#         self.embed.add_field(name=f"{emojis.confirmed}", value=f"```py\nReturn```")
#         await inter.response.edit_message(view=EconomicDataStart(), embed=EconomicEmbed())



#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.btcemoji}", custom_id="databutton11",row=3, disabled=False)#botcommands
#     async def databutton11(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         self.embed= disnake.Embed(title=f"{emojis.lb}{emojis.li}{emojis.lt}{emojis.lc}{emojis.lo}{emojis.li}{emojis.ln}", description=f"```py\nYou are viewing BTC Datasets.```{emojis.btcemoji} Select one from the dropdown to view it.", color=disnake.Colour.dark_blue())
#         self.embed.add_field(name=f"{emojis.confirmed}", value=f"```py\nReturn```")
#         await inter.response.edit_message(view=BlockchainDataStart(), embed=BTCDataEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="databutton12",row=3, disabled=True)
#     async def databutton12(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=DataViewStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.fed}", custom_id="databutton13", disabled=False,row=3)
#     async def databutton13(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=FedDataStart(), embed=FedDataEmbed())




#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="databutton14",row=3, disabled=True)
#     async def databutton14(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):

#         await inter.response.edit_message(view=DataViewStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.china}", custom_id="databutton15",row=3, disabled=False)
#     async def databutton15(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         self.embed= disnake.Embed(title=f"{emojis.lh}{emojis.lk}{emojis.le}{emojis.lx}", description=f"```py\nYou are viewing FINRA {emojis.pinkcrystal} Datasets. Select one from the dropdown to view it.```", color=disnake.Colour.dark_blue())
#         self.embed.add_field(name=f"{emojis.confirmed}", value=f"```py\nReturn```")
#         await inter.response.edit_message(view=HKEXDataStart(), embed=HKEXDataEmbed())


    
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="databutton21",row=4, disabled=True)#data
#     async def databutton21(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.redline}", custom_id="databutton22",row=4, disabled=False)#pins
#     async def databutton22(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         self.embed= disnake.Embed(title=f"{emojis.le}{emojis.ls}{emojis.lm}{emojis.la}", description=f"```py\nYou are viewing ESMA MiFID II {emojis.redline} Datasets. Select one from the dropdown to view it.```", color=disnake.Colour.dark_blue())
#         self.embed.add_field(name=f"{emojis.confirmed}", value=f"```py\nReturn```")
        
#         await inter.response.edit_message(view=EconomicDataStart(), embed = EconomicEmbed())


#     @disnake.ui.button(style=disnake.ButtonStyle.green, emoji=f"{emojis.downarrow}", custom_id="databutton23",row=4, disabled=False)#alert
#     async def databutton23(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.treasury}", custom_id="databutton24",row=4, disabled=False)#sectorrotation
#     async def databutton24(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):

#         await inter.response.edit_message(view=TreasuryDataStart(), embed=TreasuryDataEmbed())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="databutton25",row=4, disabled=True)#data
#     async def linkbutton25(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message()





# class CitedWorksViewStart(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)


#     @disnake.ui.button(style=disnake.ButtonStyle.grey,emoji=f"{emojis.coolchart}", custom_id="cited1button1",row=0, disabled=True)#data
#     async def cited1button1(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="cited1button2",row=0, disabled=True)#tools
#     async def cited1button2(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=CitedWorksViewStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="cited1button3",row=0, disabled=True)#check
#     async def cited1button3(self, bug: str, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart(), embed=MainEmbedAPP())
    
    
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="cited1button4",row=0, disabled=True)#citedworks
#     async def cited1button4(self, button: disnake.ui.Button, inter: disnake.AppCommandInter):
#         await inter.response.edit_message(view=CitedWorksViewStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.blurple, emoji=f"{emojis.fed}", custom_id="cited1button5",row=0, disabled=False)#data
#     async def cited1button5(self, button: disnake.ui.Button, inter: disnake.AppCommandInter):
#         embed = disnake.Embed(title=f"{emojis.lf}{emojis.le}{emojis.ld}", description=f"```py\nThe Repo Market```")
#         embed.add_field(name=f"{emojis.repo}", value=f"```py\nLearn about the literal heartbeat of the markets that have been the centerpieces of Monetary Policy since the onset of COVID19 - The Repo and Securities Lending Markets.```")
#         await inter.response.edit_message(view=RepoCitedViewStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="cited1button6",row=1, disabled=True)#botcommands
#     async def cited1button6(self, button: disnake.ui.Button, inter: disnake.AppCommandInter):
#         await inter.response.edit_message(view=RepoDataStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="cited1button7",row=1, disabled=True)
#     async def cited1button7(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="cited1button8", disabled=True,row=1)
#     async def cited1button8(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=CitedWorksViewStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="cited1button9",row=1, disabled=True)
#     async def cited1button9(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="cited1button10",row=1, disabled=True)
#     async def cited1button10(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=CitedWorksViewStart())



#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="cited1button11",row=3, disabled=True)#botcommands
#     async def cited1button11(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=CitedWorksViewStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="cited1button12",row=3, disabled=True)
#     async def cited1button12(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=CitedWorksViewStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="cited1button13", disabled=True,row=3)
#     async def cited1button13(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):

#         await inter.response.edit_message(view=CitedWorksViewStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="cited1button14",row=3, disabled=True)
#     async def cited1button14(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=DataViewStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="cited1button15",row=3, disabled=True)
#     async def cited1button15(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=CitedWorksViewStart())


    
#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="cited1button21",row=4, disabled=True)#data
#     async def cited1button21(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="cited1button22",row=4, disabled=True)#pins
#     async def cited1button22(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=CitedWorksViewStart())


#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="cited1button23",row=4, disabled=True)#alert
#     async def cited1button23(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=LitStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="cited1button24",row=4, disabled=True)#sectorrotation
#     async def cited1button24(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message(view=CitedWorksViewStart())

#     @disnake.ui.button(style=disnake.ButtonStyle.grey, emoji=f"{emojis.coolchart}", custom_id="cited1button25",row=4, disabled=True)#data
#     async def linkbutton25(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
#         await inter.response.edit_message()


# class ViewDrop(disnake.ui.Select):
#     def __init__(self):
#         super().__init__( 
#             placeholder="Make A Selection -->",
#             min_values=1,
#             max_values=1,
#             custom_id="viewdropwut",
#             options = [ 
#                 disnake.SelectOption(emoji=f"{emojis.repo}",value=1, description="View the fX Swaps Counterparties.")
#             ]
#         )

#     async def callback(self, interaction: disnake.MessageCommandInteraction):
#         if self.values[0] == "1":
#             await interaction.send(f"```py\nThe Current Counterparties for fX Swaps:``````py\n      Banco de Mexico",
#       "Bank of Canada",
#       "Bank of England",
#       "Bank of Japan",
#       "Bank of Korea",
#       "Danmarks Nationalbank",
#       "European Central Bank",
#       "Monetary Authority of Singapore",
#       "Norges Bank",
#       "Reserve Bank of Australia",
#       "Swiss National Bank```")




# class UltimateCryptoPage1(disnake.ui.View):
#     def __init__(self):
#         super().__init__(timeout=None)


