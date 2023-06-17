import requests
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
from examples.webull_data import Webull
from cfg import thirty_days_from_now_str
import aiohttp
webull = AsyncWebullSDK()



async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()

async def get_price_data(api_key,tickers: str):
    if tickers.startswith('SPX'):
        ticker = "I:SPX"
        type = "v3/snapshot/indices/I:SPX"
        url = f"https://api.polygon.io/v3/snapshot/indices?ticker.any_of=I:SPX&apiKey={api_key}"
        async with aiohttp.ClientSession() as session:
            return await fetch(session, url)
    else:
        type = "v2/snapshot/locale/us/markets/stocks/tickers"
        url = f"https://api.polygon.io/v3/snapshot?ticker.any_of={tickers}&apiKey={api_key}"
        print(url)
        async with aiohttp.ClientSession() as session:
            return await fetch(session, url)

async def get_near_the_money_symbols(ticker,api_key, lower_strike, upper_strike, today_str):

    url = f"https://api.polygon.io/v3/snapshot/options/{ticker}?strike_price.gte={lower_strike}&strike_price.lte={upper_strike}&expiration_date.gte={today_str}&expiration_date.lte={today_str}&limit=250&apiKey={api_key}"
    async with aiohttp.ClientSession() as session:
        return await fetch(session, url)

async def get_filtered_contracts(api_key, output):
    url = f"https://api.polygon.io/v3/snapshot?ticker.any_of={output}&apiKey={api_key}"
    async with aiohttp.ClientSession() as session:
        return await fetch(session, url)


async def earnings_calendar_endpoint(ticker):
    earnings_calendar = await webull.get_earnings_calendar(date_str=thirty_days_from_now_str)
    
    earnings_data = {
        "earning_release_id": earnings_calendar[0].earning_release_id,
        "eps": earnings_calendar[0].eps,
        "eps_estimate": earnings_calendar[0].eps_estimate,
        "is_live": earnings_calendar[0].is_live,
        "last_release_date": earnings_calendar[0].last_release_date,
        "publish_status": earnings_calendar[0].publish_status,
        "qualifier": earnings_calendar[0].qualifier,
        "quarter": earnings_calendar[0].quarter,
        "release_date": earnings_calendar[0].release_date,
        "region_id": earnings_calendar[0].region_id,
        "year": earnings_calendar[0].year,
        "ticker": earnings_calendar[0].ticker,
        "ticker_id": earnings_calendar[0].ticker_id
    }
    
    return earnings_data

async def stock_data_endpoint(ticker):
    stock_data = await webull.get_webull_stock_data(ticker)
    if stock_data:
        avg_10d_vol = stock_data.avg_10d_vol
        avg_vol3m = stock_data.avg_vol3m
        estimated_earnings = stock_data.estimated_earnings
        fifty_high = stock_data.fifty_high
        fifty_low = stock_data.fifty_low
        last_earnings = stock_data.last_earnings
        outstanding_shares = stock_data.outstanding_shares
        web_change_ratio = round(float(stock_data.web_change_ratio)*100,2)
        total_shares = stock_data.total_shares
        web_exchange = stock_data.web_exchange
        web_name = stock_data.web_name
        web_stock_close = stock_data.web_stock_close
        web_stock_high = stock_data.web_stock_high
        web_stock_low = stock_data.web_stock_low
        web_stock_open = stock_data.web_stock_open
        web_stock_vol = float(stock_data.web_stock_vol)
        web_symb = stock_data.web_symb
        web_vibrate_ratio = stock_data.web_vibrate_ratio

        data_dict = {
            "Average 10 Day Volume": stock_data.avg_10d_vol,
            "Average Volume 3 Months": stock_data.avg_vol3m,
            "Estimated Earnings Data": stock_data.estimated_earnings,
            "Fifty Two Week High": stock_data.fifty_high,
            "Fifty Two Week Low": stock_data.fifty_low,
            "Next Earnings": stock_data.last_earnings,
            "Outstanding Shares": stock_data.outstanding_shares,
            "Web Change Ratio": round(float(stock_data.web_change_ratio) * 100, 2),
            "Total Shares": stock_data.total_shares,
            "Exchange": stock_data.web_exchange,
            "Company Name": stock_data.web_name,
            "Stock Close": stock_data.web_stock_close,
            "Stock High": stock_data.web_stock_high,
            "Stock Low": stock_data.web_stock_low,
            "Stock Open": stock_data.web_stock_open,
            "Stock Volume": float(stock_data.web_stock_vol),
            "Symbol": stock_data.web_symb,
            "Vibrate Ratio": stock_data.web_vibrate_ratio
        }

        return data_dict



