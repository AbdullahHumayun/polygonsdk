import disnake
from disnake.ext import commands
import requests
import finviz
from autocomp import ticker_autocomp


class Evaluate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command()
    async def analyst(self, interaction: disnake.ApplicationCommandInteraction, ticker: str=commands.Param(autocomplete=ticker_autocomp)):
        """Returns the latest analyst ratings for a given ticker."""
        stock = finviz.get_analyst_price_targets(ticker, last_ratings=25)
        items = '\n'.join(
            f"```py\n{i['date']} '{i['category']}' ANALYST: '{i['analyst']}' RATING: '{i['rating']}'```" for i in stock
        )
        embed = disnake.Embed(
            title=f"Analyst ratings for {ticker}",
            description=f"{items}",
            color=disnake.Colour.dark_theme()
        )
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1009552305869303828/1009555505699639366/ezgif-2-f4a5623248.gif")
        embed.set_footer(
            text="Implemented by FUDSTOP Trading.",
            icon_url="https://uploads-ssl.webflow.com/62661f74776abb77ef7621a8/6272ac0a541297826e1a5209_963244979063517184.gif"
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)


def setup(bot):
    bot.add_cog(Evaluate(bot))
    print(f"> Extension {__name__} is ready\n")