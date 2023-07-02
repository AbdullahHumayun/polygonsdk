import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _discord import emojis as e
import json
from cogs.analysis import Analysis
import pandas as pd
from cogs.ss import SS
from func_call_test import analyze_data
from views.mainview import MainView
import asyncio
from cogs.learn import Learn
from cogs.fmp import FMP
import disnake
from menus.embedmenus import PageSelect
from disnake.ext import commands
from disnake import Option, OptionType
from autocomp import command_autocomp, ticker_autocomp
from cfg import two_years_from_now_str
import aiohttp
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.polygon_sdk.universal_snapshot import UniversalOptionSnapshot,UniversalSnapshot,CallsOrPuts
from sdks.fudstop_sdk.fudstop_sdk import fudstopSDK
from menus.embedmenus import AlertMenus
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from cogs.skews import Skew

from tabulate import tabulate
from disnake import Option, OptionType, OptionChoice
from disnake.ext import commands

from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
from _discord import emojis


fudstop = fudstopSDK()
from stock_market import PolygonStockMarket


from views.learnviews import MenuStart,AlertStart, DiscordStart,TAStart,MarketsView,CryptoViewStart,PageTwoView,PageThreeView,HighShortsViewStart,LowFloatDropdown
from views.learnviews import ForexViewStart,FTDViewStart,LosersViewStart,GainersViewStart,ActiveViewStart
from views.learnviews import TotalOIViewStart,TotalVolumeViewStart
from views.learnviews import CoreStart, LinksStartView,LitStart,DataViewStart
from views.learnviews import WebullCmdViewStart,DDCmdViewStart,OptionCmdViewStart,FlowCmdViewStart,DPSCmdViewStart,EarningsCmdViewStart,EconomyCmdViewStart,LearnCmdViewStart,StreamCmdViewStart,StockCmdViewStart,ChartingCmdViewStart
from views.learnviews import HelpStart,VideoStartView,VideoStart2View,VideoStart3View,TopOptionsViewStart, AgencyViewStart
from views.learnviews import DTCCViewStart,NYSEViewStart, CBOEViewStart, OFRDataViewStart
from views.learnviews import TopOIDownViewStart,TopOIUpViewStart,TopIVViewStart,TopOIViewStart,TopVolumeViewStart,TotalTurnoverViewStart,TotalOIViewStart,TotalVolumeViewStart
from views.learnviews import FedDataStart,FINRADataStart,BlockchainDataStart,InflationDataStart,EconomicDataStart,TreasuryDataStart,HKEXDataStart,MMFDataStart,RepoDataStart
from views.learnviews import StockPage1,StockPage2,StockPage3,StockPage4,StockPage5, AppStart, ToolsViewStart
from views.learnviews import OFRViewStart, RepoCitedViewStart,CriteriaView,CommandsStart,PermaFTDViewStart
import disnake
from disnake.ext import commands

from views.learnviews import CriteriaView
from polygon_enhanced.polygon_enhanced.websocket import WebSocketClient,WebSocketMessage,Market,EquityAgg,EquityQuote,EquityTrade
from views.learnviews import AvoidView


from cfg import YOUR_API_KEY, YOUR_DISCORD_BOT_TOKEN


polygon = AsyncPolygonSDK(YOUR_API_KEY)
poly_options = PolygonOptionsSDK(YOUR_API_KEY)
webull = AsyncWebullSDK()

