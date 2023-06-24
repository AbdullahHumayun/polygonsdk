import requests
import disnake
from disnake.ext import commands

import stocksera
from cfg import YOUR_STOCKSERA_KEY, YOUR_IEX_CLOUD_KEY
from time import sleep

client = stocksera.Client(YOUR_STOCKSERA_KEY)


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot



    @commands.slash_command()
    async def economy(self, inter: disnake.AppCmdInter):
        """Economy slash commands category."""
        pass


    @economy.sub_command()
    async def jobless_claims(inter:disnake.AppCmdInter):
        """🪙Returns the latest data on jobless claims."""
        await inter.response.defer(with_message=True)
        sleep(2)
        data = client.jobless_claims(days=100)
        items = "\n\n".join(f"```py\n{i['Date']} Number: {i['Number']} Change: {i['Percent Change']}```" for i in data)
        em = disnake.Embed(title="Jobless Claims", description=f"{items}",color=disnake.Colour.dark_blue())
        await inter.edit_original_message(embed=em)

    @economy.sub_command()
    async def ambs(interaction: disnake.ApplicationCommandInteraction, transaction: str=commands.Param
        (name="transaction", choices=["all", "sales", "purchases", "roll", "swap"])):
        """🪙Return the latest Agency Mortgage Backed Securities Transactions out of the FED."""
        await interaction.response.defer(ephemeral=True)
        r = requests.get(url=f"https://markets.newyorkfed.org/api/ambs/{transaction}/results/summary/last/3.json")
        d = r.json()
        ambs = d['ambs']
        auctions = ambs['auctions']
        items1 = '\n\n'.join(f"⭐DATE: {i['operationDate']}\nTYPE: '{i['operationType']}'\nRELEASED: '{i['releaseTime']}'\nCLOSED: {i['closeTime']}\nCLASS: '{i['classType']}'\nSETTLEMENT DATE: '{i['settlementDate']}'\nAmount Submitted: ${i['totalAmtSubmittedPar']}\nAmount Accepted: ${i['totalAmtAcceptedPar']}\n" for i in auctions)
        for i in auctions:
            operationdate = i.get('operationDate')
            type = i.get('operationType')
            release = i.get('releaseTime')
            closed = i.get('closeTime')
            clas = i.get('classType')
            settlement = i.get('settlementDate')
            accepted = i.get('totalAmtAcceptedPar')
            submitted = i.get('totalAmtSubmittedPar')

    

        items2 = '\n\n'.join(f" 🅰️ DATE: {operationdate}  TYPE: {type}"
        f"RELEASED: {release} CLOSED: {closed} CLASS: {clas} SETTLEMENT DATE: {settlement}"
        f"Amount Submitted: ${submitted} ACCEPTED: ${accepted}" for i in auctions)
        embed=disnake.Embed(title="Agency Mortgage Backed Securities - Fed Reserve", description=f"```py\n{items1}```", color=disnake.Colour.blue())
        embed.set_footer( text="Implemented by Fudstop Trading - Data Provided by Newyork FED")
        await interaction.edit_original_message(embed=embed)



    @economy.sub_command()
    async def retail_repo(inter: disnake.AppCmdInter):
        """🪙Current amount of Retail funds in the repo market."""
        await inter.response.defer(with_message=True)
        r = requests.get(url=f"https://cloud.iexapis.com/stable/data-points/market/WRMFSL?token={YOUR_IEX_CLOUD_KEY}")
        em = disnake.Embed(title=f"Current Retail money funds returned as billions of dollars, seasonally adjusted", color=disnake.Colour.random())
        em.set_footer(text="Source: The Federal Reserve Bank of New York", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Seal_of_the_United_States_Federal_Reserve_System.svg/150px-Seal_of_the_United_States_Federal_Reserve_System.svg.png")
        
        em.add_field(name=f"Current amount of Retail dollars in Money Market Funds:", value=f"🪙**{r}** billion dollars. \n")
        view = disnake.ui.View()
        await inter.edit_original_message(embed=em)


    @economy.sub_command()
    async def house_trades(inter:disnake.AppCmdInter):
        """🪙Returns the 25 most recent House Trades"""
        await inter.response.defer(with_message=True)
        df = client.house()
        house = df['house'][0:19]
        items = "\n\n".join(f"Date: {i['Transaction Date']} Owner: {i['Owner']} Ticker:{i['Ticker']} Type: {i['Type']} Amt: {i['Amount']} Rep: {i['Representative']}\n Link:{i['Link']}" for i in house)
        em = disnake.Embed(title="House Trades - Latest", description=f"```py\n {items}```", color=disnake.Colour.dark_red())
        await inter.edit_original_message(embed=em)


    @economy.sub_command()
    async def inflation(inter:disnake.AppCmdInter):
        """🪙Returns historic inflation with average per year back to 2007."""
        await inter.response.defer(with_message=True)
        df = client.inflation()
        year2022 = df['2022']
        jan2022 = year2022['Jan']
        feb2022 = year2022['Feb']
        march2022 = year2022['Mar']
        april2022 = year2022['Apr']
        may2022 = year2022['May']
        june2022 = year2022['Jun']
        july2022 = year2022['Jul']
        august2022 = year2022['Aug']
        september2022 = year2022['Sep']
        ave2022 = year2022['Ave']

        year2021 = df['2021']
        jan2021 = year2021['Jan']
        feb2021 = year2021['Feb']
        march2021 = year2021['Mar']
        april2021 = year2021['Apr']
        may2021 = year2021['May']
        june2021 = year2021['Jun']
        july2021 = year2021['Jul']
        august2021 = year2021['Aug']
        september2021 = year2021['Sep']
        september2021 = year2021['Sep']
        october2021 = year2021['Oct']
        november2021 = year2021['Nov']
        december2021 = year2021['Dec']
        ave2021 = year2021['Ave']

        year2020 = df['2020']
        jan2020 = year2020['Jan']
        feb2020 = year2020['Feb']
        march2020 = year2020['Mar']
        april2020 = year2020['Apr']
        may2020 = year2020['May']
        june2020 = year2020['Jun']
        july2020 = year2020['Jul']
        august2020 = year2020['Aug']
        september2020 = year2020['Sep']
        october2020 = year2020['Oct']
        november2020 = year2020['Nov']
        december2020 = year2020['Dec']
        ave2020 = year2020['Ave']

        year2019 = df['2019']
        jan2019 = year2019['Jan']
        feb2019 = year2019['Feb']
        march2019 = year2019['Mar']
        april2019 = year2019['Apr']
        may2019 = year2019['May']
        june2019 = year2019['Jun']
        july2019 = year2019['Jul']
        august2019 = year2019['Aug']
        september2019 = year2019['Sep']
        october2019 = year2019['Oct']
        november2019 = year2019['Nov']
        december2019 = year2019['Dec']
        ave2018 = year2019['Ave']


        year2018 = df['2018']
        ave2018 = year2018['Ave']
        year2017 = df['2017']
        ave2017 = year2017['Ave']
        year2016 = df['2016']
        ave2016 = year2016['Ave']
        year2015 = df['2015']
        ave2015 = year2015['Ave']
        year2014 = df['2014']
        ave2014 = year2014['Ave']
        year2013 = df['2013']
        ave2013 = year2013['Ave']
        year2012 = df['2012']
        ave2012 = year2012['Ave']
        year2011 = df['2011']
        ave2011 = year2011['Ave']
        year2010 = df['2010']
        ave2010 = year2010['Ave']
        year2009 = df['2009']
        ave2009 = year2009['Ave']
        year2008 = df['2008']
        ave2008 = year2008['Ave']
        year2007 = df['2007']
        ave2007 = year2007['Ave']
        em = disnake.Embed(title="Inflation Data", description=f"```py\n Inflation data since 2007.``` *2022:**```py\n Jan: {jan2022}  Feb: {feb2022} March: {march2022}\nApril: {april2022} May: {may2022} June: {june2022}\nJuly: {july2022} August: {august2022} September: {september2022}\n\n AVERAGE: {ave2022} \n"
    f" **2021:**```py\n Jan: {jan2021}  Feb: {feb2021} March: {march2021}\nApril: {april2021} May: {may2021} June: {june2021}\nJuly: {july2021} August: {august2021} September: {september2021}\nOctober: {october2021} November: {november2021} December: {december2021}``` \n"
    f" **2020:** ```py\n Jan: {jan2020}  Feb: {feb2020} March: {march2020}\nApril: {april2020} May: {may2020} June: {june2020}\nJuly: {july2020} August: {august2020} September: {september2020}\nOctober: {october2020} November: {november2020} December: {december2020}``` \n"
    f" **2019:** ```py\n Jan: {jan2019}  Feb: {feb2019} March: {march2019}\nApril: {april2019} May: {may2019} June: {june2019}\nJuly: {july2019} August: {august2019} September: {september2019}\nOctober: {october2019} November: {november2019} December: {december2019}``` \n", color=disnake.Colour.dark_gold())
        em.add_field(name="Avg 2018", value=f"```py\n{ave2018}```")
        em.add_field(name="Avg 2017", value=f"```py\n{ave2017}```")
        em.add_field(name="Avg 2016", value=f"```py\n{ave2016}```")
        em.add_field(name="Avg 2015", value=f"```py\n{ave2015}```")
        em.add_field(name="Avg 2014", value=f"```py\n{ave2014}```")
        em.add_field(name="Avg 2013", value=f"```py\n{ave2013}```")
        em.add_field(name="Avg 2012", value=f"```py\n{ave2012}```")
        em.add_field(name="Avg 2011", value=f"```py\n{ave2011}```")
        em.add_field(name="Avg 2010", value=f"```py\n{ave2010}```")
        em.add_field(name="Avg 2009", value=f"```py\n{ave2009}```")
        em.add_field(name="Avg 2008", value=f"```py\n{ave2008}```")
        em.add_field(name="Avg 2007", value=f"```py\n{ave2007}```")
        await inter.edit_original_message(embed=em)


    @economy.sub_command()
    async def reverserepo(inter:disnake.AppCmdInter):
        """🪙Returns the last 10 days of REPO with a moving average."""
        await inter.response.defer(with_message=True)
        repo = client.reverse_repo(days=10)
        date = [i['Date'] for i in repo]
        amount =[i['Amount'] for i in repo]
        avg = [i['Average'] for i in repo]
        parties = [i['Num Parties'] for i in repo]
        ma = [i['Moving Avg'] for i in repo]

        for i in repo:
            date = i.get('Date')
            amount = i.get('Amount')
            avg = i.get('Average')
            parties = i.get('Num Parties')
            ma = round(i.get('Moving Avg'), ndigits=2)
        items = "\n\n".join(f"{i['Date']} Amt: ${i['Amount']} Avg: ${i['Average']} bill\n#Parties: {i['Num Parties']} Moving Avg: {i['Moving Avg']}" for i in repo)
        em = disnake.Embed(title="Repo Numbers", description=f"```py\n{items}```", color=disnake.Colour.dark_red())
        print(f"```py\n{items}")
        await inter.edit_original_message(embed=em)


    @economy.sub_command()
    async def data(inter:disnake.AppCmdInter):
        """🪙Returns Economic Indicator Datasets"""
        await inter.response.defer(with_message=True)
        em = disnake.Embed(title="Economic Datasets", description=f"```py\nThis data is provided by Census.gov. Here's a link to the most recent report:``` https://www.census.gov/econ/indicators/advance_report.pdf", color=disnake.Colour.dark_purple(), url="https://www.census.gov/econ/currentdata/datasets/index")
        em.add_field(name="U.S. International Trade in Goods and Services",value="```py\nLast Updated: 05-Oct-2022 08:30```https://www.census.gov/econ/currentdata/datasets/FTD-mf.zip")
        em.add_field(name="Quarterly Survey of Public Pensions",value="```py\nLast Updated: 31.95 KB	29-Sep-2022 10:00``` https://www.census.gov/econ/currentdata/datasets/QPR-mf.zip")
        em.add_field(name="Quarterly Summary of State & Local Taxes",value="```py\nLast Updated:15-Sep-2022 10:00``` https://www.census.gov/econ/currentdata/datasets/QTAX-mf.zip")
        em.add_field(name="Quarterly Services Survey",value=" https://www.census.gov/econ/currentdata/datasets/QSS-mf.zip")
        em.add_field(name="Quarterly Financial Report",value="https://www.census.gov/econ/currentdata/datasets/QFR-mf.zip")
        em.add_field(name="New Residential Construction",value="https://www.census.gov/econ/currentdata/datasets/RESCONST-mf.zip")
        em.add_field(name="New Home Sales",value="https://www.census.gov/econ/currentdata/datasets/RESSALES-mf.zip")
        em.add_field(name="Monthly Wholesale Trade: Sales and Inventories",value="https://www.census.gov/econ/currentdata/datasets/MWTS-mf.zip")
        em.add_field(name="Monthly Retail Trade and Food Services",value="https://www.census.gov/econ/currentdata/datasets/MRTS-mf.zip")
        em.add_field(name="Manufacturing and Trade Inventories and Sales",value="https://www.census.gov/econ/currentdata/datasets/MTIS-mf.zip")
        em.add_field(name="Manufacturers' Shipments, Inventories, and Orders",value="https://www.census.gov/econ/currentdata/datasets/M3-mf.zip")
        em.add_field(name="Manufactured Housing Survey (Current)",value="https://www.census.gov/econ/currentdata/datasets/MHS2-mf.zip")
        em.add_field(name="Manufactured Housing Survey (1980-2013)",value="https://www.census.gov/econ/currentdata/datasets/MHS-mf.zip")
        em.add_field(name="Housing Vacancies and Homeownership",value="https://www.census.gov/econ/currentdata/datasets/HV-mf.zip")
        em.add_field(name="Construction Spending",value="https://www.census.gov/econ/currentdata/datasets/VIP-mf.zip")
        em.add_field(name="Business Formation Statistics",value="https://www.census.gov/econ/currentdata/datasets/BFS-mf.zip")
        em.add_field(name="Advance Monthly Sales for Retail and Food Services",value="https://www.census.gov/econ/currentdata/datasets/MARTS-mf.zip")
        em.add_field(name="Advance Monthly Manufacturers' Shipments, Inventories and Orders",value="https://www.census.gov/econ/currentdata/datasets/M3ADV-mf.zip")
        em.set_footer(text="The U.S. Census Bureau")
        await inter.edit_original_message(embed=em)


async def setup(bot: commands.Bot):
    """SETUP COG"""
    await bot.add_cog(Economy(bot))
    print(f"> Extension {__name__} is ready\n")
