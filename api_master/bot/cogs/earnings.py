"""EARNINGS COMMANDS"""
import disnake
from disnake.ext import commands
import requests
from requests.auth import HTTPBasicAuth

from autocomp import ticker_autocomp

intents = disnake.Intents.all()

class Earnings(commands.Cog):
    """COG"""
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def earnings(self, inter):

        """
        >>> Earnings Commands Category 
        
        """

    
    @earnings.sub_command()
    async def upcoming(self,inter: disnake.AppCmdInter, date):
        """💸Type in a date: YYYY-MM-DD to return earnings for that date."""
        await inter.response.defer(with_message=True, ephemeral=False)
        rup = requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/explore/calendar/earnings?regionId=6&pageIndex=1&pageSize=100&startDate={date}")
        dup = rup.json()
        data = dup['data']
        #values = [dup['values'] for dup in data]
        ticker = [dup['ticker'] for dup in data]
        dater1 = ''.join(f"**{i['symbol']}**, " for i in ticker)
        dater2 = '\n\n'.join(f"{i['symbol']} " for i in ticker)
        embed1 = disnake.Embed(title=f"Upcoming earnings for {date}", description=f"READABLE FORMAT \n **{dater2}**", url="https://www.alphaquery.com/table",color=disnake.Colour.random())
        embed = disnake.Embed(title=f"Upcoming earnings for {date}", description=f"**SYMBOL WITH EARNINGS ON {date}. COPY/PASTE THESE INTO ALPHAQUERY FOR EASY ANALYSIS. \n\n {dater1}**", url="https://www.alphaquery.com/table",color=disnake.Colour.greyple())
        button = disnake.ui.Button(label="Alphaquery Format", style = disnake.ButtonStyle.blurple)
        button1 = disnake.ui.Button(label="Readable Format (mobile)", style = disnake.ButtonStyle.red)
        button.callback = lambda interaction: interaction.response.edit_message(embed=embed, view=view)
        button1.callback = lambda interaction: interaction.response.edit_message(embed=embed1, view=view)
        view = disnake.ui.View()
        view.add_item(button)
        view.add_item(button1)
        embed.set_footer(text="Data Provided by Financial Modeling Prep and Implemented by FUDSTOP Trading.", icon_url="https://uploads-ssl.webflow.com/62661f74776abb77ef7621a8/6272ac0a541297826e1a5209_963244979063517184.gif")
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed1.set_footer(text="Data Provided by Financial Modeling Prep and Implemented by FUDSTOP Trading.", icon_url="https://uploads-ssl.webflow.com/62661f74776abb77ef7621a8/6272ac0a541297826e1a5209_963244979063517184.gif")
        embed1.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        await inter.edit_original_message(embed=embed1, view=view)

    # @earnings.sub_command()
    # async def crush(self, inter: disnake.AppCmdInter, ticker: str=commands.Param(autocomplete=ticker_autocomp)):
    #     """💸Returns the % IV expected to be lost after the next earnings report."""
    #     rcr = requests.get(url=f"https://data.nasdaq.com/api/v3/datasets/QOR/{ticker}/data.json?api_key={YOUR_NASDAQ_KEY}")
    #     dcr = rcr.json()
    #     dataset = dcr['dataset_data']
    #     data = dataset['data']
    #     values = data[0]
    #     ercrush = values[1] * 100
    #     erconv = round(100 - ercrush, ndigits=2)
    #     emb = disnake.Embed(title=f"Earnings Crush % Expected for {ticker}", description=f"{ticker}'s IV is expected to be crushed **{erconv}%** after earnings is released. The next ER report is scheduled for", color = disnake.Colour.dark_gold())
    #     emb.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
    #     emb.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
    #     await inter.response.send_message(embed=emb)

    # @crush.error
    # async def assetserror(self,inter: disnake.AppCmdInter, error):
    #     """ERROR HANDLING"""
    #     if isinstance(error, commands.CheckAnyFailure):
    #         await inter.send("```py\n Make sure you're using an ETF and that youre using all CAPS.```")

async def setup(bot: commands.Bot):
    """SETUP COG"""
    await bot.add_cog(Earnings(bot))
    print(f"> Extension {__name__} is ready\n")
