import disnake
from disnake.ext import commands
import requests


intents = disnake.Intents.all()
bot = commands.Bot( command_prefix="!", intents=intents)




PATTERNS = ["🐻Head and Shoulders🔴", "🐻STRONG Rising Wedge🔴", "🐻STRONG Rising Wedge & Overbought RSI🔴", "🐻STRONG Descending Triangle🔴", "🐻Double Top🔴",
"🐂Inverse Head and Shoulders🟢", "👑Channel", "👑Horizontal Channel", "🐂STRONG Rising Channel with RSI > 50🟢", "🐂Ascending Triangle🟢"]


class prices_and_technicals(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command()
    async def check(self, inter):
        pass
    


    @check.sub_command()
    async def all_52s(interaction:disnake.ApplicationCommandInteraction, type: str=commands.Param(name="type", choices=["nearHigh", "nearLow", "newHigh", "newLow"]), ):
        """Scan 52 week highs / lows + near high / near lows."""
        r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/wlas/ranking/52weeks?regionId=6&rankType={type}&pageSize=10&order=lastChangeRatio&direction=1")
        d = r.json()
        data = d['data']
        ticker = [d['ticker'] for d in data]
        items = '\n'.join(f"```py\n{i['name']}, {i['symbol']}, ${i['close']}```" for i in ticker)
        embed = disnake.Embed(title=f"Returned tickers that are {type}:", description=f"{items}", color=disnake.Colour.dark_theme())
        embed.set_thumbnail(url="https://i.ibb.co/vm0P0jW/ODLxwfPE.gif")
        embed.set_footer(text="Data Provided By Webull \n Implemented by FUDSTOP Trading -")
        await interaction.response.send_message(embed=embed, ephemeral=False)


def setup(bot:commands.Bot):
    bot.add_cog(prices_and_technicals(bot))
    print(f"> Extension {__name__} is ready\n")