"""WEBULL COG"""
from disnake.ext import commands

import pyEX as p
import disnake
from utils.lists_and_dicts import pics_list
from _discord import emojis as e
from views.learnviews import OptionsPaperView,OrderView,ChainView,CustomizeView, AnalysisView
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
from autocomp import tickerlist_autocomp, graphics_autocomp

intents = disnake.Intents.all()
from cfg import YOUR_API_KEY
webull_sdk = AsyncWebullSDK()
polygon_sdk = AsyncPolygonSDK(YOUR_API_KEY)

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
    async def volume_analysis(self, inter: disnake.MessageCommandInteraction, ticker:str=commands.Param(autocomplete=tickerlist_autocomp)):
        """Stream Volume Analysis for 30 Seconds"""
        counter=0
        await inter.send(f"-")
        while True:
            
            counter=counter+1
            vol_analysis_data = await webull_sdk.get_webull_vol_analysis_data(ticker)


            buyvol = float(vol_analysis_data.buyVolume)
            sellvol = float(vol_analysis_data.sellVolume)
            neutvol = float(vol_analysis_data.nVolume)
            avg_price_traded = float(vol_analysis_data.avePrice)
            total = float(vol_analysis_data.totalVolume)
            buyPct = (buyvol / total) * 100
            sellPct = (sellvol / total) * 100
            nPct = (neutvol / total) * 100

            if buyPct >= sellPct and buyPct >= nPct:
                color = disnake.Colour.dark_green()

            if sellPct >= buyPct and sellPct >= nPct:
                color = disnake.Colour.dark_red()
            else:
                color = disnake.Colour.darker_gray()
            embed = disnake.Embed(title=f"Volume Analysis - Webull", description=f"```py\nViewing live volume analysis data for {ticker}.```", color=color)
            embed.add_field(name=f"Volume Analysis:", value=f"> {e.greenfire} Buy: **{buyvol:,}**\n> {e.greyfire} Neut: **{neutvol:,}**\n> {e.redfire} Sell: **{sellvol:,}**\n> {e.movers} Total: **{total:,}**", inline=False)
            embed.add_field(name=f"Volume Percentile:", value=f"> {e.greenfire} Buy: **{round(float(buyPct),2)}%**\n> {e.greyfire} Neut: **{round(float(nPct),2)}%**\n> {e.redfire} Sell: **{round(float(sellPct),2)}%**", inline=False)
            embed.add_field(name=f"Avg. Price Traded:", value=f"> **{e.redline}** **${avg_price_traded}**", inline=False)
            embed.set_footer(text=f"{counter} | Implemented by FUDSTOP")
            embed.set_thumbnail(await polygon_sdk.get_polygon_logo(ticker))
            await inter.edit_original_message(embed=embed)
            if counter ==100:
                view = disnake.ui.View()
                button = disnake.ui.Button(style=disnake.ButtonStyle.red, emoji=f"{e.confirmed}", label=f"RUN", custom_id="run button")
                
                view.add_item(button)
                button.callback = lambda inter: self.volume_analysis(inter, ticker)
                await inter.send(embed=embed, view=view)
                await inter.delete_original_message()
                break

def setup(bot:commands.Bot):
    bot.add_cog(Webull(bot))
    print(f"> Extension {__name__} is ready\n")