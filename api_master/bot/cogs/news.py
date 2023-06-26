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

    
    #@commands.cooldown(1, 86400, commands.BucketType.user)
    @news.sub_command()
    async def headlines(interaction:disnake.ApplicationCommandInteraction, symbol: str = commands.Param(autocomplete=ticker_autocomp)):
        """🌐Returns the latest headlines for a given ticker."""
        await interaction.response.defer(with_message=True, ephemeral=True)
        stock = finviz.get_news(f"{symbol}")
        today = date.today()
        index = stock[0]
        latest= stock[0]
        headline = stock[1]
        link = stock[2]
        embed = disnake.Embed(title=f"Latest headline for {symbol}:", description=f"{headline} \n\n {link}", colour=disnake.Colour.dark_gold())
        embed.add_field(name="Time Headline Published:", value=f"{latest}")
        await interaction.edit_original_message(embed=embed)
    


    @news.sub_command()
    async def narrative(inter: disnake.AppCmdInter, symbol: str = commands.Param(autocomplete=ticker_autocomp)):
        """🌐Returns the latest news headline, psyop picture, and summary for a stock."""
        await inter.response.defer(with_message=True, ephemeral=True)
        r = requests.get(url=f"https://workspace.iex.cloud/v1/data/CORE/NEWS/{symbol}/?token={YOUR_IEX_CLOUD_KEY}&last=10")
        d = r.json()
        index = d[0]
        headlines = index['headline']
        imageurls = index['imageUrl']
        summarys = index['summary']
        headline = [i['headline'] for i in d]
        imageurl = [i['imageUrl'] for i in d]
        summary = [i['summary'] for i in d]

        urls = index['url']
        em = disnake.Embed(title=f"Narrative Check for {symbol}", description=f"```py\nHeadline:``` ```py\n{headlines}```",url=urls, color=disnake.Colour.dark_gold())
        em.add_field(name=f"Summary:", value=f"{summarys}") 
        em.set_thumbnail(url=f"{imageurls}")
        em.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading, Data Provided By Apperate")
        await inter.edit_original_message(embed=em)


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