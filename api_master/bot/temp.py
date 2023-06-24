import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))


import aiohttp
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
import asyncio
import pandas as pd
from sdks.polygon_sdk.option_snapshot import OptionSnapshotData
from cfg import YOUR_API_KEY, today_str, thirty_days_from_now_str

tickers='PG,RBLX,JD,TSCO,BYND,GOOG,UBER,CAG,GME,CCL,QQQ,CSCO,FUTU,ARCC,GPN,CG,HUN,TNA,DXC,GRPN,ENTG,PEP,PGR,MSFT,PACW,PCG,ADBE,KRE,GILD,VST,VFC,JNJ,AMC,SQNS,CVS,CDE,SUP,TBIO,YALA,INO,LVS,WDAY,SPXU,TDOC,SBUX,LTRX,KIM,EMR,BOX,DD,TMUS,ATVI,ASAN,FTDR,HD,SCHW,IPSC,TARO,HASI,DIA,JWN,AVDX,MARA,PPL,MOS,ET,IAI,HOLI,QS,JBT,KEY,SFIX,AUPH,DXCM,CHRS,CRVS,SMRT,IBN,SQ,ACGL,ABT,AZN,INFN,KLR,BBAI,LYV,CTLT,TECK,BRMK,EFA,FCEL,ZGN,SBOW,NOVA,ARDX,FITB,GOOGL,SHOP,DAC,LNC,AMGN,TUYA,SYNH,NMTR,SMH,BGS,AEG,DKNG,FCX,NI,NMR,TSE,OBLG,CHPT,AES,NU,CRC,UNH,CIEN,FTCH,SWN,UP,RNG,EZPW,XPEV,PAAS,LBTYA,MUFG,BUD,INTZ,RKT,CLNE,APO,OTIS,VLY,DT,M,QCOM,PCT,TIL,IPG,ARKK,ADI,YUM,WMT,SMCI,XP,CCCC,AG,SAM,MGM,BOH,CAT,RYAN,MDT,HOWL,JETS,SYY,FLEX,VTRS,PYPL,VVV,UNIT,MRK,BANX,MRIN,VTR,NVDA,AVGO,GLUE,DOCU,KR,ASTS,CANO,MMM,ADVM,BIGC,SNDL,CZR,LX,HOOD,MDB,VIAV,SO,FTFT,STKH,RMTI,WEN,V,RYAM,AEP,TAP,PM,LOW,ALLO,DRH,AR,HBB,LESL,TELL,VTS,GLD,ASX,CCJ,STNE,NAT,SEE,NET,EA,EVA,LMB,BN,IEF,DELL,DADA,CX,RFL,DOW,INDI,DASH,ISEE,KWEB,XOP,TBLA,BX,FTV,PAYX,CL,XLU,LQD,STLA,MCHX,MSTR,ALLY,SU,HST,MULN,DLO,ONB,ACB,ABBV,FHN,XLI,AI,ORCL,CNET,BILI,COMP,EWZ,DSEY,WOW,BABA,BA,TLRY,EEM,SQQQ,CS,ANSS,NTCO,RIOT,KGC,TSP,BRDG,SKY,CSX,IBM,XIN,NEX,AAP,MCD,WRAP,LUMN,RPRX,BLDR,RXT,LABU,SYF,RPD,SGBX,RVLP,NXE,FNCB,SYPR,DVN,AQN,ONON,CNX,AGI,SPY,SVM,XLE,APPS,FRHC,AGEN,IOT,ZIM,BHC,ACN,AAL,SNAP,AFL,CRDO,BLNK,BOWL,VRAY,TRTX,ELAN,EOSE,UVXY,ZYNE,MQ,LYFT,ENVX,NKE,TNP,SAND,VZ,IWM,GE,XME,HTHT,XLK,GT,FAST,GLNG,IYR,DAL,KPTI,GS,BLDP,AVTR,BAC,NEWR,USAP,API,ANET,CRNT,LXP,SHLS,IP,BMBL,S,BFLY,LBTYK,LNT,DHT,CCO,NTAP,DOC,NGVC,PD,LAW,GTBP,RTX,BAX,LLY,FFIE,FLNT,PEG,FLO,COIN,CLOV,YMM,ETRN,IMAX,HSKA,WFC,GH,NEM,HITI,SSTI,EXPE,PFE,PATH,MFIN,ZTO,SGEN,UPRO,BCRX,CSIQ,ALIT,KOLD,AFRM,RXRX,TLT,NGM,OCGN,CTRA,FE,VERA,UDR,EVLV,XLC,NLY,TMF,GRAB,HAL,BITO,VALE,GSM,LBRDK,PRU,DNB,BP,HTZ,PXLW,CHWY,HYFM,LMNL,STT,ST,BGFV,FUBO,RUN,XLY,CGC,EFC,CNP,DISH,MANU,CVNA,AAOI,FSR,SANW,MREO,W,TMO,USB,DE,TDCX,ITRI,ZDGE,FXLV,ROKU,AVAH,PINS,VOD,SLP,PDS,AESI,CMCSA,PR,INTC,XLV,TSLA,WMB,OXY,IONQ,AMH,PLTR,ALEC,ACI,OSS,BIVI,JPM,MGNX,SPWR,LMT,SCPL,DLTR,ED,HPQ,LAZR,OSK,AIRS,FHTX,INSE,X,ADP,VMW,HRTG,BRLT,RDFN,ITUB,ETON,BIG,RCL,CBAT,RRC,ARR,SLI,ETN,OPEN,SENS,OWL,HBI,NVAX,DEI,ARMK,XRT,WEX,LSCC,LRCX,GOOS,IVZ,TLSA,APA,ROST,SLM,CERS,LGMK,DDOG,KMI,BTCM,AXLA,BTE,PAGS,FNGS,CRWD,ENOB,MGI,CMA,KHC,SGMO,WYNN,HYG,IOVA,ENSV,AMLX,VZIO,F,CIM,NFLX,ASC,WAL,AUMN,SOFI,DFS,TFC,FATE,JCI,CPB,HUT,CFG,IRIX,SKX,KSS,NRG,HZO,MCHP,AMX,KMB,MO,SPXS,IBRX,T,LC,MMAT,FUSN,FYBR,PEAK,CROX,PRDO,AMD,AEM,IFF,AMBA,U,CUZ,BOIL,XLF,EQT,DHI,AMZN,EGO,SOXS,VTGN,BBWI,FOXA,ASRT,GSAT,TXN,SPWH,HR,PDD,NVTS,ESI,KDP,DB,ERIC,OGN,SOXL,UPST,WOOF,PENN,ARAV,AIN,TPR,VKTX,MS,TIGR,GTLB,TSN,IRS,MA,GDXJ,FANH,UUP,FTCI,UNG,ETSY,KO,PAA,DNN,AA,TJX,ARRY,AM,CVE,AIG,COTY,LNG,TSM,NWL,BRFS,WTI,COST,AGNC,MTLS,RF,TOST,WBD,HLIT,MRNA,BMY,Z,TGT,XOM,URBN,DIS,SSSS,ENIC,DBRG,VXX,MLCO,RYN,ANF,ORC,LULU,SLG,SAVE,XENE,VERX,GEN,BIDU,SONO,GPRK,GP,NM,UAL,RITM,FXI,UPS,GURE,REXR,AAPL,SLB,MITT,IMBI,ODV,NEE,MESA,AEO,TQQQ,MRVL,SIG,ULTA,FDX,BB,ABR,EL,BEN,SIMO,PBR,CRBP,CAH,USO,SLV,META,GOLD,HPE,JFIN,EGHT,IEP,NTR,SID,SMWB,SPCE,ESLT,XBI,MSOS,CVX,RXST,CVT,AMRS,MTG,PRM,CHS,EPIX,COLB,ATUS,GM,MET,HZNP,SHEL,EQH,AMRN,PARA,ICLN,TARS,GFI,BEKE,NIO,GOEV,NCLH,EMB'

