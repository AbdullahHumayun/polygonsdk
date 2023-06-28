import disnake
from disnake.ext import commands
import requests
from autocomp import videos_autocomp
from views.learnviews import TechDropdown,TechDropdown2,SFTView,OCCView
from views.learnviews import ChinaView,DTCCView,ICEView,ETFView,NSCCView,FINRAView,Opt101View,TechView,NyseVIDView,CBOEView,NSFRView, PermaFTDViewStart
import pandas as pd
from menus.embedmenus import AlertMenus
from menus.pagination import PageSelect

from _discord import emojis
class ViewCmd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command()
    async def view(self, inter):
        pass


    @view.sub_command()
    async def technical_pattern(self, inter:disnake.AppCmdInter):
        """👁️Returns an animated example + a link to a detailed explanation of technicals."""
        await inter.response.defer(with_message=True, ephemeral=False)
        view = disnake.ui.View()
        view.add_item(TechDropdown())
        view.add_item(TechDropdown2())
        await inter.edit_original_response(view=view)

    @view.sub_command()
    async def dictionary(self, inter:disnake.AppCmdInter, word):
        """👁️Define something! Enter a word to get the definition."""
        await inter.response.defer(with_message=True, ephemeral=False)
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

    @view.sub_command()
    async def videos(self, inter: disnake.AppCmdInter, videos: str = commands.Param(autocomplete=videos_autocomp)):
        """👁️View a plethora of topics of educational videos!"""
        await inter.response.defer(with_message=True, ephemeral=False)
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
    async def markets(self, inter:disnake.AppCmdInter, market: str=commands.Param(choices=["Repo Market","Short Term Funding Market", "Corporate Bond Market", "Commercial Real Estate Market", "Leveraged Loans Market", "Resitential Mortgage Market", "Municipal Securities Market"])):
        """👁️View the ecosystem for several different Financial Markets."""
        await inter.response.defer(with_message=True, ephemeral=False)
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
    async def futures(self, inter:disnake.ApplicationCommandInteraction, map: str = commands.Param(choices=["Dow Jones Industrial Average🏗️", "Crude Oil🛢️", "Crude Oil🛢️ Brent", "Cotton 👕", "Orange Juice🍊",
        "Platinum🍽️", "SP500🦾", "Corn🌽", "GBP British Pound 🇬🇧", "CAD Canadian Dollar 🇨🇦", "Swiss Francs 🇨🇭", "Oats🐴", "Japan 🇯🇵", "Canola", "Soybean Oil", "Silver🥈",
        "Natural GAS⛽", "Coacoa🍫"])):
        """Get futures for a wide variety of options."""
        await inter.response.defer(with_message=True, ephemeral=False)
        if map == "Dow Jones Industrial Average🏗️":
            embed = disnake.Embed(title="Dow Jones Industrial Average🏗️ Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?ym_d1_s.png")
            embed.set_footer(text="Real time Data Provided by IEXCloud")
            await inter.edit_original_message(embed=embed, ephemeral=False)

        elif map == "Crude Oil🛢️":
            embed = disnake.Embed(title="Crude Oil🛢️ Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?cl_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=False)

        elif map == "Crude Oil🛢️ Brent":
            embed = disnake.Embed(title="Crude Oil🛢️ Brent Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?qa_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=False)

        elif map == "Cotton 👕":
            embed = disnake.Embed(title="Cotton 👕 Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?ct_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=False)

        elif map == "Orange Juice🍊":
            embed = disnake.Embed(title="Orange Juice🍊 Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?jo_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=False)

        elif map == "Platinum🍽️":
            embed = disnake.Embed(title="Platinum🍽️ Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?pl_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=False)

        elif map == "SP500🦾":
            embed = disnake.Embed(title="SP500", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?es_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=False)

        elif map == "Corn🌽":
            embed = disnake.Embed(title="Corn Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?zc_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=False)

        elif map == "GBP British Pound 🇬🇧":
            embed = disnake.Embed(title="GBP Futures 🇬🇧", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?6b_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=False)

        elif map == "CAD Canadian Dollar 🇨🇦":
            embed = disnake.Embed(title="CAD Futures 🇨🇦", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?6c_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=False)

        elif map == "Swiss Francs 🇨🇭":
            embed = disnake.Embed(title="Swiss Francs 🇨🇭 Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?6s_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=False)

        elif map == "Oats🐴":
            embed = disnake.Embed(title="Oats🐴 Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?zo_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=False)

        elif map == "Canola":
            embed = disnake.Embed(title="Canola Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?rs_d1_s.png")
            await inter.edit_original_message(embed=embed, ephemeral=False)

        elif map == "Japan 🇯🇵":
            embed = disnake.Embed(title="Japan 🇯🇵 Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?6j_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=False)

        elif map == "Natural GAS⛽":
            embed = disnake.Embed(title="Natural Gas Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?ng_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=False)

        elif map == "Silver🥈":
            embed = disnake.Embed(title="Silver🥈 Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?si_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=False)

        elif map == "Coacoa🍫":
            embed = disnake.Embed(title="Coacoa 🍫 Futures", color=disnake.Colour.random())
            embed.set_image(url="https://elite.finviz.com/fut_image.ashx?cc_d1_s.png")
            embed.set_footer(text="Real time Data Provided by Nasdaq Datalink - Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=embed, ephemeral=False)









    @view.sub_command()
    async def highftds(self, inter:disnake.AppCmdInter):
        """Returns the 25 highest FTDs with their T+35 Settlement Dates"""
        await inter.response.defer()
        view = PermaFTDViewStart()
        view.ptds1button1.disabled = True
        view.ptds1button2.disabled = True
        view.ptds1button4.disabled = True
        view.ptds1button5.disabled = True
        view.ptds1button6.disabled = True
        view.ptds1button7.disabled = True
        view.ptds1button8.disabled = True
        view.ptds1button9.disabled = True
        view.ptds1button10.disabled = True
        view.ptds1button16.disabled = True
        view.ptds1button17.disabled = True
        view.ptds1button18.disabled = True
        view.ptds1button19.disabled = True
        view.ptds1button20.disabled = True
        view.ptds1button21.disabled = True
        view.ptds1button22.disabled = True
        view.ptds1button23.disabled = True
        view.ptds1button24.disabled = True
        view.linkbutton25.disabled = True
        view.menu.callback = lambda interaction: interaction.response.edit_message(view=view,embed=embed)
        embed = disnake.Embed(title="High Failures to Deliver", description=f"```py\nHigh FTDs can be an extremely lucrative opportunity to play around the dates listed in the drop-down below - ESPECIALLY - if the dates fall within the short settlement window.``` To refresh the data shown here, simply click the green button below.```", color=disnake.Colour.dark_green())
        embed.set_image(url="https://i.imgur.com/Z3i9TNK.png")
        await inter.edit_original_message(view=view,embed=embed)


    @view.sub_command()
    async def patterns(inter: disnake.AppCmdInter):
        view = disnake.ui.View()
        view.add_item(TechDropdown())
        view.add_item(TechDropdown2())
        await inter.send(view=view)


    @view.sub_command()
    async def cmds(self, inter:disnake.AppCmdInter):
        """Returns a list of server commands"""
        await inter.response.defer()
        embeds = [
        disnake.Embed(title=f"Server Commands - OPENBB Bot", description=f"> **Charting Commands:**\n\n> **Chart 3 Minute:**\n> </c3m:1004263746090324062>\n> **Chart 5 Minute:**\n> </c5m:1004263746090324063>\n> **Chart 15 Minute:**\n> </c15m:1004263746090324064>\n> **Chart Day:**\n> </cd:1004263746090324061>\n> **Chart Fib:**\n> </chartfib:1007163283276562512>\n> **Chart Support/Resistance:**\n> </chartsr:1009175257590026281>\n> **Chart Custom:**\n> </chart:1004263746090324065>", color=disnake.Colour.dark_magenta()),
        disnake.Embed(title=f"Open BB Bot - DD Commands", description=f"> **Earnings:**\n> </dd earnings:1004263746090324066>\n> **After Hours:**\n> </dd ah:1004263746090324066>\n> **Analyst:**\n> </dd analyst:1004263746090324066>\n> **Biography:**\n> </dd bio:1004263746090324066>\n> **Customer:**\n> </dd customer:1004263746090324066>\n> **Dividends:**\n> </dd divinfo:1004263746090324066>\n> **Earnings Move:**\n> </dd ermove:1004263746090324066>\n> **Earnings Estimate:**\n> </dd est:1004263746090324066>\n> **Financials:**\n> </dd financials:1004263746090324066>\n> **Insiders:**\n> </dd insiders:1004263746090324066>\n> **Institutions:**\n> </dd instholdings:1004263746090324066>\n> **Premarket:**\n> </dd pm:1004263746090324066>\n> **Price Target Chart:**\n> </dd pt:1004263746090324066>\n> **SEC Filings:**\n> </dd sec:1004263746090324066>\n> **Splits:**\n> </dd splits:1004263746090324066>\n> **Supplier:**\n> </dd supplier:1004263746090324066>\n> **YTD Performance:**\n> </dd ytd:1004263746090324066>", color=disnake.Colour.dark_teal()),
        disnake.Embed(title=f"Open BB Bot - Disc Commands", description=f"> **Ark Trades:**\n> </disc arktrades:1004263746090324067>\n> **Gov. Contracts:**\n> </disc contracts:1004263746090324067>\n> **Fear and Greek Index:**\n> </disc fgindex:1004263746090324067>\n> **Halts:**\n> </disc halts:1004263746090324067>\n> **Holidays:**\n> </disc holidays:1004263746090324067>\n> **House Trades:**\n> </disc house:1004263746090324067>\n> **IPO List:**\n> </disc ipolist:1004263746090324067>\n> **Senate Trades:**\n> </disc senate:1004263746090324067>\n> **Splits:**\n> </disc splits:1004263746090324067>\n> **Trending Stocks:**\n> </disc trendingst:1004263746090324067>\n> **WSB Mentions:**\n> </disc wsb:1004263746090324067>"),
        disnake.Embed(title=f"Open BB - Dark Pool Commands", description=f"> **All Blocks:**\n> </dp allblocks:1004263746170011748>\n> **All Darkpools:**\n> </dp alldp:1004263746170011748>\n> **All Prints:**\n> </dp allprints:1004263746170011748>\n> **Big Prints:**\n> </dp bigprints:1004263746170011748>\n> **Levels:**\n> </dp levels:1004263746170011748>\n> **Sectors:**\n> </dp sectors:1004263746170011748>\n> **Summary:**\n> </dp summary:1004263746170011748>\n> **Top Total:**\n> </dp topsum:1004263746170011748>"),
        disnake.Embed(title=f"Open BB - Economy Commands", description=f"> **Reverse Repo:**\n> </econ revrepo:1004263746111275130>\n> **Econ Calendar:**\n> </econ calendar:1004263746111275130>\n> **Commodities:**\n> </econ commodities:1004263746111275130>\n> **Currencies:**\n> </econ currencies:1004263746111275130>\n> **Fed Rates:**\n> </econ fedrates:1004263746111275130>\n> **Global Bonds:**\n> </econ glbonds:1004263746111275130>\n> **Indices:**\n> </econ indices:1004263746111275130>\n> **US Bonds:**\n> </econ usbonds:1004263746111275130>\n> **Yield Curve:**\n> </econ yieldcurve:1004263746111275130>"),
        disnake.Embed(title=f"Open BB - Flow Commands",description=f"> **Big Flow:**\n> </flow bigflow:1004263746170011749>\n> **Day:**\n> </flow day:1004263746170011749>\n> **Opening:**\n> </flow opening:1004263746170011749>\n> **Premium:**\n> </flow premium:1004263746170011749>\n> **Sector Flow:**\n> </flow sectors:1004263746170011749>\n> **Day Summary:**\n> </flow sumday:1004263746170011749>\n> **Flow By Expiry:**\n> </flow sumexp:1004263746170011749>\n> **Flow Summary:**\n> </flow summary:1004263746170011749>\n> **Top Flow Summary:**\n> </flow sumtop:1004263746170011749>\n> **Week Summary:**\n> </flow sumweek:1004263746170011749>\n> **Unusual Flow:**\n> </flow unu:1004263746170011749>\n> **Top Weekly:**\n> </flow weekly:1004263746170011749>"),
        disnake.Embed(title=f"Open BB - Options Commands", description=f"> **Chains:**\n> </op chains:1004263746111275138>\n> **Put/Call Ratio:**\n> </op equitypc:1004263746111275138>\n> **Gamma:**\n> </op gamma:1004263746111275138>\n> **High IV:**\n> </op highiv:1004263746111275138>\n> **Price History:**\n> </op hist:1004263746111275138>\n> **Index Put/Call Ratio:**\n> </op indexpc:1004263746111275138>\n> **Option Info:**\n> </op info:1004263746111275138>\n> **In The Money:**\n> </op itm:1004263746111275138>\n> **Max Pain:**\n> </op maxpain:1004263746111275138>\n> **Open Interest:**\n> </op oi:1004263746111275138>\n> **Chart OI:**\n> </op oichart:1004263746111275138>\n> **Smile:**\n> </op smile:1004263746111275138>\n> **Option Stats:**\n> </op stats:1004263746111275138>\n> **Top OI:**\n> </op topoi:1004263746111275138>\n> **Top OI Change:**\n> </op topoichange:1004263746111275138>\n> **Top Strike Volume:**\n> </op topstrikevol:1004263746111275138>\n> **Top Volume:**\n> </op topvol:1004263746111275138>\n> **Top ETF Volume:**\n> </op topvoletf:1004263746111275138>\n> **Unusual Options:**\n> </op unu:1004263746111275138>\n> **Top 20day Avg:**\n> </op uoastock:1004263746111275138>\n> **Volume:**\n> </op vol:1004263746111275138>\n> **Volatility Surface:**\n> </op vsurf:1004263746111275138>"),
        disnake.Embed(title=f"Open BB - Short Commands", description=f"> **Borrowed Shares:**\n> </sh borrowed:1004263746170011751>\n> **Top Short Interest:**\n> </sh hsi:1004263746170011751>\n> **Short Rate:**\n> </sh shortrate:1004263746170011751>\n> **Short Volume:**\n> </sh shortvol:1004263746170011751>\n> **Top Volume Shorted:**\n> </sh topshortvol:1004263746170011751>"),
        disnake.Embed(title=f"FUDSTOP 🔍 Analysis Commands", description=f"> **Finscreener:**\n> </analysis finscreen:1121296423032475749>\n> **Gaps Down:**\n> </analysis gaps_down:1121296423032475749>\n> **Gaps Up:**\n> </analysis gaps_up:1121296423032475749>\n> **Overbought Gap:**\n> </analysis overbought_gap:1121296423032475749>\n> **Analyst Ratings:**\n> </analysis rating:1121296423032475749>\n> **Top Shorts:**\n> </analysis topshorts:1121296423032475749>"),
        disnake.Embed(title=f"FUDSTOP <a:_:1043216082644766811> Discord-Related:", description=f"> **User Avatar:**\n> </discord avatar:1121296423032475751>\n> **Data:**\n> </discord data:1121296423032475751>\n> **Define:**\n> </discord define:1121296423032475751>\n> **Tools:**\n> </discord tools:1121296423032475751>"),
        disnake.Embed(title=f"FUDSTOP 🪙 Economy Commands:", description=f"> **Economy Data:**\n> </economy data:1121296423032475753>\n> **Agency MBS:**\n> </economy ambs:1121296423032475753>\n> **House Trades:**\n> </economy house_trades:1121296423032475753>\n> **Inflation:**\n> </economy inflation:1121296423032475753>\n> **Jobless Claims:**\n> </economy jobless_claims:1121296423032475753>\n> **Retail Repo:**\n> </economy retail_repo:1121296423032475753>\n> **Reverse Repo:**\n> </economy reverserepo:1121296423032475753>"),
        disnake.Embed(title=f"FUDSTOP 🧠 Learn Commands", description=f"> **Learn Calls:**\n> </learn calls:1121296423296708620>\n> **Learn Candle Patterns:**\n> </learn candle_patterns:1121296423296708620>\n> **Learn China:**\n> </learn china:1121296423296708620>\n> **Learn Core Logic:**\n> </learn core_logic:1121296423296708620>\n> **Learn Covered Calls:**\n> </learn covered_calls:1121296423296708620>\n> **Learn Discord:**\n> </learn discord:1121296423296708620>\n> **Learn ETFs:**\n> </learn etfs:1121296423296708620>\n> **Learn SEC Filings:**\n> </learn filings:1121296423296708620>\n> **Learn Finra:**\n> </learn finra:1121296423296708620>\n> **Learn Greeks:**\n> </learn greeks:1121296423296708620>\n> **Learn NSFR Ratio:**\n> </learn nsfr_ratio:1121296423296708620>\n> **Learn OCC:**\n> </learn occ:1121296423296708620>\n> **Learn Option Strategies:**\n> </learn option_strategies:1121296423296708620>\n> **Options 101:**\n> </learn options_101:1121296423296708620>\n> **Order Types:**\n> </learn order_types:1121296423296708620>\n> **Learn TA:**\n> </learn ta:1121296423296708620>"),
        disnake.Embed(title=f"FUDSTOP - Navigation Commands", description=f"> **Navigate Channels:**\n> </navigate channels:1121296423296708621>\n> **Navigate Forums:**\n> </navigate forums:1121296423296708621>\n> **Navigate Threads:**\n> </navigate threads:1121296423296708621>"),
        disnake.Embed(title=f"FUDSTOP 🔥 Webull Commands:", description=f"> **Analysis Tools:**\n> </webull analysis_tools:1121296424097820673>\n> **Bid ask Spread:**\n> </webull bid_ask_spread:1121296424097820673>\n> **Webull Graphics:**\n> </webull graphics:1121296424097820673>\n> **Option Chain:**\n> </webull options_chain:1121296424097820673>\n> **Options Setup:**\n> </webull options_setup:1121296424097820673>\n> **Order Types:**\n> </webull orders:1121296424097820673>\n> **Paper Trading:**\n> </webull paper_trading:1121296424097820673>\n> **Webull Quote:**\n> </webull webull_quote:1121296424097820673>"),
        disnake.Embed(title=f"MORE COMING YO!", description=f"This command: `>>cmds`")
        ]
        select = PageSelect(embeds[:25])
        view = AlertMenus(embeds).add_item(select)
        await inter.edit_original_message(view=view, embed=embeds[0])



    @view.sub_command()
    async def technicals(inter:disnake.AppCmdInter):
        """View a dropdown of technical patterns"""
        await inter.response.defer(with_message=True, ephemeral=False)
        await inter.edit_original_response(view=TechView())


def setup(bot:commands.Bot):
    bot.add_cog(ViewCmd(bot))
    print(f"> Extension {__name__} is ready\n")