async def analyst_ratings_endpoint(ticker):
    analysis_data = await webull.get_analysis_data(ticker)
    if analysis_data is None:
        return

    buy = analysis_data.buy if analysis_data.buy is not None else "N/A"
    hold = analysis_data.hold if analysis_data.hold is not None else "N/A"
    overall_rating = analysis_data.rating if analysis_data.rating is not None else "N/A"
    suggestion = analysis_data.rating_suggestion if analysis_data.rating_suggestion is not None else "N/A"
    rating_totals = analysis_data.rating_totals if analysis_data.rating_totals is not None else "N/A"
    sell = analysis_data.sell if analysis_data.sell is not None else "N/A"
    strongbuy = analysis_data.strongbuy if analysis_data.strongbuy is not None else "N/A"
    underperform = analysis_data.underperform if analysis_data.underperform is not None else "N/A"

    data_dict = { 
        'Strong Buy Ratings': strongbuy,
        'Buy Ratings': buy,
        'Hold Ratings': hold,
        'Underperform Rating': underperform,
        'Sell Rating': sell,
        'Analyst Count': rating_totals,
        'Suggestion': suggestion,
        'Overall Rating': overall_rating
    }

    return data_dict
async def institutional_holdings_endpoint(ticker):
    institutionHoldings = await webull.get_institutional_holdings(ticker)
    if institutionHoldings is None:
        return

    decreaseChange = float(institutionHoldings.institution_holding.decrease.holding_count_change) if institutionHoldings.institution_holding.decrease.holding_count_change is not None else "N/A"
    decreasedShares = float(institutionHoldings.institution_holding.decrease.institutional_count) if institutionHoldings.institution_holding.decrease.institutional_count is not None else "N/A"
    increaseChange = float(institutionHoldings.institution_holding.increase.holding_count_change) if institutionHoldings.institution_holding.increase.holding_count_change is not None else "N/A"
    increasedShares = float(institutionHoldings.institution_holding.increase.institutional_count) if institutionHoldings.institution_holding.increase.institutional_count is not None else "N/A"
    newChange = float(institutionHoldings.institution_holding.new_position.holding_count_change) if institutionHoldings.institution_holding.new_position.holding_count_change is not None else "N/A"
    newShares = float(institutionHoldings.institution_holding.new_position.institutional_count) if institutionHoldings.institution_holding.new_position.institutional_count is not None else "N/A"
    soldOutChange = float(institutionHoldings.institution_holding.sold_out.holding_count_change) if institutionHoldings.institution_holding.sold_out.holding_count_change is not None else "N/A"
    soldOutShares = float(institutionHoldings.institution_holding.sold_out.institutional_count) if institutionHoldings.institution_holding.sold_out.institutional_count is not None else "N/A"
    net_shares_changed = soldOutChange + newChange + increaseChange + decreaseChange
    net_institution_change = newShares + soldOutShares + increasedShares + decreasedShares

    stats = institutionHoldings.institution_holding.stat
    totalHeldShares = stats.holding_count if stats.holding_count is not None else "N/A"
    totalHeldSharesChange = stats.holding_count_change if stats.holding_count_change is not None else "N/A"
    totalOwnershipRatioOfFloat = stats.holding_ratio if stats.holding_ratio is not None else "N/A"
    totalOwnershipRatioOfFloatChange = stats.holding_ratio_change if stats.holding_ratio_change is not None else "N/A"
    totalNumberOfInstitutions = float(stats.institutional_count) if stats.institutional_count is not None else "N/A"

    data_dict = {
        'decreaseChange': float(institutionHoldings.institution_holding.decrease.holding_count_change) if institutionHoldings.institution_holding.decrease.holding_count_change is not None else "N/A",
        'decreasedShares': float(institutionHoldings.institution_holding.decrease.institutional_count) if institutionHoldings.institution_holding.decrease.institutional_count is not None else "N/A",
        'increaseChange': float(institutionHoldings.institution_holding.increase.holding_count_change) if institutionHoldings.institution_holding.increase.holding_count_change is not None else "N/A",
        'increasedShares': float(institutionHoldings.institution_holding.increase.institutional_count) if institutionHoldings.institution_holding.increase.institutional_count is not None else "N/A",
        'newChange': float(institutionHoldings.institution_holding.new_position.holding_count_change) if institutionHoldings.institution_holding.new_position.holding_count_change is not None else "N/A",
        'newShares': float(institutionHoldings.institution_holding.new_position.institutional_count) if institutionHoldings.institution_holding.new_position.institutional_count is not None else "N/A",
        'soldOutChange': float(institutionHoldings.institution_holding.sold_out.holding_count_change) if institutionHoldings.institution_holding.sold_out.holding_count_change is not None else "N/A",
        'soldOutShares': float(institutionHoldings.institution_holding.sold_out.institutional_count) if institutionHoldings.institution_holding.sold_out.institutional_count is not None else "N/A"
    }

    data_dict['net_shares_changed'] = data_dict['soldOutChange'] + data_dict['newChange'] + data_dict['increaseChange'] + data_dict['decreaseChange']
    data_dict['net_institution_change'] = data_dict['newShares'] + data_dict['soldOutShares'] + data_dict['increasedShares'] + data_dict['decreasedShares']

    stats = institutionHoldings.institution_holding.stat
    data_dict['totalHeldShares'] = stats.holding_count if stats.holding_count is not None else "N/A"
    data_dict['totalHeldSharesChange'] = stats.holding_count_change if stats.holding_count_change is not None else "N/A"
    data_dict['totalOwnershipRatioOfFloat'] = stats.holding_ratio if stats.holding_ratio is not None else "N/A"
    data_dict['totalOwnershipRatioOfFloatChange'] = stats.holding_ratio_change if stats.holding_ratio_change is not None else "N/A"
    data_dict['totalNumberOfInstitutions'] = float(stats.institutional_count) if stats.institutional_count is not None else "N/A"


    return data_dict


