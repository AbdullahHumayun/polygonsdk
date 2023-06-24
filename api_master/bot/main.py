import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import disnake
from disnake.ext import commands

from tabulate import tabulate
import aiohttp
from sdks.polygon_sdk.async_polygon_sdk import AsyncPolygonSDK
from sdks.polygon_sdk.async_options_sdk import PolygonOptionsSDK
from tabulate import tabulate

from sdks.webull_sdk.webull_sdk import AsyncWebullSDK
from _discord import emojis
from testicles import get_option_data

import pandas as pd
from utils.technicals import bullish_continuationdiamond,bullish_continuationwedge,triplebottom,diamondbottom,roundedbottom,gapdown,gapup,diamondtop,bullish_gravestone,islandtop,doubletop,macd,bullish_headandshoulders
from utils.technicals import bollingerbands,momentum,bearish_outsidebar,bearflag,cci,bullish_outsidebar,tripletop,bullflag,rsi,doublebottom
from views.learnviews import MenuStart,AlertStart, DiscordStart,TAStart,MarketsView,CryptoViewStart,PageTwoView,PageThreeView,HighShortsViewStart,LowFloatDropdown
from views.learnviews import ForexViewStart,FTDViewStart,LosersViewStart,GainersViewStart,ActiveViewStart
from views.learnviews import TotalOIViewStart,TotalVolumeViewStart
from views.learnviews import CoreStart, LinksStartView,LitStart,DataViewStart
from views.learnviews import WebullCmdViewStart,DDCmdViewStart,OptionCmdViewStart,FlowCmdViewStart,DPSCmdViewStart,EarningsCmdViewStart,EconomyCmdViewStart,LearnCmdViewStart,StreamCmdViewStart,StockCmdViewStart,ChartingCmdViewStart
from views.learnviews import HelpStart,VideoStartView,VideoStart2View,VideoStart3View,TopOptionsViewStart, AgencyViewStart
from views.learnviews import DTCCViewStart,NYSEViewStart, CBOEViewStart, OFRDataViewStart
from views.learnviews import TopOIDownViewStart,TopOIUpViewStart,TopIVViewStart,TopOIViewStart,TopVolumeViewStart,TotalTurnoverViewStart,TotalOIViewStart,TotalVolumeViewStart
from views.learnviews import FedDataStart,FINRADataStart,BlockchainDataStart,InflationDataStart,EconomicDataStart,TreasuryDataStart,HKEXDataStart,MMFDataStart,RepoDataStart
from views.learnviews import StockPage1,StockPage2,StockPage3,StockPage4,StockPage5, AppStart, ToolsViewStart
from views.learnviews import OFRViewStart, RepoCitedViewStart,CriteriaView,CommandsStart,PermaFTDViewStart
from views.learnviews import AvoidView

import asyncio


from cfg import YOUR_API_KEY, YOUR_DISCORD_BOT_TOKEN


polygon = AsyncPolygonSDK(YOUR_API_KEY)
poly_options = PolygonOptionsSDK(YOUR_API_KEY)
webull = AsyncWebullSDK()

