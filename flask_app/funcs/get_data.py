
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK

webull = AsyncWebullSDK()

async def get_webull_data(ticker):
    # Initialize your variables with default values

    # Try to get your data
    try:
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
    except Exception as e:
        print(f"Failed to get stock data for {ticker}: {e}")


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


    short_interest = await webull.get_short_interest(ticker)
    if short_interest is None:
        return

    short_int = f"{float(short_interest.short_int[0]):,}" if short_interest.short_int[0] is not None else "N/A"
    avg_vol = f"{float(short_interest.avg_volume[0]):,}" if short_interest.avg_volume[0] is not None else "N/A"
    days_to_cover = short_interest.days_to_cover[0] if short_interest.days_to_cover[0] is not None else "N/A"
    settlement = short_interest.settlement[0] if short_interest.settlement[0] is not None else "N/A"

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

    costDistribution = await webull.cost_distribution(ticker)
    if costDistribution is None:
        return None

    avgCost = [i.avgCost if i.avgCost is not None else "N/A" for i in costDistribution]
    sharesInProfit70End = [i.chip70End if i.chip70End is not None else "N/A" for i in costDistribution]
    sharesInProfit70Ratio = [i.chip70Ratio if i.chip70Ratio is not None else "N/A" for i in costDistribution]
    sharesInProfit70Start = [i.chip70Start if i.chip70Start is not None else "N/A" for i in costDistribution]
    sharesInProfit90End = [i.chip90End if i.chip90End is not None else "N/A" for i in costDistribution]
    sharesInProfit90Ratio = [i.chip90Ratio if i.chip90Ratio is not None else "N/A" for i in costDistribution]
    sharesInProfit90Start = [i.chip90Start if i.chip90Start is not None else "N/A" for i in costDistribution]
    Close = [i.close if i.close is not None else "N/A" for i in costDistribution]
    traders_profiting = [i.closeProfitRatio if i.closeProfitRatio is not None else "N/A" for i in costDistribution]
    distributions = [i.distributions if i.distributions is not None else "N/A" for i in costDistribution]
    totalShares = [i.totalShares if i.totalShares is not None else "N/A" for i in costDistribution]

    if traders_profiting is not None:
        traders_profiting = traders_profiting[0]
    else:
        traders_profiting = None


    capitalFlow = await webull.capital_flow(ticker)
    if capitalFlow is None:
        return None

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


    vol_analysis_data = await webull.get_webull_vol_analysis_data(ticker)

    buyvol = float(vol_analysis_data.buyVolume) if vol_analysis_data.buyVolume is not None else None
    sellvol = float(vol_analysis_data.sellVolume) if vol_analysis_data.sellVolume is not None else None
    nvol = float(vol_analysis_data.nVolume) if vol_analysis_data.nVolume is not None else None
    tvol = float(vol_analysis_data.totalVolume) if vol_analysis_data.totalVolume is not None else None

    vol_analysis_results = { 
        'Buy Volume': f"{buyvol:,}",
        'Neutral Volume': f"{nvol:,}",
        'Sell Volume': f"{sellvol:,}",


    }





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

    try:
        financial_statement_result = {
            'Cost of Revenue (Total)': cost_of_revenue_total[0] if cost_of_revenue_total else "N/A",
            'Depreciation and Amortization': depreciation_and_amortization[0] if depreciation_and_amortization else "N/A",
            'Diluted EPS Excluding Extraordinary Items': diluted_eps_excl_extra_items[0] if diluted_eps_excl_extra_items else "N/A",
            'Diluted EPS Including Extraordinary Items': diluted_eps_incl_extra_items[0] if diluted_eps_incl_extra_items else "N/A",
            'Diluted Net Income': diluted_net_income[0] if diluted_net_income else "N/A",
            'Diluted Normalized EPS': diluted_normalized_eps[0] if diluted_normalized_eps else "N/A",
            'Diluted Weighted Average Shares': diluted_weighted_average_shares[0] if diluted_weighted_average_shares else "N/A",
            'Earnings After Tax': earning_after_tax[0] if earning_after_tax else "N/A",
            'Earnings Before Tax': earning_before_tax[0] if earning_before_tax else "N/A",
            'End Date': end_date[0] if end_date else "N/A",
            'Financial Statement Fiscal Period': fiscal_period[0] if fiscal_period else "N/A",
            'Financial Statement Fiscal Year': fiscal_year[0] if fiscal_year else "N/A",
            'Gross Profit': gross_profit[0] if gross_profit else "N/A",
            'Income Available to Common Excluding Extraordinary Items': income_avaito_com_excl_extra_ord[0] if income_avaito_com_excl_extra_ord else "N/A",
            'Income Available to Common Including Extraordinary Items': income_avaito_com_incl_extra_ord[0] if income_avaito_com_incl_extra_ord else "N/A",
            'Income Tax': income_tax[0] if income_tax else "N/A",
            'Interest Expense (Income), Net - Operating': inter_expse_inc_net_oper[0] if inter_expse_inc_net_oper else "N/A",
            'Interest Income (Expense), Net - Non-Operating': inter_inc_expse_net_non_oper[0] if inter_inc_expse_net_non_oper else "N/A",
            'Net Income': net_income[0] if net_income else "N/A",
            'Net Income After Tax': net_income_after_tax[0] if net_income_after_tax else "N/A",
            'Net Income Before Extraordinary Items': net_income_before_extra[0] if net_income_before_extra else "N/A",
            'Net Income Before Tax': net_income_before_tax[0] if net_income_before_tax else "N/A",
            'Operating Expense': operating_expense[0] if operating_expense else "N/A",
            'Operating Income': operating_income[0] if operating_income else "N/A",
            'Operating Profit': operating_profit[0] if operating_profit else "N/A",
            'Financial Statement Publish Date': publish_date[0] if publish_date else "N/A",
            'Revenue': revenue[0] if revenue else "N/A",
            'Selling, General, and Administrative Expenses': sell_gen_admin_expenses[0] if sell_gen_admin_expenses else "N/A",
            'Total Extraordinary Items': total_extraordinary_items[0] if total_extraordinary_items else "N/A",
            'Total Revenue': total_revenue[0] if total_revenue else "N/A",
            'Financial Statement Type': type[0] if type else "N/A",
        }

        cashflow_result = {
            'Capital Expenditures': capital_expenditures[0] if capital_expenditures else "N/A",
            'Cash from Financing Activities': cash_from_financing_activities[0] if cash_from_financing_activities else "N/A",
            'Cash from Investing Activities': cash_from_investing_activities[0] if cash_from_investing_activities else "N/A",
            'Cash from Operating Activities': cash_from_operating_activities[0] if cash_from_operating_activities else "N/A",
            'Changes in Working Capital': changes_in_working_capital[0] if changes_in_working_capital else "N/A",
            'Deferred Taxes': deferred_taxes[0] if deferred_taxes else "N/A",
            'Depreciation and Amortization': depreciation_and_amortization[0] if depreciation_and_amortization else "N/A",
            'Cash Flow End Date': cashflow_end_date[0] if cashflow_end_date else "N/A",
            'Financing Cash Flow Items': financing_cashflow_items[0] if financing_cashflow_items else "N/A",
            'Cash Flow Fiscal Period': cashflow_fiscal_period[0] if cashflow_fiscal_period else "N/A",
            'Cash Flow Fiscal Year': cashflow_fiscal_year[0] if cashflow_fiscal_year else "N/A",
            'Foreign Exchange Effects': foreign_exchange_effects[0] if foreign_exchange_effects else "N/A",
            'Issuance/Retirement of Debt, Net': issuance_retirement_of_debt_net[0] if issuance_retirement_of_debt_net else "N/A",
            'Issuance/Retirement of Stock, Net': issuance_retirement_of_stock_net[0] if issuance_retirement_of_stock_net else "N/A",
            'Net Change in Cash': net_change_in_cash[0] if net_change_in_cash else "N/A",
            'Net Income': net_income[0] if net_income else "N/A",
            'Non-Cash Items': non_cash_items[0] if non_cash_items else "N/A",
            'Other Investing Cash Flow Items, Total': other_investing_cashflow_items_total[0] if other_investing_cashflow_items_total else "N/A",
            'Cash Flow Publish Date': cashflow_publish_date[0] if cashflow_publish_date else "N/A",
            'Total Cash Dividends Paid': total_cash_dividends_paid[0] if total_cash_dividends_paid else "N/A",
            'Cash Flow Type': cashflow_type[0] if cashflow_type else "N/A",
        }

        balance_sheet_result = {
            'Accounts Payable': accounts_payable[0] if accounts_payable else "N/A",
            'Accounts Receivable': accounts_receivable[0] if accounts_receivable else "N/A",
            'Accrued Expenses': accrued_expenses[0] if accrued_expenses else "N/A",
            'Accumulated Depreciation': accumulated_depreciation[0] if accumulated_depreciation else "N/A",
            'Additional Paid-In Capital': additional_paid_in_capital[0] if additional_paid_in_capital else "N/A",
            'Cash and Short-Term Investments': cash_and_short_term_investments[0] if cash_and_short_term_investments else "N/A",
            'Cash Equivalents': cash_equivalents[0] if cash_equivalents else "N/A",
            'Common Stock': common_stock[0] if common_stock else "N/A",
            'Current Portion of Long-Term Debt': current_port_of_long_term_debt[0] if current_port_of_long_term_debt else "N/A",
            'Balance Sheet End Date': balance_sheet_end_date[0] if balance_sheet_end_date else "N/A",
            'Balance Sheet Fiscal Period': balance_sheet_fiscal_period[0] if balance_sheet_fiscal_period else "N/A",
            'Balance Sheet Fiscal Year': balance_sheet_fiscal_year[0] if balance_sheet_fiscal_year else "N/A",
            'Long-Term Debt': long_term_debt[0] if long_term_debt else "N/A",
            'Notes Payable/Short-Term Debt': notes_payable_short_term_debt[0] if notes_payable_short_term_debt else "N/A",
            'Other Current Assets': other_current_assets[0] if other_current_assets else "N/A",
            'Other Equity': other_equity[0] if other_equity else "N/A",
            'Other Liabilities': other_liabilities[0] if other_liabilities else "N/A",
            'Other Long-Term Assets': other_long_term_assets[0] if other_long_term_assets else "N/A",
            'PPE Total Gross': ppe_total_gross[0] if ppe_total_gross else "N/A",
            'PPE Total Net': ppe_total_net[0] if ppe_total_net else "N/A",
            'Prepaid Expenses': prepaid_expenses[0] if prepaid_expenses else "N/A",
            'Balance Sheet Publish Date': balance_sheet_publish_date[0] if balance_sheet_publish_date else "N/A",
            'Retained Earnings': retained_earnings[0] if retained_earnings else "N/A",
            'Short-Term Investments': short_term_investments[0] if short_term_investments else "N/A",
            'Total Assets': total_assets[0] if total_assets else "N/A",
            'Total Common Shares Outstanding': total_common_shares_outstanding[0] if total_common_shares_outstanding else "N/A",
            'Total Current Assets': total_current_assets[0] if total_current_assets else "N/A",
            'Total Current Liabilities': total_current_liabilities[0] if total_current_liabilities else "N/A",
            'Total Debt': total_debt[0] if total_debt else "N/A",
            'Total Equity': total_equity[0] if total_equity else "N/A",
            'Total Inventory': total_inventory[0] if total_inventory else "N/A",
            'Total Liabilities': total_liabilities[0] if total_liabilities else "N/A",
            'Total Liabilities and Shareholders Equity': total_liabilities_shareholders_equity[0] if total_liabilities_shareholders_equity else "N/A",
            'Total Long-Term Debt': total_long_term_debt[0] if total_long_term_debt else "N/A",
            'Total Non-Current Assets': total_non_current_assets[0] if total_non_current_assets else "N/A",
            'Total Non-Current Liabilities': total_non_current_liabilities[0] if total_non_current_liabilities else "N/A",
            'Total Receivables Net': total_receivables_net[0] if total_receivables_net else "N/A",
            'Total Stockholders Equity': total_stockholders_equity[0] if total_stockholders_equity else "N/A",
            'Balance Sheet Type': balance_sheet_type[0] if balance_sheet_type else "N/A",
        }

        capital_flow_result = {
            'Large Inflow': largeIn if largeIn else "N/A",
            'Large Outflow': largeOut if largeOut else "N/A",
            'Large Net Flow': largeNet if largeNet else "N/A",
            'New Large Inflow': newLargeIn if newLargeIn else "N/A",
            'New Large Outflow': newLargeOut if newLargeOut else "N/A",
            'New Large Net Flow': newLargeNet if newLargeNet else "N/A",
            'New Large Inflow Ratio': newLargeInRatio if newLargeInRatio else "N/A",
            'New Large Outflow Ratio': newLargeOutRatio if newLargeOutRatio else "N/A",
            'Major Inflow': majorIn if majorIn else "N/A",
            'Major Outflow': majorOut if majorOut else "N/A",
            'Major Net Flow': majorNet if majorNet else "N/A",
            'Major Inflow Ratio': majorInRatio if majorInRatio else "N/A",
            'Major Outflow Ratio': majorOutRatio if majorOutRatio else "N/A",
            'Medium Inflow': mediumIn if mediumIn else "N/A",
            'Medium Outflow': mediumOut if mediumOut else "N/A",
            'Medium Net Flow': mediumNet if mediumNet else "N/A",
            'Medium Inflow Ratio': mediumInRatio if mediumInRatio else "N/A",
            'Medium Outflow Ratio': mediumOutRatio if mediumOutRatio else "N/A",
            'Small Inflow': smallIn if smallIn else "N/A",
            'Small Outflow': smallOut if smallOut else "N/A",
            'Small Net Flow': smallNet if smallNet else "N/A",
            'Small Inflow Ratio': smallInRatio if smallInRatio else "N/A",
            'Small Outflow Ratio': smallOutRatio if smallOutRatio else "N/A",
            'Retail Inflow': retailIn if retailIn else "N/A",
            'Retail Outflow': retailOut if retailOut else "N/A",
            'Retail Inflow Ratio': retailInRatio if retailInRatio else "N/A",
            'Retail Outflow Ratio': retailOutRatio if retailOutRatio else "N/A",
        }

        cost_distribution_result = {
            'Average Cost': avgCost[0] if avgCost else "N/A",
            'Close': Close[0] if Close else "N/A",
            'Shares Profiting 70% End': sharesInProfit70End[0] if sharesInProfit70End else "N/A",
            'Shares Profiting 70% Ratio': sharesInProfit70Ratio[0] if sharesInProfit70Ratio else "N/A",
            'Shares Profiting 70% Start': sharesInProfit70Start[0] if sharesInProfit70Start else "N/A",
            'Shares Profiting 90% End': sharesInProfit90End[0] if sharesInProfit90End else "N/A",
            'Shares Profiting 90% Ratio': sharesInProfit90Ratio[0] if sharesInProfit90Ratio else "N/A",
            'Shares Profiting 90% End': sharesInProfit90Start[0] if sharesInProfit90Start else "N/A",
            'Percent of Traders in Profit': traders_profiting[0] if traders_profiting else "N/A",
            'Total Shares': total_shares[0] if total_shares else "N/A",
        }

        institutional_ownership_result = {
            'Decreased Numer of Shares': decreaseChange if decreaseChange else "N/A",
            'Decreased Numer of Institutions': decreasedShares if decreasedShares else "N/A",
            'Increased Number of Shares': increaseChange if increaseChange else "N/A",
            'Increased Number of Institutions': increasedShares if increasedShares else "N/A",
            'Shares from New Positions': newChange if newChange else "N/A",
            'Institutions with New Positions': newShares if newShares else "N/A",
            'Net Shares Changed': net_shares_changed if net_shares_changed else "N/A",
            'Net Institutions Changed': net_institution_change if net_institution_change else "N/A",
            'Total Held Shares': totalHeldShares if totalHeldShares else "N/A",
            'Total Held Shares Changed': totalHeldSharesChange if totalHeldSharesChange else "N/A",
            'Total Number of Institutions': totalNumberOfInstitutions if totalNumberOfInstitutions else "N/A",
            f'Total Ownership of {ticker}': totalOwnershipRatioOfFloat if totalOwnershipRatioOfFloat else "N/A",
            f'Total Ownership of {ticker} Raio Change': totalOwnershipRatioOfFloatChange if totalOwnershipRatioOfFloatChange else "N/A",
        }



        stock_data_result = {
            'Symbol': web_symb if web_symb else "N/A",
            'High Price': web_stock_high if web_stock_high else "N/A",
            'Low Price': web_stock_low if web_stock_low else "N/A",
            'Open Price': web_stock_open if web_stock_open else "N/A",
            'Volume': f"{web_stock_vol:,}" if web_stock_vol else "N/A",
            'Last Price': web_stock_close if web_stock_close else "N/A",
            'Company Name': web_name if web_name else "N/A",
            'Average 10 Day Volume': avg_10d_vol if avg_10d_vol else "N/A",
            'Average 3 Month Volume': avg_vol3m if avg_vol3m else "N/A",
            'Estimated Earnings': estimated_earnings if estimated_earnings else "N/A",
            '52week High': fifty_high if fifty_high else "N/A",
            '52week Low': fifty_low if fifty_low else "N/A",
            'Last Earnings': last_earnings if last_earnings else "N/A",
            'Outstanding Shares': outstanding_shares if outstanding_shares else "N/A",
            'Total Shares': total_shares if total_shares else "N/A",
            'Change Percent': web_change_ratio if web_change_ratio else "N/A",
            'Exchange': web_exchange if web_exchange else "N/A",
            'Vibration Ratio': web_vibrate_ratio if web_vibrate_ratio else "N/A",
        }

        analyst_result = {
            'Buy Rating Count': buy if buy else "N/A",
            'Strong Buy Rating Count': strongbuy if strongbuy else "N/A",
            'Hold Rating Count': hold if hold else "N/A",
            'Under Perform Rating Count:': underperform if underperform else "N/A",
            'Sell Rating Count': sell if sell else "N/A",
            'Rating Suggestion': suggestion if suggestion else "N/A",
            'Number of Analysts': rating_totals if rating_totals else "N/A",
        }

        short_interest_result = {
            'Short Interest': short_int if short_int else "N/A",
            'Days to Cover': short_interest.days_to_cover[0] if short_interest and short_interest.days_to_cover else "N/A",
            'Settlement Date': short_interest.settlement[0] if short_interest and short_interest.settlement else "N/A",
            'Average Volume': avg_vol if avg_vol else "N/A",
        }

        return (stock_data_result, vol_analysis_results,financial_statement_result, cashflow_result, balance_sheet_result, 
                capital_flow_result, cost_distribution_result, institutional_ownership_result, analyst_result,
                short_interest_result, news_result)
    except Exception as e:
        print(f"An error occurred while retrieving Webull data: {str(e)}")
        return None