# # Define the base URL for the Polygon API
# base_url = "https://api.polygon.io/v3/snapshot/options/"

# class OptionContract:
#     def __init__(self, data):
#         self.callsymbol = [i['call symbol'] if 'call symbol' in i else None for i in data]
#         self.callname = [i['call name'] if 'call name' in i else None for i in data]
#         self.callstrike = [i['call strike'] if 'call strike' in i else None for i in data]
#         self.callexpiry = [i['call expiry'] if 'call expiry' in i else None for i in data]
#         self.callvolume = [i['call volume'] if 'call volume' in i else None for i in data]
#         self.calliv = [i['call iv'] if 'call iv' in i else None for i in data]

#         self.putsymbol = [i['put symbol'] if 'put symbol' in i else None for i in data]
#         self.putname = [i['put name'] if 'put name' in i else None for i in data]
#         self.putstrike = [i['put strike'] if 'put strike' in i else None for i in data]
#         self.putexpiry = [i['put expiry'] if 'put expiry' in i else None for i in data]
#         self.putvolume = [i['put volume'] if 'put volume' in i else None for i in data]
#         self.putiv = [i['put iv'] if 'put iv' in i else None for i in data]


#         self.call_data_dict = { 


#             'call name': self.callname,
#             'call strike': self.callstrike,
#             'call expiry': self.callexpiry,
#             'call volume': self.callvolume,
#             'call iv': self.calliv
#         }

