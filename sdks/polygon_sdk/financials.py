
class BalanceSheet:
    def __init__(self, financials):

        self.balance_sheet = [i['balance_sheet'] for i in financials if i is not None and i.get('balance_sheet') is not None]


        liabilities_and_equity =[i['liabilities_and_equity'] for i in self.balance_sheet if 'liabilities_and_equity' in i]
        self.liabilities_and_equity_value = [i['value'] if i['value'] is not None else 0 for i in liabilities_and_equity]

        fixed_assets=[i['fixed_assets'] for i in self.balance_sheet if 'fixed_assets' in i]
        self.fixed_assets_value= [i['value'] if i['value'] is not None else 0 for i in fixed_assets]


        other_than_fixed_noncurrent_assets=[i['other_than_fixed_noncurrent_assets'] for i in self.balance_sheet if 'other_than_fixed_noncurrent_assets' in i]
        self.other_than_fixed_noncurrent_assets_value=[i['value'] if i['value'] is not None else 0 for i in other_than_fixed_noncurrent_assets]


        equity_attributable_to_noncontrolling_interest=[i['equity_attributable_to_noncontrolling_interest'] for i in self.balance_sheet if 'equity_attributable_to_noncontrolling_interest' in i]
        self.equity_attributable_to_noncontrolling_interest_value=[i['value'] if i['value'] is not None else 0 for i in equity_attributable_to_noncontrolling_interest]


        equity_attributable_to_parent=[i['equity_attributable_to_parent'] for i in self.balance_sheet if 'equity_attributable_to_parent' in i]
        self.equity_attributable_to_parent_value=[i['value'] if i['value'] is not None else 0 for i in equity_attributable_to_parent]


        assets=[i['assets'] for i in self.balance_sheet if 'assets' in i]
        self.assets_value=[i['value'] if i['value'] is not None else 0 for i in assets]


        noncurrent_assets =[i['noncurrent_assets'] for i in self.balance_sheet if 'noncurrent_assets' in i]
        self.noncurrent_assets_value =[i['value'] if i['value'] is not None else 0 for i in noncurrent_assets]


        current_assets =[i['current_assets'] for i in self.balance_sheet if 'current_assets' in i]
        self.current_assets_value =[i['value'] if i['value'] is not None else 0 for i in current_assets]


        equity =[i['equity'] for i in self.balance_sheet if 'equity' in i]
        self.equity_value =[i['value'] if i['value'] is not None else 0 for i in equity]


        liabilities =[i['liabilities'] for i in self.balance_sheet if 'liabilities' in i]
        self.liabilities_value =[i['value'] if i['value'] is not None else 0 for i in liabilities]


        noncurrent_liabilities =[i['noncurrent_liabilities'] for i in self.balance_sheet if 'noncurrent_liabilities' in i]
        self.noncurrent_liabilities_value =[i['value'] if i['value'] is not None else 0 for i in noncurrent_liabilities]


        current_liabilities =[i['current_liabilities'] for i in self.balance_sheet if 'current_liabilities' in i]
        self.current_liabilities_value =[i['value'] if i['value'] is not None else 0 for i in current_liabilities]



class CashFlow:
    def __init__(self, financials):
                




        self.cash_flow = [i['cash_flow_statement'] for i in financials if i is not None and i.get('cash_flow_statement') is not None]

        net_cash_flow_from_investing_activities= [i['net_cash_flow_from_investing_activities'] for i in self.cash_flow if 'net_cash_flow_from_investing_activities' in i]
        self.net_cash_flow_from_investing_activities_value= [i['value'] if i['value'] is not None else 0 for i in net_cash_flow_from_investing_activities]



        net_cash_flow_continuing=[i['net_cash_flow_continuing'] for i in self.cash_flow if 'net_cash_flow_continuing' in i]
        self.net_cash_flow_continuing_value = [i['value'] if i['value'] is not None else 0 for i in net_cash_flow_continuing]

        exchange_gains_losses=[i['exchange_gains_losses'] for i in self.cash_flow if 'exchange_gains_losses' in i]
        self.exchange_gains_losses_value = [i['value'] if i['value'] is not None else 0 for i in exchange_gains_losses]


        net_cash_flow=[i['net_cash_flow'] for i in self.cash_flow if 'net_cash_flow' in i]
        self.net_cash_flow= [i['value'] if i['value'] is not None else 0 for i in net_cash_flow]


        net_cash_flow_from_operating_activities=[i['net_cash_flow_from_operating_activities'] for i in self.cash_flow if 'net_cash_flow_from_operating_activities' in i]
        self.net_cash_flow_from_operating_activities_value=[i['value'] if i['value'] is not None else 0 for i in net_cash_flow_from_operating_activities]


        net_cash_flow_from_financing_activities_continuing=[i['net_cash_flow_from_financing_activities_continuing'] for i in self.cash_flow if 'net_cash_flow_from_financing_activities_continuing' in i]
        self.net_cash_flow_from_financing_activities_continuing_value=[i['value'] if i['value'] is not None else 0 for i in net_cash_flow_from_financing_activities_continuing]


        net_cash_flow_from_operating_activities_continuing=[i['net_cash_flow_from_operating_activities_continuing'] for i in self.cash_flow if 'net_cash_flow_from_operating_activities_continuing' in i]
        self.net_cash_flow_from_operating_activities_continuing_value=[i['value'] if i['value'] is not None else 0 for i in net_cash_flow_from_operating_activities_continuing]


        net_cash_flow_from_financing_activities=[i['net_cash_flow_from_financing_activities'] for i in self.cash_flow if 'net_cash_flow_from_financing_activities' in i]
        self.net_cash_flow_from_financing_activities_value=[i['value'] if i['value'] is not None else 0 for i in net_cash_flow_from_financing_activities]


        net_cash_flow_from_investing_activities_continuing=[i['net_cash_flow_from_investing_activities_continuing'] for i in self.cash_flow if 'net_cash_flow_from_investing_activities_continuing' in i]
        self.net_cash_flow_from_investing_activities_continuing_value=[i['value'] if i['value'] is not None else 0 for i in net_cash_flow_from_investing_activities_continuing]


