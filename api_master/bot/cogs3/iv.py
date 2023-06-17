import disnake
from disnake.ext import commands
from api_master.cfg import YOUR_NASDAQ_KEY
from autocomp import ticker_autocomp
import requests


class IV(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def iv(inter:disnake.AppCmdInter, symbol: str = commands.Param(autocomplete=ticker_autocomp)):
        pass


    @iv.sub_command()
    async def rank(inter:disnake.AppCmdInter, symbol: str = commands.Param(autocomplete=ticker_autocomp)):
        """💉Ranks IV compared to the ticker's historic IV."""
        await inter.response.defer(with_message=True, ephemeral=True)
        r = requests.get(url=f"https://data.nasdaq.com/api/v3/datasets/QOR/{symbol}/data.json?api_key={YOUR_NASDAQ_KEY}")
        d = r.json()
        dataset = d['dataset_data']
        data = dataset['data']
        values = data[0]
        Date = values[0]
        ivrank30 = round(values[7]* 100, ndigits=2)
        ivrank60 = round(values[10]* 100, ndigits=2)
        ivrank90 = round(values[13]* 100, ndigits=2)
        ivrank90 = round(values[15]* 100, ndigits=2)
        ivrank360= round(values[16]* 100, ndigits=2)
        ivrank360 = round(values[18]* 100, ndigits=2)
        view = disnake.ui.View()
        button1 = disnake.ui.Button(label=f"📅 {Date}", style=disnake.ButtonStyle.grey)
        button2 = disnake.ui.Button(label=f"IV Rank(30): {ivrank30}%", style=disnake.ButtonStyle.blurple)
        button3 = disnake.ui.Button(label=f"IV Rank(60) {ivrank60}%", style=disnake.ButtonStyle.blurple)
        button4 = disnake.ui.Button(label=f"IV Rank(90) {ivrank90}%", style=disnake.ButtonStyle.blurple)
        button5 = disnake.ui.Button(label=f"IV Rank(360) {ivrank360}%", style=disnake.ButtonStyle.red)
        button1.callback = lambda interaction: interaction.response.edit_message(embed=embed, view=view)
        button2.callback = lambda interaction: interaction.response.edit_message(embed=embed, view=view)
        button3.callback = lambda interaction: interaction.response.edit_message(embed=embed, view=view)
        button4.callback = lambda interaction: interaction.response.edit_message(embed=embed, view=view)
        button5.callback = lambda interaction: interaction.response.edit_message(embed=embed, view=view)
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)
        view.add_item(button4)
        view.add_item(button5)
        embed = disnake.Embed(title=f" IV Rank % for {symbol}", description=f"One method for rating the current IV is to **rank it relative to its historical low/high range.** \n\n For example, if the past year of IV measurements **has ranged from a low of 20 to a high of 50, a current IV of 35 would be halfway between the low and high, producing an IV Rank of 50%.** \n\n **If the current IV were 44, then it would be 4/5 of the way from 20 to 50, resulting in an IV Rank of 80%.**", color=disnake.Colour.dark_orange())

        embed.set_footer( text="Implemented by Fudstop Trading")
        await inter.edit_original_message(embed=embed, view=view)






    @iv.sub_command()
    async def percentile(inter:disnake.AppCmdInter, symbol: str = commands.Param(autocomplete=ticker_autocomp)):
        """💉Shows the % of measurements that have been lower vs the current IV"""
        await inter.response.defer(with_message=True, ephemeral=True)
        r = requests.get(url=f"https://data.nasdaq.com/api/v3/datasets/QOR/{symbol}/data.json?api_key={YOUR_NASDAQ_KEY}")
        d = r.json()
        dataset = d['dataset_data']
        data = dataset['data']
        column_names = dataset['column_names']
        Date = column_names[0]
        values = data[0]
        Date = values[0]
        ivper30 = round(values[8] * 100, ndigits=2)
        ivper60 = round(values[11]* 100, ndigits=2)
        ivper90 = round(values[14]* 100, ndigits=2)
        ivper360 = round(values[17]* 100, ndigits=2)
        ivperavg = round((ivper30 + ivper60 + ivper90 + ivper360) / 4, ndigits=2)
        view = disnake.ui.View()
        button1 = disnake.ui.Button(label=f"Updated: {Date}", style=disnake.ButtonStyle.grey)
        button2 = disnake.ui.Button(label=f"IV Percentile(30): {ivper30}%", style=disnake.ButtonStyle.blurple)
        button3 = disnake.ui.Button(label=f"IV Percentile(60): {ivper60}%", style=disnake.ButtonStyle.blurple)
        button4 = disnake.ui.Button(label=f"IV Percentile(90): {ivper90}%", style=disnake.ButtonStyle.blurple)
        button5 = disnake.ui.Button(label=f"IV Percentile(360): {ivper360}%", style=disnake.ButtonStyle.blurple)
        button6 = disnake.ui.Button(label=f"IV Percentile(Average): {ivper360}%", style=disnake.ButtonStyle.blurple)
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)
        view.add_item(button4)
        view.add_item(button5)
        embed = disnake.Embed(title=f"IV Percentile for {symbol}", description=f"Another method for rating the current IV is to rank it relative to all IV measurements over the historical term. \n\n For example, **if half of the past year’s measurements of IV have been lower than the current IV, then the current IV Percentile would be 50%.** \n\n** If only 20% of the measurements were below the current IV, then the IV Percentile would be 20%.** \n\n This approach effectively accounts for the density of historical measurements.", color=disnake.Colour.dark_orange())

        embed.set_footer( text="Implemented by Fudstop Trading")
        await inter.edit_original_message(embed=embed, view=view)

    @iv.sub_command()
    async def parkinson(inter:disnake.AppCmdInter, symbol: str = commands.Param(autocomplete=ticker_autocomp)):
        """💉Returns Parkinsons HV for a ticker."""
        await inter.response.defer(with_message=True, ephemeral=True)
        r = requests.get(url=f"https://data.nasdaq.com/api/v3/datasets/QOR/{symbol}/data.json?api_key={YOUR_NASDAQ_KEY}")
        d = r.json()
        dataset = d['dataset_data']
        data = dataset['data']
        values = data[0]
        column_names = dataset['column_names']
        Date = values[0]
        ercrush = values[1]
        calendar = values[2]
        tradingdays = values[3]
        liquidity = values[4]
        leaps = values[5]
        weeklies = values[6]
        ivrank30 = round(values[7]* 100, ndigits=2)
        ivper30 = round(values[8] * 100, ndigits=2)
        ivrate30 = round(values[9]* 100, ndigits=2)
        ivrank60 = round(values[10]* 100, ndigits=2)
        ivper60 = round(values[11]* 100, ndigits=2)
        ivrate60 =round(values[12]* 100, ndigits=2)
        ivrank90 = round(values[13]* 100, ndigits=2)
        ivper90 = round(values[14]* 100, ndigits=2)
        ivrank90 = round(values[15]* 100, ndigits=2)
        ivrank360= round(values[16]* 100, ndigits=2)
        ivper360 = round(values[17]* 100, ndigits=2)
        ivrank360 = round(values[18]* 100, ndigits=2)
        phv10 = round(values[9]*100, ndigits=2)
        phv20 = round(values[10]* 100, ndigits=2)
        phv30 = round(values[11]* 100, ndigits=2)
        phv60 = round(values[12]* 100, ndigits=2)
        phv90 = round(values[13]* 100, ndigits=2)
        phv120 = round(values[14]* 100, ndigits=2)
        phv150 =round(values[15]* 100, ndigits=2)
        phv180 = round(values[16]* 100, ndigits=2)

        Date = values[0]
        view = disnake.ui.View()
        button1 = disnake.ui.Button(label=f"📅 {Date}", style=disnake.ButtonStyle.grey)
        button2 = disnake.ui.Button(label=f"PHV (10 Day): {phv10}%", style=disnake.ButtonStyle.blurple)
        button3 = disnake.ui.Button(label=f"PHV (20 Day): {phv20}%", style=disnake.ButtonStyle.blurple)
        button4 = disnake.ui.Button(label=f"PHV (30 Day): {phv30}%", style=disnake.ButtonStyle.blurple)
        button5 = disnake.ui.Button(label=f"PHV (60 Day): {phv60}%", style=disnake.ButtonStyle.blurple)
        button6 = disnake.ui.Button(label=f"PHV (90 Day): {phv90}%", style=disnake.ButtonStyle.blurple)
        button7 = disnake.ui.Button(label=f"PHV (120 Day): {phv120}%", style=disnake.ButtonStyle.blurple)
        button8 = disnake.ui.Button(label=f"PHV (150 Day): {phv150}%", style=disnake.ButtonStyle.blurple)
        button8 = disnake.ui.Button(label=f"PHV (180 Day): {phv180}%", style=disnake.ButtonStyle.blurple)
        button1.callback = lambda interaction: interaction.response.edit_message(embed=embed, view=view)
        button2.callback = lambda interaction: interaction.response.edit_message(embed=embed, view=view)
        button3.callback = lambda interaction: interaction.response.edit_message(embed=embed, view=view)
        button4.callback = lambda interaction: interaction.response.edit_message(embed=embed, view=view)
        button5.callback = lambda interaction: interaction.response.edit_message(embed=embed, view=view)
        button6.callback = lambda interaction: interaction.response.edit_message(embed=embed, view=view)
        button7.callback = lambda interaction: interaction.response.edit_message(embed=embed, view=view)
        button8.callback = lambda interaction: interaction.response.edit_message(embed=embed, view=view)
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)
        view.add_item(button4)
        view.add_item(button5)
        view.add_item(button6)
        view.add_item(button7)
        view.add_item(button8)
        embed = disnake.Embed(title=f"Parkinson's Historical Volatility for {symbol}", description=f"**Parkinson volatility** *(Phv, such as Phv10, etc)* is calculated using the **high and low prices of the stock on each trading day for a calendar period leading up to the most recent trading close.** \n\n Parkinson volatility, a historical volatility measure calculated using the high and low prices of the stock on each trading day for over approximately n calendar days leading up to the most recent trading close.", color=disnake.Colour.dark_orange())
        embed.add_field(name="Calendar Days", value="10\n20\n30\n60\n90\n120\n150\n180", inline=True)
        embed.add_field(name="Trading Days", value="7\n14\n21\n41\n62\n83\n104\n124")

        embed.set_footer( text="Implemented by Fudstop Trading")
        await inter.edit_original_message(embed=embed, view=view)

def setup(bot):
    bot.add_cog(IV(bot))
    print(f"> Extension {__name__} is ready\n")