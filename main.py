from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
import asyncio
from cfg import date_string, webull_headers
sdk = AsyncWebullSDK()



"""YOU CAN USE DOT NOTATION FOR ALL OF THESE COMMANDS"""




async def main():
    ticker = "GME"

    capital_flow = await sdk.capital_flow(ticker) #good
   # print(capital_flow.largein)

    balance_sheet = await sdk.get_balancesheet(ticker)
    fin_statement = await sdk.get_financial_statement(ticker)
    cash_flow = await sdk.get_cash_flow(ticker)
    
    market_data = await sdk.get_webull_stock_data(ticker)
    price = market_data.web_stock_close
    print(market_data.avg_10d_vol)

    financial_ratios=    await sdk.calculate_ratios(balance_sheet, fin_statement, cash_flow, price)
    print(financial_ratios)




    score = await sdk.calculate_score(capital_expenditures=cash_flow[0].capital_expenditures, cash_from_financing_activities=cash_flow[0].cash_from_financing_activities,cash_from_investing_activities=cash_flow[0].cash_from_investing_activities,cash_from_operating_activities=cash_flow[0].cash_from_operating_activities,net_change_in_cash=cash_flow[0].net_change_in_cash,total_cash_dividends_paid=cash_flow[0].total_cash_dividends_paid, net_income=cash_flow[0].net_income)
    print(score)



    calendar = await sdk.get_earnings_calendar(date_string)
    tickers = [i.ticker for i in calendar]
    for i in tickers:
        symbol = i['symbol']
        print(symbol)


    recentnews = await sdk.check_recent_news(ticker, webull_headers=webull_headers)
    print(recentnews)


    financial_score = await sdk.financial_score(ticker)
    print(financial_score)


    analysts = await sdk.get_analysis_data(ticker)
    print(analysts.buy)


    inst = await sdk.get_institutional_holdings(ticker)

    print(inst.institution_holding.decrease.holding_count_change)


    etfs = await sdk.get_etf_categories("commodity")
    print(etfs[0].asset_type)


   # news_for_real = await sdk.get_recent_news_for_tickers(ticker, webull_headers=webull_headers)
    #print(news_for_real[0]['news_url'])

    shortint = await sdk.get_short_interest(ticker)
    print(shortint.avg_volume)


    vol_anal = await sdk.get_webull_vol_analysis_data(ticker)

    print(vol_anal.avePrice)


asyncio.run(main())