async def short_interest_endpoint(ticker):
    short_interest = await webull.get_short_interest(ticker)
    if short_interest is None:
        return

    short_int = f"{float(short_interest.short_int[0]):,}" if short_interest.short_int[0] is not None else "N/A"
    avg_vol = f"{float(short_interest.avg_volume[0]):,}" if short_interest.avg_volume[0] is not None else "N/A"
    days_to_cover = short_interest.days_to_cover[0] if short_interest.days_to_cover[0] is not None else "N/A"
    settlement = short_interest.settlement[0] if short_interest.settlement[0] is not None else "N/A"


    data_dict = { 
        'Short Interest': short_int,
        'Average Volume': avg_vol,
        'Days to Cover': days_to_cover,
        'Settlement Date': settlement
    }

    return data_dict

async def capital_flow_endpoint(ticker):
    capitalFlow = await webull.capital_flow(ticker)
    largeNet = capitalFlow.largenet if capitalFlow.largenet is not None else "N/A"
    largeIn = capitalFlow.largein if capitalFlow.largein is not None else "N/A"
    largeOut = capitalFlow.largeout if capitalFlow.largeout is not None else "N/A"

    majorNet = capitalFlow.majornet if capitalFlow.majornet is not None else "N/A"
    majorIn = capitalFlow.majorin if capitalFlow.majorin is not None else "N/A"
    majorOut = capitalFlow.majorout if capitalFlow.majorout is not None else "N/A"
    majorInRatio = capitalFlow.majorinratio if capitalFlow.majorinratio is not None else "N/A"
    majorOutRatio = capitalFlow.majoroutratio if capitalFlow.majoroutratio is not None else "N/A"

    smallNet = capitalFlow.smallnet if capitalFlow.smallnet is not None else "N/A"
    smallIn = capitalFlow.smallin if capitalFlow.smallin is not None else "N/A"
    smallOut = capitalFlow.smallout if capitalFlow.smallout is not None else "N/A"
    smallInRatio = capitalFlow.smallinratio if capitalFlow.smallinratio is not None else "N/A"
    smallOutRatio = capitalFlow.smalloutratio if capitalFlow.smalloutratio is not None else "N/A"

    retailIn = capitalFlow.retailin if capitalFlow.retailin is not None else "N/A"
    retailOutRatio = capitalFlow.retailoutratio if capitalFlow.retailoutratio is not None else "N/A"
    retailInRatio = capitalFlow.retailinratio if capitalFlow.retailinratio is not None else "N/A"
    retailOut = capitalFlow.retailout if capitalFlow.retailout is not None else "N/A"

    mediumIn = capitalFlow.mediumin if capitalFlow.mediumin is not None else "N/A"
    mediumOut = capitalFlow.mediumout if capitalFlow.mediumout is not None else "N/A"
    mediumNet = capitalFlow.mediumnet if capitalFlow.mediumnet is not None else "N/A"
    mediumInRatio = capitalFlow.mediuminratio if capitalFlow.mediuminratio is not None else "N/A"
    mediumOutRatio = capitalFlow.mediumoutratio if capitalFlow.mediumoutratio is not None else "N/A"

    superIn = capitalFlow.superin if capitalFlow.superin is not None else "N/A"
    superOut = capitalFlow.superout if capitalFlow.superout is not None else "N/A"
    superNet = capitalFlow.supernet if capitalFlow.supernet is not None else "N/A"

    newLargeIn = capitalFlow.newlargein if capitalFlow.newlargein is not None else "N/A"
    newLargeOut = capitalFlow.newlargeout if capitalFlow.newlargeout is not None else "N/A"
    newLargeNet = capitalFlow.newlargenet if capitalFlow.newlargenet is not None else "N/A"
    newLargeInRatio = capitalFlow.newlargeinratio if capitalFlow.newlargeinratio is not None else "N/A"
    newLargeOutRatio = capitalFlow.newlargeoutratio if capitalFlow.newlargeoutratio is not None else "N/A"
    capital_flow_dict = {
        'largeNet': largeNet,
        'largeIn': largeIn,
        'largeOut': largeOut,
        'majorNet': majorNet,
        'majorIn': majorIn,
        'majorOut': majorOut,
        'majorInRatio': majorInRatio,
        'majorOutRatio': majorOutRatio,
        'smallNet': smallNet,
        'smallIn': smallIn,
        'smallOut': smallOut,
        'smallInRatio': smallInRatio,
        'smallOutRatio': smallOutRatio,
        'retailIn': retailIn,
        'retailOutRatio': retailOutRatio,
        'retailInRatio': retailInRatio,
        'retailOut': retailOut,
        'mediumIn': mediumIn,
        'mediumOut': mediumOut,
        'mediumNet': mediumNet,
        'mediumInRatio': mediumInRatio,
        'mediumOutRatio': mediumOutRatio,
        'superIn': superIn,
        'superOut': superOut,
        'superNet': superNet,
        'newLargeIn': newLargeIn,
        'newLargeOut': newLargeOut,
        'newLargeNet': newLargeNet,
        'newLargeInRatio': newLargeInRatio,
        'newLargeOutRatio': newLargeOutRatio
    }

    return capital_flow_dict

