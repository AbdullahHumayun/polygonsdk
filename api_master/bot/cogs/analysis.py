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