import disnake
from disnake.ext import commands
from views.learnviews import CoreView, CallView,OCCView,GreeksView,OStratsView,VideoView,LearnView,FINRAView,ChinaOptView,OrderView,ccView,ETFView,Opt101View
from views.learnviews import TechDropdown, TechDropdown2, CandleDropdown,TrendDropdown
from views.learnviews import TutorialsView, CriteriaView


class Learn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def learn(self, inter):
        """Learn slash commands category."""
        pass




    @learn.sub_command()
    async def china(inter:disnake.AppCmdInter):
        """🧠Learn About the China Transformation Opportunity"""
        await inter.response.defer(with_message=True)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"China Education  - Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed, view=ChinaOptView())


    @learn.sub_command()
    async def filings(inter:disnake.AppCmdInter):
        """🧠Learn about filings from self regulatory organizations."""
        await inter.response.defer(with_message=True)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"Intercontinental Exchange Filings  - Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed, view=VideoView())

    @learn.sub_command()
    async def etfs(inter:disnake.AppCmdInter):
        """🧠Learn all about ETFs"""
        await inter.response.defer(with_message=True)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"Learn about ETFs  - Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed, view=ETFView())


    @learn.sub_command()
    async def options_101(inter:disnake.AppCmdInter):
        """🧠OIC Options 101 Course - Full"""
        await inter.response.defer(with_message=True)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"Options 101 Course Provided by the Options Industry Council  - Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed, view=Opt101View())

    @learn.sub_command()
    async def option_strategies(inter:disnake.AppCmdInter):
        """🧠Learn about differente Options Strategies"""
        await inter.response.defer(with_message=True)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"Learn About Different Options Strategies - Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed, view=OStratsView())

    @learn.sub_command()
    async def covered_calls(inter:disnake.AppCmdInter):
        """🧠Learn about the Covered Call Option Strategy"""
        await inter.response.defer(with_message=True)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"Learn the Covered Call Options Strategy - Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed,view=ccView())

    @learn.sub_command()
    async def core_logic(inter:disnake.AppCmdInter):
        """🧠Learn about the Core Logic"""
        await inter.response.defer(with_message=True)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"Learn About the Core Logic- Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed, view=CoreView())

    @learn.sub_command()
    async def calls(inter:disnake.AppCmdInter):
        """🧠Learn all about Call Options!"""
        await inter.response.defer(with_message=True)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"Learn About Calls", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed, view=CallView())

    @learn.sub_command()
    async def greeks(inter:disnake.AppCmdInter):
        """🧠Learn all about the Options Greeks"""
        await inter.response.defer(with_message=True)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"Learn about GAMMA / DELTA / RHO / VEGA and THETA - Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed, view=GreeksView())


    @learn.sub_command()
    async def discord(inter:disnake.AppCmdInter):
        """🧠Learn all about discord with these helpful tricks!"""
        await inter.response.defer(with_message=True)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"Learn About Calls", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed, view=TutorialsView())


    @learn.sub_command()
    async def order_types(inter:disnake.AppCmdInter):
        """🧠Learn about the different order types."""
        await inter.response.defer(with_message=True)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"Learn About Different Order Types - Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed, view=OrderView())

    @learn.sub_command()
    async def occ(inter:disnake.AppCmdInter):
        """🧠Learn about filings out of the Options Clearing Corporation"""
        await inter.response.defer(with_message=True)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"Options Clearing Corporation Filings - Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed, view=OCCView())


    @learn.sub_command()
    async def finra(inter:disnake.AppCmdInter):
        """🧠Learn about Filings out of FINRA"""
        await inter.response.defer(with_message=True)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"FINRA Filings - Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed, view=FINRAView())



        
    @learn.sub_command()
    async def criteria(inter:disnake.AppCmdInter):
        em = disnake.Embed(title="Criteria for Core", description="```py\nThe core logic has specific criteria for identifying play candidates.```", color=disnake.Colour.dark_red())
        em.add_field(name="Criteria:", value="```py\nGaps, earnings, low iv, broken RSI, and MACD Banana - as well as what to avoid and when to exit - are the gist of core. Select a button below to view the criteria.```")
        await inter.send(embed=em,view=CriteriaView())


    @learn.sub_command()
    async def nsfr_ratio(inter: disnake.AppCmdInter):
        """🧠Learn about the Webull APP and about Markets"""
        await inter.response.defer(with_message=True)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"FINRA Filings - Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed, view=LearnView())
    
    
    @learn.sub_command()
    async def ta(inter: disnake.AppCmdInter):
        """🧠Info-graphics on over 50 selectable Tech Patterns to learn about."""
        view = disnake.ui.View()
        view.add_item(TechDropdown())
        view.add_item(TechDropdown2())
        embed = disnake.Embed(title=f"Choose a Pattern Below", color=disnake.Colour.dark_gold())
        embed.set_image(url="https://assets.winton.com/cms/Images/longer-view/Technical-Analysis/TechAn4.gif")
        await inter.send(embed=embed, view=view)

    @learn.sub_command()
    async def candle_patterns(inter:disnake.AppCmdInter):
        """🧠Choose from candles and trend info-graphics to learn about."""
        view = disnake.ui.View()
        view.add_item(CandleDropdown())
        view.add_item(TrendDropdown())
        await inter.send("```py\nLearn Candle Patterns and Trends```", view=view)

async def setup(bot:commands.Bot):
    """SETUP"""
    await bot.add_cog(Learn(bot))
    print(f"> Extension {__name__} is ready\n")