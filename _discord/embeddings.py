


from discord_webhook import DiscordEmbed, AsyncDiscordWebhook

from sdks.webull_sdk.webull_sdk import AsyncWebullSDK



from _discord.hooks.channel_webhooks import daybanana,weekbanana,hourbanana





webull = AsyncWebullSDK()
class Data:
    def __init__(self, symbol=None):
        self.symbol = symbol
        self.avePrice: float = None
        self.buyvol: float = None
        self.neutralvol: float = None
        self.sell_vol: float = None
        self.total_vol: float = None
        self.change_ratio: float = None
        self.vibration: float = None
        self.fifty_high: str = None
        self.fifty_low: str = None
        self.name: str = None
        self.open: str = None
        self.close: str = None
        self.high: str = None
        self.low: str = None
        self.next_earnings: str = None
        self.outstanding_shares: float = None
        self.total_shares: float = None
        self.volume: float = None
        self.average_10d_volume: float = None
        self.average_3m_volume: float = None
        self.ask = None
        self.bid = None
        self.bid_size: float = None
        self.ask_size: float = None
        self.snapshot_close = None
        self.snapshot_low = None
        self.snapshot_open = None
        self.snapshot_high = None
        self.today_change_percent = None
        self.today_change = None
        self.snapshot_volume = None
        self.prev_volume: float = None
        self.prev_vwap = None
        self.snapshot_vwap = None
        self.snapshot_exchange = None
        self.conditions: list = None
        self.snapshot_size: float = None
        self.snapshot_price = None
        self.minute_close = None
        self.minute_high = None
        self.minute_low = None
        self.minute_open = None
        self.minute_volume: float = None
        self.minute_accumulated_volume: float = None
        self.minute_vwap = None
        self.prev_close = None
        self.prev_high = None
        self.prev_low = None
        self.prev_open = None
        self.prev_volume: float = None
        self.last_exchange = None

        # Data Metrics Calculation
        self.spread = self.ask - self.bid
        self.bid_ask_size_ratio = self.bid_size / self.ask_size
        self.price_change = self.snapshot_close - self.prev_close
        self.price_range = self.snapshot_high - self.snapshot_low
        self.price_range_percent = (self.price_range / self.prev_close) * 100
        self.volume_change = self.snapshot_volume - self.prev_volume
        self.volume_ratio = self.snapshot_volume / self.prev_volume
        self.vwap_change = self.snapshot_vwap - self.prev_vwap

        
    async def volume_analysis(self, symbol):
        vol_analysis = await webull.get_webull_vol_analysis_data(symbol)
        
        self.avePrice = vol_analysis.avePrice
        self.buyvol = vol_analysis.buyVolume
        self.neutralvol = vol_analysis.nVolume
        self.sell_vol = vol_analysis.sellVolume
        self.total_vol = vol_analysis.totalVolume


        return self.avePrice, self.buyvol, self.neutralvol, self.sell_vol, self.total_vol
    

    async def webull_stock_data(self, symbol):
        stock_data = await webull.get_webull_stock_data(symbol)
        self.open = stock_data.web_stock_open
        self.low = stock_data.web_stock_low
        self.high = stock_data.web_stock_high
        self.close = stock_data.web_stock_close
        self.name = stock_data.web_name
        self.fifty_high = stock_data.fifty_high
        self.fifty_low = stock_data.fifty_low
        self.vibration = stock_data.web_vibrate_ratio
        self.change_ratio = stock_data.web_change_ratio
        self.next_earnings = stock_data.last_earnings
        self.outstanding_shares = stock_data.outstanding_shares
        self.total_shares = stock_data.total_shares
        self.volume = stock_data.web_stock_vol
        self.average_10d_volume = stock_data.avg_10d_vol
        self.average_3m_volume = stock_data.avg_vol3m




    async def create_snapshot_fields(self, webhook_url: AsyncDiscordWebhook, embed: DiscordEmbed=None):


        webhook_url.add_embed(embed)
        embed.add_embed_field(name=f"Volume Analysis:",value=f"> Buy: **{self.buyvol:,}**\n> Neut: **{self.neutralvol:,}**\n> Sell: **{self.sell_vol:,}**\n> Total: **{self.total_vol:,}**")
        embed.add_embed_field(name=f"Avg. Price:", value=f"> **${self.avePrice}**")
        embed.add_embed_field(name=f"Day Stats:", value=f"> Open: **${self.open}**\n> High: **${self.high}**\n> Last: **${self.close}**\n> Low: **${self.low}**\n> Change%: **{round(self.change_ratio*100,2)}%**")
        embed.add_embed_field(name=f"52week High / Low:",value=f"> High: **${self.fifty_high}**\n> Low: **${self.fifty_low}**")
        embed.add_embed_field(name=f"Next ER:", value=f"> **{self.next_earnings}**")
        embed.add_embed_field(name=f"Volume Snapshot:", value=f"> Avg: **{self.average_3m_volume:,}**\n> VS.\n> Current: **{self.total_vol:,}**")
        embed.add_embed_field(name=f"Spread:", value=f"> {self.spread}\n> Bid/ask Size Ratio: **{self.bid_ask_size_ratio}**")

        await webhook_url.execute()


    async def make_news_embed(self, webhook_url, image_url, title, description, name, icon_url, article_url, tickers, home_url, keywords, author):
        webhook = AsyncDiscordWebhook(webhook_url, content="YOUR CONTENT")
        embed = DiscordEmbed(title=title, description=f"```py\n{description}```", url=article_url)
        embed.add_embed_field(name="Relevant tickers:", value=f"```py\n{tickers}```", inline=False)
        embed.add_embed_field(name="News Keywords:", value=f"```py\n{keywords}```", inline=True)
        embed.add_embed_field(name="Publisher:", value=f"```py\n{name}```")
        embed.add_embed_field(name=f"Author:", value=f"> **{author}**")
        embed.set_image(image_url)
        embed.set_footer(text="Data provided by Polygon.io", icon_url=icon_url)
        embed.set_author(name=author)
        embed.set_timestamp()
        webhook.add_embed(embed)
        await webhook.execute()


    async def make_test_event_embed(self, webhook_url: AsyncDiscordWebhook, symbol):
        embed = DiscordEmbed(title=f"Market Analysis - {symbol}")
        embed.add_embed_field(name=f"> {self.name}")
        webhook_url.add_embed(embed)
        await webhook_url.execute()

    async def process_NYSE_American(self, webhook_url:AsyncDiscordWebhook, symbol):
        # Code for processing when stock exchange is "NYSE American, LLC"
        await self.make_test_event_embed(webhook_url)

    async def process_Nasdaq_OMX_BX(self, webhook_url, symbol):
        # Code for processing when stock exchange is "Nasdaq OMX BX, Inc."
        await self.make_test_event_embed(webhook_url)

    async def process_NYSE_National(self, webhook_url, symbol):
        # Code for processing when stock exchange is "NYSE National, Inc."
        await self.make_test_event_embed(webhook_url)

    async def process_FINRA_NYSE_TRF(self, webhook_url, symbol):
        # Code for processing when stock exchange is "FINRA NYSE TRF"
        await self.make_test_event_embed(webhook_url)

    async def process_FINRA_Nasdaq_TRF_Carteret(self, webhook_url, symbol):
        # Code for processing when stock exchange is "FINRA Nasdaq TRF Carteret"
        await self.make_test_event_embed(webhook_url)

    async def process_FINRA_Nasdaq_TRF_Chicago(self, webhook_url, symbol):
        # Code for processing when stock exchange is "FINRA Nasdaq TRF Chicago"
        await self.make_test_event_embed(webhook_url)

    async def process_FINRA_Alternative_Display_Facility(self, webhook_url, symbol):
        # Code for processing when stock exchange is "FINRA Alternative Display Facility"
        await self.make_test_event_embed(webhook_url)

    async def process_Unlisted_Trading_Privileges(self, webhook_url, symbol):
        # Code for processing when stock exchange is "Unlisted Trading Privileges"
        await self.make_test_event_embed(webhook_url)

    async def process_International_Securities_Exchange(self, webhook_url, symbol):
        # Code for processing when stock exchange is "International Securities Exchange, LLC - Stocks"
        await self.make_test_event_embed(webhook_url)

    async def process_Cboe_EDGA(self, webhook_url, symbol):
        # Code for processing when stock exchange is "Cboe EDGA"
        pass

    async def process_Cboe_EDGX(self, webhook_url, symbol):
        # Code for processing when stock exchange is "Cboe EDGX"
        await self.make_test_event_embed(webhook_url)

    async def process_NYSE_Chicago(self, webhook_url, symbol):
        # Code for processing when stock exchange is "NYSE Chicago, Inc."
        await self.make_test_event_embed(webhook_url)

    async def process_New_York_Stock_Exchange(self, webhook_url, symbol):
        # Code for processing when stock exchange is "New York Stock Exchange"
        await self.make_test_event_embed(webhook_url)

    async def process_NYSE_Arca(self, webhook_url, symbol):
        # Code for processing when stock exchange is "NYSE Arca, Inc."
        await self.make_test_event_embed(webhook_url)

    async def process_Nasdaq(self, webhook_url, symbol):
        # Code for processing when stock exchange is "Nasdaq"
        await self.make_test_event_embed(webhook_url)

    async def process_Consolidated_Tape_Association(self, webhook_url, symbol):
        # Code for processing when stock exchange is "Consolidated Tape Association"
        await self.make_test_event_embed(webhook_url)

    async def process_Long_Term_Stock_Exchange(self, webhook_url, symbol):
        # Code for processing when stock exchange is "Long-Term Stock Exchange"
        await self.make_test_event_embed(webhook_url)

    async def process_Investors_Exchange(self, webhook_url, symbol):
        # Code for processing when stock exchange is "Investors Exchange"
        await self.make_test_event_embed(webhook_url)

    async def process_Cboe_Stock_Exchange(self, webhook_url, symbol):
        # Code for processing when stock exchange is "Cboe Stock Exchange"
        await self.make_test_event_embed(webhook_url)

    async def process_Nasdaq_Philadelphia_Exchange(self, webhook_url, symbol):
        # Code for processing when stock exchange is "Nasdaq Philadelphia Exchange LLC"
        await self.make_test_event_embed(webhook_url)

    async def process_Cboe_BYX(self, webhook_url, symbol):
        # Code for processing when stock exchange is "Cboe BYX"
        await self.make_test_event_embed(webhook_url)

    async def process_Cboe_BZX(self, webhook_url, symbol):
        # Code for processing when stock exchange is "Cboe BZX"
        await self.make_test_event_embed(webhook_url)

    async def process_MIAX_Pearl(self, webhook_url, symbol):
        # Code for processing when stock exchange is "MIAX Pearl"
        await self.make_test_event_embed(webhook_url)

    async def process_Members_Exchange(self, webhook_url, symbol):
        # Code for processing when stock exchange is "Members Exchange"
        await self.make_test_event_embed(webhook_url)

    async def process_OTC_Equity_Security(self, webhook_url, symbol):
        # Code for processing when stock exchange is "OTC Equity Security"
        await self.make_test_event_embed(webhook_url)




