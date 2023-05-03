class FinancialStatement:
    def __init__(self, data):
        self.quote_id = data.get("quoteId", None)
        self.type = data.get("type", None)
        self.fiscal_year = data.get("fiscalYear", None)
        self.fiscal_period = data.get("fiscalPeriod", None)
        self.end_date = data.get("endDate", None)
        self.currency_id = data.get("currencyId", None)
        self.publish_date = data.get("publishDate", None)
        self.total_revenue = data.get("totalRevenue", None)
        self.revenue = data.get("revenue", None)
        self.cost_of_revenue_total = data.get("costofRevenueTotal", None)
        self.gross_profit = data.get("grossProfit", None)
        self.operating_expense = data.get("operatingExpense", None)
        self.sell_gen_admin_expenses = data.get("sellGenAdminExpenses", None)
        self.depreciation_and_amortization = data.get("depreciationAndAmortization", None)
        self.inter_expse_inc_net_oper = data.get("interExpseIncNetOper", None)
        self.unusual_expense_income = data.get("unusualExpenseIncome", None)
        self.operating_income = data.get("operatingIncome", None)
        self.inter_inc_expse_net_non_oper = data.get("interIncExpseNetNonOper", None)
        self.net_income_before_tax = data.get("netIncomeBeforeTax", None)
        self.income_tax = data.get("incomeTax", None)
        self.net_income_after_tax = data.get("netIncomeAfterTax", None)
        self.net_income_before_extra = data.get("netIncomeBeforeExtra", None)
        self.total_extraordinary_items = data.get("totalExtraordinaryItems", None)
        self.net_income = data.get("netIncome", None)
        self.income_avaito_com_excl_extra_ord = data.get("incomeAvaitoComExclExtraOrd", None)
        self.income_avaito_com_incl_extra_ord = data.get("incomeAvaitoComInclExtraOrd", None)
        self.diluted_net_income = data.get("dilutedNetIncome", None)
        self.diluted_weighted_average_shares = data.get("dilutedWeightedAverageShares", None)
        self.diluted_eps_excl_extra_items = data.get("dilutedEPSExclExtraItems", None)
        self.diluted_eps_incl_extra_items = data.get("dilutedEPSInclExtraItems", None)
        self.diluted_normalized_eps = data.get("dilutedNormalizedEPS", None)
        self.operating_profit = data.get("operatingProfit", None)
        self.earning_after_tax = data.get("earningAfterTax", None)
        self.earning_before_tax = data.get("earningBeforeTax", None)

    def __repr__(self):
        return f'<FinancialStatement quote_id={self.quote_id} fiscal_year={self.fiscal_year} fiscal_period={self.fiscal_period}>'
    


class CashFlow:
    def __init__(self, data):
      self.quoteid=data.get("quoteId", None)
      self.type=data.get("type", None)
      self.fiscal_year=data.get("fiscalYear", None)
      self.fiscal_period=data.get("fiscalPeriod", None)
      self.end_date=data.get("endDate", None)
      self.currency_id=data.get("currencyId", None)
      self.publish_date=data.get("publishDate", None)
      self.cash_from_operating_activities=data.get("cashfromOperatingActivities", None)
      self.net_income=data.get("netIncome", None)
      self.depreciation_and_amortization=data.get("depreciationAndAmortization", None)
      self.deferred_taxes=data.get("deferredTaxes", None)
      self.non_cash_items=data.get("nonCashItems", None)
      self.changes_in_working_capital=data.get("changesinWorkingCapital", None)
      self.cash_from_investing_activities=data.get("cashfromInvestingActivities", None)
      self.capital_expenditures=data.get("capitalExpenditures", None)
      self.other_investing_cashflow_items_total=data.get("otherInvestingCashFlowItemsTotal", None)
      self.cash_from_financing_activities=data.get("cashfromFinancingActivities", None)
      self.financing_cashflow_items=data.get("financingCashFlowItems", None)
      self.total_cash_dividends_paid=data.get("totalCashDividendsPaid", None)
      self.issuance_retirement_of_stock_net=data.get("issuanceRetirementofStockNet", None)
      self.issuance_retirement_of_debt_net=data.get("issuanceRetirementofDebtNet", None)
      self.foreign_exchange_effects=data.get("foreignExchangeEffects", None)
      self.net_change_in_cash=data.get("netChangeinCash", None)
    def __repr__(self):
        return f'<CashFlow quote_id={self.quoteid} fiscal_year={self.fiscal_year} fiscal_period={self.fiscal_period}>'
    