intents=disnake.Intents.all()
class PersistentViewBot(commands.Bot):
    def __init__(self, command_prefix, intents, ticker=None, embeds=None):
        self.ticker = ticker
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.persistent_views_added = False
        self.embeds = embeds

    async def on_ready(self):
        if not self.persistent_views_added:
            # Register the persistent view for listening here.
            # Note that this does not send the view to any message.
            # In order to do this you need to first send a message with the View, which is shown below.
            # If you have the message_id you can also pass it as a keyword argument, but for this example
            # we don't have one.
            self.add_view(AvoidView())
            self.add_view(PageTwoView())
            self.add_view(PageThreeView())
            self.add_view(CommandsStart())
            self.add_view(MenuStart())
            self.add_view(CoreStart())
            self.add_view(AlertStart())
            self.add_view(LitStart())
            self.add_view(DiscordStart())
            self.add_view(TAStart())
            self.add_view(MarketsView())
            self.add_view(CryptoViewStart())
            self.add_view(ForexViewStart())
            self.add_view(HighShortsViewStart())
            self.add_view(LowFloatDropdown())
            self.add_view(FTDViewStart())
            self.add_view(LosersViewStart())
            self.add_view(GainersViewStart())
            self.add_view(ActiveViewStart())
            self.add_view(TotalOIViewStart())
            self.add_view(TotalVolumeViewStart())
            self.add_view(LinksStartView())
            self.add_view(AppStart())
            self.add_view(TopOptionsViewStart())
            self.add_view(WebullCmdViewStart())
            self.add_view(OptionCmdViewStart())
            self.add_view(PermaFTDViewStart())
            self.add_view(OFRViewStart())
            self.add_view(DDCmdViewStart())
            self.add_view(FlowCmdViewStart())
            self.add_view(DPSCmdViewStart())
            self.add_view(EconomyCmdViewStart())
            self.add_view(EarningsCmdViewStart())
            self.add_view(FlowCmdViewStart())
            self.add_view(StreamCmdViewStart())
            self.add_view(ChartingCmdViewStart())
            self.add_view(StockCmdViewStart())
            self.add_view(HelpStart())
            self.add_view(LearnCmdViewStart())
            self.add_view(ToolsViewStart())
            self.add_view(NYSEViewStart())
            self.add_view(DTCCViewStart())
            self.add_view(CBOEViewStart())
            self.add_view(StockPage1())
            self.add_view(StockPage2())
            self.add_view(StockPage3())
            self.add_view(StockPage4())
            self.add_view(StockPage5())
            self.add_view(TopIVViewStart())
            self.add_view(TopOIDownViewStart())
            self.add_view(TopOIUpViewStart())
            self.add_view(TotalTurnoverViewStart())
            self.add_view(TopVolumeViewStart())
            self.add_view(TopOIViewStart())
            self.add_view(VideoStartView())
            self.add_view(VideoStart3View())
            self.add_view(VideoStart2View())
            self.add_view(OFRDataViewStart())
            self.add_view(AgencyViewStart())
            self.add_view(DataViewStart())
            self.add_view(InflationDataStart())
            self.add_view(BlockchainDataStart())
            self.add_view(HKEXDataStart())
            self.add_view(FINRADataStart())
            self.add_view(MMFDataStart())
            self.add_view(FedDataStart())
            self.add_view(TreasuryDataStart())
            self.add_view(EconomicDataStart())
            self.add_view(RepoDataStart())
            self.add_view(RepoCitedViewStart())
            self.add_view(CriteriaView())
            self.add_view(AvoidView())
            self.add_view(ServerMenuView())

            self.persistent_views_added = True


        print(f"Logged in as {self.user} (ID: {self.user.id})")





bot = PersistentViewBot(command_prefix=">>", intents=intents)



class RestartStreamView(disnake.ui.View):
    def __init__(self, tickers=str):
        self.tickers=tickers
        super().__init__(timeout=None)


    @disnake.ui.button(style=disnake.ButtonStyle.green,emoji=f"{emojis.greencircle}", custom_id="startbutton")
    async def start(self, button: disnake.ui.Button, inter:disnake.AppCmdInter):
        """Starts the live-stream"""
        button.disabled = False
        await allskew(interaction=inter, tickers=self.tickers)


global_inter = None
global_tickers = None
@bot.event
async def on_disconnect():
    print("Bot has disconnected, waiting to reconnect...")



ticker_symbols = ['AAPL', 'MSFT', 'AMZN', 'NVDA', 'GOOGL', 'TSLA', 'GOOG', 'META', 'UNH', 
                  'JNJ', 'XOM', 'JPM', 'V', 'LLY', 'PG', 'AVGO', 'MA', 'HD', 'MRK', 'CVX', 'PEP', 
                  'ABBV', 'KO', 'COST', 'ADBE', 'PFE', 'WMT', 'MCD', 'CSCO', 'CRM', 'TMO', 'ACN', 
                  'BAC', 'ABT', 'NFLX', 'ORCL', 'LIN', 'AMD', 'CMCSA', 'DIS', 'DHR', 'TXN', 'WFC', 'HAL',
                  'NEE', 'VZ', 'PM', 'RTX', 'BMY', 'INTC', 'NKE', 'HON', 'QCOM', 'LOW', 'SPGI', 'INTU',
                  'UNP', 'UPS', 'COP', 'AMGN', 'CAT', 'IBM', 'AMAT', 'BA', 'MDT', 'SBUX', 'ISRG', 
                  'GE', 'DE', 'NOW', 'T', 'MS', 'PLD', 'ELV', 'GS', 'LMT', 'BLK', 'MDLZ', 'SYK', 
                  'AXP', 'BKNG', 'GILD', 'ADI', 'TJX', 'ADP', 'C', 'MMC', 'VRTX', 'CVS', 'AMT', 
                  'REGN', 'LRCX', 'CI', 'CB', 'ZTS', 'SCHW', 'BSX', 'MO', 'ETN', 'SO', 'TMUS', 'SNAP','AMC','GME',
                  'PGR', 'PYPL', 'PANW', 'FI', 'BDX', 'MU', 'EQIX', 'SPY', 'U', 'W', 'SHOP', 'KRE', 'EEM', 'EWZ', 'BABA', 'BIDU', 'BEKE']


