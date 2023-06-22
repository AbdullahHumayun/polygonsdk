import requests
import disnake
from disnake.ext import commands
from time import sleep
from requests.auth import HTTPBasicAuth
import time
import pandas as pd
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK

from cfg import YOUR_API_KEY
polygon_options = PolygonOptionsSDK(YOUR_API_KEY)


class Options(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command()
    async def options(self, inter):
        pass


    @options.sub_command()
    async def fetch_entire_chain(ctx: disnake.AppCommandInter, tickers: str):
        await ctx.response.defer()
        for ticker in tickers:
            all_options = await polygon_options.get_option_chain_all(ticker)
            df = all_options[0].df
            df.to_csv(f'files/options/ticker_chains/all_{ticker}_chains.csv', index=False)
            await ctx.send(file=disnake.File(f'files/options/ticker_chains/all_{ticker}_chains.csv'))




        


    @options.sub_command()
    async def top(self, inter):
        """🎯Top OI Decrease // 
        Most VOL / Most Premium 
        / Most Active"""
        await inter.response.defer(with_message=True)

        em = disnake.Embed(title="Real time top options", description=f"```py\nThese are the top 5 options as far as overall volume/open interest activity:```", color=disnake.Colour.dark_teal(), url="https://www.webull.com/quote/us/options")
        
        em.add_field(name="Open Interest Put/Call Ratio:", value="```py\nPCR (OI) = open interest of put options on a given day/open interest of call options on the same given day```", inline=False)
        em.add_field(name="Volume Put/Call Ratio:", value="```py\nPCR (VOL) = volume of put options on a given day/volume of call options on the same given day```", inline=False)
        #em.add_field(name="Top Active Option #1:", value=f"```py\n {symbol1}``` ```py\n Vibrate Ratio: {vibrate1}``` ```py\n Volume Put Call Ratio: {volpcrround1}``` ```py\nOI Put/Call Ratio: {pcround1}``` ```py\n Position: {roundposition1} million \n Volume: {roundvol1} million```")
        #em.add_field(name="Top Active Option #1:", value=f"```py\n {symbol2}``` ```py\n Vibrate Ratio: {vibrate2}``` ```py\n Volume Put Call Ratio: {volpcrround2}``` ```py\nOI Put/Call Ratio: {pcround2}``` ```py\n Position: {roundposition2} million \n Volume: {roundvol2} million```")
        #em.add_field(name="Top Active Option #3:", value=f"```py\n {symbol3}``` ```py\n Vibrate Ratio: {vibrate3}``` ```py\n Volume Put Call Ratio: {volpcrround3}``` ```py\nOI Put/Call Ratio: {pcround3}``` ```py\n Position: {roundposition3} million \n Volume: {roundvol3} million```")
        #em.add_field(name="Top Active Option #4:", value=f"```py\n {symbol4}``` ```py\n Vibrate Ratio: {vibrate4}``` ```py\n Volume Put Call Ratio: {volpcrround4}``` ```py\nOI Put/Call Ratio: {pcround4}``` ```py\n Position: {roundposition4} million \n Volume: {roundvol4} million```")
        #em.add_field(name="Top Active Option #5:", value=f"```py\n {symbol5}``` ```py\n Vibrate Ratio: {vibrate5}``` ```py\n Volume Put Call Ratio: {volpcrround5}``` ```py\nOI Put/Call Ratio: {pcround5}``` ```py\n Position: {roundposition5} million \n Volume: {roundvol5} million```")
        view = disnake.ui.View()
        button = disnake.ui.Button(label="Learn About ☀️ PCR, OI, and VOL", style=disnake.ButtonStyle.url, url="https://www.mdpi.com/2227-7099/7/1/24/pdf-vor#:~:text=Put%E2%80%93Call%20volume%20(open%20interest,and%20t%20%E2%80%93%201%2C%20respectively.")
        button2 = disnake.ui.Button(label="Learn aout 🩸 Implied Volatility", style=disnake.ButtonStyle.url, url="https://web.wpi.edu/Pubs/E-project/Available/E-project-012617-235702/unrestricted/Active_Trading_in_the_Stock_Market_Using_Implied_Volatility-final.pdf")
        view.add_item(button)
        view.add_item(button2)
        #view.add_item(MostActive())
        #view.add_item(HighestStats())
        # view.add_item(TopIV())
        #view.add_item(TopOIDecrease())
        await inter.edit_original_response(embed=em, view=view)


    @options.sub_command()
    async def top_active(inter:disnake.AppCmdInter):
        """🎯Returns the top 5 options for volume and activity market wide."""
        await inter.response.defer(with_message=True)

        em = disnake.Embed(title="Real time top options", description=f"```py\nThese are the top 5 options as far as overall volume/open interest activity:```", color=disnake.Colour.random())
        
        em.add_field(name="Open Interest Put/Call Ratio:", value="```py\nPCR (OI) = open interest of put options on a given day/open interest of call options on the same given day```", inline=False)
        em.add_field(name="Volume Put/Call Ratio:", value="```py\nPCR (VOL) = volume of put options on a given day/volume of call options on the same given day```", inline=False)
        #em.add_field(name="Top Active Option #1:", value=f"```py\n {symbol1}``` ```py\n Vibrate Ratio: {vibrate1}``` ```py\n Volume Put Call Ratio: {volpcrround1}``` ```py\nOI Put/Call Ratio: {pcround1}``` ```py\n Position: {roundposition1} million \n Volume: {roundvol1} million```")
        #em.add_field(name="Top Active Option #1:", value=f"```py\n {symbol2}``` ```py\n Vibrate Ratio: {vibrate2}``` ```py\n Volume Put Call Ratio: {volpcrround2}``` ```py\nOI Put/Call Ratio: {pcround2}``` ```py\n Position: {roundposition2} million \n Volume: {roundvol2} million```")
        #em.add_field(name="Top Active Option #3:", value=f"```py\n {symbol3}``` ```py\n Vibrate Ratio: {vibrate3}``` ```py\n Volume Put Call Ratio: {volpcrround3}``` ```py\nOI Put/Call Ratio: {pcround3}``` ```py\n Position: {roundposition3} million \n Volume: {roundvol3} million```")
        #em.add_field(name="Top Active Option #4:", value=f"```py\n {symbol4}``` ```py\n Vibrate Ratio: {vibrate4}``` ```py\n Volume Put Call Ratio: {volpcrround4}``` ```py\nOI Put/Call Ratio: {pcround4}``` ```py\n Position: {roundposition4} million \n Volume: {roundvol4} million```")
        #em.add_field(name="Top Active Option #5:", value=f"```py\n {symbol5}``` ```py\n Vibrate Ratio: {vibrate5}``` ```py\n Volume Put Call Ratio: {volpcrround5}``` ```py\nOI Put/Call Ratio: {pcround5}``` ```py\n Position: {roundposition5} million \n Volume: {roundvol5} million```")
        view = disnake.ui.View()
        button = disnake.ui.Button(label="Learn About ☀️ PCR, OI, and VOL", style=disnake.ButtonStyle.url, url="https://www.mdpi.com/2227-7099/7/1/24/pdf-vor#:~:text=Put%E2%80%93Call%20volume%20(open%20interest,and%20t%20%E2%80%93%201%2C%20respectively.")
        button2 = disnake.ui.Button(label="Learn aout 🩸 Implied Volatility", style=disnake.ButtonStyle.url, url="https://web.wpi.edu/Pubs/E-project/Available/E-project-012617-235702/unrestricted/Active_Trading_in_the_Stock_Market_Using_Implied_Volatility-final.pdf")
        view.add_item(button)
        view.add_item(button2)
        #view.add_item(MostActive())
        #view.add_item(HighestStats())
        #view.add_item(TopIV())
        await inter.edit_original_message(embed=em, view=view)

    @options.sub_command()
    async def oi_increase(inter:disnake.AppCmdInter):
        """🎯Returns Top 5 Increase of Option Open Interest."""
        await inter.response.defer(with_message=True)
        r = requests.get(url="https://quotes-gw.webullfintech.com/api/wlas/option/rank/list?regionId=6&rankType=posIncrease&pageIndex=0&pageSize=50")
        d = r.json()
        data = d['data']
        index1 = data[0]
        index2 = data[1]
        index3 = data[2]
        index4 = data[3]
        index5 = data[4]
        belongticker1 = index1['belongTicker']
        derivative1 = index1['derivative']
        values1 = index1['values']
        name1 = belongticker1['name']
        symbol1 = belongticker1['symbol']
        direction1 = derivative1['direction']
        price1 = derivative1['price']
        exp1 = derivative1['expireDate']
        strike1 = derivative1['strikePrice']
        close1 = derivative1['close']
        impvol1 = values1['implVol']



        belongticker2 = index2['belongTicker']
        derivative2 = index2['derivative']
        values2 = index2['values']
        name2 = belongticker2['name']
        symbol2 = belongticker2['symbol']
        direction2 = derivative2['direction']
        price2 = derivative2['price']
        exp2 = derivative2['expireDate']
        strike2 = derivative2['strikePrice']
        close2 = derivative2['close']
        impvol2 = values2['implVol']


        belongticker3 = index3['belongTicker']
        derivative3 = index3['derivative']
        values3 = index3['values']
        name3 = belongticker3['name']
        symbol3 = belongticker3['symbol']
        direction3 = derivative3['direction']
        price3 = derivative3['price']
        exp3 = derivative3['expireDate']
        strike3 = derivative3['strikePrice']
        close3 = derivative3['close']
        impvol3 = values3['implVol']
        
        belongticker4 = index4['belongTicker']
        derivative4 = index4['derivative']
        values4 = index4['values']
        name4 = belongticker4['name']
        symbol4 = belongticker4['symbol']
        direction4 = derivative4['direction']
        price4 = derivative4['price']
        exp4 = derivative4['expireDate']
        strike4 = derivative4['strikePrice']
        close4 = derivative4['close']
        impvol4 = values4['implVol']
        
        belongticker5 = index5['belongTicker']
        derivative5 = index5['derivative']
        values5 = index5['values']
        name5 = belongticker5['name']
        symbol5 = belongticker5['symbol']
        direction5 = derivative5['direction']
        price5 = derivative5['price']
        exp5 = derivative5['expireDate']
        strike5 = derivative5['strikePrice']
        close5 = derivative5['close']
        impvol5 = values5['implVol']
        em = disnake.Embed(title=f"Top 5 Increase of Options Open Interest:", description=f"```py\nThis command scans for the top 5 contracts where positions have increased the most.```", color=disnake.Colour.dark_green())
        em.add_field(name="Top Increase of Open Interest #1:", value=f"```py\n {name1} {symbol1}``` **Contract:** ```py\n {symbol1} ${strike1} {direction1} {exp1}``` ```py\n IV: {impvol1} Price: ${price1}```", inline=False)
        em.add_field(name="Top Increase of Open Interest #2:", value=f"```py\n {name2} {symbol2}``` **Contract:** ```py\n {symbol2} ${strike2} {direction2} {exp2}``` ```py\n IV: {impvol2} Price: ${price2}```", inline=False)
        em.add_field(name="Top Increase of Open Interest #3:", value=f"```py\n {name3} {symbol3}``` **Contract:** ```py\n {symbol3} ${strike3} {direction3} {exp3}``` ```py\n IV: {impvol3} Price: ${price3}```", inline=False)
        em.add_field(name="Top Increase of Open Interest #4:", value=f"```py\n {name4} {symbol4}``` **Contract:** ```py\n {symbol4} ${strike4} {direction4} {exp4}``` ```py\n IV: {impvol4} Price: ${price4}```", inline=False)
        em.add_field(name="Top Increase of Open Interest #5:", value=f"```py\n {name5} {symbol5}``` **Contract:** ```py\n {symbol5} ${strike5} {direction5} {exp5}``` ```py\n IV: {impvol5} Price: ${price5}```", inline=False)
        await inter.edit_original_message(embed=em)



    @options.sub_command()
    async def top_iv(inter:disnake.AppCmdInter):
        """🎯Returns highest IV for 5 stocks realtime."""
        await inter.response.defer(with_message=True)
        r = requests.get(url="https://quotes-gw.webullfintech.com/api/wlas/option/rank/list?regionId=6&rankType=impVol&pageIndex=0&pageSize=50")
        d = r.json()
        data = d['data']
        ivindex1 = data[0]
        ivindex2 = data[1]
        ivindex3 = data[2]
        ivindex4 = data[3]
        ivindex5 = data[4]
        belongticker1 = ivindex1['belongTicker']
        derivative1 = ivindex1['derivative']
        values1 = ivindex1['values']
        name1 = belongticker1['name']
        symbol1 = belongticker1['symbol']
        direction1 = derivative1['direction']
        price1 = derivative1['price']
        exp1 = derivative1['expireDate']
        strike1 = derivative1['strikePrice']
        close1 = derivative1['close']
        impvol1 = values1['implVol']



        belongticker2 = ivindex2['belongTicker']
        derivative2 = ivindex2['derivative']
        values2 = ivindex2['values']
        name2 = belongticker2['name']
        symbol2 = belongticker2['symbol']
        direction2 = derivative2['direction']
        price2 = derivative2['price']
        exp2 = derivative2['expireDate']
        strike2 = derivative2['strikePrice']
        close2 = derivative2['close']
        impvol2 = values2['implVol']


        belongticker3 = ivindex3['belongTicker']
        derivative3 = ivindex3['derivative']
        values3 = ivindex3['values']
        name3 = belongticker3['name']
        symbol3 = belongticker3['symbol']
        direction3 = derivative3['direction']
        price3 = derivative3['price']
        exp3 = derivative3['expireDate']
        strike3 = derivative3['strikePrice']
        close3 = derivative3['close']
        impvol3 = values3['implVol']

        belongticker4 = ivindex4['belongTicker']
        derivative4 = ivindex4['derivative']
        values4 = ivindex4['values']
        name4 = belongticker4['name']
        symbol4 = belongticker4['symbol']
        direction4 = derivative4['direction']
        price4 = derivative4['price']
        exp4 = derivative4['expireDate']
        strike4 = derivative4['strikePrice']
        close4 = derivative4['close']
        impvol4 = values4['implVol']
        
        belongticker5 = ivindex5['belongTicker']
        derivative5 = ivindex5['derivative']
        values5 = ivindex5['values']
        name5 = belongticker5['name']
        symbol5 = belongticker5['symbol']
        direction5 = derivative5['direction']
        price5 = derivative5['price']
        exp5 = derivative5['expireDate']
        strike5 = derivative5['strikePrice']
        close5 = derivative5['close']
        impvol5 = values5['implVol']
        em = disnake.Embed(title=f"Top 5 Highest IV Contracts:", description=f"```py\nThis command scans for the top 5 contracts where implied volatiltiy is HIGHEST.```", color=disnake.Colour.dark_red())
        em.add_field(name="Top IV #1:", value=f"```py\n {name1} {symbol1}``` **Contract:** ```py\n {symbol1} ${strike1} {direction1} {exp1}``` ```py\n IV: {impvol1} Price: ${price1}```", inline=False)
        em.add_field(name="Top IV #2:", value=f"```py\n {name2} {symbol2}``` **Contract:** ```py\n {symbol2} ${strike2} {direction2} {exp2}``` ```py\n IV: {impvol2} Price: ${price2}```", inline=False)
        em.add_field(name="Top IV #3:", value=f"```py\n {name3} {symbol3}``` **Contract:** ```py\n {symbol3} ${strike3} {direction3} {exp3}``` ```py\n IV: {impvol3} Price: ${price3}```", inline=False)
        em.add_field(name="Top IV #4:", value=f"```py\n {name4} {symbol4}``` **Contract:** ```py\n {symbol4} ${strike4} {direction4} {exp4}``` ```py\n IV: {impvol4} Price: ${price4}```", inline=False)
        em.add_field(name="Top IV #5:", value=f"```py\n {name5} {symbol5}``` **Contract:** ```py\n {symbol5} ${strike5} {direction5} {exp5}``` ```py\n IV: {impvol5} Price: ${price5}```", inline=False)
        await inter.edit_original_message(embed = em)

    @options.sub_command()
    async def oi_decrease(inter:disnake.AppCmdInter):
        """🎯Returns the top 3 most decreased options positions in real-time."""
        await inter.response.defer(with_message=True)
        r = requests.get(url="https://quotes-gw.webullfintech.com/api/wlas/option/rank/list?regionId=6&rankType=posDecrease&pageIndex=0&pageSize=50")
        d = r.json()
        data = d['data']
        index1 = data[0]
        index2 = data[1]
        index3 = data[2]
        index4 = data[3]
        index5 = data[4]
        belongticker1 = index1['belongTicker']
        derivative1 = index1['derivative']
        values1 = index1['values']
        name1 = belongticker1['name']
        symbol1 = belongticker1['symbol']
        direction1 = derivative1['direction']
        price1 = derivative1['price']
        exp1 = derivative1['expireDate']
        strike1 = derivative1['strikePrice']
        close1 = derivative1['close']
        impvol1 = values1['implVol']



        belongticker2 = index2['belongTicker']
        derivative2 = index2['derivative']
        values2 = index2['values']
        name2 = belongticker2['name']
        symbol2 = belongticker2['symbol']
        direction2 = derivative2['direction']
        price2 = derivative2['price']
        exp2 = derivative2['expireDate']
        strike2 = derivative2['strikePrice']
        close2 = derivative2['close']
        impvol2 = values2['implVol']


        belongticker3 = index3['belongTicker']
        derivative3 = index3['derivative']
        values3 = index3['values']
        name3 = belongticker3['name']
        symbol3 = belongticker3['symbol']
        direction3 = derivative3['direction']
        price3 = derivative3['price']
        exp3 = derivative3['expireDate']
        strike3 = derivative3['strikePrice']
        close3 = derivative3['close']
        impvol3 = values3['implVol']

        belongticker4 = index4['belongTicker']
        derivative4 = index4['derivative']
        values4 = index4['values']
        name4 = belongticker4['name']
        symbol4 = belongticker4['symbol']
        direction4 = derivative4['direction']
        price4 = derivative4['price']
        exp4 = derivative4['expireDate']
        strike4 = derivative4['strikePrice']
        close4 = derivative4['close']
        impvol4 = values4['implVol']
        
        belongticker5 = index5['belongTicker']
        derivative5 = index5['derivative']
        values5 = index5['values']
        name5 = belongticker5['name']
        symbol5 = belongticker5['symbol']
        direction5 = derivative5['direction']
        price5 = derivative5['price']
        exp5 = derivative5['expireDate']
        strike5 = derivative5['strikePrice']
        close5 = derivative5['close']
        impvol5 = values5['implVol']
        em = disnake.Embed(title=f"Top  5 Largest Decreases in Open Interest", description=f"```py\nThis command scans for the top 5 contracts where positions have DECREASED the most.```", color=disnake.Colour.dark_red())
        em.add_field(name="Top Decrease #1:", value=f"```py\n {name1} {symbol1}``` **Contract:** ```py\n {symbol1} ${strike1} {direction1} {exp1}``` ```py\n IV: {impvol1} Price: ${price1}```", inline=False)
        em.add_field(name="Top Decrease #2:", value=f"```py\n {name2} {symbol2}``` **Contract:** ```py\n {symbol2} ${strike2} {direction2} {exp2}``` ```py\n IV: {impvol2} Price: ${price2}```", inline=False)
        em.add_field(name="Top Decrease #3:", value=f"```py\n {name3} {symbol3}``` **Contract:** ```py\n {symbol3} ${strike3} {direction3} {exp3}``` ```py\n IV: {impvol3} Price: ${price3}```", inline=False)
        em.add_field(name="Top Decrease #4:", value=f"```py\n {name4} {symbol4}``` **Contract:** ```py\n {symbol4} ${strike4} {direction4} {exp4}``` ```py\n IV: {impvol4} Price: ${price4}```", inline=False)
        em.add_field(name="Top Decrease #5:", value=f"```py\n {name5} {symbol5}``` **Contract:** ```py\n {symbol5} ${strike5} {direction5} {exp5}``` ```py\n IV: {impvol5} Price: ${price5}```", inline=False)
        
        await inter.edit_original_message(embed = em)



def setup(bot):
    bot.add_cog(Options(bot))
    print(f"> Extension {__name__} is ready\n")