class BalanceSheet:
    def __init__(self, data):
        self.quoteId = data.get('quoteId')
        self.type = data.get('type')
        self.fiscalYear = data.get('fiscalYear')
        self.fiscalPeriod = data.get('fiscalPeriod')
        self.endDate = data.get('endDate')
        self.currencyId = data.get('currencyId')
        self.publishDate = data.get('publishDate')
        self.totalAssets = data.get('totalAssets')
        self.totalCurrentAssets = data.get('totalCurrentAssets')
        self.cashAndShortTermInvest = data.get('cashAndShortTermInvest')
        self.cashEquivalents = data.get('cashEquivalents')
        self.shortTermInvestments = data.get('shortTermInvestments')
        self.totalReceivablesNet = data.get('totalReceivablesNet')
        self.accountsReceTradeNet = data.get('accountsReceTradeNet')
        self.totalInventory = data.get('totalInventory')
        self.prepaidExpenses = data.get('prepaidExpenses')
        self.otherCurrentAssetsTotal = data.get('otherCurrentAssetsTotal')
        self.totalNonCurrentAssets = data.get('totalNonCurrentAssets')
        self.ppeTotalNet = data.get('ppeTotalNet')
        self.ppeTotalGross = data.get('ppeTotalGross')
        self.accumulatedDepreciationTotal = data.get('accumulatedDepreciationTotal')
        self.otherLongTermAssetsTotal = data.get('otherLongTermAssetsTotal')
        self.totalLiabilities = data.get('totalLiabilities')
        self.totalCurrentLiabilities = data.get('totalCurrentLiabilities')
        self.accountsPayable = data.get('accountsPayable')
        self.accruedExpenses = data.get('accruedExpenses')
        self.notesPayableShortTermDebt = data.get('notesPayableShortTermDebt')
        self.currentPortofLTDebtCapitalLeases = data.get('currentPortofLTDebtCapitalLeases')
        self.totalNonCurrentLiabilities = data.get('totalNonCurrentLiabilities')
        self.totalLongTermDebt = data.get('totalLongTermDebt')
        self.longTermDebt = data.get('longTermDebt')
        self.totalDebt = data.get('totalDebt')
        self.otherLiabilitiesTotal = data.get('otherLiabilitiesTotal')
        self.totalEquity = data.get('totalEquity')
        self.totalStockhodersEquity = data.get('totalStockhodersEquity')
        self.commonStock = data.get('commonStock')
        self.additionalPaidInCapital = data.get('additionalPaidInCapital')
        self.retainedEarnings = data.get('retainedEarnings')
        self.otherEquityTotal = data.get('otherEquityTotal')
        self.totalLiabilitiesShareholdersEquity = data.get('totalLiabilitiesShareholdersEquity')

        self.totalLiabilitiesShareholdersEquity = data.get('totalLiabilitiesShareholdersEquity')
        self.totalCommonSharesOutstanding = data.get('totalCommonSharesOutstanding')


class Forecast:
    def __init__(self, data):
        self.id = data.get('id')
        self.title = data.get('title')
        self.currencyName = data.get('currencyName')
        self.points = data.get('points')

    def __str__(self):
        return f"{self.title}: {self.points}"

    def get_trend(self):
        if len(self.points) < 2:
            return "Unknown"
        
        if self.points[-1].get("valueForecast", 0) > self.points[-2].get("valueForecast", 0):
            return "Increasing"
        else:
            return "Decreasing"