#         self.put_data_dict = [ 


#             self.putname,
#             self.putstrike,
#             self.putexpiry,
#             self.putvolume,
#             self.putiv
#         ]

#         self.call_df = pd.DataFrame(self.call_data_dict)
#         self.put_df = pd.DataFrame(self.put_data_dict)


        
#         self.lowest_iv_calls = self.call_df.loc[0].dropna(how="any").loc
#         self.lowest_iv_puts = self.put_df.loc[0].dropna(how="any").loc



# async def get_near_the_money_options(ticker, lower_strike, upper_strike, today_str):
#     url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte={thirty_days_from_now_str}&limit=250&apiKey={YOUR_API_KEY}"

#     async with aiohttp.ClientSession() as session:
#         all_ticker = []  # to hold all the option symbols
#         next_url = None

#         while url:
#             async with session.get(url) as filtered_resp:
#                 if filtered_resp.status != 200:
#                     return None, None  # Return None for both URL and all_ticker
#                 data = await filtered_resp.json()
#                 results = data['results'] if data['results'] is not None else None
#                 details = [i['details'] if i['details'] is not None else None for i in results]
#                 ticker = [i.get('ticker', None) for i in details]
#                 all_ticker.extend(ticker)

#                 next_url = data.get('next_url')  # get the next page URL
#                 if next_url and YOUR_API_KEY not in next_url:
#                     next_url += f"&apiKey={YOUR_API_KEY}"  # append the API key to the URL

      

#             return all_ticker



# async def main():
#     tickers=["GME", "AMC"]
#     for ticker in tickers:
#         price = await poly.get_stock_price(ticker=ticker)

#         lower_strike = round(price * 0.90)
#         upper_strike = round(price * 1.00)

#         atm_options = str(await get_near_the_money_options(ticker,lower_strike,upper_strike,today_str))

#         atm_options = atm_options.replace("[", "").replace("]", "").replace("'", "").replace(" ", "").replace("None,", "").replace("(", "").replace(")", "")


#         url = f"https://api.polygon.io/v3/snapshot?ticker.any_of={atm_options}&apiKey={YOUR_API_KEY}"
#         # Find the index of the first "(" character


#         x=await opts.find_lowest_iv(url)
#         calldata, putdata = [OptionContract(i) for i in x]

#         calls = list(calldata.call_data_dict.items())
#         puts = list(putdata.put_data_dict[0])
        
# asyncio.run(main())
#https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte={five_days_from_now_str}&limit=250&apiKey={YOUR_API_KEY}

from urllib.parse import urlencode


async def _request_all_pages_concurrently(session, initial_url, params=None, api_key=YOUR_API_KEY):
    if params is None:
        params = {}
    params["apiKey"] = api_key

    all_results = []
    next_url = initial_url
    while next_url:
        try:
            async with session.get(next_url, params=params) as response:
                response.raise_for_status()
                data = await response.json()

                if "results" in data:
                    all_results.extend(data["results"])

                next_url = data.get("next_url")
                if next_url:
                    next_url += f'&{urlencode({"apiKey": api_key})}'
                    params = {}

        except aiohttp.ClientResponseError as http_err:
            print(f"An HTTP error occurred: {http_err}")
            break
        except Exception as err:
            print(f"An error occurred: {err}")
            break

    return all_results


ticker_symbols = ['AAPL', 'MSFT', 'AMZN', 'NVDA', 'GOOGL', 'TSLA', 'GOOG', 'META', 'BRK.B', 'UNH', 
                  'JNJ', 'XOM', 'JPM', 'V', 'LLY', 'PG', 'AVGO', 'MA', 'HD', 'MRK', 'CVX', 'PEP', 
                  'ABBV', 'KO', 'COST', 'ADBE', 'PFE', 'WMT', 'MCD', 'CSCO', 'CRM', 'TMO', 'ACN', 
                  'BAC', 'ABT', 'NFLX', 'ORCL', 'LIN', 'AMD', 'CMCSA', 'DIS', 'DHR', 'TXN', 'WFC', 'HAL',
                  'NEE', 'VZ', 'PM', 'RTX', 'BMY', 'INTC', 'NKE', 'HON', 'QCOM', 'LOW', 'SPGI', 'INTU',
                  'UNP', 'UPS', 'COP', 'AMGN', 'CAT', 'IBM', 'AMAT', 'BA', 'MDT', 'SBUX', 'ISRG', 
                  'GE', 'DE', 'NOW', 'T', 'MS', 'PLD', 'ELV', 'GS', 'LMT', 'BLK', 'MDLZ', 'SYK', 
                  'AXP', 'BKNG', 'GILD', 'ADI', 'TJX', 'ADP', 'C', 'MMC', 'VRTX', 'CVS', 'AMT', 
                  'REGN', 'LRCX', 'CI', 'CB', 'ZTS', 'SCHW', 'BSX', 'MO', 'ETN', 'SO', 'TMUS', 'SNAP','AMC','GME',
                  'PGR', 'PYPL', 'PANW', 'FI', 'BDX', 'MU', 'EQIX', 'SPY', 'U', 'W', 'SHOP', 'KRE', 'EEM', 'EWZ', 'BABA', 'BIDU', 'BEKE']
