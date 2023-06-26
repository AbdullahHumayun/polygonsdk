import requests
import disnake
from disnake.ext import commands
from autocomp import tickerlist_autocomp
from time import sleep
from utils.webull_tickers import ticker_list
from autocomp import coin_autocomp
from utils.crypto_coins import coins
import json




class Stream(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def stream(self, inter):
        pass

    @stream.sub_command()
    async def time_and_sales(inter:disnake.AppCmdInter, ticker: str=commands.Param(autocomplete=tickerlist_autocomp)):
        """🫧Returns real-time time and sales date for 100 ticks."""
        ids = ticker_list[ticker]
        counter = 0
        await inter.response.defer(with_message=True)
        while True:
            counter = counter + 1
            r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/stock/capitalflow/deals?count=100&tickerId={ids}")
            d= r.json()
            data = d['data']
            index1 = data[0]
            time = index1['tradeTime']
            price = index1['price']
            volume = index1['volume']
            trdbs = index1['trdBs']
            trdex = index1['trdEx']
            em = disnake.Embed(title=f"Realtime Stock Price / Trade Exhange info for {ticker}", description=f"```py\n⏰{time} Price: ${price} Vol: {volume} Type: '{trdbs}' Exchange: '{trdex}'```", color=disnake.Colour.random())
            em.set_footer(text="This command displays real-time data provided by Cboe Hanweck. Data Ticks  100 times before becoming static.")
            await inter.edit_original_message(embed = em)
            with open('timeandsales.txt', 'a') as outfile:
                json.dump(f"{ticker} | {time} | {price} | {volume} | {trdbs} | {trdex}", outfile, indent=2)
                outfile.close()
            if counter == 250:
                break
    @stream.sub_command()
    async def double_quote(inter:disnake.AppCmdInter, ticker: str=commands.Param(autocomplete=tickerlist_autocomp), ticker1: str=commands.Param(autocomplete=tickerlist_autocomp)):
        """🫧Choose two stonks and stream their price in real-time for 200 ticks."""
        ids = ticker_list[ticker]
        ids1 = ticker_list[ticker1]
        counter = 0
        await inter.response.defer(with_message=True, ephemeral=True)
        while True:
            counter = counter + 1
            r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={ids},{ids1}&includeSecu=1&delay=0&more=1")
            d = r.json()
            items = "\n".join(f"```py\n{i['disSymbol']} Price: ${i['close']} Vol: {i['volume']}```" for i in d)
            em = disnake.Embed(title=f"Realtime Double-Quote for tickers: {ticker} {ticker1}", description=f"```py\nThis will tick for 200 times, and then it will become static.```", color=disnake.Colour.random())
            em.add_field(name=f"{ticker} & {ticker1} Double Quote:", value=f"{items}")
            em.set_footer(text="Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=em)
            if counter == 200:
                await inter.edit_original_message(f"Live Sequence Ended.", embed=em)
                break

    @stream.sub_command()
    async def quote(inter:disnake.AppCmdInter, ticker: str=commands.Param(autocomplete=tickerlist_autocomp)):
        """🫧Choose a stonk and stream their price in real-time for 200 ticks."""
        ids = ticker_list[ticker].lower()
        counter = 0
        await inter.response.defer(with_message=True, ephemeral=False)
        while True:
            counter = counter + 1
            r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={ids}&includeSecu=1&delay=0&more=1")
            d = r.json()
            items = "\n".join(f"```py\n{i['disSymbol']} Price: ${i['close']} Vol: {i['volume']}```" for i in d)
            em = disnake.Embed(title=f"Realtime Double-Quote for tickers: {ticker}", description=f"```py\nThis will tick for 200 times, and then it will become static.```", color=disnake.Colour.random())
            em.add_field(name=f"{ticker}", value=f"{items}")
            em.set_footer(text="Implemented by FUDSTOP Trading")
            await inter.edit_original_message(embed=em)
            if counter == 200:
                await inter.edit_original_message(f"Live Sequence Ended.", embed=em)
                break


    @stream.sub_command()
    async def double_crypto(inter:disnake.AppCmdInter, coin: str=commands.Param(autocomplete=coin_autocomp), coin2: str=commands.Param(autocomplete=coin_autocomp)):
        """🫧Choose two crypto coins and stream their price in real-time for 200 ticks."""
        ids = coins[coin]
        ids2 = coins[coin2]
        counter = 0
        await inter.response.defer(with_message=True, ephemeral=True)
        while True:
            counter = counter+ 1
            r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={ids},{ids2}&includeSecu=1&delay=0&more=1")
            d = r.json()
            items = "\n".join(f"{i['disSymbol']} ```py\nHigh: ${i['high']} Low: ${i['low']}``` ```py\nPrice: ${i['close']}```" for i in d)
            em = disnake.Embed(title="Realtime Crypto Quote - Ticks for 200 Times", description=f"{items}", color = disnake.Colour.random())
            await inter.edit_original_message(embed=em)
            if [i['close'] for i in d] >= [i['high'] for i in d]:
                await inter.edit_original_message(f"```py\nHIGHS BREACHED!```", embed=em)
            if counter == 1000:
                await inter.edit_original_message(f"```py\nLive Sequence Ended.```", embed=em)
                break

    @stream.sub_command()
    async def crypto(inter:disnake.AppCmdInter, coin: str=commands.Param(autocomplete=coin_autocomp)):
        """🫧Choose a crypto coin and stream their price in real-time for 200 ticks."""
        ids = coins[coin]
        counter = 0
        await inter.response.defer(with_message=True, ephemeral=True)
        while True:
            counter = counter+ 1
            r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids={ids}&includeSecu=1&delay=0&more=1")
            d = r.json()
            items = "\n".join(f"{i['disSymbol']} ```py\nHigh: ${i['high']} Low: ${i['low']}``` ```py\nPrice: ${i['close']}```" for i in d)
            em = disnake.Embed(title="Realtime Crypto Quote - Ticks for 200 Times", description=f"{items}", color = disnake.Colour.random())
            await inter.edit_original_message(embed=em)
            if [i['close'] for i in d] >= [i['high'] for i in d]:
                await inter.edit_original_message(f"```py\nHIGHS BREACHED!```", embed=em)
            if counter == 1000:
                await inter.edit_original_message(f"```py\nLive Sequence Ended.```", embed=em)
                break

    @stream.sub_command()
    async def topvolume(inter: disnake.AppCmdInter):
        """🫧Find the top option for volume in real time."""
        await inter.response.defer(with_message=True)
        counter = 0
        while True:
            counter = counter+1
            r = "https://quotes-gw.webullfintech.com/api/wlas/option/rank/list?regionId=6&rankType=volume&pageIndex=1&pageSize=50"
            response = requests.get(url=r)
            d = response.json()
            rank = d['rankType']
            direction = d['direction']
            data = d['data'][0]
            tabs = d['tabs']
            deriv = data['derivative']

            sym = deriv['unSymbol']
            direction = deriv['direction']
            weekly = deriv['weekly']
            expiry = deriv['expireDate']
            strike = deriv['strikePrice']
            price = deriv['price']
            close = deriv['close']
            changer = round(float(deriv['changeRatio'])*100,ndigits=2)
            cycle = deriv['cycle']
            optsym = deriv['symbol']


            values = data['values']
            dt = values['dt']
            volume = values['volume']
            oi = values['position']
            price = values['price']
            pchanger = round(float(values['changeRatio'])*100, ndigits=2)
            mid = values['middlePrice']
            turnover = values['turnover']
            poschange = values['positionChange']
            iv = round(float(values['implVol'])*100,ndigits=2)

            bT = data['belongTicker']
            name = bT['name']
            symbol = bT['disSymbol']
            closing = bT['close']
            scloser = round(float(bT['changeRatio'])*100, ndigits=2)
            svol = bT['volume']
            fiftyhigh = bT['fiftyTwoWkHigh']
            fiftylow = bT['fiftyTwoWkLow']
            o = bT['open']
            h = bT['high']
            low = bT['low']
            vr = bT['vibrateRatio']
            em = disnake.Embed(title="Real-time top Option Tracker (Volume)", description=f"```py\nCurrent top option: {symbol} | ${strike} | {direction} | {expiry}```", color=disnake.Colour.random())
            em.add_field(name=f"Volume / OI / OI Change", value=f"```py\nVolume: {volume} | OI: {oi}\n\nOI Change: {poschange}```")
            em.add_field(name=f"%Change on day / mid / price:", value=f"```py\nChange on Day: {pchanger}% | Price: ${price} | Mid: {mid}```")
            em.add_field(name=f"Implied Volatility:", value=f"```py\n{iv}%```")
            await inter.edit_original_message(embed=em)
            if counter == 100:
                em.clear_fields()
                await inter.send(f"```py\n Live Stream Ended. Scan for the top volume option again?```\n\n ```py\nClick me:```</stream topvolume:1028916905194561546>")
                
                break


    @stream.sub_command()
    async def tits(inter:disnake.AppCmdInter):
        """🫧Does exactly what it says..."""
        counter = 0
        await inter.response.defer(with_message=True)
        while True:
            counter = counter +1
            await inter.edit_original_message("```py\n( > *   *  )>\n(  .) Y (.  )```")
            sleep(0.1)
            await inter.edit_original_message("```py\n( > *   *  )>\n(  .)Y(.  )```")
            sleep(0.1)
            await inter.edit_original_message("```py\n( > *   *  )>\n(.  )Y(  .)```")
            sleep(0.1)
            await inter.edit_original_message("```py\n( > *   *  )>\n( . )Y( . )```")
            sleep(0.1)
            if counter == 50:
                break

def setup(bot:commands.Bot):
    bot.add_cog(Stream(bot))
    print(f"> Extension {__name__} is ready\n")