intents=disnake.Intents.all()
class PersistentViewBot(commands.Bot):
    def __init__(self, command_prefix, intents, tickers=['PG', 'RBLX', 'JD', 'TSCO', 'BYND', 'GOOG', 'UBER', 'CAG', 'GME', 'CCL', 'QQQ', 'CSCO', 'FUTU', 'ARCC', 'GPN', 'CG', 'HUN', 'TNA', 'DXC', 'GRPN', 'ENTG', 'PEP', 'PGR', 'MSFT', 'PACW', 'PCG', 'ADBE', 'KRE', 'GILD', 'VST', 'VFC', 'JNJ', 'AMC', 'SQNS', 'CVS', 'CDE', 'SUP', 'TBIO', 'YALA', 'INO', 'LVS', 'WDAY', 'SPXU', 'TDOC', 'SBUX', 'LTRX', 'KIM', 'EMR', 'BOX', 'DD', 'TMUS', 'ATVI', 'ASAN', 'FTDR', 'HD', 'SCHW', 'IPSC', 'TARO', 'HASI', 'DIA', 'JWN', 'AVDX', 'MARA', 'PPL', 'MOS', 'ET', 'IAI', 'HOLI', 'QS', 'JBT', 'KEY', 'SFIX', 'AUPH', 'DXCM', 'CHRS', 'CRVS', 'SMRT', 'IBN', 'SQ', 'ACGL', 'ABT', 'AZN', 'INFN', 'KLR', 'BBAI', 'LYV', 'CTLT', 'TECK', 'BRMK', 'EFA', 'FCEL', 'ZGN', 'SBOW', 'NOVA', 'ARDX', 'FITB', 'GOOGL', 'SHOP', 'DAC', 'LNC', 'AMGN', 'TUYA', 'SYNH', 'NMTR', 'SMH', 'BGS', 'AEG', 'DKNG', 'FCX', 'NI', 'NMR', 'TSE', 'OBLG', 'CHPT', 'AES', 'NU', 'CRC', 'UNH', 'CIEN', 'FTCH', 'SWN', 'UP', 'RNG', 'EZPW', 'XPEV', 'PAAS', 'LBTYA', 'MUFG', 'BUD', 'INTZ', 'RKT', 'CLNE', 'APO', 'OTIS', 'VLY', 'DT', 'M', 'QCOM', 'PCT', 'TIL', 'IPG', 'ARKK', 'ADI', 'YUM', 'WMT', 'SMCI', 'XP', 'CCCC', 'AG', 'SAM', 'MGM', 'BOH', 'CAT', 'RYAN', 'MDT', 'HOWL', 'JETS', 'SYY', 'FLEX', 'VTRS', 'PYPL', 'VVV', 'UNIT', 'MRK', 'BANX', 'MRIN', 'VTR', 'NVDA', 'AVGO', 'GLUE', 'DOCU', 'KR', 'ASTS', 'CANO', 'MMM', 'ADVM', 'BIGC', 'SNDL', 'CZR', 'LX', 'HOOD', 'MDB', 'VIAV', 'SO', 'FTFT', 'STKH', 'RMTI', 'WEN', 'V', 'RYAM', 'AEP', 'TAP', 'PM', 'LOW', 'ALLO', 'DRH', 'AR', 'HBB', 'LESL', 'TELL', 'VTS', 'GLD', 'ASX', 'CCJ', 'STNE', 'NAT', 'SEE', 'NET', 'EA', 'EVA', 'LMB', 'BN', 'IEF', 'DELL', 'DADA', 'CX', 'RFL', 'DOW', 'INDI', 'DASH', 'ISEE', 'KWEB', 'XOP', 'TBLA', 'BX', 'FTV', 'PAYX', 'CL', 'XLU', 'LQD', 'STLA', 'MCHX', 'MSTR', 'ALLY', 'SU', 'HST', 'MULN', 'DLO', 'ONB', 'ACB', 'ABBV', 'FHN', 'XLI', 'AI', 'ORCL', 'CNET', 'BILI', 'COMP', 'EWZ', 'DSEY', 'WOW', 'BABA', 'BA', 'TLRY', 'EEM', 'SQQQ', 'CS', 'ANSS', 'NTCO', 'RIOT', 'KGC', 'TSP', 'BRDG', 'SKY', 'CSX', 'IBM', 'XIN', 'NEX', 'AAP', 'MCD', 'WRAP', 'LUMN', 'RPRX', 'BLDR', 'RXT', 'LABU', 'SYF', 'RPD', 'SGBX', 'RVLP', 'NXE', 'FNCB', 'SYPR', 'DVN', 'AQN', 'ONON', 'CNX', 'AGI', 'SPY', 'SVM', 'XLE', 'APPS', 'FRHC', 'AGEN', 'IOT', 'ZIM', 'BHC', 'ACN', 'AAL', 'SNAP', 'AFL', 'CRDO', 'BLNK', 'BOWL', 'VRAY', 'TRTX', 'ELAN', 'EOSE', 'UVXY', 'ZYNE', 'MQ', 'LYFT', 'ENVX', 'NKE', 'TNP', 'SAND', 'VZ', 'IWM', 'GE', 'XME', 'HTHT', 'XLK', 'GT', 'FAST', 'GLNG', 'IYR', 'DAL', 'KPTI', 'GS', 'BLDP', 'AVTR', 'BAC', 'NEWR', 'USAP', 'API', 'ANET', 'CRNT', 'LXP', 'SHLS', 'IP', 'BMBL', 'S', 'BFLY', 'LBTYK', 'LNT', 'DHT', 'CCO', 'NTAP', 'DOC', 'NGVC', 'PD', 'LAW', 'GTBP', 'RTX', 'BAX', 'LLY', 'FFIE', 'FLNT', 'PEG', 'FLO', 'COIN', 'CLOV', 'YMM', 'ETRN', 'IMAX', 'HSKA', 'WFC', 'GH', 'NEM', 'HITI', 'SSTI', 'EXPE', 'PFE', 'PATH', 'MFIN', 'ZTO', 'SGEN', 'UPRO', 'BCRX', 'CSIQ', 'ALIT', 'KOLD', 'AFRM', 'RXRX', 'TLT', 'NGM', 'OCGN', 'CTRA', 'FE', 'VERA', 'UDR', 'EVLV', 'XLC', 'NLY', 'TMF', 'GRAB', 'HAL', 'BITO', 'VALE', 'GSM', 'LBRDK', 'PRU', 'DNB', 'BP', 'HTZ', 'PXLW', 'CHWY', 'HYFM', 'LMNL', 'STT', 'ST', 'BGFV', 'FUBO', 'RUN', 'XLY', 'CGC', 'EFC', 'CNP', 'DISH', 'MANU', 'CVNA', 'AAOI', 'FSR', 'SANW', 'MREO', 'W', 'TMO', 'USB', 'DE', 'TDCX', 'ITRI', 'ZDGE', 'FXLV', 'ROKU', 'AVAH', 'PINS', 'VOD', 'SLP', 'PDS', 'AESI', 'CMCSA', 'PR', 'INTC', 'XLV', 'TSLA', 'WMB', 'OXY', 'IONQ', 'AMH', 'PLTR', 'ALEC', 'ACI', 'OSS', 'BIVI', 'JPM', 'MGNX', 'SPWR', 'LMT', 'SCPL', 'DLTR', 'ED', 'HPQ', 'LAZR', 'OSK', 'AIRS', 'FHTX', 'INSE', 'X', 'ADP', 'VMW', 'HRTG', 'BRLT', 'RDFN', 'ITUB', 'ETON', 'BIG', 'RCL', 'CBAT', 'RRC', 'ARR', 'SLI', 'ETN', 'OPEN', 'SENS', 'OWL', 'HBI', 'NVAX', 'DEI', 'ARMK', 'XRT', 'WEX', 'LSCC', 'LRCX', 'GOOS', 'IVZ', 'TLSA', 'APA', 'ROST', 'SLM', 'CERS', 'LGMK', 'DDOG', 'KMI', 'BTCM', 'AXLA', 'BTE', 'PAGS', 'FNGS', 'CRWD', 'ENOB', 'MGI', 'CMA', 'KHC', 'SGMO', 'WYNN', 'HYG', 'IOVA', 'ENSV', 'AMLX', 'VZIO', 'F', 'CIM', 'NFLX', 'ASC', 'WAL', 'AUMN', 'SOFI', 'DFS', 'TFC', 'FATE', 'JCI', 'CPB', 'HUT', 'CFG', 'IRIX', 'SKX', 'KSS', 'NRG', 'HZO', 'MCHP', 'AMX', 'KMB', 'MO', 'SPXS', 'IBRX', 'T', 'LC', 'MMAT', 'FUSN', 'FYBR', 'PEAK', 'CROX', 'PRDO', 'AMD', 'AEM', 'IFF', 'AMBA', 'U', 'CUZ', 'BOIL', 'XLF', 'EQT', 'DHI', 'AMZN', 'EGO', 'SOXS', 'VTGN', 'BBWI', 'FOXA', 'ASRT', 'GSAT', 'TXN', 'SPWH', 'HR', 'PDD', 'NVTS', 'ESI', 'KDP', 'DB', 'ERIC', 'OGN', 'SOXL', 'UPST', 'WOOF', 'PENN', 'ARAV', 'AIN', 'TPR', 'VKTX', 'MS', 'TIGR', 'GTLB', 'TSN', 'IRS', 'MA', 'GDXJ', 'FANH', 'UUP', 'FTCI', 'UNG', 'ETSY', 'KO', 'PAA', 'DNN', 'AA', 'TJX', 'ARRY', 'AM', 'CVE', 'AIG', 'COTY', 'LNG', 'TSM', 'NWL', 'BRFS', 'WTI', 'COST', 'AGNC', 'MTLS', 'RF', 'TOST', 'WBD', 'HLIT', 'MRNA', 'BMY', 'Z', 'TGT', 'XOM', 'URBN', 'DIS', 'SSSS', 'ENIC', 'DBRG', 'VXX', 'MLCO', 'RYN', 'ANF', 'ORC', 'LULU', 'SLG', 'SAVE', 'XENE', 'VERX', 'GEN', 'BIDU', 'SONO', 'GPRK', 'GP', 'NM', 'UAL', 'RITM', 'FXI', 'UPS', 'GURE', 'REXR', 'AAPL', 'SLB', 'MITT', 'IMBI', 'ODV', 'NEE', 'MESA', 'AEO', 'TQQQ', 'MRVL', 'SIG', 'ULTA', 'FDX', 'BB', 'ABR', 'EL', 'BEN', 'SIMO', 'PBR', 'CRBP', 'CAH', 'USO', 'SLV', 'META', 'GOLD', 'HPE', 'JFIN', 'EGHT', 'IEP', 'NTR', 'SID', 'SMWB', 'SPCE', 'ESLT', 'XBI', 'MSOS', 'CVX', 'RXST', 'CVT', 'AMRS', 'MTG', 'PRM', 'CHS', 'EPIX', 'COLB', 'ATUS', 'GM', 'MET', 'HZNP', 'SHEL', 'EQH', 'AMRN', 'PARA', 'ICLN', 'TARS', 'GFI', 'BEKE', 'NIO', 'GOEV', 'NCLH', 'EMB'], embeds=str):
        self.ticker = tickers
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.persistent_views_added = False
        self.embeds = []

    async def on_ready(self):
        if not self.persistent_views_added:
            # Register the persistent view for listening here.
            # Note that this does not send the view to any message.
            # In order to do this you need to first send a message with the View, which is shown below.
            # If you have the message_id you can also pass it as a keyword argument, but for this example
            # we don't have one.
            self.add_view(AvoidView())
            self.add_view(PageTwoView())
            self.add_view(PageThreeView())
            self.add_view(CommandsStart())
            self.add_view(MenuStart())
            self.add_view(CoreStart())
            self.add_view(AlertStart())
            self.add_view(LitStart())
            self.add_view(DiscordStart())
            self.add_view(TAStart())
            self.add_view(MarketsView())
            self.add_view(CryptoViewStart())
            self.add_view(ForexViewStart())
            self.add_view(HighShortsViewStart())
            self.add_view(LowFloatDropdown())
            self.add_view(AlertMenus(embeds=self.embeds))
            self.add_view(FTDViewStart())
            self.add_view(LosersViewStart())
            self.add_view(GainersViewStart())
            self.add_view(ActiveViewStart())
            self.add_view(TotalOIViewStart())
            self.add_view(TotalVolumeViewStart())
            self.add_view(LinksStartView())
            self.add_view(AppStart())
            self.add_view(TopOptionsViewStart())
            self.add_view(WebullCmdViewStart())
            self.add_view(OptionCmdViewStart())
            self.add_view(PermaFTDViewStart())
            self.add_view(OFRViewStart())
            self.add_view(DDCmdViewStart())
            self.add_view(FlowCmdViewStart())
            self.add_view(DPSCmdViewStart())
            self.add_view(EconomyCmdViewStart())
            self.add_view(EarningsCmdViewStart())
            self.add_view(FlowCmdViewStart())
            self.add_view(StreamCmdViewStart())
            self.add_view(ChartingCmdViewStart())
            self.add_view(StockCmdViewStart())
            self.add_view(HelpStart())
            self.add_view(LearnCmdViewStart())
            self.add_view(ToolsViewStart())
            self.add_view(NYSEViewStart())
            self.add_view(DTCCViewStart())
            self.add_view(CBOEViewStart())
            self.add_view(StockPage1())
            self.add_view(StockPage2())
            self.add_view(StockPage3())
            self.add_view(StockPage4())
            self.add_view(StockPage5())
            self.add_view(TopIVViewStart())
            self.add_view(TopOIDownViewStart())
            self.add_view(TopOIUpViewStart())
            self.add_view(TotalTurnoverViewStart())
            self.add_view(TopVolumeViewStart())
            self.add_view(TopOIViewStart())
            self.add_view(VideoStartView())
            self.add_view(VideoStart3View())
            self.add_view(VideoStart2View())
            self.add_view(OFRDataViewStart())
            self.add_view(AgencyViewStart())
            self.add_view(DataViewStart())
            self.add_view(InflationDataStart())
            self.add_view(BlockchainDataStart())
            self.add_view(HKEXDataStart())
            self.add_view(FINRADataStart())
            self.add_view(MMFDataStart())
            self.add_view(FedDataStart())
            self.add_view(TreasuryDataStart())
            self.add_view(EconomicDataStart())
            self.add_view(RepoDataStart())
            self.add_view(RepoCitedViewStart())
            self.add_view(CriteriaView())
            self.add_view(AvoidView())
            self.add_view(ServerMenuView())


            self.persistent_views_added = True


        print(f"Logged in as {self.user} (ID: {self.user.id})")