async def send_weekbanana(symbol):
    stock_data = await webull.get_webull_stock_data(symbol)
    vol_anal = await webull.get_webull_vol_analysis_data(symbol)
    buy = float(vol_anal.buyVolume)
    sell = float(vol_anal.sellVolume)
    neut = float(vol_anal.nVolume)
    fiftyhigh = stock_data.fifty_high
    fiftylow = stock_data.fifty_low
    close = stock_data.web_stock_close
    high = stock_data.web_stock_high
    low = stock_data.web_stock_low
    open = stock_data.web_stock_open
    changeratio = round(float(stock_data.web_change_ratio)*100,2)
    vol = float(stock_data.web_stock_vol)
    vr = stock_data.web_vibrate_ratio
    weekbananahook = AsyncDiscordWebhook(weekbanana, content="<@375862240601047070>")
    weekbananaembed = DiscordEmbed(title=f"🍌", description=f"> 🍌 **RIPE BANANA WITH OVERSOLD RSI!** 🍌", color=f"FFFF00")
    weekbananaembed.add_embed_field(name=f'Ticker:', value=f"> **{symbol}**\n\n> Timeframe: **WEEK**")
    weekbananaembed.add_embed_field(name=f"Day Stats", value=f"> Open: **${open}**\n> High: **${high}**\n> Last: **${close}**\n> Low: **${low}**\n> Change: **{changeratio}%**")
    weekbananaembed.add_embed_field(name=f"Volume Analysis:", value=f"> Buy: **{buy:,}**\n> Neut: **{neut:,}**\n> Sell: **{sell:,}**\n> Total: **{vol:,}**")
    weekbananaembed.add_embed_field(name="Year High/Low:", value=f"> High: **${fiftyhigh}**\n> Low: **${fiftylow}**")
    weekbananaembed.add_embed_field(name=f"Vibration:", value=f"> **{vr}**")
    weekbananaembed.set_footer(text=f"{symbol} | Data provided by Polygon.io")
    weekbananaembed.set_timestamp()
    weekbananahook.add_embed(weekbananaembed)
    await weekbananahook.execute()


