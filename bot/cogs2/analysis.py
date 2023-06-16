"""ANALYSIS COG"""
import disnake
import requests
import webull
from disnake.ext import commands
from autocomp import ticker_autocomp



class Analysis(commands.Cog):
    def __init__(self, bot):
        """PARENT CLASS"""
        self.bot = bot



    @commands.slash_command()
    async def analysis(self,inter):
        """Analysis slash command list."""



    @analysis.sub_command()
    async def all_52s(self,interaction:disnake.ApplicationCommandInteraction, choice: str=commands.Param(name="type", choices=["nearHigh", "nearLow", "newHigh", "newLow"]), ):
        """🔎Scan 52 week highs / lows + near high / near lows."""
        await interaction.response.defer(with_message=True, ephemeral=False)
        nearhighr = requests.get(url=f"https://quotes-gw.webullfintech.com/api/wlas/ranking/52weeks?regionId=6&rankType={choice}&pageSize=10&order=lastChangeRatio&direction=1")
        nearhighd = nearhighr.json()
        data = nearhighd['data']
        #tt1 = data[0]
        #t1t = t1['ticker']
        #t1name = t1t['name']
        #t1sym = t1t['disSymbol']
        #t1exch = t1t['disExchangeCode']
        #t1opt = t1t['derivativeSupport']
        #t1close = t1t['close']
        #t1open = t1t['open']
        #t1low = t1t['low']
        #t152h = t1t['fiftyTwoWkHigh']
        #t152l = t1t['fiftyTwoWkLow']
        #t1vol = round(float(t1t['volume'])*0.000001,ndigits=2)#million
        #t1vr = t1t['vibrateRatio']


        #t1v = t1['values']
        #t1week = t1v['weeksPrice']
        #t1hist = t1v['historyPrice']
        #t1lpch = round(float(t1v['lastChangeRatio'])*100,ndigits=2)



        #tt2 = data[1]
        #t2t = t2['ticker']
        #t2name = t2t['name']
        #t2sym = t2t['disSymbol']
        #t2exch = t2t['disExchangeCode']
        #t2opt = t2t['derivativeSupport']
        #t2close = t2t['close']
        #t2open = t2t['open']
        #t2low = t2t['low']
        #t252h = t2t['fiftyTwoWkHigh']
        #t252l = t2t['fiftyTwoWkLow']
        #t2vol = round(float(t2t['volume'])*0.000001,ndigits=2)#million
        #t2vr = t2t['vibrateRatio']



        #t2v = t2['values']
        #t2week = t2v['weeksPrice']
        #t2hist = t2v['historyPrice']
        #t2lpch = round(float(t2v['lastChangeRatio'])*100,ndigits=2)


        #tt3 = data[2]
        #t3t = t3['ticker']
        #t3name = t3t['name']
        #t3sym = t3t['disSymbol']
        #t3exch = t3t['disExchangeCode']
        #t3opt = t3t['derivativeSupport']
        #t3close = t3t['close']
        #t3open = t3t['open']
        #t3low = t3t['low']
        #t352h = t3t['fiftyTwoWkHigh']
        #t352l = t3t['fiftyTwoWkLow']
        #t3vol = round(float(t3t['volume'])*0.000001,ndigits=2)#million

        #t3vr = t3t['vibrateRatio']
        #t3v = t3['values']
        #t3week = t3v['weeksPrice']
        #t3hist = t3v['historyPrice']
        #t3lpch = round(float(t3v['lastChangeRatio'])*100,ndigits=2)

        #tt4 = data[3]
        #t4t = t4['ticker']
        #t4name = t4t['name']
        #t4sym = t4t['disSymbol']
        #t4exch = t4t['disExchangeCode']
        #t4opt = t4t['derivativeSupport']
        #t4close = t4t['close']
        #t4open = t4t['open']
        #t4low = t4t['low']
        #t452h = t4t['fiftyTwoWkHigh']
        #t452l = t4t['fiftyTwoWkLow']
        #t4vol = round(float(t4t['volume'])*0.000001,ndigits=2)#million
        #t4vr = t4t['vibrateRatio']

        #t4v = t4['values']
        #t4week = t4v['weeksPrice']
        #t4hist = t4v['historyPrice']
        #t4lpch = round(float(t4v['lastChangeRatio'])*100,ndigits=2)

        #tt5 = data[4]
        #t5t = t5['ticker']
        #t5name = t5t['name']
        #t5sym = t5t['disSymbol']
        #t5exch = t5t['disExchangeCode']
        #t5opt = t5t['derivativeSupport']
        #t5close = t5t['close']
        #t5open = t5t['open']
        #t5low = t5t['low']
        #t552h = t5t['fiftyTwoWkHigh']
        #t552l = t5t['fiftyTwoWkLow']
        #t5vol = round(float(t5t['volume'])*0.000001,ndigits=2)#million
        #t5vr = t5t['vibrateRatio']

        #t5v = t5['values']
        #t5week = t5v['weeksPrice']
        #t5hist = t5v['historyPrice']
        #t5lpch = round(float(t5v['lastChangeRatio'])*100,ndigits=2)

        #tt6 = data[5]
        #t6t = t6['ticker']
        #t6name = t6t['name']
        #t6sym = t6t['disSymbol']
        #t6exch = t6t['disExchangeCode']
        #t6opt = t6t['derivativeSupport']
        #t6close = t6t['close']
        #t6open = t6t['open']
        #t6low = t6t['low']
        #t652h = t6t['fiftyTwoWkHigh']
        #t652l = t6t['fiftyTwoWkLow']
        #t6vol = round(float(t6t['volume'])*0.000001,ndigits=2)#million


        #t6v = t6['values']
        #t6week = t6v['weeksPrice']
        #t6hist = t6v['historyPrice']
        #t6lpch = round(float(t6v['lastChangeRatio'])*100,ndigits=2)

        #tt7 = data[6]
        #t7t = t7['ticker']
        #t7name = t7t['name']
        #t7sym = t7t['disSymbol']
        #t7exch = t7t['disExchangeCode']
        #t7opt = t7t['derivativeSupport']
        #t7close = t7t['close']
        #t7open = t7t['open']
        #t7low = t7t['low']
        #t752h = t7t['fiftyTwoWkHigh']
        #t752l = t7t['fiftyTwoWkLow']
        #t7vol = round(float(t7t['volume'])*0.000001,ndigits=2)#million

        #t7v = t7['values']
        #t7week = t7v['weeksPrice']
        #t7hist = t7v['historyPrice']
        #t7lpch = round(float(t7v['lastChangeRatio'])*100,ndigits=2)

        #tt8 = data[7]
        #t8t = t8['ticker']
        #t8name = t8t['name']
        #t8sym = t8t['disSymbol']
        #t8exch = t8t['disExchangeCode']
        #t8opt = t8t['derivativeSupport']
        #t8close = t8t['close']
        #t8open = t8t['open']
        #t8low = t8t['low']
        #t852h = t8t['fiftyTwoWkHigh']
        #t852l = t8t['fiftyTwoWkLow']
        #t8vol = round(float(t8t['volume'])*0.000001,ndigits=2)#million


        #t8v = t8['values']
        #t8week = t8v['weeksPrice']
        #t8hist = t8v['historyPrice']
        #t8lpch = round(float(t8v['lastChangeRatio'])*100,ndigits=2)

        tt9 = data[8]
        #t9t = t9['ticker']
        #t9name = t9t['name']
        #t9sym = t9t['disSymbol']
        #t9exch = t9t['disExchangeCode']
        #t9opt = t9t['derivativeSupport']
        #t9close = t9t['close']
        #t9open = t9t['open']
        #t9low = t9t['low']
        #t952h = t9t['fiftyTwoWkHigh']
        #t952l = t9t['fiftyTwoWkLow']
        #t9vol = round(float(t9t['volume'])*0.000001,ndigits=2)#million


        #t9v = t9['values']
        #t9week = t9v['weeksPrice']
        #t9hist = t9v['historyPrice']
        #t9lpch = round(float(t9v['lastChangeRatio'])*100,ndigits=2)

        t10 = data[9]
        #t10t = t10['ticker']
        #t10name = t10t['name']
        #t10sym = t10t['disSymbol']
        #t10exch = t10t['disExchangeCode']
        #t10opt = t10t['derivativeSupport']
        #t10close = t10t['close']
        #t10open = t10t['open']
        #t10low = t10t['low']
        #t1052h = t10t['fiftyTwoWkHigh']
        #t1052l = t10t['fiftyTwoWkLow']
        #t10vol = round(float(t10t['volume'])*0.000001,ndigits=2)#million


        #t10v = t10['values']
        #t10week = t10v['weeksPrice']
        #t10hist = t10v['historyPrice']
        #t10lpch = round(float(t10v['lastChangeRatio'])*100,ndigits=2)
        view = disnake.ui.View()


        await interaction.edit_original_message(view=view)


    @analysis.sub_command(guild_ids=[888488311927242753])
    async def finscreen(self,inter:disnake.ApplicationCommandInteraction, pattern: str = commands.Param(name="pattern", choices=["channeldown", "channelup", "wedgeup", "wedgedown", "wedgeresistance", "wedgesupport", "tlsupport", "tlresistance", "doublebottom", "doubletop", "headandshoulders", "headandshouldersinv"]), direction: str = commands.Param(name="direction", choices=["u", "d"]), rsi: str = commands.Param(name="rsi_type", choices=["os30", "os20", "ob60", "ob70"]), new_20d_high_or_low: str = commands.Param(name="new_20d_high_or_low", choices=["nh", "nl"])):
        """🔎Use the FinViz screener and customize your options."""
        url = f"https://finviz.com/screener.ashx?v=111&f=ta_gap_{direction},ta_highlow20d_{new_20d_high_or_low},ta_pattern_{pattern},ta_rsi_{rsi}&ft=3&ar=180"
        embed = disnake.Embed(title="Results:",description=f"```py\nGaps {direction} with {pattern} with the rsi at {rsi} with a 20-day {new_20d_high_or_low} \n\n (NH = NEW HIGH) \n\n (NL = NEW LOW)```", color=disnake.Colour.random(), url=f"{url}")
        embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        await inter.response.send_message(embed=embed, ephemeral=True)


    @analysis.sub_command()
    async def gaps_down(self,inter: disnake.ApplicationCommandInteraction, percent):
        """🔎Returns a link to tickers with % gap down that you chooose."""
        url = f"https://finviz.com/screener.ashx?v=111&f=ta_gap_d{percent}&ft=3"
        embed = disnake.Embed(title=f"Tickers that have gapped down {percent}%.", url=f"https://finviz.com/screener.ashx?v=111&f=ta_gap_d{percent}&ft=3", color=disnake.Colour.dark_green())
        embed.add_field(name="Results", value=url)
        embed.set_footer(text="Implemented by FUDSTOP Trading")
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        await inter.response.send_message(embed=embed, ephemeral=True)

    @analysis.sub_command()
    async def gaps_up(self,inter: disnake.ApplicationCommandInteraction, percent):
        """🔎Returns a link to tickers with % gap up that you chooose."""
        url = f"https://finviz.com/screener.ashx?v=111&f=ta_gap_u{percent}&ft=3"
        embed = disnake.Embed(title=f"Tickers that have gapped up {percent}%.", url=f"https://finviz.com/screener.ashx?v=111&f=ta_gap_u{percent}&ft=3", color=disnake.Colour.dark_red())
        embed.add_field(name="Results", value=url)
        embed.set_footer(text="Implemented by FUDSTOP Trading")
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        await inter.response.send_message(embed=embed, ephemeral=True)

    @analysis.sub_command()
    async def overbought_gap(self,inter: disnake.ApplicationCommandInteraction):
        """🔎Returns a link to tickers that are overbought, gapped up, and are in a downward channel."""
        url = "https://finviz.com/screener.ashx?v=111&f=ta_gap_u,ta_pattern_channeldown,ta_rsi_ob70&ft=3"
        embed = disnake.Embed(title="Tickers that gapped up, have an overbought RSI (70+) and are in a downward channel.", description=f"{url}", color=disnake.Color.dark_red())
        embed.set_footer(text="Implemented by FUDSTOP Trading")
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        await inter.response.send_message(embed=embed, ephemeral=True)


    @analysis.sub_command()
    async def topshorts(self,inter: disnake.ApplicationCommandInteraction):
        """🔎Returns tickers with over 30% short interest"""
        url = "https://finviz.com/screener.ashx?v=111&s=ta_topgainers&f=sh_short_o30"
        embed = disnake.Embed(title="Top Shorts  with over 30% Short Interest", description=f"{url}", color=disnake.Colour.green())
        embed.set_footer(text="Implemented by FUDSTOP Trading")
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        await inter.response.send_message(embed=embed, ephemeral=True)
    


    @analysis.sub_command()
    async def rating(self,inter:disnake.AppCmdInter, stock: str=commands.Param(autocomplete=ticker_autocomp)):
        """🔎Returns the buy / sell / or hold ratings for a ticker"""
        await inter.response.defer(with_message=True, ephemeral=True)
        wbb = webull.webull()

        wbdata = wbb.get_analysis(stock=f"{stock}")
        rating = wbdata['rating']

        analysistotals = str(rating['ratingAnalysisTotals'])#42


        analysis = rating['ratingAnalysis']
        print(analysis)
        spread = rating['ratingSpread']
        under = spread['underPerform']
        buy = spread['buy']
        sell = spread['sell']
        strong = spread['strongBuy']
        #hold = spread['hold']

        target = wbdata['targetPrice']
        low = target['low']
        high = target['high']
        current = target['current']
        mean = target['mean']
        em = disnake.Embed(title=f"Rating Analysis for {stock}", description=f"```py\nTotal Analysts: {analysistotals}\n\nOverall Analysis: {analysis}``` ```py\nTarget Prices:\n\nLow: ${low} High: ${high} Current: ${current} Mean: ${mean}.```", color=disnake.Colour.dark_blue())
        em.add_field(name="Buy:", value=f"```py\n{buy}```", inline=True)
        em.add_field(name="Strong Buy:", value=f"```py\n{strong}```", inline=True)
        em.add_field(name="Sell:", value=f"```py\n{sell}```", inline=True)
        em.add_field(name="Underperform:", value=f"```py\n{under}```", inline=False)
        await inter.edit_original_message(embed=em)
def setup(bot):
    """SETUP COG"""
    bot.add_cog(Analysis(bot))
    print(f"> Extension {__name__} is ready\n")