bot = PersistentViewBot(command_prefix=">>", intents=intents)
skew_cmds = Skew(bot=bot)
analysis_cmds = Analysis(bot)
learn_cmds = Learn(bot)
ss_cmds = SS(bot)
fmp_cmds = FMP(bot)




stock_market = PolygonStockMarket()

class RsiHourOption(OptionChoice):
    name = "rsi_hour"
    description = "Get the RSI for the specified hour"
    type = OptionType.sub_command
    options = [
        Option(
            name="ticker",
            description="Ticker to get RSI for",
            type=OptionType.string,
            required=True
        )
    ]

@bot.command()
async def gpt4(ctx: commands.Context, prompt: str, ticker=None):
    # Step 1: Send the conversation and available functions to GPT
    messages = [{"role": "user", "content": prompt}]
    functions = [
        {
            "name": "analyze_data",
            "description": "Analyze the given data to determine the likely direction.",
            "parameters": {
                "type": "object",
                "properties": {
                    "ticker": {
                        "type": "string",
                        "description": f"The ticker to query. {ticker}",
                    },
                },
                "required": ["ticker"],
                "returns": {
                    "type": "object",
                    "properties": {
                        "strike_price": {
                            "type": "string",
                            "description": "The strike price of the option symbol."
                        },
                        "expiration": {
                            "type": "string",
                            "description": "The expiration date of the option symbol."
                        },
                        "implied_volatility": {
                            "type": "number",
                            "description": "The implied volatility of the option symbol."
                        },
                        "theta": {
                            "type": "number",
                            "description": "The theta value."
                        },
                        "gamma": {
                            "type": "number",
                            "description": "The gamma value."
                        },
                        "delta": {
                            "type": "number",
                            "description": "The delta value."
                        },
                        "vega": {
                            "type": "number",
                            "description": "The vega value."
                        },
                        "change_percent": {
                            "type": "number",
                            "description": "The contract's performance."
                        },
                        "ask": {
                            "type": "number",
                            "description": "The ask price."
                        },
                        "bid": {
                            "type": "number",
                            "description": "The bid price."
                        },
                        "ask_size": {
                            "type": "number",
                            "description": "The size of the ask."
                        },
                        "bid_size": {
                            "type": "number",
                            "description": "The size of the bid."
                        },
                        "volume": {
                            "type": "number",
                            "description": "The volume of the option."
                        },
                        "open_interest": {
                            "type": "number",
                            "description": "The open interest for the option."
                        }
                    }
                }
            }
        }
    ]

    while True:
        # Send user message and get GPT's response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
            functions=functions,
            function_call="auto",
        )
        response_message = response["choices"][0]["message"]
        await ctx.send(response_message["content"])

        # Check if GPT wanted to call a function
        if response_message.get("function_call"):
            # Call the function
            available_functions = {
                "analyze_data": analyze_data,
            }
            function_name = response_message["function_call"]["name"]
            function_to_call = available_functions[function_name]
            function_args = json.loads(response_message["function_call"]["arguments"])
            function_response = await function_to_call(**function_args)
            await ctx.send(str(function_response))

            # Convert function_response to a string format
            function_response_str = str(function_response)

            # Send the info on the function call and function response to GPT
            messages.append(response_message)  # Extend conversation with assistant's reply
            messages.append(
                {
                    "role": "function",
                    "name": function_name,
                    "content": function_response_str,
                }
            )
        else:
            # Send the user message and GPT's response to continue the conversation
            messages.append(response_message)  # Extend conversation with assistant's reply

        # Check if the user wants to stop the conversation
        user_input = await bot.wait_for("message", check=lambda m: m.author == ctx.author)
        user_input = user_input.content
        if user_input.lower() == "stop":
            break  # Exit the loop if the user inputs "Stop"

        # Add the user's message to the conversation
        messages.append({"role": "user", "content": user_input})


@bot.slash_command()

async def get_live_trades(inter:disnake.AppCmdInter, subscription: str = commands.Param(choices=["trades", "quotes", "aggregates"])):
    if subscription == "trades":
        
        await stock_market.run_stream(subscriptions="T.*", inter=inter)
        await inter.edit_original_message(WebSocketMessage)

    elif subscription == "quotes":
        await stock_market.run_stream(subscriptions="Q.*", inter=inter)
 




    """Stream live trades directly from the polygon cluster."""

    await inter.edit_original_message(WebSocketMessage)
    



@bot.slash_command()
async def test(inter: disnake.AppCommandInter, command:str=commands.Param(autocomplete=command_autocomp)):

    if command == "all_options":
        await inter.send(f"> **Click to Run:**\n> </all_options:1122312195154387024>")
    elif command == "learn discord":
        await learn_cmds.discord(inter)
    elif command == "learn_order_types":
        await learn_cmds.order_types(inter)
    elif command == "learn_core_logic":
        await learn_cmds.core_logic(inter)
    elif command == "learn_filings":
        await learn_cmds.filings(inter)
    elif command == "learn_cmds.calls":
        await learn_cmds.calls(inter)
    elif command == "learn_etfs":
        await learn_cmds.etfs(inter)
    elif command == "learn_greeks":
        await learn_cmds.greeks(inter)
    elif command == "learn_china":
        await learn_cmds.china(inter)
    elif command == "learn_options_101":
        await learn_cmds.options_101(inter)
    elif command == "learn_option_strategies":
        await learn_cmds.option_strategies(inter)
    elif command == "learn_core_logic":
        await learn_cmds.core_logic(inter)
    elif command == "learn_covered_calls":
        await learn_cmds.covered_calls(inter)
    elif command == "learn_nsfr_ratio":
        await learn_cmds.nsfr_ratio(inter)
    elif command == "learn_candle_patterns":
        await learn_cmds.candle_patterns(inter)
    elif command == "learn_occ":
        await learn_cmds.occ(inter)
    elif command == "learn_criteria":
        await learn_cmds.criteria(inter)
    elif command == "learn_ta":
        await learn_cmds.ta(inter)
    elif command == "learn_finra":
         await learn_cmds.finra(inter)      

    elif command == "analysis_gaps_up":
        await inter.send(f"**Click to Run:**\n> </analysis gaps_up:1122243463723876533>")
    
    elif command == "analysis_gaps_down":
        await inter.send(f"**Click to Run:**\n> </analysis gaps_down:1122243463723876533>")
    


    elif command == "analysis_overbought_gap":
        
        await inter.send(f"**Click to Run:**\n> </analysis overbought_gap:1122243463723876533>")

    elif command == "analysis_topshorts":
        await analysis_cmds.topshorts(inter)


    elif command == "rsi":
        await inter.send(f"> **Click to Run:**\n> </ta rsi_snapshot:1122650723021238362>")


      

    elif command == "company_information":
        await inter.send(f"> **Click to Run:**\n> </poly company_info:1122243463862300754")



    elif command == "earnings_calendar":
        await ss_cmds.earnings(inter)

    elif command == "insider_trading_market_wide":
        await ss_cmds.insider_summary(inter)


    elif command == "daily_treasury_balance":
        await ss_cmds.treasury(inter)

    elif command == "inflation":
        await ss_cmds.inflation(inter)

    elif command == "jobless_claims":
        await ss_cmds.jobless_claims(inter)

    elif command == "market_news":
        await ss_cmds.market_news(inter)

    elif command == "short_volume":
        await inter.send(f"> **Click to run:**\n> </ss short_volume:1122243463862300759>")


    elif command == "reverse_repo":
        await ss_cmds.reverse_repo(inter)




    elif command =="low_floats":
        await ss_cmds.low_floats(inter)


    elif command == "short_interest":

        await ss_cmds.short_interest(inter)



    elif command == "news_sentiment":
        await inter.send(f"> **Click to Run:**\n> </ss news_sentiment:1122243463862300759>")



    elif command == "sec_filings":
        await inter.send(f"> **Click to Run:**\n> </ss sec_filings:1122243463723876533>")

        

    elif command == "short_interest":
        await ss_cmds.short_interest(inter)


    elif command == "price_target":
        await inter.send(f"> **Click to Run:**\n> </fmp price_target:1122711896773103698>")
    elif command == "subreddits":
        await inter.send(f"> **Click to Run:**\n> </ss subreddits:1122243463862300759>")