async def send_daybanana(symbol):
    stock_data = await webull.get_webull_stock_data(symbol)
    vol_anal = await webull.get_webull_vol_analysis_data(symbol)
    buy = float(vol_anal.buyVolume)
    sell = float(vol_anal.sellVolume)
    neut = float(vol_anal.nVolume)
    fiftyhigh = stock_data.fifty_high
    fiftylow = stock_data.fifty_low
    close = stock_data.web_stock_close
    high = stock_data.web_stock_high
    low = stock_data.web_stock_low
    open = stock_data.web_stock_open
    changeratio = round(float(stock_data.web_change_ratio)*100,2)
    vol = float(stock_data.web_stock_vol)
    vr = stock_data.web_vibrate_ratio
    daybananahook = AsyncDiscordWebhook(daybanana, content="<@375862240601047070>")
    daybananaembed = DiscordEmbed(title=f"🍌", description=f"> 🍌 **RIPE BANANA WITH OVERSOLD RSI!** 🍌", color=f"FFFF00")
    daybananaembed.add_embed_field(name=f'Ticker:', value=f"> **{symbol}**\n\n> Timeframe: **DAY**")
    daybananaembed.add_embed_field(name=f"Day Stats", value=f"> Open: **${open}**\n> High: **${high}**\n> Last: **${close}**\n> Low: **${low}**\n> Change: **{changeratio}%**")
    daybananaembed.add_embed_field(name=f"Volume Analysis:", value=f"> Buy: **{buy:,}**\n> Neut: **{neut:,}**\n> Sell: **{sell:,}**\n> Total: **{vol:,}**")
    daybananaembed.add_embed_field(name="Year High/Low:", value=f"> High: **${fiftyhigh}**\n> Low: **${fiftylow}**")
    daybananaembed.add_embed_field(name=f"Vibration:", value=f"> **{vr}**")
    daybananaembed.set_footer(text=f"{symbol} | Data provided by Polygon.io")
    daybananaembed.set_timestamp()
    daybananahook.add_embed(daybananaembed)
    await daybananahook.execute()


