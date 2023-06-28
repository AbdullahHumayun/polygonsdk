import disnake
from disnake.ext import commands
import requests
from autocomp import ticker_autocomp
import finviz
from datetime import date
import webull
from cfg import YOUR_IEX_CLOUD_KEY
intents = disnake.Intents.all()
bot = commands.Bot( command_prefix="!", intents=intents)





class News(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.slash_command()
    async def news(self, inter:disnake.AppCmdInter):
        """News slash commands category."""
        pass

    



    @news.sub_command()
    async def announcement(inter:disnake.AppCmdInter,stock:str=commands.Param(autocomplete=ticker_autocomp)):
        """🌐Returns the latest announcement for a company."""
        await inter.response.defer(with_message=True)
        wb = webull.webull()

        d = wb.get_press_releases(stock=f"{stock}")
        for i in d:
            try:
                ann = list(d['announcements'])
                index1 = ann[0]
                title = index1['title']
                publish = index1['publishDate']
                url = index1['htmlUrl']
                name = index1['typeName']
                form = index1['formType']
                em = disnake.Embed(title=f"Latest Announcement for {stock}", description=f"```py\nTitle: {title} Published: {publish}\n\nName: {name}\n\nForm: {form}```", color=disnake.Colour.dark_blue(), url=f"{url}")
                await inter.edit_original_message(embed=em)
            except IndexError:
                index1 = "N/A"
                await inter.edit_original_message("N/A")
def setup(bot:commands.Bot):
    bot.add_cog(News(bot))
    print(f"> Extension {__name__} is ready\n")