async def search_chain(underlying_asset, limit=250):
        
        """
        Get all options contracts for an underlying ticker across all pages.

        :param underlying_asset: The underlying ticker symbol of the option contract.
        :param strike_price: Query by strike price of a contract.
        :param expiration_date: Query by contract expiration with date format YYYY-MM-DD.
        :param contract_type: Query by the type of contract.
        :param order: Order results based on the sort field.
        :param limit: Limit the number of results returned, default is 10 and max is 250.
        :param sort: Sort field used for ordering.
        :return: A list containing all option chain data across all pages.
        """
poly = AsyncPolygonSDK(YOUR_API_KEY)
async def get_option_data(ticker, session):

    base_url = "https://api.polygon.io/v3/snapshot/options/"
    price = await poly.get_stock_price(ticker)
    if price is not None:
        lower_strike = round(price * 0.97)
        upper_strike = round(price * 1.03)
        
        endpoint = f"{base_url}{ticker}"
        params = {
            "strike_price.gte": lower_strike,
            "strike_price.lte": upper_strike,
            "expiration_date.gte": today_str,
            "expiration_date.lte": thirty_days_from_now_str,
            "limit": 250,
            "apiKey": YOUR_API_KEY
        }
        response_data = await _request_all_pages_concurrently(session, endpoint, params=params, api_key=YOUR_API_KEY)
        option_data = OptionSnapshotData(response_data)

        if option_data is not None:
            df = pd.DataFrame(option_data.data_dict).dropna(how="any").sort_values('implied_volatility', ascending=True)
            if not df.empty:
                df = df.iloc[[0]]
                for _, row in df.iterrows():
                    strike = row['strike_price']
                    symbol = row['underlying_ticker']
                    iv = round(float(row['implied_volatility'])*100,5)
                    underlying_price = row['underlying_price']
                    expiry = row['expiration_date']
                    expiry = expiry[5:]
                    skew = "🔥" if strike <= underlying_price else "🟢"
                    skew_metric = strike - underlying_price

                    return [symbol, strike, underlying_price, expiry, iv, skew, skew_metric]
        return None
    
async def get_option_data(ticker, price, session):

    base_url = "https://api.polygon.io/v3/snapshot/options/"
    price = await poly.get_stock_price(ticker)
    if price is not None:
        lower_strike = round(price * 0.97)
        upper_strike = round(price * 1.03)
        
        endpoint = f"{base_url}{ticker}"
        params = {
            "strike_price.gte": lower_strike,
            "strike_price.lte": upper_strike,
            "expiration_date.gte": today_str,
            "expiration_date.lte": thirty_days_from_now_str,
            "limit": 250,
            "apiKey": YOUR_API_KEY
        }
        response_data = await _request_all_pages_concurrently(session, endpoint, params=params, api_key=YOUR_API_KEY)
        option_data = OptionSnapshotData(response_data)

        if option_data is not None:
            df = pd.DataFrame(option_data.data_dict).dropna(how="any").sort_values('implied_volatility', ascending=True)
            if not df.empty:
                df = df.iloc[[0]]
                for _, row in df.iterrows():
                    strike = row['strike_price']
                    symbol = row['underlying_ticker']
                    iv = round(float(row['implied_volatility'])*100,5)
                    underlying_price = row['underlying_price']
                    expiry = row['expiration_date']
                    expiry = expiry[5:]
                    skew = "🔥" if strike <= underlying_price else "🟢"
                    skew_metric = strike - underlying_price
                    if skew_metric < -5.5 or skew_metric > 5.5:
                                        return [symbol, strike, underlying_price, expiry, iv, skew, skew_metric]
        return None


# import aiohttp
# async def main():
#     tasks = []
    
#     async with aiohttp.ClientSession() as session:

#         for ticker in ticker_symbols:
#             tasks.append(asyncio.ensure_future(get_option_data(ticker, session)))
#         await asyncio.gather(*tasks)

# if __name__ == "__main__":
#     asyncio.run(main())