async def send_hourbanana(symbol):
    stock_data = await webull.get_webull_stock_data(symbol)
    vol_anal = await webull.get_webull_vol_analysis_data(symbol)
    buy = float(vol_anal.buyVolume)
    sell = float(vol_anal.sellVolume)
    neut = float(vol_anal.nVolume)
    fiftyhigh = stock_data.fifty_high
    fiftylow = stock_data.fifty_low
    close = stock_data.web_stock_close
    high = stock_data.web_stock_high
    low = stock_data.web_stock_low
    open = stock_data.web_stock_open
    changeratio = round(float(stock_data.web_change_ratio)*100,2)
    vol = float(stock_data.web_stock_vol)
    vr = stock_data.web_vibrate_ratio
    hourbananahook = AsyncDiscordWebhook(hourbanana, content="<@375862240601047070>")
    hourbananaembed = DiscordEmbed(title=f"🍌", description=f"> 🍌 **RIPE BANANA WITH OVERSOLD RSI!** 🍌", color=f"FFFF00")
    hourbananaembed.add_embed_field(name=f'Ticker:', value=f"> **{symbol}**\n\n> Timeframe: **HOUR**")
    hourbananaembed.add_embed_field(name=f"Day Stats", value=f"> Open: **${open}**\n> High: **${high}**\n> Last: **${close}**\n> Low: **${low}**\n> Change: **{changeratio}%**")
    hourbananaembed.add_embed_field(name=f"Volume Analysis:", value=f"> Buy: **{buy:,}**\n> Neut: **{neut:,}**\n> Sell: **{sell:,}**\n> Total: **{vol:,}**")
    hourbananaembed.add_embed_field(name="Year High/Low:", value=f"> High: **${fiftyhigh}**\n> Low: **${fiftylow}**")
    hourbananaembed.add_embed_field(name=f"Vibration:", value=f"> **{vr}**")
    hourbananaembed.set_footer(text=f"{symbol} | Data provided by Polygon.io")
    hourbananahook.add_embed(hourbananaembed)

    await hourbananahook.execute()
