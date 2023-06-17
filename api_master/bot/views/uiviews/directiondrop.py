import requests
import re
from bs4 import BeautifulSoup
import disnake
from webull import webull
from disnake.ext import commands
import stocksera
from api_master.cfg import YOUR_STOCKSERA_KEY, YOUR_NASDAQ_KEY

from utils.webull_tickers import ticker_list

client = stocksera.Client(api_key=YOUR_STOCKSERA_KEY)


"""     forecast = a['forecast']
    simple = a['simpleStatement']

    industry = analysis['industryName']#good
    total = analysis['totalCount']# of analysts | good
    datas = analysis['datas']
    eps = datas[0]
    epsname = eps['name']#good
    epsval = eps['value']#good
    epsrank = eps['rank']#good


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

    incomerevenueq2 = round(float(incomestatementlist[3]['revenue'])*0.000000001,ndigits=2)#good

    netincomeq2 = round(float(incomestatementlist[3]['netIncomeAfterTax'])*0.000001,ndigits=2)#good




    balancesheet = simple[1]
    balancetitle = balancesheet['title']
    balancelist = balancesheet['list']


    balanceliabilityq2 = balancelist[3]['liabilityRate']


    balanceassetsq2 = round(float(balancelist[3]['totalAsset'])*0.000000001,ndigits=2)#billion
    cashflow = simple[2]
    cashflowtitle = cashflow['title']
    cashflowlist = cashflow['list']

    cashfinancingbriefq2 = round(float(cashflowlist[2]['netFinancingCashBrief'])*0.000000001,ndigits=2)

    cashoperatingbriefq2 = round(float(cashflowlist[2]['netOperatingCashBrief'])*0.000000001,ndigits=2)

    finsel = disnake.ui.Select(
        placeholder=f"💸 🇫 🇮 🇳 🇦 🇳 🇨 🇮 🇦 🇱 🇸 💸 for {self.values[0]}",
        min_values=1,
        max_values=1,
        custom_id ="financials",
        
        options= [
        disnake.SelectOption(label=f"Next earnings: {estimateEarningsDate}🗓️", description=f"Industry: {industry}"),
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
        ])
    view = disnake.ui.View()
    view.add_item(finsel)

    r2 = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/ticker?tickerId={ids}&showHis=true")
    d2 = r2.json()
    latest = d2['latest']
    date = latest['date']
    item = latest['item']
    superlgin=round(float(item["superLargeInflow"]*0.000001), ndigits=2)
    superlgout=round(float(item["superLargeOutflow"]*0.000001), ndigits=2)
    superlgnet=round(float(item["superLargeNetFlow"]*0.000001), ndigits=2)
    lgin = round(float(item["largeInflow"]*0.000001), ndigits=2)
    lgout =round(float(item["largeOutflow"]*0.000001), ndigits=2)
    lgnet = round(float(item["largeNetFlow"]*0.000001), ndigits=2)
    newlgin =round(float(item["newLargeInflow"]*0.000001), ndigits=2)
    newlgout = round(float(item["newLargeOutflow"]*0.000001), ndigits=2)
    newlgnet = round(float(item["newLargeNetFlow"]*0.000001), ndigits=2)
    medin = round(float(item["mediumInflow"]*0.000001), ndigits=2)
    medout = round(float(item["mediumOutflow"]*0.000001), ndigits=2)
    mednet = round(float(item["mediumNetFlow"]*0.000001), ndigits=2)
    smallin = round(float(item["smallInflow"]*0.000001), ndigits=2)
    smallout = round(float(item["smallOutflow"]*0.000001), ndigits=2)
    smallnet = round(float(item["smallNetFlow"]*0.000001), ndigits=2)
    majorin = round(float(item["majorInflow"]*0.000001), ndigits=2)
    majorout = round(float(item["majorOutflow"]*0.000001), ndigits=2)
    majornet = round(float(item["majorNetFlow"]*0.000001), ndigits=2)
    retailin = round(float(item["retailInflow"]*0.000001), ndigits=2)
    retailout = round(float(item["retailOutflow"]*0.000001), ndigits=2)
    retailinratio =round(float(item["retailInflowRatio"]*100), ndigits=2)
    retailoutratio = round(float(item["retailOutflowRatio"]*100), ndigits=2)
    newlginratio =round(float(item["newLargeInflowRatio"]*100), ndigits=2)
    newlgoutratio = round(float(item["newLargeOutflowRatio"]*100), ndigits=2)
    mediuminratio =round(float(item["mediumInflowRatio"]*100),ndigits=2)
    mediumoutratio = round(float(item["mediumOutflowRatio"]*100),ndigits=2)
    smallinratio =round(float(item["smallInflowRatio"]*100),ndigits=2)
    smalloutratio = round(float(item["smallOutflowRatio"]*100),ndigits=2)
    majorinratio =round(float(item["majorInflowRatio"]*100),ndigits=2)
    majoroutratio = round(float(item["majorOutflowRatio"]*100),ndigits=2)
    orderflow = requests.get(f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/stat?count=10&tickerId={ids}&type=0")
    orderflowd = orderflow.json()
    dateset = orderflowd['dates']
    datelist = [i['date'] for i in dateset]

    date1 = datelist[0]
    sellvol1 = round(float(orderflowd['sellVolume']) * 0.000001, ndigits=2)
    nvol1 = round(float(orderflowd['nVolume']) * 0.000001, ndigits=2)
    buyvol1 = round(float(orderflowd['buyVolume']) * 0.000001, ndigits=2)
    avg1 = orderflowd['avePrice']
    max1 = round(float(orderflowd['maxT']) * 0.000001, ndigits=2)
    



    
    await interaction.edit_original_message(view=view) """