async def get_option_calls(ticker):
    url = f"https://api.polygon.io/v3/reference/options/contracts?underlying_ticker={ticker}&limit=1000&apiKey={YOUR_API_KEY}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url):
            results = await polygon._request_all_pages(url)
            if results is not None:
                data = CallsOrPuts(results, ticker)
                print(data.df)
                return data.df

# Global dictionary to store user's tickers





@bot.slash_command()
async def all_spx(ctx: disnake.AppCommandInter):
    await ctx.response.defer(with_message=True)
    ticker = "SPX"

    def chunk_list(input_list, chunk_size):
        """Yield successive n-sized chunks from a list."""
        for i in range(0, len(input_list), chunk_size):
            yield input_list[i:i + chunk_size]
    if ticker.startswith("SPX"): #check if the ticker is SPX - must be queried differently
        price = await polygon.get_index_price(ticker)
        lower_strike = round(price) * 0.98
        upper_strike = round(price) * 1.02
        print(f"SPX TICKER: {ticker}: {lower_strike}, {price}, {upper_strike}")
        
        async with aiohttp.ClientSession() as session:
            initial_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte=2023-06-27&expiration_date.lte={two_years_from_now_str}&limit=250&apiKey={YOUR_API_KEY}"
            async with session.get(initial_url) as resp:
                results = await polygon._request_all_pages(initial_url)
                if results is not None:
                    option_data = UniversalOptionSnapshot(results)


                    
                    # Assuming option_data.ticker gives a list of tickers
      
                    symbols_list = option_data.ticker
                    chunks = list(chunk_list(symbols_list, 250))

                    # Create a dictionary to hold results grouped by expiration date
        
                    for chunk in chunks:
                        # Use chunk for API request
                        # Each chunk will contain max 250 items
                        chunk = str(chunk).replace("'","").replace(']','').replace('[','').replace(' ','')
                        initial_url = f"https://api.polygon.io/v3/snapshot?ticker.any_of={chunk}&apiKey={YOUR_API_KEY}"
                        async with session.get(initial_url):

                            near_money = await polygon._request_all_pages(initial_url)
                            near_money_results = near_money['results']
                            print(near_money_results)
                            atm_data = UniversalSnapshot(near_money_results)
                            # Append DataFrame to the list
                            atm_data.df.to_csv('atm_spx.csv')
                            await ctx.send(file=disnake.File('atm_spx.csv'))  # Print the DataFrame for debugging
        




# @bot.slash_command(name="allskew")
# async def allskew(inter: disnake.AppCmdInter):
#     """Scan multiple skews in real time"""
#     tickers = [
#         'COIN', 'WFC', 'GM', 'PYPL', 'CVS', 'CVX', 'BKNG', 'NVDA', 'AMD', 'MSFT',
#         'META', 'U', 'W', 'ADBE', 'MSTR', 'LLY', 'BLK', 'MCD', 'WMT', 'TGT', 'SPY',
#         'F', 'SHOP', 'SNAP', 'AMC', 'GME', 'BABA', 'BIDU', 'JD', 'NFLX', 'AMZN',
#         'BAC', 'KRE', 'EWZ', 'M', 'SO', 'KO', 'PEP', 'CSCO', 'COST', 'SBUX', 'BBY',
#         'SQQQ', 'QQQ', 'TQQQ', 'EEM', 'CHZ', 'HYG', 'TSLA', 'AMD', 'QCOM', 'INTC'
#     ]

#     await inter.response.defer()

#     counter = 0
#     while True:
#         counter += 1

#         # Get prices for all tickers concurrently
#         price_tasks = [polygon.get_stock_price(ticker) for ticker in tickers]
#         prices = await asyncio.gather(*price_tasks)
#         ticker_prices = dict(zip(tickers, prices))  # Assuming no None prices
#         print(ticker_prices)

#         # Now get option data concurrently
#         option_data_tasks = [
#             poly_options.get_option_data(ticker, ticker_prices[ticker]) for ticker in tickers
#         ]
#         results = await asyncio.gather(*option_data_tasks)
#         print(results)

#         # Filter out None results and add valid results to data_list
#         data_list = [result for result in results if result is not None]
#         data_list = sorted(data_list, key=lambda x: x[6], reverse=True)

#         # Create a new list that only includes the parts you want to display
#         display_data = [row[:7] for row in data_list]

#         # Now, display_data contains the data you want to display for all tickers.
#         # Format it into a table and send it in discord chat.
#         table = tabulate(display_data, headers=['Symbol', 'Skew', ' ', 'Price', 'Expiry', 'IV', 'Vol','Skew Metric'], tablefmt='fancy')

#         embed = disnake.Embed(
#             title=f"All - Skew",
#             description=f"```\n" + table + "\n```",
#             color=disnake.Colour.random()
#         )
#         embed.set_footer(text=f"{counter} | Data Provided by Polygon.io | Implemented by FUDSTOP")
#         await inter.edit_original_message(embed=embed)  # Send the table in a code block

#         if counter == 100:
#             await inter.send(f"> **Click to Run:**\n> </allskew:1121980575276879983>")
#             break




class ServerMenu(disnake.ui.ChannelSelect):
    def __init__(self):
        
        super().__init__(custom_id="ServerMenuSel",placeholder="Select A Channel!",min_values=1,max_values=1,channel_types=[disnake.ChannelType.forum])

    async def callback(self, interaction: disnake.ApplicationCommandInteraction):
        if self.values:
            selected_channel = self.values[0]
            embed = disnake.Embed(title=f"{emojis.ls}{emojis.le}{emojis.lr}{emojis.lv}{emojis.le}{emojis.lr}🌟{emojis.lm}{emojis.le}{emojis.ln}{emojis.lu}")
            
            await interaction.send(f"The selected channel is: {selected_channel.mention}", ephemeral=False)
        else:
            await interaction.send("No channel was selected!", ephemeral=False)


class ServerMenuView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(ServerMenu())
        self.add_item(TextMenu())
        self.add_item(ThreadMenu())

class ServerMenu(disnake.ui.ChannelSelect):
    def __init__(self):
        
        super().__init__(custom_id="ServerMenuSel2", placeholder="Select or Search for a Forum Channel!", min_values=1, max_values=1, channel_types=[disnake.ChannelType.forum])

    async def callback(self, interaction: disnake.ApplicationCommandInteraction):
        if self.values:
            selected_channel = self.values[0]
            await interaction.send(f"The selected channel is: {selected_channel.mention}", delete_after=10)
        else:
            await interaction.send("No channel was selected!", delete_after=10)


class TextMenu(disnake.ui.ChannelSelect):
    def __init__(self):
        
        super().__init__(custom_id="ServerMenuSel3", placeholder="Select or Search for a Text Channel!", min_values=1, max_values=1, channel_types=[disnake.ChannelType.text])

    async def callback(self, interaction: disnake.ApplicationCommandInteraction):
        if self.values:
            selected_channel = self.values[0]
            await interaction.send(f"The selected channel is: {selected_channel.mention}", delete_after=10)
        else:
            await interaction.send("No channel was selected!", ephemeral=False)


class ThreadMenu(disnake.ui.ChannelSelect):
    def __init__(self):
        
        super().__init__(custom_id="ServerMenuSel4", placeholder="Select or Search for a Thread!", min_values=1, max_values=1, channel_types=[disnake.ChannelType.public_thread])

    async def callback(self, interaction: disnake.ApplicationCommandInteraction):
        if self.values:
            selected_channel = self.values[0]
            await interaction.send(f"The selected channel is: {selected_channel.mention}", delete_after=10)
        else:
            await interaction.send("No channel was selected!", ephemeral=False)


