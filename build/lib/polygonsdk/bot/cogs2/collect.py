import disnake
from disnake.ext import commands
import requests
import webull
from autocomp import ticker_autocomp
import json




class Collect(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def collect(self, inter):
        """Collect slash commands category."""
        pass

    @collect.sub_command()
    async def collect_ticker(inter:disnake.AppCmdInter, keyword):
        """Collects webull tickers for json formatting in python dict."""
        await inter.response.defer(with_message=True)

        r = requests.get(url=f"https://quotes-gw.webullfintech.com/api/search/pc/tickers?keyword={keyword}&pageIndex=1&pageSize=1000")
        d = r.json()
        data = d['data']
        for i in data:
            tickerid = i.get('tickerId')
            sym = i.get('disSymbol')
            (print(f"''{sym}'':''{tickerid}'',"))
            json_object = json.dumps((f"''{sym}'':''{tickerid}'',"), indent=4)
            await inter.edit_original_message(f"Ticker added: ```py\n''{sym}'':''{tickerid}'',```")
            with open('pairs.txt', 'a') as outfile:
                json.dump(f"''{sym}'':''{tickerid}'',",outfile,indent=2)
                outfile.close()


    @collect.sub_command() #discord bot decorator
    async def get_webull_tickers(inter: disnake.AppCmdInter, symbol): #discord bot command name and define arguments
        """Automatically pairs ticker IDS to symbols in pythonic format."""
        await inter.response.defer(with_message=True) #defer the response to give the requests time to work for us
        r = requests.get(url=f"https://api.coinmarketcap.com/dexer/v3/dexer/search/main-site?keyword={symbol}") # the requests url
        data = r.json() # converting the request to json data
        data = data['data'] #you print data here to get a cleaner output to grab variable names from
        for i in data: #for all items in data :
            tickerid = i.get('tickerId') #we want the tickerid
            symbol = i.get('disSymbol') #and we want the symbol
            em = disnake.Embed(title="Webull Ticker Gather", description=f"\n Success! Search query {symbol} has been added to the list of ticker / id pairs.", color=disnake.Colour.random()) #defining the embed for discord output
            print(f"''{symbol}'':''{tickerid}'',") #print results to consol
            await inter.edit_original_message(embed = em) #output to discord

    @collect.sub_command()
    async def get_coin_ids(inter:disnake.AppCmdInter, symbol):
        """Builds a python dictionary for Coins to use in commands."""
        await inter.response.defer(with_message=True)
        r = requests.get(url=f"https://api.coinmarketcap.com/dexer/v3/dexer/search/main-site?keyword={symbol}")
        d = r.json()
        data = d['data']
        totals = data['total']
        pairs=data['pairs']
        for i in pairs:
            try:
                cid = i.get('platFormCryptoId')
                sym = i.get('baseTokenSymbol')
                em = disnake.Embed(title="Coin Symbol Pairer!", description=f"```py\nSuccess! Search query {sym} has been added to the crypto list !```", color=disnake.Colour.random())
                await inter.edit_original_message(embed=em)
                with open('coinsdude.txt', 'a') as outfile:
                    json.dump(f"''{sym}'':''{cid}'',", outfile, indent=2)
                    outfile.close()
            except:
                if KeyError:
                    await inter.send("Try again with a different keyword.")

    @collect.sub_command()
    async def optionids(inter:disnake.AppCmdInter, expiry_date, stock:str=commands.Param(autocomplete=ticker_autocomp), direction: str=commands.Param(choices=["call", "put", "all"])):
        """Scan and return options for a ticker"""
        await inter.response.defer(with_message=True)
        wb = webull.webull()
        option_chain = wb.get_options(stock="AMD", count=5, direction=f"{direction}", expireDate=f"{expiry_date}")
        d = wb.get_options_bars(derivativeId=option_chain[0]['call']['tickerId'], interval="1m")
        high = d['high']
        low = d['low']
        open = d['open']
        vwap = d['vwap']
        for i in vwap:
            print(i)
        em = disnake.Embed(title=f"Vwap for {stock}", description=f"```py\nContract:\n\n")
        await inter.edit_original_message(embed=em)

def setup(bot):
    bot.add_cog(Collect(bot))
    print(f"> Extension {__name__} is ready\n")