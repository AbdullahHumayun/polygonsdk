import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
import pandas as pd
import csv

from sdks.webull_sdk.webull_sdk import AsyncWebullSDK

sdk = AsyncWebullSDK()

async def main():
    
    ticker = "AMD"

    #cash flow - company financials#
    cash_flow = await sdk.get_cash_flow(ticker)
    cashflow = cash_flow[0]
    capital_expenditures = cashflow.capital_expenditures
    cash_from_financing_activities = cashflow.cash_from_financing_activities
    cash_from_investing_activities = cashflow.cash_from_investing_activities
    cash_from_operating_activities = cashflow.cash_from_operating_activities
    changes_in_working_capital = cashflow.changes_in_working_capital
    deferred_taxes = cashflow.deferred_taxes
    depreciation_and_amortization = cashflow.depreciation_and_amortization
    end_date = cashflow.end_date
    financing_cashflow_items = cashflow.financing_cashflow_items
    foreign_exchange_effects = cashflow.foreign_exchange_effects
    issuance_retirement_of_debt_net = cashflow.issuance_retirement_of_debt_net
    issuance_retirement_of_stock_net = cashflow.issuance_retirement_of_stock_net
    net_change_in_cash = cashflow.net_change_in_cash
    net_income = cashflow.net_income
    non_cash_items = cashflow.non_cash_items
    other_investing_cashflow_items_total = cashflow.other_investing_cashflow_items_total
    publish_date = cashflow.publish_date
    total_cash_dividends_paid = cashflow.total_cash_dividends_paid
    type = cashflow.type

    print("capital_expenditures:", capital_expenditures)
    print("cash_from_financing_activities:", cash_from_financing_activities)
    print("cash_from_investing_activities:", cash_from_investing_activities)
    print("cash_from_operating_activities:", cash_from_operating_activities)
    print("changes_in_working_capital:", changes_in_working_capital)
    print("deferred_taxes:", deferred_taxes)
    print("depreciation_and_amortization:", depreciation_and_amortization)
    print("end_date:", end_date)
    print("financing_cashflow_items:", financing_cashflow_items)
    print("foreign_exchange_effects:", foreign_exchange_effects)
    print("issuance_retirement_of_debt_net:", issuance_retirement_of_debt_net)
    print("issuance_retirement_of_stock_net:", issuance_retirement_of_stock_net)
    print("net_change_in_cash:", net_change_in_cash)
    print("net_income:", net_income)
    print("non_cash_items:", non_cash_items)
    print("other_investing_cashflow_items_total:", other_investing_cashflow_items_total)
    print("publish_date:", publish_date)
    print("total_cash_dividends_paid:", total_cash_dividends_paid)
    print("type:", type)


    # Create a list of dictionaries to store the attribute values
    data = []

    # Iterate over the balance_sheet objects and extract attribute values
    for sheet in cash_flow:
        data.append(sheet.to_dict())

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data)

    # Define the file path
    filename = f'files/financials/cash_flow/{ticker}_cash_flow.csv'

    # Save the DataFrame to a CSV file
    df.to_csv(filename, index=False)




asyncio.run(main())