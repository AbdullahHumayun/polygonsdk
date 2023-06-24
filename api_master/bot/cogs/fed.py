import disnake
from disnake.ext import commands
import requests
import fredapi as Fred
from cfg import YOUR_FRED_API_KEY
class Fed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def fed(self, inter):
        pass



    @fed.sub_command()
    async def rates(inter:disnake.AppCmdInter):
        """🎆Returns the SOFRAI, TGCR, BGCR, and SOFR Secured Fed Rates."""
        await inter.response.defer(with_message=True, ephemeral=True)
        r = requests.get(url="https://markets.newyorkfed.org/api/rates/secured/all/latest.json")
        d = r.json()
        rates = d['refRates']
        sofrai = rates[0]
        sofraidate = sofrai['effectiveDate']
        sofraitype = sofrai['type']
        sofrai30 = float(round(sofrai['average30day'],ndigits=2))
        sofrai90 = float(round(sofrai['average90day'],ndigits=2))
        sofrai180 = float(round(sofrai['average180day'],ndigits=2))
        sofraiindex = sofrai['index']
        sofraiindicator = sofrai['revisionIndicator']


        tgcrai = rates[1]
        tgcrdate = tgcrai['effectiveDate']
        tgcrtype = tgcrai['type']
        tgcrpercentrate = tgcrai['percentRate']
        tgcrpercetile1 = tgcrai['percentPercentile1']
        tgcrpercetile2 = tgcrai['percentPercentile25']
        tgcrpercetile3 = tgcrai['percentPercentile75']
        tgcrvol = tgcrai['volumeInBillions']
        tgcrpercetile1 = tgcrai['percentPercentile1']
        tgcrindicator = tgcrai['revisionIndicator']

        bgcr = rates[2]
        bgcrdate = bgcr['effectiveDate']
        bgcrtype = bgcr['type']
        bgcrpercentrate = bgcr['percentRate']
        bgcrpercetile1 = bgcr['percentPercentile1']
        bgcrpercetile2 = bgcr['percentPercentile25']
        bgcrpercetile3 = bgcr['percentPercentile75']
        bgcrvol = bgcr['volumeInBillions']
        bgcrindicator = bgcr['revisionIndicator']



        sofr = rates[3]
        sofrdate = sofr['effectiveDate']
        sofrtype = sofr['type']
        sofrpercentrate = sofr['percentRate']
        sofrpercetile1 = sofr['percentPercentile1']
        sofrpercetile2 = sofr['percentPercentile25']
        sofrpercetile3 = sofr['percentPercentile75']
        sofrvol = sofr['volumeInBillions']
        sofrpercetile1 = sofr['percentPercentile1']
        sofrindicator =sofr['revisionIndicator']

        em = disnake.Embed(title="Fed Secured Rates", description=f"```py\nCurrent Secured Rated:```", color=disnake.Colour.dark_red())
        em.add_field(name=f"TGCR - {tgcrdate}", value=f"```py\nRate: {tgcrpercentrate}% ``` ```py\nVol: {tgcrvol} b.``` ```py\nRevision: {tgcrindicator}```", inline=True)
        em.add_field(name=f"BGCR {bgcrdate}", value=f"```py\nRate: {bgcrpercentrate}%``` ```py\nVol: {bgcrvol} b.``` ```py\nRevision: {bgcrindicator}```", inline=True)
        em.add_field(name=f"SOFR {sofrdate}", value=f"```py\nRate: {sofrpercentrate}%``` ```py\nVol: {sofrvol} b. ``` ```py\nRevision: {sofrindicator}```", inline=True)
        em.add_field(name=f"SOFRAI - {sofraidate}", value=f"```py\n30DayAvg: {sofrai30}%``` ```py\n90DayAvg: {sofrai90}%``` ```py\n180DayAvg: {sofrai180}%``` ```py\nRevision:{sofrindicator}```", inline=False)
        await inter.edit_original_response(embed=em)


    @fed.sub_command()
    async def soma(inter:disnake.AppCmdInter):
        """🎆Returns the latest soma holdings, if any."""
        await inter.response.defer(with_message=True, ephemeral=True)
        r = requests.get(url="https://markets.newyorkfed.org/api/soma/summary.json")
        d = r.json()
        soma = d['soma']
        summary = soma['summary']
        for i in summary:
            date = i.get('asOfDate')
            mbs = i.get('mbs')
            mbsf = float(mbs)
            mbsr = round(mbsf*0.000000000001, ndigits=2)
            cmbs = i.get('cmbs')
            cmbsf = float(cmbs)
            cmbsr = round(cmbsf*0.000000000001,ndigits=2)
            tips = i.get('tips')
            tipsf = float(tips)
            tipsr = round(tipsf*0.000000001,ndigits=2)
            frn = i.get('frn') or 0
            frnf = float(frn) or 0
            frnr = round(frnf*0.000000001, ndigits=2)
            incomp = i.get('tipsInflationCompensation')
            incompf = float(incomp)
            incompr = round(incompf*0.000000001,ndigits=2)
            notes = i.get('notesbonds')
            notesf = float(notes)
            notesr = round(notesf*0.000000000001, ndigits=2)
            bills = i.get('bills')
            billsf = float(bills)
            billsr = round(billsf*0.000000001, ndigits=2)
            agencies = i.get('agencies') or 0
            agenciesf = float(agencies) or 0
            agenciesr = round(agenciesf*0.000000001, ndigits=2)
            total = i.get('total')
            floatt = float(total)
            totalsr = round(floatt*0.000000000001, ndigits=2)

        em = disnake.Embed(title=f"FED SOMA Holdings as of {date}", description=f"```py\nMBS: {mbsr} trillion``` ```py\n CMBS: {cmbsr} billion``` ```py\nTIPS: ${tipsr} billion``` ```py\n FRN: ${frnr} billion``` ```py\nInflation Compensation: ${incompr} billion``` ```py\nNotes: ${notesr} trillion.``` ```py\nBills: ${billsr} billion``` ```py\nAgencies: ${agenciesr} billion``` ```py\nTotal: ${totalsr} TRILLION```", color=disnake.Colour.dark_gold())

        await inter.edit_original_response(embed=em)

                

    @fed.sub_command()
    async def swaps(inter:disnake.AppCmdInter):
        """🎆Returns recent AMBS transactions from the New York Fed."""
        await inter.response.defer(with_message=True, ephemeral=True)
        r = requests.get(url=f"https://api.stlouisfed.org/fred/series/observations?series_id=SWPT&api_key={YOUR_FRED_API_KEY}&file_type=json&limit=1&observation_start=2022-10-01")
        d = r.json()
        obs = d['observations']
        value = obs['value']
        date = obs['date']
        em = disnake.Embed(title=f"FRED API - Swaps Recorded {date}", description=f"```py\n{value}```", color=disnake.Colour.dark_red())
        await inter.edit_original_response(embed=em)

    @fed.sub_command()
    async def datasearch(inter:disnake.AppCmdInter, query: str):

        query = query.lower()
        await inter.response.defer(with_message=True, ephemeral=True)
        try:
            fred = Fred.Fred.__fetch_data(api_key=YOUR_FRED_API_KEY)
            data = fred.search(f"{query}")
            id = data['id']
            start = data['realtime_start']
            end = data['realtime_end']
            title = data['title']
            obs_start = data['observation_start']
            obs_end = data['observation_end']
            freq = data['frequency']
            frequencys = data['frequency_short']
            units = data['units']
            unitss = data['units_short']
            seasonal = data['seasonal_adjustment']
            seasonals = data['seasonal_adjustment_short']
            last_updated = data['last_updated']
            popularity = data['popularity']
            notes = data['notes']
            print(f"```py\n{notes[0]} | {last_updated}```")
            em = disnake.Embed(title=f"Fred API - {title[0]}", description=f"```py\n{notes[0]} | {last_updated[0]}``` ```py\nID: {id[0]}```")
            await inter.edit_original_response(embed=em)

        except commands.CheckAnyFailure:
            await inter.send("```py\nNone found.```")



    @fed.sub_command()
    async def swaps_non_us(inter:disnake.AppCmdInter):
        """🎆Returns the last 10 non-us Swaps"""
        await inter.response.defer(with_message=True, ephemeral=True)
        r = requests.get(url="https://markets.newyorkfed.org/api/fxs/nonusdollar/last/10.json")
        d = r.json()
        swaps = d['fxSwaps']
        operations = swaps['operations']

        index1 = operations[0]
        type1 = index1['operationType']
        counterparty1 = index1['counterparty']
        currency1 = index1['currency']
        tradedate1 = index1['tradeDate']
        settlement1 = index1['settlementDate']
        maturity1 = index1['maturityDate']
        term1 = index1['termInDays']
        amount1 = index1['amount']
        small1 = index1['isSmallValue']
        updated1 = index1['lastUpdated']

        index2 = operations[1]
        type2 = index2['operationType']
        counterparty2 = index2['counterparty']
        currency2 = index2['currency']
        tradedate2 = index2['tradeDate']
        settlement2 = index2['settlementDate']
        maturity2 = index2['maturityDate']
        term2 = index2['termInDays']
        amount2 = index2['amount']
        small2 = index2['isSmallValue']
        updated2 = index2['lastUpdated']

        index3 = operations[2]
        type3 = index3['operationType']
        counterparty3 = index3['counterparty']
        currency3 = index3['currency']
        tradedate3 = index3['tradeDate']
        settlement3 = index3['settlementDate']
        maturity3 = index3['maturityDate']
        term3 = index3['termInDays']
        amount3 = index3['amount']
        small3 = index3['isSmallValue']
        updated3 = index3['lastUpdated']

        index4 = operations[3]
        type4 = index4['operationType']
        counterparty4 = index4['counterparty']
        currency4 = index4['currency']
        tradedate4 = index4['tradeDate']
        settlement4 = index4['settlementDate']
        maturity4 = index4['maturityDate']
        term4 = index4['termInDays']
        amount4 = index4['amount']
        small4 = index4['isSmallValue']
        updated4 = index4['lastUpdated']

        index5 = operations[4]
        type5 = index5['operationType']
        counterparty5 = index5['counterparty']
        currency5 = index5['currency']
        tradedate5 = index5['tradeDate']
        settlement5 = index5['settlementDate']
        maturity5 = index5['maturityDate']
        term5 = index5['termInDays']
        amount5 = index5['amount']
        small5 = index5['isSmallValue']
        updated5 = index5['lastUpdated']

        index6 = operations[5]
        type6 = index6['operationType']
        counterparty6 = index6['counterparty']
        currency6 = index6['currency']
        tradedate6 = index6['tradeDate']
        settlement6 = index6['settlementDate']
        maturity6 = index6['maturityDate']
        term6 = index6['termInDays']
        amount6 = index6['amount']
        small6 = index6['isSmallValue']
        updated6 = index6['lastUpdated']

        index7 = operations[6]
        type7 = index7['operationType']
        counterparty7 = index7['counterparty']
        currency7 = index7['currency']
        tradedate7 = index7['tradeDate']
        settlement7 = index7['settlementDate']
        maturity7 = index7['maturityDate']
        term7 = index7['termInDays']
        amount7 = index7['amount']
        small7 = index7['isSmallValue']
        updated7 = index7['lastUpdated']

        index8 = operations[7]
        type8 = index8['operationType']
        counterparty8 = index8['counterparty']
        currency8 = index8['currency']
        tradedate8 = index8['tradeDate']
        settlement8 = index8['settlementDate']
        maturity8 = index8['maturityDate']
        term8 = index8['termInDays']
        amount8 = index8['amount']
        small8 = index8['isSmallValue']
        updated8 = index8['lastUpdated']

        index9 = operations[8]
        type9 = index9['operationType']
        counterparty9 = index9['counterparty']
        currency9 = index9['currency']
        tradedate9 = index9['tradeDate']
        settlement9 = index9['settlementDate']
        maturity9 = index9['maturityDate']
        term9 = index9['termInDays']
        amount9 = index9['amount']
        small9 = index9['isSmallValue']
        updated9 = index9['lastUpdated']

        index10 = operations[9]
        type10 = index10['operationType']
        counterparty10 = index10['counterparty']
        currency10 = index10['currency']
        tradedate10 = index10['tradeDate']
        settlement10 = index10['settlementDate']
        maturity10 = index10['maturityDate']
        term10 = index10['termInDays']
        amount10 = index10['amount']
        small10 = index10['isSmallValue']
        updated10 = index10['lastUpdated']

        em = disnake.Embed(title="Non-US Dollar Liquidity Swap", description=f"```py\nType: {type1}\nCounterparty: {counterparty1}\nCurrency: {currency1}\n\nTrade Date: {tradedate1}\nSettlement Date: {settlement1}\n Maturity Date: {maturity1}\n\nTerm: {term1}\nAmount: {amount1}\n Small? {small1}", color=disnake.Colour.dark_purple())
        em.add_field(name=f"{type2}", value=f"```py\n\nCounterparty: {counterparty2}\nCurrency: {currency2}\n\nTrade Date: {tradedate2}\nSettlement Date: {settlement2}\n Maturity Date: {maturity2}\n\nTerm: {term2}\nAmount: {amount2}\n Small? {small2}```")
        em.add_field(name=f"{type2}", value=f"```py\n\nCounterparty: {counterparty3}\nCurrency: {currency3}\n\nTrade Date: {tradedate3}\nSettlement Date: {settlement3}\n Maturity Date: {maturity3}\n\nTerm: {term3}\nAmount: {amount3}\n Small? {small3}```")
        em.add_field(name=f"{type2}", value=f"```py\n\nCounterparty: {counterparty4}\nCurrency: {currency4}\n\nTrade Date: {tradedate4}\nSettlement Date: {settlement4}\n Maturity Date: {maturity4}\n\nTerm: {term4}\nAmount: {amount4}\n Small? {small4}```")
        em.add_field(name=f"{type2}", value=f"```py\n\nCounterparty: {counterparty5}\nCurrency: {currency5}\n\nTrade Date: {tradedate5}\nSettlement Date: {settlement5}\n Maturity Date: {maturity5}\n\nTerm: {term5}\nAmount: {amount5}\n Small? {small5}```")
        em.add_field(name=f"{type2}", value=f"```py\n\nCounterparty: {counterparty6}\nCurrency: {currency6}\n\nTrade Date: {tradedate6}\nSettlement Date: {settlement6}\n Maturity Date: {maturity6}\n\nTerm: {term6}\nAmount: {amount6}\n Small? {small6}```")
        em.add_field(name=f"{type2}", value=f"```py\n\nCounterparty: {counterparty7}\nCurrency: {currency7}\n\nTrade Date: {tradedate7}\nSettlement Date: {settlement7}\n Maturity Date: {maturity7}\n\nTerm: {term7}\nAmount: {amount7}\n Small? {small7}```")
        em.add_field(name=f"{type2}", value=f"```py\n\nCounterparty: {counterparty8}\nCurrency: {currency8}\n\nTrade Date: {tradedate8}\nSettlement Date: {settlement8}\n Maturity Date: {maturity8}\n\nTerm: {term8}\nAmount: {amount8}\n Small? {small8}```")
        em.add_field(name=f"{type2}", value=f"```py\n\nCounterparty: {counterparty9}\nCurrency: {currency9}\n\nTrade Date: {tradedate9}\nSettlement Date: {settlement9}\n Maturity Date: {maturity9}\n\nTerm: {term9}\nAmount: {amount9}\n Small? {small9}```")
        em.add_field(name=f"{type2}", value=f"```py\n\nCounterparty: {counterparty10}\nCurrency: {currency10}\n\nTrade Date: {tradedate10}\nSettlement Date: {settlement10}\n Maturity Date: {maturity10}\n\nTerm: {term10}\nAmount: {amount10}\n Small? {small10}```")
        await inter.edit_original_response(embed=em)

async def setup(bot:commands.Bot):
    await bot.add_cog(Fed(bot))
    print(f"> Extension {__name__} is ready\n")