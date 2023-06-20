import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

import pandas as pd


from sdks.webull_sdk.webull_sdk import AsyncWebullSDK


sdk = AsyncWebullSDK()


async def financial_statement(ticker="META"):



    #financials - cash statement
    fin_statement=await sdk.get_financial_statement(ticker)
    statement = fin_statement[0]
    cost_of_revenue_total = statement.cost_of_revenue_total
    depreciation_and_amortization = statement.depreciation_and_amortization
    diluted_eps_excl_extra_items = statement.diluted_eps_excl_extra_items
    diluted_eps_incl_extra_items = statement.diluted_eps_incl_extra_items
    diluted_net_income = statement.diluted_net_income
    diluted_normalized_eps = statement.diluted_normalized_eps
    diluted_weighted_average_shares = statement.diluted_weighted_average_shares
    earning_after_tax = statement.earning_after_tax
    earning_before_tax = statement.earning_before_tax
    fiscal_period = statement.fiscal_period
    fiscal_year = statement.fiscal_year
    income_avaito_com_excl_extra_ord = statement.income_avaito_com_excl_extra_ord
    income_avaito_com_incl_extra_ord = statement.income_avaito_com_incl_extra_ord
    income_tax = statement.income_tax
    inter_expse_inc_net_oper = statement.inter_expse_inc_net_oper
    inter_inc_expse_net_non_oper = statement.inter_inc_expse_net_non_oper
    net_income = statement.net_income
    net_income_after_tax = statement.net_income_after_tax
    net_income_before_extra = statement.net_income_before_extra
    net_income_before_tax = statement.net_income_before_tax
    operating_expense = statement.operating_expense
    operating_income = statement.operating_income
    operating_profit = statement.operating_profit
    publish_date = statement.publish_date
    revenue = statement.revenue
    sell_gen_admin_expenses = statement.sell_gen_admin_expenses
    total_extraordinary_items = statement.total_extraordinary_items
    total_revenue = statement.total_revenue
    type = statement.type

    print("cost_of_revenue_total:", cost_of_revenue_total)
    print("depreciation_and_amortization:", depreciation_and_amortization)
    print("diluted_eps_excl_extra_items:", diluted_eps_excl_extra_items)
    print("diluted_eps_incl_extra_items:", diluted_eps_incl_extra_items)
    print("diluted_net_income:", diluted_net_income)
    print("diluted_normalized_eps:", diluted_normalized_eps)
    print("diluted_weighted_average_shares:", diluted_weighted_average_shares)
    print("earning_after_tax:", earning_after_tax)
    print("earning_before_tax:", earning_before_tax)
    print("fiscal_period:", fiscal_period)
    print("fiscal_year:", fiscal_year)
    print("income_avaito_com_excl_extra_ord:", income_avaito_com_excl_extra_ord)
    print("income_avaito_com_incl_extra_ord:", income_avaito_com_incl_extra_ord)
    print("income_tax:", income_tax)
    print("inter_expse_inc_net_oper:", inter_expse_inc_net_oper)
    print("inter_inc_expse_net_non_oper:", inter_inc_expse_net_non_oper)
    print("net_income:", net_income)
    print("net_income_after_tax:", net_income_after_tax)
    print("net_income_before_extra:", net_income_before_extra)
    print("net_income_before_tax:", net_income_before_tax)
    print("operating_expense:", operating_expense)
    print("operating_income:", operating_income)
    print("operating_profit:", operating_profit)
    print("publish_date:", publish_date)
    print("revenue:", revenue)
    print("sell_gen_admin_expenses:", sell_gen_admin_expenses)
    print("total_extraordinary_items:", total_extraordinary_items)
    print("total_revenue:", total_revenue)
    print("type:", type)

    # Create a list of dictionaries to store the attribute values
    data = []

    # Iterate over the balance_sheet objects and extract attribute values
    for sheet in fin_statement:
        data.append(sheet.to_dict())

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data)

    # Define the file path
    filename = f'files/financials/financial_statement/{ticker}financial_statement.csv'

    # Save the DataFrame to a CSV file
    df.to_csv(filename, index=False)


asyncio.run(financial_statement(ticker="META"))