import datetime
@bot.slash_command()
async def allskew(inter: disnake.AppCmdInter, tickers= str):
    """Scan multiple skews in real time"""
    if not tickers:
        tickers = ticker_symbols
    tickers = tickers.split(',')

    await inter.response.defer()

    # Set the time for next refresh
    next_disconnect_time = datetime.datetime.now() + datetime.timedelta(minutes=14)
    view = RestartStreamView()
    view.start.disabled = True
    counter = 0
    while True:
        counter = counter  +1

 
            


        async with aiohttp.ClientSession() as session:
            # Get prices for all tickers concurrently
            price_tasks = [polygon.get_stock_price(ticker) for ticker in tickers]
            prices = await asyncio.gather(*price_tasks)
            ticker_prices = dict(zip(tickers, prices))  # Assuming no None prices

            # Now get option data concurrently
            option_data_tasks = [get_option_data(ticker, ticker_prices[ticker], session) for ticker in tickers]
            results = await asyncio.gather(*option_data_tasks)
            # Filter out None results and add valid results to data_list
            data_list = [result for result in results if result is not None]

            data_list = sorted(data_list, key=lambda x: x[4], reverse=True)
            # Create a new list that only includes the parts you want to display
            display_data = [row[:6] for row in data_list]

            # Now, display_data contains the data you want to display for all tickers. Format it into a table and send it in discord chat.
            table = tabulate(display_data, headers=['Symbol', 'Strike', 'Price', 'Expiry', 'IV', 'Skew'], tablefmt='fancy')

            embed = disnake.Embed(title=f"All - Skew", description=f"```\n" + table + "\n```", color=disnake.Colour.random())
            embed.set_footer(text=f"{counter} | Data Provided by Polygon.io | Implemented by FUDSTOP")
            await inter.edit_original_message(embed=embed, view=view) # Send the table in a code block
            if counter == 100:
                view.start.disabled = False
                await bot.close()
                break
@bot.event
async def on_disconnect():
    print("Bot has disconnected, waiting to reconnect...")

@bot.event
async def on_ready():
    print("Bot has reconnected, restarting allskew command...")
    if global_inter is not None and global_tickers is not None:
        await allskew(global_inter, global_tickers)
class ServerMenu(disnake.ui.ChannelSelect):
    def __init__(self):
        
        super().__init__(custom_id="ServerMenuSel",placeholder="Select A Channel!",min_values=1,max_values=1,channel_types=[disnake.ChannelType.forum])

    async def callback(self, interaction: disnake.ApplicationCommandInteraction):
        if self.values:
            selected_channel = self.values[0]
            embed = disnake.Embed(title=f"{emojis.ls}{emojis.le}{emojis.lr}{emojis.lv}{emojis.le}{emojis.lr}🌟{emojis.lm}{emojis.le}{emojis.ln}{emojis.lu}")
            
            await interaction.send(f"The selected channel is: {selected_channel.mention}", ephemeral=False)
        else:
            await interaction.send("No channel was selected!", ephemeral=False)


class ServerMenuView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(ServerMenu())
        self.add_item(TextMenu())
        self.add_item(ThreadMenu())

class ServerMenu(disnake.ui.ChannelSelect):
    def __init__(self):
        
        super().__init__(custom_id="ServerMenuSel2", placeholder="Select or Search for a Forum Channel!", min_values=1, max_values=1, channel_types=[disnake.ChannelType.forum])

    async def callback(self, interaction: disnake.ApplicationCommandInteraction):
        if self.values:
            selected_channel = self.values[0]
            await interaction.send(f"The selected channel is: {selected_channel.mention}", delete_after=10)
        else:
            await interaction.send("No channel was selected!", delete_after=10)


