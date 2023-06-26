import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from cogs.analysis import Analysis
from cogs.ss import SS
from cogs.learn import Learn
from cogs.fmp import FMP
import disnake
from disnake.ext import commands
from disnake import Option, OptionType
from autocomp import command_autocomp

import aiohttp
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from _discord.views.menus import AlertMenus
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from cogs.skews import Skew

from tabulate import tabulate
from disnake import Option, OptionType, OptionChoice
from disnake.ext import commands

from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
from _discord import emojis






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

from views.learnviews import AvoidView

import asyncio


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







@bot.slash_command()
async def test(inter: disnake.AppCommandInter, command:str=commands.Param(autocomplete=command_autocomp)):
    if command == "allskew":
        await allskew(inter)

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




@bot.slash_command(name="allskew")
async def allskew(inter: disnake.AppCmdInter):
    """Scan multiple skews in real time"""
    tickers = [
        'COIN', 'WFC', 'GM', 'PYPL', 'CVS', 'CVX', 'BKNG', 'NVDA', 'AMD', 'MSFT',
        'META', 'U', 'W', 'ADBE', 'MSTR', 'LLY', 'BLK', 'MCD', 'WMT', 'TGT', 'SPY',
        'F', 'SHOP', 'SNAP', 'AMC', 'GME', 'BABA', 'BIDU', 'JD', 'NFLX', 'AMZN',
        'BAC', 'KRE', 'EWZ', 'M', 'SO', 'KO', 'PEP', 'CSCO', 'COST', 'SBUX', 'BBY',
        'SQQQ', 'QQQ', 'TQQQ', 'EEM', 'CHZ', 'HYG', 'TSLA', 'AMD', 'QCOM', 'INTC'
    ]

    await inter.response.defer()

    counter = 0
    while True:
        counter += 1

        # Get prices for all tickers concurrently
        price_tasks = [polygon.get_stock_price(ticker) for ticker in tickers]
        prices = await asyncio.gather(*price_tasks)
        ticker_prices = dict(zip(tickers, prices))  # Assuming no None prices
        print(ticker_prices)

        # Now get option data concurrently
        option_data_tasks = [
            poly_options.get_option_data(ticker, ticker_prices[ticker]) for ticker in tickers
        ]
        results = await asyncio.gather(*option_data_tasks)
        print(results)

        # Filter out None results and add valid results to data_list
        data_list = [result for result in results if result is not None]
        data_list = sorted(data_list, key=lambda x: x[6], reverse=True)

        # Create a new list that only includes the parts you want to display
        display_data = [row[:7] for row in data_list]

        # Now, display_data contains the data you want to display for all tickers.
        # Format it into a table and send it in discord chat.
        table = tabulate(display_data, headers=['Symbol', 'Skew', ' ', 'Price', 'Expiry', 'IV', 'Vol','Skew Metric'], tablefmt='fancy')

        embed = disnake.Embed(
            title=f"All - Skew",
            description=f"```\n" + table + "\n```",
            color=disnake.Colour.random()
        )
        embed.set_footer(text=f"{counter} | Data Provided by Polygon.io | Implemented by FUDSTOP")
        await inter.edit_original_message(embed=embed)  # Send the table in a code block

        if counter == 100:
            await inter.send(f"> **Click to Run:**\n> </allskew:1121980575276879983>")
            break




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