class DirectionDropdown(disnake.ui.Select):
    def __init__(self):

        # Set the options that will be presented inside the dropdown
        options = [
            disnake.SelectOption(
                label="Top Gainers - Premarket" ,description="Top gainers from pre-market session on the day.",
            ),
            disnake.SelectOption(
                label="Top Gainers - Aftermarket",description="Top gainers from after-market session on the day.",
            ),
            disnake.SelectOption(
                label="Top Gainers - 5 minutes",description="Top gainers from the past 5minutes on the day and updates real time.",
            ),
            disnake.SelectOption(
                label="Top Gainers - One Day",description="Top gainers from the daily time-frame.",
            ),
            disnake.SelectOption(
                label="Top Gainers - Five Days",description="Top gainers from the past five trading days.",
            ),
            disnake.SelectOption(
                label="Top Gainers - 3 Months",description="Top gainers from the past three months.",
            ),
            disnake.SelectOption(
                label="Top Losers - Premarket" ,description="Top Losers from pre-market session on the day.",
            ),
            disnake.SelectOption(
                label="Top Losers - Aftermarket",description="Top Losers from after-market session on the day.",
            ),
            disnake.SelectOption(
                label="Top Losers - 5 minutes",description="Top Losers from the past 5minutes on the day and updates real time.",
            ),
            disnake.SelectOption(
                label="Top Losers - One Day",description="Top Losers from the daily time-frame.",
            ),
            disnake.SelectOption(
                label="Top Losers - Five Days",description="Top Losers from the past five trading days.",
            ),
            disnake.SelectOption(
                label="Top Losers - 3 Months",description="Top Losers from the past three months.",
            ),

        ]

        super().__init__(
            placeholder="🛒 🇹  🇴  🇵 | 🇲  🇴  🇻  🇪  🇷  🇸 🛒",
            min_values=1,
            max_values=1,
            custom_id ="xxxx9",
            options=options,
        ),

    async def callback(self, interaction: disnake.MessageInteraction):
        await interaction.response.defer(with_message=False)
        if self.values[0] == "Top Gainers - Premarket":
            r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/wlas/ranking/topGainers?regionId=6&rankType=preMarket&pageIndex=1&pageSize=15")
            d = r.json()
            data = d['data']
            items = '\n\n'.join(f"\n{d['symbol']} {d['name']} | ${d['close']} 52W_LOW: ${d['fiftyTwoWkLow']} 52W_HIGH: ${d['fiftyTwoWkHigh']}" for d in ticker)
            embed = disnake.Embed(title=f"Realtime Gainers", description=f" ```py\n{items}```", colour=disnake.Colour.green())
            await interaction.edit_original_message(embed=embed)
        elif self.values[0] == "Top Gainers - Aftermarket":
            r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/wlas/ranking/topGainers?regionId=6&rankType=afterMarket&pageIndex=1&pageSize=15")
            d = r.json()
            data = d['data']
            ticker = [d['ticker'] for d in data]
            iitems = '\n\n'.join(f"\n{d['symbol']} {d['name']} | ${d['close']} 52W_LOW: ${d['fiftyTwoWkLow']} 52W_HIGH: ${d['fiftyTwoWkHigh']}" for d in ticker)
            embed = disnake.Embed(title=f"Realtime Gainers", description=f"```py\n ```{items}```", colour=disnake.Colour.green())
            await interaction.edit_original_message(embed=embed)
            
        elif self.values[0] == "Top Gainers - 5 minutes":
            r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/wlas/ranking/topGainers?regionId=6&rankType=5min&pageIndex=1&pageSize=15")
            d = r.json()
            data = d['data']
            ticker = [d['ticker'] for d in data]
            items = '\n\n'.join(f"\n{d['symbol']} {d['name']} | ${d['close']} 52W_LOW: ${d['fiftyTwoWkLow']} 52W_HIGH: ${d['fiftyTwoWkHigh']}" for d in ticker)
            embed = disnake.Embed(title=f"Realtime Gainers", description=f" ```py\n{items}```", colour=disnake.Colour.green())
            await interaction.edit_original_message(embed=embed)
        elif self.values[0] == "Top Gainers - One Day":
            r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/wlas/ranking/topGainers?regionId=6&rankType=5min&pageIndex=1&pageSize=15")
            d = r.json()
            data = d['data']
            ticker = [d['ticker'] for d in data]
            items = '\n\n'.join(f"\n{d['symbol']} {d['name']} | ${d['close']} 52W_LOW: ${d['fiftyTwoWkLow']} 52W_HIGH: ${d['fiftyTwoWkHigh']}" for d in ticker)
            embed = disnake.Embed(title=f"Realtime Gainers", description=f" ```py\n{items}```", colour=disnake.Colour.green())
            await interaction.edit_original_message(embed=embed)
            
        elif self.values[0] == "Top Gainers - Five Days":
            r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/wlas/ranking/topGainers?regionId=6&rankType=5min&pageIndex=1&pageSize=15")
            d = r.json()
            data = d['data']
            ticker = [d['ticker'] for d in data]
            items = '\n\n'.join(f"\n{d['symbol']} {d['name']} | ${d['close']} 52W_LOW: ${d['fiftyTwoWkLow']} 52W_HIGH: ${d['fiftyTwoWkHigh']}" for d in ticker)
            embed = disnake.Embed(title=f"Realtime Gainers", description=f" ```py\n{items}```", colour=disnake.Colour.green())
            await interaction.edit_original_message(embed=embed)
            
        elif self.values[0] == "Top Gainers - 3 Months":
            r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/wlas/ranking/topGainers?regionId=6&rankType=5min&pageIndex=1&pageSize=15")
            d = r.json()
            data = d['data']
            ticker = [d['ticker'] for d in data]
            items = '\n\n'.join(f"\n{d['symbol']} {d['name']} | ${d['close']} 52W_LOW: ${d['fiftyTwoWkLow']} 52W_HIGH: ${d['fiftyTwoWkHigh']}" for d in ticker)
            embed = disnake.Embed(title=f"Realtime Gainers", description=f" ```py\n{items}```", colour=disnake.Colour.green())
            await interaction.edit_original_message(embed=embed)
            
        elif self.values[0] == "Top Losers - Premarket":
            r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/wlas/ranking/dropGainers?regionId=6&rankType=preMarket&pageIndex=1&pageSize=15")
            d = r.json()
            data = d['data']
            ticker = [d['ticker'] for d in data]
            items = '\n\n'.join(f"\n{d['symbol']} {d['name']} | ${d['close']} 52W_LOW: ${d['fiftyTwoWkLow']} 52W_HIGH: ${d['fiftyTwoWkHigh']}" for d in ticker)
            embed = disnake.Embed(title=f"Realtime Losers - PreMarket", description=f" ```py\n{items}```", colour=disnake.Colour.green())

            await interaction.edit_original_message(embed=embed)
            
        elif self.values[0] == "Top Losers - Aftermarket":
            r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/wlas/ranking/topLosers?regionId=6&rankType=afterMarket&pageIndex=1&pageSize=15")
            d = r.json()
            data = d['data']
            ticker = [d['ticker'] for d in data]
            items = '\n\n'.join(f"\n{d['symbol']} {d['name']} | ${d['close']} 52W_LOW: ${d['fiftyTwoWkLow']} 52W_HIGH: ${d['fiftyTwoWkHigh']}" for d in ticker)
            embed = disnake.Embed(title=f"Realtime Losers - AfterMarket", description=f" ```py\n{items}```", colour=disnake.Colour.green())
            await interaction.edit_original_message(embed=embed)
            
        elif self.values[0] == "Top Losers - 5 minutes":
            r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/wlas/ranking/dropGainers?regionId=6&rankType=5min&pageIndex=1&pageSize=15")
            d = r.json()
            data = d['data']
            ticker = [d['ticker'] for d in data]
            items = '\n\n'.join(f"\n{d['symbol']} {d['name']} | ${d['close']} 52W_LOW: ${d['fiftyTwoWkLow']} 52W_HIGH: ${d['fiftyTwoWkHigh']}" for d in ticker)
            embed = disnake.Embed(title=f"Realtime Losers - 5 Minutes", description=f" ```py\n{items}```", colour=disnake.Colour.green())
            await interaction.edit_original_message(embed=embed)
            
        elif self.values[0] == "Top Losers - One Day":
            r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/wlas/ranking/dropGainers?regionId=6&rankType=1d&pageIndex=1&pageSize=15")
            d = r.json()
            data = d['data']
            ticker = [d['ticker'] for d in data]
            items = '\n\n'.join(f"\n{d['symbol']} {d['name']} | ${d['close']} 52W_LOW: ${d['fiftyTwoWkLow']} 52W_HIGH: ${d['fiftyTwoWkHigh']}" for d in ticker)
            embed = disnake.Embed(title=f"Realtime Losers - One Day", description=f" ```py\n{items}```", colour=disnake.Colour.green())
            await interaction.edit_original_message(embed=embed)
            
        elif self.values[0] == "Top Losers - Five Days":
            r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/wlas/ranking/dropGainers?regionId=6&rankType=5d&pageIndex=1&pageSize=15")
            d = r.json()
            data = d['data']
            ticker = [d['ticker'] for d in data]
            items = '\n\n'.join(f"\n{d['symbol']} {d['name']} | ${d['close']} 52W_LOW: ${d['fiftyTwoWkLow']} 52W_HIGH: ${d['fiftyTwoWkHigh']}" for d in ticker)
            embed = disnake.Embed(title=f"Realtime Losers", description=f" ```py\n{items}```", colour=disnake.Colour.green())

            await interaction.edit_original_message(embed=embed)

        elif self.values[0] == "Top Losers - 3 Months":
            r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/wlas/ranking/dropGainers?regionId=6&rankType=3m&pageIndex=1&pageSize=15")
            d = r.json()
            data = d['data']
            ticker = [d['ticker'] for d in data]
            items = '\n\n'.join(f"\n{d['symbol']} {d['name']} | ${d['close']} 52W_LOW: ${d['fiftyTwoWkLow']} 52W_HIGH: ${d['fiftyTwoWkHigh']}" for d in ticker)
            embed = disnake.Embed(title=f"Realtime Losers - 3 months", description=f" ```py\n{items}```", colour=disnake.Colour.green())

            await interaction.edit_original_message(embed=embed)