class TextMenu(disnake.ui.ChannelSelect):
    def __init__(self):
        
        super().__init__(custom_id="ServerMenuSel3", placeholder="Select or Search for a Text Channel!", min_values=1, max_values=1, channel_types=[disnake.ChannelType.text])

    async def callback(self, interaction: disnake.ApplicationCommandInteraction):
        if self.values:
            selected_channel = self.values[0]
            await interaction.send(f"The selected channel is: {selected_channel.mention}", delete_after=10)
        else:
            await interaction.send("No channel was selected!", ephemeral=False)


class ThreadMenu(disnake.ui.ChannelSelect):
    def __init__(self):
        
        super().__init__(custom_id="ServerMenuSel4", placeholder="Select or Search for a Thread!", min_values=1, max_values=1, channel_types=[disnake.ChannelType.public_thread])

    async def callback(self, interaction: disnake.ApplicationCommandInteraction):
        if self.values:
            selected_channel = self.values[0]
            await interaction.send(f"The selected channel is: {selected_channel.mention}", delete_after=10)
        else:
            await interaction.send("No channel was selected!", ephemeral=False)








@bot.listen()
async def on_message( message: disnake.Message):
    
    if "repo?" in message.content:
        await message.channel.send("```py\nPosts every day at 12:15PM CST.``` https://www.newyorkfed.org/markets/desk-operations/reverse-repo")
    if "start!" in message.content:
        await message.channel.send(view=LinksStartView())
    if "short volume?" in message.content:
        await message.channel.send("```py\nHere is FINRA's daily short volume files. Simply open the current date's file and search for the ticker with control + f or the search feature in your phone.``` https://www.finra.org/finra-data/browse-catalog/short-sale-volume-data/daily-short-sale-volume-files ")


    if "market share?" in message.content:
        await message.channel.send(
            "```py\nView the lit and un-lit market share graph from CBOE.``` https://media.discordapp.net/attachments/896207280117264434/1045612084169293824/image.png?width=999&height=671")



    if "rsi?" in message.content:
        await message.channel.send(rsi, delete_after=10)

    if "macd" in message.content:
        await message.channel.send(macd, delete_after=10)

    if "bullish continuation diamond" in message.content:
        await message.channel.send(bullish_continuationdiamond, delete_after=10)

    if "bullish continuationwedge" in message.content:
        await message.channel.send(bullish_continuationwedge)

    if "bullish gravestone" in message.content:
        await message.channel.send(bullish_gravestone, delete_after=10)

    if "bullish heada and shoulders" in message.content:
        await message.channel.send(bullish_headandshoulders, delete_after=10)

    if "triple bottom" in message.content:
        await message.channel.send(triplebottom, delete_after=10)

    if "diamond bottom" in message.content:
        await message.channel.send(diamondbottom, delete_after=10)


    if "rounded bottom" in message.content:
        await message.channel.send(roundedbottom, delete_after=10)

    if "double bottom" in message.content:
        await message.channel.send(doublebottom, delete_after=10)


    if "gap down" in message.content:
        await message.channel.send(gapdown, delete_after=10)


    if "gap up" in message.content:
        await message.channel.send(gapup, delete_after=10)



    if "diamond top" in message.content:
        await message.channel.send(diamondtop, delete_after=10)


    if "triple top" in message.content:
        await message.channel.send(tripletop, delete_after=10)


    if "double top" in message.content:
        await message.channel.send(doubletop, delete_after=10)


    if "island top" in message.content:
        await message.channel.send(islandtop, delete_after=10)


    if "bbands" in message.content:
        await message.channel.send(bollingerbands, delete_after=10)

    if "momentum" in message.content:
        await message.channel.send(momentum, delete_after=10)

    if "oi?" in message.content:
        view=disnake.ui.View()
        await message.channel.send(view=TotalOIViewStart(), delete_after=10)


    if "top volume?" in message.content:
        await message.channel.send(view=TotalVolumeViewStart(), delete_after=10)



    if "mainmenu" in message.content:
        await message.channel.send(view=LitStart(), delete_after=10)


    if "data?" in message.content:
        await message.channel.send(view=DataViewStart(), delete_after=10)


    if "webull commands" in message.content:
        await message.channel.send(view=WebullCmdViewStart(), delete_after=10)


    if "dd commands" in message.content:
        await message.channel.send(view=DDCmdViewStart(), delete_after=10)


    if "option commands" in message.content:
        await message.channel.send(view=OptionCmdViewStart(), delete_after=10)


    if "flow commands" in message.content:
        await message.channel.send(view=FlowCmdViewStart(), delete_after=10)


    if "dps commands" in message.content:
        await message.channel.send(view=DPSCmdViewStart(), delete_after=10)


    if "earnings commands" in message.content:
        await message.channel.send(view=EarningsCmdViewStart(), delete_after=10)


    if "economy commands" in message.content:
        await message.channel.send(view=EconomyCmdViewStart(), delete_after=10)


    if "learn commands" in message.content:
        await message.channel.send(view=LearnCmdViewStart(), delete_after=10)


    if "stream commands" in message.content:
        await message.add_reaction(emojis.clockspin)
        await message.channel.send(view=StreamCmdViewStart(), delete_after=10)


    if "stock commands" in message.content:
        await message.channel.send(view=StockCmdViewStart(), delete_after=10)


    if "charting commands" in message.content:
        await message.channel.send(view=ChartingCmdViewStart())

    if "send conditions" in message.content:
        await message.channel.send(file=disnake.File("views/TRADE CONDITIONS.csv"))

    if "videos1" in message.content:
        await message.channel.send(view=VideoStartView())


    if "videos2" in message.content:
        await message.channel.send(view=VideoStart2View())

    if "conditions" in message.content:
        from cfg import YOUR_API_KEY
        embeds = [ 
        disnake.Embed(title=f"Conditions", url=f"https://api.polygon.io/v3/reference/conditions?asset_class=options&apiKey={YOUR_API_KEY}"),
        disnake.Embed(title=f"Conditions", url=f"https://api.polygon.io/v3/reference/conditions?cursor=YXA9MTAmYXM9JmFzc2V0X2NsYXNzPW9wdGlvbnMmbGltaXQ9MTAmc29ydD1hc3NldF9jbGFzcw&apiKey={YOUR_API_KEY}"),
        disnake.Embed(title=f"Conditions", url=f"https://api.polygon.io/v3/reference/conditions?cursor=YXA9MTAmYXM9JmFzc2V0X2NsYXNzPW9wdGlvbnMmbGltaXQ9MTAmc29ydD1hc3NldF9jbGFzcw&apiKey={YOUR_API_KEY}"),
        disnake.Embed(title=f"Conditions", url=f"https://api.polygon.io/v3/reference/conditions?cursor=YXA9MTAmYXM9JmFzc2V0X2NsYXNzPW9wdGlvbnMmbGltaXQ9MTAmc29ydD1hc3NldF9jbGFzcw&apiKey={YOUR_API_KEY}"),
        disnake.Embed(title=f"Conditions", url=f"https://api.polygon.io/v3/reference/conditions?cursor=YXA9MjAmYXM9JmFzc2V0X2NsYXNzPW9wdGlvbnMmbGltaXQ9MTAmc29ydD1hc3NldF9jbGFzcw&apiKey={YOUR_API_KEY}"),
        disnake.Embed(title=f"Conditions", url=f"https://api.polygon.io/v3/reference/conditions?cursor=YXA9MzAmYXM9JmFzc2V0X2NsYXNzPW9wdGlvbnMmbGltaXQ9MTAmc29ydD1hc3NldF9jbGFzcw&apiKey={YOUR_API_KEY}")
        ]
        await message.channel.send(view=AlertStart(embeds[0]), embed=embeds[0])

    if "videos3" in message.content:
        await message.channel.send(view=VideoStart3View())


    if "top options?" in message.content:
        await message.channel.send(view=TopOptionsViewStart())


    if "agency?" in message.content:
        await message.channel.send(view=AgencyViewStart())


    if "dtcc?" in message.content:
        await message.channel.send(view=DTCCViewStart())


    if "nyse?" in message.content:
        await message.channel.send(view=NYSEViewStart())


    if "cboe?" in message.content:
        await message.channel.send(view=CBOEViewStart())


    if "top oi_down?" in message.content:
        await message.channel.send(view=TopOIDownViewStart())


    if "top oi_up?" in message.content:
        await message.channel.send(view=TopOIUpViewStart())


    if "top iv?" in message.content:
        await message.channel.send(view=TopIVViewStart())


    if "top oi?" in message.content:
        await message.channel.send(view=TopOIViewStart())


    if "top volume?" in message.content:
        await message.channel.send(view=TopVolumeViewStart())


    if "total turnover?" in message.content:
        await message.channel.send(view=TotalTurnoverViewStart())


    if "total oi?" in message.content:
        await message.channel.send(view=TotalOIViewStart())


    if "total volume?" in message.content:
        await message.channel.send(view=TotalVolumeViewStart())


    if "fed data?" in message.content:
        await message.channel.send(view=FedDataStart())


    if "finra data?" in message.content:
        await message.channel.send(view=FINRADataStart())


    if "blockchain data?" in message.content:
        await message.channel.send(view=BlockchainDataStart())


    if "inflation data?" in message.content:
        await message.channel.send(view=InflationDataStart())


    if "economic data?" in message.content:
        await message.channel.send(view=EconomicDataStart())


    if "treasury data?" in message.content:
        await message.channel.send(view=TreasuryDataStart())


    if "hkex data?" in message.content:
        await message.channel.send(view=HKEXDataStart())


    if "mmf data?" in message.content:
        await message.channel.send(view=MMFDataStart())


    if "repo data?" in message.content:
        await message.channel.send(view=RepoDataStart())


    if "bull flag?" in message.content:
        await message.channel.send(bullflag)


    if "bear flag?" in message.content:
        await message.channel.send(bearflag)


    if "bearish_outsidebar?" in message.content:
        await message.channel.send(bearish_outsidebar)


    if "bullish_outsidebar?" in message.content:
        await message.channel.send(bullish_outsidebar)

    if "cci?" in message.content:
        await message.channel.send(cci)

    if "treasury auctions?" in message.content:
        await message.channel.send("```py\nHere are the latest Treasury Auction Operations for the last two weeks:``` https://markets.newyorkfed.org/api/tsy/sales/results/summary/lastTwoWeeks.csv")

    if "soma holdings?" in message.content:
        await message.channel.send("```py\nHere are the latest details on the Federal Reserve's SOMA Holdings:``` https://markets.newyorkfed.org/api/soma/summary.csv")

    if "lending?" in message.content:
        await message.channel.send("```py\nHere are the latest operations data for the last two weeks of securities lending operations:``` https://markets.newyorkfed.org/api/seclending/all/results/details/lastTwoWeeks.csv")

    if "earnings per share?" in message.content:
        await message.channel.send( 
            "```py\nEarnings per share (EPS) refers to the net profit earned by a company during one period divided by the number of outstanding common shares. It tells us the amount shareholders will receive per share if the company distributes all its profits earned in one period. It is an important indicator of a company's profitability."

            "\nSpecifically, there are two forms of EPS: basic and diluted. We won't elaborate on their calculation here, but their difference should be noticed."

            "```py\nBasic EPS: This only includes current outstanding common shares.```"
            "```py\nDiluted EPS: Assuming all potentially dilutive financial instruments (e.g., stock options, convertible bonds, etc.) are converted into common shares, there would be more common shares outstanding than before.```"
            "\nTherefore, the diluted EPS is equal to or less than basic EPS.")
        
    if "market cap?" in message.content:
        await message.channel.send( 
            "```py\nSimply put, market capitalization refers to the market value of a company. It is calculated by multiplying the current stock price of the company by the number of total outstanding shares:```"

            "```py\nMarket Capitalization = Stock Price×Shares Outstanding```"

            "```py\nFor example, company C has 100 million common shares outstanding, trading at $10 per share. Its market capitalization is $1 billion.```"
        )

    if "profit margin?" in message.content:
        await message.channel.send("```py\nWhen looking at an income statement from any listed company, you can usually find three types of profit: gross profit, operating profit, and net income. The three types of profit margins are calculated below, generally in percentage.```"

            "```py\n'Gross Margin' = Gross Profits/Revenues\n"
            "'Operating Margin' = Operating Profits/Revenues\n"
            "'Net Margin' = Net Income/Revenues```"
            "```py\nProfit margins measure a company's profitability, used in both horizontal and trend analysis. Now we can answer the question posed at the beginning of the article: which company is more profitable? Even though company A has a higher net income, its net margin is 10% (=1÷10), lower than company B's net margin of 25% (=0.5÷2). We can conclude that Company B is more profitable than A due to its higher net margin ratio.```")


    if "price multiples?" in message.content:
        
        view = disnake.ui.View()
        button = disnake.ui.Button(style=disnake.ButtonStyle.blurple,emoji=f"{emojis.pink1}", label="PE RATIO")
        button2 = disnake.ui.Button(style=disnake.ButtonStyle.blurple,emoji=f"{emojis.pink2}",label="PB RATIO")
        button3 = disnake.ui.Button(style=disnake.ButtonStyle.blurple,emoji=f"{emojis.pink3}", label="PS RATIO")
        button4 = disnake.ui.Button(style=disnake.ButtonStyle.blurple,emoji=f"{emojis.pink3}", label="P/CF RATIO")
        
        button.callback = lambda interaction:interaction.response.edit_message( 

    "```py\nThe P/E ratio measures the value of a company's stock price to its earnings per share.```"

    "```py\nP/E Ratio= Share Price/Earnings per Share```"

    "```py\nSuppose company ABC has a P/E ratio of 30. It indicates that investors are willing to pay 30 times company ABC's earnings to purchase one share.```"

    "```py\nWhen you buy stocks, you, in a sense, buy the rights to receive the firm's future earnings. Suppose stock A has higher current earnings than stock B. In that case, you are generally willing to pay a higher price to buy stock A, assuming the two companies' profitability stays the same.```"
            , view=view)

        button2.callback = lambda interaction: interaction.response.edit_message( 
            "```py\nThe Price/Book ratio (P/B) measures a company's stock price to its book value per share.```"
    "```py\nP/B Ratio = Share Price/Book Value per Share```"
        , view=view)

        button3.callback = lambda interaction: interaction.response.edit_message( 
    "```py\nThe Price/Sales ratio (P/S) measures a company's stock price to its sales per share.```"
    "```py\nP/S Ratio = Share Price/Sales per Share```"
        , view=view)

        button4.callback = lambda interaction: interaction.response.edit_message( 
            "```py\nThe Price/Cash Flow ratio (P/CF) measures a company's stock price to the cash flow per share, which includes free cash flow (FCF) and operating cash flow (OCF).```"
    "```py\nP/CF Ratio = Share Price/Free Cash Flow per Share```"


    "Or"
    "```py\nP/CF Ratio = Share Price/Operating Cash Flow per Share```"
            ,view=view)
        view.add_item(button)
        view.add_item(button2)
        view.add_item(button3)
        view.add_item(button4)
        await message.channel.send("```py\nLet's talk about four common price multiples. Select one by clicking a button:```", view=view)


    if "options?" in message.content:
        view = disnake.ui.View()
        select = disnake.ui.Select( 
            placeholder=f"Options Videos:",
            min_values=1,
            max_values=1,
            custom_id="vidvid!@4e",
            options = [ 
        
            disnake.SelectOption(emoji=f"{emojis.video}",label="Options Course - Options Introduction",value="https://youtu.be/7jcqknbX99c"),
            disnake.SelectOption(emoji=f"{emojis.video}",label="Options Course - Options Terminology",value="https://youtu.be/namg44EBFBs"),
            disnake.SelectOption(emoji=f"{emojis.video}",label="Options Course - Buying Calls",value="https://youtu.be/Bc5gpsa7Z1M"),
            disnake.SelectOption(emoji=f"{emojis.video}",label="Options Course - Buying Puts",value="https://youtu.be/jrYUzSibjzo"),
            disnake.SelectOption(emoji=f"{emojis.video}",label="Options Course - Exercising and Assignment 1",value="https://youtu.be/Dgc2fO4GlR8"),
            disnake.SelectOption(emoji=f"{emojis.video}",label="Options Course - Exercising and Assignment 2",value="https://youtu.be/e_W_5jd-2v4"),
            disnake.SelectOption(emoji=f"{emojis.video}",label="Options Course - Options Premium",value="https://youtu.be/22X3h_rwiEA"),
            disnake.SelectOption(emoji=f"{emojis.video}",label="Options Course - Risk v. Reward",value="https://youtu.be/p36Ovh8x89I"),
            disnake.SelectOption(emoji=f"{emojis.video}",label="Options Course - Calls and Put Specifics",value="https://youtu.be/NpSQdICvNBk"),])
        view.add_item(select)
        select.callback = lambda interaction: interaction.response.edit_message(f"{select.values[0]}",view=view)
        await message.channel.send(view=view, delete_after=45)






async def main():




    extensions = []
    cogs_directory = os.path.join(os.path.dirname(__file__), 'cogs')

    for filename in os.listdir(cogs_directory):
        if filename.endswith('.py'):
            extension_name = filename[:-3]  # Remove the .py extension
            extensions.append(f'cogs.{extension_name}')

    for extension in extensions:
       await bot.load_extension(f'bot.{extension}')

bot.run(YOUR_DISCORD_BOT_TOKEN)
