import disnake
import stocksera
from api_master.cfg import YOUR_STOCKSERA_KEY
from utils.webull_tickers import ticker_list
client = stocksera.Client(api_key=YOUR_STOCKSERA_KEY)
class FTDStocksDropdown(disnake.ui.Select):
    def __init__(self):
        data = client.ftd()
        index0 = data[0]
        index1 = data[1]
        index2 = data[2]
        index3 = data[3]
        index4 = data[4]
        index5 = data[5]
        index6 = data[6]
        index7 = data[7]
        index8 = data[8]
        index9 = data[9]
        index10 = data[10]
        index11 = data[11]
        index12 = data[12]
        index13 = data[13]
        index14 = data[14]
        t350 = index0['T+35 Date']
        t351 = index1['T+35 Date']
        t352 = index2['T+35 Date']
        t353 = index3['T+35 Date']
        t354 = index4['T+35 Date']
        t355 = index5['T+35 Date']
        t356 = index6['T+35 Date']
        t357 = index7['T+35 Date']
        t358 = index8['T+35 Date']
        t359 = index9['T+35 Date']
        t3510 = index10['T+35 Date']
        t3511 = index11['T+35 Date']
        t3512 = index12['T+35 Date']
        t3513 = index13['T+35 Date']
        t3514 = index14['T+35 Date']
        symbol0 = index0['Ticker']
        symbol1 = index1['Ticker']
        symbol2 = index2['Ticker']
        symbol3 = index3['Ticker']
        symbol4 = index4['Ticker']
        symbol5 = index5['Ticker']
        symbol6 = index6['Ticker']
        symbol7 = index7['Ticker']
        symbol8 = index8['Ticker']
        symbol9 = index9['Ticker']
        symbol10 = index10['Ticker']
        symbol11 = index11['Ticker']
        symbol12 = index12['Ticker']
        symbol13 = index13['Ticker']
        symbol14 = index14['Ticker']

        options = [
            disnake.SelectOption(label=f"{symbol0} | T35 🗓️ Date: {t350}"),
            disnake.SelectOption(label=f"{symbol1} | T35 🗓️ Date: {t351}"),
            disnake.SelectOption(label=f"{symbol2} | T35 🗓️ Date: {t352}"),
            disnake.SelectOption(label=f"{symbol3} | T35 🗓️ Date: {t353}"),
            disnake.SelectOption(label=f"{symbol4} | T35 🗓️ Date: {t354}"),
            disnake.SelectOption(label=f"{symbol5} | T35 🗓️ Date: {t355}"),
            disnake.SelectOption(label=f"{symbol6} | T35 🗓️ Date: {t356}"),
            disnake.SelectOption(label=f"{symbol7} | T35 🗓️ Date: {t357}"),
            disnake.SelectOption(label=f"{symbol8} | T35 🗓️ Date: {t358}"),
            disnake.SelectOption(label=f"{symbol9} | T35 🗓️ Date: {t359}"),
            disnake.SelectOption(label=f"{symbol10} | T35 🗓️ Date: {t3510}"),
            disnake.SelectOption(label=f"{symbol11} | T35 🗓️ Date: {t3511}"),
            disnake.SelectOption(label=f"{symbol12} | T35 🗓️ Date: {t3512}"),
            disnake.SelectOption(label=f"{symbol13} | T35 🗓️ Date: {t3513}"),
            disnake.SelectOption(label=f"{symbol14} | T35 🗓️ Date: {t3514}"),

        ]
        super().__init__(
            placeholder = "🇫 🇹 🇩 🇸",
            min_values = 1,
            max_values = 1,
            options = options
        )
    async def callback(self, interaction:disnake.MessageCommandInteraction):
        await interaction.send("Soon dad or mom, soon!")





