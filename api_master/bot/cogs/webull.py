"""WEBULL COG"""
from datetime import timedelta
from datetime import date
import re
from disnake.ext import commands
import requests
import pyEX as p
import disnake
from utils.lists_and_dicts import pics_list
from utils.webull_tickers import ticker_list
from menus.menu import Menu

from views.learnviews import OptionsPaperView,OrderView,ChainView,CustomizeView, AnalysisView
from cfg import YOUR_RAPIDAPI_KEY
from autocomp import tickerlist_autocomp, graphics_autocomp

intents = disnake.Intents.all()




class Webull(commands.Cog):
    """WEBULL COG"""
    def __init__(self, bot):
        pass




    @commands.slash_command()
    async def webull(self,inter):
        """Webull slash commands category."""
        pass


    @webull.sub_command()
    async def graphics(inter:disnake.AppCmdInter, graphic: str=commands.Param(autocomplete=graphics_autocomp)):
        """🔥Returns Webull Gifs / PNGs of various market topics."""
        
        link = pics_list[graphic]
        em = disnake.Embed(title="Graphic Helpers", color=disnake.Colour.dark_gold())
        em.set_image(url=link)
        await inter.send(embed=em)



    @webull.sub_command()
    async def analysis_tools(self,inter: disnake.AppCmdInter):
        """🔥Learn Webull Analysis Tools"""
        await inter.response.defer(with_message=True)
        emb = disnake.Embed(title="Webull Analysis Tools")
        emb.set_footer(text="Implemented by FUDSTOP Trading", icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        emb.set_thumbnail(url="https://media.discordapp.net/attachments/1009552305869303828/1009555505699639366/ezgif-2-f4a5623248.gif")
        await inter.edit_original_message(embed=emb, view=AnalysisView())

    @webull.sub_command()
    async def paper_trading(self,inter: disnake.AppCmdInter):
        """🔥Learn about Webull OPTIONS Paper Trading"""
        await inter.response.defer(with_message=True)
        emb = disnake.Embed(title="Webull Analysis Tools")
        emb.set_footer(text="Implemented by FUDSTOP Trading", icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        emb.set_thumbnail(url="https://media.discordapp.net/attachments/1009552305869303828/1009555505699639366/ezgif-2-f4a5623248.gif")
        await inter.edit_original_message(embed=emb, view=OptionsPaperView())

    @webull.sub_command()
    async def options_setup(self,inter: disnake.AppCmdInter):
        """🔥Learn to customize the Options Chain"""
        await inter.response.defer(with_message=True)
        emb = disnake.Embed(title="Learn about customization in Webull.")
        emb.set_footer(text="Implemented by FUDSTOP Trading", icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        emb.set_thumbnail(url="https://media.discordapp.net/attachments/1009552305869303828/1009555505699639366/ezgif-2-f4a5623248.gif")
        await inter.edit_original_message(embed=emb, view=CustomizeView())

    @webull.sub_command()
    async def options_chain(self,inter: disnake.AppCmdInter):
        """🔥Learn about the Options Chain"""
        await inter.response.defer(with_message=True)
        emb = disnake.Embed(title="Learn about customization in Webull.")
        emb.set_footer(text="Implemented by FUDSTOP Trading", icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        emb.set_thumbnail(url="https://media.discordapp.net/attachments/1009552305869303828/1009555505699639366/ezgif-2-f4a5623248.gif")
        await inter.edit_original_message(embed=emb, view=ChainView())

    @webull.sub_command()
    async def orders(self,inter: disnake.AppCmdInter):
        """🔥Learn about order types."""
        await inter.response.defer(with_message=True)
        emb = disnake.Embed(title="Learn about order types.")
        emb.set_footer(text="Implemented by FUDSTOP Trading", icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        emb.set_thumbnail(url="https://media.discordapp.net/attachments/1009552305869303828/1009555505699639366/ezgif-2-f4a5623248.gif")
        await inter.edit_original_message(embed=emb, view=OrderView())

    @webull.sub_command()
    async def bid_ask_spread(self,inter: disnake.AppCmdInter):
        """🔥Returns the bid/ask spread for a ticker."""
        await inter.response.defer(with_message=True)
        emb = disnake.Embed(title="Learn about the bid ask spread.")
        emb.set_footer(text="Implemented by FUDSTOP Trading", icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        emb.set_thumbnail(url="https://media.discordapp.net/attachments/1009552305869303828/1009555505699639366/ezgif-2-f4a5623248.gif")
        await inter.edit_original_message(embed=emb, view=OrderView())


    @webull.sub_command()
    async def webull_quote(self,inter:disnake.AppCmdInter, ticker: str=commands.Param(autocomplete=tickerlist_autocomp)):
        """🔥Pulls webull data to discord in the form of price quote info."""
        await inter.response.defer(with_message=True)
        ids = ticker_list[ticker.upper()]
        quoter = requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={ids},&includeSecu=1&delay=0&more=1")
        quoted = quoter.json()
        index = quoted[0]
        #name=index["name"]
        #symbol=index["symbol"]
        dissymbol=index["disSymbol"]
        #disExchangeCode=index["disExchangeCode"]
        #exchangeCode=index["exchangeCode"]
        #listStatus=index["listStatus"]
        #template=index["template"]
        #derivativeSupport=index["derivativeSupport"]
        #tradeTime=index["tradeTime"]
        #status=index["status"]
        close=index["close"]
        #change=index["change"]
        #changeRatio=index["changeRatio"]
        #marketValue=index["marketValue"]
        #volume=index["volume"]
        #turnoverRate=index["turnoverRate"]
        #timeZone=index["timeZone"]
        #tzName=index["tzName"]
        #preClose=index["preClose"]
        #open=index["open"]
        high=index["high"]
        low=index["low"]
        vibrateratio=index["vibrateRatio"]
        #avgVol10D=index["avgVol10D"]
        #avgVol3M=index["avgVol3M"]
        #dealAmount=index["dealAmount"]
        negmarketvalue=index["negMarketValue"]
        #pe=index["pe"]
        #indicatedPe=index["indicatedPe"]
        #peTtm=index["peTtm"]
        #eps=index["eps"]
        #epsTtm=index["epsTtm"]
        #pb=index["pb"]
        #totalShares=index["totalShares"]
        #outstandingShares=index["outstandingShares"]
        #fiftyTwoWkHigh=index["fiftyTwoWkHigh"]
        #fiftyTwoWkLow=index["fiftyTwoWkLow"]
        #yields=index["yield"]
        #currencyCode=index["currencyCode"]
        #lotSize=index["lotSize"]
        #latestDividendDate=index["latestDividendDate"]
        #latestEarningsDate=index["latestEarningsDate"]
        #ps=index["ps"]
        #bps=index["bps"]
        #estimateEarningsDate=index["estimateEarningsDate"]
        #tradeStatus=index["tradeStatus"]
        view = disnake.ui.View()
        bu2 = disnake.ui.Button(label=f"SYMBOL: {dissymbol}", style = disnake.ButtonStyle.grey,row=0)
        bu3 = disnake.ui.Button(label=f"Vibration Ratio: {vibrateratio}", style = disnake.ButtonStyle.green,row=1)
        bu4 = disnake.ui.Button(label=f"Negative Mkt Value: {negmarketvalue}", style = disnake.ButtonStyle.red, row=1)
        bu5 = disnake.ui.Button(label=f"High on Day: ${high}", style = disnake.ButtonStyle.green,row=2)
        bu6 = disnake.ui.Button(label=f"Today's Open: ${open}", style = disnake.ButtonStyle.grey, row=2)
        bu7 = disnake.ui.Button(label=f"Low of Day: ${low}", style = disnake.ButtonStyle.red,row=2)
        bu8 = disnake.ui.Button(label=f"Current: ${close}", style = disnake.ButtonStyle.blurple, row=3)
        bu9 = disnake.ui.Button(label="PUSHING NEW HIGHS!!!", style = disnake.ButtonStyle.blurple, row=3)
        view.add_item(bu2)
        view.add_item(bu3)
        view.add_item(bu4)
        view.add_item(bu5)
        view.add_item(bu6)
        view.add_item(bu7)
        view.add_item(bu8)
        emb = disnake.Embed(title=f"Webull Data for {dissymbol}", color=disnake.Colour.dark_blue())
        if close > high:
            view.remove_item(bu5)
            view.add_item(bu9)
        emb.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        emb.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        await inter.edit_original_message(embed = emb, view=view)



def setup(bot):
    """SETUP COG"""
    bot.add_cog(Webull(bot))
    print(f"> Extension {__name__} is ready\n")
