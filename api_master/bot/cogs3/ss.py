from disnake.ext import commands
import disnake
from utils import e
from sdks.stocksera_sdk.sdk import StockSeraSDK
import pandas as pd
import math
from typing import List

from api_master.cfg import today_str, thirty_days_from_now_str, five_days_ago_str
sdk = StockSeraSDK()





class PageSelect(disnake.ui.Select):
    def __init__(self, embeds):
        options = [
            disnake.SelectOption(
                label=f"Page {i+1}",
                value=f"{i}"
            ) for i in range(len(embeds))
        ]

        super().__init__(
            custom_id="page_selector1",
            placeholder="Page Select",
            min_values=1,
            max_values=1,
            options=options
        )
        
        self.embeds = embeds

    async def callback(self, interaction: disnake.Interaction):
        await interaction.response.edit_message(embed=self.embeds[int(self.values[0])])



class AlertMenus(disnake.ui.View):
    def __init__(
        self, embeds: List[disnake.Embed], total_pages:str = None, options: List[disnake.Embed] = None
    ):
        super().__init__(timeout=None)
        self.embeds = embeds
        self.options = options
        # Sets the embed list variable.
        self.total_pages = total_pages
        #self.options2 = options2

        # Current embed number.
        self.embed_count = 0

        # Disables previous page button by default.
        self.prev_page.disabled = True


        # Sets the footer of the embeds with their respective page numbers.
        self.count = 0

        for i, embed in enumerate(self.embeds):
            embed.set_footer(
                text=f"Page {i + 1} of {len(self.embeds)}",
            )



    @disnake.ui.button(
        emoji="<a:_:1042677512284680321>",
        style=disnake.ButtonStyle.red,
        custom_id=f"persistent_view:prevqwfpage_{str(disnake.Member)}aq2wfwa",
        row=4,
        label=f"🇵 🇷 🇪 🇻"

    )
    async def prev_page(  # pylint: disable=W0613
        self,
        button: disnake.ui.Button,
        interaction: disnake.MessageInteraction,
    ):
        # Decrements the embed count.
        self.embed_count -= 1

        # Gets the embed object.
        embed = self.embeds[self.embed_count]

        # Enables the next page button and disables the previous page button if we're on the first embed.
        self.next_page.disabled = False

        await interaction.response.edit_message(embed=embed, view=self)


    @disnake.ui.button(
        emoji="<a:_:1042677591196319765>",
        style=disnake.ButtonStyle.red,
        custom_id=f"persistent_view:nextpage_{str(disnake.Member)}awfawwa",
        label=f"🇳 🇪 🇽 🇹",
        row=4
    )
    async def next_page(  # pylint: disable=W0613
        self,
        button: disnake.ui.Button,
        interaction: disnake.MessageInteraction,
    ):
        # Increments the embed count.
        self.embed_count += 1

        # Gets the embed object.
        embed = self.embeds[self.embed_count]

        # Enables the previous page button and disables the next page button if we're on the last embed.
        self.prev_page.disabled = False

        await interaction.response.edit_message(embed=embed, view=self)