class FTDStocks(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(FTDStocksDropdown())

        data = client.ftd()
        index0 = data[0]
        index1 = data[1]
        index2 = data[2]
        index3 = data[3]
        index4 = data[4]
        index5 = data[5]
        index6 = data[6]
        index7 = data[7]
        index8 = data[8]
        index9 = data[9]
        index10 = data[10]
        index11 = data[11]
        index12 = data[12]
        index13 = data[13]
        index14 = data[14]
        t350 = index0['T+35 Date']
        t351 = index1['T+35 Date']
        t352 = index2['T+35 Date']
        t353 = index3['T+35 Date']
        t354 = index4['T+35 Date']
        t355 = index5['T+35 Date']
        t356 = index6['T+35 Date']
        t357 = index7['T+35 Date']
        t358 = index8['T+35 Date']
        t359 = index9['T+35 Date']
        t3510 = index10['T+35 Date']
        t3511 = index11['T+35 Date']
        t3512 = index12['T+35 Date']
        t3513 = index13['T+35 Date']
        t3514 = index14['T+35 Date']
        symbol0 = index0['Ticker']
        symbol1 = index1['Ticker']
        symbol2 = index2['Ticker']
        symbol3 = index3['Ticker']
        symbol4 = index4['Ticker']
        symbol5 = index5['Ticker']
        symbol6 = index6['Ticker']
        symbol7 = index7['Ticker']
        symbol8 = index8['Ticker']
        symbol9 = index9['Ticker']
        symbol10 = index10['Ticker']
        symbol11 = index11['Ticker']
        symbol12 = index12['Ticker']
        symbol13 = index13['Ticker']
        symbol14 = index14['Ticker']

        @disnake.ui.button(label=f"#1: {symbol0} | T35 Date: 🗓️ {t350}", style= disnake.ButtonStyle.grey)
        async def button1(self,inter: disnake.AppCmdInter):
            em = disnake.Embed(title=f"Stocks with high FTDS", description=f"```py\nTop 15 FTDs with t35 Dates``````", color = disnake.Colour.dark_orange())


            await inter.response.edit_message(embed=em, view=FTDStocks())

        @disnake.ui.button(label=f"#2: {symbol1} | T35 Date: 🗓️ {t351}", style= disnake.ButtonStyle.grey)
        async def button2(self,inter: disnake.AppCmdInter):
            em = disnake.Embed(title=f"Stocks with high FTDS", description=f"```py\nTop 15 FTDs with t35 Dates``````", color = disnake.Colour.dark_orange())
            em.set_footer( text="Implemented by Fudstop Trading, Data Provided By Apperate")

            await inter.response.edit_message(embed=em, view=FTDStocks())

        @disnake.ui.button(label=f"#3: {symbol2} | T35 Date: 🗓️ {t352}", style= disnake.ButtonStyle.grey)
        async def button3(self,inter: disnake.AppCmdInter):
            em = disnake.Embed(title=f"Stocks with high FTDS", description=f"```py\nTop 15 FTDs with t35 Dates```", color = disnake.Colour.dark_orange())
            em.set_footer( text="Implemented by Fudstop Trading, Data Provided By Apperate")

            await inter.response.edit_message(embed=em, view=FTDStocks())

        @disnake.ui.button(label=f"#4: {symbol3} | T35 Date: 🗓️{t353}", style= disnake.ButtonStyle.grey)
        async def button4(self,inter: disnake.AppCmdInter):
            em = disnake.Embed(title=f"Stocks with high FTDS", description=f"```py\nTop 15 FTDs with t35 Dates```", color = disnake.Colour.dark_orange())
            em.set_footer( text="Implemented by Fudstop Trading, Data Provided By Apperate")

            await inter.response.edit_message(embed=em, view=FTDStocks())

        @disnake.ui.button(label=f"#5: {symbol4} | T35 Date: {t354}", style= disnake.ButtonStyle.grey)
        async def button5(self,inter: disnake.AppCmdInter):
            em = disnake.Embed(title=f"Stocks with high FTDS", description=f"```py\nTop 15 FTDs with t35 Dates```", color = disnake.Colour.dark_orange())
            em.set_footer( text="Implemented by Fudstop Trading, Data Provided By Apperate")

            await inter.response.edit_message(embed=em, view=FTDStocks())

        @disnake.ui.button(label=f"#6: {symbol5} | T35 Date: 🗓️ {t355}", style= disnake.ButtonStyle.grey)
        async def button6(self,inter: disnake.AppCmdInter):
            em = disnake.Embed(title=f"Stocks with high FTDS", description=f"```py\nTop 15 FTDs with t35 Dates```", color = disnake.Colour.dark_orange())
            em.set_footer( text="Implemented by Fudstop Trading, Data Provided By Apperate")

            await inter.response.edit_message(embed=em, view=FTDStocks())

        @disnake.ui.button(label=f"#7: {symbol6} | T35 Date: 🗓️ {t356}", style= disnake.ButtonStyle.grey)
        async def button7(self,inter: disnake.AppCmdInter):
            em = disnake.Embed(title=f"Stocks with high FTDS", description=f"```py\nTop 15 FTDs with t35 Dates```", color = disnake.Colour.dark_orange())
            em.set_footer( text="Implemented by Fudstop Trading, Data Provided By Apperate")

            await inter.response.edit_message(embed=em, view=FTDStocks())

        @disnake.ui.button(label=f"#8: {symbol7} | T35 Date: 🗓️ {t357}", style= disnake.ButtonStyle.grey)
        async def button9(self,inter: disnake.AppCmdInter):
            em = disnake.Embed(title=f"Stocks with high FTDS", description=f"```py\nTop 15 FTDs with t35 Dates```", color = disnake.Colour.dark_orange())
            em.set_footer( text="Implemented by Fudstop Trading, Data Provided By Apperate")

            await inter.response.edit_message(embed=em, view=FTDStocks())

        @disnake.ui.button(label=f"#9: {symbol8} | T35 Date: 🗓️ {t358}", style= disnake.ButtonStyle.grey)
        async def button10(self,inter: disnake.AppCmdInter):
            em = disnake.Embed(title=f"Stocks with high FTDS", description=f"```py\nTop 15 FTDs with t35 Dates```", color = disnake.Colour.dark_orange())
            em.set_footer( text="Implemented by Fudstop Trading, Data Provided By Apperate")

            await inter.response.edit_message(embed=em, view=FTDStocks())

        @disnake.ui.button(label=f"#10: {symbol9} | T35 Date: 🗓️ {t359}", style= disnake.ButtonStyle.grey)
        async def buttona(self,inter: disnake.AppCmdInter):
            em = disnake.Embed(title=f"Stocks with high FTDS", description=f"```py\nTop 15 FTDs with t35 Dates```", color = disnake.Colour.dark_orange())
            em.set_footer( text="Implemented by Fudstop Trading, Data Provided By Apperate")

            await inter.response.edit_message(embed=em, view=FTDStocks())

        @disnake.ui.button(label=f"#11: {symbol10} | T35 Date: 🗓️ {t3510}", style= disnake.ButtonStyle.grey)
        async def buttonb(self,inter: disnake.AppCmdInter):
            em = disnake.Embed(title=f"Stocks with high FTDS", description=f"```py\nTop 15 FTDs with t35 Dates```", color = disnake.Colour.dark_orange())
            em.set_footer( text="Implemented by Fudstop Trading, Data Provided By Apperate")

            await inter.response.edit_message(embed=em, view=FTDStocks())
        @disnake.ui.button(label=f"#12: {symbol11} | T35 Date: 🗓️ {t3511}", style= disnake.ButtonStyle.grey)
        async def buttonc(self,inter: disnake.AppCmdInter):
            em = disnake.Embed(title=f"Stocks with high FTDS", description=f"```py\nTop 15 FTDs with t35 Dates```", color = disnake.Colour.dark_orange())
            em.set_footer( text="Implemented by Fudstop Trading, Data Provided By Apperate")

            await inter.response.edit_message(embed=em, view=FTDStocks())

        @disnake.ui.button(label=f"#13: {symbol12} | T35 Date: 🗓️ {t3512}", style= disnake.ButtonStyle.grey)
        async def buttone(self,inter: disnake.AppCmdInter):
            em = disnake.Embed(title=f"Stocks with high FTDS", description=f"```py\nTop 15 FTDs with t35 Dates```", color = disnake.Colour.dark_orange())
            em.set_footer( text="Implemented by Fudstop Trading, Data Provided By Apperate")

            await inter.response.edit_message(embed=em, view=FTDStocks())

        @disnake.ui.button(label=f"#14: {symbol13} | T35 Date: 🗓️ {t3513}", style= disnake.ButtonStyle.grey)
        async def buttond(self,inter: disnake.AppCmdInter):
            em = disnake.Embed(title=f"Stocks with high FTDS", description=f"```py\nTop 15 FTDs with t35 Dates```", color = disnake.Colour.dark_orange())
            em.set_footer( text="Implemented by Fudstop Trading, Data Provided By Apperate")

            await inter.response.edit_message(embed=em, view=FTDStocks())

        @disnake.ui.button(label=f"#15: {symbol14} | T35 Date: 🗓️ {t3514}", style= disnake.ButtonStyle.grey)
        async def buttonf(self, inter: disnake.AppCmdInter):
            em = disnake.Embed(title=f"Stocks with high FTDS", description=f"```py\nTop 15 FTDs with t35 Dates```", color = disnake.Colour.dark_orange())
            em.set_footer( text="Implemented by Fudstop Trading, Data Provided By Apperate")

            await inter.response.edit_message(embed=em, view=FTDStocks())