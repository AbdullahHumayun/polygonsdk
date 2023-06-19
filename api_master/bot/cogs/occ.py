import disnake
from disnake.ext import commands
import requests

import datetime
import pandas as pd
from _discord.views.menus import AlertMenus
from sdks.occ_sdk.sdk import occSDK

occ = occSDK()

class PageSelect(disnake.ui.Select):
    def __init__(self, embeds):
        options = [
            disnake.SelectOption(
                label=f"Page {i+1}",
                value=f"{i}"
            ) for i in range(1, 25) 
        ]

        super().__init__(
            custom_id="page_selector1",
            placeholder="Pages 1-25",
            min_values=1,
            max_values=1,
            options=options,
            row=0
        )
        
        self.embeds = embeds

    async def callback(self, interaction: disnake.Interaction):
        await interaction.response.edit_message(embed=self.embeds[int(self.values[0])])


class OCC(commands.Cog):
    def __init__(self, bot):
        bot = bot


    @commands.slash_command()
    async def occ(self, inter):
        pass


    @occ.sub_command()
    async def stock_loans(self, inter:disnake.AppCmdInter, report_date: str, type=str):
        """Returns the number of new bi-lateral and market loans + totals."""
        await inter.response.defer()
        stock_loan_data = occ.stock_loans(report_date=report_date, type=type)
        df = pd.DataFrame(vars(stock_loan_data))
        df.to_csv('files/occ/stock_loans/stock_loans.csv')
        embeds = []
        for i,row in df.iterrows():
            
            business_date = row['businessDate']
            newMarketLoanCount = float(row['newMarketLoanCount'])
            totalMarketLoanVal = float(row['totalMarketLoanVal'])
            newBilateralLoanCount = float(row['newBilateralLoanCount'])
            totalBilateralLoanVal = float(row['totalBilateralLoanVal'])
            embed = disnake.Embed(title=f"Market Loans - OCC", description=f"```py\nYou are viewing Bilateral and market loan data from the Options Clearing Corporation. Bilateral settlement is when there are two parties involved outside of central clearing.```", color=disnake.Colour.dark_blue(), url=f"https://www.theocc.com")
            embed.add_field(name=f"Business Date:", value=f"```py\n{business_date}```", inline=False)
            embed.add_field(name=f"Market Loans", value=f"> New Count: **{newMarketLoanCount:,}**\n> Total Value: **${totalMarketLoanVal:,}**")
            embed.add_field(name=f"Market Loans", value=f"> New Count: **{newBilateralLoanCount:,}**\n> Total Value: **${totalBilateralLoanVal:,}**")
            embeds.append(embed)

        select = PageSelect(embeds[:25])


        view = AlertMenus(embeds).add_item(select)
        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji="🔻", label=f"Download", row=4)
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File('files/occ/stock_loans/stock_loans.csv'))

        
        view.add_item(button)
  

        await inter.edit_original_message(embed=embeds[0], view=view)

    @occ.sub_command()
    async def totals(self, inter: disnake.AppCmdInter):
        """Returns total futures, options, and trade volume averages."""
        await inter.response.defer(with_message=True)
       
        
        r = requests.get(url="https://marketdata.theocc.com/mdapi/volume-totals").json()

        entity=r["entity"]
        fifty2low = round(float(entity['fiftytwo_week_low'])*0.000001, ndigits=2)
        fifty2high = round(float(entity['fiftytwo_week_high'])*0.000001, ndigits=2)
        monthlyDaily = round(float(entity['monthlyDailyAverage'])*0.000001, ndigits=2)
        yeardaily = round(float(entity['yearlyDailyAverage'])*0.000001, ndigits=2)
        weeklyvol = entity['weekly_volume']
        tradedate = round(float(weeklyvol[0]['trade_date'])*0.000001, ndigits=2)
        tradevol = round(float(weeklyvol[0]['trade_volume'])*0.000001, ndigits=2)
        totalvol = round(float(entity['totalVolume'])*0.000001, ndigits=2)
        options = round(float(entity['optionsVolume'])*0.000001, ndigits=2)
        futures = round(float(entity['futuresVolume'])*0.000001, ndigits=2)
        
        ltseepoch = int(tradedate/1000)
        ltseupdate = datetime.datetime.fromtimestamp(ltseepoch)

        em = disnake.Embed(title=f"<a:_:1044647404693106728><a:_:1044647558133334126><a:_:1044647558133334126> Volume for {ltseupdate}", description="```py\nHere are today's total numbers as far as volume as reported from the Options Clearing Corporation:```", color=disnake.Colour.dark_blue(), url="https://www.theocc.com/market-data/market-data-reports/volume-and-open-interest/daily-volume")
        em.add_field(name="52 Week High/Low<a:_:1045174789150605375>", value=f"```py\nHigh: ${fifty2high} million``````py\nLow:  ${fifty2low} million```")
        em.add_field(name="Monthly & Yearly Daily Averages:<a:_:1044795645799714846>", value=f"```py\nMontlhy/Daily: ${monthlyDaily} million``` ```py\nYearly/Daily: ${yeardaily} million```")
        em.add_field(name="Options/Futures Volume:<a:_:1044897178059026432>", value=f"```py\nOptions: ${options} million.``` ```py\nFutures: ${futures} million.```")
        em.add_field(name="Trade Vol & Total Volume:<a:_:1044503960842670150>", value=f"```py\nTrade Volume{tradevol}``` ```py\n${totalvol} million``` ")
        em.set_footer(text="Data provided by OCC. Implemented by FUDstop.```")
        await inter.edit_original_response(embed=em)

    @occ.sub_command()
    async def top_equity(self, inter:disnake.AppCmdInter):
        """Displays the top 20 traded options on the day."""
        r = requests.get(url="https://cdn.optionseducation.org/rest/customtableitem.customtable.OICTradeAlertEquity?hash=8668d92358b2cb481080a7da3d75b9b8e7c4a2bee9768160655cc20e45afb105&format=json").json()
        cc = r["customtableitem_customtable_OICTradeAlertEquities"]
        co = cc[0]['customtable_OICTradeAlertEquity']
            
        opt1 = co[0]
        cvol1=opt1["call_volume"]
        ItemModifiedBy1=opt1["ItemModifiedBy"]
        time_weight1=opt1["time_weight"]
        avgtc1=round(float(opt1["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen1=opt1["ItemModifiedWhen"]
        ptrades1=opt1["put_trades"]
        ItemID1=opt1["ItemID"]
        pvol1=opt1["put_volume"]
        avgtp1=round(float(opt1["avg_total_puts"])*0.000001,ndigits=2)
        ctrades1=opt1["call_trades"]
        ItemCreatedBy1=opt1["ItemCreatedBy"]
        ItemOrder1=opt1["ItemOrder"]
        ItemCreatedWhen1=opt1["ItemCreatedWhen"]
        s1=opt1["usymbol"]
        Date1=opt1["Date"][0:10]
            
            
        opt2 = co[1]
        cvol2=opt2["call_volume"]
        ItemModifiedBy2=opt2["ItemModifiedBy"]
        time_weight2=opt2["time_weight"]
        avgtc2=round(float(opt2["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen2=opt2["ItemModifiedWhen"]
        ptrades2=opt2["put_trades"]
        ItemID2=opt2["ItemID"]
        pvol2=opt2["put_volume"]
        avgtp2=round(float(opt2["avg_total_puts"])*0.000001,ndigits=2)
        ctrades2=opt2["call_trades"]
        ItemCreatedBy2=opt2["ItemCreatedBy"]
        ItemOrder2=opt2["ItemOrder"]
        ItemCreatedWhen2=opt2["ItemCreatedWhen"]
        s2=opt2["usymbol"]
        Date2=opt2["Date"][0:10]
            
            
            
        opt3 = co[2]
        cvol3=opt3["call_volume"]
        ItemModifiedBy3=opt3["ItemModifiedBy"]
        time_weight3=opt3["time_weight"]
        avgtc3=round(float(opt3["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen3=opt3["ItemModifiedWhen"]
        ptrades3=opt3["put_trades"]
        ItemID3=opt3["ItemID"]
        pvol3=opt3["put_volume"]
        avgtp3=round(float(opt3["avg_total_puts"])*0.000001,ndigits=2)
        ctrades3=opt3["call_trades"]
        ItemCreatedBy3=opt3["ItemCreatedBy"]
        ItemOrder3=opt3["ItemOrder"]
        ItemCreatedWhen3=opt3["ItemCreatedWhen"]
        s3=opt3["usymbol"]
        Date3=opt3["Date"][0:10]
            
            
            
        opt4 = co[3]
        cvol4=opt4["call_volume"]
        ItemModifiedBy4=opt4["ItemModifiedBy"]
        time_weight4=opt4["time_weight"]
        avgtc4=round(float(opt4["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen4=opt4["ItemModifiedWhen"]
        ptrades4=opt4["put_trades"]
        ItemID4=opt4["ItemID"]
        pvol4=opt4["put_volume"]
        avgtp4=round(float(opt4["avg_total_puts"])*0.000001,ndigits=2)
        ctrades4=opt4["call_trades"]
        ItemCreatedBy4=opt4["ItemCreatedBy"]
        ItemOrder4=opt4["ItemOrder"]
        ItemCreatedWhen4=opt4["ItemCreatedWhen"]
        s4=opt4["usymbol"]
        Date4=opt4["Date"][0:10]
            
            
        opt5 = co[4]
        cvol5=opt5["call_volume"]
        ItemModifiedBy5=opt5["ItemModifiedBy"]
        time_weight5=opt5["time_weight"]
        avgtc5=round(float(opt5["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen5=opt5["ItemModifiedWhen"]
        ptrades5=opt5["put_trades"]
        ItemID5=opt5["ItemID"]
        pvol5=opt5["put_volume"]
        avgtp5=round(float(opt5["avg_total_puts"])*0.000001,ndigits=2)
        ctrades5=opt5["call_trades"]
        ItemCreatedBy5=opt5["ItemCreatedBy"]
        ItemOrder5=opt5["ItemOrder"]
        ItemCreatedWhen5=opt5["ItemCreatedWhen"]
        s5=opt5["usymbol"]
        Date5=opt5["Date"][0:10]
            
            
        opt6 = co[5]
        cvol6=opt6["call_volume"]
        ItemModifiedBy6=opt6["ItemModifiedBy"]
        time_weight6=opt6["time_weight"]
        avgtc6=round(float(opt6["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen6=opt6["ItemModifiedWhen"]
        ptrades6=opt6["put_trades"]
        ItemID6=opt6["ItemID"]
        pvol6=opt6["put_volume"]
        avgtp6=round(float(opt6["avg_total_puts"])*0.000001,ndigits=2)
        ctrades6=opt6["call_trades"]
        ItemCreatedBy6=opt6["ItemCreatedBy"]
        ItemOrder6=opt6["ItemOrder"]
        ItemCreatedWhen6=opt6["ItemCreatedWhen"]
        s6=opt6["usymbol"]
        Date6=opt6["Date"][0:10]
            
            
        opt7 = co[6]
        cvol7=opt7["call_volume"]
        ItemModifiedBy7=opt7["ItemModifiedBy"]
        time_weight7=opt7["time_weight"]
        avgtc7=round(float(opt7["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen7=opt7["ItemModifiedWhen"]
        ptrades7=opt7["put_trades"]
        ItemID7=opt7["ItemID"]
        pvol7=opt7["put_volume"]
        avgtp7=round(float(opt7["avg_total_puts"])*0.000001,ndigits=2)
        ctrades7=opt7["call_trades"]
        ItemCreatedBy7=opt7["ItemCreatedBy"]
        ItemOrder7=opt7["ItemOrder"]
        ItemCreatedWhen7=opt7["ItemCreatedWhen"]
        s7=opt7["usymbol"]
        Date7=opt7["Date"][0:10]
            
            
        opt8 = co[7]
        cvol8=opt8["call_volume"]
        ItemModifiedBy8=opt8["ItemModifiedBy"]
        time_weight8=opt8["time_weight"]
        avgtc8=round(float(opt8["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen8=opt8["ItemModifiedWhen"]
        ptrades8=opt8["put_trades"]
        ItemID8=opt8["ItemID"]
        pvol8=opt8["put_volume"]
        avgtp8=round(float(opt8["avg_total_puts"])*0.000001,ndigits=2)
        ctrades8=opt8["call_trades"]
        ItemCreatedBy8=opt8["ItemCreatedBy"]
        ItemOrder8=opt8["ItemOrder"]
        ItemCreatedWhen8=opt8["ItemCreatedWhen"]
        s8=opt8["usymbol"]
        Date8=opt8["Date"][0:10]
            
            
        opt9 = co[8]
        cvol9=opt9["call_volume"]
        ItemModifiedBy9=opt9["ItemModifiedBy"]
        time_weight9=opt9["time_weight"]
        avgtc9=round(float(opt9["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen9=opt9["ItemModifiedWhen"]
        ptrades9=opt9["put_trades"]
        ItemID9=opt9["ItemID"]
        pvol9=opt9["put_volume"]
        avgtp9=round(float(opt9["avg_total_puts"])*0.000001,ndigits=2)
        ctrades9=opt9["call_trades"]
        ItemCreatedBy9=opt9["ItemCreatedBy"]
        ItemOrder9=opt9["ItemOrder"]
        ItemCreatedWhen9=opt9["ItemCreatedWhen"]
        s9=opt9["usymbol"]
        Date9=opt9["Date"][0:10]
            
            
        opt10 = co[9]
        cvol10=opt10["call_volume"]
        ItemModifiedBy10=opt10["ItemModifiedBy"]
        time_weight10=opt10["time_weight"]
        avgtc10=round(float(opt10["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen10=opt10["ItemModifiedWhen"]
        ptrades10=opt10["put_trades"]
        ItemID10=opt10["ItemID"]
        pvol10=opt10["put_volume"]
        avgtp10=round(float(opt10["avg_total_puts"])*0.000001,ndigits=2)
        ctrades10=opt10["call_trades"]
        ItemCreatedBy10=opt10["ItemCreatedBy"]
        ItemOrder10=opt10["ItemOrder"]
        ItemCreatedWhen10=opt10["ItemCreatedWhen"]
        s10=opt10["usymbol"]
        Date10=opt10["Date"][0:10]
            
            
        opt11 = co[10]
        cvol11=opt11["call_volume"]
        ItemModifiedBy11=opt11["ItemModifiedBy"]
        time_weight11=opt11["time_weight"]
        avgtc11=round(float(opt11["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen11=opt11["ItemModifiedWhen"]
        ptrades11=opt11["put_trades"]
        ItemID11=opt11["ItemID"]
        pvol11=opt11["put_volume"]
        avgtp11=round(float(opt11["avg_total_puts"])*0.000001,ndigits=2)
        ctrades11=opt11["call_trades"]
        ItemCreatedBy11=opt11["ItemCreatedBy"]
        ItemOrder11=opt11["ItemOrder"]
        ItemCreatedWhen11=opt11["ItemCreatedWhen"]
        s11=opt11["usymbol"]
        Date11=opt11["Date"][0:10]
            
            
        opt12 = co[11]
        cvol12=opt12["call_volume"]
        ItemModifiedBy12=opt12["ItemModifiedBy"]
        time_weight12=opt12["time_weight"]
        avgtc12=round(float(opt12["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen12=opt12["ItemModifiedWhen"]
        ptrades12=opt12["put_trades"]
        ItemID12=opt12["ItemID"]
        pvol12=opt12["put_volume"]
        avgtp12=round(float(opt12["avg_total_puts"])*0.000001,ndigits=2)
        ctrades12=opt12["call_trades"]
        ItemCreatedBy12=opt12["ItemCreatedBy"]
        ItemOrder12=opt12["ItemOrder"]
        ItemCreatedWhen12=opt12["ItemCreatedWhen"]
        s12=opt12["usymbol"]
        Date12=opt12["Date"][0:10]
            
            
        opt13 = co[12]
        cvol13=opt13["call_volume"]
        ItemModifiedBy13=opt13["ItemModifiedBy"]
        time_weight13=opt13["time_weight"]
        avgtc13=round(float(opt13["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen13=opt13["ItemModifiedWhen"]
        ptrades13=opt13["put_trades"]
        ItemID13=opt13["ItemID"]
        pvol13=opt13["put_volume"]
        avgtp13=round(float(opt13["avg_total_puts"])*0.000001,ndigits=2)
        ctrades13=opt13["call_trades"]
        ItemCreatedBy13=opt13["ItemCreatedBy"]
        ItemOrder13=opt13["ItemOrder"]
        ItemCreatedWhen13=opt13["ItemCreatedWhen"]
        s13=opt13["usymbol"]
        Date13=opt13["Date"][0:10]
            
            
        opt14 = co[13]
        cvol14=opt14["call_volume"]
        ItemModifiedBy14=opt14["ItemModifiedBy"]
        time_weight14=opt14["time_weight"]
        avgtc14=round(float(opt14["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen14=opt14["ItemModifiedWhen"]
        ptrades14=opt14["put_trades"]
        ItemID14=opt14["ItemID"]
        pvol14=opt14["put_volume"]
        avgtp14=round(float(opt14["avg_total_puts"])*0.000001,ndigits=2)
        ctrades14=opt14["call_trades"]
        ItemCreatedBy14=opt14["ItemCreatedBy"]
        ItemOrder14=opt14["ItemOrder"]
        ItemCreatedWhen14=opt14["ItemCreatedWhen"]
        s14=opt14["usymbol"]
        Date14=opt14["Date"][0:10]
            
            
        opt15 = co[14]
        cvol15=opt15["call_volume"]
        ItemModifiedBy15=opt15["ItemModifiedBy"]
        time_weight15=opt15["time_weight"]
        avgtc15=round(float(opt15["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen15=opt15["ItemModifiedWhen"]
        ptrades15=opt15["put_trades"]
        ItemID15=opt15["ItemID"]
        pvol15=opt15["put_volume"]
        avgtp15=round(float(opt15["avg_total_puts"])*0.000001,ndigits=2)
        ctrades15=opt15["call_trades"]
        ItemCreatedBy15=opt15["ItemCreatedBy"]
        ItemOrder15=opt15["ItemOrder"]
        ItemCreatedWhen15=opt15["ItemCreatedWhen"]
        s15=opt15["usymbol"]
        Date15=opt15["Date"][0:10]
            
            
        opt16 = co[15]
        cvol16=opt16["call_volume"]
        ItemModifiedBy16=opt16["ItemModifiedBy"]
        time_weight16=opt16["time_weight"]
        avgtc16=round(float(opt16["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen16=opt16["ItemModifiedWhen"]
        ptrades16=opt16["put_trades"]
        ItemID16=opt16["ItemID"]
        pvol16=opt16["put_volume"]
        avgtp16=round(float(opt16["avg_total_puts"])*0.000001,ndigits=2)
        ctrades16=opt16["call_trades"]
        ItemCreatedBy16=opt16["ItemCreatedBy"]
        ItemOrder16=opt16["ItemOrder"]
        ItemCreatedWhen16=opt16["ItemCreatedWhen"]
        s16=opt16["usymbol"]
        Date16=opt16["Date"][0:10]
            
            
        opt17 = co[16]
        cvol17=opt17["call_volume"]
        ItemModifiedBy17=opt17["ItemModifiedBy"]
        time_weight17=opt17["time_weight"]
        avgtc17=round(float(opt17["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen17=opt17["ItemModifiedWhen"]
        ptrades17=opt17["put_trades"]
        ItemID17=opt17["ItemID"]
        pvol17=opt17["put_volume"]
        avgtp17=round(float(opt17["avg_total_puts"])*0.000001,ndigits=2)
        ctrades17=opt17["call_trades"]
        ItemCreatedBy17=opt17["ItemCreatedBy"]
        ItemOrder17=opt17["ItemOrder"]
        ItemCreatedWhen17=opt17["ItemCreatedWhen"]
        s17=opt17["usymbol"]
        Date17=opt17["Date"][0:10]
            
            
        opt18 = co[17]
        cvol18=opt18["call_volume"]
        ItemModifiedBy18=opt18["ItemModifiedBy"]
        time_weight18=opt18["time_weight"]
        avgtc18=round(float(opt18["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen18=opt18["ItemModifiedWhen"]
        ptrades18=opt18["put_trades"]
        ItemID18=opt18["ItemID"]
        pvol18=opt18["put_volume"]
        avgtp18=round(float(opt18["avg_total_puts"])*0.000001,ndigits=2)
        ctrades18=opt18["call_trades"]
        ItemCreatedBy18=opt18["ItemCreatedBy"]
        ItemOrder18=opt18["ItemOrder"]
        ItemCreatedWhen18=opt18["ItemCreatedWhen"]
        s18=opt18["usymbol"]
        Date18=opt18["Date"][0:10]
            
            
        opt19 = co[18]
        cvol19=opt19["call_volume"]
        ItemModifiedBy19=opt19["ItemModifiedBy"]
        time_weight19=opt19["time_weight"]
        avgtc19=round(float(opt19["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen19=opt19["ItemModifiedWhen"]
        ptrades19=opt19["put_trades"]
        ItemID19=opt19["ItemID"]
        pvol19=opt19["put_volume"]
        avgtp19=round(float(opt19["avg_total_puts"])*0.000001,ndigits=2)
        ctrades19=opt19["call_trades"]
        ItemCreatedBy19=opt19["ItemCreatedBy"]
        ItemOrder19=opt19["ItemOrder"]
        ItemCreatedWhen19=opt19["ItemCreatedWhen"]
        s19=opt19["usymbol"]
        Date19=opt19["Date"][0:10]
            
            
        opt20 = co[19]
        cvol20=opt20["call_volume"]
        ItemModifiedBy20=opt20["ItemModifiedBy"]
        time_weight20=opt20["time_weight"]
        avgtc20=round(float(opt20["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen20=opt20["ItemModifiedWhen"]
        ptrades20=opt20["put_trades"]
        ItemID20=opt20["ItemID"]
        pvol20=opt20["put_volume"]
        avgtp20=round(float(opt20["avg_total_puts"])*0.000001,ndigits=2)
        ctrades20=opt20["call_trades"]
        ItemCreatedBy20=opt20["ItemCreatedBy"]
        ItemOrder20=opt20["ItemOrder"]
        ItemCreatedWhen20=opt20["ItemCreatedWhen"]
        s20=opt20["usymbol"]
        Date20=opt20["Date"][0:10]
        view = disnake.ui.View()
        select = disnake.ui.Select(placeholder="🇹 🇴 🇵  2️⃣ 0️⃣ Traded Contracts",
        min_values=1,
        max_values=1,
        custom_id="top20occ",
        options= [ 
            disnake.SelectOption(label=f"{s1} Calls: ${cvol1:,} Puts: ${pvol1:,}",value=1,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades1:,} Put Trades: {ptrades1:,} | AvgCalls: {avgtc1} AvgPuts: {avgtp1}"),
            disnake.SelectOption(label=f"{s2} Calls: ${cvol2:,} Puts: ${pvol2:,}",value=2,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades2:,} Put Trades: {ptrades2:,} | AvgCalls: {avgtc2} AvgPuts: {avgtp2}"),
            disnake.SelectOption(label=f"{s3} Calls: ${cvol3:,} Puts: ${pvol3:,}",value=3,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades3:,} Put Trades: {ptrades3:,} | AvgCalls: {avgtc3} AvgPuts: {avgtp3}"),
            disnake.SelectOption(label=f"{s4} Calls: ${cvol4:,} Puts: ${pvol4:,}",value=4,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades4:,} Put Trades: {ptrades4:,} | AvgCalls: {avgtc4} AvgPuts: {avgtp4}"),
            disnake.SelectOption(label=f"{s5} Calls: ${cvol4:,} Puts: ${pvol5:,}",value=5,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades5:,} Put Trades: {ptrades5:,} | AvgCalls: {avgtc5} AvgPuts: {avgtp5}"),
            disnake.SelectOption(label=f"{s6} Calls: ${cvol6:,} Puts: ${pvol6:,}",value=6,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades6:,} Put Trades: {ptrades6:,} | AvgCalls: {avgtc6} AvgPuts: {avgtp6}"),
            disnake.SelectOption(label=f"{s7} Calls: ${cvol7:,} Puts: ${pvol7:,}",value=7,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades7:,} Put Trades: {ptrades7:,} | AvgCalls: {avgtc7} AvgPuts: {avgtp7}"),
            disnake.SelectOption(label=f"{s8} Calls: ${cvol8:,} Puts: ${pvol8:,}",value=8,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades8:,} Put Trades: {ptrades8:,} | AvgCalls: {avgtc8} AvgPuts: {avgtp8}"),
            disnake.SelectOption(label=f"{s9} Calls: ${cvol9:,} Puts: ${pvol9:,}",value=9,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades9:,} Put Trades: {ptrades9:,} | AvgCalls: {avgtc9} AvgPuts: {avgtp9}"),
            disnake.SelectOption(label=f"{s10} Calls: ${cvol10:,} Puts: ${pvol10:,}",value=100,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades10:,} Put Trades: {ptrades10:,} | AvgCalls: {avgtc10} AvgPuts: {avgtp10}"),
            disnake.SelectOption(label=f"{s11} Calls: ${cvol11:,} Puts: ${pvol11:,}",value=1111,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades11:,} Put Trades: {ptrades11:,} | AvgCalls: {avgtc11} AvgPuts: {avgtp11}"),
            disnake.SelectOption(label=f"{s12} Calls: ${cvol12:,} Puts: ${pvol12:,}",value=122,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades12:,} Put Trades: {ptrades12:,} | AvgCalls: {avgtc12} AvgPuts: {avgtp12}"),
            disnake.SelectOption(label=f"{s13} Calls: ${cvol13:,} Puts: ${pvol13:,}",value=133,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades13:,} Put Trades: {ptrades13:,} | AvgCalls: {avgtc13} AvgPuts: {avgtp13}"),
            disnake.SelectOption(label=f"{s14} Calls: ${cvol14:,} Puts: ${pvol14:,}",value=144,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades14:,} Put Trades: {ptrades14:,} | AvgCalls: {avgtc14} AvgPuts: {avgtp14}"),
            disnake.SelectOption(label=f"{s15} Calls: ${cvol15:,} Puts: ${pvol15:,}",value=155,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades15:,} Put Trades: {ptrades15:,} | AvgCalls: {avgtc15} AvgPuts: {avgtp15}"),
            disnake.SelectOption(label=f"{s16} Calls: ${cvol16:,} Puts: ${pvol16:,}",value=166,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades16:,} Put Trades: {ptrades16:,} | AvgCalls: {avgtc16} AvgPuts: {avgtp16}"),
            disnake.SelectOption(label=f"{s17} Calls: ${cvol17:,} Puts: ${pvol17:,}",value=177,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades17:,} Put Trades: {ptrades17:,} | AvgCalls: {avgtc17} AvgPuts: {avgtp17}"),
            disnake.SelectOption(label=f"{s18} Calls: ${cvol18:,} Puts: ${pvol18:,}",value=188,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades18:,} Put Trades: {ptrades18:,} | AvgCalls: {avgtc18} AvgPuts: {avgtp18}"),
            disnake.SelectOption(label=f"{s19} Calls: ${cvol19:,} Puts: ${pvol19:,}",value=199,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades19:,} Put Trades: {ptrades19:,} | AvgCalls: {avgtc19} AvgPuts: {avgtp19}"),
            disnake.SelectOption(label=f"{s20} Calls: ${cvol20:,} Puts: ${pvol20:,}",value=20,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades20:,} Put Trades: {ptrades20:,} | AvgCalls: {avgtc20} AvgPuts: {avgtp20}"),
        ]

        )


        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji="<a:_:1043679047617622078>")
        button.callback = lambda interaction: interaction.response.send_message(embed=embed, ephemeral=False)
        embed = disnake.Embed(title=f"Top 20 Options Traded for {Date1}", description=f"```py\nTop 20 tickers: {s1} , {s2} , {s3}, {s4} , {s5} , {s6} , {s7} , {s8} , {s9} , {s10} , {s11} , {s12} , {s13} , {s14} , {s15} , {s16} , {s17} , {s18} , {s19} , {s20}```")
        embed.add_field(name=f"{s1} Calls: ${cvol1:,} Puts: ${pvol1:,}",value=f"```py\nCall Trades: {ctrades1:,}\nPut Trades: {ptrades1:,} | AvgCalls: {avgtc1} AvgPuts: {avgtp1}```")
        embed.add_field(name=f"{s2} Calls: ${cvol2:,}\nPuts: ${pvol2:,}",value=f"```py\nCall Trades: {ctrades2:,}\nPut Trades: {ptrades2:,} | AvgCalls: {avgtc2} AvgPuts: {avgtp2}```")
        embed.add_field(name=f"{s3} Calls: ${cvol3:,}\nPuts: ${pvol3:,}",value=f"```py\nCall Trades: {ctrades3:,}\nPut Trades: {ptrades3:,} | AvgCalls: {avgtc3} AvgPuts: {avgtp3}```")
        embed.add_field(name=f"{s4} Calls: ${cvol4:,}\nPuts: ${pvol4:,}",value=f"```py\nCall Trades: {ctrades4:,}\nPut Trades: {ptrades4:,} | AvgCalls: {avgtc4} AvgPuts: {avgtp4}```")
        embed.add_field(name=f"{s5} Calls: ${cvol4:,}\nPuts: ${pvol5:,}",value=f"```py\nCall Trades: {ctrades5:,}\nPut Trades: {ptrades5:,} | AvgCalls: {avgtc5} AvgPuts: {avgtp5}```")
        embed.add_field(name=f"{s6} Calls: ${cvol6:,}\nPuts: ${pvol6:,}",value=f"```py\nCall Trades: {ctrades6:,}\nPut Trades: {ptrades6:,} | AvgCalls: {avgtc6} AvgPuts: {avgtp6}```")
        embed.add_field(name=f"{s7} Calls: ${cvol7:,}\nPuts: ${pvol7:,}",value=f"```py\nCall Trades: {ctrades7:,}\nPut Trades: {ptrades7:,} | AvgCalls: {avgtc7} AvgPuts: {avgtp7}```")
        embed.add_field(name=f"{s8} Calls: ${cvol8:,}\nPuts: ${pvol8:,}",value=f"```py\nCall Trades: {ctrades8:,}\nPut Trades: {ptrades8:,} | AvgCalls: {avgtc8} AvgPuts: {avgtp8}```")
        embed.add_field(name=f"{s9} Calls: ${cvol9:,}\nPuts: ${pvol9:,}",value=f"```py\nCall Trades: {ctrades9:,}\nPut Trades: {ptrades9:,} | AvgCalls: {avgtc9} AvgPuts: {avgtp9}```")
        embed.add_field(name=f"{s10} Calls: ${cvol10:,}\nPuts: ${pvol10:,}",value=f"```py\nCall Trades: {ctrades10:,}\nPut Trades: {ptrades10:,} | AvgCalls: {avgtc10} AvgPuts: {avgtp10}```")
        embed.add_field(name=f"{s11} Calls: ${cvol11:,}\nPuts: ${pvol11:,}",value=f"```py\nCall Trades: {ctrades11:,}\nPut Trades: {ptrades11:,} | AvgCalls: {avgtc11} AvgPuts: {avgtp11}```")
        embed.add_field(name=f"{s12} Calls: ${cvol12:,}\nPuts: ${pvol12:,}",value=f"```py\nCall Trades: {ctrades12:,}\nPut Trades: {ptrades12:,} | AvgCalls: {avgtc12} AvgPuts: {avgtp12}```")
        embed.add_field(name=f"{s13} Calls: ${cvol13:,}\nPuts: ${pvol13:,}",value=f"```py\nCall Trades: {ctrades13:,}\nPut Trades: {ptrades13:,} | AvgCalls: {avgtc13} AvgPuts: {avgtp13}```")
        embed.add_field(name=f"{s14} Calls: ${cvol14:,}\nPuts: ${pvol14:,}",value=f"```py\nCall Trades: {ctrades14:,}\nPut Trades: {ptrades14:,} | AvgCalls: {avgtc14} AvgPuts: {avgtp14}```")
        embed.add_field(name=f"{s15} Calls: ${cvol15:,}\nPuts: ${pvol15:,}",value=f"```py\nCall Trades: {ctrades15:,}\nPut Trades: {ptrades15:,} | AvgCalls: {avgtc15} AvgPuts: {avgtp15}```")
        embed.add_field(name=f"{s16} Calls: ${cvol16:,}\nPuts: ${pvol16:,}",value=f"```py\nCall Trades: {ctrades16:,}\nPut Trades: {ptrades16:,} | AvgCalls: {avgtc16} AvgPuts: {avgtp16}```")
        embed.add_field(name=f"{s17} Calls: ${cvol17:,}\nPuts: ${pvol17:,}",value=f"```py\nCall Trades: {ctrades17:,}\nPut Trades: {ptrades17:,} | AvgCalls: {avgtc17} AvgPuts: {avgtp17}```")
        embed.add_field(name=f"{s18} Calls: ${cvol18:,}\nPuts: ${pvol18:,}",value=f"```py\nCall Trades: {ctrades18:,}\nPut Trades: {ptrades18:,} | AvgCalls: {avgtc18} AvgPuts: {avgtp18}```")
        embed.add_field(name=f"{s19} Calls: ${cvol19:,}\nPuts: ${pvol19:,}",value=f"```py\nCall Trades: {ctrades19:,}\nPut Trades: {ptrades19:,} | AvgCalls: {avgtc19} AvgPuts: {avgtp19}```")
        embed.add_field(name=f"{s20} Calls: ${cvol20   :,}\nPuts: ${pvol20:,}",value=f"```py\nCall Trades: {ctrades20:,}\nPut Trades: {ptrades20:,} | AvgCalls: {avgtc20} AvgPuts: {avgtp20}```")

        view.add_item(button)
        view.add_item(select)
        await inter.response.send_message(view=view)



    


    @occ.sub_command()
    async def top_index(self, inter:disnake.AppCmdInter):
        """Displays the top 20 traded options on the day."""
        await inter.response.defer()
        r = requests.get(url="https://cdn.optionseducation.org/rest/customtableitem.customtable.OICTradeAlertIndex?hash=768f0347138583e335d6cdd28ce2a0af459043c40808567ce4321d4c77604e03&format=json").json()
        cc = r["customtableitem_customtable_OICTradeAlertIndexes"]
        co = cc[0]['customtable_OICTradeAlertINDEX']
            
        opt1 = co[0]
        cvol1=opt1["call_volume"]
        ItemModifiedBy1=opt1["ItemModifiedBy"]
        time_weight1=opt1["time_weight"]
        avgtc1=round(float(opt1["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen1=opt1["ItemModifiedWhen"]
        ptrades1=opt1["put_trades"]
        ItemID1=opt1["ItemID"]
        pvol1=opt1["put_volume"]
        avgtp1=round(float(opt1["avg_total_puts"])*0.000001,ndigits=2)
        ctrades1=opt1["call_trades"]
        ItemCreatedBy1=opt1["ItemCreatedBy"]
        ItemOrder1=opt1["ItemOrder"]
        ItemCreatedWhen1=opt1["ItemCreatedWhen"]
        s1=opt1["usymbol"]
        Date1=opt1["Date"][0:10]
            
            
        opt2 = co[1]
        cvol2=opt2["call_volume"]
        ItemModifiedBy2=opt2["ItemModifiedBy"]
        time_weight2=opt2["time_weight"]
        avgtc2=round(float(opt2["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen2=opt2["ItemModifiedWhen"]
        ptrades2=opt2["put_trades"]
        ItemID2=opt2["ItemID"]
        pvol2=opt2["put_volume"]
        avgtp2=round(float(opt2["avg_total_puts"])*0.000001,ndigits=2)
        ctrades2=opt2["call_trades"]
        ItemCreatedBy2=opt2["ItemCreatedBy"]
        ItemOrder2=opt2["ItemOrder"]
        ItemCreatedWhen2=opt2["ItemCreatedWhen"]
        s2=opt2["usymbol"]
        Date2=opt2["Date"][0:10]
            
            
            
        opt3 = co[2]
        cvol3=opt3["call_volume"]
        ItemModifiedBy3=opt3["ItemModifiedBy"]
        time_weight3=opt3["time_weight"]
        avgtc3=round(float(opt3["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen3=opt3["ItemModifiedWhen"]
        ptrades3=opt3["put_trades"]
        ItemID3=opt3["ItemID"]
        pvol3=opt3["put_volume"]
        avgtp3=round(float(opt3["avg_total_puts"])*0.000001,ndigits=2)
        ctrades3=opt3["call_trades"]
        ItemCreatedBy3=opt3["ItemCreatedBy"]
        ItemOrder3=opt3["ItemOrder"]
        ItemCreatedWhen3=opt3["ItemCreatedWhen"]
        s3=opt3["usymbol"]
        Date3=opt3["Date"][0:10]
            
            
            
        opt4 = co[3]
        cvol4=opt4["call_volume"]
        ItemModifiedBy4=opt4["ItemModifiedBy"]
        time_weight4=opt4["time_weight"]
        avgtc4=round(float(opt4["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen4=opt4["ItemModifiedWhen"]
        ptrades4=opt4["put_trades"]
        ItemID4=opt4["ItemID"]
        pvol4=opt4["put_volume"]
        avgtp4=round(float(opt4["avg_total_puts"])*0.000001,ndigits=2)
        ctrades4=opt4["call_trades"]
        ItemCreatedBy4=opt4["ItemCreatedBy"]
        ItemOrder4=opt4["ItemOrder"]
        ItemCreatedWhen4=opt4["ItemCreatedWhen"]
        s4=opt4["usymbol"]
        Date4=opt4["Date"][0:10]
            
            
        opt5 = co[4]
        cvol5=opt5["call_volume"]
        ItemModifiedBy5=opt5["ItemModifiedBy"]
        time_weight5=opt5["time_weight"]
        avgtc5=round(float(opt5["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen5=opt5["ItemModifiedWhen"]
        ptrades5=opt5["put_trades"]
        ItemID5=opt5["ItemID"]
        pvol5=opt5["put_volume"]
        avgtp5=round(float(opt5["avg_total_puts"])*0.000001,ndigits=2)
        ctrades5=opt5["call_trades"]
        ItemCreatedBy5=opt5["ItemCreatedBy"]
        ItemOrder5=opt5["ItemOrder"]
        ItemCreatedWhen5=opt5["ItemCreatedWhen"]
        s5=opt5["usymbol"]
        Date5=opt5["Date"][0:10]
            
            
        opt6 = co[5]
        cvol6=opt6["call_volume"]
        ItemModifiedBy6=opt6["ItemModifiedBy"]
        time_weight6=opt6["time_weight"]
        avgtc6=round(float(opt6["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen6=opt6["ItemModifiedWhen"]
        ptrades6=opt6["put_trades"]
        ItemID6=opt6["ItemID"]
        pvol6=opt6["put_volume"]
        avgtp6=round(float(opt6["avg_total_puts"])*0.000001,ndigits=2)
        ctrades6=opt6["call_trades"]
        ItemCreatedBy6=opt6["ItemCreatedBy"]
        ItemOrder6=opt6["ItemOrder"]
        ItemCreatedWhen6=opt6["ItemCreatedWhen"]
        s6=opt6["usymbol"]
        Date6=opt6["Date"][0:10]
            
            
        opt7 = co[6]
        cvol7=opt7["call_volume"]
        ItemModifiedBy7=opt7["ItemModifiedBy"]
        time_weight7=opt7["time_weight"]
        avgtc7=round(float(opt7["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen7=opt7["ItemModifiedWhen"]
        ptrades7=opt7["put_trades"]
        ItemID7=opt7["ItemID"]
        pvol7=opt7["put_volume"]
        avgtp7=round(float(opt7["avg_total_puts"])*0.000001,ndigits=2)
        ctrades7=opt7["call_trades"]
        ItemCreatedBy7=opt7["ItemCreatedBy"]
        ItemOrder7=opt7["ItemOrder"]
        ItemCreatedWhen7=opt7["ItemCreatedWhen"]
        s7=opt7["usymbol"]
        Date7=opt7["Date"][0:10]
            
            
        opt8 = co[7]
        cvol8=opt8["call_volume"]
        ItemModifiedBy8=opt8["ItemModifiedBy"]
        time_weight8=opt8["time_weight"]
        avgtc8=round(float(opt8["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen8=opt8["ItemModifiedWhen"]
        ptrades8=opt8["put_trades"]
        ItemID8=opt8["ItemID"]
        pvol8=opt8["put_volume"]
        avgtp8=round(float(opt8["avg_total_puts"])*0.000001,ndigits=2)
        ctrades8=opt8["call_trades"]
        ItemCreatedBy8=opt8["ItemCreatedBy"]
        ItemOrder8=opt8["ItemOrder"]
        ItemCreatedWhen8=opt8["ItemCreatedWhen"]
        s8=opt8["usymbol"]
        Date8=opt8["Date"][0:10]
            
            
        opt9 = co[8]
        cvol9=opt9["call_volume"]
        ItemModifiedBy9=opt9["ItemModifiedBy"]
        time_weight9=opt9["time_weight"]
        avgtc9=round(float(opt9["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen9=opt9["ItemModifiedWhen"]
        ptrades9=opt9["put_trades"]
        ItemID9=opt9["ItemID"]
        pvol9=opt9["put_volume"]
        avgtp9=round(float(opt9["avg_total_puts"])*0.000001,ndigits=2)
        ctrades9=opt9["call_trades"]
        ItemCreatedBy9=opt9["ItemCreatedBy"]
        ItemOrder9=opt9["ItemOrder"]
        ItemCreatedWhen9=opt9["ItemCreatedWhen"]
        s9=opt9["usymbol"]
        Date9=opt9["Date"][0:10]
            
            
        opt10 = co[9]
        cvol10=opt10["call_volume"]
        ItemModifiedBy10=opt10["ItemModifiedBy"]
        time_weight10=opt10["time_weight"]
        avgtc10=round(float(opt10["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen10=opt10["ItemModifiedWhen"]
        ptrades10=opt10["put_trades"]
        ItemID10=opt10["ItemID"]
        pvol10=opt10["put_volume"]
        avgtp10=round(float(opt10["avg_total_puts"])*0.000001,ndigits=2)
        ctrades10=opt10["call_trades"]
        ItemCreatedBy10=opt10["ItemCreatedBy"]
        ItemOrder10=opt10["ItemOrder"]
        ItemCreatedWhen10=opt10["ItemCreatedWhen"]
        s10=opt10["usymbol"]
        Date10=opt10["Date"][0:10]
            
            
        opt11 = co[10]
        cvol11=opt11["call_volume"]
        ItemModifiedBy11=opt11["ItemModifiedBy"]
        time_weight11=opt11["time_weight"]
        avgtc11=round(float(opt11["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen11=opt11["ItemModifiedWhen"]
        ptrades11=opt11["put_trades"]
        ItemID11=opt11["ItemID"]
        pvol11=opt11["put_volume"]
        avgtp11=round(float(opt11["avg_total_puts"])*0.000001,ndigits=2)
        ctrades11=opt11["call_trades"]
        ItemCreatedBy11=opt11["ItemCreatedBy"]
        ItemOrder11=opt11["ItemOrder"]
        ItemCreatedWhen11=opt11["ItemCreatedWhen"]
        s11=opt11["usymbol"]
        Date11=opt11["Date"][0:10]
            
            
        opt12 = co[11]
        cvol12=opt12["call_volume"]
        ItemModifiedBy12=opt12["ItemModifiedBy"]
        time_weight12=opt12["time_weight"]
        avgtc12=round(float(opt12["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen12=opt12["ItemModifiedWhen"]
        ptrades12=opt12["put_trades"]
        ItemID12=opt12["ItemID"]
        pvol12=opt12["put_volume"]
        avgtp12=round(float(opt12["avg_total_puts"])*0.000001,ndigits=2)
        ctrades12=opt12["call_trades"]
        ItemCreatedBy12=opt12["ItemCreatedBy"]
        ItemOrder12=opt12["ItemOrder"]
        ItemCreatedWhen12=opt12["ItemCreatedWhen"]
        s12=opt12["usymbol"]
        Date12=opt12["Date"][0:10]
            
            
        opt13 = co[12]
        cvol13=opt13["call_volume"]
        ItemModifiedBy13=opt13["ItemModifiedBy"]
        time_weight13=opt13["time_weight"]
        avgtc13=round(float(opt13["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen13=opt13["ItemModifiedWhen"]
        ptrades13=opt13["put_trades"]
        ItemID13=opt13["ItemID"]
        pvol13=opt13["put_volume"]
        avgtp13=round(float(opt13["avg_total_puts"])*0.000001,ndigits=2)
        ctrades13=opt13["call_trades"]
        ItemCreatedBy13=opt13["ItemCreatedBy"]
        ItemOrder13=opt13["ItemOrder"]
        ItemCreatedWhen13=opt13["ItemCreatedWhen"]
        s13=opt13["usymbol"]
        Date13=opt13["Date"][0:10]
            
            
        opt14 = co[13]
        cvol14=opt14["call_volume"]
        ItemModifiedBy14=opt14["ItemModifiedBy"]
        time_weight14=opt14["time_weight"]
        avgtc14=round(float(opt14["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen14=opt14["ItemModifiedWhen"]
        ptrades14=opt14["put_trades"]
        ItemID14=opt14["ItemID"]
        pvol14=opt14["put_volume"]
        avgtp14=round(float(opt14["avg_total_puts"])*0.000001,ndigits=2)
        ctrades14=opt14["call_trades"]
        ItemCreatedBy14=opt14["ItemCreatedBy"]
        ItemOrder14=opt14["ItemOrder"]
        ItemCreatedWhen14=opt14["ItemCreatedWhen"]
        s14=opt14["usymbol"]
        Date14=opt14["Date"][0:10]
            
            
        opt15 = co[14]
        cvol15=opt15["call_volume"]
        ItemModifiedBy15=opt15["ItemModifiedBy"]
        time_weight15=opt15["time_weight"]
        avgtc15=round(float(opt15["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen15=opt15["ItemModifiedWhen"]
        ptrades15=opt15["put_trades"]
        ItemID15=opt15["ItemID"]
        pvol15=opt15["put_volume"]
        avgtp15=round(float(opt15["avg_total_puts"])*0.000001,ndigits=2)
        ctrades15=opt15["call_trades"]
        ItemCreatedBy15=opt15["ItemCreatedBy"]
        ItemOrder15=opt15["ItemOrder"]
        ItemCreatedWhen15=opt15["ItemCreatedWhen"]
        s15=opt15["usymbol"]
        Date15=opt15["Date"][0:10]
            
            
        opt16 = co[15]
        cvol16=opt16["call_volume"]
        ItemModifiedBy16=opt16["ItemModifiedBy"]
        time_weight16=opt16["time_weight"]
        avgtc16=round(float(opt16["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen16=opt16["ItemModifiedWhen"]
        ptrades16=opt16["put_trades"]
        ItemID16=opt16["ItemID"]
        pvol16=opt16["put_volume"]
        avgtp16=round(float(opt16["avg_total_puts"])*0.000001,ndigits=2)
        ctrades16=opt16["call_trades"]
        ItemCreatedBy16=opt16["ItemCreatedBy"]
        ItemOrder16=opt16["ItemOrder"]
        ItemCreatedWhen16=opt16["ItemCreatedWhen"]
        s16=opt16["usymbol"]
        Date16=opt16["Date"][0:10]
            
            
        opt17 = co[16]
        cvol17=opt17["call_volume"]
        ItemModifiedBy17=opt17["ItemModifiedBy"]
        time_weight17=opt17["time_weight"]
        avgtc17=round(float(opt17["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen17=opt17["ItemModifiedWhen"]
        ptrades17=opt17["put_trades"]
        ItemID17=opt17["ItemID"]
        pvol17=opt17["put_volume"]
        avgtp17=round(float(opt17["avg_total_puts"])*0.000001,ndigits=2)
        ctrades17=opt17["call_trades"]
        ItemCreatedBy17=opt17["ItemCreatedBy"]
        ItemOrder17=opt17["ItemOrder"]
        ItemCreatedWhen17=opt17["ItemCreatedWhen"]
        s17=opt17["usymbol"]
        Date17=opt17["Date"][0:10]
            
            
 
            

        view = disnake.ui.View()
        select = disnake.ui.Select(placeholder="🇹 🇴 🇵 Index",
        min_values=1,
        max_values=1,
        custom_id="top20occ",
        options= [ 
            disnake.SelectOption(label=f"{s1} Calls: ${cvol1:,} Puts: ${pvol1:,}",value=1,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades1:,} Put Trades: {ptrades1:,} | AvgCalls: {avgtc1} AvgPuts: {avgtp1}"),
            disnake.SelectOption(label=f"{s2} Calls: ${cvol2:,} Puts: ${pvol2:,}",value=2,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades2:,} Put Trades: {ptrades2:,} | AvgCalls: {avgtc2} AvgPuts: {avgtp2}"),
            disnake.SelectOption(label=f"{s3} Calls: ${cvol3:,} Puts: ${pvol3:,}",value=3,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades3:,} Put Trades: {ptrades3:,} | AvgCalls: {avgtc3} AvgPuts: {avgtp3}"),
            disnake.SelectOption(label=f"{s4} Calls: ${cvol4:,} Puts: ${pvol4:,}",value=4,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades4:,} Put Trades: {ptrades4:,} | AvgCalls: {avgtc4} AvgPuts: {avgtp4}"),
            disnake.SelectOption(label=f"{s5} Calls: ${cvol4:,} Puts: ${pvol5:,}",value=5,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades5:,} Put Trades: {ptrades5:,} | AvgCalls: {avgtc5} AvgPuts: {avgtp5}"),
            disnake.SelectOption(label=f"{s6} Calls: ${cvol6:,} Puts: ${pvol6:,}",value=6,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades6:,} Put Trades: {ptrades6:,} | AvgCalls: {avgtc6} AvgPuts: {avgtp6}"),
            disnake.SelectOption(label=f"{s7} Calls: ${cvol7:,} Puts: ${pvol7:,}",value=7,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades7:,} Put Trades: {ptrades7:,} | AvgCalls: {avgtc7} AvgPuts: {avgtp7}"),
            disnake.SelectOption(label=f"{s8} Calls: ${cvol8:,} Puts: ${pvol8:,}",value=8,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades8:,} Put Trades: {ptrades8:,} | AvgCalls: {avgtc8} AvgPuts: {avgtp8}"),
            disnake.SelectOption(label=f"{s9} Calls: ${cvol9:,} Puts: ${pvol9:,}",value=9,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades9:,} Put Trades: {ptrades9:,} | AvgCalls: {avgtc9} AvgPuts: {avgtp9}"),
            disnake.SelectOption(label=f"{s10} Calls: ${cvol10:,} Puts: ${pvol10:,}",value=100,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades10:,} Put Trades: {ptrades10:,} | AvgCalls: {avgtc10} AvgPuts: {avgtp10}"),
            disnake.SelectOption(label=f"{s11} Calls: ${cvol11:,} Puts: ${pvol11:,}",value=1111,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades11:,} Put Trades: {ptrades11:,} | AvgCalls: {avgtc11} AvgPuts: {avgtp11}"),
            disnake.SelectOption(label=f"{s12} Calls: ${cvol12:,} Puts: ${pvol12:,}",value=122,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades12:,} Put Trades: {ptrades12:,} | AvgCalls: {avgtc12} AvgPuts: {avgtp12}"),
            disnake.SelectOption(label=f"{s13} Calls: ${cvol13:,} Puts: ${pvol13:,}",value=133,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades13:,} Put Trades: {ptrades13:,} | AvgCalls: {avgtc13} AvgPuts: {avgtp13}"),
            disnake.SelectOption(label=f"{s14} Calls: ${cvol14:,} Puts: ${pvol14:,}",value=144,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades14:,} Put Trades: {ptrades14:,} | AvgCalls: {avgtc14} AvgPuts: {avgtp14}"),
            disnake.SelectOption(label=f"{s15} Calls: ${cvol15:,} Puts: ${pvol15:,}",value=155,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades15:,} Put Trades: {ptrades15:,} | AvgCalls: {avgtc15} AvgPuts: {avgtp15}"),
            disnake.SelectOption(label=f"{s16} Calls: ${cvol16:,} Puts: ${pvol16:,}",value=166,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades16:,} Put Trades: {ptrades16:,} | AvgCalls: {avgtc16} AvgPuts: {avgtp16}"),
            disnake.SelectOption(label=f"{s17} Calls: ${cvol17:,} Puts: ${pvol17:,}",value=177,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades17:,} Put Trades: {ptrades17:,} | AvgCalls: {avgtc17} AvgPuts: {avgtp17}"),
            

        ]

        )


        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji="<a:_:1043679047617622078>")
        button.callback = lambda interaction: interaction.response.send_message(embed=embed, ephemeral=False)
        embed = disnake.Embed(title=f"Top 20 Options Traded for {Date1}", description=f"```py\nTop 20 tickers: {s1} , {s2} , {s3}, {s4} , {s5} , {s6} , {s7} , {s8} , {s9} , {s10} , {s11} , {s12} , {s13} , {s14} , {s15} , {s16} , {s17}```")
        embed.add_field(name=f"{s1} Calls: ${cvol1:,} Puts: ${pvol1:,}",value=f"```py\nCall Trades: {ctrades1:,}\nPut Trades: {ptrades1:,} | AvgCalls: {avgtc1} AvgPuts: {avgtp1}```")
        embed.add_field(name=f"{s2} Calls: ${cvol2:,}\nPuts: ${pvol2:,}",value=f"```py\nCall Trades: {ctrades2:,}\nPut Trades: {ptrades2:,} | AvgCalls: {avgtc2} AvgPuts: {avgtp2}```")
        embed.add_field(name=f"{s3} Calls: ${cvol3:,}\nPuts: ${pvol3:,}",value=f"```py\nCall Trades: {ctrades3:,}\nPut Trades: {ptrades3:,} | AvgCalls: {avgtc3} AvgPuts: {avgtp3}```")
        embed.add_field(name=f"{s4} Calls: ${cvol4:,}\nPuts: ${pvol4:,}",value=f"```py\nCall Trades: {ctrades4:,}\nPut Trades: {ptrades4:,} | AvgCalls: {avgtc4} AvgPuts: {avgtp4}```")
        embed.add_field(name=f"{s5} Calls: ${cvol4:,}\nPuts: ${pvol5:,}",value=f"```py\nCall Trades: {ctrades5:,}\nPut Trades: {ptrades5:,} | AvgCalls: {avgtc5} AvgPuts: {avgtp5}```")
        embed.add_field(name=f"{s6} Calls: ${cvol6:,}\nPuts: ${pvol6:,}",value=f"```py\nCall Trades: {ctrades6:,}\nPut Trades: {ptrades6:,} | AvgCalls: {avgtc6} AvgPuts: {avgtp6}```")
        embed.add_field(name=f"{s7} Calls: ${cvol7:,}\nPuts: ${pvol7:,}",value=f"```py\nCall Trades: {ctrades7:,}\nPut Trades: {ptrades7:,} | AvgCalls: {avgtc7} AvgPuts: {avgtp7}```")
        embed.add_field(name=f"{s8} Calls: ${cvol8:,}\nPuts: ${pvol8:,}",value=f"```py\nCall Trades: {ctrades8:,}\nPut Trades: {ptrades8:,} | AvgCalls: {avgtc8} AvgPuts: {avgtp8}```")
        embed.add_field(name=f"{s9} Calls: ${cvol9:,}\nPuts: ${pvol9:,}",value=f"```py\nCall Trades: {ctrades9:,}\nPut Trades: {ptrades9:,} | AvgCalls: {avgtc9} AvgPuts: {avgtp9}```")
        embed.add_field(name=f"{s10} Calls: ${cvol10:,}\nPuts: ${pvol10:,}",value=f"```py\nCall Trades: {ctrades10:,}\nPut Trades: {ptrades10:,} | AvgCalls: {avgtc10} AvgPuts: {avgtp10}```")
        embed.add_field(name=f"{s11} Calls: ${cvol11:,}\nPuts: ${pvol11:,}",value=f"```py\nCall Trades: {ctrades11:,}\nPut Trades: {ptrades11:,} | AvgCalls: {avgtc11} AvgPuts: {avgtp11}```")
        embed.add_field(name=f"{s12} Calls: ${cvol12:,}\nPuts: ${pvol12:,}",value=f"```py\nCall Trades: {ctrades12:,}\nPut Trades: {ptrades12:,} | AvgCalls: {avgtc12} AvgPuts: {avgtp12}```")
        embed.add_field(name=f"{s13} Calls: ${cvol13:,}\nPuts: ${pvol13:,}",value=f"```py\nCall Trades: {ctrades13:,}\nPut Trades: {ptrades13:,} | AvgCalls: {avgtc13} AvgPuts: {avgtp13}```")
        embed.add_field(name=f"{s14} Calls: ${cvol14:,}\nPuts: ${pvol14:,}",value=f"```py\nCall Trades: {ctrades14:,}\nPut Trades: {ptrades14:,} | AvgCalls: {avgtc14} AvgPuts: {avgtp14}```")
        embed.add_field(name=f"{s15} Calls: ${cvol15:,}\nPuts: ${pvol15:,}",value=f"```py\nCall Trades: {ctrades15:,}\nPut Trades: {ptrades15:,} | AvgCalls: {avgtc15} AvgPuts: {avgtp15}```")
        embed.add_field(name=f"{s16} Calls: ${cvol16:,}\nPuts: ${pvol16:,}",value=f"```py\nCall Trades: {ctrades16:,}\nPut Trades: {ptrades16:,} | AvgCalls: {avgtc16} AvgPuts: {avgtp16}```")
        embed.add_field(name=f"{s17} Calls: ${cvol17:,}\nPuts: ${pvol17:,}",value=f"```py\nCall Trades: {ctrades17:,}\nPut Trades: {ptrades17:,} | AvgCalls: {avgtc17} AvgPuts: {avgtp17}```")



        view.add_item(button)
        view.add_item(select)
        await inter.edit_original_message(view=view)



    @occ.sub_command()
    async def top_etf(self, inter:disnake.AppCmdInter):
        """Displays the top 20 traded options on the day."""
        r = requests.get(url="https://cdn.optionseducation.org/rest/customtableitem.customtable.OICTradeAlertEFT?hash=10a7f70a9922efb76e1ca884441a0df7f307da85e463d66037ddd8268b97a54f&format=json").json()
        cc = r["customtableitem_customtable_OICTradeAlertEFTs"]
        co = cc[0]['customtable_OICTradeAlertEFT']
            
        opt1 = co[0]
        cvol1=opt1["call_volume"]
        ItemModifiedBy1=opt1["ItemModifiedBy"]
        time_weight1=opt1["time_weight"]
        avgtc1=round(float(opt1["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen1=opt1["ItemModifiedWhen"]
        ptrades1=opt1["put_trades"]
        ItemID1=opt1["ItemID"]
        pvol1=opt1["put_volume"]
        avgtp1=round(float(opt1["avg_total_puts"])*0.000001,ndigits=2)
        ctrades1=opt1["call_trades"]
        ItemCreatedBy1=opt1["ItemCreatedBy"]
        ItemOrder1=opt1["ItemOrder"]
        ItemCreatedWhen1=opt1["ItemCreatedWhen"]
        s1=opt1["usymbol"]
        Date1=opt1["Date"][0:10]
            
            
        opt2 = co[1]
        cvol2=opt2["call_volume"]
        ItemModifiedBy2=opt2["ItemModifiedBy"]
        time_weight2=opt2["time_weight"]
        avgtc2=round(float(opt2["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen2=opt2["ItemModifiedWhen"]
        ptrades2=opt2["put_trades"]
        ItemID2=opt2["ItemID"]
        pvol2=opt2["put_volume"]
        avgtp2=round(float(opt2["avg_total_puts"])*0.000001,ndigits=2)
        ctrades2=opt2["call_trades"]
        ItemCreatedBy2=opt2["ItemCreatedBy"]
        ItemOrder2=opt2["ItemOrder"]
        ItemCreatedWhen2=opt2["ItemCreatedWhen"]
        s2=opt2["usymbol"]
        Date2=opt2["Date"][0:10]
            
            
            
        opt3 = co[2]
        cvol3=opt3["call_volume"]
        ItemModifiedBy3=opt3["ItemModifiedBy"]
        time_weight3=opt3["time_weight"]
        avgtc3=round(float(opt3["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen3=opt3["ItemModifiedWhen"]
        ptrades3=opt3["put_trades"]
        ItemID3=opt3["ItemID"]
        pvol3=opt3["put_volume"]
        avgtp3=round(float(opt3["avg_total_puts"])*0.000001,ndigits=2)
        ctrades3=opt3["call_trades"]
        ItemCreatedBy3=opt3["ItemCreatedBy"]
        ItemOrder3=opt3["ItemOrder"]
        ItemCreatedWhen3=opt3["ItemCreatedWhen"]
        s3=opt3["usymbol"]
        Date3=opt3["Date"][0:10]
            
            
            
        opt4 = co[3]
        cvol4=opt4["call_volume"]
        ItemModifiedBy4=opt4["ItemModifiedBy"]
        time_weight4=opt4["time_weight"]
        avgtc4=round(float(opt4["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen4=opt4["ItemModifiedWhen"]
        ptrades4=opt4["put_trades"]
        ItemID4=opt4["ItemID"]
        pvol4=opt4["put_volume"]
        avgtp4=round(float(opt4["avg_total_puts"])*0.000001,ndigits=2)
        ctrades4=opt4["call_trades"]
        ItemCreatedBy4=opt4["ItemCreatedBy"]
        ItemOrder4=opt4["ItemOrder"]
        ItemCreatedWhen4=opt4["ItemCreatedWhen"]
        s4=opt4["usymbol"]
        Date4=opt4["Date"][0:10]
            
            
        opt5 = co[4]
        cvol5=opt5["call_volume"]
        ItemModifiedBy5=opt5["ItemModifiedBy"]
        time_weight5=opt5["time_weight"]
        avgtc5=round(float(opt5["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen5=opt5["ItemModifiedWhen"]
        ptrades5=opt5["put_trades"]
        ItemID5=opt5["ItemID"]
        pvol5=opt5["put_volume"]
        avgtp5=round(float(opt5["avg_total_puts"])*0.000001,ndigits=2)
        ctrades5=opt5["call_trades"]
        ItemCreatedBy5=opt5["ItemCreatedBy"]
        ItemOrder5=opt5["ItemOrder"]
        ItemCreatedWhen5=opt5["ItemCreatedWhen"]
        s5=opt5["usymbol"]
        Date5=opt5["Date"][0:10]
            
            
        opt6 = co[5]
        cvol6=opt6["call_volume"]
        ItemModifiedBy6=opt6["ItemModifiedBy"]
        time_weight6=opt6["time_weight"]
        avgtc6=round(float(opt6["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen6=opt6["ItemModifiedWhen"]
        ptrades6=opt6["put_trades"]
        ItemID6=opt6["ItemID"]
        pvol6=opt6["put_volume"]
        avgtp6=round(float(opt6["avg_total_puts"])*0.000001,ndigits=2)
        ctrades6=opt6["call_trades"]
        ItemCreatedBy6=opt6["ItemCreatedBy"]
        ItemOrder6=opt6["ItemOrder"]
        ItemCreatedWhen6=opt6["ItemCreatedWhen"]
        s6=opt6["usymbol"]
        Date6=opt6["Date"][0:10]
            
            
        opt7 = co[6]
        cvol7=opt7["call_volume"]
        ItemModifiedBy7=opt7["ItemModifiedBy"]
        time_weight7=opt7["time_weight"]
        avgtc7=round(float(opt7["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen7=opt7["ItemModifiedWhen"]
        ptrades7=opt1["put_trades"]
        ItemID7=opt7["ItemID"]
        pvol7=opt7["put_volume"]
        avgtp7=round(float(opt7["avg_total_puts"])*0.000001,ndigits=2)
        ctrades7=opt7["call_trades"]
        ItemCreatedBy7=opt7["ItemCreatedBy"]
        ItemOrder7=opt7["ItemOrder"]
        ItemCreatedWhen7=opt7["ItemCreatedWhen"]
        s7=opt7["usymbol"]
        Date7=opt7["Date"][0:10]
            
            
        opt8 = co[7]
        cvol8=opt8["call_volume"]
        ItemModifiedBy8=opt8["ItemModifiedBy"]
        time_weight8=opt8["time_weight"]
        avgtc8=round(float(opt8["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen8=opt8["ItemModifiedWhen"]
        ptrades8=opt8["put_trades"]
        ItemID8=opt8["ItemID"]
        pvol8=opt8["put_volume"]
        avgtp8=round(float(opt8["avg_total_puts"])*0.000001,ndigits=2)
        ctrades8=opt8["call_trades"]
        ItemCreatedBy8=opt8["ItemCreatedBy"]
        ItemOrder8=opt8["ItemOrder"]
        ItemCreatedWhen8=opt8["ItemCreatedWhen"]
        s8=opt8["usymbol"]
        Date8=opt8["Date"][0:10]
            
            
        opt9 = co[8]
        cvol9=opt9["call_volume"]
        ItemModifiedBy9=opt9["ItemModifiedBy"]
        time_weight9=opt9["time_weight"]
        avgtc9=round(float(opt9["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen9=opt9["ItemModifiedWhen"]
        ptrades9=opt9["put_trades"]
        ItemID9=opt9["ItemID"]
        pvol9=opt9["put_volume"]
        avgtp9=round(float(opt9["avg_total_puts"])*0.000001,ndigits=2)
        ctrades9=opt9["call_trades"]
        ItemCreatedBy9=opt9["ItemCreatedBy"]
        ItemOrder9=opt9["ItemOrder"]
        ItemCreatedWhen9=opt9["ItemCreatedWhen"]
        s9=opt9["usymbol"]
        Date9=opt9["Date"][0:10]
            
            
        opt10 = co[9]
        cvol10=opt10["call_volume"]
        ItemModifiedBy10=opt10["ItemModifiedBy"]
        time_weight10=opt10["time_weight"]
        avgtc10=round(float(opt10["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen10=opt10["ItemModifiedWhen"]
        ptrades10=opt10["put_trades"]
        ItemID10=opt10["ItemID"]
        pvol10=opt10["put_volume"]
        avgtp10=round(float(opt10["avg_total_puts"])*0.000001,ndigits=2)
        ctrades10=opt10["call_trades"]
        ItemCreatedBy10=opt10["ItemCreatedBy"]
        ItemOrder10=opt10["ItemOrder"]
        ItemCreatedWhen10=opt10["ItemCreatedWhen"]
        s10=opt10["usymbol"]
        Date10=opt10["Date"][0:10]
            
            
        opt11 = co[10]
        cvol11=opt11["call_volume"]
        ItemModifiedBy11=opt11["ItemModifiedBy"]
        time_weight11=opt11["time_weight"]
        avgtc11=round(float(opt11["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen11=opt11["ItemModifiedWhen"]
        ptrades11=opt11["put_trades"]
        ItemID11=opt11["ItemID"]
        pvol11=opt11["put_volume"]
        avgtp11=round(float(opt11["avg_total_puts"])*0.000001,ndigits=2)
        ctrades11=opt11["call_trades"]
        ItemCreatedBy11=opt11["ItemCreatedBy"]
        ItemOrder11=opt11["ItemOrder"]
        ItemCreatedWhen11=opt11["ItemCreatedWhen"]
        s11=opt11["usymbol"]
        Date11=opt11["Date"][0:10]
            
            
        opt12 = co[11]
        cvol12=opt12["call_volume"]
        ItemModifiedBy12=opt12["ItemModifiedBy"]
        time_weight12=opt12["time_weight"]
        avgtc12=round(float(opt12["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen12=opt12["ItemModifiedWhen"]
        ptrades12=opt12["put_trades"]
        ItemID12=opt12["ItemID"]
        pvol12=opt12["put_volume"]
        avgtp12=round(float(opt12["avg_total_puts"])*0.000001,ndigits=2)
        ctrades12=opt12["call_trades"]
        ItemCreatedBy12=opt12["ItemCreatedBy"]
        ItemOrder12=opt12["ItemOrder"]
        ItemCreatedWhen12=opt12["ItemCreatedWhen"]
        s12=opt12["usymbol"]
        Date12=opt12["Date"][0:10]
            
            
        opt13 = co[12]
        cvol13=opt13["call_volume"]
        ItemModifiedBy13=opt13["ItemModifiedBy"]
        time_weight13=opt13["time_weight"]
        avgtc13=round(float(opt13["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen13=opt13["ItemModifiedWhen"]
        ptrades13=opt13["put_trades"]
        ItemID13=opt13["ItemID"]
        pvol13=opt13["put_volume"]
        avgtp13=round(float(opt13["avg_total_puts"])*0.000001,ndigits=2)
        ctrades13=opt13["call_trades"]
        ItemCreatedBy13=opt13["ItemCreatedBy"]
        ItemOrder13=opt13["ItemOrder"]
        ItemCreatedWhen13=opt13["ItemCreatedWhen"]
        s13=opt13["usymbol"]
        Date13=opt13["Date"][0:10]
            
            
        opt14 = co[13]
        cvol14=opt14["call_volume"]
        ItemModifiedBy14=opt14["ItemModifiedBy"]
        time_weight14=opt14["time_weight"]
        avgtc14=round(float(opt14["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen14=opt14["ItemModifiedWhen"]
        ptrades14=opt14["put_trades"]
        ItemID14=opt14["ItemID"]
        pvol14=opt14["put_volume"]
        avgtp14=round(float(opt14["avg_total_puts"])*0.000001,ndigits=2)
        ctrades14=opt14["call_trades"]
        ItemCreatedBy14=opt14["ItemCreatedBy"]
        ItemOrder14=opt14["ItemOrder"]
        ItemCreatedWhen14=opt14["ItemCreatedWhen"]
        s14=opt14["usymbol"]
        Date14=opt14["Date"][0:10]
            
            
        opt15 = co[14]
        cvol15=opt15["call_volume"]
        ItemModifiedBy15=opt15["ItemModifiedBy"]
        time_weight15=opt15["time_weight"]
        avgtc15=round(float(opt15["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen15=opt15["ItemModifiedWhen"]
        ptrades15=opt15["put_trades"]
        ItemID15=opt15["ItemID"]
        pvol15=opt15["put_volume"]
        avgtp15=round(float(opt15["avg_total_puts"])*0.000001,ndigits=2)
        ctrades15=opt15["call_trades"]
        ItemCreatedBy15=opt15["ItemCreatedBy"]
        ItemOrder15=opt15["ItemOrder"]
        ItemCreatedWhen15=opt15["ItemCreatedWhen"]
        s15=opt15["usymbol"]
        Date15=opt15["Date"][0:10]
            
            
        opt16 = co[15]
        cvol16=opt16["call_volume"]
        ItemModifiedBy16=opt16["ItemModifiedBy"]
        time_weight16=opt16["time_weight"]
        avgtc16=round(float(opt16["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen16=opt16["ItemModifiedWhen"]
        ptrades16=opt16["put_trades"]
        ItemID16=opt16["ItemID"]
        pvol16=opt16["put_volume"]
        avgtp16=round(float(opt16["avg_total_puts"])*0.000001,ndigits=2)
        ctrades16=opt16["call_trades"]
        ItemCreatedBy16=opt16["ItemCreatedBy"]
        ItemOrder16=opt16["ItemOrder"]
        ItemCreatedWhen16=opt16["ItemCreatedWhen"]
        s16=opt16["usymbol"]
        Date16=opt16["Date"][0:10]
            
            
        opt17 = co[16]
        cvol17=opt17["call_volume"]
        ItemModifiedBy17=opt17["ItemModifiedBy"]
        time_weight17=opt17["time_weight"]
        avgtc17=round(float(opt17["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen17=opt17["ItemModifiedWhen"]
        ptrades17=opt17["put_trades"]
        ItemID17=opt17["ItemID"]
        pvol17=opt17["put_volume"]
        avgtp17=round(float(opt17["avg_total_puts"])*0.000001,ndigits=2)
        ctrades17=opt17["call_trades"]
        ItemCreatedBy17=opt17["ItemCreatedBy"]
        ItemOrder17=opt17["ItemOrder"]
        ItemCreatedWhen17=opt17["ItemCreatedWhen"]
        s17=opt17["usymbol"]
        Date17=opt17["Date"][0:10]
            
            
        opt18 = co[17]
        cvol18=opt18["call_volume"]
        ItemModifiedBy18=opt18["ItemModifiedBy"]
        time_weight18=opt18["time_weight"]
        avgtc18=round(float(opt18["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen18=opt18["ItemModifiedWhen"]
        ptrades18=opt18["put_trades"]
        ItemID18=opt18["ItemID"]
        pvol18=opt18["put_volume"]
        avgtp18=round(float(opt18["avg_total_puts"])*0.000001,ndigits=2)
        ctrades18=opt18["call_trades"]
        ItemCreatedBy18=opt18["ItemCreatedBy"]
        ItemOrder18=opt18["ItemOrder"]
        ItemCreatedWhen18=opt18["ItemCreatedWhen"]
        s18=opt18["usymbol"]
        Date18=opt18["Date"][0:10]
            
            
        opt19 = co[18]
        cvol19=opt19["call_volume"]
        ItemModifiedBy19=opt19["ItemModifiedBy"]
        time_weight19=opt19["time_weight"]
        avgtc19=round(float(opt19["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen19=opt19["ItemModifiedWhen"]
        ptrades19=opt19["put_trades"]
        ItemID19=opt19["ItemID"]
        pvol19=opt19["put_volume"]
        avgtp19=round(float(opt19["avg_total_puts"])*0.000001,ndigits=2)
        ctrades19=opt19["call_trades"]
        ItemCreatedBy19=opt19["ItemCreatedBy"]
        ItemOrder19=opt19["ItemOrder"]
        ItemCreatedWhen19=opt19["ItemCreatedWhen"]
        s19=opt19["usymbol"]
        Date19=opt19["Date"][0:10]
            
            
        opt20 = co[19]
        cvol20=opt20["call_volume"]
        ItemModifiedBy20=opt20["ItemModifiedBy"]
        time_weight20=opt20["time_weight"]
        avgtc20=round(float(opt20["avg_total_calls"])*0.000001,ndigits=2)
        ItemModifiedWhen20=opt20["ItemModifiedWhen"]
        ptrades20=opt20["put_trades"]
        ItemID20=opt20["ItemID"]
        pvol20=opt20["put_volume"]
        avgtp20=round(float(opt20["avg_total_puts"])*0.000001,ndigits=2)
        ctrades20=opt20["call_trades"]
        ItemCreatedBy20=opt20["ItemCreatedBy"]
        ItemOrder20=opt20["ItemOrder"]
        ItemCreatedWhen20=opt20["ItemCreatedWhen"]
        s20=opt20["usymbol"]
        Date20=opt20["Date"][0:10]
        view = disnake.ui.View()
        select = disnake.ui.Select(placeholder="🇹 🇴 🇵  2️⃣ 0️⃣ Traded ETFs",
        min_values=1,
        max_values=1,
        custom_id="top20occ22",
        options= [ 
            disnake.SelectOption(label=f"{s1} Calls: ${cvol1:,} Puts: ${pvol1:,}",value=1,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades1:,} Put Trades: {ptrades1:,} | AvgCalls: {avgtc1} AvgPuts: {avgtp1}"),
            disnake.SelectOption(label=f"{s2} Calls: ${cvol2:,} Puts: ${pvol2:,}",value=2,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades2:,} Put Trades: {ptrades2:,} | AvgCalls: {avgtc2} AvgPuts: {avgtp2}"),
            disnake.SelectOption(label=f"{s3} Calls: ${cvol3:,} Puts: ${pvol3:,}",value=3,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades3:,} Put Trades: {ptrades3:,} | AvgCalls: {avgtc3} AvgPuts: {avgtp3}"),
            disnake.SelectOption(label=f"{s4} Calls: ${cvol4:,} Puts: ${pvol4:,}",value=4,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades4:,} Put Trades: {ptrades4:,} | AvgCalls: {avgtc4} AvgPuts: {avgtp4}"),
            disnake.SelectOption(label=f"{s5} Calls: ${cvol4:,} Puts: ${pvol5:,}",value=5,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades5:,} Put Trades: {ptrades5:,} | AvgCalls: {avgtc5} AvgPuts: {avgtp5}"),
            disnake.SelectOption(label=f"{s6} Calls: ${cvol6:,} Puts: ${pvol6:,}",value=6,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades6:,} Put Trades: {ptrades6:,} | AvgCalls: {avgtc6} AvgPuts: {avgtp6}"),
            disnake.SelectOption(label=f"{s7} Calls: ${cvol7:,} Puts: ${pvol7:,}",value=7,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades7:,} Put Trades: {ptrades7:,} | AvgCalls: {avgtc7} AvgPuts: {avgtp7}"),
            disnake.SelectOption(label=f"{s8} Calls: ${cvol8:,} Puts: ${pvol8:,}",value=8,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades8:,} Put Trades: {ptrades8:,} | AvgCalls: {avgtc8} AvgPuts: {avgtp8}"),
            disnake.SelectOption(label=f"{s9} Calls: ${cvol9:,} Puts: ${pvol9:,}",value=9,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades9:,} Put Trades: {ptrades9:,} | AvgCalls: {avgtc9} AvgPuts: {avgtp9}"),
            disnake.SelectOption(label=f"{s10} Calls: ${cvol10:,} Puts: ${pvol10:,}",value=100,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades10:,} Put Trades: {ptrades10:,} | AvgCalls: {avgtc10} AvgPuts: {avgtp10}"),
            disnake.SelectOption(label=f"{s11} Calls: ${cvol11:,} Puts: ${pvol11:,}",value=1111,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades11:,} Put Trades: {ptrades11:,} | AvgCalls: {avgtc11} AvgPuts: {avgtp11}"),
            disnake.SelectOption(label=f"{s12} Calls: ${cvol12:,} Puts: ${pvol12:,}",value=122,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades12:,} Put Trades: {ptrades12:,} | AvgCalls: {avgtc12} AvgPuts: {avgtp12}"),
            disnake.SelectOption(label=f"{s13} Calls: ${cvol13:,} Puts: ${pvol13:,}",value=133,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades13:,} Put Trades: {ptrades13:,} | AvgCalls: {avgtc13} AvgPuts: {avgtp13}"),
            disnake.SelectOption(label=f"{s14} Calls: ${cvol14:,} Puts: ${pvol14:,}",value=144,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades14:,} Put Trades: {ptrades14:,} | AvgCalls: {avgtc14} AvgPuts: {avgtp14}"),
            disnake.SelectOption(label=f"{s15} Calls: ${cvol15:,} Puts: ${pvol15:,}",value=155,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades15:,} Put Trades: {ptrades15:,} | AvgCalls: {avgtc15} AvgPuts: {avgtp15}"),
            disnake.SelectOption(label=f"{s16} Calls: ${cvol16:,} Puts: ${pvol16:,}",value=166,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades16:,} Put Trades: {ptrades16:,} | AvgCalls: {avgtc16} AvgPuts: {avgtp16}"),
            disnake.SelectOption(label=f"{s17} Calls: ${cvol17:,} Puts: ${pvol17:,}",value=177,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades17:,} Put Trades: {ptrades17:,} | AvgCalls: {avgtc17} AvgPuts: {avgtp17}"),
            disnake.SelectOption(label=f"{s18} Calls: ${cvol18:,} Puts: ${pvol18:,}",value=188,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades18:,} Put Trades: {ptrades18:,} | AvgCalls: {avgtc18} AvgPuts: {avgtp18}"),
            disnake.SelectOption(label=f"{s19} Calls: ${cvol19:,} Puts: ${pvol19:,}",value=199,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades19:,} Put Trades: {ptrades19:,} | AvgCalls: {avgtc19} AvgPuts: {avgtp19}"),
            disnake.SelectOption(label=f"{s20} Calls: ${cvol20:,} Puts: ${pvol20:,}",value=20,emoji="<a:_:1044795645799714846>", description=f"Call Trades: {ctrades20:,} Put Trades: {ptrades20:,} | AvgCalls: {avgtc20} AvgPuts: {avgtp20}"),
        ]

        )


        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji="<a:_:1043679047617622078>")
        button.callback = lambda interaction: interaction.response.send_message(embed=embed, ephemeral=False)
        embed = disnake.Embed(title=f"Top 20 Options Traded for {Date1}", description=f"```py\nTop 20 tickers: {s1} , {s2} , {s3}, {s4} , {s5} , {s6} , {s7} , {s8} , {s9} , {s10} , {s11} , {s12} , {s13} , {s14} , {s15} , {s16} , {s17} , {s18} , {s19} , {s20}```")
        embed.add_field(name=f"{s1} Calls: ${cvol1:,} Puts: ${pvol1:,}",value=f"```py\nCall Trades: {ctrades1:,}\nPut Trades: {ptrades1:,} | AvgCalls: {avgtc1} AvgPuts: {avgtp1}```")
        embed.add_field(name=f"{s2} Calls: ${cvol2:,}\nPuts: ${pvol2:,}",value=f"```py\nCall Trades: {ctrades2:,}\nPut Trades: {ptrades2:,} | AvgCalls: {avgtc2} AvgPuts: {avgtp2}```")
        embed.add_field(name=f"{s3} Calls: ${cvol3:,}\nPuts: ${pvol3:,}",value=f"```py\nCall Trades: {ctrades3:,}\nPut Trades: {ptrades3:,} | AvgCalls: {avgtc3} AvgPuts: {avgtp3}```")
        embed.add_field(name=f"{s4} Calls: ${cvol4:,}\nPuts: ${pvol4:,}",value=f"```py\nCall Trades: {ctrades4:,}\nPut Trades: {ptrades4:,} | AvgCalls: {avgtc4} AvgPuts: {avgtp4}```")
        embed.add_field(name=f"{s5} Calls: ${cvol4:,}\nPuts: ${pvol5:,}",value=f"```py\nCall Trades: {ctrades5:,}\nPut Trades: {ptrades5:,} | AvgCalls: {avgtc5} AvgPuts: {avgtp5}```")
        embed.add_field(name=f"{s6} Calls: ${cvol6:,}\nPuts: ${pvol6:,}",value=f"```py\nCall Trades: {ctrades6:,}\nPut Trades: {ptrades6:,} | AvgCalls: {avgtc6} AvgPuts: {avgtp6}```")
        embed.add_field(name=f"{s7} Calls: ${cvol7:,}\nPuts: ${pvol7:,}",value=f"```py\nCall Trades: {ctrades7:,}\nPut Trades: {ptrades7:,} | AvgCalls: {avgtc7} AvgPuts: {avgtp7}```")
        embed.add_field(name=f"{s8} Calls: ${cvol8:,}\nPuts: ${pvol8:,}",value=f"```py\nCall Trades: {ctrades8:,}\nPut Trades: {ptrades8:,} | AvgCalls: {avgtc8} AvgPuts: {avgtp8}```")
        embed.add_field(name=f"{s9} Calls: ${cvol9:,}\nPuts: ${pvol9:,}",value=f"```py\nCall Trades: {ctrades9:,}\nPut Trades: {ptrades9:,} | AvgCalls: {avgtc9} AvgPuts: {avgtp9}```")
        embed.add_field(name=f"{s10} Calls: ${cvol10:,}\nPuts: ${pvol10:,}",value=f"```py\nCall Trades: {ctrades10:,}\nPut Trades: {ptrades10:,} | AvgCalls: {avgtc10} AvgPuts: {avgtp10}```")
        embed.add_field(name=f"{s11} Calls: ${cvol11:,}\nPuts: ${pvol11:,}",value=f"```py\nCall Trades: {ctrades11:,}\nPut Trades: {ptrades11:,} | AvgCalls: {avgtc11} AvgPuts: {avgtp11}```")
        embed.add_field(name=f"{s12} Calls: ${cvol12:,}\nPuts: ${pvol12:,}",value=f"```py\nCall Trades: {ctrades12:,}\nPut Trades: {ptrades12:,} | AvgCalls: {avgtc12} AvgPuts: {avgtp12}```")
        embed.add_field(name=f"{s13} Calls: ${cvol13:,}\nPuts: ${pvol13:,}",value=f"```py\nCall Trades: {ctrades13:,}\nPut Trades: {ptrades13:,} | AvgCalls: {avgtc13} AvgPuts: {avgtp13}```")
        embed.add_field(name=f"{s14} Calls: ${cvol14:,}\nPuts: ${pvol14:,}",value=f"```py\nCall Trades: {ctrades14:,}\nPut Trades: {ptrades14:,} | AvgCalls: {avgtc14} AvgPuts: {avgtp14}```")
        embed.add_field(name=f"{s15} Calls: ${cvol15:,}\nPuts: ${pvol15:,}",value=f"```py\nCall Trades: {ctrades15:,}\nPut Trades: {ptrades15:,} | AvgCalls: {avgtc15} AvgPuts: {avgtp15}```")
        embed.add_field(name=f"{s16} Calls: ${cvol16:,}\nPuts: ${pvol16:,}",value=f"```py\nCall Trades: {ctrades16:,}\nPut Trades: {ptrades16:,} | AvgCalls: {avgtc16} AvgPuts: {avgtp16}```")
        embed.add_field(name=f"{s17} Calls: ${cvol17:,}\nPuts: ${pvol17:,}",value=f"```py\nCall Trades: {ctrades17:,}\nPut Trades: {ptrades17:,} | AvgCalls: {avgtc17} AvgPuts: {avgtp17}```")
        embed.add_field(name=f"{s18} Calls: ${cvol18:,}\nPuts: ${pvol18:,}",value=f"```py\nCall Trades: {ctrades18:,}\nPut Trades: {ptrades18:,} | AvgCalls: {avgtc18} AvgPuts: {avgtp18}```")
        embed.add_field(name=f"{s19} Calls: ${cvol19:,}\nPuts: ${pvol19:,}",value=f"```py\nCall Trades: {ctrades19:,}\nPut Trades: {ptrades19:,} | AvgCalls: {avgtc19} AvgPuts: {avgtp19}```")
        embed.add_field(name=f"{s20} Calls: ${cvol20   :,}\nPuts: ${pvol20:,}",value=f"```py\nCall Trades: {ctrades20:,}\nPut Trades: {ptrades20:,} | AvgCalls: {avgtc20} AvgPuts: {avgtp20}```")

        view.add_item(button)
        view.add_item(select)
        await inter.response.send_message(view=view)


    @occ.sub_command()
    async def total_volume(inter:disnake.AppCmdInter):
        """Returns the total calls / puts / ratio / volume for the day."""
        await inter.response.defer(with_message=True)
        r = requests.get(url="https://marketdata.theocc.com/mdapi/daily-volume-totals?report_date=2023-02-01").json()
        entity = r['entity']

        total_vol = entity['total_volume']
        equity_vol = entity['equity_volume']
        index_vol = entity['index_volume']
        debt_vol = entity['debt_volume']
        futures_vol = entity['futures_volume']


        df = pd.DataFrame(total_vol)
        df2 = pd.DataFrame(equity_vol)
        df3 = pd.DataFrame(index_vol)
        df4 = pd.DataFrame(debt_vol)


        total = total_vol[-1]
        calls = total['calls']
        puts = total['puts']
        ratio = total['ratio']
        volume = total['volume']
        embed = disnake.Embed()
        embed.title=f"Volume from the OCC"
        embed.description=f"```py\nThis command returns the total calls / puts / the put and call ratio / and the volume from the day as reported by the OCC.```"
        embed.color=disnake.Colour.dark_gold()
        embed.add_field(name=f"Calls:",value=f"```py\n{calls:,}```",inline=False)
        embed.add_field(name="Puts:",value=f"```py\n{puts:,}```",inline=False)
        embed.add_field(name=f"Put/Call Ratio:", value=f"```py\n{ratio}```",inline=False)
        embed.add_field(name=f"Total Volume:", value=f"```py\n{volume:,}```",inline=False)
        await inter.edit_original_message(embed=embed)


def setup(bot):
    bot.add_cog(OCC(bot))
    print(f"> Extension {__name__} is ready\n")
