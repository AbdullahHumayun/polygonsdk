"""COG"""
import disnake
from disnake.ext import commands
from autocomp import definitions_autocomp, tools_autocomp, data_autocomp
from views.learnviews import NotesView
from views.learnviews import RepoView,MoneySupplyView,IncomeExpendituresView
from views.learnviews import InflationView,SP500View,GrowthView,HelperView,TraderToolsView
from views.learnviews import BigMacView,DebtView,InterestRateView,CFTCView,SECView
from views.learnviews import UnemploymentView,EconomicIndicatorsView,FuturesView
from views.learnviews import BitcoinView,UsefulLinksView,DictView,MarketGlossaryView
from views.learnviews import FudstopCommandsView
from utils.lists_and_dicts import definitions
class Discord(commands.Cog):
    """Discord Cog"""
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def discord(self, inter):
        """Discord slash commands category."""

    @discord.sub_command()
    async def cmd(inter:disnake.AppCmdInter,category: str=commands.Param(choices=["⚙️ Options Commands",
        "📈 Stock Commands",
        "🔍 Analysis Commands",
        "💵 Earnings Commands",
        "🧠 Learn Commands",
        "🤖Quant Data Commands",
        "📰 News Commands"])):
        """💦Returns a list of bots with
        commands that can be used in the server."""
        await inter.response.defer(with_message=True)
        if category == "📈 Stock Commands":
            await inter.edit_original_message("```py\n📈/stock commands are used to view important data metrics. Utilizes high-quality data from CBOE, iexcloud, and NASDAQ Datalink as well as Webull.\n\nClick a command below to have it automatically loaded in your command box. Make sure to use ALL CAPS if typing in a ticker.``` </stock capitalflow:1029251181987500134> | </stock orderflow:1029251181987500134> | </stock liquidity:1029251181987500134> | </stock criminals:1029251181987500134> \n\n </stock leverage:1029251181987500134> | </stock company_brief:1029251181987500134> | </stock insider_summary:1029251181987500134> | </stock institutions:1029251181987500134>",view=FudstopCommandsView())
        elif category == "💦 Stream Commands":
            await inter.edit_original_message("```py\n💦/stream commands are real-time data commands that run for a moment before becoming static. Choose from options data, stock price data, crypto coin streams, double-quoting, and more.n\nClick a command below to have it automatically loaded in your command box. Make sure to use ALL CAPS if typing in a ticker. ``` </stream time_and_sales:1034275861865705478> | </stream crypto:1034275861865705478> | </stream double_crypto:1034275861865705478> | </stream double_quote:1034275861865705478> \n\n </stream topvolume:1034275861865705478> |  | </analysis newhigh:1025074283942248481> | </analysis gaps_up:1025074283942248481> | </analysis gaps_down:1025074283942248481>",view=FudstopCommandsView())
        elif category =="🔍 Analysis Commands":
            await inter.edit_original_message("```py\n🔍/analysis commands are used to identify specific criteria market-wide, such as technical patterns, screeners, and analyst ratings.\n\nClick a command below to have it automatically loaded in your command box. Make sure to use ALL CAPS if typing in a ticker. ``` </analysis all_52s:1025074283942248481> | </analyst:1026367610708832328> | </analysis finscreen:1025074283942248481> | </analysis topshorts:1025074283942248481> \n\n </analysis newlow:1025074283942248481> </analyst:1026367610708832328> | </analysis newhigh:1025074283942248481> | </analysis gaps_up:1025074283942248481> | </analysis gaps_down:1025074283942248481>",view=FudstopCommandsView())
        elif category == "💵 Earnings Commands":
            await inter.edit_original_message("```py\n💵/earnings commands are used to find earnings dates, earnings crush, earnings projections, earnings performance, and company financials.\n\nClick a command below to have it automatically loaded in your command box. Make sure to use ALL CAPS if typing in a ticker.```</earnings upcoming:1026367610708832327> | </earnings crush:1026367610708832327> | </earnings projection:1026367610708832327>",view=FudstopCommandsView())
        elif category == "⚙️ Options Commands":
            await inter.edit_original_message("```py\n⚙️/options commands commands can be used to analyze options in real-time from a premium perspective, volume perspective, flow perspective, and much more!\n\nClick a command below to have it automatically loaded in your command box. Make sure to use ALL CAPS if typing in a ticker.```  </options top_active:1034727628902498335> | </options highest_stats:1034727628902498335> | </options oi_increase:1034727628902498335> |  \n\n </options top_iv:1034727628902498335> | </options unusual:1034727628902498335>",view=FudstopCommandsView())
        elif category == "🧠 Learn Commands":
            await inter.edit_original_message("```py\n🧠/learn commands are used to help get the user up to speed with several topics - including discord, market research, discord setup, discord tutorials, youtube videos, technical indicators, and more. Also - be sure to check out the <#1016105093269045289>!\n\nClick a command below to have it automatically loaded in your command box. Make sure to use ALL CAPS if typing in a ticker.``` </learn core_logic:1026367610708832329> | </learn discord:1026367610708832329> | </learn options_101:1026367610708832329> | </learn calls:1026367610708832329> \n\n </learn etfs:1026367610708832329> | </learn covered_calls:1026367610708832329> | </learn china:1026367610708832329> | </learn filings:1026367610708832329>",view=FudstopCommandsView())
        elif category == "📰 News Commands":
            await inter.edit_original_message("```py\n📰 /news commands can be used to gather recent headlines to assess the current news narrative. Remember - news is best used as an indicator rather than taking what they say at face value. Often times - news articles are released to manipulate the viewer. Always approach news with a skeptical mindset.\n\nClick a command below to have it automatically loaded in your command box. Make sure to use ALL CAPS if typing in a ticker.``` </news announcement:1034275861941211158> | </news headlines:1034275861941211158> | </news narrative:1034275861941211158> | </learn calls:1026367610708832329> \n\n",view=FudstopCommandsView())
        elif category == "🤖Quant Data Commands":
            await inter.edit_original_message("```py\nQuant Data is a very nice bot that has a lot of useful commands. Try some out!``` ```py\n For Dividend Commands:``` </dividends today:911140318118838276> | </dividends tomorrow:911140318118838276> | </dividends date:911140318118838276> | </dividends ticker:911140318118838276> | </dividends calendar:911140318118838276> ```py\n /fib <ticker> <timeframe>``` </fib:910724015541334088> ```py\nEarnings Commands:``` </earnings calendar:911140318118838277> | </earnings ticker:911140318118838277> | </earnings date:911140318118838277> ```py\nFor FED Reserve Events:``` </federal-reserve today:1002066714198024197> </federal-reserve calendar:1002066714198024197> ```py\nSec Filings:``` </sec-filings:1002066714198024198>",view=FudstopCommandsView())
            await inter.send("```py\nOptions Commands:``` </flow:910724015490998293> | </stats contract:911140318118838274> | </stats market:911140318118838274> | </stats ticker:911140318118838274>",view=FudstopCommandsView())          
    @discord.sub_command()
    async def notes(self, inter:disnake.ApplicationCommandInteraction):
        """⚙️Shortcut to the FUDSTOP Notes section in /fudstop"""
        await inter.response.defer(with_message=True)
        embed = disnake.Embed(title="Important NOTES", color=disnake.Colour.random())
        embed.set_footer(text="Implemented by FUDSTOP Trading")
        await inter.edit_original_message(embed=embed, view=NotesView())

    @discord.sub_command()
    async def define(self, inter:disnake.AppCmdInter, term: str=commands.Param(autocomplete=definitions_autocomp)):
        """⚙️Start typing and learn what your heart desires"""
        await inter.response.defer(with_message=True)
        link = definitions[term]
        emb = disnake.Embed(title=f"Market Glossary - {term}", description=f"{link}", color=disnake.Colour.random())
        emb.set_footer(text="Implemented by FUDSTOP Trading")

        await inter.edit_original_message(embed=emb, view=DictView())



    @discord.sub_command()
    async def tools(self, inter: disnake.AppCmdInter, tools: str = commands.Param(autocomplete=tools_autocomp)):
        """⚙️Shortcut to the FUDSTOP Tools Menu"""
        await inter.response.defer(with_message=True)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", color = disnake.Colour.random())
        embed.set_thumbnail(
            url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(
            icon_url=
            "https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif",
            text="Implemented by Fudstop Trading")
        if tools == "Useful Links🔗":
            await inter.edit_original_message(embed=embed, view=UsefulLinksView())
        elif tools == "Trader Tools🛠️":
            await inter.edit_original_message(view=TraderToolsView())
        elif tools == "Market Glossary📖":
            await inter.edit_original_message(view=MarketGlossaryView())

    @discord.sub_command()
    async def data(self, inter: disnake.AppCmdInter,
    data: str = commands.Param(autocomplete=data_autocomp)):
        """⚙️Shortcut to the FUDSTOP Data Menu"""
        await inter.response.defer(with_message=True)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", color = disnake.Colour.random())
        embed.set_thumbnail(
        url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(
        icon_url=
        "https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif",
        text="Implemented by Fudstop Trading")
        if data == "SP500":
            await inter.edit_original_message(embed=embed, view=SP500View())

        elif data == "Inflation":
            await inter.edit_original_message(embed=embed, view=InflationView())

        elif data == "Unemployment":
            await inter.edit_original_message(embed=embed, view=UnemploymentView())

        elif data == "BigMac":
            await inter.edit_original_message(embed=embed, view=BigMacView())

        elif data=="Repo":
            await inter.edit_original_message(embed=embed, view=RepoView())

        elif data =="IncomeExpenditures":
            await inter.edit_original_message(embed=embed, view=IncomeExpendituresView())

        elif data =="Debt":
            await inter.edit_original_message(embed=embed, view=DebtView())

        elif data =="EconomicIndicators":
            await inter.edit_original_message(embed=embed, view=EconomicIndicatorsView())

        elif data =="MoneySupply":
            await inter.edit_original_message(embed=embed, view=MoneySupplyView())

        elif data =="Growth":
            await inter.edit_original_message(embed=embed, view=GrowthView())

        elif data =="InterestRate":
            await inter.edit_original_message(embed=embed, view=InterestRateView())

        elif data =="Futures":
            await inter.edit_original_message(embed=embed, view=FuturesView())

        elif data =="Bitcoin":
            await inter.edit_original_message(embed=embed, view=BitcoinView())

        elif data =="SEC":
            await inter.edit_original_message(embed=embed, view=SECView())

        elif data =="CFTC":
            await inter.edit_original_message(embed=embed, view=CFTCView())





    @discord.sub_command()
    async def help_me(self,inter:disnake.AppCmdInter):
        """⚙️Quick shortcut to the help menu for discord."""
        await inter.response.defer(with_message=True,ephemeral=False)
        await inter.edit_original_response(view=HelperView())


    @discord.sub_command(name="avatar", guild_ids=[888488311927242753])  # optional
    async def user_avatar(self, inter: disnake.ApplicationCommandInteraction, user: disnake.User):
        """⚙️Get a closer look at our friends in discord!"""
        await inter.response.defer(with_message=True)
        emb = disnake.Embed(title=f"{user}'s avatar")
        emb.set_image(url=user.display_avatar.url)
        emb.set_footer(text="Implemented by FUDSTOP Trading")
        emb.set_thumbnail(
        url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        await inter.edit_original_response(embed=emb)


async def setup(bot: commands.Bot):
    """SETUP COG"""
    await bot.add_cog(Discord(bot))
    print(f"> Extension {__name__} is ready\n")