@bot.command()
async def cmds(ctx: commands.Context):
    """Views the server commands from all bots."""
    embeds = [ 

        disnake.Embed(title=f"FUDSTOP Commands - Webull", description=f"```py\nYou are viewing fudstop commands regarding webull. Learn how to use the Webull App, customize it, and view several graphics such as TA, Trend Analysis, Candlestick analysis, and general market knowledge.```\n> The webull commands can be accessed by using:\n\n> **/webull**"),
        disnake.Embed(title=f"FUDSTOP Commands - Stocksera", description=f"```py\nYou are viewing the fudstop implemented commands from the Stocksera API. View economic data, FTDs, low floats, short interest, short volume, social media chatter and more.```\n> The Stocksera commands can be access by using:\n\n> **/ss**")
    ]

    # Add fields to a specific embed (e.g., the second embed at index 1)
    embed1 = 0
    embed2 = 1
    embed3 = 2
    embed4 = 3
    embed5 = 4
    embed1target = embeds[embed1]
    embed1target.add_field(name="Analysis Tools", value="> View webull tools pertaining to how to utilize data analysis tools.\n> Click to use:\n\n</webull analysis_tools:1122243464042659942>", inline=True)
    embed1target.add_field(name="Bid/Ask Spread", value="> Learn about the bid ask spread.\n> Click to use:\n\n</webull bid_ask_spread:1122243464042659942>", inline=True)
    embed1target.add_field(name="Graphics", value="> View several webull graphics such as TA, Chart Patterns, and more.\n> Click to use:\n\n</webull graphics:1122243464042659942>", inline=True)
    embed1target.add_field(name="Options Chain", value="> Learn about the Webull Option Chain and how to use it.\n> Click to use:\n\n</webull options_chain:1122243464042659942>", inline=True)
    embed1target.add_field(name="Options Setup", value="> Learn how to cutsomize your webull options chart.\n> Click to use:\n\n> </webull options_setup:1122243464042659942>", inline=True)
    embed1target.add_field(name="Orders", value="> Learn about the different market order types.\n> Click to use:\n\n</webull orders:1122243464042659942>", inline=True)
    embed1target.add_field(name="Paper Trading", value="> Learn about paper trading and options paper trading via Webull.\n> Click to use:\n\n</webull paper_trading:1122243464042659942>", inline=True)
    embed1target.add_field(name="Volume Analysis", value="> Returns a live stream of the input ticker's volume analysis on the day.\n> Click to use:\n\n</webull volume_analysis:1122243464042659942>", inline=True)

    embed2target = embeds[embed2]
    embed2target.add_field(name=f"Earnings", value=f"> Returns earnings tickers for the given date range.\n> Click to use:\n\n</ss earnings:1122243463862300759>")
    embed2target.add_field(name=f"FTDs", value=f"> Search market-wide FTDs ranked by highest to lowest with T+35 dates.\n> Click to use:\n\n</ss ftds:1122243463862300759>")
    embed2target.add_field(name=f"Inflation", value=f"> Returns historic inflation up to the current day dated back to 1977.\n> Click to use:\n\n</ss inflation:1122243463862300759>")
    embed2target.add_field(name=f"Insider Summary", value=f"> View the latest insider trades across the market.\n> Click to use:\n\n</ss insider_summary:1122243463862300759>")
    embed2target.add_field(name=f"Jobless Claims", value=f"> View the latest and historic jobless claims numbers.\n> Click to use:\n\n</ss jobless_claims:1122243463862300759>")
    embed2target.add_field(name=f"Low Floats", value=f"> Returns tickers with extremely low free floats.\n> Click to use:\n\n</ss low_floats:1122243463862300759>")
    embed2target.add_field(name=f"Market News", value=f"> Return market-wide news to track narratives.\n> Click to use:\n\n</ss market_news:1122243463862300759>")
    embed2target.add_field(name=f"News Sentiment", value=f"> View headlines for a ticker and the underlying sentiment.\n> Click to use:\n\n</ss news_sentiment:1122243463862300759>")
    embed2target.add_field(name=f"Reverse Repo", value=f"> View the latest and historic repo numbers from the FED.\n\n</ss reverse_repo:1122243463862300759>")
    embed2target.add_field(name=f"SEC Filings", value=f"> View the latest SEC Filings for a ticker.\n> Click to use:\n\n</ss sec_filings:1122243463862300759>")
    embed2target.add_field(name=f"Short Interest", value=f"> View tickers with high % of their float shorted.\n> Click to use:\n\n</ss short_interest:1122243463862300759>")
    embed2target.add_field(name=f"Short Volume", value=f"> View a stock's latest and historic short volume.\n> Click to use:\n\n</ss short_volume:1122243463862300759>")
    embed2target.add_field(name=f"Stocktwits", value=f"> Return a ticker's rank on StockTwits.\n> Click to use:\n\n</ss stocktwits:1122243463862300759>")
    embed2target.add_field(name=f"Subreddits", value=f"> View a ticker's popular subreddit / active users and rank.\n> Click to use:\n\n</ss subreddits:1122243463862300759>")



    # Add more fields as needed

    await ctx.send(embed=embed1target, view=AlertMenus(embeds))
extensions = []
cogs_directory = os.path.join(os.path.dirname(__file__), 'cogs')

for filename in os.listdir(cogs_directory):
    if filename.endswith('.py'):
        extension_name = filename[:-3]  # Remove the .py extension
        extensions.append(f'cogs.{extension_name}')

for extension in extensions:
    bot.load_extension(f'bot.{extension}')

bot.run(YOUR_DISCORD_BOT_TOKEN)