class IncomeStatement:
    def __init__(self, financials):

        self.income = [i['income_statement'] for i in financials if i is not None and i.get('income_statement') is not None]


        income_tax_expense_benefit_deferred=[i['income_tax_expense_benefit_deferred'] for i in self.income if 'income_tax_expense_benefit_deferred' in i]
        self.income_tax_expense_benefit_deferred_value = [i['value'] if i['value'] is not None else 0 for i in income_tax_expense_benefit_deferred]



        preferred_stock_dividends_and_other_adjustments =[i['preferred_stock_dividends_and_other_adjustments'] for i in self.income if 'preferred_stock_dividends_and_other_adjustments' in i]
        self.preferred_stock_dividends_and_other_adjustments_value = [i['value'] if i['value'] is not None else 0 for i in preferred_stock_dividends_and_other_adjustments]


        net_income_loss =[i['net_income_loss'] for i in self.income if 'net_income_loss' in i]
        self.net_income_loss_value = [i['value'] if i['value'] is not None else 0 for i in net_income_loss]


        costs_and_expenses =[i['costs_and_expenses'] for i in self.income if 'costs_and_expenses' in i]
        self.costs_and_expenses_value = [i['value'] if i['value'] is not None else 0 for i in costs_and_expenses]


        cost_of_revenue =[i['cost_of_revenue'] for i in self.income if 'cost_of_revenue' in i]
        self.cost_of_revenue_value = [i['value'] if i['value'] is not None else 0 for i in cost_of_revenue]


        income_loss_from_continuing_operations_before_tax =[i['income_loss_from_continuing_operations_before_tax'] for i in self.income if 'income_loss_from_continuing_operations_before_tax' in i]
        self.income_loss_from_continuing_operations_before_tax_value = [i['value'] if i['value'] is not None else 0 for i in income_loss_from_continuing_operations_before_tax]


        net_income_loss_attributable_to_noncontrolling_interest =[i['net_income_loss_attributable_to_noncontrolling_interest'] for i in self.income if 'net_income_loss_attributable_to_noncontrolling_interest' in i]
        self.net_income_loss_attributable_to_noncontrolling_interest_value = [i['value'] if i['value'] is not None else 0 for i in net_income_loss_attributable_to_noncontrolling_interest]


        operating_income_loss =[i['operating_income_loss'] for i in self.income if 'operating_income_loss' in i]
        self.operating_income_loss_value = [i['value'] if i['value'] is not None else 0 for i in operating_income_loss]


        income_loss_from_continuing_operations_after_tax=[i['income_loss_from_continuing_operations_after_tax'] for i in self.income if 'income_loss_from_continuing_operations_after_tax' in i]
        self.income_loss_from_continuing_operations_after_tax_value = [i['value'] if i['value'] is not None else 0 for i in income_loss_from_continuing_operations_after_tax]


        income_loss_from_discontinued_operations_net_of_tax =[i['income_loss_from_discontinued_operations_net_of_tax'] for i in self.income if 'income_loss_from_discontinued_operations_net_of_tax' in i]
        self.income_loss_from_discontinued_operations_net_of_tax_value = [i['value'] if i['value'] is not None else 0 for i in income_loss_from_discontinued_operations_net_of_tax]


        income_tax_expense_benefit_current =[i['income_tax_expense_benefit_current'] for i in self.income if 'income_tax_expense_benefit_current' in i]
        self.income_tax_expense_benefit_current_value = [i['value'] if i['value'] is not None else 0 for i in income_tax_expense_benefit_current]


        benefits_costs_expenses =[i['benefits_costs_expenses'] for i in self.income if 'benefits_costs_expenses' in i]
        self.benefits_costs_expenses_value = [i['value'] if i['value'] is not None else 0 for i in benefits_costs_expenses]


        interest_income_expense_operating_net =[i['interest_income_expense_operating_net'] for i in self.income if 'interest_income_expense_operating_net' in i]
        self.interest_income_expense_operating_net_value = [i['value'] if i['value'] is not None else 0 for i in interest_income_expense_operating_net]


        net_income_loss_attributable_to_parent =[i['net_income_loss_attributable_to_parent'] for i in self.income if 'net_income_loss_attributable_to_parent' in i]
        self.net_income_loss_attributable_to_parent_value = [i['value'] if i['value'] is not None else 0 for i in net_income_loss_attributable_to_parent]


        gross_profit =[i['gross_profit'] for i in self.income if 'gross_profit' in i]
        self.gross_profit_value = [i['value'] if i['value'] is not None else 0 for i in gross_profit]


        revenues =[i['revenues'] for i in self.income if 'revenues' in i]
        self.revenues_value = [i['value'] if i['value'] is not None else 0 for i in revenues]


        diluted_earnings_per_share =[i['diluted_earnings_per_share'] for i in self.income if 'diluted_earnings_per_share' in i]
        self.diluted_earnings_per_share_value = [i['value'] if i['value'] is not None else 0 for i in diluted_earnings_per_share]


        operating_expenses =[i['operating_expenses'] for i in self.income if 'operating_expenses' in i]
        self.operating_expenses_value = [i['value'] if i['value'] is not None else 0 for i in operating_expenses]


        participating_securities_distributed_and_undistributed_earnings_loss_basic =[i['participating_securities_distributed_and_undistributed_earnings_loss_basic'] for i in self.income if 'participating_securities_distributed_and_undistributed_earnings_loss_basic' in i]
        self.participating_securities_distributed_and_undistributed_earnings_loss_basic_value = [i['value'] if i['value'] is not None else 0 for i in participating_securities_distributed_and_undistributed_earnings_loss_basic]


        basic_earnings_per_share =[i['basic_earnings_per_share'] for i in self.income if 'basic_earnings_per_share' in i]
        self.basic_earnings_per_share_value = [i['value'] if i['value'] is not None else 0 for i in basic_earnings_per_share]


        net_income_loss_available_to_common_stockholders_basic =[i['net_income_loss_available_to_common_stockholders_basic'] for i in self.income if 'net_income_loss_available_to_common_stockholders_basic' in i]
        self.net_income_loss_available_to_common_stockholders_basic_value = [i['value'] if i['value'] is not None else 0 for i in net_income_loss_available_to_common_stockholders_basic]


        provision_for_loan_lease_and_other_losses =[i['provision_for_loan_lease_and_other_losses'] for i in self.income if 'provision_for_loan_lease_and_other_losses' in i]
        self.provision_for_loan_lease_and_other_losses_value = [i['value'] if i['value'] is not None else 0 for i in provision_for_loan_lease_and_other_losses]


        income_tax_expense_benefit_deferred =[i['income_tax_expense_benefit'] for i in self.income if 'income_tax_expense_benefit' in i]
        self.income_tax_expense_benefit_deferred_value = [i['value'] if i['value'] is not None else 0 for i in income_tax_expense_benefit_deferred]


        interest_income_expense_after_provision_for_losses =[i['interest_income_expense_after_provision_for_losses'] for i in self.income if 'interest_income_expense_after_provision_for_losses' in i]
        self.interest_income_expense_after_provision_for_losses_value = [i['value'] if i['value'] is not None else 0 for i in interest_income_expense_after_provision_for_losses]


