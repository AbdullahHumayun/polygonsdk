import disnake
from disnake.ext import commands
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY
from autocomp import ticker_autocomp

poly = AsyncPolygonSDK(YOUR_API_KEY)



class TA(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot=bot



    @commands.slash_command()
    async def ta(self, inter):
        pass



    @ta.sub_command(name="rsi_snapshot")
    async def rsi_snapshot(self, inter:disnake.AppCmdInter, ticker:str=commands.Param(autocomplete=ticker_autocomp)):
        """Returns the RSI value across all time-spans for a ticker."""
        ticker = ticker.upper()
        await inter.response.defer()
        rsi  = await poly.get_rsi(symbol=ticker,timespan="hour",window=14)
        rsi_hour_value = rsi.rsi_value[0]
        rsi_min = await poly.get_rsi(symbol=ticker, timespan="minute",window=14)
        rsi_min_value = rsi_min.rsi_value[0]
        rsi_day = await poly.get_rsi(symbol=ticker, timespan="day", window=14)
        rsi_day_value = rsi_day.rsi_value[0]
        rsi_week = await poly.get_rsi(symbol=ticker, timespan="week", window=14)
        rsi_week_value = rsi_week.rsi_value[0]
        rsi_month = await poly.get_rsi(symbol=ticker, window=14, timespan="month")
        rsi_month_value = rsi_month.rsi_value[0]
        rsi_quarter = await poly.get_rsi(symbol=ticker, window=14, timespan="month")
        rsi_quarter_value = rsi_quarter.rsi_value[0]
        rsi_year = await poly.get_rsi(symbol=ticker, timespan="year")
        rsi_year_value = rsi_year.rsi_value[0]
        if rsi_quarter_value > 70:
            rsi_quarter_result = "🐻"
        elif rsi_quarter_value < 30:
            rsi_quarter_result = "🐂"
        else: 
            rsi_quarter_result = "🫥"


        if rsi_min_value > 70:
            rsi_min_result = "🐻"
        elif rsi_min_value < 30:
            rsi_min_result = "🐂"
        else:
            rsi_min_result = ""

        if rsi_day_value > 70:
            rsi_day_result = "🐻"
        elif rsi_day_value < 30:
            rsi_day_result = "🐂"
        else:
            rsi_day_result = ""
 

        if rsi_week_value > 70:
            rsi_week_result = "🐻"
        elif rsi_week_value < 30:
            rsi_week_result = "🐂"
        else:
            rsi_week_result = ""           
  

        if rsi_month_value > 70:
            rsi_month_result = "🐻"
        elif rsi_month_value < 30:
            rsi_month_result = "🐂"
        else:
            rsi_month_result = "" 

        if rsi_hour_value > 70 :
            rsi_hour_result = "🐻"
        elif rsi_hour_value < 30:
            rsi_hour_result = "🐂"
        else:
            rsi_hour_result = ""

        if rsi_quarter_value > 70:
            rsi_quarter_result = "🐻"
        elif rsi_quarter_value < 30:
            rsi_quarter_result = "🐂"
        else:
            rsi_quarter_result = ""


        if rsi_year_value > 70:
            rsi_year_result = "🐻"
        elif rsi_year_value < 30:
            rsi_year_result = "🐂"
        else:
            rsi_year_result = ""


        embed=disnake.Embed(title=f"📸 RSI - Snapshot - {ticker} 📸",description=f"```py\n RSI Snapshot for {ticker}:```\n> 1Min: {rsi_min_result} **{rsi_min_value}**\n\n> 1Hour: {rsi_hour_result} **{rsi_hour_value}**\n\n> 1Day: {rsi_day_result} **{rsi_day_value}**\n\n> Weekly: {rsi_week_result} **{rsi_week_value}**\n\n> Monthly: {rsi_month_result} **{rsi_month_value}**\n\n> Quarter: {rsi_quarter_result} **{rsi_quarter_value}**\n\n> Yearly: {rsi_year_result} **{rsi_year_value}**", color=disnake.Colour.dark_gold())
        embed.add_field(name=f"Click to Run:", value=f"> **</ta rsi_snapshot:1122650723021238362>**")
        embed.set_thumbnail(await poly.get_polygon_logo(ticker))
        await inter.send(embed=embed)


def setup(bot:commands.Bot):
    bot.add_cog(TA(bot))
    print(f"> Extension {__name__} is ready\n")