"""SCHOOL COG"""
from time import sleep
import disnake
from disnake.ext import commands
from views.learnviews import TechView
from views.learnviews import WebullTAView,WebullETFView
from views.learnviews import TimeRelatedDropdown








class School(commands.Cog):
    """MAIN CLASS"""
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def school(self, inter):
        """PARENT"""





    @school.sub_command()
    async def tech_analysis(self,inter:disnake.AppCmdInter):
        """🏫Learn about Technical Analysis"""
        await inter.response.defer(with_message=True,ephemeral=False)
        emb = disnake.Embed(title="Technical Analysis",
        description="```py\nClick the buttons below to learn about Technical Analysis.```",
        color=disnake.Colour.random())
        await inter.edit_original_response(embed=emb, view=WebullTAView())


    @school.sub_command()
    async def patterns(self,inter:disnake.AppCmdInter):
        """🏫Learn about candlestick patterns"""
        await inter.response.defer(with_message=True,ephemeral=False)
        emb = disnake.Embed(title="Candlestick Patterns",
        description="```py\nChoose a pattern from the dropdown to visualize it"
        "as well as recieve an explanation.```",
        color=disnake.Colour.random())
        await inter.edit_original_response(embed=emb, view=TechView())



    @school.sub_command()
    async def etfs(self, inter:disnake.AppCmdInter):
        """🏫Learn about Exchange Traded Funds"""
        await inter.response.defer(ephemeral=False)
        sleep(0.3)
        emb = disnake.Embed(title="Exchange Traded Funds",
        description="```py\nClick the buttons below to learn more about ETFs.```",
        color=disnake.Colour.dark_blue(),
        url="https://www.webull.com/learn/MKieXQ/dTCNgc/What-Is-An-ETF")
        emb.set_image(
            url="https://u1sweb.webullfinance.com/social/4cbadac7d4fd4c8ca442b3fcbced227d.png")
        await inter.edit_original_response(embed = emb, view=WebullETFView())


    @school.sub_command()
    async def time(self, inter:disnake.AppCmdInter):
        """🏫Learn about time-related events and historic dates."""
        await inter.response.defer(with_message=True, ephemeral=False)
        view = disnake.ui.View()
        view.add_item(TimeRelatedDropdown())
        await inter.edit_original_response(view=view)


def setup(bot:commands.Bot):
    bot.add_cog(School(bot))
    print(f"> Extension {__name__} is ready\n")