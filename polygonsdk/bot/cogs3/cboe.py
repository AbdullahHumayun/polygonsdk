import disnake
import requests

from disnake.ext import commands
from autocomp import ticker_autocomp
import base64


class Cboe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command()
    async def cboe(self, inter):
        pass

    @cboe.sub_command()
    async def spy(inter:disnake.AppCmdInter, date, ticker: str=commands.Param(autocomplete=ticker_autocomp)):
        """Get historic Options Data by date. Must be YYYY-MM-DD format."""
        await inter.response.defer(with_message=True)
        api_url=f"https://api.livevol.com/v1/delayed/allaccess/market/option-trades-breakdown?date={date}&symbol={ticker}"
        client_id = "brandybrand69420@gmail.com_api_client_1665098595"
        client_secret = "69a7aced5bb340d3a2c838952165b26d"

        identity_url = "https://id.livevol.com/connect/token"


        authorization_token  = base64.b64encode((client_id + ':' + client_secret).encode())
        headers = {"Authorization": "Basic " + authorization_token.decode('ascii')}
        payload = {"grant_type": "client_credentials"}

        # Requesting access token
        token_data = requests.post(identity_url, data=payload, headers=headers)
        access_token = token_data.json()['access_token']
        result = requests.get(api_url, headers={"Authorization": "Bearer " + access_token})
        data = result.json()
        symbol = data['symbol']
        cob = data['calls_on_bid']
        coa = data['calls_on_ask']
        otmcob = data['otm_calls_on_bid']
        otmcoa = data['otm_calls_on_ask']
        cbba = data['calls_between_bid_ask']
        pob = data['puts_on_bid']
        poa = data['puts_on_ask']
        otmpob = data['otm_puts_on_bid']
        otmpoa = data['otm_puts_on_ask']
        pbba = data['puts_between_bid_ask']
        callprem = round(float(data['call_premium']*0.000001),ndigits=2)
        putprem=round(float(data['put_premium']*0.000001),ndigits=2)
        call_delta = round(float(data['call_delta']*0.000001*10),ndigits=2)
        put_delta = round(float(data['put_delta']*0.000001*10),ndigits=2)
        call_gamma = round(float(data['call_gamma']*0.000001),ndigits=2)
        put_gamma = round(float(data['put_gamma']*0.000001),ndigits=2)
        call_vega = round(float(data['call_vega']*0.000001),ndigits=2)
        put_vega = round(float(data['put_vega']*0.000001),ndigits=2)
        callcount = data['call_trade_count']
        putcount = data['put_trade_count']
        calloi = round(float(data['call_oi']*0.000001),ndigits=2)
        putoi = round(float(data['put_oi']*0.000001),ndigits=2)
        em = disnake.Embed(title="Cboe Hanweck", description=f"```py\nData for {ticker} on trading day: {date}```", color=disnake.Colour.random(), url=f"https://api.livevol.com/v1/delayed/allaccess/market/option-trades-breakdown?date={date}&symbol={ticker}")
        # em.add_field(name=f"{ticker} Trade Summary:", value=f"```py\nCalls on Bid: {cob} Calls on Ask: {coa} Calls In-Between: {cbba}\nPuts on Bid: {pob} Puts on Ask: {poa} Puts In-Between: {pbba}```", inline=True)
        em.add_field(name=f"{ticker} OTM Summary:", value=f"```py\n🟩OTM Calls on Bid: {otmcob}\nOtm Calls on Ask: {otmcoa}``` ```py\n🟥OTM Puts on Bid: {otmpob}\nOTM Puts on Ask: {otmpoa}```", inline=False)
        em.add_field(name=f"Premium Snapshot:", value=f"```py\n🟩Call Premium: ${callprem} million``` ```py\n🟥Put Premium: ${putprem} million```",inline=True)
        #em.add_field(name=f"Greeks:", value=f"```py\nCall Delta: {call_delta}\n Put Delta: {put_delta}``` ```py\nCall Gamma: {call_gamma}\nPut Gamma: {put_gamma}``` ```py\nCall Vega: {call_vega}\nPut Vega: {put_veta}```", inline=True)
        em.add_field(name=f"Trade Count:", value=f"```py\n🟩Call trade count:\n{callcount}``` ```py\n🟥Put trade count:\n{putcount}```", inline=True)
        em.add_field(name=f"Open Interest:", value=f"```py\n🟥Put OI: {putoi} million.``` ```py\n🟩Call OI: {calloi} million.```", inline=True)
        em.add_field(name=f"Delta:", value=f"```py\nCalls: {call_delta}% average chance to close ITM by expiry.``` ```py\nPuts: {put_delta}% average chance to close ITM by expiry```", inline=False)
        em.add_field(name=f"Vega:", value=f"```py\nCalls: {call_vega}``` ```py\nPuts: {put_vega}```", inline=False)
        em.add_field(name=f"Gamma:", value=f"```py\nCalls: {call_gamma}``` ```py\nPuts: {put_gamma}```", inline=False)
        await inter.edit_original_message(embed=em)




def setup(bot):
    bot.add_cog(Cboe(bot))
    print(f"> Extension {__name__} is ready\n")