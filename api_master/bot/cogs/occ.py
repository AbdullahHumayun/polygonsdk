import disnake
from disnake.ext import commands
import requests

import datetime
import pandas as pd
from menus.embedmenus import AlertMenus
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
        await inter.edit_original_message(embed=em)



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


def setup(bot:commands.Bot):
    bot.add_cog(OCC(bot))
    print(f"> Extension {__name__} is ready\n")