class StockSera(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command()
    async def ss(self, inter):
        pass


    @ss.sub_command()
    async def treasury(self, inter: disnake.AppCmdInter):
        
        """Returns the treasury balance as well as open/close and moving avg."""
        await inter.response.defer()
        treasury = sdk.daily_treasury(500)

        df = pd.DataFrame(vars(treasury))
        df = df[::-1]
        filename = f'daily_treasury_{today_str}.csv'.replace('-','')
        df.to_csv(filename)
        embeds = []
        for i, row in df.iterrows():
            date = row['date']
            close_balance = row['close_balance']
            open_balance = row['open_balance']
            amount_change = row['amount_change']
            percent_change = row['percent_change']
            moving_avg = row['moving_avg']
            embed = disnake.Embed(title=f"Daily Treasury Balance", description=f"```py\nThe Daily Treasury Balance refers to the balance of funds held by the U.S. Department of the Treasury on a daily basis. It represents the total amount of money available in the Treasury's accounts, including revenues from taxes, borrowings, and other sources, as well as expenditures made by the government.```", color=disnake.Colour.dark_purple())
            embed.add_field(name=f"Date:", value=f"> {e.econcalendar} **{date}**", inline=False)
            embed.add_field(name=f"Balance Info:", value=f"> **Open Balance: **${open_balance}**\n> Closing Balance: **${close_balance}**")
            embed.add_field(name=f"Change:", value=f"> **{percent_change}%**\n> Moving AVG: **{moving_avg}**")
            embeds.append(embed)

        view = AlertMenus(embeds).add_item(PageSelect(embeds))
    
        await inter.edit_original_message(embed=embeds[0], view=view, file=disnake.File(filename))



    @ss.sub_command()
    async def earnings(self, inter: disnake.AppCommandInter, date_from=today_str, date_to=thirty_days_from_now_str, page="1"):
        """Returns upcoming earnings for a set amount of dates or 30 days by default."""
        await inter.response.defer()

        page = int(page)  # Convert the page argument to an integer

        earnings_cal = sdk.earnings_calendar(date_from=date_from, date_to=date_to)

        df = pd.DataFrame(vars(earnings_cal))
        filename = df.to_csv('earnings_calendar.csv')

        embeds = []
        tickers_in_embed = 0
        embed = None

        for i, row in df.iterrows():
            ticker = row['ticker']
            
            hour = row['hour']
            if hour == "BMO":
                hour = 'PreMarket'
            elif hour == "AMC":
                hour = 'AfterMarket'
            else:
                hour = 'Unknown'
            
            # If we have 10 tickers in the current embed or we don't have an embed yet, create a new one
            if tickers_in_embed >= 10 or not embed:
                embed = disnake.Embed(title=f"{e.earnings} Earnings Results {e.earnings}", description=f"```py\nEarnings Data - {row['date']}```", color=disnake.Colour.dark_blue())
                embeds.append(embed)
                tickers_in_embed = 0

            embed.add_field(name=f"{row['ticker']}", value=f"> {e.clockspin} Hour: **{hour}**\n> {e.moneytower} EPS Est: **{row['eps_est']}**")
            tickers_in_embed += 1

        select = PageSelect(embeds)


        view = AlertMenus(embeds).add_item(select)
        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji=e.download, label=f"Download")
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File('market_news.csv'))

        
        view.add_item(button)
  

        await inter.edit_original_message(embed=embeds[0], view=view)

    @ss.sub_command()
    async def ftds(self, inter:disnake.AppCmdInter, symbol=str, date_from=today_str, date_to=thirty_days_from_now_str):
        """Fetch market-wide or specific ticker FTDs overall or by date."""
        await inter.response.defer()
        _fails = sdk.ftd(from_date=date_from, date_to=thirty_days_from_now_str)

        df = pd.DataFrame(vars(_fails))

        filename = 'ftds.csv'
        df.to_csv(filename)
        tickers_in_embed = 0
        embeds = []
        embed = None
        for i, row in df.iterrows():
            date = row['date']
            FTD = row['amount_ftd']
            price = row['price']
            dollar_amount = row['dollar_cost']
            t_35 = row['t35_date']
                        # If we have 10 tickers in the current embed or we don't have an embed yet, create a new one
            if tickers_in_embed >= 10 or not embed:
                embed = disnake.Embed(title=f"{e.fail} Fail To Deliver {e.fail}", description=f"```py\nDisplaying tickers with the largest amount of fails with T+35 dates as well as dollar cost.```", color=disnake.Colour.dark_blue())
                embeds.append(embed)
                tickers_in_embed = 0
            embed.add_field(name=f"{row['ticker']} {row['date']}", value=f"> Amount: **{FTD}**\n> Price: **${price}**\n> Dollar Amount: **${dollar_amount}**\n> T+35: **{t_35}**")
            tickers_in_embed += 1

        select = PageSelect(embeds)


        view = AlertMenus(embeds).add_item(select)
        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji=e.download, label=f"Download")
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File('market_news.csv'))

        
        view.add_item(button)
        await inter.edit_original_message(embed=embeds[0], view=view)


    @ss.sub_command()

    async def house_trades(self, inter:disnake.AppCmdInter, ticker=str, name=str, state=str, date_to = five_days_ago_str, date_from = today_str):
        """Returns latest house trades. Search by ticker, house rep, state."""
        await inter.response.defer()
        house_trades = sdk.house(ticker=ticker,name=name,state=state,date_from=date_from,date_to=date_to)  # Assuming `sdk` is your SDK instance
        
        df = pd.DataFrame(vars(house_trades))
        print(df)
        embeds = []
        df.to_csv('house_trades.csv')
        embeds=[]
        for i, row in df.iterrows():
            trans_date = row['trans_date']
            amount = float(row['amount'])
            asset_type = row['asset_type']
            asset_desc = row['asset_desc']
            capital_gains_over_200k = row['capital_gains_over_200k']
            disclosure_date = row['disclosure_date']
            district = row['district']
            link = row['link']
            owner = row['owner']
            rep = row['rep']
            ticker = row['ticker']
            trans_date = row['trans_date']
            transaction_type = row['type']
            if transaction_type == 'Sale (Full)':
                color = disnake.Colour.dark_red()
            elif transaction_type == 'Purchase':
                color = disnake.Colour.dark_green()
            else:
                color = disnake.Colour.dark_grey()

            embed = disnake.Embed(title=f"🏠 House Trades 🏠", description=f"```py\nShowing trades out of the House of Representatives.```", color=color)
            embed.add_field(name=f"Representative:", value=f"> **{rep}**\n> District: **{district}**\n> Owner: **{owner}**")
            embed.add_field(name=f"Transaction Details:", value=f"> Date: **{trans_date}**\n> Disclosure: **{disclosure_date}")
            embed.add_field(name=f"Trade Info:", value=f"> Asset Type: **{asset_type}**\n> Asset Desc: **{asset_desc}**\n> Amount: **{amount:,}**")
            embed.add_field(name=f"Transaction:", value=f"> Type: **{transaction_type}**\n> Link: **{link}**")
            embed.add_field(name=f"Capital Gains over $200k?", value=f"> **{capital_gains_over_200k}")
            embeds.append(embed)

        select = PageSelect(embeds[:25])


        
        view = AlertMenus(embeds).add_item(select)
        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji=e.download, label=f"Download")
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File(f'house_trades.csv'))

        
        view.add_item(button)

        await inter.edit_original_message(embed=embeds[0], view=view)

    @ss.sub_command()
    async def sec_filings(self, inter:disnake.AppCmdInter, ticker):
        """Return SEC filings for a ticker."""
        await inter.response.defer()
        sec_filings = sdk.sec_fillings(ticker)
        df = pd.DataFrame(vars(sec_filings))
        df.to_csv(f'sec_filings_{ticker}.csv')
        embeds = []
        for i,row in df.iterrows():
            
            Description=row['Description']
            filing_url=row['filing_url']
            Filling=row['Filling']
            FillingDate=row['FillingDate']
            report_url=row['report_url']

            embed = disnake.Embed(title=f"{e.book} Sec Filings - {ticker} {e.book}", description=f"```py\nDisplaying SEC Filings for {ticker}```", color=disnake.Colour.dark_orange())
            embed.add_field(name=f"Filing:", value=f"> **{Filling}**\n\n> **{FillingDate}**")
            embed.add_field(name=f"Description:", value=f" > **{Description}**")
            embed.add_field(name=f"Filing URL:", value=f"> **{filing_url}")
            embed.add_field(name=f"Report URL:", value=f"> **{report_url}**")
            embeds.append(embed)


        select = PageSelect(embeds[:25])


        
        view = AlertMenus(embeds).add_item(select)
        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji=e.download, label=f"Download")
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File(f'sec_filings_{ticker}.csv'))

        
        view.add_item(button)

        await inter.edit_original_message(embed=embeds[0], view=view)


    @ss.sub_command()
    async def market_news(self, inter:disnake.AppCmdInter):
        """Returns market news in paginated form."""
        await inter.response.defer()
        news = sdk.market_news()
        df = pd.DataFrame(vars(news))
        df.to_csv('market_news.csv')
        embeds = []
        for i, row in df.iterrows():
            Date = row['Date']
            Title = row['Title']
            Source = row['Source']
            URL = row['URL']
            Section = row['Section']
            embed = disnake.Embed(title=f"{e.worldwide} {Source} - {Date} {e.worldwide}", description=f"```py\n{Title}\n\n{Section}```", url=URL, color=disnake.Colour.dark_magenta())
            embeds.append(embed)
        select = PageSelect(embeds[:25])


        
        view = AlertMenus(embeds).add_item(select)
        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji=e.download, label=f"Download")
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File('market_news.csv'))

        
        view.add_item(button)
        await inter.edit_original_message(embed=embeds[0], view=view)
           
    @ss.sub_command()
    async def jobless_claims(self, interaction: disnake.AppCommandInteraction, days:str=100):
        """Returns jobless claims data."""
        jobless_claims_data = sdk.jobless_claims(days=days)
        
        df = pd.DataFrame(vars(jobless_claims_data))
        df = df[::-1]
        df.to_csv('jobless_claims.csv')
        embeds = []
        for i, row in df.iterrows():
            date = row['Date']
            percent_change = row['Percent Change']
            number = float(row['Number'])
            embed = disnake.Embed(title=f"Jobless Claims", description=f"```py\nJobless Claims are the numbers of people who have recently lost their jobs and are requesting financial help from the government for the first time: The department said initial jobless claims fell again last week for the third week in a row.```", color=disnake.Colour.dark_red())
            embed.add_field(name=f"Date:", value=f"> **{date}**")
            embed.add_field(name=f"Results:", value=f"> Number: **{number:,}**")
            embeds.append(embed)
        select = PageSelect(embeds[:25])


        
        view = AlertMenus(embeds).add_item(select)
        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji=e.download, label=f"Download")
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File('jobless_claims.csv'))

        
        view.add_item(button)
        await interaction.edit_original_message(embed=embeds[0], view=view)

def setup(bot: commands.Bot):
    bot.add_cog(StockSera(bot))