@bot.slash_command()
async def data(inter:disnake.AppCmdInter, ticker: str):
    """Launch the terminal."""
    ticker = ticker.upper()
    logo = await polygon.get_polygon_logo(ticker)
    view = MainView(bot, ticker)
    totals = await fudstop.option_market_totals()

    f2high=float(totals.fiftytwohigh)
    f2low=float(totals.fiftytwolow)
    futures=float(totals.futures_vol)
    mdaily=float(totals.monthlydailyavg)
    optvol=float(totals.optionsVol)
    ydaily=float(totals.yearlydailyavg)

    embed = disnake.Embed(title=f"{emojis.redline} Data Ready {emojis.redline}", description=f"```py\nWelcome. Before you look at {ticker}'s data - here are the total option stats on the day:```", color=disnake.Colour.old_blurple())
    embed.add_field(name=f"Today's Volume Summary:", value=f"> {emojis.alert} Futures: **{futures:,}**\n> {emojis.redline} 52w High: **{f2high:,}**\n\n> {emojis.webullcmd} Today: **{optvol:,}**\n\n> {emojis.redline} 52w Low: **{f2low:,}**")
    embed.add_field(name=f"Averages:", value=f"> Monthly-Daily: **{mdaily:,}**\n> Yearly-Dayly: **{ydaily:,}**", inline=False)
    embed.set_thumbnail(logo)
    embed.set_footer(text=f"Viewing data for {ticker} | Data Provided by Polygon.io -")


    await inter.send(view=view, embed=embed)



