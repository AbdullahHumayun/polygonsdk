"""COG"""
import requests
import disnake
from disnake.ext import commands
import stocksera
from autocomp import ticker_autocomp
from views.learnviews import NotesView
from cfg import YOUR_FINNHUB_KEY,YOUR_STOCKSERA_KEY, YOUR_FMP_KEY


client = stocksera.Client(api_key=YOUR_STOCKSERA_KEY)

class Social(commands.Cog):
    """Social Commands"""
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command()
    async def social(self,inter):
        """Social slash commands category."""


    @social.sub_command()
    async def score(self,inter:disnake.AppCmdInter,
        ticker: str=commands.Param(autocomplete=ticker_autocomp)):
        """🫂Lookup the positive vs negative mentions for a ticker."""
        await inter.response.defer(with_message=True, ephemeral=True)
        rscore = requests.get(url=f"https://finnhub.io/api/v1/stock/social-sentiment?symbol={ticker}&token={YOUR_FINNHUB_KEY}")
        dscore = rscore.json()
        reddit = dscore['reddit']
        twitter = dscore['twitter']
        twitpositive = sum([i['positiveMention'] for i in twitter])
        twitnegative = sum([i['negativeMention'] for i in twitter])
        redpositive = sum([i['positiveMention'] for i in reddit])
        rednegative = sum([i['negativeMention'] for i in reddit])
        condition = twitpositive > twitnegative
        condition2 = redpositive > rednegative
        emb = disnake.Embed(
            title=f"Social Sentiment for {ticker}",
            color=disnake.Colour.dark_orange())
        emb.add_field(name="Twitter:",
        value=f"There have been a total of 🟢 **{twitpositive}** positive mentions for **{ticker}** out of Twitter today."
        "\n\n There have been a total of 🔴 **{twitnegative}** negative mentions for **{ticker}** out of Twitter today.", inline=False)
        emb.add_field(name="Reddit:",
        value=f"There have been a total of 🟢 **{redpositive}** positive mentions for **{ticker}** out of Reddit today."
        "\n\n There have been a total of 🔴 **{rednegative}** negative mentions for **{ticker}** out of Reddit today.", inline=False)
        if condition is True:
            emb.add_field(name="Twitter Sentiment:", value=f"```py\nThe overall sentiment from Twitter today has been 🟢 Positive for {ticker}.```", inline=False)
            await inter.edit_original_message(embed=emb)
        elif condition2 is True:
            emb.add_field(name="Twitter:", value=f"The overall sentiment from Reddit today has been  🟢 Positive for {ticker}.```", inline=False)
            await inter.edit_original_message(embed=emb)


    @social.sub_command()
    async def wsb(self, inter: disnake.AppCmdInter, symbol: str = commands.Param(autocomplete=ticker_autocomp)):
        """🫂Returns mentions of calls/puts from Wallstreet Bets for a Ticker"""
        await inter.response.defer(with_message=True, ephemeral=True)
        data = client.wsb_mentions(days=2, ticker=f"{symbol}")
        index = data[0]
        index2 = data[1]
        index3 = data[3]
        index4 = data[4]
        index5 = data[5]
        mentions = index['mentions']
        calls = index['calls']
        puts = index['puts']
        date_updated= index['date_updated']
        mentions2 = index2['mentions']
        calls2 = index2['calls']
        puts2 = index2['puts']
        date_updated2= index2['date_updated']
        mentions3 = index3['mentions']
        calls3 = index3['calls']
        puts3 = index3['puts']
        date_updated3= index3['date_updated']
        mentions4 = index4['mentions']
        calls4 = index4['calls']
        puts4 = index4['puts']
        date_updated4= index4['date_updated']
        mentions5 = index5['mentions']
        calls5 = index5['calls']
        puts5 = index5['puts']
        date_updated5= index5['date_updated']
        totalcalls = calls + calls2 + calls3 + calls4 + calls5
        totalputs = puts + puts2 + puts3 + puts4 + puts5
        totalmentions = mentions + mentions2 + mentions3 + mentions4 + mentions5
        emb = disnake.Embed(title=f"Wallstreet Bets mentions for {symbol}", description="Counts the number of mentions, call-mentions, and put mentions since the last measurement.")
        emb.add_field(name=f"{date_updated}", value=f"Mentions: **{mentions}**\n Call Mentions🟢: **{calls}**\n Put Mentions🔴: **{puts}**", inline=False)
        emb.add_field(name=f"{date_updated2}", value=f"Total Mentions: **{mentions2}**\n Call Mentions🟢: **{calls2}**\n Put Mentions🔴: **{puts2}**", inline = False)
        emb.add_field(name=f"{date_updated3}", value=f"Total Mentions: **{mentions3}**\n Call Mentions🟢: **{calls3}**\n Put Mentions🔴: **{puts3}**", inline = True)
        emb.add_field(name=f"{date_updated4}", value=f"Total Mentions: **{mentions4}**\n Call Mentions🟢: **{calls4}**\n Put Mentions🔴: **{puts4}**", inline = True)
        emb.add_field(name=f"{date_updated5}", value=f"Total Mentions: **{mentions5}**\n Call Mentions🟢: **{calls5}**\n Put Mentions🔴: **{puts5}**", inline = True)
        emb.add_field(name=f"TOTAL MENTIONS FOR {symbol}:", value=f"Total Mentions: **{totalmentions}** \n Total Calls: **{totalcalls}** \n Total Puts: **{totalputs}**")
        emb.set_image(url="https://d1lss44hh2trtw.cloudfront.net/resize?type=webp&url=https%3A%2F%2Fshacknews-www.s3.amazonaws.com%2Fassets%2Farticle%2F2021%2F04%2F16%2Fwallstreetbets_feature.jpg&width=2064&sign=IUz-mrgqo67_-6l6qfh5Wbx_oyfRgepTXxZVyuuyV8s")

        await inter.edit_original_message(embed=emb, view=NotesView())
    @social.sub_command()
    async def tradingview_spying(self, inter: disnake.AppCmdInter):
        """🫂Spy on the Public TradingView Chat"""
        counter = 1
        await inter.response.defer(with_message=True, ephemeral=True)
        while True:
            counter = 1 + 1
            rtv = requests.get(url="https://www.tradingview.com/chats/public/get/")
            dtv = rtv.json()
            title = [i['title'] for i in dtv]
            for items in dtv:
                title = items.get('title')
                msgs_last_text = items.get('msgs_last_text')
                emb = disnake.Embed(title="Tradingview SPYING", description="SPYing on the unsafe, unsound, and unsatisfying garbage known as TRADINGVIEW. The messages you see are the most recent message posted and description of the room that the traders are in. \n\n PSYCHOLOGICAL EXPERIMENTATION? If I can do it - so can they.", color=disnake.Colour.random())
                emb.add_field(name=f"TITLE OF ROOM: **{title}**", value=f"\n\n\nLATEST MESSAGE: **{msgs_last_text}**")
                emb.set_footer(icon_url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif", text="Implemented by Fudstop Trading")

                await inter.edit_original_message(embed=emb)
                if counter == 30:
                    break
    @social.sub_command()
    async def sentiment(self, inter:disnake.ApplicationCommandInteraction, symbol: str = commands.Param(autocomplete=ticker_autocomp)):
        """🫂Returns Buy / Sell / Hold Ratings for a Specific Stock"""
        await inter.response.defer(with_message=True, ephemeral=True)
        sentimentr = requests.get(url=f"https://financialmodelingprep.com/api/v4/upgrades-downgrades-consensus?symbol={symbol}&apikey={YOUR_FMP_KEY}")
        sentimentd = sentimentr.json()
        index = sentimentd[0]
        symbol = index["symbol"]
        strongbuy = index["strongBuy"]
        buy = index["buy"]
        hodl = index["hold"]
        sell = index["sell"]
        strongsell= index["strongSell"]
        consensus = index["consensus"]
        embed=disnake.Embed(title=f"Sentiment Consensus for {symbol}", color=disnake.Colour.random())
        embed.add_field(name="Strong Buy", value=f"**{strongbuy}**")
        embed.add_field(name="Buy", value=f"**{buy}**")
        embed.add_field(name="Hodl", value=f"**{hodl}**")
        embed.add_field(name="Sell", value=f"**{sell}**")
        embed.add_field(name="Strong Sell", value=f"**{strongsell}**")
        embed.add_field(name="Consensus Total", value=f"**{consensus}**")
        embed.set_footer(
            text="Data Provided by Financial Modeling Prep and Implemented by FUDSTOP Trading.",
            icon_url="https://uploads-ssl.webflow.com/62661f74776abb77ef7621a8/6272ac0a541297826e1a5209_963244979063517184.gif")
        embed.set_thumbnail(
            url="https://static.wixstatic.com/media/3235bb_fedadfcf38994349b7fa98fbf3f6f372~mv2.gif")
        await inter.edit_original_message(embed=embed)

async def setup(bot:commands.Bot):
    await bot.add_cog(Social(bot))
    print(f"> Extension {__name__} is ready\n")