class ComprehensiveIncome:
    def __init__(self, financials):
        self.comp_income = [i['comprehensive_income'] for i in financials if i is not None and i.get('comprehensive_income') is not None]


        comprehensive_income_loss_attributable_to_noncontrolling_interest=[i['comprehensive_income_loss_attributable_to_noncontrolling_interest'] for i in self.comp_income if 'comprehensive_income_loss_attributable_to_noncontrolling_interest' in i]
        self.comprehensive_income_loss_attributable_to_noncontrolling_interest_value = [i['value'] if i['value'] is not None else None for i in comprehensive_income_loss_attributable_to_noncontrolling_interest]

        comprehensive_income_loss_attributable_to_parent=[i['comprehensive_income_loss_attributable_to_parent'] if i['comprehensive_income_loss_attributable_to_parent'] is not None else None for i in self.comp_income]
        self.comprehensive_income_loss_attributable_to_parent_value = [i['value'] if i['value'] is not None else None for i in comprehensive_income_loss_attributable_to_parent]
        
        comprehensive_income_loss=[i['comprehensive_income_loss'] for i in self.comp_income if 'comprehensive_income_loss' in i]
        self.comprehensive_income_loss_value=[i['value'] if i['value'] is not None else 0 for i in comprehensive_income_loss]

        other_comprehensive_income_loss=[i['other_comprehensive_income_loss'] for i in self.comp_income if 'other_comprehensive_income_loss' in i]
        self.other_comprehensive_income_loss_value = [i['value'] if i['value'] is not None else 0 for i in other_comprehensive_income_loss]