async def financial_ratios_endpoint(ticker):
    balance_sheet = await webull.get_balancesheet(ticker)
    fin_statement = await webull.get_financial_statement(ticker)
    cash_flow = await webull.get_cash_flow(ticker)
    
    market_data = await webull.get_webull_stock_data(ticker)
    price = market_data.web_stock_close
    print(market_data.avg_10d_vol)

    financial_ratios=    await webull.calculate_ratios(balance_sheet, 
                                                    fin_statement, 
                                                    cash_flow, price)
    
    return financial_ratios


async def balance_sheet_endpoint(ticker):
    balance_sheet = await webull.get_balancesheet(ticker)
    if balance_sheet is None:
        return None

    try:
        accounts_payable = [i.accountsPayable if i.accountsPayable is not None else "N/A" for i in balance_sheet]
        accounts_receivable = [i.accountsReceTradeNet if i.accountsReceTradeNet is not None else "N/A" for i in balance_sheet]
        accrued_expenses = [i.accruedExpenses if i.accruedExpenses is not None else "N/A" for i in balance_sheet]
        accumulated_depreciation = [i.accumulatedDepreciationTotal if i.accumulatedDepreciationTotal is not None else "N/A" for i in balance_sheet]
        additional_paid_in_capital = [i.additionalPaidInCapital if i.additionalPaidInCapital is not None else "N/A" for i in balance_sheet]
        cash_and_short_term_investments = [i.cashAndShortTermInvest if i.cashAndShortTermInvest is not None else "N/A" for i in balance_sheet]
        cash_equivalents = [i.cashEquivalents if i.cashEquivalents is not None else "N/A" for i in balance_sheet]
        common_stock = [i.commonStock if i.commonStock is not None else "N/A" for i in balance_sheet]
        current_port_of_long_term_debt = [i.currentPortofLTDebtCapitalLeases if i.currentPortofLTDebtCapitalLeases is not None else "N/A" for i in balance_sheet]
        balance_sheet_end_date = [i.endDate if i.endDate is not None else "N/A" for i in balance_sheet]
        balance_sheet_fiscal_period = [i.fiscalPeriod if i.fiscalPeriod is not None else "N/A" for i in balance_sheet]
        balance_sheet_fiscal_year = [i.fiscalYear if i.fiscalYear is not None else "N/A" for i in balance_sheet]
        long_term_debt = [i.longTermDebt if i.longTermDebt is not None else "N/A" for i in balance_sheet]
        notes_payable_short_term_debt = [i.notesPayableShortTermDebt if i.notesPayableShortTermDebt is not None else "N/A" for i in balance_sheet]
        other_current_assets = [i.otherCurrentAssetsTotal if i.otherCurrentAssetsTotal is not None else "N/A" for i in balance_sheet]
        other_equity = [i.otherEquityTotal if i.otherEquityTotal is not None else "N/A" for i in balance_sheet]
        other_liabilities = [i.otherLiabilitiesTotal if i.otherLiabilitiesTotal is not None else "N/A" for i in balance_sheet]
        other_long_term_assets = [i.otherLongTermAssetsTotal if i.otherLongTermAssetsTotal is not None else "N/A" for i in balance_sheet]
        ppe_total_gross = [i.ppeTotalGross if i.ppeTotalGross is not None else "N/A" for i in balance_sheet]
        ppe_total_net = [i.ppeTotalNet if i.ppeTotalNet is not None else "N/A" for i in balance_sheet]
        prepaid_expenses = [i.prepaidExpenses if i.prepaidExpenses is not None else "N/A" for i in balance_sheet]
        balance_sheet_publish_date = [i.publishDate if i.publishDate is not None else "N/A" for i in balance_sheet]
        retained_earnings = [i.retainedEarnings if i.retainedEarnings is not None else "N/A" for i in balance_sheet]
        short_term_investments = [i.shortTermInvestments if i.shortTermInvestments is not None else "N/A" for i in balance_sheet]
        total_assets = [i.totalAssets if i.totalAssets is not None else "N/A" for i in balance_sheet]
        total_common_shares_outstanding = [i.totalCommonSharesOutstanding if i.totalCommonSharesOutstanding is not None else "N/A" for i in balance_sheet]
        total_current_assets = [i.totalCurrentAssets if i.totalCurrentAssets is not None else "N/A" for i in balance_sheet]
        total_current_liabilities = [i.totalCurrentLiabilities if i.totalCurrentLiabilities is not None else "N/A" for i in balance_sheet]
        total_debt = [i.totalDebt if i.totalDebt is not None else "N/A" for i in balance_sheet]
        total_equity = [i.totalEquity if i.totalEquity is not None else "N/A" for i in balance_sheet]
        total_inventory = [i.totalInventory if i.totalInventory is not None else "N/A" for i in balance_sheet]
        total_liabilities = [i.totalLiabilities if i.totalLiabilities is not None else "N/A" for i in balance_sheet]
        total_liabilities_shareholders_equity = [i.totalLiabilitiesShareholdersEquity if i.totalLiabilitiesShareholdersEquity is not None else "N/A" for i in balance_sheet]
        total_long_term_debt = [i.totalLongTermDebt if i.totalLongTermDebt is not None else "N/A" for i in balance_sheet]
        total_non_current_assets = [i.totalNonCurrentAssets if i.totalNonCurrentAssets is not None else "N/A" for i in balance_sheet]
        total_non_current_liabilities = [i.totalNonCurrentLiabilities if i.totalNonCurrentLiabilities is not None else "N/A" for i in balance_sheet]
        total_receivables_net = [i.totalReceivablesNet if i.totalReceivablesNet is not None else "N/A" for i in balance_sheet]
        total_stockholders_equity = [i.totalStockhodersEquity if i.totalStockhodersEquity is not None else "N/A" for i in balance_sheet]
        balance_sheet_type = [i.type if i.type is not None else "N/A" for i in balance_sheet]
    except Exception as e:
        print(f"Failed to get balance sheet data for {ticker}: {e}")
        return None



    balance_sheet_data = {}

    for i in range(len(balance_sheet)):
        publish_date = balance_sheet_publish_date[i]
        year = balance_sheet_fiscal_year[i]
        sheet_data = {
            'Year': year,
            'Accounts Payable': accounts_payable[i],
            'Accounts Receivable': accounts_receivable[i],
            'Accrued Expenses': accrued_expenses[i],
            'Accumulated Depreciation': accumulated_depreciation[i],
            'Additional Paid-in Capital': additional_paid_in_capital[i],
            'Cash and Short-Term Investments': cash_and_short_term_investments[i],
            'Cash Equivalents': cash_equivalents[i],
            'Common Stock': common_stock[i],
            'Current Portion of Long-Term Debt': current_port_of_long_term_debt[i],
            'Balance Sheet End Date': balance_sheet_end_date[i],
            'Long-Term Debt': long_term_debt[i],
            'Notes Payable/Short-Term Debt': notes_payable_short_term_debt[i],
            'Other Current Assets': other_current_assets[i],
            'Other Equity': other_equity[i],
            'Other Liabilities': other_liabilities[i],
            'Other Long-Term Assets': other_long_term_assets[i],
            'PPE Total Gross': ppe_total_gross[i],
            'PPE Total Net': ppe_total_net[i],
            'Prepaid Expenses': prepaid_expenses[i],
            'Retained Earnings': retained_earnings[i],
            'Short-Term Investments': short_term_investments[i],
            'Total Assets': total_assets[i],
            'Total Common Shares Outstanding': total_common_shares_outstanding[i],
            'Total Current Assets': total_current_assets[i],
            'Total Current Liabilities': total_current_liabilities[i],
            'Total Debt': total_debt[i],
            'Total Equity': total_equity[i],
            'Total Inventory': total_inventory[i],
            'Total Liabilities': total_liabilities[i],
            'Total Liabilities & Shareholders Equity': total_liabilities_shareholders_equity[i],
            'Total Long-Term Debt': total_long_term_debt[i],
            'Total Non-Current Assets': total_non_current_assets[i],
            'Total Non-Current Liabilities': total_non_current_liabilities[i],
            'Total Receivables Net': total_receivables_net[i],
            'Total Stockholders Equity': total_stockholders_equity[i],
            'Balance Sheet Type': balance_sheet_type[i]
        }

        if publish_date not in balance_sheet_data:
            balance_sheet_data[publish_date] = []
        
        balance_sheet_data[publish_date].append(sheet_data)


        return balance_sheet_data

