"""WEBULL COG"""
from datetime import timedelta
from datetime import date
import re
from disnake.ext import commands
import requests
import pyEX as p
import disnake
from utils.lists_and_dicts import pics_list
from utils.webull_tickers import ticker_list
from menus.menu import Menu

from views.learnviews import OptionsPaperView,OrderView,ChainView,CustomizeView, AnalysisView

from autocomp import tickerlist_autocomp, graphics_autocomp

intents = disnake.Intents.all()




class Webull(commands.Cog):
    """WEBULL COG"""
    def __init__(self, bot):
        pass




    @commands.slash_command()
    async def webull(self,inter):
        """Webull slash commands category."""
        pass


    @webull.sub_command()
    async def graphics(inter:disnake.AppCmdInter, graphic: str=commands.Param(autocomplete=graphics_autocomp)):
        """🔥Returns Webull Gifs / PNGs of various market topics."""
        
        link = pics_list[graphic]
        em = disnake.Embed(title="Graphic Helpers", color=disnake.Colour.dark_gold())
        em.set_image(url=link)
        await inter.send(embed=em)

    @webull.sub_command()
    async def quant(self,inter:disnake.AppCmdInter, ticker: str=commands.Param(autocomplete=tickerlist_autocomp)):
        """🔥Returns Operations, Business, Profit, and Profile earnings outlook."""
        await inter.response.defer(with_message=True)
        url = "https://webull.p.rapidapi.com/stock/get-financials"
        ids = ticker_list[ticker.upper()]
        querystring = {"tickerId":f"{ids}","fiscalYear":"2022","fiscalPeriod":"4","type":"2","count":"5"}

        headers = {
            "X-RapidAPI-Key": f"YOUR RAPIDAPI KEY",
            "X-RapidAPI-Host": "webull.p.rapidapi.com"
        }

        quantr = requests.request("GET", url, headers=headers, params=querystring)
        quantdat = quantr.json()
        interpret = quantdat['indexInterprets']
        profit = interpret['profitability']
        business = interpret['business']
        debtpaying = interpret['debtpaying']
        operation = interpret['operation']

        result1 = re.sub("<.*?>", "", profit)#
        result2 = re.sub("<.*?>", "", business)#
        result3 = re.sub("<.*?>", "", debtpaying)#
        result4 = re.sub("<.*?>", "", operation)#
        emb = disnake.Embed(title=f"Earnings Breakdown for {ticker}", description=f"```py\nProfit:\n\n{result1}```", color=disnake.Colour.dark_gold())
        emb.add_field(name="Business:", value=f"```py\n{result2}```")
        emb.add_field(name="Debt Paying:", value=f"```py\n{result3}```")
        emb.add_field(name="Operation:", value=f"```py\n{result4}```")
        await inter.edit_original_message(embed=emb)


    @webull.sub_command()
    async def news(self,interaction: disnake.AppCmdInter, query: str):
        """🔥Search for the news by query! Returns latest news articles."""
        
        await interaction.response.defer(with_message=True)
        url = "https://webull.p.rapidapi.com/news/search"

        querystring = {"keyword":f"{query}","pageSize":"10","pageIndex":"1"}

        headers = {
            "X-RapidAPI-Key": "YOUR_RAPID_API_KEY",
            "X-RapidAPI-Host": "webull.p.rapidapi.com"
}

        rdat = requests.request("GET", url, headers=headers, params=querystring)
        newsdat = rdat.json()
        news = newsdat['news']
        #pageindex = news['pageIndex']
        datas = news['datas']


        nd1 = datas[0]
        #n1id = nd1['newsId']
        n1title = nd1['title']
        n1url = nd1['newsUrl']
        n1source1 =nd1['sourceName']


        nd2 = datas[1]
        #n2id = n2['newsId']
        n2title = nd2['title']
        n2url = nd2['newsUrl']
        n2source2 =nd2['sourceName']

        nd3 = datas[2]
        #n3id = nd3['newsId']
        n3title = nd3['title']
        n3url = nd3['newsUrl']
        n3source3 =nd3['sourceName']

        nd4 = datas[3]
        #n4id = n4['newsId']
        n4title = nd4['title']
        n4url = nd4['newsUrl']
        n4source4 =nd4['sourceName']


        nd5 = datas[4]
        #n5id = n5['newsId']
        n5title = nd5['title']
        n5url = nd5['newsUrl']
        n5source5 =nd5['sourceName']


        nd6 = datas[5]
        #n6id = n6['newsId']
        n6title = nd6['title']
        n6url = nd6['newsUrl']
        n6source6 =nd6['sourceName']

        nd7 = datas[6]
        #n7id = nd7['newsId']
        n7title = nd7['title']
        n7url = nd7['newsUrl']
        n7source7 =nd7['sourceName']


        nd8 = datas[7]
        #n8id = n8['newsId']
        n8title = nd8['title']
        n8url = nd8['newsUrl']
        n8source8 =nd8['sourceName']

        nd9 = datas[8]
        #n9id = nd9['newsId']
        n9title = nd9['title']
        n9url = nd9['newsUrl']
        n9source9 =nd9['sourceName']

        nd10 = datas[9]
        #n10id = nd10['newsId']
        n10title = nd10['title']
        n10url = nd10['newsUrl']
        n10source10 =nd10['sourceName']

        embeds = [
            disnake.Embed(title=f"Source: {n1source1}", description=f"```py\n{n1title}````", color=disnake.Colour.random(), url=f"{n1url}"),
            disnake.Embed(title=f"Source: {n2source2}", description=f"```py\n{n2title}```", color=disnake.Colour.random(), url=f"{n2url}"),
            disnake.Embed(title=f"Source: {n3source3}", description=f"```py\n{n3title}```", color=disnake.Colour.random(), url=f"{n3url}"),
            disnake.Embed(title=f"Source: {n4source4}", description=f"```py\n{n4title}```", color=disnake.Colour.random(), url=f"{n4url}"),
            disnake.Embed(title=f"Source: {n5source5}", description=f"```py\n{n5title}```", color=disnake.Colour.random(), url=f"{n5url}"),
            disnake.Embed(title=f"Source: {n6source6}", description=f"```py\n{n6title}```", color=disnake.Colour.random(), url=f"{n6url}"),
            disnake.Embed(title=f"Source: {n7source7}", description=f"```py\n{n7title}```", color=disnake.Colour.random(), url=f"{n7url}"),
            disnake.Embed(title=f"Source: {n8source8}", description=f"```py\n{n8title}```", color=disnake.Colour.random(), url=f"{n8url}"),
            disnake.Embed(title=f"Source: {n9source9}", description=f"```py\n{n9title}```", color=disnake.Colour.random(), url=f"{n9url}"),
            disnake.Embed(title=f"Source: {n10source10}", description=f"```py\n{n10title}```", color=disnake.Colour.random(), url=f"{n10url}")
        ]
        await interaction.edit_original_message(embed=embeds[0], view=Menu(embeds))


    @webull.sub_command()
    async def cost(self,inter:disnake.AppCmdInter, ticker: str=commands.Param(autocomplete=tickerlist_autocomp)):
        """🔥Returns the Cost Distribution Analysis straight from Webull."""
        await inter.response.defer(with_message=True)
        ids = ticker_list[ticker.upper()]
        url = "https://webull.p.rapidapi.com/stock/get-cost-distribution-analysis"
        querystring = {"tickerId":f"{ids}"}
        headers = {
            "X-RapidAPI-Key": "YOUR_RAPID_API_KEY",
            "X-RapidAPI-Host": "webull.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring).json()
        data = response['data']
        dist = data[0]['distributions']
        avg = data[0]['avgCost']
        profitratio = round(float(data[0]['closeProfitRatio'])*100, ndigits=2)
        dist1 = dist[0]
        price1 = float(dist1[0])
        cost1 = float(dist1[1])
        avg1 = round(float(dist1[2])*100,ndigits=3)
        co1 = format(int(cost1),",")

        dist2 = dist[1]
        price2 = float(dist2[0])
        cost2 = float(dist2[1])
        avg2 = round(float(dist2[2])*100,ndigits=3)
        co2 = format(int(cost2),",")

        dist3 = dist[2]
        price3 = float(dist3[0])
        cost3 = float(dist3[1])
        avg3 = round(float(dist3[2])*100,ndigits=3)
        co3 = format(int(cost3),",")



        dist4 = dist[3]
        price4 = float(dist4[0])
        cost4 = float(dist4[1])
        avg4 = round(float(dist4[2])*100,ndigits=3)
        co4 = format(int(cost4),",")

        dist5 = dist[4]
        price5 = float(dist5[0])
        cost5 = float(dist5[1])
        avg5 = round(float(dist5[2])*100,ndigits=3)
        co5 = format(int(cost5),",")


        dist6 = dist[5]
        price6 = float(dist6[0])
        cost6 = float(dist6[1])
        avg6 = round(float(dist6[2])*100,ndigits=3)
        co6 = format(int(cost6),",")


        dist7 = dist[6]
        price7 = float(dist7[0])
        cost7 = float(dist7[1])
        avg7 = round(float(dist7[2])*100,ndigits=3)
        co7 = format(int(cost7),",")




        dist8 = dist[7]
        price8 = float(dist8[0])
        cost8 = float(dist8[1])
        avg8 = round(float(dist8[2])*100,ndigits=3)
        co8 = format(int(cost8),",")


        dist9 = dist[8]
        price9 = float(dist9[0])
        cost9 = float(dist9[1])
        avg9 = round(float(dist9[2])*100,ndigits=3)
        co9 = format(int(cost9),",")


        dist10 = dist[9]
        price10 = float(dist10[0])
        cost10 = float(dist10[1])
        avg10 = round(float(dist10[2])*100,ndigits=3)
        c10 = format(int(cost10),",")


        dist11 = dist[10]
        price11 = float(dist11[0])
        cost11 = float(dist11[1])
        avg11 = round(float(dist11[2])*100,ndigits=3)
        c11 = format(int(cost11),",")

        dist12 = dist[11]
        price12 = float(dist12[0])
        cost12 = float(dist12[1])
        avg12 = round(float(dist12[2])*100,ndigits=3)
        c12 = format(int(cost12),",")

        dist13 = dist[12]
        price13 = float(dist13[0])
        cost13 = float(dist13[1])
        avg13 = round(float(dist13[2])*100,ndigits=3)
        c13 = format(int(cost13),",")

        dist14 = dist[13]
        price14 = float(dist14[0])
        cost14 = float(dist14[1])
        avg14 = round(float(dist14[2])*100,ndigits=3)
        c14 = format(int(cost14),",")

        dist15 = dist[14]
        price15 = float(dist15[0])
        cost15 = float(dist15[1])
        avg15 = round(float(dist15[2])*100,ndigits=3)
        c15 = format(int(cost15),",")

        dist16 = dist[15]
        price16 = float(dist16[0])
        cost16 = float(dist16[1])
        avg16 = round(float(dist16[2])*100,ndigits=3)
        c16 = format(int(cost16),",")

        dist17 = dist[16]
        price17 = float(dist17[0])
        cost17 = float(dist17[1])
        avg17 = round(float(dist17[2])*100,ndigits=3)
        c17 = format(int(cost17),",")

        dist18 = dist[17]
        price18 = float(dist18[0])
        cost18 = float(dist18[1])
        avg18 = round(float(dist18[2])*100,ndigits=3)
        c18 = format(int(cost18),",")


        dist19 = dist[18]
        price19 = float(dist19[0])
        cost19 = float(dist19[1])
        avg19 = round(float(dist19[2])*100,ndigits=3)
        c19 = format(int(cost19),",")


        dist20 = dist[19]
        price20 = float(dist20[0])
        cost20 = float(dist20[1])
        avg20 = round(float(dist20[2])*100,ndigits=3)
        c20 = format(int(cost20),",")

        dist21 = dist[20]
        price21 = float(dist21[0])
        cost21 = float(dist21[1])
        avg21 = round(float(dist21[2])*100,ndigits=3)
        c21 = format(int(cost21),",")

        dist22 = dist[21]
        price22 = float(dist22[0])
        cost22 = float(dist22[1])
        avg22 = round(float(dist22[2])*100,ndigits=3)
        c22 = format(int(cost22),",")

        dist23 = dist[22]
        price23 = float(dist23[0])
        cost23 = float(dist23[1])
        avg23 = round(float(dist23[2])*100,ndigits=3)
        c23 = format(int(cost23),",")

        dist24 = dist[23]
        price24 = float(dist24[0])
        cost24 = float(dist24[1])
        avg24 = round(float(dist24[2])*100,ndigits=3)
        c24 = format(int(cost24),",")

        dist25 = dist[24]
        price25 = float(dist25[0])
        cost25 = float(dist25[1])
        avg25 = round(float(dist25[2])*100,ndigits=3)
        c25 = format(int(cost25),",")

        dist26 = dist[25]
        price26 = float(dist26[0])
        cost26 = float(dist26[1])
        avg26 = round(float(dist26[2])*100,ndigits=3)
        c26 = format(int(cost26),",")

        dist27 = dist[26]
        price27 = float(dist27[0])
        cost27 = float(dist27[1])
        avg27 = round(float(dist27[2])*100,ndigits=3)
        c27 = format(int(cost27),",")

        dist28 = dist[27]
        price28 = float(dist28[0])
        cost28 = float(dist28[1])
        avg28 = round(float(dist28[2])*100,ndigits=3)
        c28 = format(int(cost28),",")

        dist29 = dist[28]
        price29 = float(dist29[0])
        cost29 = float(dist29[1])
        avg29 = round(float(dist29[2])*100,ndigits=3)
        c29 = format(int(cost29),",")

        dist30 = dist[29]
        price30 = float(dist30[0])
        cost30 = float(dist30[1])
        avg30 = round(float(dist30[2])*100,ndigits=3)
        c30 = format(int(cost30),",")

        dist31 = dist[30]
        price31 = float(dist31[0])
        cost31 = float(dist31[1])
        avg31 = round(float(dist31[2])*100,ndigits=3)
        c31 = format(int(cost31),",")

        dist32 = dist[31]
        price32 = float(dist32[0])
        cost32 = float(dist32[1])
        avg32 = round(float(dist32[2])*100,ndigits=3)
        c32 = format(int(cost32),",")

        dist33 = dist[32]
        price33 = float(dist33[0])
        cost33 = float(dist33[1])
        avg33 = round(float(dist33[2])*100,ndigits=3)
        c33 = format(int(cost33),",")

        dist34 = dist[33]
        price34 = float(dist34[0])
        cost34 = float(dist34[1])
        avg34 = round(float(dist34[2])*100,ndigits=3)
        c34 = format(int(cost34),",")

        dist35 = dist[34]
        price35 = float(dist35[0])
        cost35 = float(dist35[1])
        avg35 = round(float(dist35[2])*100,ndigits=3)
        c35 = format(int(cost35),",")

        dist36 = dist[35]
        price36 = float(dist36[0])
        cost36 = float(dist36[1])
        avg36 = round(float(dist36[2])*100,ndigits=3)
        c36 = format(int(cost36),",")

        dist37 = dist[36]
        price37 = float(dist37[0])
        cost37 = float(dist37[1])
        avg37 = round(float(dist37[2])*100,ndigits=3)
        c37 = format(int(cost37),",")



        #dist50 = dist[49]
        #price50 = float(dist50[0])
        #cost50 = float(dist50[1])
        #avg50 = round(float(dist50[2])*100,ndigits=3)
        #c50 = format(int(cost50),",")

        pd1 = date.today() - timedelta(days=1)
        pd2 = date.today() - timedelta(days=2)
        pd3 = date.today() - timedelta(days=3)
        pd4 = date.today() - timedelta(days=4)
        pd5 = date.today() - timedelta(days=5)
        pd6 = date.today() - timedelta(days=6)
        pd7 = date.today() - timedelta(days=7)
        pd8 = date.today() - timedelta(days=8)
        pd9 = date.today() - timedelta(days=9)
        pd10 = date.today() - timedelta(days=10)
        pd11 = date.today() - timedelta(days=11)
        pd12 = date.today() - timedelta(days=12)
        pd13 = date.today() - timedelta(days=13)
        pd14 = date.today() - timedelta(days=14)
        pd15 = date.today() - timedelta(days=15)
        pd16 = date.today() - timedelta(days=16)
        pd17 = date.today() - timedelta(days=17)
        pd18 = date.today() - timedelta(days=18)
        pd19 = date.today() - timedelta(days=19)
        pd20 = date.today() - timedelta(days=20)
        pd21 = date.today() - timedelta(days=21)
        pd22 = date.today() - timedelta(days=22)
        pd23 = date.today() - timedelta(days=23)
        pd24 = date.today() - timedelta(days=24)
        pd25 = date.today() - timedelta(days=25)
        pd26 = date.today() - timedelta(days=26)
        pd27 = date.today() - timedelta(days=27)
        pd28 = date.today() - timedelta(days=28)
        pd29 = date.today() - timedelta(days=29)
        pd30 = date.today() - timedelta(days=30)
        pd31 = date.today() - timedelta(days=31)
        pd32 = date.today() - timedelta(days=32)
        pd33 = date.today() - timedelta(days=33)
        pd34 = date.today() - timedelta(days=34)
        pd35 = date.today() - timedelta(days=35)
        pd36 = date.today() - timedelta(days=36)

        today = date.today()
        embeds = [
        disnake.Embed(title=f"Cost Distribution Analysis for {today}", description=f"```py\nThe current profited shares proportion for {ticker} is {profitratio}%``` ```py\nAverage Cost:\n\nThe average share price for {ticker} is ${avg}``````py\nCost distribution for {today} = {avg1}% of {ticker} shares profited  at ${price1} for ${co1}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd1} for {ticker}", description=f"```py\n{avg2}% of {ticker} volume came in at ${price2} for ${co2}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd2} for {ticker}", description=f"```py\n{avg3}% of {ticker} volume came in at ${price3} for ${co3}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd3} for {ticker}", description=f"```py\n{avg4}% of {ticker} volume came in at ${price4} for ${co4}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd4} for {ticker}", description=f"```py\n{avg5}% of {ticker} volume came in at ${price5} for ${co5}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd5} for {ticker}", description=f"```py\n{avg6}% of {ticker} volume came in at ${price6} for ${co6}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd6} for {ticker}", description=f"```py\n{avg7}% of {ticker} volume came in at ${price7} for ${co7}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd7} for {ticker}", description=f"```py\n{avg8}% of {ticker} volume came in at ${price8} for ${co8}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd8} for {ticker}", description=f"```py\n{avg9}% of {ticker} volume came in at ${price9} for ${co9}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd9} for {ticker}", description=f"```py\n{avg10}% of {ticker} volume came in at ${price10} for ${c10}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd10} for {ticker}", description=f"```py\n{avg11}% of {ticker} volume came in at ${price11} for ${c11}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd11} for {ticker}", description=f"```py\n{avg12}% of {ticker} volume came in at ${price12} for ${c12}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd12} for {ticker}", description=f"```py\n{avg13}% of {ticker} volume came in at ${price13} for ${c13}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd13} for {ticker}", description=f"```py\n{avg14}% of {ticker} volume came in at ${price14} for ${c14}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd14} for {ticker}", description=f"```py\n{avg15}% of {ticker} volume came in at ${price15} for ${c15}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd15} for {ticker}", description=f"```py\n{avg16}% of {ticker} volume came in at ${price16} for ${c16}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd16} for {ticker}", description=f"```py\n{avg17}% of {ticker} volume came in at ${price17} for ${c17}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd17} for {ticker}", description=f"```py\n{avg18}% of {ticker} volume came in at ${price18} for ${c18}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd18} for {ticker}", description=f"```py\n{avg19}% of {ticker} volume came in at ${price19} for ${c19}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd19} for {ticker}", description=f"```py\n{avg20}% of {ticker} volume came in at ${price20} for ${c20}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd20} for {ticker}", description=f"```py\n{avg21}% of {ticker} volume came in at ${price21} for ${c21}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd21} for {ticker}", description=f"```py\n{avg22}% of {ticker} volume came in at ${price22} for ${c22}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd22} for {ticker}", description=f"```py\n{avg23}% of {ticker} volume came in at ${price23} for ${c23}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd23} for {ticker}", description=f"```py\n{avg24}% of {ticker} volume came in at ${price24} for ${c24}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd24} for {ticker}", description=f"```py\n{avg25}% of {ticker} volume came in at ${price25} for ${c25}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd25} for {ticker}", description=f"```py\n{avg26}% of {ticker} volume came in at ${price26} for ${c26}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd26} for {ticker}", description=f"```py\n{avg27}% of {ticker} volume came in at ${price27} for ${c27}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd27} for {ticker}", description=f"```py\n{avg28}% of {ticker} volume came in at ${price28} for ${c28}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd28} for {ticker}", description=f"```py\n{avg29}% of {ticker} volume came in at ${price29} for ${c29}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd29} for {ticker}", description=f"```py\n{avg30}% of {ticker} volume came in at ${price30} for ${c30}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd30} for {ticker}", description=f"```py\n{avg31}% of {ticker} volume came in at ${price31} for ${c31}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd31} for {ticker}", description=f"```py\n{avg32}% of {ticker} volume came in at ${price32} for ${c32}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd32} for {ticker}", description=f"```py\n{avg33}% of {ticker} volume came in at ${price33} for ${c33}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd33} for {ticker}", description=f"```py\n{avg34}% of {ticker} volume came in at ${price34} for ${c34}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd34} for {ticker}", description=f"```py\n{avg35}% of {ticker} volume came in at ${price35} for ${c35}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd35} for {ticker}", description=f"```py\n{avg36}% of {ticker} volume came in at ${price36} for ${c36}\n```", color=disnake.Colour.random()),
        disnake.Embed(title=f"Cost distribution for {pd36} for {ticker}", description=f"```py\n{avg37}% of {ticker} volume came in at ${price37} for ${c37}\n```", color=disnake.Colour.random()),]

        await inter.edit_original_message(embed=embeds[0], view=Menu(embeds))

    @webull.error
    async def costerror(self,inter: disnake.AppCmdInter, error):
        """ERROR"""
        if isinstance(error, commands.CheckAnyFailure):
            await inter.send("```py\n Must use caps - and can't be an ETF as ETFs dont have financial data such as earnings metrics.```")


    @webull.sub_command()
    async def analysis_tools(self,inter: disnake.AppCmdInter):
        """🔥Learn Webull Analysis Tools"""
        await inter.response.defer(with_message=True, ephemeral=True)
        emb = disnake.Embed(title="Webull Analysis Tools")
        emb.set_footer(text="Implemented by FUDSTOP Trading", icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        emb.set_thumbnail(url="https://media.discordapp.net/attachments/1009552305869303828/1009555505699639366/ezgif-2-f4a5623248.gif")
        await inter.edit_original_message(embed=emb, view=AnalysisView())

    @webull.sub_command()
    async def paper_trading(self,inter: disnake.AppCmdInter):
        """🔥Learn about Webull OPTIONS Paper Trading"""
        await inter.response.defer(with_message=True, ephemeral=True)
        emb = disnake.Embed(title="Webull Analysis Tools")
        emb.set_footer(text="Implemented by FUDSTOP Trading", icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        emb.set_thumbnail(url="https://media.discordapp.net/attachments/1009552305869303828/1009555505699639366/ezgif-2-f4a5623248.gif")
        await inter.edit_original_message(embed=emb, view=OptionsPaperView())

    @webull.sub_command()
    async def options_setup(self,inter: disnake.AppCmdInter):
        """🔥Learn to customize the Options Chain"""
        await inter.response.defer(with_message=True, ephemeral=True)
        emb = disnake.Embed(title="Learn about customization in Webull.")
        emb.set_footer(text="Implemented by FUDSTOP Trading", icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        emb.set_thumbnail(url="https://media.discordapp.net/attachments/1009552305869303828/1009555505699639366/ezgif-2-f4a5623248.gif")
        await inter.edit_original_message(embed=emb, view=CustomizeView())

    @webull.sub_command()
    async def options_chain(self,inter: disnake.AppCmdInter):
        """🔥Learn about the Options Chain"""
        await inter.response.defer(with_message=True, ephemeral=True)
        emb = disnake.Embed(title="Learn about customization in Webull.")
        emb.set_footer(text="Implemented by FUDSTOP Trading", icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        emb.set_thumbnail(url="https://media.discordapp.net/attachments/1009552305869303828/1009555505699639366/ezgif-2-f4a5623248.gif")
        await inter.edit_original_message(embed=emb, view=ChainView())

    @webull.sub_command()
    async def orders(self,inter: disnake.AppCmdInter):
        """🔥Learn about order types."""
        await inter.response.defer(with_message=True, ephemeral=True)
        emb = disnake.Embed(title="Learn about order types.")
        emb.set_footer(text="Implemented by FUDSTOP Trading", icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        emb.set_thumbnail(url="https://media.discordapp.net/attachments/1009552305869303828/1009555505699639366/ezgif-2-f4a5623248.gif")
        await inter.edit_original_message(embed=emb, view=OrderView())

    @webull.sub_command()
    async def bid_ask_spread(self,inter: disnake.AppCmdInter):
        """🔥Returns the bid/ask spread for a ticker."""
        await inter.response.defer(with_message=True)
        emb = disnake.Embed(title="Learn about the bid ask spread.")
        emb.set_footer(text="Implemented by FUDSTOP Trading", icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        emb.set_thumbnail(url="https://media.discordapp.net/attachments/1009552305869303828/1009555505699639366/ezgif-2-f4a5623248.gif")
        await inter.edit_original_message(embed=emb, view=OrderView())


    @webull.sub_command()
    async def webull_quote(self,inter:disnake.AppCmdInter, ticker: str=commands.Param(autocomplete=tickerlist_autocomp)):
        """🔥Pulls webull data to discord in the form of price quote info."""
        await inter.response.defer(with_message=True)
        ids = ticker_list[ticker.upper()]
        quoter = requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={ids},&includeSecu=1&delay=0&more=1")
        quoted = quoter.json()
        index = quoted[0]
        #name=index["name"]
        #symbol=index["symbol"]
        dissymbol=index["disSymbol"]
        #disExchangeCode=index["disExchangeCode"]
        #exchangeCode=index["exchangeCode"]
        #listStatus=index["listStatus"]
        #template=index["template"]
        #derivativeSupport=index["derivativeSupport"]
        #tradeTime=index["tradeTime"]
        #status=index["status"]
        close=index["close"]
        #change=index["change"]
        #changeRatio=index["changeRatio"]
        #marketValue=index["marketValue"]
        #volume=index["volume"]
        #turnoverRate=index["turnoverRate"]
        #timeZone=index["timeZone"]
        #tzName=index["tzName"]
        #preClose=index["preClose"]
        #open=index["open"]
        high=index["high"]
        low=index["low"]
        vibrateratio=index["vibrateRatio"]
        #avgVol10D=index["avgVol10D"]
        #avgVol3M=index["avgVol3M"]
        #dealAmount=index["dealAmount"]
        negmarketvalue=index["negMarketValue"]
        #pe=index["pe"]
        #indicatedPe=index["indicatedPe"]
        #peTtm=index["peTtm"]
        #eps=index["eps"]
        #epsTtm=index["epsTtm"]
        #pb=index["pb"]
        #totalShares=index["totalShares"]
        #outstandingShares=index["outstandingShares"]
        #fiftyTwoWkHigh=index["fiftyTwoWkHigh"]
        #fiftyTwoWkLow=index["fiftyTwoWkLow"]
        #yields=index["yield"]
        #currencyCode=index["currencyCode"]
        #lotSize=index["lotSize"]
        #latestDividendDate=index["latestDividendDate"]
        #latestEarningsDate=index["latestEarningsDate"]
        #ps=index["ps"]
        #bps=index["bps"]
        #estimateEarningsDate=index["estimateEarningsDate"]
        #tradeStatus=index["tradeStatus"]
        view = disnake.ui.View()
        bu2 = disnake.ui.Button(label=f"SYMBOL: {dissymbol}", style = disnake.ButtonStyle.grey,row=0)
        bu3 = disnake.ui.Button(label=f"Vibration Ratio: {vibrateratio}", style = disnake.ButtonStyle.green,row=1)
        bu4 = disnake.ui.Button(label=f"Negative Mkt Value: {negmarketvalue}", style = disnake.ButtonStyle.red, row=1)
        bu5 = disnake.ui.Button(label=f"High on Day: ${high}", style = disnake.ButtonStyle.green,row=2)
        bu6 = disnake.ui.Button(label=f"Today's Open: ${open}", style = disnake.ButtonStyle.grey, row=2)
        bu7 = disnake.ui.Button(label=f"Low of Day: ${low}", style = disnake.ButtonStyle.red,row=2)
        bu8 = disnake.ui.Button(label=f"Current: ${close}", style = disnake.ButtonStyle.blurple, row=3)
        bu9 = disnake.ui.Button(label="PUSHING NEW HIGHS!!!", style = disnake.ButtonStyle.blurple, row=3)
        view.add_item(bu2)
        view.add_item(bu3)
        view.add_item(bu4)
        view.add_item(bu5)
        view.add_item(bu6)
        view.add_item(bu7)
        view.add_item(bu8)
        emb = disnake.Embed(title=f"Webull Data for {dissymbol}", color=disnake.Colour.dark_blue())
        if close > high:
            view.remove_item(bu5)
            view.add_item(bu9)
        emb.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")
        emb.set_thumbnail(url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        await inter.edit_original_message(embed = emb, view=view)



def setup(bot):
    """SETUP COG"""
    bot.add_cog(Webull(bot))
    print(f"> Extension {__name__} is ready\n")
