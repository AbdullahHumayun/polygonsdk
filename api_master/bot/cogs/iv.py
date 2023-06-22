from disnake.ext import commands
import disnake
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from cfg import YOUR_API_KEY

from tabulate import tabulate


class IV(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.polygon = AsyncPolygonSDK(YOUR_API_KEY)



    @commands.slash_command()
    async def iv(self, inter):
        pass









    @iv.sub_command()
    async def tv(self, inter: disnake.AppCmdInter, ticker= str):  # default ticker to SPX if not provided
        await inter.response.defer()
        counter = 0
        while True:
            counter = counter + 1
            price = await self.polygon.get_price(ticker=ticker)
            lower_strike = 0.98 * price
            upper_strike = 1.02 * price

            atm_options = await self.polygon.get_near_the_money_options(ticker, lower_strike=lower_strike, upper_strike=upper_strike)
            print(atm_options)
            redfire = "🔥"  # Red flame emoji
            greenfire = "🟢"  # Green flame emoji

            low_iv_data = await self.polygon.find_lowest_iv(atm_options)
            table = []

            for k in low_iv_data:
                for i in range(100):
                    try:
                        strike = k[i]['strike']
                        expiry = k[i]['expiry']
                        name = k[i]['name']
                        iv = k[i]['iv']
                        vol = float(k[i]['volume'])
                        #change = k[i]['percent_change']
                        #volume = k[i]['volume']
                        #oi = k[i]['oi']
                        #mid = k[i]['mid']
                        skew = redfire if strike < price else greenfire

                        if 'call' in name:

                            row = [expiry, f"${price}", skew, f"${strike}", f"{round(float(iv)*100, 6)}", f"{vol:,}"]
                            table.append(row)
                    except IndexError:
                        continue

            table_formatted = tabulate(table, headers=['Expiry', 'Price', 'Skew', 'Low Strike', 'IV', 'Vol'], tablefmt='fancy')

            embed = disnake.Embed(title=f"{ticker} IV TV", description=f"> <a:_:1043215847038144572>")
            embed.add_field(name="Emojis:", value="```🔥: Put Skew\n🟢 : Call Skew\n```", inline=False)
            embed.set_footer(text=f'{counter} Viewing Skews for {ticker}', icon_url=await self.polygon.get_polygon_logo(ticker))
            embed.description = f"`{table_formatted}`"
            await inter.edit_original_message(embed=embed)
            if counter == 100:
                await inter.send(f"> RUN AGAIN! </iv tv:1120580297717719121>")
                break



def setup(bot: commands.Bot):
    """SETUP"""
    bot.add_cog(IV(bot))
    print(f"> Extension {__name__} is ready\n")