async def cash_flow_endpoint(ticker):
    cash_flow = await webull.get_cash_flow(ticker)
    if cash_flow is None:
        return

    capital_expenditures = [i.capital_expenditures if i.capital_expenditures is not None else "N/A" for i in cash_flow]
    cash_from_financing_activities = [i.cash_from_financing_activities if i.cash_from_financing_activities is not None else "N/A" for i in cash_flow]
    cash_from_investing_activities = [i.cash_from_investing_activities if i.cash_from_investing_activities is not None else "N/A" for i in cash_flow]
    cash_from_operating_activities = [i.cash_from_operating_activities if i.cash_from_operating_activities is not None else "N/A" for i in cash_flow]
    changes_in_working_capital = [i.changes_in_working_capital if i.changes_in_working_capital is not None else "N/A" for i in cash_flow]
    deferred_taxes = [i.deferred_taxes if i.deferred_taxes is not None else "N/A" for i in cash_flow]
    depreciation_and_amortization = [i.depreciation_and_amortization if i.depreciation_and_amortization is not None else "N/A" for i in cash_flow]
    cashflow_end_date = [i.end_date if i.end_date is not None else "N/A" for i in cash_flow]
    financing_cashflow_items = [i.financing_cashflow_items if i.financing_cashflow_items is not None else "N/A" for i in cash_flow]
    cashflow_fiscal_period = [i.fiscal_period if i.fiscal_period is not None else "N/A" for i in cash_flow]
    cashflow_fiscal_year = [i.fiscal_year if i.fiscal_year is not None else "N/A" for i in cash_flow]
    foreign_exchange_effects = [i.foreign_exchange_effects if i.foreign_exchange_effects is not None else "N/A" for i in cash_flow]
    issuance_retirement_of_debt_net = [i.issuance_retirement_of_debt_net if i.issuance_retirement_of_debt_net is not None else "N/A" for i in cash_flow]
    issuance_retirement_of_stock_net = [i.issuance_retirement_of_stock_net if i.issuance_retirement_of_stock_net is not None else "N/A" for i in cash_flow]
    net_change_in_cash = [i.net_change_in_cash if i.net_change_in_cash is not None else "N/A" for i in cash_flow]
    net_income = [i.net_income if i.net_income is not None else "N/A" for i in cash_flow]
    non_cash_items = [i.non_cash_items if i.non_cash_items is not None else "N/A" for i in cash_flow]
    other_investing_cashflow_items_total = [i.other_investing_cashflow_items_total if i.other_investing_cashflow_items_total is not None else "N/A" for i in cash_flow]
    cashflow_publish_date = [i.publish_date if i.publish_date is not None else "N/A" for i in cash_flow]
    total_cash_dividends_paid = [i.total_cash_dividends_paid if i.total_cash_dividends_paid is not None else "N/A" for i in cash_flow]
    cashflow_type = [i.type if i.type is not None else "N/A" for i in cash_flow]

    cash_flow_data = {}

    for i in range(len(cash_flow)):
        publish_date = cashflow_publish_date[i]
        year = cashflow_fiscal_year[i]
        statement_data = {
            'Year': year,
            'Capital Expenditures': capital_expenditures[i],
            'Cash from Financing Activities': cash_from_financing_activities[i],
            'Cash from Investing Activities': cash_from_investing_activities[i],
            'Cash from Operating Activities': cash_from_operating_activities[i],
            'Changes in Working Capital': changes_in_working_capital[i],
            'Deferred Taxes': deferred_taxes[i],
            'Depreciation and Amortization': depreciation_and_amortization[i],
            'Cash Flow End Date': cashflow_end_date[i],
            'Financing Cash Flow Items': financing_cashflow_items[i],
            'Foreign Exchange Effects': foreign_exchange_effects[i],
            'Issuance/Retirement of Debt (Net)': issuance_retirement_of_debt_net[i],
            'Issuance/Retirement of Stock (Net)': issuance_retirement_of_stock_net[i],
            'Net Change in Cash': net_change_in_cash[i],
            'Net Income': net_income[i],
            'Non-Cash Items': non_cash_items[i],
            'Other Investing Cash Flow Items (Total)': other_investing_cashflow_items_total[i],
            'Cash Flow Publish Date': cashflow_publish_date[i],
            'Total Cash Dividends Paid': total_cash_dividends_paid[i],
            'Cash Flow Type': cashflow_type[i]
        }

        
        if publish_date not in cash_flow_data:
            cash_flow_data[publish_date] = []
        
        cash_flow_data[publish_date].append(statement_data)

        return cash_flow_data

