import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
import pandas as pd
import csv

from sdks.webull_sdk.webull_sdk import AsyncWebullSDK

sdk = AsyncWebullSDK()

async def balance_sheet(ticker="AAPL"):
    


    #financials - balance sheet
    balance_sheet = await sdk.get_balancesheet(ticker)
    accounts_payable = balance_sheet[0].accountsPayable 
    accounts_payable = balance_sheet[0].accountsPayable
    accounts_receivable_trade_net = balance_sheet[0].accountsReceTradeNet
    accrued_expenses = balance_sheet[0].accruedExpenses
    accumulated_depreciation_total = balance_sheet[0].accumulatedDepreciationTotal
    additional_paid_in_capital = balance_sheet[0].additionalPaidInCapital
    cash_and_short_term_invest = balance_sheet[0].cashAndShortTermInvest
    cash_equivalents = balance_sheet[0].cashEquivalents
    common_stock = balance_sheet[0].commonStock
    current_port_of_LT_debt_capital_leases = balance_sheet[0].currentPortofLTDebtCapitalLeases
    end_date = balance_sheet[0].endDate
    fiscal_period = balance_sheet[0].fiscalPeriod
    fiscal_year = balance_sheet[0].fiscalYear
    long_term_debt = balance_sheet[0].longTermDebt
    notes_payable_short_term_debt = balance_sheet[0].notesPayableShortTermDebt
    other_current_assets_total = balance_sheet[0].otherCurrentAssetsTotal
    other_long_term_assets_total = balance_sheet[0].otherLongTermAssetsTotal
    other_equity_total = balance_sheet[0].otherEquityTotal
    other_liabilities_total = balance_sheet[0].otherLiabilitiesTotal
    ppe_total_gross = balance_sheet[0].ppeTotalGross
    ppe_total_net = balance_sheet[0].ppeTotalNet
    prepaid_expenses = balance_sheet[0].prepaidExpenses
    publish_date = balance_sheet[0].publishDate
    quote_id = balance_sheet[0].quoteId
    retained_earnings = balance_sheet[0].retainedEarnings
    short_term_investments = balance_sheet[0].shortTermInvestments
    total_assets = balance_sheet[0].totalAssets
    total_common_shares_outstanding = balance_sheet[0].totalCommonSharesOutstanding
    total_current_assets = balance_sheet[0].totalCurrentAssets
    total_current_liabilities = balance_sheet[0].totalCurrentLiabilities
    total_debt = balance_sheet[0].totalDebt
    total_equity = balance_sheet[0].totalEquity
    total_inventory = balance_sheet[0].totalInventory
    total_liabilities = balance_sheet[0].totalLiabilities
    total_liabilities_shareholders_equity = balance_sheet[0].totalLiabilitiesShareholdersEquity
    total_long_term_debt = balance_sheet[0].totalLongTermDebt
    total_non_current_assets = balance_sheet[0].totalNonCurrentAssets
    total_non_current_liabilities = balance_sheet[0].totalNonCurrentLiabilities
    total_receivables_net = balance_sheet[0].totalReceivablesNet
    total_stockholders_equity = balance_sheet[0].totalStockhodersEquity

    #output
    print("accountsPayable:", accounts_payable)
    print("accountsReceTradeNet:", accounts_receivable_trade_net)
    print("accruedExpenses:", accrued_expenses)
    print("accumulatedDepreciationTotal:", accumulated_depreciation_total)
    print("additionalPaidInCapital:", additional_paid_in_capital)
    print("cashAndShortTermInvest:", cash_and_short_term_invest)
    print("cashEquivalents:", cash_equivalents)
    print("commonStock:", common_stock)
    print("currentPortofLTDebtCapitalLeases:", current_port_of_LT_debt_capital_leases)
    print("endDate:", end_date)
    print("fiscalPeriod:", fiscal_period)
    print("fiscalYear:", fiscal_year)
    print("longTermDebt:", long_term_debt)
    print("notesPayableShortTermDebt:", notes_payable_short_term_debt)
    print("otherCurrentAssetsTotal:", other_current_assets_total)
    print("otherLongTermAssetsTotal:", other_long_term_assets_total)
    print("otherEquityTotal:", other_equity_total)
    print("otherLiabilitiesTotal:", other_liabilities_total)
    print("ppeTotalGross:", ppe_total_gross)
    print("ppeTotalNet:", ppe_total_net)
    print("prepaidExpenses:", prepaid_expenses)
    print("publishDate:", publish_date)
    print("quoteId:", quote_id)
    print("retainedEarnings:", retained_earnings)
    print("shortTermInvestments:", short_term_investments)
    print("totalAssets:", total_assets)
    print("totalCommonSharesOutstanding:", total_common_shares_outstanding)
    print("totalCurrentAssets:", total_current_assets)
    print("totalCurrentLiabilities:", total_current_liabilities)
    print("totalDebt:", total_debt)
    print("totalEquity:", total_equity)
    print("totalInventory:", total_inventory)
    print("totalLiabilities:", total_liabilities)
    print("totalLiabilitiesShareholdersEquity:", total_liabilities_shareholders_equity)
    print("totalLongTermDebt:", total_long_term_debt)
    print("totalNonCurrentAssets:", total_non_current_assets)
    print("totalNonCurrentLiabilities:", total_non_current_liabilities)
    print("totalReceivablesNet:", total_receivables_net)
    print("totalStockhodersEquity:", total_stockholders_equity)

    data = []

    # Iterate over the balance_sheet objects and extract attribute values
    for sheet in balance_sheet:
        data.append(sheet.to_dict())

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data)

    # Define the file path
    filename = f'files/financials/balance_sheet/{ticker}_balance_sheet.csv'

    # Save the DataFrame to a CSV file
    df.to_csv(filename, index=False)

asyncio.run(balance_sheet(ticker="AAPL"))