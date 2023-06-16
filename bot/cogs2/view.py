import disnake
from disnake.ext import commands
import requests
from autocomp import videos_autocomp
from views.learnviews import TechDropdown,TechDropdown2,SFTView,OCCView
from views.learnviews import ChinaView,DTCCView,ICEView,ETFView,NSCCView,FINRAView,Opt101View,TechView,NyseVIDView,CBOEView,NSFRView

class ViewCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command()
    async def view(self, inter):
        pass


    @view.sub_command()
    async def technical_pattern(inter:disnake.AppCmdInter):
        """👁️Returns an animated example + a link to a detailed explanation of technicals."""
        await inter.response.defer(with_message=True, ephemeral=True)
        view = disnake.ui.View()
        view.add_item(TechDropdown())
        view.add_item(TechDropdown2())
        await inter.edit_original_response(view=view)

    @view.sub_command()
    async def dictionary(inter:disnake.AppCmdInter, word):
        """👁️Define something! Enter a word to get the definition."""
        await inter.response.defer(with_message=True, ephemeral=True)
        raw = requests.get(f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key=c4695830-f1ab-4d67-a2ce-301bfd661c2d")
        d = raw.json()
        index1 = d[0]
        try:
            shortdef = index1['shortdef']
            em = disnake.Embed(title=f"{word}", description=f"```py\n{shortdef}")
            await inter.edit_original_message(embed=em)
        except KeyError:
            if shortdef is None:
                await inter.edit_original_message(f"```py\n {word} is not a word, dood.```")

    @view.sub_command
    async def videos(inter: disnake.AppCmdInter, videos: str = commands.Param(autocomplete=videos_autocomp)):
        """👁️View a plethora of topics of educational videos!"""
        await inter.response.defer(with_message=True, ephemeral=True)
        embed = disnake.Embed(title ="FUDSTOP Application Online🟢", color = disnake.Colour.random())
        embed.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        embed.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        if videos=="China Videos📹":
            await inter.edit_original_message(embed=embed, view=ChinaView())
            if videos=="NSCC Videos📹":
                await inter.edit_original_message(embed=embed, view=NSCCView())

            elif videos=="FINRA Videos📹":
                await inter.edit_original_message(embed=embed, view=FINRAView())

            elif videos=="OCC Videos📹":
                await inter.edit_original_message(embed=embed, view=OCCView())

            elif videos=="NYSE Videos📹":
                await inter.edit_original_message(embed=embed, view=NyseVIDView())

            elif videos=="DTCC Videos📹":
                await inter.edit_original_message(embed=embed, view=DTCCView())

            elif videos=="SFT Videos📹":
                await inter.edit_original_message(embed=embed, view=SFTView())

            elif videos=="NSFR Videos📹":
                await inter.edit_original_message(embed=embed, view=NSFRView())

            elif videos== "Options 101📹":
                await inter.edit_original_message(embed=embed, view=Opt101View())

            elif videos=="CBOE Videos📹":
                await inter.edit_original_message(embed=embed, view=CBOEView())

            elif videos=="ICE Videos📹":
                await inter.edit_original_message(embed=embed, view=ICEView())

            elif videos=="ETF Videos📹":
                await inter.edit_original_response(embed=embed, view=ETFView())

    @view.sub_command()
    async def markets(inter:disnake.AppCmdInter, market: str=commands.Param(choices=["Repo Market","Short Term Funding Market", "Corporate Bond Market", "Commercial Real Estate Market", "Leveraged Loans Market", "Resitential Mortgage Market", "Municipal Securities Market"])):
        """👁️View the ecosystem for several different Financial Markets."""
        await inter.response.defer(with_message=True, ephemeral=True)
        if market == "Repo Market":
            em = disnake.Embed(title="The Repo Market", description=f"```py\nTo learn more about this complex ecosystem - see URL in title.``` ```py\n The approximately $4 trillion repo market provides secured, short-term, marked-to-market funding against various forms of securities collateral.``` ```py\n The collateral from several short- and long-term funding markets and participants connects the repo market to the rest of the financial system.``` ```py\n The repo market is a critical source of liquidity and, accordingly, essential to the ongoing operations of various market participants, including market makers in virtually all sectors of the capital markets.```", url="https://www.financialresearch.gov/briefs/2016/01/13/us-bilateral-repo-market-lessons-from-a-new-survey/", color=disnake.Colour.dark_gold())
            em.set_image(url="https://i.ibb.co/P1jtpDw/repo-MARKET.png")
            await inter.edit_original_response(embed = em)
        elif market == "Short Term Funding Market":
            em = disnake.Embed(title="Short Term Funding Market", description=f"This figure shows borrowers on the left and lenders on the right, so that credit risk flows from left to right and money flows from right to left. The width of the bands represents outstanding credit as of December 31, 2019 ($1 trillion shown at bottom right for scale). Data sources and other technical details are in the Appendix.``` ```py\nThe figure 'does not include securities lending' and prime brokerage activity because of the lack of reliable disaggregated (and in some cases, reliable aggregated) data. The figure also nets some repo connections for simplicity.```",url="https://www.sec.gov/files/US-Credit-Markets_COVID-19_Report.pdf", color=disnake.Colour.dark_gold())
            em.set_image(url="https://i.ibb.co/HY98Kst/Short-term-funding-removebg-preview.png")
            await inter.edit_original_response(embed = em)
        elif market == "Corporate Bond Market":
            em = disnake.Embed(title="Corporate Bond Market", description=f"", url="https://www.sec.gov/files/US-Credit-Markets_COVID-19_Report.pdf", color=disnake.Colour.dark_gold())
            em.set_image(url="https://i.ibb.co/NFPd1xh/corporate-bonds-market-removebg-preview.png")
            await inter.edit_original_response(embed = em)
        elif market == "Residential Mortgage Market":
            em = disnake.Embed(title="Residential Mortgage", description=f"```py\n This figure shows borrowers on the left and lenders on the right, so that credit risk flows from left to right and money flows from right to left. The width of the bands represents outstanding credit as of December 31, 2019 ($5 trillion shown at bottom right for scale). Data sources and other technical details are in the Appendix.```", url="https://www.sec.gov/files/US-Credit-Markets_COVID-19_Report.pdf", color=disnake.Colour.dark_gold())
            em.set_image(url="https://i.ibb.co/0JkJgWm/resedentialmortgage-removebg-preview.png")
            await inter.edit_original_response(embed = em)
        elif market == "Commercial Real Estate Market":
            em = disnake.Embed(title="Commercial Real Estate Market", description=f"```py\n This figure shows borrowers on the left and lenders on the right, so that credit risk flows from left to right and money flows from right to left. The width of the bands represents outstanding credit as of December 31, 2019 ($1 trillion shown at bottom right for scale). Data sources and other technical details are in the Appendix.```", url="https://www.sec.gov/files/US-Credit-Markets_COVID-19_Report.pdf", color=disnake.Colour.dark_gold())
            em.set_image(url="https://i.ibb.co/6v2pNtP/commercial-real-estate-removebg-preview.png")
            await inter.edit_original_response(embed = em)
        elif market == "Leveraged Loans Market":
            em = disnake.Embed(title="Leveraged Loans Market", description=f"```py\nThis figure shows borrowers on the left and lenders on the right, so that credit risk flows from left to right and money flows from right to left. The width of the bands represents outstanding credit as of December 31, 2019 ($500 billion shown at bottom right for scale). Data sources and other technical details are in the Appendix.```", url="https://www.sec.gov/files/US-Credit-Markets_COVID-19_Report.pdf", color=disnake.Colour.dark_gold())
            em.set_image(url="https://i.ibb.co/G9PX57C/leveragedloans-markets-removebg-preview.png")
            await inter.edit_original_response(embed = em)
        elif market == "Municipal Securities Market":
            em = disnake.Embed(title="Municipal Securities Market", description=f"```py\nThis figure shows borrowers on the left and lenders on the right, so that credit risk flows from left to right and money flows from right to left. The width of the bands represents outstanding credit as of December 31, 2019 ($1 trillion shown at bottom right for scale).``` ```py\n Data sources and other technical details are in the Appendix.```", url="https://www.sec.gov/files/US-Credit-Markets_COVID-19_Report.pdf", color=disnake.Colour.dark_gold())
            em.set_image(url="https://i.ibb.co/NL5H82B/municipalsecurities-removebg-preview.png")
            await inter.edit_original_response(embed = em)





    @view.sub_command(guild_ids=[888488311927242753])
    async def futures(inter:disnake.ApplicationCommandInteraction, map: str = commands.Param(choices=["Dow Jones Industrial Average🏗️", "Crude Oil🛢️", "Crude Oil🛢️ Brent", "Cotton 👕", "Orange Juice🍊",
        "Platinum🍽️", "SP500🦾", "Corn🌽", "GBP British Pound 🇬🇧", "CAD Canadian Dollar 🇨🇦", "Swiss Francs 🇨🇭", "Oats🐴", "Japan 🇯🇵", "Canola", "Soybean Oil", "Silver🥈",
        "Natural GAS⛽", "Coacoa🍫"])):
        """Get futures for a wide variety of options."""
        await inter.response.defer(with_message=True, ephemeral=True)
        if map == "Dow Jones Industrial Average🏗️":
            embed = disnake.Embed(title="Dow Jones Industrial Average🏗️ Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?ym_d1_s.png")
            embed.set_footer(text="Real time Data Provided by IEXCloud")
            await inter.edit_original_message(embed=embed, ephemeral=True)

        elif map == "Crude Oil🛢️":
            embed = disnake.Embed(title="Crude Oil🛢️ Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?cl_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=True)

        elif map == "Crude Oil🛢️ Brent":
            embed = disnake.Embed(title="Crude Oil🛢️ Brent Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?qa_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=True)

        elif map == "Cotton 👕":
            embed = disnake.Embed(title="Cotton 👕 Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?ct_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=True)

        elif map == "Orange Juice🍊":
            embed = disnake.Embed(title="Orange Juice🍊 Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?jo_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=True)

        elif map == "Platinum🍽️":
            embed = disnake.Embed(title="Platinum🍽️ Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?pl_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=True)

        elif map == "SP500🦾":
            embed = disnake.Embed(title="SP500", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?es_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=True)

        elif map == "Corn🌽":
            embed = disnake.Embed(title="Corn Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?zc_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=True)

        elif map == "GBP British Pound 🇬🇧":
            embed = disnake.Embed(title="GBP Futures 🇬🇧", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?6b_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=True)

        elif map == "CAD Canadian Dollar 🇨🇦":
            embed = disnake.Embed(title="CAD Futures 🇨🇦", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?6c_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=True)

        elif map == "Swiss Francs 🇨🇭":
            embed = disnake.Embed(title="Swiss Francs 🇨🇭 Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?6s_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=True)

        elif map == "Oats🐴":
            embed = disnake.Embed(title="Oats🐴 Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?zo_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=True)

        elif map == "Canola":
            embed = disnake.Embed(title="Canola Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?rs_d1_s.png")
            await inter.edit_original_message(embed=embed, ephemeral=True)

        elif map == "Japan 🇯🇵":
            embed = disnake.Embed(title="Japan 🇯🇵 Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?6j_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=True)

        elif map == "Natural GAS⛽":
            embed = disnake.Embed(title="Natural Gas Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?ng_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=True)

        elif map == "Silver🥈":
            embed = disnake.Embed(title="Silver🥈 Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?si_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=True)

        elif map == "Coacoa🍫":
            embed = disnake.Embed(title="Coacoa 🍫 Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?cc_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=True)





    @view.sub_command()
    async def technicals(inter:disnake.AppCmdInter):
        """View a dropdown of technical patterns"""
        await inter.response.defer(with_message=True, ephemeral=True)
        await inter.edit_original_response(view=TechView())


def setup(bot):
    bot.add_cog(ViewCmd(bot))
    print(f"> Extension {__name__} is ready\n")