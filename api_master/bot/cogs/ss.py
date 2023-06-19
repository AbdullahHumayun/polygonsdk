from disnake.ext import commands
import disnake
from _discord.views.menus import AlertMenus
import os
from autocomp import ticker_autocomp
from sdks.stocksera_sdk.sdk import StockeraSDK
import pandas as pd
import math
from typing import List

from cfg import today_str, thirty_days_from_now_str, five_days_ago_str, thirty_days_ago_str
sdk = StockeraSDK()
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
            placeholder="Pages 1-25",
            min_values=1,
            max_values=1,
            options=options,
            row=0
        )
        
        self.embeds = embeds

    async def callback(self, interaction: disnake.Interaction):
        await interaction.response.edit_message(embed=self.embeds[int(self.values[0])])
class PageSelect2(disnake.ui.Select):
    def __init__(self, embeds):
        options = [
            disnake.SelectOption(
                label=f"Page {i+1}",
                value=f"{i}"
            ) for i in range(25, 50) 
        ]

        super().__init__(
            custom_id="page_selector2",
            placeholder="Pages 26-50",
            min_values=1,
            max_values=1,
            options=options,
            row=1,
        )
        
        self.embeds = embeds

    async def callback(self, interaction: disnake.Interaction):
        await interaction.response.edit_message(embed=self.embeds[int(self.values[0])])
class PageSelect3(disnake.ui.Select):
    def __init__(self, embeds):
        options = [
            disnake.SelectOption(
                label=f"Page {i+1}",
                value=f"{i}"
            ) for i in range(51, 75)  # Generates numbers from 51 through 75
        ]

        super().__init__(
            custom_id="page_selector3",
            placeholder="Pages 51-75",
            min_values=1,
            max_values=1,
            options=options,
        )
        
        self.embeds = embeds

    async def callback(self, interaction: disnake.Interaction):
        await interaction.response.edit_message(embed=self.embeds[int(self.values[0])])


class PageSelect4(disnake.ui.Select):
    def __init__(self, embeds):
        options = [
            disnake.SelectOption(
                label=f"Page {i+1}",
                value=f"{i}"
            ) for i in range(76, 100)  # Generates numbers from 76 through 100
        ]

        super().__init__(
            custom_id="page_selector4",
            placeholder="Pages 76-100",
            min_values=1,
            max_values=1,
            options=options,
        )
        
        self.embeds = embeds

    async def callback(self, interaction: disnake.Interaction):
        await interaction.response.edit_message(embed=self.embeds[int(self.values[0])])

