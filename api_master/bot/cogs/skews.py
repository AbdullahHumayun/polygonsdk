import disnake
from autocomp import ticker_autocomp
from disnake.ext import commands
import aiohttp
import asyncio
from menus.embedmenus import SkewPageSelect,SkewAlertMenus
from tabulate import tabulate
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
from cfg import YOUR_API_KEY
import numpy as np
from cfg import today_str,seven_days_from_now_str, today_str
from sdks.polygon_sdk.universal_snapshot import UniversalOptionSnapshot,UniversalSnapshot
from sdks.polygon_sdk.masterSDK import MasterSDK
poly = AsyncPolygonSDK(YOUR_API_KEY)
from _discord import emojis
import pandas as pd
poly_opt = PolygonOptionsSDK(YOUR_API_KEY)
sdk = MasterSDK()
master = MasterSDK()
webull = AsyncWebullSDK()
subs = ['PTON', 'MTCH', 'SBUX', 'AZN', 'KHC', 'EBIX', 'ENPH', 'BTAI', 'BEKE', 'APA', 'CMG', 'HPQ', 'NNDM', 'SWN', 'KMI', 'SQQQ', 'SGEN', 'LNC', 'GFI', 'XOP', 'LOW', 'CHWY', 'DRI', 'TEVA', 'AMZN', 'BBY', 'WMB', 'ZM', 'AFRM', 'BYND', 'PARA', 'AMD', 'SAVE', 'UNG', 'FTCH', 'DM', 'C', 'TWLO', 'RUN', 'DNN', 'PBR', 'TSM', 'CIM', 'CCL', 'ORCL', 'DB', 'VFC', 'EEM', 'PDD', 'CPRI', 'GSAT', 'MGM', 'VLO', 'GT', 'MCD', 'MDB', 'AR', 'KO', 'NLY', 'FSLR', 'JWN', 'STNE', 'MRK', 'U', 'FCEL', 'IYR', 'UBS', 'VMW', 'ZIM', 'AMC', 'IQ', 'MRNA', 'EOSE', 'NKE', 'KWEB', 'XLE', 'MA', 'XLI', 'KR', 'DIS', 'FIS', 'IONQ', 'PG', 'NEM', 'TMC', 'AMGN', 'BCS', 'PAA', 'DOCU', 'ISEE', 'JBLU', 'CRWD', 'CMCSA', 'LAZR', 'CLOV', 'TLT', 'MARA', 'FUBO', 'IEF', 'HAL', 'NCLH', 'SPWR', 'CHPT', 'FDX', 'STLA', 'CRBU', 'AUPH', 'IBM', 'BA', 'MRVL', 'LABU', 'MP', 'MMM', 'MSFT', 'MT', 'TBT', 'ETSY', 'XHB', 'COTY', 'APLD', 'LCID', 'CLF', 'SIRI', 'SNDL', 'EWZ', 'NEE', 'RIO', 'TNA', 'JNJ', 'GENI', 'TFC', 'HD', 'KOLD', 'TECK', 'UAL', 'NKLA', 'SLV', 'LULU', 'DD', 'MET', 'GOLD', 'Z', 'BBBYQ', 'CVNA', 'EWJ', 'SABR', 'LVS', 'ASTS', 'SVXY', 'SLB', 'DOW', 'X', 'BBD', 'PLUG', 'COIN', 'ABT', 'ALB', 'UBER', 'GM', 'SCHW', 'XRT', 'RIOT', 'CBL', 'ABNB', 'RIVN', 'PINS', 'BITO', 'RUT', 'DDOG', 'DNA', 'TIP', 'SE', 'TDOC', 'CSCO', 'HL', 'GOEV', 'KRE', 'FUTU', 'XLU', 'SOXL', 'EFA', 'KEY', 'TRUP', 'NDX', 'LQD', 'GDX', 'SLG', 'GME', 'LLY', 'EWU', 'COST', 'QQQ', 'MRO', 'BMBL', 'AAL', 'PEP', 'NIO', 'LUV', 'IAT', 'XLV', 'SNAP', 'BMY', 'BTU', 'XLF', 'RCL', 'DOCN', 'AAP', 'MVIS', 'LRCX', 'UPS', 'INTC', 'HOOD', 'PAAS', 'SMH', 'MPW', 'WBA', 'BRK B', 'SPXS', 'PENN', 'NVDA', 'HUM', 'BITF', 'JPM', 'BP', 'ROKU', 'TSLA', 'JOBY', 'CZR', 'XP', 'LEVI', 'BIDU', 'SPX', 'WFC', 'SPCE', 'PACW', 'SOXS', 'EWG', 'JETS', 'BAC', 'AG', 'DWAC', 'UNH', 'DAL', 'FXI', 'HTZ', 'AGNC', 'PCG', 'CCJ', 'HYG', 'ZS', 'FFIE', 'NYCB', 'GILD', 'INVZ', 'MANU', 'MS', 'LEN', 'BTG', 'SHOP', 'CVX', 'IWM', 'DIA', 'XOM', 'COF', 'UUP', 'RTX', 'RIG', 'GS', 'AEM', 'BBIO', 'OPEN', 'COP', 'IEI', 'JMIA', 'TZA', 'USO', 'UVXY', 'VOD', 'ZION', 'WBD', 'ACB', 'KGC', 'OSTK', 'MELI', 'GE', 'BUD', 'CLSK', 'SBSW', 'EPD', 'MOS', 'SHEL', 'SU', 'MSOS', 'AI', 'XLP', 'TXN', 'XLK', 'VBIV', 'UVIX', 'ONON', 'SMCI', 'ON', 'BABA', 'ITB', 'MULN', 'LUMN', 'T', 'DVN', 'PSNY', 'CVS', 'GLD', 'ATVI', 'SPXU', 'TMUS', 'VXX', 'DASH', 'ABBV', 'CRM', 'PANW', 'DUK', 'ARKK', 'BOIL', 'AMAT', 'TTD', 'ABR', 'PFE', 'OXY', 'WMT', 'OKTA', 'RBLX', 'MU', 'ALLY', 'GOOGL', 'SOUN', 'UPST', 'QS', 'AVGO', 'XSP', 'GNRC', 'SQ', 'MQ', 'LYFT', 'AXP', 'HZNP', 'PLTR', 'WYNN', 'NFLX', 'XBI', 'QCOM', 'AA', 'F', 'NU', 'CARR', 'MSTR', 'TLRY', 'SPY', 'HBI', 'SNOW', 'NVAX', 'AAPL', 'JD', 'EQT', 'W', 'BX', 'FNGS', 'SOFI', 'SIMO', 'VIX', 'CGC', 'PYPL', 'XPEV', 'XLY', 'PATH', 'PACB', 'VZ', 'MMAT', 'DISH', 'CROX', 'WDC', 'TMF', 'EBAY', 'MO', 'CPNG', 'LI', 'ENVX', 'META', 'NOK', 'BVN', 'ETRN', 'V', 'MDT', 'TSLL', 'FCX', 'TSN', 'VALE', 'M', 'TELL', 'NET', 'GOOG', 'BB', 'USB', 'ET', 'BILI', 'HUT', 'TQQQ', 'FSR', 'DKNG', 'TGT', 'CAT', 'ADBE']