@bot.slash_command()
async def cmds(ctx: disnake.AppCommandInter):
    """Views the server commands from all bots."""
    # Create a list of embeds
    embeds = [
        disnake.Embed(title=f"FUDSTOP Commands - Webull", description=f"```py\nYou are viewing fudstop commands regarding webull. Learn how to use the Webull App, customize it, and view several graphics such as TA, Trend Analysis, Candlestick analysis, and general market knowledge.```\n> The webull commands can be accessed by using:\n\n> **/webull**"),
        disnake.Embed(title=f"FUDSTOP Commands - Stocksera", description=f"```py\nYou are viewing the fudstop implemented commands from the Stocksera API. View economic data, FTDs, low floats, short interest, short volume, social media chatter and more.```\n> The Stocksera commands can be access by using:\n\n> **/ss**"),
        disnake.Embed(title=f"FUDSTOP Commands - Analysis", description=f"```py\nYou are viewing FUDSTOP Implemented commands from finviz. Analyze technicals and patterns with the analysis commands.```"),
        disnake.Embed(title=f"FUDSTOP Commands - Learn", description=f"```py\nYou are viewing FUDSTOP Learn commands which has a multitude of information from webull guides to SEC Filings, and videos from my channel.```"),
        disnake.Embed(title=f"FUDSTOP Commands - Agencies", description=f"```py\nYou are viewing FUDSTOP implemented commands from the Federal Reserve of New York's API, the Options Clearing Corporation API, and the Office of Financial Research API. View economic data, repo data, and others straight from the source.```"),
        disnake.Embed(title=f"FUDSTOP Commands - School", description=f"```py\nYou are viewing FUDSTOP school commands which aim to help educate the viewer by providing an interactive application where you can select the content via buttons.```"),
        disnake.Embed(title=f"FUDSTOP Commands - Options", description=f"```py\nYou are viewing the FUDSTOP Implemented options commands from polygon.io. This is being actively revamped. Stay tuned!```"),
        disnake.Embed(title=f"FUDSTOP Commands - FMP", description=f"```py\n Viewing commands from the Financial Modeling Prep API. Will be actively building this section which will contain many areas of data analytics.```"),
        disnake.Embed(title=f"FUDSTOP Commands - Other", description=f"```py\n Skews, bananas, GPT4, and other FUDSTOP-originated commands can be found here.```"),
        disnake.Embed(title=f"FUDSTOP Commands - Stream", description=f"```py\n Viewing commands that stream live data - from stock and crypto prices to live options volume. (coming soon).```"),
        disnake.Embed(title=f"FUDSTOP Commands - Stock", description=f"```py\n Viewing commands that stream live data - from stock and crypto prices to live options volume. (coming soon).```"),
        disnake.Embed(title=f"FUDSTOP Commands - Navigation", description=f"```py\n Easily navigate throughout the server by utilizing the navigation commands. You can search threads, forums, or channels.```"),
        disnake.Embed(title=f"Open BB - Charting", description=f"```py\nView these commands from OpenBB that allow you to chart right from discord.```"),
        disnake.Embed(title=f"Open BB - Economy", description=f"```py\nView these commands for getting economic data from Open BB.```"),
        disnake.Embed(title=f"Open BB - Due Diligence", description=f"```py\nView these commands for getting earnings info, split, company financials, company bio, and more.```"),
        disnake.Embed(title=f"Open BB - Dark Pools", description=f"```py\nView these commands to call data related to dark pools.```"),
        disnake.Embed(title=f"Open BB - Flow", description=f"```py\nView commands relating to money flow, premium, options summaries - and more.```"),
        disnake.Embed(title=f"Open BB - Options", description=f"```py\nView these commands to chart open interest, volume, view option stats, option history, volatiltiy, and more.```")
    ]

    # Add fields to a specific embed (e.g., the second embed at index 1)
    fudstop_webull = 0
    fudstop_stocksera = 1
    fudstop_analysis = 2
    fudstop_learn = 3
    fudstop_agencies = 4
    fudstop_school = 5
    fudstop_opts = 6
    
    fudstop_fmp = 7
    fudstop_other = 8
    fudstop_stream = 9
    fudstop_stock = 10
    fudstop_nav = 11
    openbb_charting = 12
    openbb_economy = 13
    openbb_dd = 14
    openbb_dp = 15
    openbb_flow = 16
    openbb_op = 17

    webull_commands = embeds[fudstop_webull]
    webull_commands.add_field(name="Analysis Tools", value="> View webull tools pertaining to how to utilize data analysis tools.\n> Click to use:\n\n</webull analysis_tools:1122243464042659942>", inline=True)
    webull_commands.add_field(name="Bid/Ask Spread", value="> Learn about the bid ask spread.\n> Click to use:\n\n</webull bid_ask_spread:1122243464042659942>", inline=True)
    webull_commands.add_field(name="Graphics", value="> View several webull graphics such as TA, Chart Patterns, and more.\n> Click to use:\n\n</webull graphics:1122243464042659942>", inline=True)
    webull_commands.add_field(name="Options Chain", value="> Learn about the Webull Option Chain and how to use it.\n> Click to use:\n\n</webull options_chain:1122243464042659942>", inline=True)
    webull_commands.add_field(name="Options Setup", value="> Learn how to cutsomize your webull options chart.\n> Click to use:\n\n> </webull options_setup:1122243464042659942>", inline=True)
    webull_commands.add_field(name="Orders", value="> Learn about the different market order types.\n> Click to use:\n\n</webull orders:1122243464042659942>", inline=True)
    webull_commands.add_field(name="Paper Trading", value="> Learn about paper trading and options paper trading via Webull.\n> Click to use:\n\n</webull paper_trading:1122243464042659942>", inline=True)
    webull_commands.add_field(name="Volume Analysis", value="> Returns a live stream of the input ticker's volume analysis on the day.\n> Click to use:\n\n</webull volume_analysis:1122243464042659942>", inline=True)
    webull_commands.add_field(name=f"News Announcement", value=f"> Get the latest market news for a ticker.\n\n</webull news_announcement:1122243464042659942>")


    stocksera_commands = embeds[fudstop_stocksera]
    stocksera_commands.add_field(name=f"Earnings", value=f"> Returns earnings tickers for the given date range.\n> Click to use:\n\n</ss earnings_calendar:1122243463862300759>")
    stocksera_commands.add_field(name=f"FTDs", value=f"> Search market-wide FTDs ranked by highest to lowest with T+35 dates.\n> Click to use:\n\n</ss fails_to_deliver_market_wide:1122243463862300759>")
    stocksera_commands.add_field(name=f"Inflation", value=f"> Returns historic inflation up to the current day dated back to 1977.\n> Click to use:\n\n</ss inflation:1122243463862300759>")
    stocksera_commands.add_field(name=f"Insider Summary", value=f"> View the latest insider trades across the market.\n> Click to use:\n\n</ss insider_trading_market_wide:1122243463862300759>")
    stocksera_commands.add_field(name=f"Jobless Claims", value=f"> View the latest and historic jobless claims numbers.\n> Click to use:\n\n</ss jobless_claims:1122243463862300759>")
    stocksera_commands.add_field(name=f"Low Floats", value=f"> Returns tickers with extremely low free floats.\n> Click to use:\n\n</ss low_floats:1122243463862300759>")
    stocksera_commands.add_field(name=f"Market News", value=f"> Return market-wide news to track narratives.\n> Click to use:\n\n</ss market_news:1122243463862300759>")
    stocksera_commands.add_field(name=f"News Sentiment", value=f"> View headlines for a ticker and the underlying sentiment.\n> Click to use:\n\n</ss news_sentiment:1122243463862300759>")
    stocksera_commands.add_field(name=f"Reverse Repo", value=f"> View the latest and historic repo numbers from the FED.\n\n</ss reverse_repo:1122243463862300759>")
    stocksera_commands.add_field(name=f"SEC Filings", value=f"> View the latest SEC Filings for a ticker.\n> Click to use:\n\n</ss sec_filings:1122243463862300759>")
    stocksera_commands.add_field(name=f"Short Interest", value=f"> View tickers with high % of their float shorted.\n> Click to use:\n\n</ss short_interest:1122243463862300759>")
    stocksera_commands.add_field(name=f"Short Volume", value=f"> View a stock's latest and historic short volume.\n> Click to use:\n\n</ss short_volume:1122243463862300759>")
    stocksera_commands.add_field(name=f"Stocktwits", value=f"> Return a ticker's rank on StockTwits.\n> Click to use:\n\n</ss stocktwits:1122243463862300759>")
    stocksera_commands.add_field(name=f"Subreddits", value=f"> View a ticker's popular subreddit / active users and rank.\n> Click to use:\n\n</ss subreddits:1122243463862300759>")

    chart_commands = embeds[openbb_charting]
    chart_commands.add_field(name=f"Chart 3 Minute", value=f"> Charts a ticker on the 3 minute timeframe.\n\n</c3m:1004263746090324062>")
    chart_commands.add_field(name=f"Chart 5 Minute", value=f"> Charts a ticker on the 5 minute timeframe.\n\n</c5m:1004263746090324063>")
    chart_commands.add_field(name=f"Chart 15 Minute", value=f"> Charts a ticker on the 15 minute timeframe.\n\n</c15m:1004263746090324064>")
    chart_commands.add_field(name=f"Chart Daily", value=f"> Charts a ticker on the daily timeframe.\n\n</cd:1004263746090324061>")
    chart_commands.add_field(name=f"Chart Week", value=f"> Charts a ticker on the weekly timeframe.\n\n</cw:1004263746090324060>")
    chart_commands.add_field(name=f"Chart Custom", value=f"> Charts a ticker with custom timeframe.\n\n</chart:1004263746090324065>")
    chart_commands.add_field(name=f"Chart FIB", value=f"> Charts the fibbonaci for a ticker.\n\n</chartfib:1007163283276562512>")
    chart_commands.add_field(name=f"Chart Support & Resistance", value=f"> Charts support/resistance for a given ticker.\n\n</chartsr:1009175257590026281>")
  
    econ_commands = embeds[openbb_economy]
    econ_commands.add_field(name=f"Reverse Repo", value=f"> Get the latest reverse repo data.\n\n</econ revrepo:1004263746111275130>")
    econ_commands.add_field(name=f"Economic Calendar", value=f"> Displays a calendar of economic events.\n\n</econ calendar:1004263746111275130>")
    econ_commands.add_field(name=f"Commodities", value=f"> Futures and comoddities overview.\n\n</econ commodities:1004263746111275130>")
    econ_commands.add_field(name=f"Currencies", value=f"> Currencies overview.\n\n</econ currencies:1004263746111275130>")
    econ_commands.add_field(name=f"Fed Rates", value=f"> Upcoming Federal Rates decision with percent chance.\n\n</econ fedrates:1004263746111275130>")
    econ_commands.add_field(name=f"Global Bonds", value=f"> Global Bonds Overview.\n\n</econ glbonds:1004263746111275130>")
    econ_commands.add_field(name=f"Indicies", value=f"> Indices overview.\n\n</econ indices:1004263746111275130>")
    econ_commands.add_field(name=f"US Bonds", value=f"> Us bonds overview.\n\n</econ usbonds:1004263746111275130>")
    econ_commands.add_field(name=f"Yield Curve", value=f"> Displays US Bonds and Yield Curve.\n\n</econ yieldcurve:1004263746111275130>")


    dd_commands = embeds[openbb_dd]
    dd_commands.add_field(name=f"Earnings", value=f"> Earnings to occur in the coming business days.\n\n</dd earnings:1004263746090324066>")
    dd_commands.add_field(name=f"Pre-Market", value=f"> Displays pre-market data for a ticker.\n\n</dd pm:1004263746090324066>")
    dd_commands.add_field(name=f"After-Hours", value=f"> Displays after hours data for a ticker.\n\n</dd ah:1004263746090324066>")
    dd_commands.add_field(name=f"Analyst", value=f"> Displays analyst recommendations.\n\n</dd analyst:1004263746090324066>")
    dd_commands.add_field(name=f"Bio", value=f"> Displays a stock companie's bio.\n\n</dd bio:1004263746090324066>")
    dd_commands.add_field(name=f"Customers", value=f"> Displays customers of the company.\n\n</dd customers:1004263746090324066>")
    dd_commands.add_field(name=f"Dividend Info", value=f"> Displays dividend information for a ticker.\n\n</dd divinfo:1004263746090324066>")
    dd_commands.add_field(name=f"Earnings Move", value=f"> Displays implied earnings move based on option prices.\n\n</dd ermove:1004263746090324066>")
    dd_commands.add_field(name=f"Earnings Estimate", value=f"> Display earnings estimates for a ticker.\n\n</dd est:1004263746090324066>")
    dd_commands.add_field(name=f"Insider Trades", value=f"> Displays latest 15 transactions from insiders for a ticker.\n\n</dd financials:1004263746090324066>")
    dd_commands.add_field(name=f"Institution Holdings", value=f"> View institutional holdings for a ticker.\n\n</dd institutions:1004263746090324066>")
    dd_commands.add_field(name=f"Next Earnings", value=f"> Displays next earnings for a ticker.\n\n</dd nexter:1004263746090324066>")
    dd_commands.add_field(name=f"Price Target", value=f"> Displays recent price targets with chart for a ticker.\n\n</dd pt:1004263746090324066>")
    dd_commands.add_field(name=f"SEC Filings", value=f"> Displays recent SEC filings for a ticker.\n\n</dd sec:1004263746090324066>")
    dd_commands.add_field(name=f"Splits", value=f"> Displays split and historic split info for a ticker.\n\n</dd splits:1004263746090324066>")
    dd_commands.add_field(name=f"Suppliers", value=f"> Displays suppliers of a company.\n\n</dd supplier:1004263746090324066>")
    dd_commands.add_field(name=f"Year to Date", value=f"> Displays year to date performance for a ticker.\n\n</dd ytd:1004263746090324066>")

    dp_commands = embeds[openbb_dp]
    dp_commands.add_field(name=f"All Blocks", value=f"> Displays the last 15 block trades.\n\n</dp allblocks:1004263746170011748>")
    dp_commands.add_field(name=f"All Dark Pools", value=f"> Displays the last 15 dark pool trades.\n\n</dp alldp:1004263746170011748>")
    dp_commands.add_field(name=f"All Prints", value=f"> Displays the last 15 combination of dark pool and block trades.\n\n</dp allprints:1004263746170011748>")
    dp_commands.add_field(name=f"Big Prints", value=f"> Biggest levels of all prints over x number of days.\n\n</dp bigprints:1004263746170011748>")
    dp_commands.add_field(name=f"Dark Pool Levels", value=f"> Displays the last 15 block trades.\n\n</dp levels:1004263746170011748>")
    dp_commands.add_field(name=f"Dark Pool Sectors", value=f"> Summary of all prints by market cap and sector.\n\n</dp sectors:1004263746170011748>")
    dp_commands.add_field(name=f"Dark Pool Summary", value=f"> Summary of all prints by % market cap.\n\n</dp summary:1004263746170011748>")
    dp_commands.add_field(name=f"Top Summary", value=f"> Displays total block and dark pool data.\n\n</dp topsum:1004263746170011748>")


    flow_commands = embeds[openbb_flow]

    flow_commands.add_field(name=f"Big Flow", value=f"> Returns the top 20 largest option trades by premium. \n\n</flow bigflow:1004263746170011749>")
    flow_commands.add_field(name=f"Day Flow", value=f"> Returns the most recent flow for a stock.\n\n</flow day:1004263746170011749>")
    flow_commands.add_field(name=f"Opening Flow", value=f"> Top 20 opening flow where volume is greater than open interest.\n\n</flow opening:1004263746170011749>")
    flow_commands.add_field(name=f"Flow Premium", value=f"> Returns a chart with the summary of premium per day by calls and puts.\n\n</flow prem:1004263746170011749>")
    flow_commands.add_field(name=f"Sector Flow", value=f"> Summary of all flow by market cap per sector.\n\n</flow sectors:1004263746170011749>")
    flow_commands.add_field(name=f"Day Summary", value=f"> Graphs today's total premium for a stock.\n\n</flow sumday:1004263746170011749>")
    flow_commands.add_field(name=f"Expiration Summary", value=f"> Flow summary by expiration date for a ticker.\n\n</flow bigflow:1004263746170011749>")
    flow_commands.add_field(name=f"Flow Summary", value=f"> Summary of all flow by % market cap.\n\n</flow summary:1004263746170011749>")
    flow_commands.add_field(name=f"Flow Sumtop", value=f"> Top flow for the day - calls vs puts by stock.\n\n</flow sumtop:1004263746170011749>")
    flow_commands.add_field(name=f"Weekly Summary", value=f"> Graph the weekly premium for a stock.\n\n</flow sumweek:1004263746170011749>")
    flow_commands.add_field(name=f"Unusual Flow", value=f"> Unusual option trades with over $100,000 in premium.\n\n</flow unu:1004263746170011749>")
    flow_commands.add_field(name=f"Weekly Flow", value=f"> Top 20 flow premium for a stock with weekly expirations.\n\n</flow bigflow:1004263746170011749>")
    

    options_commands = embeds[openbb_op]
    options_commands.add_field(name=f"Options Chains", value=f"> Displays the option chain by expiry for a stock.\n\n</op chains:1004263746111275138>")
    options_commands.add_field(name=f"Equity Put/Call Ratio", value=f"> Displays the equity put/call volume ratio.\n\n</op equitypc:1004263746111275138>")
    options_commands.add_field(name=f"Gamma", value=f"> Displays gamma levels for a stock.\n\n</op gamma:1004263746111275138>")
    options_commands.add_field(name=f"High IV", value=f"> Displays the top 15 IV30 tickers.\n\n</op highiv:1004263746111275138>")
    options_commands.add_field(name=f"Price History", value=f"> Displays option price history on a chart.\n\n</op hist:1004263746111275138>")
    options_commands.add_field(name=f"Index Put/Call Ratio", value=f"> Displays the index put/call ratio for the market.\n\n</op indexpc:1004263746111275138>")
    options_commands.add_field(name=f"In the Money", value=f"> Displays in the money options by expiry for a stock.\n\n</op itm:1004263746111275138>")
    options_commands.add_field(name=f"Max Pain", value=f"> Displays max pain by expiry for a stock.\n\n</op maxpain:1004263746111275138>")
    options_commands.add_field(name=f"Open Interest", value=f"> Displays the open interest and put/call ratio for a stock in a table.\n\n</op oi:1004263746111275138>")
    options_commands.add_field(name=f"Open Interst Chart", value=f"> Charts total open interest by strike price.\n\n</op oichart:1004263746111275138>")
    options_commands.add_field(name=f"Option Smile", value=f"> Charts the option volatility smile for a stock.\n\n</op smile:1004263746111275138>")
    options_commands.add_field(name=f"Option Stats", value=f"> Displays options statistics for a stock.\n\n</op stats:1004263746111275138>")
    options_commands.add_field(name=f"Top Open Interest", value=f"> Displays top open interest for a ticker.\n\n</op topoi:1004263746111275138>")
    options_commands.add_field(name=f"Top Open Interest Change", value=f"> Displays top open interest changes for a ticker.\n\n</op topoichange:1004263746111275138>")
    options_commands.add_field(name=f"Top Strike Volume", value=f"> Displays top strikes recieving volume for a ticker. Can also query by expiration.\n\n</op topstrikevol:1004263746111275138>")
    options_commands.add_field(name=f"Unusual Options", value=f"> Shows unusual options.\n\n</op unu:1004263746111275138>")
    options_commands.add_field(name=f"Unusual Options Stock", value=f"> Displays top 20 average volume tickers.\n\n</op uoastock:1004263746111275138>")
    options_commands.add_field(name=f"ETF Options", value=f"> Displays top 15 etfs for option volume.\n\n</op topvoletf:1004263746111275138>")
    options_commands.add_field(name=f"Volatility Surface", value=f"> Displays a ticker's option volatility surface.\n\n</op vsurf:1004263746111275138>")

    analysis_commands = embeds[fudstop_analysis]
    analysis_commands.add_field(name=f"Finscreener", value=f"> Screen for different patterns, technical conditions, and more using the fin-screener command.\n\n</analysis finscreen:1122243463723876533>")
    analysis_commands.add_field(name=f"Gaps Up", value=f"> Screen for gaps down - customizable by percent.\n\n</analysis gaps_up:1122243463723876533>")
    analysis_commands.add_field(name=f"Gaps Down", value=f"> Screen for gaps up - customizable by percent.\n\n</analysis gaps_down:1122243463723876533>")
    analysis_commands.add_field(name=f"Overbought Gaps", value=f"> Search for gaps paired with an overbought RSI for a downside opportunity.\n\n</analysis overbought_gaps:1122243463723876533>")
    analysis_commands.add_field(name=f"Top Shorts", value=f"> Screen for different patterns, technical conditions, and more using the fin-screener command.\n\n</analysis top_shorts:1122243463723876533>")
    
    learn_commands = embeds[fudstop_learn]
    learn_commands.add_field(name=f"Learn Covered Calls", value=f"> Learn about Level 1 Options - Covered Calls\n\n</learn covered_calls:1122243463723876538>")
    learn_commands.add_field(name=f"Learn Calls", value=f"> Learn about Level 2 Options - Long Call options.\n\n</learn calls:1122243463723876538>")
    learn_commands.add_field(name=f"Learn Candle Patterns", value=f"> Learn about various candlestick patterns and view animated gifs.\n\n</learn candle_patterns:1122243463723876538>")
    learn_commands.add_field(name=f"Learn China", value=f"> Learn about the China opportunity and how it's tied into US Monetary Policy.\n\n</learn china:1122243463723876538>")
    learn_commands.add_field(name=f"Learn Core Criteria", value=f"> Learn the Core Logic criteria for trading options.\n\n</learn core_criteria:1122243463723876538>")
    learn_commands.add_field(name=f"Learn Core Logic", value=f"> Learn about the Core Logic trading strategy used in the FUDSTOP Discord.\n\n</learn core_logic:1122243463723876538>")
    learn_commands.add_field(name=f"Learn Discord", value=f"> Learn about Discord, the FUDSTOP Server, and helpful tips and tricks.\n\n</learn discord:1122243463723876538>")
    learn_commands.add_field(name=f"Learn ETFs", value=f"> Learn about exchange traded funds.\n\n</learn etfs:1122243463723876538>")
    learn_commands.add_field(name=f"Learn SEC Filings", value=f"> Learn about SEC Filings out of the NSCC, DTCC, OCC, FINRA, PCAOB, NYSE, MIAX, NASDAQ, CFR, the Fed, and many more market agencies.\n\n</learn filings:1122243463723876538>")
    learn_commands.add_field(name=f"Learn FINRA", value=f"> Learn about FINRA and their history.\n\n</learn finra:1122243463723876538>")
    learn_commands.add_field(name=f"Learn Greeks", value=f"> Learn about the option greeks.\n\n</learn greeks:1122243463723876538>")
    learn_commands.add_field(name=f"Learn NSFR Ratio", value=f"> Learn about the Net Stable Funding Ratio\n\n</learn nsfr_ratio:1122243463723876538>")
    learn_commands.add_field(name=f"Learn OCC", value=f"> Learn about the Options Clearing Corporation and important developments since Covid out of this industry.\n\n</learn occ:1122243463723876538>")
    learn_commands.add_field(name=f"Learn Option Strategies", value=f"> Learn about different option trading strategies.\n\n</learn option_strategies:1122243463723876538>")
    learn_commands.add_field(name=f"Learn Options 101", value=f"> Take the Options 101 Course provided by CBOE Global Markets.\n\n</learn options_101:1122243463723876538>")
    learn_commands.add_field(name=f"Learn Order Types", value=f"> Learn about the different market order types.\n\n</learn order_types:1122243463723876538>")
    learn_commands.add_field(name=f"Learn Technical Analysis", value=f"> Learn about technical analysis patterns and how they can be utilized.\n\n</learn ta:1122243463723876538>")



    navigation_commands = embeds[fudstop_nav]
    navigation_commands.add_field(name=f"Navigate Channels", value=f"> Navigate through the discord by searching through the channels with a convenient auto-complete search menu.\n\n> </navigate channels:1122243463723876539>")
    navigation_commands.add_field(name=f"Navigate Forums", value=f"> Navigate through the discord by searching through the forums with a convenient auto-complete search menu.\n\n> </navigate forums:1122243463723876539>")
    navigation_commands.add_field(name=f"Navigate Threads", value=f"> Navigate through the discord by searching through the member threads and forum threats with a convenient auto-complete search menu.\n\n> </navigate threads:1122243463723876539>")

    agency_commands = embeds[fudstop_agencies]
    agency_commands.add_field(name=f"Soma Holdings", value=f"> View the latest FED SOMA holdings, The Federal Reserve System Open Market Account (SOMA) contains dollar-denominated assets acquired through open market operations.\n\n> These securities serve several purposes:\n\n> They are:collateral for U.S. currency in circulation and other liabilities on the Federal Reserve System’s balance sheet;\n> a tool for the Federal Reserve’s management of reserve balances;\n> and a tool for achieving the Federal Reserve’s macroeconomic objectives.\n\n**Click to Run:**\n</fed soma:1122243463723876535>", inline=False)
    agency_commands.add_field(name=f"Rates", value=f"> Returns global rates for all central banks - secured rates.\n\n</fed rates:1122243463723876535>")
    agency_commands.add_field(name=f"Swaps Non-Us", value=f"> Returns the latest Non-US denominated currency swaps from the FED.\n\n</fed swaps_non_us:1122243463723876535>")
    agency_commands.add_field(name=f"OCC Volume", value=f"> Returns the day's volume stats from the Options Clearing Corporation.\n\n</occ total_volume:1122243463723876541>")
    agency_commands.add_field(name=f"OCC Totals", value=f"> Returns total futures, options, and trade volume averages.\n\n</occ totals:1122243463723876541> ")
    agency_commands.add_field(name=f"OFR Advanced Repo", value=f"> View and download all participant repo data.\n\n</ofr advanced_repo:1122243463723876542>")






    school_commands = embeds[fudstop_school]
    school_commands.add_field(name=f"Technical Signals", value=f"> Learn about technical analysis signals\n\n</school tech_analysis:1122243463862300756>")
    school_commands.add_field(name=f"ETFs", value=f"> Learn about ETFs, how they're made - and how they work.\n\n</school etfs:1122243463862300756>")
    school_commands.add_field(name=f"Time-Related Vocabulary", value=f"> Learn about the different time-related vocabulary frequently encountered in markets.\n\n</school time:1122243463862300756>")
    school_commands.add_field(name=f"Candlestick Patterns", value=f"> Learn about different technical candlestick patterns.\n\n</school patterns:1122243463862300756>")
    




    stream_commands = embeds[fudstop_stream]
    stream_commands.add_field(name=f"Double Crypto", value=f"> Stream two crypto coins simultaneously.\n\n</stream double_crypto:1122243463862300762>")
    stream_commands.add_field(name=f"Crypto", value=f"> Stream a single crypto coin with live prices.\n\n</stream crypto:1122243463862300762>")
    stream_commands.add_field(name=f"Double-Quote", value=f"> Stream two stock tickers simultaneously and also track live volume.\n\n</stream double_quote:1122243463862300762>")
    stream_commands.add_field(name=f"Top Volume", value=f"> Constantly monitors the top-most traded option contract in real time.\n\n</stream topvolume:1122243463862300762>")
    stream_commands.add_field(name=f"Tits", value=f"> Stream some titties.\n\n</stream tits:1122243463862300762>")

    stock_commands = embeds[fudstop_stock]
    stock_commands.add_field(name=f"Capital-flow",value=f"> View the capital flow broken down by player size for a ticker.\n\n</stock capitalflow:1122243463862300760>")
    stock_commands.add_field(name=f"Company Brief",value=f"> View company information.\n\n</poly company_information:1122243463862300754>")
    stock_commands.add_field(name=f"IPO Calendar",value=f"> Pull up the IPO Calendar, or tickers that are listing on the markets for the first time.\n\n</stock ipos:1122243463862300760>")
    stock_commands.add_field(name=f"Institutions",value=f"> View Institutional Holdings for a ticker.\n\n</stock institutions:1122243463862300760>")
    stock_commands.add_field(name=f"Short Interest",value=f"> View the latest short interest report out of FINRA for a ticker.\n\n</stock shortinterest:1122243463862300760>")
    stock_commands.add_field(name=f"Insider Summary",value=f"> View the latest insider transactions for a stock.\n\n</stock insider_summary:1122243463862300760>")
    stock_commands.add_field(name=f"Order Flow",value=f"> View live order-flow for a ticker.\n\n</stock orderflow:1122243463862300760>")
    stock_commands.add_field(name=f"Leverage",value=f"> View stock leverage information such as interest rate, overnight rates, margin, and shortability.\n\n</stock leverage:1122243463862300760>")

    


    other_commands = embeds[fudstop_other]
    other_commands.add_field(name=f"GPT4", value=f"> Call upon and interact with GPT4 right in discord. After calling the command initially - carry on as if you were having a normal conversation. A helpful tool for productivity but not an all-seeing magician.\n\n</gpt4:1122365837739819029>")
    other_commands.add_field(name=f"AllSkew", value=f"> Track all option skews across the top most 800 traded tickers in real time.\n\n</allskew:1121980575276879983>")
    other_commands.add_field(name=f"Skew Finder", value=f"> Find and track the skew of any ticker in real time.\n\n</skew finder:1122736124524249088>")
    other_commands.add_field(name=f"Social Sentiment", value=f"> View current social sentiment surrounding a ticker.\n\n</social sentiment:1122243463862300758>")
    other_commands.add_field(name=f"TradingView Spying", value=f"> Spy on tradingview conversations. (BUGGY)\n\n</social tradingview_spying:1122243463862300758>")


    fmp_commands = embeds[fudstop_fmp]
    fmp_commands.add_field(name=f"Country Risk Premium", value=f"> View global risk in order from riskiest country to least risky country.\n\n</fmp country_risk_premium:1122711896773103698>")
    fmp_commands.add_field(name=f"Price Target", value=f"> View price target data for a ticker.\n\n</fmp price_target:1122711896773103698>")

    fudopt_commands = embeds[fudstop_opts]
    fudopt_commands.add_field(name=f"Fetch Entire Chain", value=f"> Fetches a ticker's entire options chain across all expirations with all accompanying data - such as last trade, last quote, greeks, day stats, underlying ticker stats, and contract stats.\n\n</options fetch_entire_chain:1122243463862300753>")
    fudopt_commands.add_field(name=f"All Market Options", value=f"> Fetche's the entire options market organized by the data metric of your choosing.\n\n</options all_market_options:1122243463862300753>")
    page_select = PageSelect(embeds)
    view = AlertMenus(embeds).add_item(page_select)

    

    
    

    await ctx.send(embed=webull_commands, view=view)