class PageSelect5(disnake.ui.Select):
    def __init__(self, embeds):
        options = [
            disnake.SelectOption(
                label=f"Page {i+1}",
                value=f"{i}"
            ) for i in range(101, 125)  # Generates numbers from 76 through 100
        ]

        super().__init__(
            custom_id="page_selector5",
            placeholder="Pages 101-125",
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
        treasury = sdk.daily_treasury()

        df = pd.DataFrame(vars(treasury))
        df = df[::-1]
        os.makedirs('files/ss_cmds/treasury', exist_ok=True)
        filename = f'files/ss_cmds/treasury/daily_treasury_{today_str}.csv'.replace('-','')
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
            embed.add_field(name=f"Date:", value=f"> 🗓️ **{date}**", inline=False)
            embed.add_field(name=f"Balance Info:", value=f"> **Open Balance: **${open_balance}**\n> Closing Balance: **${close_balance}**")
            embed.add_field(name=f"Change:", value=f"> **{percent_change}%**\n> Moving AVG: **{moving_avg}**")
            embed.add_field(name=f"Net Balance:", value=f"> **{amount_change}**")
            embeds.append(embed)
        select = PageSelect(embeds[:25])
        view = AlertMenus(embeds).add_item(select)

        if len(embeds) > 25:
            select2 = PageSelect2(embeds[25:50])
            view.add_item(select2)

        if len(embeds) > 50:
            select3 = PageSelect3(embeds[50:75])
            view.add_item(select3)

        if len(embeds) > 75:
            select4 = PageSelect4(embeds[75:100])
            view.add_item(select4)





        view = AlertMenus(embeds).add_item(select)
        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji="🔻", label=f"Download", row=4)
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File(filename))

        
        view.add_item(button)
        await inter.edit_original_message(embed=embeds[0], view=view)
        
    @ss.sub_command()
    async def earnings(self, inter: disnake.AppCommandInter, date_from=today_str, date_to=thirty_days_from_now_str, page="1"):
        """Returns upcoming earnings for a set amount of dates or 30 days by default."""
        await inter.response.defer()

        page = int(page)  # Convert the page argument to an integer

        earnings_cal = sdk.earnings_calendar(date_from=date_from, date_to=date_to)

        df = pd.DataFrame(vars(earnings_cal))
        filename = df.to_csv('files/ss_cmds/earnings/earnings_calendar.csv')

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
                embed = disnake.Embed(title=f"💸 Earnings Results 💸", description=f"```py\nEarnings Data - {row['date']}```", color=disnake.Colour.dark_blue())
                embeds.append(embed)
                tickers_in_embed = 0

            embed.add_field(name=f"{row['ticker']}", value=f"> ⌚ Hour: **{hour}**\n> 💸 EPS Est: **{row['eps_est']}**")
            tickers_in_embed += 1

        select = PageSelect(embeds[:25])


        view = AlertMenus(embeds).add_item(select)
        if len(embeds) > 25:
            select2 = PageSelect2(embeds[25:50])
            AlertMenus(embeds).add_item(select2)
        elif len(embeds) > 50:
            select3 = PageSelect3(embeds[50:75])
            AlertMenus(embeds).add_item(select3)
        elif len(embeds) > 75:
            select4 = PageSelect4(embeds[75:100])
            AlertMenus(embeds).add_item(select4)
        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji="🔻", label=f"Download", row=4)
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File('files/ss_cmds/earnings/earnings_calendar.csv'))

        
        view.add_item(button)
  

        await inter.edit_original_message(embed=embeds[0], view=view)

    @ss.sub_command()
    async def ftds(self, inter:disnake.AppCmdInter, symbol=str, date_from=today_str, to_date=thirty_days_from_now_str):
        """Fetch market-wide or specific ticker FTDs overall or by date."""
        await inter.response.defer()
        _fails = sdk.ftd(symbol=symbol,from_date=date_from, to_date=to_date)

        df = pd.DataFrame(vars(_fails))

        filename = 'files/ss_cmds/ftds/ftds.csv'
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
                embed = disnake.Embed(title=f"❌ Fail To Deliver ❌", description=f"```py\nDisplaying tickers with the largest amount of fails with T+35 dates as well as dollar cost.```", color=disnake.Colour.dark_blue())
                embeds.append(embed)
                tickers_in_embed = 0
            embed.add_field(name=f"{row['ticker']} {row['date']}", value=f"> Amount: **{FTD}**\n> Price: **${price}**\n> Dollar Amount: **${dollar_amount}**\n> T+35: **{t_35}**")
            tickers_in_embed += 1

        select = PageSelect(embeds[:25])
        view = AlertMenus(embeds).add_item(select)
        if len(embeds) > 25:
            select2 = PageSelect2(embeds[25:50])
            AlertMenus(embeds).add_item(select2)
        elif len(embeds) > 50:
            select3 = PageSelect3(embeds[50:75])
            AlertMenus(embeds).add_item(select3)
        elif len(embeds) > 75:
            select4 = PageSelect4(embeds[75:100])
            AlertMenus(embeds).add_item(select4)


        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji="🔻", label=f"Download", row=4)
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File(filename))

        
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
        df.to_csv('files/ss_cmds/house/house_trades.csv')
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
        if len(embeds) > 25:
            select2 = PageSelect2(embeds[25:50])
            view.add_item(select2)
        elif len(embeds) > 50:
            select3 = PageSelect3(embeds[50:75])
            view.add_item(select3)
        elif len(embeds) > 75:
            select4 = PageSelect4(embeds[75:100])
            view.add_item(select4)


        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji="🔻", label=f"Download", row=4)
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File(f'files/ss_cmds/house/house_trades.csv'))

        
        view.add_item(button)

        await inter.edit_original_message(embed=embeds[0], view=view)

    @ss.sub_command()
    async def insider_summary(self, inter:disnake.AppCmdInter):
        """Returns market-wide insider trading summary."""
        await inter.response.defer()
        insiders = sdk.latest_insider_summary()
        df = pd.DataFrame(vars(insiders))
        df.to_csv(f'files/ss_cmds/insiders/insider_summary.csv')
        embeds = []
        for i, row in df.iterrows():
            ticker=row['ticker']
            amount=float(row['amount'])
            marketcap=float(row['market_cap'])
            percent_marketcap=row['percent_of_market_cap']
            embed = disnake.Embed(title=f"🉐 Insider Trading Summary 🉐", description=f"```py\nView market-wide insider trades below.```", color=disnake.Colour.blurple())
            embed.add_field(name="Ticker:", value=f"> **{ticker}**\n> Amount: **{amount:,}**")
            embed.add_field(name=f"Market Cap:", value=f"> **{marketcap:,}**")
            embed.add_field(name=f"% of Market Cap:", value=f"> **{percent_marketcap}%**")
            embeds.append(embed)
        select = PageSelect(embeds[:25])
        view = AlertMenus(embeds).add_item(select)
        if len(embeds) > 25:
            select2 = PageSelect2(embeds[25:50])
            view.add_item(select2)
        elif len(embeds) > 50:
            select3 = PageSelect3(embeds[50:75])
            view.add_item(select3)
        elif len(embeds) > 75:
            select4 = PageSelect4(embeds[75:100])
            view.add_item(select4)




        
        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji="🔻", label=f"Download", row=4)
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File(f'files/ss_cmds/insiders/insider_summary.csv'))

        
        view.add_item(button)

        await inter.edit_original_message(embed=embeds[0], view=view)


    @ss.sub_command()
    async def short_interest(self, inter:disnake.AppCmdInter):
        """Returns tickers with the highest levels of short interest."""
        await inter.response.defer()
        short_interest = sdk.short_interest()
        df = pd.DataFrame(vars(short_interest))
        df = df[::1]
        print(df)
        df.to_csv(f'files/ss_cmds/short_interest/{ticker}_short_interest.csv')

        embeds = []
        for i, row in df.iterrows():
            rank = row['Rank']
            ticker = row['Ticker']
            date = row['Date']
            short_int = float(row['ShortInterest'])
            avg_vol = float(row['AverageVolume'])
            dtc = row['DaysToCover']
            floatshort = row['FloatShort']
            embed = disnake.Embed(title=f"🩳 Highest Short Interest 🩳", description=f"```py\nThis command is displaying the tickers with the highest amount of short interest relative to their floats. Short settlement is during the middle and beginning of each month.```", color=disnake.Colour.dark_green())
            embed.add_field(name=f"Ticker", value=f"> **{ticker}**\n> Rank: **{rank}**\n> **{date}**")
            embed.add_field(name=f"Short Interest:", value=f"> **{short_int:,}**")
            embed.add_field(name=f"Days to Cover:", value=f"> **{dtc}**\n> Avg. Volume: **{avg_vol:,}**")
            embeds.append(embed)
        select = PageSelect(embeds[:25])
        view = AlertMenus(embeds).add_item(select)
        if len(embeds) > 25:
            select2 = PageSelect2(embeds[25:50])
            view.add_item(select2)
        elif len(embeds) > 50:
            select3 = PageSelect3(embeds[50:75])
            view.add_item(select3)
        elif len(embeds) > 75:
            select4 = PageSelect4(embeds[75:100])
            view.add_item(select4)


        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji="🔻", label=f"Download",row=4)
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File(f'files/ss_cmds/short_interest/{ticker}_short_interest.csv'))

        
        view.add_item(button)

        await inter.edit_original_message(embed=embeds[0], view=view)

    @ss.sub_command()
    async def low_floats(self, inter:disnake.AppCmdInter):
        """Returns tickers with the lowest free floats."""
        await inter.response.defer()
        floats = sdk.low_float()
        df = pd.DataFrame(vars(floats))
        df = df[::1]
        df.to_csv(f'files/ss_cmds/float_data/{ticker}_low_floats.csv')
        embeds = []
        for i,row in df.iterrows():
            
            rank = row['Rank']
            ticker = row['ticker']
            company = row['company_name']
            exchange = row['exchange']
            prev_close = row['previous_close']
            oneDchange = row['one_day_change']
            floating_shares = row['floating_shares']
            outstanding_shares = row['outstanding_shares']
            short_interest = row['short_int']
            market_cap = row['market_cap']
            industry = row['industry']
            embed = disnake.Embed(title=f"🪷 Low Floats 🪷", description=f"```py\nDisplaying tickers across the market with the lowest floats as well as short interest.```", color=disnake.Colour.dark_green())
            embed.add_field(name=f"Ticker:", value=f"> **{ticker}**\n> **#{rank}**")
            embed.add_field(name=f"Company:", value=f"> **{company}**\n> Exchange: **{exchange}**")
            embed.add_field(name=f"Day Stats:", value=f"> 1d Change: **{oneDchange}**\n> Prev. Close: **${prev_close}**")
            embed.add_field(name=f"Company Shares:", value=f"> Outstanding: **{outstanding_shares}**\n> Float: **{floating_shares}**")
            embed.add_field(name=f"% Shorted:", value=f"> **{short_interest}%**")
            embed.add_field(name=f"Industry:", value=f"> **{industry}**\n> Market Cap: **{market_cap}**")
            embed.set_footer(text=f"Data Provided by Stocksera | Implemented by FUDSTOP")
    
            embeds.append(embed)
        select = PageSelect(embeds[:25])
        view = AlertMenus(embeds).add_item(select)
        if len(embeds) > 25:
            select2 = PageSelect2(embeds[25:50])
            view.add_item(select2)
        elif len(embeds) > 50:
            select3 = PageSelect3(embeds[50:75])
            view.add_item(select3)
        elif len(embeds) > 75:
            select4 = PageSelect4(embeds[75:100])
            view.add_item(select4)

        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji="🔻", label=f"Download", row=4)
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File(f'files/ss_cmds/float_data/{ticker}_low_floats.csv'))

        
        view.add_item(button)

        await inter.edit_original_message(embed=embeds[0], view=view)

    @ss.sub_command()
    async def sec_filings(self, inter:disnake.AppCmdInter, ticker):
        """Return SEC filings for a ticker."""
        await inter.response.defer()
        sec_filings = sdk.sec_fillings(ticker)
        df = pd.DataFrame(vars(sec_filings))
        print(df)
        df.to_csv(f'files/ss_cmds/sec_filings_{ticker}.csv')
        embeds = []
        for i,row in df.iterrows():
            
            Description=row['Description']
            filing_url=row['filing_url']
            Filling=row['Filling']
            FillingDate=row['FillingDate']
            report_url=row['report_url']

            embed = disnake.Embed(title=f"📖 Sec Filings - {ticker} 📖", description=f"```py\nDisplaying SEC Filings for {ticker}```", color=disnake.Colour.dark_orange())
            embed.add_field(name=f"Filing:", value=f"> **{Filling}**\n\n> **{FillingDate}**")
            embed.add_field(name=f"Description:", value=f" > **{Description}**")
            embed.add_field(name=f"Filing URL:", value=f"> **{filing_url}")
            embed.add_field(name=f"Report URL:", value=f"> **{report_url}**")
            embeds.append(embed)
        select = PageSelect(embeds[:25])
        view = AlertMenus(embeds).add_item(select)
        if len(embeds) > 25:
            select2 = PageSelect2(embeds[25:50])
            view.add_item(select2)
        elif len(embeds) > 50:
            select3 = PageSelect3(embeds[50:75])
            view.add_item(select3)
        elif len(embeds) > 75:
            select4 = PageSelect3(embeds[75:100])
            view.add_item(select4)



        
        view = AlertMenus(embeds).add_item(select)
        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji="🔻", label=f"Download", row=4)
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File(f'files/ss_cmds/sec_filings_{ticker}.csv'))

        
        view.add_item(button)

        await inter.edit_original_message(embed=embeds[0], view=view)


    @ss.sub_command()
    async def market_news(self, inter:disnake.AppCmdInter):
        """Returns market news in paginated form."""
        await inter.response.defer()
        news = sdk.market_news()
        df = pd.DataFrame(vars(news))
        df.to_csv('files/ss_cmds/news_data/market_news.csv')
        embeds = []
        for i, row in df.iterrows():
            Date = row['Date']
            Title = row['Title']
            Source = row['Source']
            URL = row['URL']
            Section = row['Section']
            embed = disnake.Embed(title=f"🌍 {Source} - {Date} 🌍", description=f"```py\n{Title}\n\n{Section}```", url=URL, color=disnake.Colour.dark_magenta())
            embeds.append(embed)
        select = PageSelect(embeds[:25])
        view = AlertMenus(embeds).add_item(select)
        if len(embeds) > 25:
            select2 = PageSelect2(embeds[25:50])
            view.add_item(select2)
        elif len(embeds) > 50:
            select3 = PageSelect3(embeds[50:75])
            view.add_item(select3)
        elif len(embeds) > 75:
            select4 = PageSelect4(embeds[75:100])
            view.add_item(select4)


        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji="🔻", label=f"Download", row=4)
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File('files/ss_cmds/news_data/market_news.csv'))

        
        view.add_item(button)
        await inter.edit_original_message(embed=embeds[0], view=view)
           
    @ss.sub_command()
    async def jobless_claims(self, interaction: disnake.AppCommandInteraction, days:str=100):
        """Returns jobless claims data."""
        await interaction.response.defer()
        jobless_claims_data = sdk.jobless_claims(days=days)
        
        df = pd.DataFrame(vars(jobless_claims_data))
        print(df)
        df = df[::-1]
        df.to_csv('files/ss_cmds/economy_data/jobless_claims.csv')
        embeds = []
        for i, row in df.iterrows():
            date = row['date']
            percent_change = row['percent_change']
            number = float(row['number'])
            embed = disnake.Embed(title=f"Jobless Claims", description=f"```py\nJobless Claims are the numbers of people who have recently lost their jobs and are requesting financial help from the government for the first time: The department said initial jobless claims fell again last week for the third week in a row.```", color=disnake.Colour.dark_red())
            embed.add_field(name=f"Date:", value=f"> **{date}**")
            embed.add_field(name=f"Results:", value=f"> Number: **{number:,}**")
            embed.add_field(name=f"% Change:", value=f"> **{percent_change}%**")
            embeds.append(embed)
        select = PageSelect(embeds[:25])
        view = AlertMenus(embeds).add_item(select)
        if len(embeds) > 25:
            select2 = PageSelect2(embeds[25:50])
            view.add_item(select2)
        elif len(embeds) > 50:
            select3 = PageSelect3(embeds[50:75])
            view.add_item(select3)
        elif len(embeds) > 75:
            select4 = PageSelect4(embeds[75:100])
            view.add_item(select4)




        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji="🔻", label=f"Download", row=4)
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File('files/ss_cmds/economy_data/jobless_claims.csv'))

        
        view.add_item(button)
        await interaction.edit_original_message(embed=embeds[0], view=view)


    @ss.sub_command()
    async def short_volume(self, inter:disnake.AppCmdInter, stock: str=commands.Param(autocomplete=ticker_autocomp), date_from=thirty_days_ago_str, to_date=today_str):
        """Returns short volume for a ticker. Enter a date range to search specific dates."""
        await inter.response.defer()
        short_volume_data = sdk.short_volume(stock=stock,date_from=date_from,to_date=to_date)
        df = pd.DataFrame(vars(short_volume_data))
        filename= f'files/ss_cmds/short_volume/short_volume_{stock}.csv'
        df.to_csv(filename)
        print(df)
        embeds = []
        for i,row in df.iterrows():
            date = row['date']
            short_vol = float(row['short_vol'])
            short_exempt_vol = float(row['short_exempt_vol'])
            total_vol = float(row['total_vol'])
            percent_shorted = row['percent_shorted']
            embed = disnake.Embed(title=f"🩳Short Volume - {stock} 🩳", description=f"```py\nView or download the short volume data for AMC below.```", color=disnake.Colour.dark_red())
            embed.add_field(name=f"Date:", value=f"> **{date}**", inline=False)
            embed.add_field(name=f"Volume Totals:", value=f"> Short: **{short_vol:,}**\n> Exempt: **{short_exempt_vol:,}**\n> Total: **{total_vol:,}**")
            embed.add_field(name=f"% Shorted:", value=f"> **{percent_shorted}%**")
            embeds.append(embed)
        select = PageSelect(embeds[:25])
        view = AlertMenus(embeds).add_item(select)
        if len(embeds) > 25:
            select2 = PageSelect2(embeds[25:50])
            view.add_item(select2)
        elif len(embeds) > 50:
            select3 = PageSelect3(embeds[50:75])
            view.add_item(select3)
        elif len(embeds) > 75:
            select4 = PageSelect4(embeds[75:100])
            view.add_item(select4)




        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji="🔻", label=f"Download", row=4)
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File(filename))

        
        view.add_item(button)
        await inter.edit_original_message(embed=embeds[0], view=view)

    @ss.sub_command()
    async def stocktwits(self, inter:disnake.AppCmdInter, stock: str=commands.Param(autocomplete=ticker_autocomp)):
        """Returns the stock's rank on StockTwits followed by # of watchlists."""
        await inter.response.defer()
        stocktwits_data = sdk.stocktwits(stock)
        df = pd.DataFrame(vars(stocktwits_data))
        filename=f'files/ss_cmds/stocktwits/stocktwits_rank_{stock}.csv'
        df.to_csv(filename)
        rank=stocktwits_data.rank[0]
        stocktwits_data.watchlist[0]
        view = disnake.ui.View()

        embed = disnake.Embed(title=f"📉 StockTwits Rank - {stock} 📈", description=f"```py\nDisplaying StockTwits rank and #of active watchlists with {stock}.```", color=disnake.Colour.dark_magenta())
        embed.add_field(name=f"Rank:", value=f"> **{rank}**")
        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji="🔻", label=f"Download", row=4)
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File(filename))

        
        view.add_item(button)
        await inter.edit_original_message(view=view, embed=embed)


    @ss.sub_command()
    async def senate(self, inter:disnake.AppCmdInter, stock=str, senator=str, date_from=thirty_days_ago_str, to_date = today_str):
        """Returns senate trades. Enter a specific ticker to search by Senator"""
        await inter.response.defer()
        senate_data = sdk.senate(ticker=stock, name=senator, date_from=date_from, date_to=to_date)
        df = pd.DataFrame(vars(senate_data))

        print(df)

    @ss.sub_command()
    async def subbredits(self, inter:disnake.AppCmdInter, stock: str=commands.Param(autocomplete=ticker_autocomp)):
        """Returns subreddit stats for a ticker."""
        await inter.response.defer()

        subbreddit_data = sdk.subreddit(stock)
        df = pd.DataFrame(vars(subbreddit_data))
        df = df[::-1]
        if stock is not None:
            filename = f"files/ss_cmds/subreddits/{stock}_subreddit_data.csv"
        else:
            filename = f"files/ss_cmds/subreddits/subreddit_data.csv"
        df.to_csv(filename)

        embeds = []
        for i,row in df.iterrows():
            Date = row['Date']
            subreddit = row['subreddit']
            Redditors = float(row['Redditors'])
            Active = float(row['Active'])
            percActive = row['percActive']
            percGrowth = row['percGrowth']
            percPriceChange = row['percPriceChange']
            embed = disnake.Embed(title=f"🗣️ Subreddit Stats - {stock} 🗣️", description=f"```py\nViewing general subreddit stats for {stock}. Click DOWNLOAD below to download the data.```", color=disnake.Colour.dark_gold())

            embed.add_field(name=f"Date:", value=f"> **{Date}**",inline=True)
            embed.add_field(name=f"Subreddit:", value=f"> **{subreddit}**")
            embed.add_field(name=f"Active:", value=f"> Redditors: **{Redditors:,}**\n> 🏃 Active: **{Active:,}**\n> % Active: **{percActive}%**")
            embed.add_field(name=f"Percent Growth:", value=f"> **{percGrowth}%**")
            embed.add_field(name=f"% Price Change:", value=f"> **{percPriceChange}%**")
            embeds.append(embed)
        select = PageSelect(embeds[:25])
        view = AlertMenus(embeds).add_item(select)
        if len(embeds) > 25:
            select2 = PageSelect2(embeds[25:50])
            view.add_item(select2)
        elif len(embeds) > 50:
            select3 = PageSelect3(embeds[50:75])
            view.add_item(select3)
        elif len(embeds) > 75:
            select4 = PageSelect4(embeds[75:100])
            view.add_item(select4)




        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji="🔻", label=f"Download", row=4)
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File(filename))

        
        view.add_item(button)
        await inter.edit_original_message(embed=embeds[0], view=view)

    @ss.sub_command()
    async def reverse_repo(self, inter:disnake.AppCmdInter, days=100):
        """Fetch and view reverse repo data. Optionally search by number of days."""
        await inter.response.defer()
        reverse_repo_data = sdk.reverse_repo(days=days)

        df = pd.DataFrame(vars(reverse_repo_data))
        filename= f"files/ss_cmds/economy_data/reverse_repo.csv"
        df.to_csv(filename)
        embeds = []
        
        for i,row in df.iterrows():

            date = row['date']
            amount = row['amount']
            num_parties = row['num_parties']
            average = row['average']
            moving_average = row['moving_average']
            embed = disnake.Embed(title=f"🪙 Reverse Repo Data 🪙", description=f"```py\nViewing reverse repo transactions, number of parties, averages, and moving averages. To download the data - click the button below.```", color=disnake.Colour.dark_teal(), url="https://www.newyorkfed.org/markets/desk-operations/reverse-repo")
            embed.add_field(name=f"Date", value=f"```py\n{date}```", inline=False)
            embed.add_field(name=f"Transaction:", value=f"> **{amount}**\n> Parties: **{num_parties}**")
            embed.add_field(name=f"Average:", value=f"> **{average}**")
            embed.add_field(name=f"Moving Average:", value=f"> **{moving_average}**")
            embeds.append(embed)
        select = PageSelect(embeds[:25])
        view = AlertMenus(embeds).add_item(select)
        if len(embeds) > 25:
            select2 = PageSelect2(embeds[25:50])
            view.add_item(select2)
        elif len(embeds) > 50:
            select3 = PageSelect3(embeds[50:75])
            view.add_item(select3)
        elif len(embeds) > 75:
            select4 = PageSelect4(embeds[75:100])
            view.add_item(select4)




        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji="🔻", label=f"Download", row=4)
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File(filename))

        
        view.add_item(button)
        await inter.edit_original_message(embed=embeds[0], view=view)

    @ss.sub_command()
    async def inflation(self, inter: disnake.AppCmdInter):
        """Prints historic inflation back to 1972"""
        await inter.response.defer()
        data = sdk.inflation()
        df = pd.DataFrame(data)
        print(df)
        df.to_csv('files/ss_cmds/economy_data/inflation.csv')
        embeds = []
        for i, row in df.iterrows():
            year = row['Year']
            jan = row['Jan']
            feb = row['Feb']
            mar = row['Mar']
            apr = row['Apr']
            may = row['May']
            jun = row['Jun']
            jul = row['Jul']
            aug = row['Aug']
            sep = row['Sep']
            oct = row['Oct']
            nov = row['Nov']
            dec = row['Dec']
            avg = row['Avg']
            embed = disnake.Embed(title=f"🎈 Inflation Data 🎈", description=f"```py\nViewing inflation data. One year of data per page. To download - click the download button below.```", color=disnake.Colour.greyple())
            embed.add_field(name=f"Year:", value=f"```py\n{year}```", inline=False)
            embed.add_field(name=f"January:", value=f"> **{jan}**")
            embed.add_field(name="Year:", value=f"```py\n{year}```", inline=False)
            embed.add_field(name="January:", value=f"> **{jan}**", inline=True)
            embed.add_field(name="February:", value=f"> **{feb}**", inline=True)
            embed.add_field(name="March:", value=f"> **{mar}**", inline=True)
            embed.add_field(name="April:", value=f"> **{apr}**", inline=True)
            embed.add_field(name="May:", value=f"> **{may}**", inline=True)
            embed.add_field(name="June:", value=f"> **{jun}**", inline=True)
            embed.add_field(name="July:", value=f"> **{jul}**", inline=True)
            embed.add_field(name="August:", value=f"> **{aug}**", inline=True)
            embed.add_field(name="September:", value=f"> **{sep}**", inline=True)
            embed.add_field(name="October:", value=f"> **{oct}**", inline=True)
            embed.add_field(name="November:", value=f"> **{nov}**", inline=True)
            embed.add_field(name="December:", value=f"> **{dec}**", inline=True)
            embed.add_field(name=f"Average for {year}:", value=f"> **{avg}**", inline=False)
            embeds.append(embed)

        select = PageSelect(embeds[:25])
        view = AlertMenus(embeds).add_item(select)

        if len(embeds) > 25:
            select2 = PageSelect2(embeds[25:50])
            view.add_item(select2)

        if len(embeds) > 50:
            select3 = PageSelect3(embeds[50:75])
            view.add_item(select3)

        if len(embeds) > 75:
            select4 = PageSelect4(embeds[75:100])
            view.add_item(select4)



        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji="🔻", label=f"Download", row=4)
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File('files/ss_cmds/economy_data/inflation.csv'))

        
        view.add_item(button)
        await inter.edit_original_message(embed=embeds[0], view=view)


    @ss.sub_command()
    async def news_sentiment(self, inter:disnake.AppCmdInter,ticker:str=commands.Param(autocomplete=ticker_autocomp), days=100):
        """Returns news sentiment surround ticker news."""
        await inter.response.defer()
        news_data = sdk.news_sentiment(ticker="GME")

        df = pd.DataFrame(vars(news_data))
        df.to_csv(f'files/ss_cmds/news_data/{ticker}_sentiment.csv')
        print(df)
        embeds = []
        for i,row in df.iterrows():
            Date = row['Date']
            Title = row['Title']
            Link = row['Link']
            Sentiment = row['Sentiment']
            if Sentiment == "Bullish":
                color =disnake.Colour.dark_green()
            elif Sentiment == "Bearish":
                color = disnake.Colour.dark_red()
            else:
                color = disnake.Colour.darker_grey()
            embed = disnake.Embed(title=f"🗞️ News Sentiment - {ticker} 🗞️", description=f"```py\nViewing news sentiment for {ticker}. To download the data - click the button below. To view the article - click the link at the top of this Embed.```",color=color, url=Link)
            embed.add_field(name=f"Date:", value=f"> **{Date}**", inline=False)
            embed.add_field(name=f"News Title:", value=f"> **{Title}**")
            embed.add_field(name=f"Sentiment:", value=f"> **{Sentiment}**")
            embeds.append(embed)

        select = PageSelect(embeds[:25])
        view = AlertMenus(embeds).add_item(select)

        if len(embeds) > 25:
            select2 = PageSelect2(embeds[25:50])
            view.add_item(select2)

        if len(embeds) > 50:
            select3 = PageSelect3(embeds[50:75])
            view.add_item(select3)

        if len(embeds) > 75:
            select4 = PageSelect4(embeds[75:100])
            view.add_item(select4)



        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, emoji="🔻", label=f"Download", row=4)
        button.callback = lambda interaction: interaction.response.send_message(file=disnake.File('files/ss_cmds/economy_data/inflation.csv'))

        
        view.add_item(button)
        await inter.edit_original_message(embed=embeds[0], view=view)
def setup(bot: commands.Bot):
    bot.add_cog(StockSera(bot))