import disnake
from disnake.ext import commands
from autocomp import ticker_autocomp

from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
import pandas as pd
from cfg import YOUR_API_KEY
import asyncio

polygon_sdk = AsyncPolygonSDK(YOUR_API_KEY)

class PolygonCMD(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.slash_command()
    async def poly(self, inter):
        pass

    
    @poly.sub_command()
    async def scan_rsi(self, inter:disnake.AppCmdInter, timespan:str=commands.Param(choices=["minute","hour","day","week","month","quarter","year"])):
        await inter.response.defer()
        """Scan the most traded and most liquid tickers for their RSI values specifying a timeframe."""
        tickers = ['BTG', 'MMS', 'ABNB', 'NKTR', 'CGAU', 'INVH', 'OKTA','VIX', 'LWLG', 'BTU', 'AXP', 'SNCR', 'SAN', 'VLO', 'WIMI', 'PG','SPX', 'RBLX', 'HL', 'DPST','JD', 'TRHC', 'TEVA', 'TSCO', 'NOK', 'SE', 'APP', 'BYND', 'XLP', 'NNDM', 'HRL', 'ESRT', 'COP', 'AGL', 'NGD', 'BXMT', 'IQ', 'MDWD', 'TYRA', 'GOOG', 'INVZ', 'CLF', 'EXC', 'BRX', 'EWJ', 'CPNG', 'JBLU', 'FNV', 'COMM', 'UBER', 'CAG', 'XM', 'GME', 'PTEN', 'HCM', 'SIRI', 'IAU', 'HSC', 'HPP', 'CCL', 'UVIX','CFLT', 'EPD', 'TGNA', 'CNC', 'EE', 'MRO', 'VSCO', 'VRAR', 'QQQ', 'BK', 'BBIO', 'CPRI', 'CSCO', 'PLUG', 'C', 'XHB', 'BJ', 'EW', 'ZTS', 'LCID', 'STWD', 'FUTU', 'ARCC', 'GPN', 'CG', 'HUN', 'TNA', 'DXC', 'GRPN', 'ENTG', 'PEP', 'INFY', 'MPW', 'TWLO', 'AVDL', 'AKAM', 'A', 'XELA', 'MARK', 'RPTX', 'NKLA', 'BHF', 'VOR', 'MNKD', 'YUMC', 'SOXX', 'UCO', 'NOW', 'BZ', 'GDX', 'WDC', 'PGR', 'MSFT', 'EXK', 'PACW', 'PCG', 'KNDI', 'BALL', 'MU', 'TZA', 'DNA', 'SFM', 'ZION', 'KOS', 'MVIS', 'ADBE', 'PTON', 'PSTG', 'KRE', 'DBX', 'RIG', 'FIGS', 'GILD', 'VST', 'NYCB', 'MFC', 'CBIO', 'SOUN', 'GPS', 'VEON', 'WBA', 'FSLY', 'ABEV', 'NCTY', 'ENB', 'PCAR', 'NXPI', 'QUIK', 'RKLB', 'NWSA', 'UGI', 'VFC', 'LI', 'VXRT', 'ENPH', 'ZNTL', 'CBRE', 'TTD', 'CRNC', 'CLVT', 'USFD', 'ES', 'FTI', 'KKR', 'VRT', 'LUV', 'JNJ', 'XRAY', 'MRAM', 'RIVN', 'TBT', 'SABR', 'HRB', 'AMC', 'SQNS', 'CVS', 'CDE', 'SUP', 'TBIO', 'YALA', 'INO', 'LVS', 'WDAY','SPXU', 'TDOC', 'SLRN', 'SBUX', 'LTRX', 'KIM', 'EMR', 'BOX', 'DD', 'TMUS', 'ATVI', 'ASAN', 'FTDR', 'HD', 'SCHW', 'IPSC', 'TARO', 'HASI', 'DIA', 'JWN', 'AVDX', 'MARA', 'PPL', 'MOS', 'ET', 'IAI', 'HOLI', 'QS', 'JBT', 'KEY', 'SFIX', 'AUPH', 'DXCM', 'CHRS', 'CRVS', 'SMRT', 'IBN', 'SQ', 'ACGL', 'ABT', 'AZN', 'INFN', 'KLR', 'BBAI', 'LYV', 'CTLT', 'TECK', 'BRMK', 'EFA', 'FCEL', 'ZGN', 'SBOW', 'NOVA', 'ARDX', 'FITB', 'GOOGL', 'SHOP', 'DAC', 'LNC', 'AMGN', 'PXD', 'TUYA', 'SYNH', 'NMTR', 'SMH', 'BGS', 'AEG', 'DKNG', 'FCX', 'NI', 'NMR', 'TSE', 'OBLG', 'CHPT', 'AES', 'NU', 'CRC','UNH', 'CIEN', 'FTCH', 'SWN', 'UP', 'RNG', 'EZPW', 'XPEV', 'PAAS', 'LBTYA', 'MUFG', 'BUD', 'INTZ', 'RKT', 'CLNE', 'APO', 'OTIS', 'VLY', 'DT', 'M', 'QCOM', 'PCT', 'TIL', 'IPG', 'ARKK', 'ADI', 'YUM', 'WMT', 'SMCI', 'XP', 'CCCC', 'AG', 'SAM', 'SPLK', 'MGM', 'BOH', 'CAT', 'RYAN', 'MDT', 'HOWL', 'JETS', 'SYY', 'FLEX', 'VTRS', 'PYPL', 'VVV', 'UNIT', 'MRK', 'BANX', 'MRIN', 'VTR', 'NVDA', 'AVGO', 'GLUE', 'DOCU', 'KR', 'ASTS', 'CANO', 'MMM', 'ADVM', 'BIGC', 'SNDL', 'CZR', 'LX', 'HOOD', 'MDB', 'VIAV', 'SO', 'FTFT', 'STKH', 'RMTI', 'WEN', 'V', 'RYAM', 'AEP', 'TAP', 'PM', 'LOW', 'ALLO', 'DRH', 'AR', 'HBB', 'LESL', 'TELL', 'VTS', 'GLD', 'ASX', 'CCJ', 'STNE', 'NAT', 'SEE', 'NET', 'EA', 'EVA', 'LMB', 'BN', 'IEF', 'DELL', 'DADA', 'CX', 'RFL', 'DOW', 'INDI', 'DASH', 'ADSK', 'ISEE', 'KWEB', 'XOP', 'TBLA', 'BX', 'FTV', 'PAYX', 'CL', 'XLU', 'LQD', 'STLA', 'MCHX', 'MSTR', 'ALLY', 'SU', 'HST', 'MULN', 'DLO', 'ONB', 'ACB', 'ABBV', 'FHN', 'XLI', 'AI', 'ORCL', 'CNET', 'BILI', 'COMP', 'EWZ', 'DSEY', 'WOW', 'BABA', 'BA', 'TLRY', 'EEM', 'SQQQ', 'CS', 'ANSS', 'NTCO', 'RIOT', 'KGC', 'TSP', 'BRDG', 'SKY', 'CSX', 'IBM', 'XIN', 'NEX', 'AAP', 'MCD', 'WRAP', 'LUMN', 'RPRX', 'BLDR', 'RXT', 'LABU', 'SYF', 'RPD', 'SGBX', 'RVLP', 'NXE', 'FNCB', 'SYPR', 'DVN', 'AQN', 'ONON', 'CNX', 'AGI', 'SPY', 'SVM', 'XLE', 'APPS', 'FRHC', 'AGEN', 'IOT', 'ZIM', 'BHC', 'ACN', 'AAL', 'SNAP', 'AFL', 'CRDO', 'BLNK', 'BOWL', 'VRAY', 'TRTX', 'ELAN', 'EOSE', 'UVXY', 'ZYNE', 'MQ', 'LYFT', 'ENVX', 'NKE', 'TNP', 'SAND', 'VZ', 'IWM', 'GE', 'XME', 'HTHT', 'XLK', 'GT', 'FAST', 'GLNG', 'IYR', 'DAL','KPTI', 'GS', 'BLDP', 'AVTR', 'BAC', 'NEWR', 'USAP', 'API', 'ANET', 'CRNT', 'LXP', 'ZS', 'SHLS', 'IP', 'BMBL', 'S', 'BFLY', 'LBTYK', 'LNT', 'DHT', 'CCO', 'NTAP', 'DOC', 'NGVC', 'PD', 'LAW','GTBP', 'RTX', 'BAX', 'LLY', 'FFIE', 'FLNT', 'PEG', 'FLO', 'COIN', 'CLOV', 'YMM', 'ETRN', 'IMAX', 'HSKA', 'WFC', 'GH', 'NEM', 'HITI', 'SSTI', 'EXPE', 'PFE', 'PATH', 'MFIN', 'ZTO', 'SGEN', 'UPRO', 'BCRX', 'CSIQ', 'ALIT', 'KOLD', 'AFRM', 'RXRX', 'TLT', 'NGM', 'OCGN', 'CTRA', 'FE', 'VERA', 'UDR', 'EVLV', 'XLC', 'NLY', 'TMF', 'GRAB', 'HAL', 'BITO', 'VALE', 'GSM', 'LBRDK', 'PRU', 'DNB', 'BP', 'HTZ', 'PXLW', 'CHWY', 'HYFM', 'LMNL', 'STT', 'ST', 'BGFV', 'FUBO', 'RUN', 'XLY', 'CGC', 'EFC', 'CNP', 'DISH', 'MANU', 'CVNA', 'AAOI', 'CRM', 'FSR', 'SANW', 'MREO', 'W', 'TMO', 'USB', 'DE', 'TDCX', 'ITRI', 'ZDGE', 'FXLV', 'ROKU', 'AVAH', 'PINS', 'VOD', 'SLP', 'PDS', 'AESI', 'CMCSA', 'PR', 'INTC', 'XLV', 'TSLA', 'WMB', 'OXY', 'IONQ', 'AMH', 'PLTR', 'ALEC', 'ACI', 'OSS', 'BIVI', 'JPM', 'MGNX', 'SPWR', 'LMT', 'SCPL', 'DLTR', 'ED', 'HPQ', 'LAZR', 'OSK', 'PANW', 'AIRS', 'FHTX', 'INSE', 'X', 'ADP', 'VMW', 'HRTG', 'BRLT', 'RDFN', 'ITUB', 'ETON', 'BIG', 'RCL', 'CBAT', 'RRC', 'ARR', 'SLI', 'ETN', 'OPEN', 'SENS', 'OWL', 'HBI', 'NVAX', 'DEI', 'ARMK', 'XRT', 'WEX', 'LSCC', 'LRCX', 'GOOS', 'IVZ', 'TLSA', 'APA', 'ROST', 'SLM', 'CERS', 'LGMK', 'DDOG', 'KMI', 'BTCM', 'AXLA', 'BTE', 'PAGS', 'FNGS', 'CRWD', 'ENOB', 'MGI', 'CMA', 'KHC', 'SGMO', 'WYNN', 'HYG', 'IOVA', 'ENSV', 'AMLX', 'VZIO', 'F', 'CIM', 'NFLX', 'ASC', 'WAL', 'AUMN', 'SOFI', 'DFS', 'TFC', 'FATE', 'JCI', 'CPB', 'HUT', 'ZM', 'CFG', 'IRIX', 'SKX', 'KSS', 'NRG', 'HZO', 'MCHP', 'AMX', 'KMB', 'MO', 'SPXS', 'IBRX', 'T', 'LC', 'MMAT', 'FUSN', 'FYBR', 'PEAK', 'CROX', 'PRDO', 'AMD', 'AEM', 'IFF', 'AMBA', 'U', 'CUZ', 'BOIL', 'XLF', 'FSLR', 'EQT', 'DHI', 'AMZN', 'EGO', 'SOXS', 'VTGN', 'BBWI', 'FOXA', 'ASRT', 'GSAT', 'TXN', 'SPWH', 'HR', 'PDD', 'NVTS', 'ESI', 'KDP', 'DB', 'ERIC', 'OGN', 'SOXL', 'UPST', 'WOOF', 'PENN', 'ARAV', 'AIN', 'TPR', 'VKTX', 'MS', 'TIGR', 'GTLB', 'TSN', 'IRS', 'MA', 'GDXJ', 'FANH', 'UUP', 'FTCI', 'ON', 'UNG', 'ETSY', 'KO', 'PAA', 'DNN', 'AA', 'TJX', 'ARRY', 'AM', 'CVE', 'AIG', 'COTY', 'LNG', 'TSM', 'NWL', 'BRFS', 'WTI', 'COST', 'AGNC', 'MTLS', 'RF', 'TOST', 'AMAT', 'WBD', 'HLIT', 'MRNA', 'BMY', 'Z', 'DG', 'TGT', 'XOM', 'URBN', 'DIS', 'SSSS', 'ENIC', 'DBRG', 'VXX', 'MLCO', 'RYN', 'ANF', 'ORC', 'SNOW', 'LULU', 'SLG', 'SAVE', 'XENE', 'VERX', 'GEN', 'BIDU', 'SONO', 'GPRK', 'GP','NM', 'UAL', 'RITM', 'HON', 'FXI', 'UPS', 'GURE', 'REXR', 'AAPL', 'SLB', 'MITT', 'IMBI', 'ODV', 'NEE', 'MESA', 'AEO', 'TQQQ', 'MRVL', 'SIG', 'ULTA', 'FDX', 'BB', 'ABR', 'EL', 'BEN', 'SIMO', 'PBR', 'CRBP', 'CAH', 'USO', 'SLV', 'META', 'GOLD', 'HPE', 'JFIN', 'EGHT', 'IEP', 'NTR', 'SID', 'SMWB', 'ALB', 'SPCE', 'ESLT', 'XBI', 'MSOS', 'CVX', 'RXST', 'CVT', 'AMRS', 'MTG', 'PRM', 'CHS', 'EPIX', 'COLB', 'ATUS', 'GM', 'MET', 'HZNP', 'SHEL', 'EQH', 'AMRN', 'PARA', 'ICLN', 'TARS', 'GFI', 'BEKE', 'NIO', 'GOEV', 'NCLH', 'EMB']
        # Create empty DataFrames for oversold and overbought results
        oversold_results = pd.DataFrame(columns=['Ticker', 'Price', 'RSI'])
        overbought_results = pd.DataFrame(columns=['Ticker', 'Price', 'RSI'])

        async def process_ticker(ticker):
            try:
                if ticker.startswith('SPX') or ticker.startswith('VIX') or ticker.startswith('NDX'):
                    price = await polygon_sdk.get_index_price(ticker)
                else:
                    price = await polygon_sdk.get_stock_price(ticker)
                
                rsi = await polygon_sdk.get_rsi(ticker, timespan=timespan)
                if rsi is not None:
                    rsi_value = rsi.rsi_value[0]
                    if rsi_value is not None and rsi_value <= 30:
                        oversold_results.loc[len(oversold_results)] = [ticker, price, rsi_value]
                    elif rsi_value is not None and rsi_value >= 70:
                        overbought_results.loc[len(overbought_results)] = [ticker, price, rsi_value]
            except (KeyError, TypeError, AttributeError, UnboundLocalError):
                pass

        # Create a list of coroutines for each ticker
        tasks = [process_ticker(ticker) for ticker in tickers]

        # Run the tasks concurrently
        await asyncio.gather(*tasks)

        if not oversold_results.empty:
            oversold_results_table = oversold_results.to_string(index=False)
            oversold_embed = disnake.Embed(title=f"Oversold RSI results - {timespan} timeframe",
                                        description=f"```py\n{oversold_results_table}```",
                                        color=disnake.Colour.dark_green())
            await inter.edit_original_message(embed=oversold_embed)
        elif not overbought_results.empty:
            overbought_results_table = overbought_results.to_string(index=False)
            overbought_embed = disnake.Embed(title=f"Overbought RSI results - {timespan} timeframe.",
                                            description=f"```py\n{overbought_results_table}```",
                                            color=disnake.Colour.dark_red())
            await inter.edit_original_message(embed=overbought_embed)






    @poly.sub_command(name="company_information")
    async def company_info(self, inter:disnake.AppCmdInter, ticker:str=commands.Param(autocomplete=ticker_autocomp)):
        """💠Returns company information for a ticker"""
        await inter.response.defer()

        company_info_data = await polygon_sdk.company_info(ticker)

        cik = company_info_data.cik
        composite_figi = company_info_data.composite_figi
        currency_name = company_info_data.currency_name
        description = company_info_data.description
        homepage_url = company_info_data.homepage_url
        list_date = company_info_data.list_date
        locale = company_info_data.locale
        market = company_info_data.market
        market_cap = company_info_data.market_cap
        name = company_info_data.name
        phone_number = company_info_data.phone_number
        primary_exchange = company_info_data.primary_exchange
        round_lot = company_info_data.round_lot
        share_class_figi = company_info_data.share_class_figi
        share_class_shares_outstanding = float(company_info_data.share_class_shares_outstanding)
        sic_code = company_info_data.sic_code
        sic_description = company_info_data.sic_description
        ticker = company_info_data.ticker

        embed = disnake.Embed(title=f"💠 Company Information  - {ticker} 💠", description=f"```py\n{description}```", url=homepage_url, color=disnake.Colour.dark_magenta())
        embed.add_field(name=f"Codes:", value=f"> CIK#: **{cik}**\n> FIGI: **{composite_figi}**\n> SIC: **{sic_code}**\n> SIC Description: **{sic_description}**", inline=False)
        embed.add_field(name=f"Contact Details:", value=f"> **{name}**\n> **{phone_number}**")
        embed.add_field(name=f"Ticker Info:", value=f"> Primary Exchange: **{primary_exchange}**\n> Listed: **{list_date}**\n> Market: **{market}**")
        embed.add_field(name=f"Trade Info:", value=f"> MarketCap: **${float(market_cap):,}**\n> Shares Outstanding: **{share_class_shares_outstanding:,}**")
        embed.set_thumbnail(await polygon_sdk.get_polygon_logo(ticker))
        embed.add_field(name=f"This command:", value=f"> </poly company_info:1121575902459998329>")
        embed.set_footer(text=f"Data Provided by Polygon.io | Implemented by FUDSTOP")
        await inter.edit_original_message(embed=embed)




    @poly.sub_command()
    async def rsi(self, inter:disnake.AppCmdInter, ticker:str=commands.Param(autocomplete=ticker_autocomp), timespan:str=commands.Param(choices=["minute","hour","day","week","quarter","year"]), window=14):
        """💠Returns the latest RSI value for a ticker with an optional window argument."""
        await inter.response.defer()
        rsi_data = await polygon_sdk.get_rsi(symbol=ticker,timespan=timespan,window=window)
        if rsi_data is not None:
            rsi = rsi_data.rsi_value[0]
            if rsi > 70:
                color = disnake.Colour.dark_red()
            if rsi < 30:
                color = disnake.Colour.dark_green()

            embed=  disnake.Embed(title=f"💠 RSI - {ticker} 💠", description=f"```py\nThe latest RSI value is: {rsi} for the {timespan} timespan.```", color=color)
            embed.add_field(name=f"This command:", value=f"> </poly rsi:1121575902459998329>")
            embed.set_thumbnail(await polygon_sdk.get_polygon_logo(ticker))
            embed.set_footer(text=f"Data Provided by Polygon.io | Implemented by FUDSTOP")
            await inter.edit_original_message(embed=embed)

            
    

def setup(bot:commands.Bot):
    bot.add_cog(PolygonCMD(bot))
    print(f"> Extension {__name__} is ready\n")