import openai
from cfg import YOUR_OPENAI_KEY as openaikey
openai.api_key = openaikey

@bot.command()
async def gpt4(ctx: commands.Context, prompt:str):
    
    """Talk with CHATGPT. Call the command once and then reply as normal."""

    conversation_history = {}
    conversation_id = str(ctx.message.author.id)
    prompt = ctx.message.content
    # Retrieve the conversation history from the dictionary
    history = conversation_history.get(conversation_id, [])

    while True:
        # Add the new prompt to the conversation history
        history.append({"role": "user", "content": prompt})

        # Create the messages list including system message and conversation history

        messages =  [
        {"role": "system", "content": "You will help me save as much time as possible on this project for creating an sdk.'"},
        {"role": "assistant", "content": "Absolutely! Let me know when I can help you save time."},
        ]
        messages.extend(history)

        # Generate a response based on the full conversation history
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        message_content = completion.choices[0].message.content

        # Store the updated conversation history in the dictionary
        conversation_history[conversation_id] = history

        embed = disnake.Embed(title=f"Chat with GPT4 ", description=f"```py\n{message_content}```")
        embed.add_field(name=f"YOUR PROMPT:", value=f"```py\nYou asked: {prompt}```")

        # Send the response to the user
        await ctx.message.channel.send(embed=embed)
        print(message_content)
        # Check if the user wants to stop the conversation
        if prompt.lower() == "stop":
            await ctx.message.channel.send("conversation ended.")
            break

        # Wait for the user's next message
        def check(m):
            return m.author.id == ctx.message.author.id and m.channel.id == ctx.message.channel.id

        try:
            user_message = await bot.wait_for("message", check=check, timeout=60)
        except asyncio.TimeoutError:
            await ctx.message.channel.send("Conversation timed out. Please start a new conversation.")
            break

        prompt = user_message.content





extensions = []
cogs_directory = os.path.join(os.path.dirname(__file__), 'cogs')

for filename in os.listdir(cogs_directory):
    if filename.endswith('.py'):
        extension_name = filename[:-3]  # Remove the .py extension
        extensions.append(f'cogs.{extension_name}')

for extension in extensions:
    bot.load_extension(f'bot.{extension}')

bot.run(YOUR_DISCORD_BOT_TOKEN)






