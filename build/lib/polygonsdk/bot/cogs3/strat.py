"""STRAT COMMANDS"""
import disnake
import stocksera
import webull
from disnake.ext import commands
from views.learnviews import Dividend
from cfg import YOUR_STOCKSERA_KEY

client = stocksera.Client(api_key=YOUR_STOCKSERA_KEY)


class Strat(commands.Cog):
    """STRATEGY COG"""
    def __init__(self, bot):
        self.bot = bot



    @commands.slash_command()
    async def strat(self,inter):
        """PARENT"""


    @strat.sub_command()
    async def core(self, inter: disnake.AppCmdInter):
        """🟢Returns the core logic play screeners.🔴"""
        await inter.response.defer(with_message=True, ephemeral=True)
        view = disnake.ui.View()
        emb = disnake.Embed(title="Run the core screener.", description="Check the results for gaps and play ITM. Exit if pushed out of the money. Not financial advice.", color = disnake.Colour.dark_gold())
        emb.set_footer( text="Implemented by Fudstop Trading")

        screener = disnake.ui.Button(label="🏃‍♂️ 🇨  🇦  🇱  🇱  🇸  🟢", style=disnake.ButtonStyle.link, url="https://www.alphaquery.com/stock-screener/600010230?run=1", row=0)
        screener2 = disnake.ui.Button(label="🇵  🇺  🇹  🇸  🔴", style= disnake.ButtonStyle.link, url="https://www.alphaquery.com/stock-screener/600010229?run=1", row=0)
        view.add_item(screener)
        view.add_item(screener2)
        emb = disnake.Embed(title="🔴Core Plays🟢",description="```py\n PLEASE DO NOT JUST JUMP IN TRADES. BE RESPONSIBLE AND VERIFY THESE TICKERS MEET CRITERIA. JUST BECAUSE THE TICKERS ARE IN THIS DROPDOWN DOES NOT AUTOMATICALLY MEAN THEY ARE CORE PLAYS. YOU MUST VIEW EACH TICKER TO ENSURE DAILY GAPS EXIST ON THE CHART.```", color=disnake.Colour.dark_orange())
        await inter.edit_original_message(view=view, embed=emb)


    @strat.sub_command()
    async def low_float(self,inter:disnake.AppCmdInter):
        """🟢Returns tickers with low floats. Good candidates for share plays."""
        await inter.response.defer(with_message=True, ephemeral=True)
        data = client.low_float()[0:20]
        items = "\n".join(f"```py\n#{i['Rank']} {i['ticker']} {i['company_name']} 1Day Change:${i['one_day_change']}``` ```py\n Float Shares: {i['floating_shares']}\nOutstanding Shares:{i['outstanding_shares']}``` ```py\n shortInterest: {i['short_int']} Mkt Cap:{i['market_cap']} Industry:{i['industry']}```" for i in data)
        emb = disnake.Embed(title="Low Float Tickers and Short Interest", description=f"{items}",color=disnake.Colour.dark_orange())
        await inter.edit_original_message(embed = emb)

    @strat.sub_command()
    async def dividend(self,inter:disnake.AppCmdInter):
        """🔴 Returns tickers with their EX-DIV Dates for PUTS."""
        await inter.response.defer(with_message=True)
        wbb = webull.webull()
        option_chain = wbb.get_calendar_events(event="dividend")
        data = option_chain['data']
        ticker = [i['ticker'] for i in data]
        values = [i['values'] for i in data]
        ex1 = values[0]
        ex2 = values[1]
        ex3 = values[2]
        ex4 = values[3]
        ex5 = values[4]
        ex6 = values[5]
        ex7 = values[6]
        ex8 = values[7]
        ex9 = values[8]
        ex10 = values[9]
        ex11 = values[10]
        ex12 = values[11]
        ex13 = values[12]
        ex14 = values[13]
        ex15 = values[14]
        ex16 = values[15]
        ex17 = values[16]
        ex18 = values[17]
        ex19 = values[18]
        ex20 = values[19]
        ex21 = values[20]
        ex22 = values[21]
        ex23 = values[22]
        ex24 = values[23]
        exdate1 = ex1['exDate']
        exdate2 = ex2['exDate']
        exdate3 = ex3['exDate']
        exdate4 = ex4['exDate']
        exdate5 = ex5['exDate']
        exdate6 = ex6['exDate']
        exdate7 = ex7['exDate']
        exdate8 = ex8['exDate']
        exdate9 = ex9['exDate']
        exdate10 = ex10['exDate']
        exdate11 = ex11['exDate']
        exdate12 = ex12['exDate']
        exdate13 = ex13['exDate']
        exdate14 = ex14['exDate']
        exdate15 = ex15['exDate']
        exdate16 = ex16['exDate']
        exdate17 = ex17['exDate']
        exdate18 = ex18['exDate']
        exdate19 = ex19['exDate']
        exdate20 = ex20['exDate']
        exdate21 = ex21['exDate']
        exdate22 = ex22['exDate']
        exdate23 = ex23['exDate']
        exdate24 = ex24['exDate']
        sym1 = ticker[0]
        sym2 = ticker[1]
        sym3 = ticker[2]
        sym4 = ticker[3]
        sym5 = ticker[4]
        sym6 = ticker[5]
        sym7 = ticker[6]
        sym8 = ticker[7]
        sym9 = ticker[8]
        sym10 = ticker[9]
        sym11 = ticker[10]
        sym12 = ticker[11]
        sym13 = ticker[12]
        sym14 = ticker[13]
        sym15 = ticker[14]
        sym16 = ticker[15]
        sym17 = ticker[16]
        sym18 = ticker[17]
        sym19 = ticker[18]
        sym20 = ticker[19]
        sym21 = ticker[20]
        sym22 = ticker[21]
        sym23 = ticker[22]
        sym24 = ticker[23]
        symbol1 = sym1['disSymbol']
        symbol2 = sym2['disSymbol']
        symbol3 = sym3['disSymbol']
        symbol4 = sym4['disSymbol']
        symbol5 = sym5['disSymbol']
        symbol6 = sym6['disSymbol']
        symbol7 = sym7['disSymbol']
        symbol8 = sym8['disSymbol']
        symbol9 = sym9['disSymbol']
        symbol10 = sym10['disSymbol']
        symbol11 = sym11['disSymbol']
        symbol12 = sym12['disSymbol']
        symbol13 = sym13['disSymbol']
        symbol14 = sym14['disSymbol']
        symbol15 = sym15['disSymbol']
        symbol16 = sym16['disSymbol']
        symbol17 = sym17['disSymbol']
        symbol18 = sym18['disSymbol']
        symbol19 = sym19['disSymbol']
        symbol20 = sym20['disSymbol']
        symbol21 = sym21['disSymbol']
        symbol22 = sym22['disSymbol']
        symbol23 = sym23['disSymbol']
        symbol24 = sym24['disSymbol']
        select = Dividend(
            placeholder="🇩 🇮 🇻 🇮 🇩 🇪 🇳 🇩 🔴 🇵 🇱 🇦 🇾 🇸",
            min_values=1,
            max_values=1,
            custom_id="dividends",
            options= [
            disnake.SelectOption( label=f"{symbol1}", description=f"🗓️ {exdate1}"),
            disnake.SelectOption( label=f"{symbol2}", description=f"🗓️ {exdate2}"),
            disnake.SelectOption( label=f"{symbol3}", description=f"🗓️ {exdate3}"),
            disnake.SelectOption( label=f"{symbol4}", description=f"🗓️ {exdate4}"),
            disnake.SelectOption( label=f"{symbol5}", description=f"🗓️ {exdate5}"),
            disnake.SelectOption( label=f"{symbol6}", description=f"🗓️ {exdate6}"),
            disnake.SelectOption( label=f"{symbol7}", description=f"🗓️ {exdate7}"),
            disnake.SelectOption( label=f"{symbol8}", description=f"🗓️ {exdate8}"),
            disnake.SelectOption( label=f"{symbol9}", description=f"🗓️ {exdate9}"),
            disnake.SelectOption( label=f"{symbol10}", description=f"🗓️ {exdate10}"),
            disnake.SelectOption( label=f"{symbol11}", description=f"🗓️ {exdate11}"),
            disnake.SelectOption( label=f"{symbol12}", description=f"🗓️ {exdate12}"),
            disnake.SelectOption( label=f"{symbol13}", description=f"🗓️ {exdate13}"),
            disnake.SelectOption( label=f"{symbol14}", description=f"🗓️{exdate14}"),
            disnake.SelectOption( label=f"{symbol15}", description=f"🗓️{exdate15}"),
            disnake.SelectOption( label=f"{symbol16}", description=f"🗓️{exdate16}"),
            disnake.SelectOption( label=f"{symbol17}", description=f"🗓️ {exdate17}"),
            disnake.SelectOption( label=f"{symbol18}", description=f"🗓️{exdate18}"),
            disnake.SelectOption( label=f"{symbol19}", description=f"🗓️{exdate19}"),
            disnake.SelectOption( label=f"{symbol20}", description=f"🗓️{exdate20}"),
            disnake.SelectOption( label=f"{symbol21}", description=f"🗓️{exdate21}"),
            disnake.SelectOption( label=f"{symbol22}", description=f"🗓️{exdate22}"),
            disnake.SelectOption( label=f"{symbol23}", description=f"🗓️{exdate23}"),
            disnake.SelectOption( label=f"{symbol24}", description=f"{exdate24}"),])
        view = disnake.ui.View()
        view.add_item(select)
        emb = disnake.Embed(title="Dividend Opportunities", description=f"```py\nEx-Div plays are ideal for PUTS as puts tend to increase in value following the Ex-Div Date!```\n\n```py\n{symbol1} : {exdate1} |"
        f"{symbol2} : {exdate2} | {symbol3} : {exdate3}\n\n{symbol4} : {exdate4} | {symbol5} : {exdate5} | {symbol6} : {exdate6}\n\n{symbol7} : {exdate7} | {symbol8} : {exdate8} | {symbol9} : {exdate9}\n\n"
        f"{symbol10} : {exdate10} | {symbol11} : {exdate11} | {symbol12} : {exdate12}\n\n{symbol13} : {exdate13} | {symbol14} : {exdate14} | {symbol15} : {exdate15}\n\n"
        f"{symbol16} : {exdate16} | {symbol17} : {exdate17} | {symbol18} : {exdate18}\n\n{symbol19} : {exdate19} | {symbol20} | {exdate20}```", color=disnake.Colour.dark_red())
        emb.add_field(name="Note", value="```py\nDon't just automatically purchase puts becaue you see them here. Be responsible and make sure you look at open interest, IV, and other metrics you'd normally look at before entering into an options play. If you need help - PAPER TRADE - or learn the core logic.``` </learn core_logic:1030928638905958521>")
        await inter.edit_original_message(view=view, embed=emb)

def setup(bot):
    """LOAD"""
    bot.add_cog(Strat(bot))
    print(f"> Extension {__name__} is ready\n")
