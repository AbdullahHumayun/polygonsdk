import asyncio

from sdks.fed_newyork_sdk.sdk import FedNewyork
from sdks.nasdaq_sdk.sdk import Nasdaq
from sdks.occ_sdk.sdk import occSDK
from sdks.stocksera_sdk.sdk import StockeraSDK
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK

from cfg import YOUR_API_KEY,today_str ##replace with your API keys - links in cfg.py


polygon = AsyncPolygonSDK(YOUR_API_KEY) #async
polygon_options = PolygonOptionsSDK(YOUR_API_KEY) #async
webull = AsyncWebullSDK() #async

stocksera = StockeraSDK() 
nasdaq = Nasdaq()
occ = occSDK()
fed = FedNewyork()


async def polygon_quickstart(ticker="GME"): #for polygon, polygon_options, webull functions


    ##polygon##

    company_info = await polygon.company_info("GME")


    #accessing the attributes for functions works the same throughout this project
    cik = company_info
    composite_figi = company_info.composite_figi
    description = company_info.description
    homepage_url = company_info.homepage_url
    list_date = company_info.list_date
    locale = company_info.locale
    market = company_info.market
    market_cap = company_info.market_cap
    name = company_info.name
    phone_number = company_info.phone_number
    primary_exchange = company_info.primary_exchange
    round_lot = company_info.round_lot
    share_class_figi = company_info.share_class_figi
    share_class_shares_outstanding = company_info.share_class_shares_outstanding
    sic_code = company_info.sic_code
    sic_description = company_info.sic_description
    ticker = company_info.ticker

    #print the attributes
    print("CIK:", cik)
    print("Composite FIGI:", composite_figi)
    print("Currency Name:", currency_name)
    print("Description:", description)
    print("Homepage URL:", homepage_url)
    print("List Date:", list_date)
    print("Locale:", locale)
    print("Market:", market)
    print("Market Cap:", market_cap)
    print("Name:", name)
    print("Phone Number:", phone_number)
    print("Primary Exchange:", primary_exchange)
    print("Round Lot:", round_lot)
    print("Share Class FIGI:", share_class_figi)
    print("Share Class Shares Outstanding:", share_class_shares_outstanding)
    print("SIC Code:", sic_code)
    print("SIC Description:", sic_description)
    print("Ticker:", ticker)

asyncio.run(polygon_quickstart(ticker="GME"))



#webull##


async def webull_quickstart(ticker="GME"):
    ##webull##
    volume_analysis = await webull.get_webull_vol_analysis_data("GME")
    avg_price = volume_analysis.avePrice
    buy_volume = volume_analysis.buyVolume
    neutral_volume = volume_analysis.nVolume
    sell_volume = volume_analysis.sellVolume
    total_volume = volume_analysis.totalVolume

    print(f"Average Price:", avg_price)
    print(f"Buy Volume:", buy_volume)
    print(f"Sell Volume:", sell_volume)
    print(f"Neutral Volume:", neutral_volume)
    print(f"Total Volume:", total_volume)



asyncio.run(webull_quickstart(ticker="GME"))



## stocksera ##


inflation = stocksera.inflation()

print(inflation)



## nasdaq ##
bicmac = nasdaq.bigmac()



## fed ##
mbs_operations = fed.agency_mbs_search(start_date="2023-01-01", end_date=today_str)


auctionStatus = mbs_operations.auctionStatus
classType = mbs_operations.classType
closeTime = mbs_operations.closeTime
lastUpdated = mbs_operations.lastUpdated
method = mbs_operations.method
note = mbs_operations.note
operationId = mbs_operations.operationId
operationDate = mbs_operations.operationDate
operationDirection = mbs_operations.operationDirection
operationType = mbs_operations.operationType
settlementDate = mbs_operations.settlementDate
totalAcceptedOrigFace = mbs_operations.totalAcceptedOrigFace
totalAcceptedCurrFace = mbs_operations.totalAcceptedCurrFace
totalAmtAcceptedPar = mbs_operations.totalAmtAcceptedPar
totalAmtSubmittedPar = mbs_operations.totalAmtSubmittedPar
totalSubmittedCurrFace = mbs_operations.totalSubmittedCurrFace
totalSubmittedOrigFace = mbs_operations.totalSubmittedOrigFace

print("Auction Status:", mbs_operations.auctionStatus)
print("Class Type:", mbs_operations.classType)
print("Close Time:", mbs_operations.closeTime)
print("Last Updated:", mbs_operations.lastUpdated)
print("Method:", mbs_operations.method)
print("Note:", mbs_operations.note)
print("Operation ID:", mbs_operations.operationId)
print("Operation Date:", mbs_operations.operationDate)
print("Operation Direction:", mbs_operations.operationDirection)
print("Operation Type:", mbs_operations.operationType)
print("Settlement Date:", mbs_operations.settlementDate)
print("Total Accepted Original Face:", mbs_operations.totalAcceptedOrigFace)
print("Total Accepted Current Face:", mbs_operations.totalAcceptedCurrFace)
print("Total Amount Accepted Par:", mbs_operations.totalAmtAcceptedPar)
print("Total Amount Submitted Par:", mbs_operations.totalAmtSubmittedPar)
print("Total Submitted Current Face:", mbs_operations.totalSubmittedCurrFace)
print("Total Submitted Original Face:", mbs_operations.totalSubmittedOrigFace)





## occ ##
##this example shows you how to access the data-frame. all functions will have an "as_dataframe" option

loans = occ.stock_loans(report_date=today_str, type="daily")
df = loans.as_dataframe
print(df)