class Stop(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @disnake.ui.button(style=disnake.ButtonStyle.red, emoji=f"🛑", disabled=True)
    async def stop_start(self, button: disnake.ui.Button, inter:disnake.AppCmdInter):
        button.disabled = True
        await inter.client.loop.close()
        view = Start()
        await inter.edit_original_message(f"> Loop has been stopped!", view=view)
        


class Start(disnake.ui.View):

    @disnake.ui.button(style=disnake.ButtonStyle.green,emoji=f"✅", disabled=False)
    async def start_stop(self, button:disnake.ui.Button, inter:disnake.AppCmdInter):
        button.disabled = True
        view = Stop()
        await inter.client.loop.call_soon(Skew(bot=commands.Bot).allskew(inter))
        await inter.edit_original_message(view=view)



            

class Skew(commands.Cog):
    def __init__(self,bot):
        self.bot=bot





    @commands.slash_command()
    async def skew(self, inter):
        pass

    


    # @skew.sub_command()
    # async def multiple(inter: disnake.AppCmdInter, tickers: str):
    #     """Query multiple tickers for a static skew picture."""
    #     await inter.response.defer()
    #     tickers = tickers.split(',')
    #     embeds = []
        
    #     async def process_ticker(ticker: str):
    #         ticker = ticker.upper()
    #         if ticker.startswith("SPX"):
    #             price = await poly.get_index_price(ticker)
    #             lower_strike = round(price) * 0.97
    #             upper_strike = round(price) * 1.03
    #         else:
    #             price = await poly.get_stock_price(ticker)
    #             lower_strike = round(price) * 0.85
    #             upper_strike = round(price) * 1.15
    #         print(f"SPX TICKER: {ticker}: {lower_strike}, {price}, {upper_strike}")

    #         async with aiohttp.ClientSession() as session:
    #             initial_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte=2023-12-30&limit=250&apiKey={YOUR_API_KEY}"

    #             results = await poly._request_all_pages(initial_url)
    #             if results is not None:
    #                 option_data = UniversalOptionSnapshot(results)
    #                 calls = option_data.df[option_data.df['type'] == 'call']
    #                 puts = option_data.df[option_data.df['type'] == 'put']
    #                 calls_grouped = calls.groupby('exp')
    #                 puts_grouped = puts.groupby('exp')

    #                 async def process_grouped_tickers(grouped_df, session: aiohttp.ClientSession):
    #                     results = []
    #                     for _, group in grouped_df:
    #                         group_tickers = group['ticker'].tolist()
    #                         if not group_tickers:
    #                             continue
    #                         tickers_string = ','.join(group_tickers)
    #                         async with session.get(f"https://api.polygon.io/v3/snapshot?ticker.any_of={tickers_string}&apiKey={YOUR_API_KEY}") as response:
    #                             try:
    #                                 near_money = await response.json(content_type=None)
    #                                 near_money_results = near_money['results']
    #                                 atm_data = UniversalSnapshot(near_money_results)
    #                                 results.append(atm_data.df.sort_values('IV', ascending=True))
    #                             except Exception as e:
    #                                 print(f"Error processing tickers_string: {tickers_string}. Error: {e}")
    #                     return results

    #                 async with sem:  # Acquire semaphore to limit concurrent requests
    #                     calls_results = await process_grouped_tickers(calls_grouped, aiohttp.ClientSession)
    #                     calls_results_df = pd.concat(calls_results)
    #                     calls_grouped = calls_results_df.groupby('Exp', as_index=False)

    #                     puts_results = await process_grouped_tickers(puts_grouped, session)
    #                     puts_results_df = pd.concat(puts_results)
    #                     puts_grouped = puts_results_df.groupby('Exp', as_index=False)

    #                     calls_first_rows = calls_grouped.first()
    #                     puts_first_rows = puts_grouped.first()

    #                     calls_selected_columns_df = calls_first_rows[['Exp', 'IV', 'Skew', 'Price']]
    #                     puts_selected_columns_df = puts_first_rows[['Exp', 'IV', 'Skew', 'Price']]
    #                     calls_selected_columns_df['Exp'] = calls_selected_columns_df['Exp'].apply(lambda x: x[5:])
    #                     puts_selected_columns_df['Exp'] = puts_selected_columns_df['Exp'].apply(lambda x: x[5:])
    #                     calls_selected_columns_df['IV'] = (calls_selected_columns_df['IV'] * 100).round(4)
    #                     puts_selected_columns_df['IV'] = (puts_selected_columns_df['IV'] * 100).round(4)
    #                     calls_selected_columns_df = calls_selected_columns_df.reset_index(drop=True)[['Exp', 'IV', 'Skew', 'Price']]
    #                     puts_selected_columns_df = puts_selected_columns_df.reset_index(drop=True)[['Exp', 'IV', 'Skew', 'Price']]

    #                     print(calls_selected_columns_df)
    #                     print(puts_selected_columns_df)
    #                     call_table = tabulate(calls_selected_columns_df, headers='keys', tablefmt='fancy', showindex=False)
    #                     put_table = tabulate(puts_selected_columns_df, headers='keys', tablefmt='fancy', showindex=False)
    #                     embed = disnake.Embed(
    #                         title=f"Skews - {ticker} - Next 90 Days",
    #                         description=f"**CALLS:**```{call_table}```\n**PUTS:**```{put_table}```\n\n> Tickers Queried: {tickers}",
    #                         color=disnake.Colour.random()
    #                     )
    #                     embed.set_footer(text=f"Viewing Skews for {ticker}")
    #                     return embed

    #     sem = asyncio.Semaphore(100)  # Adjust the semaphore limit to a higher value

    #     tasks = [process_ticker(ticker) for ticker in tickers]

    #     results = await asyncio.gather(*tasks)
        
    #     view = SkewAlertMenus(results).add_item(SkewPageSelect(results, tickers))

    #     await inter.edit_original_message(embed=results[0], view=view)
        

    # @skew.sub_command()
    # async def pc(inter: disnake.AppCmdInter, ticker: str = commands.Param(autocomplete=ticker_autocomp)):
    #     """View skews for the next 60 days. PC Format with more columns."""
    #     MAX_CONCURRENCY = 60
    #     await inter.response.defer()
    #     ticker = ticker.upper()

    #     async def fetch_data(session, tickers):
    #         async with session.get(f"https://api.polygon.io/v3/snapshot?ticker.any_of={tickers}&apiKey={YOUR_API_KEY}") as response:
    #             try:
    #                 near_money = await response.json(content_type=None)
    #                 near_money_results = near_money['results']
    #                 atm_data = UniversalSnapshot(near_money_results)
    #                 return atm_data.df.sort_values('IV', ascending=True)
    #             except Exception as e:
    #                 print(f"Error processing tickers: {tickers}. Error: {e}")
    #                 return pd.DataFrame()

    #     async def process_option_data(grouped_df, session, sem):
    #         tasks = []
    #         for _, group in grouped_df:
    #             group_tickers = group['ticker'].tolist()
    #             if not group_tickers:
    #                 continue
    #             tickers_string = ','.join(group_tickers)
    #             task = asyncio.create_task(fetch_data(session, tickers_string))
    #             tasks.append(task)

    #         results = []
    #         async with sem:
    #             for future in asyncio.as_completed(tasks):
    #                 result = await future
    #                 results.append(result)

    #         return results

    #     async with aiohttp.ClientSession() as session:
    #         sem = asyncio.Semaphore(MAX_CONCURRENCY)
    #         counter = 0
    #         while True:
    #             counter = counter + 1
    #             if ticker.startswith("SPX"):
    #                 price = await poly.get_index_price(ticker)
    #                 lower_strike = round(price) * 0.97
    #                 upper_strike = round(price) * 1.03
    #             else:
    #                 price = await poly.get_stock_price(ticker)
    #                 lower_strike = round(price) * 0.85
    #                 upper_strike = round(price) * 1.15
    #             print(f"SPX TICKER: {ticker}: {lower_strike}, {price}, {upper_strike}")

    #             initial_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte=2023-09-30&limit=250&apiKey={YOUR_API_KEY}"
    #             results = await poly._request_all_pages(initial_url)

    #             if results is not None:
    #                 option_data = UniversalOptionSnapshot(results)
    #                 calls = option_data.df[option_data.df['type'] == 'call']
    #                 puts = option_data.df[option_data.df['type'] == 'put']
    #                 calls_grouped = calls.groupby('exp')
    #                 puts_grouped = puts.groupby('exp')

    #                 calls_results = await process_option_data(calls_grouped, session, sem)
    #                 calls_results_df = pd.concat(calls_results)
    #                 calls_grouped = calls_results_df.groupby('Exp', as_index=False)

    #                 puts_results = await process_option_data(puts_grouped, session, sem)
    #                 puts_results_df = pd.concat(puts_results)
    #                 puts_grouped = puts_results_df.groupby('Exp', as_index=False)

    #                 calls_first_rows = calls_grouped.first()
    #                 puts_first_rows = puts_grouped.first()

    #                 calls_selected_columns_df = calls_first_rows[['Exp', 'IV', 'Skew', 'Price', 'Size', 'Vol', 'OI']]
    #                 puts_selected_columns_df = puts_first_rows[['Exp', 'IV', 'Skew', 'Price', 'Size', 'Vol', 'OI']]
    #                 calls_selected_columns_df['Exp'] = calls_selected_columns_df['Exp'].apply(lambda x: x[5:])
    #                 puts_selected_columns_df['Exp'] = puts_selected_columns_df['Exp'].apply(lambda x: x[5:])
    #                 calls_selected_columns_df['IV'] = (calls_selected_columns_df['IV'] * 100).round(4)
    #                 puts_selected_columns_df['IV'] = (puts_selected_columns_df['IV'] * 100).round(4)
    #                 calls_selected_columns_df = calls_selected_columns_df.reset_index(drop=True)[['Exp', 'IV', 'Skew', 'Price', 'Size', 'Vol', 'OI']]
    #                 puts_selected_columns_df = puts_selected_columns_df.reset_index(drop=True)[['Exp', 'IV', 'Skew', 'Price', 'Size', 'Vol', 'OI']]

    #                 print(calls_selected_columns_df)
    #                 print(puts_selected_columns_df)
    #                 call_table = tabulate(calls_selected_columns_df, headers='keys', tablefmt='fancy', showindex=False)
    #                 put_table = tabulate(puts_selected_columns_df, headers='keys', tablefmt='fancy', showindex=False)
    #                 embed = disnake.Embed(title=f"Skews - {ticker} - Next 30 Days", description=f"**CALLS:**```{call_table}```\n**PUTS:**```{put_table}```", color=disnake.Colour.random())
    #                 embed.set_footer(text=f"Viewing Skews for {ticker}")
    #                 await inter.edit_original_message(embed=embed)
    #                 if counter == 50:
    #                     await inter.send("stream ended")
    #                     break


    # @skew.sub_command()
    # async def mobile(inter: disnake.AppCmdInter, ticker: str = commands.Param(autocomplete=ticker_autocomp)):
    #     "Skew command for mobile user format - less columns than PC."
    #     MAX_CONCURRENCY = 10
    #     await inter.response.defer()
    #     ticker = ticker.upper()

    #     async def fetch_data(session, tickers):
    #         async with session.get(f"https://api.polygon.io/v3/snapshot?ticker.any_of={tickers}&apiKey={YOUR_API_KEY}") as response:
    #             try:
    #                 near_money = await response.json(content_type=None)
    #                 near_money_results = near_money['results']
    #                 atm_data = UniversalSnapshot(near_money_results)
    #                 return atm_data.df.sort_values('IV', ascending=True)
    #             except Exception as e:
    #                 print(f"Error processing tickers: {tickers}. Error: {e}")
    #                 return pd.DataFrame()

    #     async def process_option_data(grouped_df, session, sem):
    #         tasks = []
    #         for _, group in grouped_df:
    #             group_tickers = group['ticker'].tolist()
    #             if not group_tickers:
    #                 continue
    #             tickers_string = ','.join(group_tickers)
    #             task = asyncio.create_task(fetch_data(session, tickers_string))
    #             tasks.append(task)

    #         results = []
    #         async with sem:
    #             for future in asyncio.as_completed(tasks):
    #                 result = await future
    #                 results.append(result)

    #         return results

    #     async with aiohttp.ClientSession() as session:
    #         sem = asyncio.Semaphore(MAX_CONCURRENCY)
    #         counter = 0
    #         while True:
    #             counter = counter + 1
    #             if ticker.startswith("SPX"):
    #                 price = await poly.get_index_price(ticker)
    #                 lower_strike = round(price) * 0.97
    #                 upper_strike = round(price) * 1.03
    #             else:
    #                 price = await poly.get_stock_price(ticker)
    #                 lower_strike = round(price) * 0.85
    #                 upper_strike = round(price) * 1.15
    #             print(f"SPX TICKER: {ticker}: {lower_strike}, {price}, {upper_strike}")

    #             initial_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte=2023-09-30&limit=250&apiKey={YOUR_API_KEY}"
    #             results = await poly._request_all_pages(initial_url)

    #             if results is not None:
    #                 option_data = UniversalOptionSnapshot(results)
    #                 calls = option_data.df[option_data.df['type'] == 'call']
    #                 puts = option_data.df[option_data.df['type'] == 'put']
    #                 calls_grouped = calls.groupby('exp')
    #                 puts_grouped = puts.groupby('exp')

    #                 calls_results = await process_option_data(calls_grouped, session, sem)
    #                 calls_results_df = pd.concat(calls_results)
    #                 calls_grouped = calls_results_df.groupby('Exp', as_index=False)

    #                 puts_results = await process_option_data(puts_grouped, session, sem)
    #                 puts_results_df = pd.concat(puts_results)
    #                 puts_grouped = puts_results_df.groupby('Exp', as_index=False)

    #                 calls_first_rows = calls_grouped.first()
    #                 puts_first_rows = puts_grouped.first()

    #                 calls_selected_columns_df = calls_first_rows[['Exp', 'IV', 'Skew', '💲', 'Size']]
    #                 puts_selected_columns_df = puts_first_rows[['Exp', 'IV', 'Skew', '💲', 'Size']]
    #                 calls_selected_columns_df['Exp'] = calls_selected_columns_df['Exp'].apply(lambda x: x[5:])
    #                 puts_selected_columns_df['Exp'] = puts_selected_columns_df['Exp'].apply(lambda x: x[5:])
    #                 calls_selected_columns_df['IV'] = (calls_selected_columns_df['IV'] * 100).round(4)
    #                 puts_selected_columns_df['IV'] = (puts_selected_columns_df['IV'] * 100).round(4)
    #                 calls_selected_columns_df = calls_selected_columns_df.reset_index(drop=True)[['Exp', 'IV', 'Skew', '💲', 'Size']]
    #                 puts_selected_columns_df = puts_selected_columns_df.reset_index(drop=True)[['Exp', 'IV', 'Skew', '💲', 'Size']]

    #                 print(calls_selected_columns_df)
    #                 print(puts_selected_columns_df)
    #                 call_table = tabulate(calls_selected_columns_df, headers='keys', tablefmt='fancy', showindex=False)
    #                 put_table = tabulate(puts_selected_columns_df, headers='keys', tablefmt='fancy', showindex=False)
    #                 embed = disnake.Embed(title=f"Skews - {ticker} - Next 30 Days", description=f"**CALLS:**```{call_table}```\n**PUTS:**```{put_table}```", color=disnake.Colour.random())
    #                 embed.set_footer(text=f"Viewing Skews for {ticker}")
    #                 await inter.edit_original_message(embed=embed)
    #                 if counter == 50:
    #                     await inter.send("stream ended")
    #                     break

                                        
            
    #         ## non - spx money query

    #             else:
    #                 counter = 0
    #                 while True:
    #                     counter = counter + 1
    #                     price = await poly.get_stock_price(ticker)
                        
    #                     lower_strike = round(price) * 0.85 #greater thresholds for non-SPX
    #                     upper_strike = round(price) * 1.15
    #                     print(f"NON-SPX TICKER: {ticker}: {lower_strike}, {price}, {upper_strike}")
    #                     #query non SPX longer


                        
    #                     async with aiohttp.ClientSession() as session:
    #                         initial_url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte={seven_days_from_now_str}&limit=250&apiKey={YOUR_API_KEY}"
    #                         async with session.get(initial_url) as resp:
    #                             data = await resp.json()
    #                             results = data['results']
    #                             if results is not None:
    #                                 option_data = UniversalOptionSnapshot(results)
    #                                 symbols = str(option_data.ticker).replace("'","").replace(']','').replace('[','').replace(' ','')
    #                                 print(symbols)


                    
    #                                 async with aiohttp.ClientSession() as session:
    #                                     async with session.get(f"https://api.polygon.io/v3/snapshot?ticker.any_of={symbols}&limit=1&apiKey={YOUR_API_KEY}") as response:
    #                                         near_money = await response.json()
    #                                         near_money_results = near_money['results']
    #                                         if near_money_results is not None:
    #                                             atm_data = UniversalSnapshot(near_money_results)
                            
    #                                             df = atm_data.df.sort_values('IV', ascending=True)
    #                                             call_df = df[df['Type'] == 'call'].sort_values('IV', ascending=True)
    #                                             put_df = df[df['Type'] == 'put'].sort_values('IV', ascending=True)
                     

                                                

    #                                             # Add a field for the call options
    #                                             call_table = call_df[['Sym','💲','Strike', 'IV', 'Exp', 'Type', 'Vol']].iloc[[0]]
    #                                             put_table = put_df[['Sym','💲','Strike', 'IV', 'Exp', 'Type', 'Vol']].iloc[[0]]
    #                                             put_rows = put_table.values.tolist()
    #                                             put_table_str = tabulate(put_rows, headers=put_table.columns, tablefmt="fancy")

    #                                             call_rows = call_table.values.tolist()
    #                                             call_table_str = tabulate(call_rows, headers=call_table.columns, tablefmt="fancy")

    #                                             combined_table = pd.concat([put_table, call_table])

    #                                             table_rows = combined_table.values.tolist()
    #                                             table_str = tabulate(table_rows, headers=combined_table.columns, tablefmt="fancy")

    #                                             embed = disnake.Embed(title=f"Skew Monitor - {ticker}", description=f"```\n{table_str}\n```", color=disnake.Colour.random())
    #                                             embed.set_footer(text=f"{ticker}",icon_url=await poly.get_polygon_logo(ticker))
    #                                 await inter.edit_original_message(embed=embed)
    #                                 if counter == 50:
    #                                     await inter.send("Stream ended")
    #                                     break

def setup(bot:commands.Bot):
    bot.add_cog(Skew(bot))
    print(f"> Extension {__name__} is ready\n")