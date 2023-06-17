import requests
import disnake
from disnake.ext import commands
from autocomp import tickerlist_autocomp
from utils.webull_tickers import ticker_list
from views.uiviews.capitalflow import CapitalFlow1
from views.uiviews.directiondrop import DirectionDropdown
from views.uiviews.financialselects import FinancialSelect
from views.uiviews.ftds import FTDStocksDropdown
from views.uiviews.lowfloat import LowFloatDropdown
from views.uiviews.quote import Quote
class AllInOne(commands.Cog):
    def __init__(self, bot):
        self.bot=bot


    @commands.slash_command()
    async def all_in_one(self, inter: disnake.AppCmdInter, ticker: str=commands.Param(autocomplete=tickerlist_autocomp)):

        """The all in one command."""
        await inter.response.defer(with_message=True)
        em = disnake.Embed(title="The All-In One Command", description="```py\nSymbol Explanations Below:```", color=disnake.Colour.dark_gold())
        embed2 = disnake.Embed(title="This is Page 2 of the Command",description=f"```py\nTESTING```",color=disnake.Colour.dark_blue())
        em.add_field(name="💸", value="```py\nFinancials```")
        em.add_field(name="⚙️", value="```py\nQuote Data```")
        em.add_field(name="📜", value="```py\nSEC Filings```")

        ids = ticker_list[ticker.upper()]
        view = disnake.ui.View()
        view2 = disnake.ui.View()
        view2.add_item(FinancialSelect(ticker=ticker))
        finbutt = disnake.ui.Button(style=disnake.ButtonStyle.green, label="💸",row=4)
        finbutt.callback= lambda interaction: interaction.response.edit_message(view=view2, embed=embed2)
        finbutt2 = disnake.ui.Button(style=disnake.ButtonStyle.green, label="💸",row=4)
        finbutt2.callback= lambda interaction: interaction.response.edit_message(view=view, embed=em)
        view2.add_item(finbutt2)
        view2.add_item(Quote(ticker=ticker))
        #view2.add_item(GainersDropdown())
        #view2.add_item(LosersDropdown())
        view.add_item(CapitalFlow1(ticker=ids))
        view.add_item(FTDStocksDropdown())
        view.add_item(DirectionDropdown())
        view2.add_item(LowFloatDropdown())
        view.add_item(finbutt)
        await inter.edit_original_response(view=view, embed=em)


def setup(bot):
    """Social Setup"""
    bot.add_cog(AllInOne(bot))
    print(f"> Extension {__name__} is ready\n")