async def financial_statement_endpoint(ticker):
    financial_statement = await webull.get_financial_statement(ticker)
    if financial_statement is None:
        return None

    cost_of_revenue_total = [i.cost_of_revenue_total if i.cost_of_revenue_total is not None else "N/A" for i in financial_statement]
    depreciation_and_amortization = [i.depreciation_and_amortization if i.depreciation_and_amortization is not None else "N/A" for i in financial_statement]
    diluted_eps_excl_extra_items = [i.diluted_eps_excl_extra_items if i.diluted_eps_excl_extra_items is not None else "N/A" for i in financial_statement]
    diluted_eps_incl_extra_items = [i.diluted_eps_incl_extra_items if i.diluted_eps_incl_extra_items is not None else "N/A" for i in financial_statement]
    diluted_net_income = [i.diluted_net_income if i.diluted_net_income is not None else "N/A" for i in financial_statement]
    diluted_normalized_eps = [i.diluted_normalized_eps if i.diluted_normalized_eps is not None else "N/A" for i in financial_statement]
    diluted_weighted_average_shares = [i.diluted_weighted_average_shares if i.diluted_weighted_average_shares is not None else "N/A" for i in financial_statement]
    earning_after_tax = [i.earning_after_tax if i.earning_after_tax is not None else "N/A" for i in financial_statement]
    earning_before_tax = [i.earning_before_tax if i.earning_before_tax is not None else "N/A" for i in financial_statement]
    end_date = [i.end_date if i.end_date is not None else "N/A" for i in financial_statement]
    fiscal_period = [i.fiscal_period if i.fiscal_period is not None else "N/A" for i in financial_statement]
    fiscal_year = [i.fiscal_year if i.fiscal_year is not None else "N/A" for i in financial_statement]
    gross_profit = [i.gross_profit if i.gross_profit is not None else "N/A" for i in financial_statement]
    income_avaito_com_excl_extra_ord = [i.income_avaito_com_excl_extra_ord if i.income_avaito_com_excl_extra_ord is not None else "N/A" for i in financial_statement]
    income_avaito_com_incl_extra_ord = [i.income_avaito_com_incl_extra_ord if i.income_avaito_com_incl_extra_ord is not None else "N/A" for i in financial_statement]
    income_tax = [i.income_tax if i.income_tax is not None else "N/A" for i in financial_statement]
    inter_expse_inc_net_oper = [i.inter_expse_inc_net_oper if i.inter_expse_inc_net_oper is not None else "N/A" for i in financial_statement]
    inter_inc_expse_net_non_oper = [i.inter_inc_expse_net_non_oper if i.inter_inc_expse_net_non_oper is not None else "N/A" for i in financial_statement]
    net_income = [i.net_income if i.net_income is not None else "N/A" for i in financial_statement]
    net_income_after_tax = [i.net_income_after_tax if i.net_income_after_tax is not None else "N/A" for i in financial_statement]
    net_income_before_extra = [i.net_income_before_extra if i.net_income_before_extra is not None else "N/A" for i in financial_statement]
    net_income_before_tax = [i.net_income_before_tax if i.net_income_before_tax is not None else "N/A" for i in financial_statement]
    operating_expense = [i.operating_expense if i.operating_expense is not None else "N/A" for i in financial_statement]
    operating_income = [i.operating_income if i.operating_income is not None else "N/A" for i in financial_statement]
    operating_profit = [i.operating_profit if i.operating_profit is not None else "N/A" for i in financial_statement]
    publish_date = [i.publish_date if i.publish_date is not None else "N/A" for i in financial_statement]
    revenue = [i.revenue if i.revenue is not None else "N/A" for i in financial_statement]
    sell_gen_admin_expenses = [i.sell_gen_admin_expenses if i.sell_gen_admin_expenses is not None else "N/A" for i in financial_statement]
    total_extraordinary_items = [i.total_extraordinary_items if i.total_extraordinary_items is not None else "N/A" for i in financial_statement]
    total_revenue = [i.total_revenue if i.total_revenue is not None else "N/A" for i in financial_statement]
    type = [i.type if i.type is not None else "N/A" for i in financial_statement]
    unusual_expense_income = [i.unusual_expense_income if i.unusual_expense_income is not None else "N/A" for i in financial_statement]

    financial_statement_data = {}

    for i in range(len(financial_statement)):
        fin_publish_date = publish_date[i]
        year = fiscal_year[i]
        statement_data = {
            'Year': year,
            'Cost of Revenue Total': cost_of_revenue_total[i],
            'Depreciation and Amortization': depreciation_and_amortization[i],
            'Diluted EPS (Excl. Extra Items)': diluted_eps_excl_extra_items[i],
            'Diluted EPS (Incl. Extra Items)': diluted_eps_incl_extra_items[i],
            'Diluted Net Income': diluted_net_income[i],
            'Diluted Normalized EPS': diluted_normalized_eps[i],
            'Diluted Weighted Average Shares': diluted_weighted_average_shares[i],
            'Earnings (After Tax)': earning_after_tax[i],
            'Earnings (Before Tax)': earning_before_tax[i],
            'Gross Profit': gross_profit[i],
            'Income Avail. to Common (Excl. Extraordinary Items)': income_avaito_com_excl_extra_ord[i],
            'Income Avail. to Common (Incl. Extraordinary Items)': income_avaito_com_incl_extra_ord[i],
            'Income Tax': income_tax[i],
            'Interest Expense/Income (Net) - Operating': inter_expse_inc_net_oper[i],
            'Interest Income/Expense (Net) - Non-operating': inter_inc_expse_net_non_oper[i],
            'Net Income': net_income[i],
            'Net Income (After Tax)': net_income_after_tax[i],
            'Net Income (Before Extraordinary Items)': net_income_before_extra[i],
            'Net Income (Before Tax)': net_income_before_tax[i],
            'Operating Expense': operating_expense[i],
            'Operating Income': operating_income[i],
            'Operating Profit': operating_profit[i],
            'Revenue': revenue[i],
            'Selling, General, and Admin. Expenses': sell_gen_admin_expenses[i],
            'Total Extraordinary Items': total_extraordinary_items[i],
            'Total Revenue': total_revenue[i],
            'Type': type[i],
            'Unusual Expense/Income': unusual_expense_income[i]
        }
        if fin_publish_date not in financial_statement_data:
            financial_statement_data[fin_publish_date] = []
        
        financial_statement_data[fin_publish_date].append(statement_data)

        return financial_statement_data
