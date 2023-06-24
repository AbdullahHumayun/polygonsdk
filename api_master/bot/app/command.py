import disnake
from disnake.ext import commands
from views.learnviews import TrendDropdown,CandleDropdown,TechDropdown,TechDropdown2,OStratsView,TutorialsView,ccView,OrderView,ChinaOptView


from views.learnviews import OCCView,FINRAView,ETFView,VideoView


class Learn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def learn(self, inter):
        pass




    @learn.sub_command()
    async def china(inter:disnake.AppCmdInter):
        """🧠Learn About the China Transformation Opportunity"""
        await inter.response.defer(with_message=True, ephemeral=False)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"China Education  - Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed, view=ChinaOptView())


    @learn.sub_command()
    async def filings(inter:disnake.AppCmdInter):
        """🧠Learn about filings from self regulatory organizations."""
        await inter.response.defer(with_message=True, ephemeral=False)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"Intercontinental Exchange Filings  - Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed, view=VideoView())

    @learn.sub_command()
    async def etfs(inter:disnake.AppCmdInter):
        """🧠Learn all about ETFs"""
        await inter.response.defer(with_message=True, ephemeral=False)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"Learn about ETFs  - Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed, view=ETFView())


    @learn.sub_command()
    async def options_101(inter:disnake.AppCmdInter):
        """🧠OIC Options 101 Course - Full"""
        await inter.response.defer(with_message=True, ephemeral=False)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"Options 101 Course Provided by the Options Industry Council  - Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed)

    @learn.sub_command()
    async def option_strategies(inter:disnake.AppCmdInter):
        """🧠Learn about differente Options Strategies"""
        await inter.response.defer(with_message=True, ephemeral=False)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"Learn About Different Options Strategies - Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed, view=OStratsView())

    @learn.sub_command()
    async def covered_calls(inter:disnake.AppCmdInter):
        """🧠Learn about the Covered Call Option Strategy"""
        await inter.response.defer(with_message=True, ephemeral=False)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"Learn the Covered Call Options Strategy - Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed,view=ccView())

    @learn.sub_command()
    async def core_logic(inter:disnake.AppCmdInter):
        """🧠Learn about the Core Logic"""
        await inter.response.defer(with_message=True, ephemeral=False)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"Learn About the Core Logic- Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        view = disnake.ui.View()
        view.add_item(disnake.ui.Button(style=disnake.ButtonStyle.url, label="🅰️LPHAQUERY", url=f"https://www.alphaquery.com/saved-screens"))
        view.add_item(disnake.ui.Button(style=disnake.ButtonStyle.url, label="🟢 Core Calls".center(1, " "), url=f"https://www.alphaquery.com/stock-screener/600010230?run=1"))
        view.add_item(disnake.ui.Button(style=disnake.ButtonStyle.url, label="🔴 Core Puts".center(1, " "), url=f"https://www.alphaquery.com/stock-screener/600010229?run=1"))
        await inter.edit_original_message(embed=embed, view=view)

    @learn.sub_command()
    async def calls(inter:disnake.AppCmdInter):
        """🧠Learn all about Call Options!"""
        await inter.response.defer(with_message=True, ephemeral=False)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"Learn About Calls", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed)

    @learn.sub_command()
    async def greeks(inter:disnake.AppCmdInter):
        """🧠Learn all about the Options Greeks"""
        await inter.response.defer(with_message=True, ephemeral=False)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"Learn about GAMMA / DELTA / RHO / VEGA and THETA - Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed)


    @learn.sub_command()
    async def discord(inter:disnake.AppCmdInter):
        """🧠Learn all about discord with these helpful tricks!"""
        await inter.response.defer(with_message=True, ephemeral=False)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"Learn About Calls", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed, view=TutorialsView())


    @learn.sub_command()
    async def order_types(inter:disnake.AppCmdInter):
        """🧠Learn about the different order types."""
        await inter.response.defer(with_message=True, ephemeral=False)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"Learn About Different Order Types - Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed, view=OrderView())

    @learn.sub_command()
    async def occ(inter:disnake.AppCmdInter):
        """🧠Learn about filings out of the Options Clearing Corporation"""
        await inter.response.defer(with_message=True, ephemeral=False)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"Options Clearing Corporation Filings - Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed, view=OCCView())


    @learn.sub_command()
    async def finra(inter:disnake.AppCmdInter):
        """🧠Learn about Filings out of FINRA"""
        await inter.response.defer(with_message=True, ephemeral=False)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"FINRA Filings - Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed, view=FINRAView())



    @learn.sub_command()
    async def webull_school(inter: disnake.AppCmdInter):
        """🧠Learn about the Webull APP and about Markets"""
        await inter.response.defer(with_message=True, ephemeral=False)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"Click the buttons below to learn about the Webull APP and about Markets in general!", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed)

    @learn.sub_command()
    async def nsfr_ratio(inter: disnake.AppCmdInter):
        """🧠Learn about the Webull APP and about Markets"""
        await inter.response.defer(with_message=True, ephemeral=False)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", description=f"FINRA Filings - Click the Buttons to View more Information", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        embed.add_field(name="Available Panels View", value="/learn")
        await inter.edit_original_message(embed=embed)
    
    
    @learn.sub_command()
    async def ta(inter: disnake.AppCmdInter):
        """📊Info-graphics on over 50 selectable Tech Patterns to learn about."""
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


async def setup(bot):
    bot.add_cog(Learn(bot))
    print(f"> Extension {__name__} is ready\n")
