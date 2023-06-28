import disnake
from disnake.ext import commands
from autocomp import ticker_autocomp
import pandas as pd
from cfg import YOUR_API_KEY
from sdks.fmp_sdk.sdk import fmpSDK
from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
from menus.embedmenus import AlertMenus
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK

poly = AsyncPolygonSDK(YOUR_API_KEY)
webull = AsyncWebullSDK()
sdk = fmpSDK()
class FMP(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot=bot



    @commands.slash_command()
    async def fmp(inter, self):
        pass



    @fmp.sub_command(name="price_target")
    async def price_target(self, inter:disnake.AppCmdInter, ticker:str=commands.Param(autocomplete=ticker_autocomp)):
        """Fetch latest price target and historic targets for a ticker."""
        await inter.response.defer()
        

        x = await sdk.price_target(ticker)
        price_data = await webull.get_webull_stock_data(ticker)
        price = float(price_data.web_stock_close)
        df = pd.DataFrame(vars(x))
        filename = f'files/fmp_cmds/price_targets/{ticker}_price_target.csv'
        df.to_csv(filename)
        embeds = []
        for i,row in df.iterrows():
            symbol = row['symbol']
            pub_date = row['pub_date']
            news_url = row['news_url']
            news_title = row['news_title']
            analyst_name = row['analyst_name']
            target = row['target']
            adjusted_target = row['adjusted_target']
            pwp = row['price_when_posted']
            news_publisher = row['news_publisher']
            newsbase_url = row['newsbase_url']
            analyst_company = row['analyst_company']

            embed = disnake.Embed(title=f"🎯 Price Target - {ticker} 🎯", description=f"```py\nViewing the latest price target for {ticker}. To view previous - use the arrows below or download the spreadsheet.```", color=disnake.Colour.dark_teal())
            embed.add_field(name=f"Published Date:", value=f"> **{pub_date}**\n> Publisher: **{news_publisher}**")
            embed.add_field(name=f"News URL:", value=f"> **{news_url}**\n> News Base: **{newsbase_url}**\n> News Title: **{news_title}**", inline=False)
            embed.add_field(name=f"Price Target:", value=f"> **${target}**\n> Adjusted Target: **${adjusted_target}**")
            embed.add_field(name=f"Price When Posted:", value=f"> PWP: **${pwp}**\n> NOW: **${price}**")
            embed.add_field(name=f"Analyst:", value=f"> **{analyst_name}**\n> Company: **{analyst_company}*")
            embed.set_footer(text=f"Implemented by FUDSTOP")
            embed.set_thumbnail(await poly.get_polygon_logo(ticker))
            embeds.append(embed)
        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, label=f"Download")
        button.callback = lambda interaction: interaction.send(file=disnake.File(filename))
        view = AlertMenus(embeds).add_item(button)

        await inter.edit_original_message(embed=embeds[0], view=view)



    @fmp.sub_command()
    async def country_risk_premium(self, inter:disnake.AppCmdInter):
        """Shows risk premium by country and continent."""
        await inter.response.defer()
        country_premium = await sdk.country_risk_premium()
        data_dict = { 

            'Country': country_premium.country,
            'Continent': country_premium.continent,
            'Total Equity Risk Premium': country_premium.totalEquityRiskPremium,
            'Country Risk Premium': country_premium.countryRiskPremium
        }

        df = pd.DataFrame(data_dict).sort_values('Country Risk Premium', ascending=False)
        filename = f'files/fmp_cmds/country_risk_premium.csv'
        embeds = []
        for i,row in df.iterrows():
            country = row['Country']
            continent = row['Continent']
            totalequity = float(row['Total Equity Risk Premium'])
            countryprem = float(row['Country Risk Premium'])
            embed = disnake.Embed(title=f"Global Risk Premium", description=f"```py\nThis command is returning risk premium by country as well as total equity risk premium - sorted by most to least risk.```", color=disnake.Colour.dark_magenta())
            embed.add_field(name=f"Country & Continent:", value=f"> **{country}**\n> **{continent}**")
            embed.add_field(name=f"Equity Risk Premium:", value=f"> **{totalequity}**")
            embed.add_field(name=f"Country Risk Premium:", value=f"> **{countryprem}**")
            embeds.append(embed)
        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple, label=f"Download")
        button.callback = lambda interaction: interaction.send(file=disnake.File(filename))
        view = AlertMenus(embeds).add_item(button)

        await inter.edit_original_message(embed=embeds[0], view=view)     


def setup(bot: commands.Bot):
    """SETUP COG"""
    bot.add_cog(FMP(bot))
    print(f"> Extension {__name__} is ready\n")