async def volume_analysis_endpoint(ticker):
    vol_analysis_data = await webull.get_webull_vol_analysis_data(ticker)

    buyvol = float(vol_analysis_data.buyVolume) if vol_analysis_data.buyVolume is not None else None
    sellvol = float(vol_analysis_data.sellVolume) if vol_analysis_data.sellVolume is not None else None
    nvol = float(vol_analysis_data.nVolume) if vol_analysis_data.nVolume is not None else None
    tvol = float(vol_analysis_data.totalVolume) if vol_analysis_data.totalVolume is not None else None
    average_traded_price = vol_analysis_data.avePrice
    vol_analysis_results = { 
        'Buy Volume': f"{buyvol:,}",
        'Neutral Volume': f"{nvol:,}",
        'Sell Volume': f"{sellvol:,}",
        'Total Volume': f"{tvol:,}",
        'Average Traded Price': f"{average_traded_price}"
    }



    return vol_analysis_results
async def get_top_gainers_data():
    types = ['1d','preMarket','afterMarket','5m','1m', '3m', '52w']
    


    data_dict = {}

    for i in types:
        r = requests.get(f"https://quotes-gw.webullfintech.com/api/bgw/market/topGainers?regionId=6&rankType={i}&pageIndex=1&pageSize=350").json()
        if 'data' in r:
            data = r['data']
            tickers = [d['ticker'] for d in data]

            ticker_data = []
            for ticker in tickers:
                exchangeId = ticker.get('exchangeId')
                type_val = ticker.get('type')
                secType = ticker.get('secType')
                regionId = ticker.get('regionId')
                currencyId = ticker.get('currencyId')
                currencyCode = ticker.get('currencyCode')
                name = ticker.get('name')
                symbol = ticker.get('symbol')
                disSymbol = ticker.get('disSymbol')
                disExchangeCode = ticker.get('disExchangeCode')
                exchangeCode = ticker.get('exchangeCode')
                listStatus = ticker.get('listStatus')
                template = ticker.get('template')
                derivativeSupport = ticker.get('derivativeSupport')
                isPTP = ticker.get('isPTP')
                tradeTime = ticker.get('tradeTime')
                faTradeTime = ticker.get('faTradeTime')
                status = ticker.get('status')
                close = ticker.get('close')
                change = ticker.get('change')
                changeRatio = ticker.get('changeRatio')
                marketValue = ticker.get('marketValue')
                volume = ticker.get('volume')
                turnoverRate = ticker.get('turnoverRate')
                regionName = ticker.get('regionName')
                regionIsoCode = ticker.get('regionIsoCode')
                peTtm = ticker.get('peTtm')
                preClose = ticker.get('preClose')
                fiftyTwoWkHigh = ticker.get('fiftyTwoWkHigh')
                fiftyTwoWkLow = ticker.get('fiftyTwoWkLow')
                open_val = ticker.get('open')
                high = ticker.get('high')
                low = ticker.get('low')
                
                ticker_dict = {
                    'Exchange ID': exchangeId,
                    'Type': type_val,
                    'Security Type': secType,
                    'Region ID': regionId,
                    'Currency ID': currencyId,
                    'Currency Code': currencyCode,
                    'Name': name,
                    'Symbol': symbol,
                    'Display Symbol': disSymbol,
                    'Display Exchange Code': disExchangeCode,
                    'Exchange Code': exchangeCode,
                    'List Status': listStatus,
                    'Template': template,
                    'Derivative Support': derivativeSupport,
                    'Is PTP': isPTP,
                    'Trade Time': tradeTime,
                    'FA Trade Time': faTradeTime,
                    'Status': status,
                    'Close Price': close,
                    'Change': change,
                    'Change Ratio': changeRatio,
                    'Market Value': marketValue,
                    'Volume': volume,
                    'Turnover Rate': turnoverRate,
                    'Region Name': regionName,
                    'Region ISO Code': regionIsoCode,
                    'PE Ratio TTM': peTtm,
                    'Previous Close': preClose,
                    '52-Week High': fiftyTwoWkHigh,
                    '52-Week Low': fiftyTwoWkLow,
                    'Open Price': open_val,
                    'High Price': high,
                    'Low Price': low
                }

                ticker_data.append(ticker_dict)

            data_dict[i] = ticker_data


            return data_dict
        

async def process_data():
    webull = Webull()
    await webull.fetch_data('AAPL')
    return webull.__dict__