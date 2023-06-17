import disnake
from disnake.ext import commands
import requests
from time import sleep
import webull



class Scan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command()
    async def scan(self, inter):
        """Scan slash commands category."""
        pass

    @scan.sub_command()
    async def ssr(interaction:disnake.AppCmdInter):
        """☢️Find a Stock based on its' % change for the day."""
        await interaction.response.defer(with_message=True)
        wb = webull.webull()
        d = wb.get_all_tickers()
        for i in d:
            tickerid = i.get('tickerId')
            name = i.get('name')
            symbol = i.get('symbol')
            close = i.get('close')
            changer = i.get('changeRatio')
            changef = float(changer)
            change = round(changef*100,ndigits=2)
            vol = i.get('volume')
            volf = float(vol)
            volr = round(volf*0.000001, ndigits=2)
            em = disnake.Embed(title="Conditionals - Tickers > 5M Volume:", description=f"Scanning . . . . \n{name}", color=disnake.Colour.random(), url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids=913243251%2C950185252&includeSecu=1&delay=0&more=1")
            em.add_field(name="Results:", value=f"```py\n{symbol} Volume: {volr} million.```")
            em.add_field(name="Volume and %Change on Day:", value=f"```py\n {change}% on the day```")
            if change <= -10:
                em.add_field(name="Results:", value=f"```py\n{symbol} Volume: {volr} million.```")
                await interaction.send(embed=em)
                sleep(5)


def setup(bot):
    bot.add_cog(Scan(bot))
    print(f"> Extension {__name__} is ready\n")
