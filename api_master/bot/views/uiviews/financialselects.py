import disnake
from disnake.ext import commands
from webull import webull
import stocksera
from api_master.cfg import YOUR_STOCKSERA_KEY
client = stocksera.Client(api_key=YOUR_STOCKSERA_KEY)

class FinancialSelect(disnake.ui.Select):
    def __init__(self, ticker: str):
        self.ticker = ticker.upper()
        wb = webull()
        a = wb.get_financials(stock=f"{ticker}")
        try:
            forecast = a['forecast']
            simple = a['simpleStatement']
            analysis = a['analysis']
        except KeyError:
            forecast = "N/A"
            simple = "N/A"
            analysis = "N/A"
        industry = analysis['industryName']#good
        try:
            total = analysis['totalCount']# of analysts | good
            datas = analysis['datas']
            eps = datas[0]
            epsname = eps['name']#good
            epsval = eps['value']#good
            epsrank = eps['rank']#good
        except KeyError:
            total = "N/A"
            datas = "N/A"
            eps = "N/A"
            epsname = "N/A"
            epsval = "N/A"
            epsrank = "N/A"


        bvps = datas[1]
        bvpsname = bvps['name']#good
        bvpsval = bvps['value']#good
        bvpsrank = bvps['rank']#good

        dps = datas[2]
        dpsname = dps['name'] #good
        dpsval = dps['label']#good
        dpsrank = dps['rank']#good

        pe = datas[3]
        pename = pe['name']#good
        peval = pe['value']#good
        perank = pe['rank']#good

        pb = datas[4]
        pbname = pb['name']#good
        pbval = pb['value']#good
        pbrank = pb['rank']#good

        roe = datas[5]
        roename = roe['name']#good
        roeval = roe['label']#good %
        roerank = roe['rank']#good

        debt_to_asset = datas[7]
        debt_to_assetname = debt_to_asset['name']#good
        debt_to_assetval = debt_to_asset['value']#good %
        debt_to_assetrank = debt_to_asset['rank']#good
        incomestatement = simple[0]
        incomestatementtitle = incomestatement['title']
        incomestatementlist = incomestatement['list']#this
        try:
            incomerevenueq3 = round(float(incomestatementlist[0]['revenue'])*0.000000001,ndigits=2)#good
        except KeyError:
            incomerevenueq3 = "N/A"
        incomerevenueq4 = round(float(incomestatementlist[1]['revenue'])*0.000000001,ndigits=2)#good
        incomerevenueq1 = round(float(incomestatementlist[2]['revenue'])*0.000000001,ndigits=2)#good
        try:
            incomerevenueq2 = round(float(incomestatementlist[3]['revenue'])*0.000000001,ndigits=2)#good
        except KeyError:
            incomerevenueq2 = "N/A"
        netincomeq3 = round(float(incomestatementlist[0]['netIncomeAfterTax'])*0.000001,ndigits=2)#good
        netincomeq4 = round(float(incomestatementlist[1]['netIncomeAfterTax'])*0.000001,ndigits=2)#good
        netincomeq1 = round(float(incomestatementlist[2]['netIncomeAfterTax'])*0.000001,ndigits=2)#good
        netincomeq2 = round(float(incomestatementlist[3]['netIncomeAfterTax'])*0.000001,ndigits=2)#good
        netincomerateq3 = round(float(incomestatementlist[0]['netIncomeRate']),ndigits=2)#good
        netincomerateq4 = round(float(incomestatementlist[1]['netIncomeRate']),ndigits=2)#good
        netincomerateq1 = round(float(incomestatementlist[2]['netIncomeRate']),ndigits=2)#good
        netincomerateq2 = round(float(incomestatementlist[3]['netIncomeRate']),ndigits=2)#good
        incomeq3 = incomestatementlist[0]['reportEndDate']#good
        incomeq4 = incomestatementlist[1]['reportEndDate']#good
        incomeq1 = incomestatementlist[2]['reportEndDate']#good
        incomeq2 = incomestatementlist[3]['reportEndDate']#good




        balancesheet = simple[1]
        balancetitle = balancesheet['title']
        balancelist = balancesheet['list']
        balanceassetsq3 = round(float(balancelist[0]['totalAsset'])*0.000000001,ndigits=2)#billion
        balanceassetsq4 = round(float(balancelist[1]['totalAsset'])*0.000000001,ndigits=2)#billion
        balanceassetsq1 = round(float(balancelist[2]['totalAsset'])*0.000000001,ndigits=2)#billion
        balanceassetsq2 = round(float(balancelist[3]['totalAsset'])*0.000000001,ndigits=2)#billion
        balanceliabilityq3 = balancelist[0]['liabilityRate']#billion
        balanceliabilityq4 = balancelist[1]['liabilityRate']#billion
        balanceliabilityq1 = balancelist[2]['liabilityRate']#billion
        balanceliabilityq2 = balancelist[3]['liabilityRate']#billion
        totalliabilityq3 = round(float(balancelist[0]['totalLiability'])*0.000000001,ndigits=2)#billion
        totalliabilityq4 = round(float(balancelist[1]['totalLiability'])*0.000000001,ndigits=2)#billion
        totalliabilityq1 = round(float(balancelist[2]['totalLiability'])*0.000000001,ndigits=2)#billion
        totalliabilityq2 = round(float(balancelist[3]['totalLiability'])*0.000000001,ndigits=2)#billion
        balanceq3 = balancelist[0]['reportEndDate']
        balanceq4 = balancelist[1]['reportEndDate']
        balanceq1 = balancelist[2]['reportEndDate']
        balanceq2 = balancelist[3]['reportEndDate']


        cashflow = simple[2]
        cashflowtitle = cashflow['title']
        cashflowlist = cashflow['list']
        cashinvestmentbriefq3 = round(float(cashflowlist[0]['netInvestmentCashBrief'])*0.000000001,ndigits=2)#billion
        cashinvestmentbriefq4 = round(float(cashflowlist[1]['netInvestmentCashBrief'])*0.000000001,ndigits=2)#billion
        cashinvestmentbriefq2 = round(float(cashflowlist[2]['netInvestmentCashBrief'])*0.000000001,ndigits=2)#billion
        cashinvestmentbriefq1 = round(float(cashflowlist[3]['netInvestmentCashBrief'])*0.000000001,ndigits=2)#billion
        cashfinancingbriefq3 = round(float(cashflowlist[0]['netFinancingCashBrief'])*0.000000001,ndigits=2)#billion
        cashfinancingbriefq4 = round(float(cashflowlist[1]['netFinancingCashBrief'])*0.000000001,ndigits=2)#billion
        cashfinancingbriefq2 = round(float(cashflowlist[2]['netFinancingCashBrief'])*0.000000001,ndigits=2)#billion
        cashfinancingbriefq1 = round(float(cashflowlist[3]['netFinancingCashBrief'])*0.000000001,ndigits=2)#billion
        cashoperatingbriefq3 = round(float(cashflowlist[0]['netOperatingCashBrief'])*0.000000001,ndigits=2)#billion
        cashoperatingbriefq4 = round(float(cashflowlist[1]['netOperatingCashBrief'])*0.000000001,ndigits=2)#billion
        cashoperatingbriefq2 = round(float(cashflowlist[2]['netOperatingCashBrief'])*0.000000001,ndigits=2)#billion
        cashoperatingbriefq1 = round(float(cashflowlist[3]['netOperatingCashBrief'])*0.000000001,ndigits=2)#billion
        cashq3 = balancelist[0]['reportEndDate']
        cashq4 = balancelist[1]['reportEndDate']
        cashq1 = balancelist[2]['reportEndDate']
        cashq2 = balancelist[3]['reportEndDate']



            
        options= [
        disnake.SelectOption(label="Industry", description=f"Industry: {industry}"),
        disnake.SelectOption(label=f"Earnings Per Share ({epsname})", description=f"Value: {epsval} | Industry Rank: {epsrank}"),
        disnake.SelectOption(label=f"Book Value Per Share ({bvpsname})", description=f"Value: {bvpsval} | Industry Rank: {bvpsrank}"),
        disnake.SelectOption(label=f"{dpsname}", description=f"Value: {dpsval} | Industry Rank: {dpsrank}"),
        disnake.SelectOption(label=f"Price to Earnings: {pename}", description=f"Value: {peval} | Industry Rank: {perank}"),
        disnake.SelectOption(label=f"Price to Book: {pbname}", description=f"Value: {pbval} | Industry Rank: {pbrank}"),
        disnake.SelectOption(label=f"Return on Equity: {roename}", description=f"Value: {roeval}% | Industry Rank: {roerank}"),
        disnake.SelectOption(label=f"Debt to Asset: {debt_to_assetname}", description=f"Value: {debt_to_assetval}% | Industry Rank: {debt_to_assetrank} billion."),
        disnake.SelectOption(label=f"{incomestatementtitle} Q2 2022🗓️", description=f"Revenue: {incomerevenueq2} billion | Net After Tax: {netincomeq2} billion."),
        disnake.SelectOption(label=f"{balancetitle} Q2 2022🗓️", description=f"Assets: {balanceassetsq2} billion | Total Liability: {balanceliabilityq2} billion."),
        disnake.SelectOption(label=f"{cashflowtitle} Q2 2022🗓️", description=f"Financing: {cashfinancingbriefq2} billion | Operating: {cashoperatingbriefq2} billion."),
        ]
        super().__init__(
            placeholder="💸🇫 🇮 🇳 🇦 🇳 🇨 🇮 🇦 🇱 🇸💸",
            min_values=1,
            max_values=1,
            custom_id ="ruleselect",
            options=options,
        ) 

    async def callback(self, interaction: disnake.MessageCommandInteraction):
        if self.values[0] == self.values[0]:
            view = disnake.ui.View()
            b = disnake.ui.Button(style=disnake.ButtonStyle.green, label="🤖 🇨  🇲  🇩  🇸")
            b.callback = lambda interaction: interaction.response.edit_message(f"</cmds:1028831096395288692>")
            view.add_item(b)
            em = disnake.Embed(title="Commands")
            await interaction.response.edit_message(view=view)