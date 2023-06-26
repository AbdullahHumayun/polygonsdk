"""JASMY COG"""
import requests
import disnake
from disnake.ext import commands




class Jasmy(commands.Cog):
    """PARENT CLASS"""
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command()
    async def jasmy(self,inter):
        """>>> Parent command category for Jasmy related commands"""



    @jasmy.sub_command()
    async def prediction(self, inter: disnake.AppCmdInter):
        """Returns price prediction and accuracy data for Jasmy."""
        await inter.response.defer(with_message=True)
        pred = requests.get(url="https://api.coinmarketcap.com/data-api/v3/price-prediction/query/half-year?cryptoId=8425")
        predd = pred.json()
        data = predd['data']
        predictions = data['predictions']
        nexthalf = data['nextHalfYearStatistics']
        lasthalf = data['lastHalfYearStatistics']
        total = lasthalf['totalEstimates']

        # Extracting prediction data
        total = nexthalf['totalEstimates']
        nextestmedian = nexthalf['estimationMedian']
        nextavg = nexthalf['estimationAverage']

        target1 = predictions[0]
        target1mo = target1['targetMonth']
        target1yr = target1['targetYear']
        votecount1 = target1['voteCount']
        avgp1 = target1['avgPrice']

        target2 = predictions[1]
        target2mo = target2['targetMonth']
        target2yr = target2['targetYear']
        votecount2 = target2['voteCount']
        avgp2 = target2['avgPrice']

        target3 = predictions[2]
        target3mo = target3['targetMonth']
        target3yr = target3['targetYear']
        votecount3 = target3['voteCount']
        avgp3 = target3['avgPrice']

        target4 = predictions[3]
        target4mo = target4['targetMonth']
        target4yr = target4['targetYear']
        votecount4 = target4['voteCount']
        avgp4 = target4['avgPrice']

        target5 = predictions[4]
        target5mo = target5['targetMonth']
        target5yr = target5['targetYear']
        votecount5 = target5['voteCount']
        avgp5 = target5['avgPrice']

        target6 = predictions[5]
        target6mo = target6['targetMonth']
        target6yr = target6['targetYear']
        votecount6 = target6['voteCount']
        avgp6 = target6['avgPrice']

        # Creating and sending embed message
        emb = disnake.Embed(
            title="Price Prediction: Jasmy",
            description=f"```py\nNext half-year estimates:``` ```py\nYear: {target1yr} Month: {target1mo} Votes: {votecount1} Avg Price: ${avgp1}\n\nYear: {target2yr} Month: {target2mo} Votes: {votecount2} AvgPrice: ${avgp2}\n\nYear:{target3yr} Month: {target3mo} Votes: {votecount3} AvgPrice: ${avgp3}\n\nYear: {target4yr} Month: {target4mo} Votes: {votecount4} AvgPrice: ${avgp4}\n\nYear: {target5yr} Month: {target5mo} Votes: {votecount5} AvgPrice: ${avgp5}\n\nYear: {target6yr} Month: {target6mo} Votes: {votecount6} AvgPrice: ${avgp6}```",
            color=disnake.Colour.dark_gold()
        )
        emb.add_field(name="Next Half-Year Estimates:", value=f"```py\nTotal Estimates: {total}``` ```py\nMedian Estimate: {nextestmedian}``` ```py\nEstimation Average: {nextavg}```")
        await inter.edit_original_message(embed=emb)


    @jasmy.sub_command()
    async def holders(self, inter: disnake.AppCmdInter):
        """Returns the current number of Jasmy holders."""
        await inter.response.defer(with_message=True)
        jholders = requests.get(url="https://api.coinmarketcap.com/data-api/v3/cryptocurrency/detail/holders/count?id=8425&range=7d")
        jholdersd = jholders.json()
        data = jholdersd['data']
        points = data['points']
        val_list = list(points.values())
        emb = disnake.Embed(title="Jasmy Holders!", description=f"```py\nAs per etherscan data - there are currently {val_list[0]} jasmy holders.```")
        await inter.edit_original_message(embed=emb)

    @jasmy.sub_command()
    async def price(self, inter:disnake.AppCmdInter):
        """🩸Returns Jasmy Data"""
        await inter.response.defer(with_message=True)
        counter = 0
        while True:
            try:
                counter = counter + 1
                request = requests.get(url="https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=Jasmy&start=1&limit=100&category=spot&centerType=all&sort=cmc_rank_advanced")
                dat = request.json()
                data = dat['data']
                #id = data['id']#
                #name = data['name']#
                #symbol = data['symbol']
                marketpairs = data['marketPairs']
                market1 = marketpairs[0]
                #marketpair1 = marketpairs[0]['marketPair']
                #exchangeid1 = market1['exchangeId']
                #liquidity1 = market1['liquidity']
                quote1 = round(market1['quote'], ndigits=7)
                volume = float(round(market1['volumeUsd']*0.000001, ndigits=2))
                market2 = marketpairs[1]
                #exchangeid2 = market2['exchangeId']
                quote2 = round(market2['quote'], ndigits=7)

                market3 = marketpairs[2]
                quote3 = str(round(market3['quote'], ndigits=7))
                #volume3 = float(round(market3['volumeUsd']*0.000001, ndigits=2))

                market4 = marketpairs[3]
                quote4 = str(round(market4['quote'], ndigits=7))
                #volume4 = float(round(market4['volumeUsd']*0.000001, ndigits=2))

                market5 = marketpairs[4]
                #exchangeid5 = market5['exchangeId']
                quote5 = str(round(market5['quote'], ndigits=7))
                #volume5 = float(round(market5['volumeUsd']*0.000001, ndigits=2))


                market6 = marketpairs[5]
                quote6 = str(round(market6['quote'], ndigits=7))
                #volume = float(round(market1['volumeUsd']*0.000001, ndigits=2))
                #volume2 = float(round(market2['volumeUsd']*0.000001, ndigits=2))
                #volume6 = float(round(market6['volumeUsd']*0.000001, ndigits=2))

                market7 = marketpairs[6]
                #exchangeid7 = market7['exchangeId']
                quote7 = round(market7['quote'], ndigits=7)
                #volume7 = float(round(market7['volumeUsd']*0.000001, ndigits=2))

                market8 = marketpairs[7]
                #liquidity8 = market8['liquidity']
                #volume8 = float(round(market6['volumeUsd']*0.000001, ndigits=2))
                quote8 = round(market8['quote'], ndigits=7)

                market9 = marketpairs[8]
                #effectiveliquidity9 = market9['effectiveLiquidity']
                #volume9 = float(round(market9['volumeUsd']*0.000001, ndigits=2))
                quote9 = round(market9['quote'], ndigits=7)

                market10 = marketpairs[9]
                #liquidity10 = market10['liquidity']
                quote10 = str(round(market10['quote'], ndigits=7))


                #volume10 = float(round(market10['volumeUsd']*0.000001, ndigits=2))

                market11 = marketpairs[10]
                #exchangeid11 = market11['exchangeId']
                #liquidity11 = market11['liquidity']
                quote11 = round(market11['quote'], ndigits=7)

                #volume11 = float(round(market11['volumeUsd']*0.000001, ndigits=2))
                market12 = marketpairs[11]

                quote12 = str(round(market12['quote'], ndigits=7))

                market13 = marketpairs[12]

                quote13 = str(round(market13['quote'], ndigits=7))

                market14 = marketpairs[13]

                quote14 = str(round(market14['quote'], ndigits=7))

                market15 = marketpairs[14]

                quote15 = round(market15['quote'], ndigits=7)

                market16 = marketpairs[15]

                quote16 = round(market16['quote'], ndigits=7)
                market17 = marketpairs[16]

                quote17 = round(market17['quote'], ndigits=7)

                market18 = marketpairs[17]

                quote18 = round(market18['quote'], ndigits=7)
                market19 = marketpairs[18]

                quote19 = round(market19['quote'], ndigits=7)

                market20 = marketpairs[19]

                quote20 = str(round(market20['quote'], ndigits=7))



                view = disnake.ui.View()
                ex1 = disnake.ui.Button(label=f"${quote1} Vol: ${volume}m", style=disnake.ButtonStyle.green)
                ex2 = disnake.ui.Button(label=f"${quote2} ", style=disnake.ButtonStyle.green)
                ex3 = disnake.ui.Button(label=f"${quote3}", style=disnake.ButtonStyle.green)
                ex4 = disnake.ui.Button(label=f"${quote4}", style=disnake.ButtonStyle.green)
                ex5 = disnake.ui.Button(label=f"${quote5}", style=disnake.ButtonStyle.green)
                ex6 = disnake.ui.Button(label=f"${quote6}", style=disnake.ButtonStyle.green)
                ex7 = disnake.ui.Button(label=f"${quote7}", style=disnake.ButtonStyle.green)
                ex8 = disnake.ui.Button(label=f"${quote8}", style=disnake.ButtonStyle.green)
                ex9 = disnake.ui.Button(label=f"${quote9}", style=disnake.ButtonStyle.green)
                ex10 = disnake.ui.Button(label=f"${quote10}", style=disnake.ButtonStyle.green)
                ex11 = disnake.ui.Button(label=f"${quote11}", style=disnake.ButtonStyle.green)
                ex12 = disnake.ui.Button(label=f"${quote12}", style=disnake.ButtonStyle.green)
                ex13 = disnake.ui.Button(label=f"${quote13}", style=disnake.ButtonStyle.green)
                ex14 = disnake.ui.Button(label=f"${quote14}", style=disnake.ButtonStyle.green)
                ex15 = disnake.ui.Button(label=f"${quote15}", style=disnake.ButtonStyle.green)
                ex16 = disnake.ui.Button(label=f"${quote16}", style=disnake.ButtonStyle.green)
                ex17 = disnake.ui.Button(label=f"${quote17}", style=disnake.ButtonStyle.green)
                ex18 = disnake.ui.Button(label=f"${quote18}", style=disnake.ButtonStyle.green)
                ex19 = disnake.ui.Button(label=f"${quote19}", style=disnake.ButtonStyle.green)
                ex20 = disnake.ui.Button(label=f"${quote20}", style=disnake.ButtonStyle.green)
                view.add_item(ex1)
                view.add_item(ex2)
                view.add_item(ex3)
                view.add_item(ex4)
                view.add_item(ex5)
                view.add_item(ex6)
                view.add_item(ex7)
                view.add_item(ex8)
                view.add_item(ex9)
                view.add_item(ex10)
                view.add_item(ex11)
                view.add_item(ex12)
                view.add_item(ex13)
                view.add_item(ex14)
                view.add_item(ex15)
                view.add_item(ex16)
                view.add_item(ex17)
                view.add_item(ex18)
                view.add_item(ex19)
                view.add_item(ex20)

                em4 = disnake.Embed(
                    title="JASMY!!!!!!!!!!!!!!!!",
                    description=f"```py\n{quote1}``` ```py\nVolume: {volume}```",
                    color=disnake.Colour.random())
                em4.set_thumbnail(
                url="https://cdn.discordapp.com/emojis/923701685321363566.gif?size=96&quality=lossless")
                await inter.edit_original_message(view=view, embed=em4)
                if counter == 100:
                    break
            except KeyError:
                await inter.send("Server busy! Try again later.")

def setup(bot:commands.Bot):
    """SETUP"""
    bot.add_cog(Jasmy(bot))
    print(f"> Extension {__name__} is ready\n")
