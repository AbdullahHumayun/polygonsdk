import requests
import disnake
from disnake.ext import commands
import stocksera
from uiviews.cmslist import MasterCommand
from cfg import YOUR_STOCKSERA_KEY
client = stocksera.Client(api_key=YOUR_STOCKSERA_KEY)


class MarketMainView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(MarketMainDrop())


    @disnake.ui.button(style=disnake.ButtonStyle.green,label="Top Gainers - 1 Day",row=0)
    async def topgain1dbutton(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
        view = disnake.ui.View()
        view.add_item(Day1Gainer())
        back = disnake.ui.Button(label="🔙", style=disnake.ButtonStyle.red)
        view.add_item(back)
        back.callback = lambda interaction: interaction.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view)


    @disnake.ui.button(style=disnake.ButtonStyle.green,label="Top Gainers - 5 minute",row=0)
    async def topgain5mbutton(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
        view = disnake.ui.View()
        view.add_item(FiveMinuteGainer())
        back = disnake.ui.Button(label="🔙", style=disnake.ButtonStyle.red)
        view.add_item(back)
        back.callback = lambda interaction: interaction.response.edit_message(view=MarketMainView())

        await inter.response.edit_message(view=view)


    @disnake.ui.button(style=disnake.ButtonStyle.green,label="Top Gainers - Premarket",row=0)
    async def topgainprebutton(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
        view = disnake.ui.View()
        view.add_item(PremarketGainer())
        back = disnake.ui.Button(label="🔙", style=disnake.ButtonStyle.red)
        view.add_item(back)
        back.callback = lambda interaction: interaction.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view)


    @disnake.ui.button(style=disnake.ButtonStyle.green,label="Top Gainers - Afterhours",row=0)
    async def topgainafterbutton(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
        view = disnake.ui.View()
        view.add_item(AfterHoursGainer())
        back = disnake.ui.Button(label="🔙", style=disnake.ButtonStyle.red)
        view.add_item(back)
        back.callback = lambda interaction: interaction.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view)


    @disnake.ui.button(style=disnake.ButtonStyle.red,label="Top Losers - 1 Day",row=0)
    async def toplose1dbutton(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
        view = disnake.ui.View()
        view.add_item(Day1Loser())
        back = disnake.ui.Button(label="🔙", style=disnake.ButtonStyle.red)
        view.add_item(back)
        back.callback = lambda interaction: interaction.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view)


    @disnake.ui.button(style=disnake.ButtonStyle.red,label="Top Losers - 5 minute",row=1)
    async def toplose5mbutton(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
        view = disnake.ui.View()
        view.add_item(FiveMinuteLoser())
        back = disnake.ui.Button(label="🔙", style=disnake.ButtonStyle.red)
        view.add_item(back)
        back.callback = lambda interaction: interaction.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view)


    @disnake.ui.button(style=disnake.ButtonStyle.red,label="Top Losers - Premarket",row=1)
    async def toploseprebutton(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
        view = disnake.ui.View()
        view.add_item(PremarketLoser())
        back = disnake.ui.Button(label="🔙", style=disnake.ButtonStyle.red)
        view.add_item(back)
        back.callback = lambda interaction: interaction.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view)


    @disnake.ui.button(style=disnake.ButtonStyle.red,label="Top Losers - Afterhours",row=1)
    async def toploseafterbutton(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
        view = disnake.ui.View()
        view.add_item(AfterHoursLoser())
        back = disnake.ui.Button(label="🔙", style=disnake.ButtonStyle.red)
        view.add_item(back)
        back.callback = lambda interaction: interaction.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view)


    @disnake.ui.button(style=disnake.ButtonStyle.blurple,label="High FTDS with T+35",row=1)
    async def ftdsbutton(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
        view = disnake.ui.View()
        view.add_item(FTDStocksDropdown())
        back = disnake.ui.Button(label="🔙", style=disnake.ButtonStyle.red)
        view.add_item(back)
        back.callback = lambda interaction: interaction.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view)



    @disnake.ui.button(style=disnake.ButtonStyle.grey,label="High Short Interest",row=1)
    async def shortintbutton(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
        view = disnake.ui.View()
        view.add_item(ShortInt())

        back = disnake.ui.Button(label="🔙", style=disnake.ButtonStyle.red)
        view.add_item(back)
        back.callback = lambda interaction: interaction.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view)



    @disnake.ui.button(style=disnake.ButtonStyle.blurple,label="Top Bonds",row=2)
    async def topbondsbutton(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
        view = disnake.ui.View()
        view.add_item()
        back = disnake.ui.Button(label="🔙", style=disnake.ButtonStyle.red)
        view.add_item(back)
        back.callback = lambda interaction: interaction.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view)



    @disnake.ui.button(style=disnake.ButtonStyle.grey,label="Top Commodity ETFs",row=2)
    async def topcommodbutton(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
        view = disnake.ui.View()
        view.add_item(CommodityETF())
        back = disnake.ui.Button(label="🔙", style=disnake.ButtonStyle.red)
        view.add_item(back)
        back.callback = lambda interaction: interaction.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view)



    @disnake.ui.button(style=disnake.ButtonStyle.blurple,label="Forex",row=2)
    async def forexbutton(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
        view = disnake.ui.View()
        view.add_item(Forex())
        back = disnake.ui.Button(label="🔙", style=disnake.ButtonStyle.red)
        view.add_item(back)
        back.callback = lambda interaction: interaction.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view)



    @disnake.ui.button(style=disnake.ButtonStyle.grey,label="Top Volume",row=2)
    async def topvolbutton(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
        view = disnake.ui.View()
        view.add_item(TopVolume())
        back = disnake.ui.Button(label="🔙", style=disnake.ButtonStyle.red)
        view.add_item(back)
        back.callback = lambda interaction: interaction.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view)



    @disnake.ui.button(style=disnake.ButtonStyle.grey,label="Top Turnover",row=2)
    async def topturnbutton(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
        view = disnake.ui.View()
        view.add_item(TurnoverDrop())
        back = disnake.ui.Button(label="🔙", style=disnake.ButtonStyle.red)
        view.add_item(back)
        back.callback = lambda interaction: interaction.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view)


    @disnake.ui.button(style=disnake.ButtonStyle.grey,label="Top Open Interest Options",row=3)
    async def topoibutton(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
        view = disnake.ui.View()
        view.add_item(TopOiDrop())
        back = disnake.ui.Button(label="🔙", style=disnake.ButtonStyle.grey)
        view.add_item(back)
        back.callback = lambda interaction: interaction.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view)


    @disnake.ui.button(style=disnake.ButtonStyle.grey,label="Top Volume Options",row=3)
    async def topvoloptbutton(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
        view = disnake.ui.View()
        view.add_item(TopVolDrop())
        back = disnake.ui.Button(label="🔙", style=disnake.ButtonStyle.grey)
        view.add_item(back)
        back.callback = lambda interaction: interaction.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view)



    @disnake.ui.button(style=disnake.ButtonStyle.grey,label="Top Open Int. Increase",row=3)
    async def topoiupbutton(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
        view = disnake.ui.View()
        view.add_item(TopOIUp())
        back = disnake.ui.Button(label="🔙", style=disnake.ButtonStyle.grey)
        view.add_item(back)
        back.callback = lambda interaction: interaction.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view)



    @disnake.ui.button(style=disnake.ButtonStyle.grey,label="Top Open Int. Decrease",row=3)
    async def topoidownbutton(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
        view = disnake.ui.View()
        view.add_item(TopOIDown())
        back = disnake.ui.Button(label="🔙", style=disnake.ButtonStyle.grey)
        view.add_item(back)
        back.callback = lambda interaction: interaction.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view)



    @disnake.ui.button(style=disnake.ButtonStyle.grey,label="Top Imp. Vol Options",row=3)
    async def topimpvolbutton(self, button:disnake.ui.Button, inter: disnake.AppCmdInter):
        view = disnake.ui.View()
        view.add_item(TopOIUp())
        back = disnake.ui.Button(label="🔙", style=disnake.ButtonStyle.grey)
        view.add_item(back)
        back.callback = lambda interaction: interaction.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view)



class MarketMainDrop(disnake.ui.Select):
    def __init__(self):

        options = [ 
            disnake.SelectOption(label="Top 🩳 Shorts", description="View the stocks with the most short interest."),
            disnake.SelectOption(label="Top 🚚 FTDs", description="View the stocks with the most FTDs + their T35 dates."),
            disnake.SelectOption(label="Top 🟩 Gainers", description="View the top gainers for the day."),
            disnake.SelectOption(label="Top 🟥 Losers", description="View the top losers for the day."),
            disnake.SelectOption(label="Top 🏃‍♀️ Volume", description="View the stocks with the most volume for the day."),
            disnake.SelectOption(label="Top 🛞 Turnover", description="View the stocks with the most turnover for the day."),
            disnake.SelectOption(label="Top 📜 Bonds", description="View the top gaining bonds for the day."),


        ]

        super().__init__(
            placeholder="🇹 🇴 🇵 🪩 🇹 🇮 🇨 🇰 🇪 🇷 🇸",
            min_values=1,
            max_values=1,
            custom_id="mainmarketdrop",
            options=options
        )

    async def callback(self, interaction: disnake.MessageCommandInteraction):
        if self.values[0] == "Top 🩳 Shorts":
            await interaction.response.edit_message(view=ShortIntView())
        
        
        elif self.values[0] == "Top 🚚 FTDs":
            await interaction.response.edit_message(view=FTDStocks())

        elif self.values[0] == "Top 🟩 Gainers":
            await interaction.response.edit_message(view=TopGainersView())


        elif self.values[0] == "Top 🟥 Losers":
            await interaction.response.edit_message(view=TopLosersView())


        elif self.values[0] == "Top 🏃‍♀️ Volume":
            await interaction.response.edit_message(view=TopVolumeView())


        elif self.values[0] == "Top 🛞 Turnover":
            await interaction.response.edit_message(view=TopTurnView())



        elif self.values[0] == "Top 📜 Bonds":
            await interaction.response.edit_message(view=TopBondsView())



    @disnake.ui.button(label="♻️", style=disnake.ButtonStyle.blurple)
    async def tocommands(self, inter:disnake.AppCommandInter):
        await inter.response.edit_message(view=MasterCommand())


class Day1Gainer(disnake.ui.Select):
    def __init__(self):

        day1gainr = requests.get(url="https://quotes-gw.webullfintech.com/api/bgw/market/topGainers?regionId=6&rankType=1d&pageIndex=1&pageSize=24").json()
        day1gainrdata = day1gainr['data']

        day1gain1 = day1gainrdata[0]
        gaind1ticker1 = day1gain1['ticker']
        gaind1change1 = round(float(gaind1ticker1['changeRatio'])*100,ndigits=2)
        gain1dsym1 = gaind1ticker1['symbol']
        gain1d52low1 = gaind1ticker1['fiftyTwoWkLow']
        gain1d52high1 = gaind1ticker1['fiftyTwoWkHigh']
        gain1dprice1 = gaind1ticker1['close']
        gain1dvol1 = round(float(gaind1ticker1['volume'])*0.000001,ndigits=2)



        day1gain2 = day1gainrdata[1]
        gaind1ticker2 = day1gain2['ticker']
        gaind1change2 = round(float(gaind1ticker2['changeRatio'])*100,ndigits=2)
        gain1dsym2 = gaind1ticker2['symbol']
        gain1d52low2 = gaind1ticker2['fiftyTwoWkLow']
        gain1d52high2 = gaind1ticker2['fiftyTwoWkHigh']
        gain1dprice2 = gaind1ticker2['close']
        gain1dvol2 = round(float(gaind1ticker2['volume'])*0.000001,ndigits=2)



        day1gain3 = day1gainrdata[2]
        gaind1ticker3 = day1gain3['ticker']
        gaind1change3 = round(float(gaind1ticker3['changeRatio'])*100,ndigits=2)
        gain1dsym3 = gaind1ticker3['symbol']
        gain1d52low3 = gaind1ticker3['fiftyTwoWkLow']
        gain1d52high3 = gaind1ticker3['fiftyTwoWkHigh']
        gain1dprice3 = gaind1ticker3['close']
        gain1dvol3 = round(float(gaind1ticker3['volume'])*0.000001,ndigits=2)



        day1gain4 = day1gainrdata[3]
        gaind1ticker4 = day1gain4['ticker']
        gaind1change4 = round(float(gaind1ticker4['changeRatio'])*100,ndigits=2)
        gain1dsym4 = gaind1ticker4['symbol']
        gain1d52low4 = gaind1ticker4['fiftyTwoWkLow']
        gain1d52high4 = gaind1ticker4['fiftyTwoWkHigh']
        gain1dprice4 = gaind1ticker4['close']
        gain1dvol4 = round(float(gaind1ticker4['volume'])*0.000001,ndigits=2)

        day1gain5 = day1gainrdata[4]
        gaind1ticker5 = day1gain5['ticker']
        gaind1change5 = round(float(gaind1ticker5['changeRatio'])*100,ndigits=2)
        gain1dsym5 = gaind1ticker5['symbol']
        gain1d52low5 = gaind1ticker5['fiftyTwoWkLow']
        gain1d52high5 = gaind1ticker5['fiftyTwoWkHigh']
        gain1dprice5 = gaind1ticker5['close']
        gain1dvol5 = round(float(gaind1ticker5['volume'])*0.000001,ndigits=2)


        day1gain6 = day1gainrdata[5]
        gaind1ticker6 = day1gain6['ticker']
        gaind1change6 = round(float(gaind1ticker6['changeRatio'])*100,ndigits=2)
        gain1dsym6 = gaind1ticker6['symbol']
        gain1d52low6 = gaind1ticker6['fiftyTwoWkLow']
        gain1d52high6 = gaind1ticker6['fiftyTwoWkHigh']
        gain1dprice6 = gaind1ticker6['close']
        gain1dvol6 = round(float(gaind1ticker6['volume'])*0.000001,ndigits=2)


        day1gain7 = day1gainrdata[6]
        gaind1ticker7 = day1gain7['ticker']
        gaind1change7 = round(float(gaind1ticker7['changeRatio'])*100,ndigits=2)
        gain1dsym7 = gaind1ticker7['symbol']
        gain1d52low7 = gaind1ticker7['fiftyTwoWkLow']
        gain1d52high7 = gaind1ticker7['fiftyTwoWkHigh']
        gain1dprice7 = gaind1ticker7['close']
        gain1dvol7 = round(float(gaind1ticker7['volume'])*0.000001,ndigits=2)


        day1gain8 = day1gainrdata[7]
        gaind1ticker8 = day1gain8['ticker']
        gaind1change8 = round(float(gaind1ticker8['changeRatio'])*100,ndigits=2)
        gain1dsym8 = gaind1ticker8['symbol']
        gain1d52low8 = gaind1ticker8['fiftyTwoWkLow']
        gain1d52high8 = gaind1ticker8['fiftyTwoWkHigh']
        gain1dprice8 = gaind1ticker8['close']
        gain1dvol8 = round(float(gaind1ticker8['volume'])*0.000001,ndigits=2)


        day1gain9 = day1gainrdata[8]
        gaind1ticker9 = day1gain9['ticker']
        gaind1change9 = round(float(gaind1ticker9['changeRatio'])*100,ndigits=2)
        gain1dsym9 = gaind1ticker9['symbol']
        gain1d52low9 = gaind1ticker9['fiftyTwoWkLow']
        gain1d52high9 = gaind1ticker9['fiftyTwoWkHigh']
        gain1dprice9 = gaind1ticker9['close']
        gain1dvol9 = round(float(gaind1ticker9['volume'])*0.000001,ndigits=2)


        day1gain10 = day1gainrdata[9]
        gaind1ticker10 = day1gain10['ticker']
        gaind1change10 = round(float(gaind1ticker10['changeRatio'])*100,ndigits=2)
        gain1dsym10 = gaind1ticker10['symbol']
        gain1d52low10 = gaind1ticker10['fiftyTwoWkLow']
        gain1d52high10 = gaind1ticker10['fiftyTwoWkHigh']
        gain1dprice10 = gaind1ticker10['close']
        gain1dvol10 = round(float(gaind1ticker10['volume'])*0.000001,ndigits=2)


        day1gain11 = day1gainrdata[10]
        gaind1ticker11 = day1gain11['ticker']
        gaind1change11 = round(float(gaind1ticker11['changeRatio'])*100,ndigits=2)
        gain1dsym11 = gaind1ticker11['symbol']
        gain1d52low11 = gaind1ticker11['fiftyTwoWkLow']
        gain1d52high11 = gaind1ticker11['fiftyTwoWkHigh']
        gain1dprice11 = gaind1ticker11['close']
        gain1dvol11 = round(float(gaind1ticker11['volume'])*0.000001,ndigits=2)


        day1gain12 = day1gainrdata[11]
        gaind1ticker12 = day1gain12['ticker']
        gaind1change12 = round(float(gaind1ticker12['changeRatio'])*100,ndigits=2)
        gain1dsym12 = gaind1ticker12['symbol']
        gain1d52low12 = gaind1ticker12['fiftyTwoWkLow']
        gain1d52high12 = gaind1ticker12['fiftyTwoWkHigh']
        gain1dprice12 = gaind1ticker12['close']
        gain1dvol12 = round(float(gaind1ticker12['volume'])*0.000001,ndigits=2)


        day1gain13 = day1gainrdata[12]
        gaind1ticker13 = day1gain13['ticker']
        gaind1change13 = round(float(gaind1ticker13['changeRatio'])*100,ndigits=2)
        gain1dsym13 = gaind1ticker13['symbol']
        gain1d52low13 = gaind1ticker13['fiftyTwoWkLow']
        gain1d52high13 = gaind1ticker13['fiftyTwoWkHigh']
        gain1dprice13 = gaind1ticker13['close']
        gain1dvol13 = round(float(gaind1ticker13['volume'])*0.000001,ndigits=2)

        day1gain14 = day1gainrdata[13]
        gaind1ticker14 = day1gain14['ticker']
        gaind1change14 = round(float(gaind1ticker14['changeRatio'])*100,ndigits=2)
        gain1dsym14 = gaind1ticker14['symbol']
        gain1d52low14 = gaind1ticker14['fiftyTwoWkLow']
        gain1d52high14 = gaind1ticker14['fiftyTwoWkHigh']
        gain1dprice14 = gaind1ticker14['close']
        gain1dvol14 = round(float(gaind1ticker14['volume'])*0.000001,ndigits=2)

        day1gain15 = day1gainrdata[14]
        gaind1ticker15 = day1gain15['ticker']
        gaind1change15 = round(float(gaind1ticker15['changeRatio'])*100,ndigits=2)
        gain1dsym15 = gaind1ticker15['symbol']
        gain1d52low15 = gaind1ticker15['fiftyTwoWkLow']
        gain1d52high15 = gaind1ticker15['fiftyTwoWkHigh']
        gain1dprice15 = gaind1ticker15['close']
        gain1dvol15 = round(float(gaind1ticker15['volume'])*0.000001,ndigits=2)


        day1gain16 = day1gainrdata[15]
        gaind1ticker16 = day1gain16['ticker']
        gaind1change16 = round(float(gaind1ticker16['changeRatio'])*100,ndigits=2)
        gain1dsym16 = gaind1ticker16['symbol']
        gain1d52low16 = gaind1ticker16['fiftyTwoWkLow']
        gain1d52high16 = gaind1ticker16['fiftyTwoWkHigh']
        gain1dprice16 = gaind1ticker16['close']
        gain1dvol16 = round(float(gaind1ticker16['volume'])*0.000001,ndigits=2)


        day1gain17 = day1gainrdata[16]
        gaind1ticker17 = day1gain17['ticker']
        gaind1change17 = round(float(gaind1ticker17['changeRatio'])*100,ndigits=2)
        gain1dsym17 = gaind1ticker17['symbol']
        gain1d52low17 = gaind1ticker17['fiftyTwoWkLow']
        gain1d52high17 = gaind1ticker17['fiftyTwoWkHigh']
        gain1dprice17 = gaind1ticker17['close']
        gain1dvol17 = round(float(gaind1ticker17['volume'])*0.000001,ndigits=2)


        day1gain18 = day1gainrdata[17]
        gaind1ticker18 = day1gain18['ticker']
        gaind1change18 = round(float(gaind1ticker18['changeRatio'])*100,ndigits=2)
        gain1dsym18 = gaind1ticker18['symbol']
        gain1d52low18 = gaind1ticker18['fiftyTwoWkLow']
        gain1d52high18 = gaind1ticker18['fiftyTwoWkHigh']
        gain1dprice18 = gaind1ticker18['close']
        gain1dvol18 = round(float(gaind1ticker18['volume'])*0.000001,ndigits=2)


        day1gain19 = day1gainrdata[18]
        gaind1ticker19 = day1gain19['ticker']
        gaind1change19 = round(float(gaind1ticker19['changeRatio'])*100,ndigits=2)
        gain1dsym19 = gaind1ticker19['symbol']
        gain1dprice19 = gaind1ticker19['close']
        gain1d52low19 = gaind1ticker19['fiftyTwoWkLow']
        gain1d52high19 = gaind1ticker19['fiftyTwoWkHigh']
        gain1dvol19 = round(float(gaind1ticker19['volume'])*0.000001,ndigits=2)


        day1gain20 = day1gainrdata[19]
        gaind1ticker20 = day1gain20['ticker']
        gaind1change20 = round(float(gaind1ticker20['changeRatio'])*100,ndigits=2)
        gain1dsym20 = gaind1ticker20['symbol']
        gain1dprice20 = gaind1ticker20['close']
        gain1d52low20 = gaind1ticker20['fiftyTwoWkLow']
        gain1d52high20 = gaind1ticker20['fiftyTwoWkHigh']
        gain1dvol20 = round(float(gaind1ticker20['volume'])*0.000001,ndigits=2)


        day1gain21 = day1gainrdata[20]
        gaind1ticker21 = day1gain21['ticker']
        gaind1change21 = round(float(gaind1ticker21['changeRatio'])*100,ndigits=2)
        gain1dsym21 = gaind1ticker21['symbol']
        gain1d52low21 = gaind1ticker21['fiftyTwoWkLow']
        gain1d52high21 = gaind1ticker21['fiftyTwoWkHigh']
        gain1dprice21 = gaind1ticker21['close']
        gain1dvol21 = round(float(gaind1ticker21['volume'])*0.000001,ndigits=2)


        day1gain22 = day1gainrdata[21]
        gaind1ticker22 = day1gain22['ticker']
        gaind1change22 = round(float(gaind1ticker22['changeRatio'])*100,ndigits=2)
        gain1dsym22 = gaind1ticker22['symbol']
        gain1d52low22 = gaind1ticker22['fiftyTwoWkLow']
        gain1dprice22= gaind1ticker22['close']
        gain1d52high22 = gaind1ticker22['fiftyTwoWkHigh']
        gain1dvol22 = round(float(gaind1ticker22['volume'])*0.000001,ndigits=2)


        day1gain23 = day1gainrdata[22]
        gaind1ticker23 = day1gain23['ticker']
        gaind1change23 = round(float(gaind1ticker23['changeRatio'])*100,ndigits=2)
        gain1dsym23 = gaind1ticker23['symbol']
        gain1d52low23 = gaind1ticker23['fiftyTwoWkLow']
        gain1d52high23 = gaind1ticker23['fiftyTwoWkHigh']
        gain1dprice23 = gaind1ticker23['close']
        gain1dvol23 = round(float(gaind1ticker23['volume'])*0.000001,ndigits=2)


        day1gain24 = day1gainrdata[23]
        gaind1ticker24 = day1gain24['ticker']
        gaind1change24 = round(float(gaind1ticker24['changeRatio'])*100,ndigits=2)
        gain1dsym24 = gaind1ticker24['symbol']
        gain1d52low24 = gaind1ticker24['fiftyTwoWkLow']
        gain1d52high24 = gaind1ticker24['fiftyTwoWkHigh']
        gain1dprice24 = gaind1ticker24['close']
        gain1dvol24 = round(float(gaind1ticker24['volume'])*0.000001,ndigits=2)



        super().__init__(
            placeholder="🇬 🇦 🇮 🇳 🇪 🇷 🇸  - 1️⃣ 🇩 🇦 🇾",
           min_values=1,
           max_values=1,
            custom_id="gain1dsel",
            options=[ 
                disnake.SelectOption(label=f"1️⃣{gain1dsym1} ${gain1dprice1}", description=f"Vol:{gain1dvol1}m 52 low:{gain1d52low1} 52 high:{gain1d52high1}"),
                disnake.SelectOption(label=f"2️⃣{gain1dsym2} ${gain1dprice2}", description=f"Vol:{gain1dvol2}m 52 low:{gain1d52low2} 52 high:{gain1d52high2}"),
                disnake.SelectOption(label=f"3️⃣{gain1dsym3} ${gain1dprice3}", description=f"Vol:{gain1dvol3}m 52 low:{gain1d52low3} 52 high:{gain1d52high3}"),
                disnake.SelectOption(label=f"4️⃣{gain1dsym4} ${gain1dprice4}", description=f"Vol:{gain1dvol4}m 52 low:{gain1d52low4} 52 high:{gain1d52high4}"),
                disnake.SelectOption(label=f"5️⃣{gain1dsym5} ${gain1dprice5}", description=f"Vol:{gain1dvol5}m 52 low:{gain1d52low5} 52 high:{gain1d52high5}"),
                disnake.SelectOption(label=f"6️⃣{gain1dsym6} ${gain1dprice6}", description=f"Vol:{gain1dvol6}m 52 low:{gain1d52low6} 52 high:{gain1d52high6}"),
                disnake.SelectOption(label=f"7️⃣{gain1dsym7} ${gain1dprice7}", description=f"Vol:{gain1dvol7}m 52 low:{gain1d52low7} 52 high:{gain1d52high7}"),
                disnake.SelectOption(label=f"8️⃣{gain1dsym8} ${gain1dprice8}", description=f"Vol:{gain1dvol8}m 52 low:{gain1d52low8} 52 high:{gain1d52high8}"),
                disnake.SelectOption(label=f"9️⃣{gain1dsym9} ${gain1dprice9}", description=f"Vol:{gain1dvol9}m 52 low:{gain1d52low9} 52 high:{gain1d52high9}"),
                disnake.SelectOption(label=f"🔟{gain1dsym10} ${gain1dprice10}", description=f"Vol:{gain1dvol10}m 52 low:{gain1d52low10} 52 high:{gain1d52high10}"),
                disnake.SelectOption(label=f"1️⃣1️⃣{gain1dsym11} ${gain1dprice11}", description=f"Vol:{gain1dvol11}m 52 low:{gain1d52low11} 52 high:{gain1d52high11}"),
                disnake.SelectOption(label=f"1️⃣2️⃣{gain1dsym12} ${gain1dprice12}", description=f"Vol:{gain1dvol12}m 52 low:{gain1d52low12} 52 high:{gain1d52high12}"),
                disnake.SelectOption(label=f"1️⃣3️⃣{gain1dsym13} ${gain1dprice13}", description=f"Vol:{gain1dvol13}m 52 low:{gain1d52low13} 52 high:{gain1d52high13}"),
                disnake.SelectOption(label=f"1️⃣4️⃣{gain1dsym14} ${gain1dprice14}", description=f"Vol:{gain1dvol14}m 52 low:{gain1d52low14} 52 high:{gain1d52high14}"),
                disnake.SelectOption(label=f"1️⃣5️⃣{gain1dsym15} ${gain1dprice15}", description=f"Vol:{gain1dvol15}m 52 low:{gain1d52low15} 52 high:{gain1d52high15}"),
                disnake.SelectOption(label=f"1️⃣6️⃣{gain1dsym16} ${gain1dprice16}", description=f"Vol:{gain1dvol16}m 52 low:{gain1d52low16} 52 high:{gain1d52high16}"),
                disnake.SelectOption(label=f"1️⃣7️⃣{gain1dsym17} ${gain1dprice17}", description=f"Vol:{gain1dvol17}m 52 low:{gain1d52low17} 52 high:{gain1d52high17}"),
                disnake.SelectOption(label=f"1️⃣8️⃣{gain1dsym18} ${gain1dprice18}", description=f"Vol:{gain1dvol18}m 52 low:{gain1d52low18} 52 high:{gain1d52high18}"),
                disnake.SelectOption(label=f"1️⃣9️⃣{gain1dsym19} ${gain1dprice19}", description=f"Vol:{gain1dvol19}m 52 low:{gain1d52low19} 52 high:{gain1d52high19}"),
                disnake.SelectOption(label=f"2️⃣0️⃣{gain1dsym20} ${gain1dprice20}", description=f"Vol:{gain1dvol20}m 52 low:{gain1d52low20} 52 high:{gain1d52high20}"),
                disnake.SelectOption(label=f"2️⃣1️⃣{gain1dsym21} ${gain1dprice21}", description=f"Vol:{gain1dvol21}m 52 low:{gain1d52low21} 52 high:{gain1d52high21}"),
                disnake.SelectOption(label=f"2️⃣2️⃣{gain1dsym22} ${gain1dprice22}", description=f"Vol:{gain1dvol22}m 52 low:{gain1d52low22} 52 high:{gain1d52high22}"),
                disnake.SelectOption(label=f"2️⃣3️⃣{gain1dsym23} ${gain1dprice23}", description=f"Vol:{gain1dvol23}m 52 low:{gain1d52low23} 52 high:{gain1d52high23}"),
                disnake.SelectOption(label=f"2️⃣4️⃣{gain1dsym24} ${gain1dprice24}", description=f"Vol:{gain1dvol24}m 52 low:{gain1d52low24} 52 high:{gain1d52high24}"),



            ]
        )

    async def callback(self, interaction:disnake.ApplicationCommandInteraction):
        if self.values[0] == self.values[0]:
            await interaction.send("```py\nSoon dad ormom, soon! For now - quick display for reference~!``")


class FiveMinuteGainer(disnake.ui.Select):
    def __init__(self):

        fivemingainr = requests.get(url="https://quotes-gw.webullfintech.com/api/bgw/market/topGainers?regionId=6&rankType=5min&pageIndex=1&pageSize=50").json()
        fivemingainrdata = fivemingainr['data']

        fivemingain1 = fivemingainrdata[0]
        gain5minticker1 = fivemingain1['ticker']
        gain5minchange1 = round(float(gain5minticker1['changeRatio'])*100,ndigits=2)
        gain5minsym1 = gain5minticker1['symbol']
        gain5min52low1 = gain5minticker1['fiftyTwoWkLow']
        gain5min52high1 = gain5minticker1['fiftyTwoWkHigh']
        gain5minprice1 = gain5minticker1['close']
        gain5minvol1 = round(float(gain5minticker1['volume'])*0.000001,ndigits=2)



        fivemingain2 = fivemingainrdata[1]
        gain5minticker2 = fivemingain2['ticker']
        gain5minchange2 = round(float(gain5minticker2['changeRatio'])*100,ndigits=2)
        gain5minsym2 = gain5minticker2['symbol']
        gain5min52low2 = gain5minticker2['fiftyTwoWkLow']
        gain5min52high2 = gain5minticker2['fiftyTwoWkHigh']
        gain5minprice2 = gain5minticker2['close']
        gain5minvol2 = round(float(gain5minticker2['volume'])*0.000001,ndigits=2)



        fivemingain3 = fivemingainrdata[2]
        gain5minticker3 = fivemingain3['ticker']
        gain5minchange3 = round(float(gain5minticker3['changeRatio'])*100,ndigits=2)
        gain5minsym3 = gain5minticker3['symbol']
        gain5min52low3 = gain5minticker3['fiftyTwoWkLow']
        gain5min52high3 = gain5minticker3['fiftyTwoWkHigh']
        gain5minprice3 = gain5minticker3['close']
        gain5minvol3 = round(float(gain5minticker3['volume'])*0.000001,ndigits=2)



        fivemingain4 = fivemingainrdata[3]
        gain5minticker4 = fivemingain4['ticker']
        gain5minchange4 = round(float(gain5minticker4['changeRatio'])*100,ndigits=2)
        gain5minsym4 = gain5minticker4['symbol']
        gain5min52low4 = gain5minticker4['fiftyTwoWkLow']
        gain5min52high4 = gain5minticker4['fiftyTwoWkHigh']
        gain5minprice4 = gain5minticker4['close']
        gain5minvol4 = round(float(gain5minticker4['volume'])*0.000001,ndigits=2)

        fivemingain5 = fivemingainrdata[4]
        gain5minticker5 = fivemingain5['ticker']
        gain5minchange5 = round(float(gain5minticker5['changeRatio'])*100,ndigits=2)
        gain5minsym5 = gain5minticker5['symbol']
        gain5min52low5 = gain5minticker5['fiftyTwoWkLow']
        gain5min52high5 = gain5minticker5['fiftyTwoWkHigh']
        gain5minprice5 = gain5minticker5['close']
        gain5minvol5 = round(float(gain5minticker5['volume'])*0.000001,ndigits=2)


        fivemingain6 = fivemingainrdata[5]
        gain5minticker6 = fivemingain6['ticker']
        gain5minchange6 = round(float(gain5minticker6['changeRatio'])*100,ndigits=2)
        gain5minsym6 = gain5minticker6['symbol']
        gain5min52low6 = gain5minticker6['fiftyTwoWkLow']
        gain5min52high6 = gain5minticker6['fiftyTwoWkHigh']
        gain5minprice6 = gain5minticker6['close']
        gain5minvol6 = round(float(gain5minticker6['volume'])*0.000001,ndigits=2)


        fivemingain7 = fivemingainrdata[6]
        gain5minticker7 = fivemingain7['ticker']
        gain5minchange7 = round(float(gain5minticker7['changeRatio'])*100,ndigits=2)
        gain5minsym7 = gain5minticker7['symbol']
        gain5min52low7 = gain5minticker7['fiftyTwoWkLow']
        gain5min52high7 = gain5minticker7['fiftyTwoWkHigh']
        gain5minprice7 = gain5minticker7['close']
        gain5minvol7 = round(float(gain5minticker7['volume'])*0.000001,ndigits=2)


        fivemingain8 = fivemingainrdata[7]
        gain5minticker8 = fivemingain8['ticker']
        gain5minchange8 = round(float(gain5minticker8['changeRatio'])*100,ndigits=2)
        gain5minsym8 = gain5minticker8['symbol']
        gain5min52low8 = gain5minticker8['fiftyTwoWkLow']
        gain5min52high8 = gain5minticker8['fiftyTwoWkHigh']
        gain5minprice8 = gain5minticker8['close']
        gain5minvol8 = round(float(gain5minticker8['volume'])*0.000001,ndigits=2)


        fivemingain9 = fivemingainrdata[8]
        gain5minticker9 = fivemingain9['ticker']
        gain5minchange9 = round(float(gain5minticker9['changeRatio'])*100,ndigits=2)
        gain5minsym9 = gain5minticker9['symbol']
        gain5min52low9 = gain5minticker9['fiftyTwoWkLow']
        gain5min52high9 = gain5minticker9['fiftyTwoWkHigh']
        gain5minprice9 = gain5minticker9['close']
        gain5minvol9 = round(float(gain5minticker9['volume'])*0.000001,ndigits=2)


        fivemingain10 = fivemingainrdata[9]
        gain5minticker10 = fivemingain10['ticker']
        gain5minchange10 = round(float(gain5minticker10['changeRatio'])*100,ndigits=2)
        gain5minsym10 = gain5minticker10['symbol']
        gain5min52low10 = gain5minticker10['fiftyTwoWkLow']
        gain5min52high10 = gain5minticker10['fiftyTwoWkHigh']
        gain5minprice10 = gain5minticker10['close']
        gain5minvol10 = round(float(gain5minticker10['volume'])*0.000001,ndigits=2)


        fivemingain11 = fivemingainrdata[10]
        gain5minticker11 = fivemingain11['ticker']
        gain5minchange11 = round(float(gain5minticker11['changeRatio'])*100,ndigits=2)
        gain5minsym11 = gain5minticker11['symbol']
        gain5min52low11 = gain5minticker11['fiftyTwoWkLow']
        gain5min52high11 = gain5minticker11['fiftyTwoWkHigh']
        gain5minprice11 = gain5minticker11['close']
        gain5minvol11 = round(float(gain5minticker11['volume'])*0.000001,ndigits=2)


        fivemingain12 = fivemingainrdata[11]
        gain5minticker12 = fivemingain12['ticker']
        gain5minchange12 = round(float(gain5minticker12['changeRatio'])*100,ndigits=2)
        gain5minsym12 = gain5minticker12['symbol']
        gain5min52low12 = gain5minticker12['fiftyTwoWkLow']
        gain5min52high12 = gain5minticker12['fiftyTwoWkHigh']
        gain5minprice12 = gain5minticker12['close']
        gain5minvol12 = round(float(gain5minticker12['volume'])*0.000001,ndigits=2)


        fivemingain13 = fivemingainrdata[12]
        gain5minticker13 = fivemingain13['ticker']
        gain5minchange13 = round(float(gain5minticker13['changeRatio'])*100,ndigits=2)
        gain5minsym13 = gain5minticker13['symbol']
        gain5min52low13 = gain5minticker13['fiftyTwoWkLow']
        gain5min52high13 = gain5minticker13['fiftyTwoWkHigh']
        gain5minprice13 = gain5minticker13['close']
        gain5minvol13 = round(float(gain5minticker13['volume'])*0.000001,ndigits=2)

        fivemingain14 = fivemingainrdata[13]
        gain5minticker14 = fivemingain14['ticker']
        gain5minchange14 = round(float(gain5minticker14['changeRatio'])*100,ndigits=2)
        gain5minsym14 = gain5minticker14['symbol']
        gain5min52low14 = gain5minticker14['fiftyTwoWkLow']
        gain5min52high14 = gain5minticker14['fiftyTwoWkHigh']
        gain5minprice14 = gain5minticker14['close']
        gain5minvol14 = round(float(gain5minticker14['volume'])*0.000001,ndigits=2)

        fivemingain15 = fivemingainrdata[14]
        gain5minticker15 = fivemingain15['ticker']
        gain5minchange15 = round(float(gain5minticker15['changeRatio'])*100,ndigits=2)
        gain5minsym15 = gain5minticker15['symbol']
        gain5min52low15 = gain5minticker15['fiftyTwoWkLow']
        gain5min52high15 = gain5minticker15['fiftyTwoWkHigh']
        gain5minprice15 = gain5minticker15['close']
        gain5minvol15 = round(float(gain5minticker15['volume'])*0.000001,ndigits=2)


        fivemingain16 = fivemingainrdata[15]
        gain5minticker16 = fivemingain16['ticker']
        gain5minchange16 = round(float(gain5minticker16['changeRatio'])*100,ndigits=2)
        gain5minsym16 = gain5minticker16['symbol']
        gain5min52low16 = gain5minticker16['fiftyTwoWkLow']
        gain5min52high16 = gain5minticker16['fiftyTwoWkHigh']
        gain5minprice16 = gain5minticker16['close']
        gain5minvol16 = round(float(gain5minticker16['volume'])*0.000001,ndigits=2)


        fivemingain17 = fivemingainrdata[16]
        gain5minticker17 = fivemingain17['ticker']
        gain5minchange17 = round(float(gain5minticker17['changeRatio'])*100,ndigits=2)
        gain5minsym17 = gain5minticker17['symbol']
        gain5min52low17 = gain5minticker17['fiftyTwoWkLow']
        gain5min52high17 = gain5minticker17['fiftyTwoWkHigh']
        gain5minprice17 = gain5minticker17['close']
        gain5minvol17 = round(float(gain5minticker17['volume'])*0.000001,ndigits=2)


        fivemingain18 = fivemingainrdata[17]
        gain5minticker18 = fivemingain18['ticker']
        gain5minchange18 = round(float(gain5minticker18['changeRatio'])*100,ndigits=2)
        gain5minsym18 = gain5minticker18['symbol']
        gain5min52low18 = gain5minticker18['fiftyTwoWkLow']
        gain5min52high18 = gain5minticker18['fiftyTwoWkHigh']
        gain5minprice18 = gain5minticker18['close']
        gain5minvol18 = round(float(gain5minticker18['volume'])*0.000001,ndigits=2)


        fivemingain19 = fivemingainrdata[18]
        gain5minticker19 = fivemingain19['ticker']
        gain5minchange19 = round(float(gain5minticker19['changeRatio'])*100,ndigits=2)
        gain5minsym19 = gain5minticker19['symbol']
        gain5minprice19 = gain5minticker19['close']
        gain5min52low19 = gain5minticker19['fiftyTwoWkLow']
        gain5min52high19 = gain5minticker19['fiftyTwoWkHigh']
        gain5minvol19 = round(float(gain5minticker19['volume'])*0.000001,ndigits=2)


        fivemingain20 = fivemingainrdata[19]
        gain5minticker20 = fivemingain20['ticker']
        gain5minchange20 = round(float(gain5minticker20['changeRatio'])*100,ndigits=2)
        gain5minsym20 = gain5minticker20['symbol']
        gain5minprice20 = gain5minticker20['close']
        gain5min52low20 = gain5minticker20['fiftyTwoWkLow']
        gain5min52high20 = gain5minticker20['fiftyTwoWkHigh']
        gain5minvol20 = round(float(gain5minticker20['volume'])*0.000001,ndigits=2)


        fivemingain21 = fivemingainrdata[20]
        gain5minticker21 = fivemingain21['ticker']
        gain5minchange21 = round(float(gain5minticker21['changeRatio'])*100,ndigits=2)
        gain5minsym21 = gain5minticker21['symbol']
        gain5min52low21 = gain5minticker21['fiftyTwoWkLow']
        gain5min52high21 = gain5minticker21['fiftyTwoWkHigh']
        gain5minprice21 = gain5minticker21['close']
        gain5minvol21 = round(float(gain5minticker21['volume'])*0.000001,ndigits=2)


        fivemingain22 = fivemingainrdata[21]
        gain5minticker22 = fivemingain22['ticker']
        gain5minchange22 = round(float(gain5minticker22['changeRatio'])*100,ndigits=2)
        gain5minsym22 = gain5minticker22['symbol']
        gain5min52low22 = gain5minticker22['fiftyTwoWkLow']
        gain5minprice22= gain5minticker22['close']
        gain5min52high22 = gain5minticker22['fiftyTwoWkHigh']
        gain5minvol22 = round(float(gain5minticker22['volume'])*0.000001,ndigits=2)


        fivemingain23 = fivemingainrdata[22]
        gain5minticker23 = fivemingain23['ticker']
        gain5minchange23 = round(float(gain5minticker23['changeRatio'])*100,ndigits=2)
        gain5minsym23 = gain5minticker23['symbol']
        gain5min52low23 = gain5minticker23['fiftyTwoWkLow']
        gain5min52high23 = gain5minticker23['fiftyTwoWkHigh']
        gain5minprice23 = gain5minticker23['close']
        gain5minvol23 = round(float(gain5minticker23['volume'])*0.000001,ndigits=2)


        fivemingain24 = fivemingainrdata[23]
        gain5minticker24 = fivemingain24['ticker']
        gain5minchange24 = round(float(gain5minticker24['changeRatio'])*100,ndigits=2)
        gain5minsym24 = gain5minticker24['symbol']
        gain5min52low24 = gain5minticker24['fiftyTwoWkLow']
        gain5min52high24 = gain5minticker24['fiftyTwoWkHigh']
        gain5minprice24 = gain5minticker24['close']
        gain5minvol24 = round(float(gain5minticker24['volume'])*0.000001,ndigits=2)



        super().__init__(
            placeholder="🇬 🇦 🇮 🇳 🇪 🇷 🇸  - 5️⃣ 🇲 🇮 🇳",
           min_values=1,
           max_values=1,
            custom_id="gain1dselsc",
            options=[ 
                disnake.SelectOption(label=f"1️⃣{gain5minsym1} ${gain5minprice1}", description=f"Vol:{gain5minvol1}m 52 low:{gain5min52low1} 52 high:{gain5min52high1}"),
                disnake.SelectOption(label=f"2️⃣{gain5minsym2} ${gain5minprice2}", description=f"Vol:{gain5minvol2}m 52 low:{gain5min52low2} 52 high:{gain5min52high2}"),
                disnake.SelectOption(label=f"3️⃣{gain5minsym3} ${gain5minprice3}", description=f"Vol:{gain5minvol3}m 52 low:{gain5min52low3} 52 high:{gain5min52high3}"),
                disnake.SelectOption(label=f"4️⃣{gain5minsym4} ${gain5minprice4}", description=f"Vol:{gain5minvol4}m 52 low:{gain5min52low4} 52 high:{gain5min52high4}"),
                disnake.SelectOption(label=f"5️⃣{gain5minsym5} ${gain5minprice5}", description=f"Vol:{gain5minvol5}m52 low:{gain5min52low5} 52 high:{gain5min52high5}"),
                disnake.SelectOption(label=f"6️⃣{gain5minsym6} ${gain5minprice6}", description=f"Vol:{gain5minvol6}m 52 low:{gain5min52low6} 52 high:{gain5min52high6}"),
                disnake.SelectOption(label=f"7️⃣{gain5minsym7} ${gain5minprice7}",description=f"Vol:{gain5minvol7}m 52 low:{gain5min52low7} 52 high:{gain5min52high7}"),
                disnake.SelectOption(label=f"8️⃣{gain5minsym8} ${gain5minprice8}",description=f"Vol:{gain5minvol8}m 52 low:{gain5min52low8} 52 high:{gain5min52high8}"),
                disnake.SelectOption(label=f"9️⃣{gain5minsym9} ${gain5minprice9}",description=f"Vol:{gain5minvol9}m 52 low:{gain5min52low9} 52 high:{gain5min52high9}"),
                disnake.SelectOption(label=f"🔟{gain5minsym10} ${gain5minprice10}",description=f"Vol:{gain5minvol10}m 52 low:{gain5min52low10} 52 high:{gain5min52high10}"),
                disnake.SelectOption(label=f"1️⃣1️⃣{gain5minsym11} ${gain5minprice11}",description=f"Vol:{gain5minvol11}m 52 low:{gain5min52low11} 52 high:{gain5min52high11}"),
                disnake.SelectOption(label=f"1️⃣2️⃣{gain5minsym12} ${gain5minprice12}",description=f"Vol:{gain5minvol12}m 52 low:{gain5min52low12} 52 high:{gain5min52high12}"),
                disnake.SelectOption(label=f"1️⃣3️⃣{gain5minsym13} ${gain5minprice13}",description=f"Vol:{gain5minvol13}m 52 low:{gain5min52low13} 52 high:{gain5min52high13}"),
                disnake.SelectOption(label=f"1️⃣4️⃣{gain5minsym14} ${gain5minprice14}",description=f"Vol:{gain5minvol14}m 52 low:{gain5min52low14} 52 high:{gain5min52high14}"),
                disnake.SelectOption(label=f"1️⃣5️⃣{gain5minsym15} ${gain5minprice15}", description=f"Vol:{gain5minvol15}m 52 low:{gain5min52low15} 52 high:{gain5min52high15}"),
                disnake.SelectOption(label=f"1️⃣6️⃣{gain5minsym16} ${gain5minprice16}", description=f"Vol:{gain5minvol16}m 52 low:{gain5min52low16} 52 high:{gain5min52high16}"),
                disnake.SelectOption(label=f"1️⃣7️⃣{gain5minsym17} ${gain5minprice17}", description=f"Vol:{gain5minvol17}m 52 low:{gain5min52low17} 52 high:{gain5min52high17}"),
                disnake.SelectOption(label=f"1️⃣8️⃣{gain5minsym18} ${gain5minprice18}", description=f"Vol:{gain5minvol18}m 52 low:{gain5min52low18} 52 high:{gain5min52high18}"),
                disnake.SelectOption(label=f"1️⃣9️⃣{gain5minsym19} ${gain5minprice19}", description=f"Vol:{gain5minvol19}m 52 low:{gain5min52low19} 52 high:{gain5min52high19}"),
                disnake.SelectOption(label=f"2️⃣0️⃣{gain5minsym20} ${gain5minprice20}", description=f"Vol:{gain5minvol20}m 52 low:{gain5min52low20} 52 high:{gain5min52high20}"),
                disnake.SelectOption(label=f"2️⃣1️⃣{gain5minsym21} ${gain5minprice21}", description=f"Vol:{gain5minvol21}m 52 low:{gain5min52low21} 52 high:{gain5min52high21}"),
                disnake.SelectOption(label=f"2️⃣2️⃣{gain5minsym22} ${gain5minprice22}", description=f"Vol:{gain5minvol22}m 52 low:{gain5min52low22} 52 high:{gain5min52high22}"),
                disnake.SelectOption(label=f"2️⃣3️⃣{gain5minsym23} ${gain5minprice23}", description=f"Vol:{gain5minvol23}m 52 low:{gain5min52low23} 52 high:{gain5min52high23}"),
                disnake.SelectOption(label=f"2️⃣4️⃣{gain5minsym24} ${gain5minprice24}", description=f"Vol:{gain5minvol24}m 52 low:{gain5min52low24} 52 high:{gain5min52high24}"),



            ]
        )

    async def callback(self, interaction:disnake.ApplicationCommandInteraction):
        if self.values[0] == self.values[0]:
            await interaction.send("```py\nSoon dad ormom, soon! For now - quick display for reference~!``")



class PremarketGainer(disnake.ui.Select):
    def __init__(self):

        pregainr = requests.get(url="https://quotes-gw.webullfintech.com/api/bgw/market/topGainers?regionId=6&rankType=preMarket&pageIndex=1&pageSize=50").json()
        pregainrdata = pregainr['data']

        pregain1 = pregainrdata[0]
        gainpreticker1 = pregain1['ticker']
        gainprechange1 = round(float(gainpreticker1['changeRatio'])*100,ndigits=2)
        gainpresym1 = gainpreticker1['symbol']
        gainpre52low1 = gainpreticker1['fiftyTwoWkLow']
        gainpre52high1 = gainpreticker1['fiftyTwoWkHigh']
        gainpreprice1 = gainpreticker1['close']
        gainprevol1 = round(float(gainpreticker1['volume'])*0.000001,ndigits=2)



        pregain2 = pregainrdata[1]
        gainpreticker2 = pregain2['ticker']
        gainprechange2 = round(float(gainpreticker2['changeRatio'])*100,ndigits=2)
        gainpresym2 = gainpreticker2['symbol']
        gainpre52low2 = gainpreticker2['fiftyTwoWkLow']
        gainpre52high2 = gainpreticker2['fiftyTwoWkHigh']
        gainpreprice2 = gainpreticker2['close']
        gainprevol2 = round(float(gainpreticker2['volume'])*0.000001,ndigits=2)



        pregain3 = pregainrdata[2]
        gainpreticker3 = pregain3['ticker']
        gainprechange3 = round(float(gainpreticker3['changeRatio'])*100,ndigits=2)
        gainpresym3 = gainpreticker3['symbol']
        gainpre52low3 = gainpreticker3['fiftyTwoWkLow']
        gainpre52high3 = gainpreticker3['fiftyTwoWkHigh']
        gainpreprice3 = gainpreticker3['close']
        gainprevol3 = round(float(gainpreticker3['volume'])*0.000001,ndigits=2)



        pregain4 = pregainrdata[3]
        gainpreticker4 = pregain4['ticker']
        gainprechange4 = round(float(gainpreticker4['changeRatio'])*100,ndigits=2)
        gainpresym4 = gainpreticker4['symbol']
        gainpre52low4 = gainpreticker4['fiftyTwoWkLow']
        gainpre52high4 = gainpreticker4['fiftyTwoWkHigh']
        gainpreprice4 = gainpreticker4['close']
        gainprevol4 = round(float(gainpreticker4['volume'])*0.000001,ndigits=2)

        pregain5 = pregainrdata[4]
        gainpreticker5 = pregain5['ticker']
        gainprechange5 = round(float(gainpreticker5['changeRatio'])*100,ndigits=2)
        gainpresym5 = gainpreticker5['symbol']
        gainpre52low5 = gainpreticker5['fiftyTwoWkLow']
        gainpre52high5 = gainpreticker5['fiftyTwoWkHigh']
        gainpreprice5 = gainpreticker5['close']
        gainprevol5 = round(float(gainpreticker5['volume'])*0.000001,ndigits=2)


        pregain6 = pregainrdata[5]
        gainpreticker6 = pregain6['ticker']
        gainprechange6 = round(float(gainpreticker6['changeRatio'])*100,ndigits=2)
        gainpresym6 = gainpreticker6['symbol']
        gainpre52low6 = gainpreticker6['fiftyTwoWkLow']
        gainpre52high6 = gainpreticker6['fiftyTwoWkHigh']
        gainpreprice6 = gainpreticker6['close']
        gainprevol6 = round(float(gainpreticker6['volume'])*0.000001,ndigits=2)


        pregain7 = pregainrdata[6]
        gainpreticker7 = pregain7['ticker']
        gainprechange7 = round(float(gainpreticker7['changeRatio'])*100,ndigits=2)
        gainpresym7 = gainpreticker7['symbol']
        gainpre52low7 = gainpreticker7['fiftyTwoWkLow']
        gainpre52high7 = gainpreticker7['fiftyTwoWkHigh']
        gainpreprice7 = gainpreticker7['close']
        gainprevol7 = round(float(gainpreticker7['volume'])*0.000001,ndigits=2)


        pregain8 = pregainrdata[7]
        gainpreticker8 = pregain8['ticker']
        gainprechange8 = round(float(gainpreticker8['changeRatio'])*100,ndigits=2)
        gainpresym8 = gainpreticker8['symbol']
        gainpre52low8 = gainpreticker8['fiftyTwoWkLow']
        gainpre52high8 = gainpreticker8['fiftyTwoWkHigh']
        gainpreprice8 = gainpreticker8['close']
        gainprevol8 = round(float(gainpreticker8['volume'])*0.000001,ndigits=2)


        pregain9 = pregainrdata[8]
        gainpreticker9 = pregain9['ticker']
        gainprechange9 = round(float(gainpreticker9['changeRatio'])*100,ndigits=2)
        gainpresym9 = gainpreticker9['symbol']
        gainpre52low9 = gainpreticker9['fiftyTwoWkLow']
        gainpre52high9 = gainpreticker9['fiftyTwoWkHigh']
        gainpreprice9 = gainpreticker9['close']
        gainprevol9 = round(float(gainpreticker9['volume'])*0.000001,ndigits=2)


        pregain10 = pregainrdata[9]
        gainpreticker10 = pregain10['ticker']
        gainprechange10 = round(float(gainpreticker10['changeRatio'])*100,ndigits=2)
        gainpresym10 = gainpreticker10['symbol']
        gainpre52low10 = gainpreticker10['fiftyTwoWkLow']
        gainpre52high10 = gainpreticker10['fiftyTwoWkHigh']
        gainpreprice10 = gainpreticker10['close']
        gainprevol10 = round(float(gainpreticker10['volume'])*0.000001,ndigits=2)


        pregain11 = pregainrdata[10]
        gainpreticker11 = pregain11['ticker']
        gainprechange11 = round(float(gainpreticker11['changeRatio'])*100,ndigits=2)
        gainpresym11 = gainpreticker11['symbol']
        gainpre52low11 = gainpreticker11['fiftyTwoWkLow']
        gainpre52high11 = gainpreticker11['fiftyTwoWkHigh']
        gainpreprice11 = gainpreticker11['close']
        gainprevol11 = round(float(gainpreticker11['volume'])*0.000001,ndigits=2)


        pregain12 = pregainrdata[11]
        gainpreticker12 = pregain12['ticker']
        gainprechange12 = round(float(gainpreticker12['changeRatio'])*100,ndigits=2)
        gainpresym12 = gainpreticker12['symbol']
        gainpre52low12 = gainpreticker12['fiftyTwoWkLow']
        gainpre52high12 = gainpreticker12['fiftyTwoWkHigh']
        gainpreprice12 = gainpreticker12['close']
        gainprevol12 = round(float(gainpreticker12['volume'])*0.000001,ndigits=2)


        pregain13 = pregainrdata[12]
        gainpreticker13 = pregain13['ticker']
        gainprechange13 = round(float(gainpreticker13['changeRatio'])*100,ndigits=2)
        gainpresym13 = gainpreticker13['symbol']
        gainpre52low13 = gainpreticker13['fiftyTwoWkLow']
        gainpre52high13 = gainpreticker13['fiftyTwoWkHigh']
        gainpreprice13 = gainpreticker13['close']
        gainprevol13 = round(float(gainpreticker13['volume'])*0.000001,ndigits=2)

        pregain14 = pregainrdata[13]
        gainpreticker14 = pregain14['ticker']
        gainprechange14 = round(float(gainpreticker14['changeRatio'])*100,ndigits=2)
        gainpresym14 = gainpreticker14['symbol']
        gainpre52low14 = gainpreticker14['fiftyTwoWkLow']
        gainpre52high14 = gainpreticker14['fiftyTwoWkHigh']
        gainpreprice14 = gainpreticker14['close']
        gainprevol14 = round(float(gainpreticker14['volume'])*0.000001,ndigits=2)

        pregain15 = pregainrdata[14]
        gainpreticker15 = pregain15['ticker']
        gainprechange15 = round(float(gainpreticker15['changeRatio'])*100,ndigits=2)
        gainpresym15 = gainpreticker15['symbol']
        gainpre52low15 = gainpreticker15['fiftyTwoWkLow']
        gainpre52high15 = gainpreticker15['fiftyTwoWkHigh']
        gainpreprice15 = gainpreticker15['close']
        gainprevol15 = round(float(gainpreticker15['volume'])*0.000001,ndigits=2)


        pregain16 = pregainrdata[15]
        gainpreticker16 = pregain16['ticker']
        gainprechange16 = round(float(gainpreticker16['changeRatio'])*100,ndigits=2)
        gainpresym16 = gainpreticker16['symbol']
        gainpre52low16 = gainpreticker16['fiftyTwoWkLow']
        gainpre52high16 = gainpreticker16['fiftyTwoWkHigh']
        gainpreprice16 = gainpreticker16['close']
        gainprevol16 = round(float(gainpreticker16['volume'])*0.000001,ndigits=2)


        pregain17 = pregainrdata[16]
        gainpreticker17 = pregain17['ticker']
        gainprechange17 = round(float(gainpreticker17['changeRatio'])*100,ndigits=2)
        gainpresym17 = gainpreticker17['symbol']
        gainpre52low17 = gainpreticker17['fiftyTwoWkLow']
        gainpre52high17 = gainpreticker17['fiftyTwoWkHigh']
        gainpreprice17 = gainpreticker17['close']
        gainprevol17 = round(float(gainpreticker17['volume'])*0.000001,ndigits=2)


        pregain18 = pregainrdata[17]
        gainpreticker18 = pregain18['ticker']
        gainprechange18 = round(float(gainpreticker18['changeRatio'])*100,ndigits=2)
        gainpresym18 = gainpreticker18['symbol']
        gainpre52low18 = gainpreticker18['fiftyTwoWkLow']
        gainpre52high18 = gainpreticker18['fiftyTwoWkHigh']
        gainpreprice18 = gainpreticker18['close']
        gainprevol18 = round(float(gainpreticker18['volume'])*0.000001,ndigits=2)


        pregain19 = pregainrdata[18]
        gainpreticker19 = pregain19['ticker']
        gainprechange19 = round(float(gainpreticker19['changeRatio'])*100,ndigits=2)
        gainpresym19 = gainpreticker19['symbol']
        gainpreprice19 = gainpreticker19['close']
        gainpre52low19 = gainpreticker19['fiftyTwoWkLow']
        gainpre52high19 = gainpreticker19['fiftyTwoWkHigh']
        gainprevol19 = round(float(gainpreticker19['volume'])*0.000001,ndigits=2)


        pregain20 = pregainrdata[19]
        gainpreticker20 = pregain20['ticker']
        gainprechange20 = round(float(gainpreticker20['changeRatio'])*100,ndigits=2)
        gainpresym20 = gainpreticker20['symbol']
        gainpreprice20 = gainpreticker20['close']
        gainpre52low20 = gainpreticker20['fiftyTwoWkLow']
        gainpre52high20 = gainpreticker20['fiftyTwoWkHigh']
        gainprevol20 = round(float(gainpreticker20['volume'])*0.000001,ndigits=2)


        pregain21 = pregainrdata[20]
        gainpreticker21 = pregain21['ticker']
        gainprechange21 = round(float(gainpreticker21['changeRatio'])*100,ndigits=2)
        gainpresym21 = gainpreticker21['symbol']
        gainpre52low21 = gainpreticker21['fiftyTwoWkLow']
        gainpre52high21 = gainpreticker21['fiftyTwoWkHigh']
        gainpreprice21 = gainpreticker21['close']
        gainprevol21 = round(float(gainpreticker21['volume'])*0.000001,ndigits=2)


        pregain22 = pregainrdata[21]
        gainpreticker22 = pregain22['ticker']
        gainprechange22 = round(float(gainpreticker22['changeRatio'])*100,ndigits=2)
        gainpresym22 = gainpreticker22['symbol']
        gainpre52low22 = gainpreticker22['fiftyTwoWkLow']
        gainpreprice22= gainpreticker22['close']
        gainpre52high22 = gainpreticker22['fiftyTwoWkHigh']
        gainprevol22 = round(float(gainpreticker22['volume'])*0.000001,ndigits=2)


        pregain23 = pregainrdata[22]
        gainpreticker23 = pregain23['ticker']
        gainprechange23 = round(float(gainpreticker23['changeRatio'])*100,ndigits=2)
        gainpresym23 = gainpreticker23['symbol']
        gainpre52low23 = gainpreticker23['fiftyTwoWkLow']
        gainpre52high23 = gainpreticker23['fiftyTwoWkHigh']
        gainpreprice23 = gainpreticker23['close']
        gainprevol23 = round(float(gainpreticker23['volume'])*0.000001,ndigits=2)


        pregain24 = pregainrdata[23]
        gainpreticker24 = pregain24['ticker']
        gainprechange24 = round(float(gainpreticker24['changeRatio'])*100,ndigits=2)
        gainpresym24 = gainpreticker24['symbol']
        gainpre52low24 = gainpreticker24['fiftyTwoWkLow']
        gainpre52high24 = gainpreticker24['fiftyTwoWkHigh']
        gainpreprice24 = gainpreticker24['close']
        gainprevol24 = round(float(gainpreticker24['volume'])*0.000001,ndigits=2)



        super().__init__(
            placeholder="🇬 🇦 🇮 🇳 🇪 🇷 🇸  - 🇵 🇷 🇪 🇲 🇦 🇷 🇰 🇪 🇹",
           min_values=1,
           max_values=1,
            custom_id="gainpremarket",
            options=[ 
                disnake.SelectOption(label=f"1️⃣{gainpresym1} ${gainpreprice1}", description=f"Vol:{gainprevol1}m 52 low:{gainpre52low1} 52 high:{gainpre52high1}"),
                disnake.SelectOption(label=f"2️⃣{gainpresym2} ${gainpreprice2}", description=f"Vol:{gainprevol2}m 52 low:{gainpre52low2} 52 high:{gainpre52high2}"),
                disnake.SelectOption(label=f"3️⃣{gainpresym3} ${gainpreprice3}", description=f"Vol:{gainprevol3}m 52 low:{gainpre52low3} 52 high:{gainpre52high3}"),
                disnake.SelectOption(label=f"4️⃣{gainpresym4} ${gainpreprice4}", description=f"Vol:{gainprevol4}m 52 low:{gainpre52low4} 52 high:{gainpre52high4}"),
                disnake.SelectOption(label=f"5️⃣{gainpresym5} ${gainpreprice5}", description=f"Vol:{gainprevol5}m52 low:{gainpre52low5} 52 high:{gainpre52high5}"),
                disnake.SelectOption(label=f"6️⃣{gainpresym6} ${gainpreprice6}", description=f"Vol:{gainprevol6}m 52 low:{gainpre52low6} 52 high:{gainpre52high6}"),
                disnake.SelectOption(label=f"7️⃣{gainpresym7} ${gainpreprice7}",description=f"Vol:{gainprevol7}m 52 low:{gainpre52low7} 52 high:{gainpre52high7}"),
                disnake.SelectOption(label=f"8️⃣{gainpresym8} ${gainpreprice8}",description=f"Vol:{gainprevol8}m 52 low:{gainpre52low8} 52 high:{gainpre52high8}"),
                disnake.SelectOption(label=f"9️⃣{gainpresym9} ${gainpreprice9}",description=f"Vol:{gainprevol9}m 52 low:{gainpre52low9} 52 high:{gainpre52high9}"),
                disnake.SelectOption(label=f"🔟{gainpresym10} ${gainpreprice10}",description=f"Vol:{gainprevol10}m 52 low:{gainpre52low10} 52 high:{gainpre52high10}"),
                disnake.SelectOption(label=f"1️⃣1️⃣{gainpresym11} ${gainpreprice11}",description=f"Vol:{gainprevol11}m 52 low:{gainpre52low11} 52 high:{gainpre52high11}"),
                disnake.SelectOption(label=f"1️⃣2️⃣{gainpresym12} ${gainpreprice12}",description=f"Vol:{gainprevol12}m 52 low:{gainpre52low12} 52 high:{gainpre52high12}"),
                disnake.SelectOption(label=f"1️⃣3️⃣{gainpresym13} ${gainpreprice13}",description=f"Vol:{gainprevol13}m 52 low:{gainpre52low13} 52 high:{gainpre52high13}"),
                disnake.SelectOption(label=f"1️⃣4️⃣{gainpresym14} ${gainpreprice14}",description=f"Vol:{gainprevol14}m 52 low:{gainpre52low14} 52 high:{gainpre52high14}"),
                disnake.SelectOption(label=f"1️⃣5️⃣{gainpresym15} ${gainpreprice15}", description=f"Vol:{gainprevol15}m 52 low:{gainpre52low15} 52 high:{gainpre52high15}"),
                disnake.SelectOption(label=f"1️⃣6️⃣{gainpresym16} ${gainpreprice16}", description=f"Vol:{gainprevol16}m 52 low:{gainpre52low16} 52 high:{gainpre52high16}"),
                disnake.SelectOption(label=f"1️⃣7️⃣{gainpresym17} ${gainpreprice17}", description=f"Vol:{gainprevol17}m 52 low:{gainpre52low17} 52 high:{gainpre52high17}"),
                disnake.SelectOption(label=f"1️⃣8️⃣{gainpresym18} ${gainpreprice18}", description=f"Vol:{gainprevol18}m 52 low:{gainpre52low18} 52 high:{gainpre52high18}"),
                disnake.SelectOption(label=f"1️⃣9️⃣{gainpresym19} ${gainpreprice19}", description=f"Vol:{gainprevol19}m 52 low:{gainpre52low19} 52 high:{gainpre52high19}"),
                disnake.SelectOption(label=f"2️⃣0️⃣{gainpresym20} ${gainpreprice20}", description=f"Vol:{gainprevol20}m 52 low:{gainpre52low20} 52 high:{gainpre52high20}"),
                disnake.SelectOption(label=f"2️⃣1️⃣{gainpresym21} ${gainpreprice21}", description=f"Vol:{gainprevol21}m 52 low:{gainpre52low21} 52 high:{gainpre52high21}"),
                disnake.SelectOption(label=f"2️⃣2️⃣{gainpresym22} ${gainpreprice22}", description=f"Vol:{gainprevol22}m 52 low:{gainpre52low22} 52 high:{gainpre52high22}"),
                disnake.SelectOption(label=f"2️⃣3️⃣{gainpresym23} ${gainpreprice23}", description=f"Vol:{gainprevol23}m 52 low:{gainpre52low23} 52 high:{gainpre52high23}"),
                disnake.SelectOption(label=f"2️⃣4️⃣{gainpresym24} ${gainpreprice24}", description=f"Vol:{gainprevol24}m 52 low:{gainpre52low24} 52 high:{gainpre52high24}"),



            ]
        )

    async def callback(self, interaction:disnake.ApplicationCommandInteraction):
        if self.values[0] == self.values[0]:
            await interaction.send("```py\nSoon dad ormom, soon! For now - quick display for reference~!``")




class AfterHoursGainer(disnake.ui.Select):
    def __init__(self):

        aftergainr = requests.get(url="https://quotes-gw.webullfintech.com/api/bgw/market/topGainers?regionId=6&rankType=afterMarket&pageIndex=1&pageSize=50").json()
        aftergainrdata = aftergainr['data']

        aftergain1 = aftergainrdata[0]
        gainafterticker1 = aftergain1['ticker']
        gainafterchange1 = round(float(gainafterticker1['changeRatio'])*100,ndigits=2)
        gainaftersym1 = gainafterticker1['symbol']
        gainafter52low1 = gainafterticker1['fiftyTwoWkLow']
        gainafter52high1 = gainafterticker1['fiftyTwoWkHigh']
        gainafterprice1 = gainafterticker1['close']
        gainaftervol1 = round(float(gainafterticker1['volume'])*0.000001,ndigits=2)



        aftergain2 = aftergainrdata[1]
        gainafterticker2 = aftergain2['ticker']
        gainafterchange2 = round(float(gainafterticker2['changeRatio'])*100,ndigits=2)
        gainaftersym2 = gainafterticker2['symbol']
        gainafter52low2 = gainafterticker2['fiftyTwoWkLow']
        gainafter52high2 = gainafterticker2['fiftyTwoWkHigh']
        gainafterprice2 = gainafterticker2['close']
        gainaftervol2 = round(float(gainafterticker2['volume'])*0.000001,ndigits=2)



        aftergain3 = aftergainrdata[2]
        gainafterticker3 = aftergain3['ticker']
        gainafterchange3 = round(float(gainafterticker3['changeRatio'])*100,ndigits=2)
        gainaftersym3 = gainafterticker3['symbol']
        gainafter52low3 = gainafterticker3['fiftyTwoWkLow']
        gainafter52high3 = gainafterticker3['fiftyTwoWkHigh']
        gainafterprice3 = gainafterticker3['close']
        gainaftervol3 = round(float(gainafterticker3['volume'])*0.000001,ndigits=2)



        aftergain4 = aftergainrdata[3]
        gainafterticker4 = aftergain4['ticker']
        gainafterchange4 = round(float(gainafterticker4['changeRatio'])*100,ndigits=2)
        gainaftersym4 = gainafterticker4['symbol']
        gainafter52low4 = gainafterticker4['fiftyTwoWkLow']
        gainafter52high4 = gainafterticker4['fiftyTwoWkHigh']
        gainafterprice4 = gainafterticker4['close']
        gainaftervol4 = round(float(gainafterticker4['volume'])*0.000001,ndigits=2)

        aftergain5 = aftergainrdata[4]
        gainafterticker5 = aftergain5['ticker']
        gainafterchange5 = round(float(gainafterticker5['changeRatio'])*100,ndigits=2)
        gainaftersym5 = gainafterticker5['symbol']
        gainafter52low5 = gainafterticker5['fiftyTwoWkLow']
        gainafter52high5 = gainafterticker5['fiftyTwoWkHigh']
        gainafterprice5 = gainafterticker5['close']
        gainaftervol5 = round(float(gainafterticker5['volume'])*0.000001,ndigits=2)


        aftergain6 = aftergainrdata[5]
        gainafterticker6 = aftergain6['ticker']
        gainafterchange6 = round(float(gainafterticker6['changeRatio'])*100,ndigits=2)
        gainaftersym6 = gainafterticker6['symbol']
        gainafter52low6 = gainafterticker6['fiftyTwoWkLow']
        gainafter52high6 = gainafterticker6['fiftyTwoWkHigh']
        gainafterprice6 = gainafterticker6['close']
        gainaftervol6 = round(float(gainafterticker6['volume'])*0.000001,ndigits=2)


        aftergain7 = aftergainrdata[6]
        gainafterticker7 = aftergain7['ticker']
        gainafterchange7 = round(float(gainafterticker7['changeRatio'])*100,ndigits=2)
        gainaftersym7 = gainafterticker7['symbol']
        gainafter52low7 = gainafterticker7['fiftyTwoWkLow']
        gainafter52high7 = gainafterticker7['fiftyTwoWkHigh']
        gainafterprice7 = gainafterticker7['close']
        gainaftervol7 = round(float(gainafterticker7['volume'])*0.000001,ndigits=2)


        aftergain8 = aftergainrdata[7]
        gainafterticker8 = aftergain8['ticker']
        gainafterchange8 = round(float(gainafterticker8['changeRatio'])*100,ndigits=2)
        gainaftersym8 = gainafterticker8['symbol']
        gainafter52low8 = gainafterticker8['fiftyTwoWkLow']
        gainafter52high8 = gainafterticker8['fiftyTwoWkHigh']
        gainafterprice8 = gainafterticker8['close']
        gainaftervol8 = round(float(gainafterticker8['volume'])*0.000001,ndigits=2)


        aftergain9 = aftergainrdata[8]
        gainafterticker9 = aftergain9['ticker']
        gainafterchange9 = round(float(gainafterticker9['changeRatio'])*100,ndigits=2)
        gainaftersym9 = gainafterticker9['symbol']
        gainafter52low9 = gainafterticker9['fiftyTwoWkLow']
        gainafter52high9 = gainafterticker9['fiftyTwoWkHigh']
        gainafterprice9 = gainafterticker9['close']
        gainaftervol9 = round(float(gainafterticker9['volume'])*0.000001,ndigits=2)


        aftergain10 = aftergainrdata[9]
        gainafterticker10 = aftergain10['ticker']
        gainafterchange10 = round(float(gainafterticker10['changeRatio'])*100,ndigits=2)
        gainaftersym10 = gainafterticker10['symbol']
        gainafter52low10 = gainafterticker10['fiftyTwoWkLow']
        gainafter52high10 = gainafterticker10['fiftyTwoWkHigh']
        gainafterprice10 = gainafterticker10['close']
        gainaftervol10 = round(float(gainafterticker10['volume'])*0.000001,ndigits=2)


        aftergain11 = aftergainrdata[10]
        gainafterticker11 = aftergain11['ticker']
        gainafterchange11 = round(float(gainafterticker11['changeRatio'])*100,ndigits=2)
        gainaftersym11 = gainafterticker11['symbol']
        gainafter52low11 = gainafterticker11['fiftyTwoWkLow']
        gainafter52high11 = gainafterticker11['fiftyTwoWkHigh']
        gainafterprice11 = gainafterticker11['close']
        gainaftervol11 = round(float(gainafterticker11['volume'])*0.000001,ndigits=2)


        aftergain12 = aftergainrdata[11]
        gainafterticker12 = aftergain12['ticker']
        gainafterchange12 = round(float(gainafterticker12['changeRatio'])*100,ndigits=2)
        gainaftersym12 = gainafterticker12['symbol']
        gainafter52low12 = gainafterticker12['fiftyTwoWkLow']
        gainafter52high12 = gainafterticker12['fiftyTwoWkHigh']
        gainafterprice12 = gainafterticker12['close']
        gainaftervol12 = round(float(gainafterticker12['volume'])*0.000001,ndigits=2)


        aftergain13 = aftergainrdata[12]
        gainafterticker13 = aftergain13['ticker']
        gainafterchange13 = round(float(gainafterticker13['changeRatio'])*100,ndigits=2)
        gainaftersym13 = gainafterticker13['symbol']
        gainafter52low13 = gainafterticker13['fiftyTwoWkLow']
        gainafter52high13 = gainafterticker13['fiftyTwoWkHigh']
        gainafterprice13 = gainafterticker13['close']
        gainaftervol13 = round(float(gainafterticker13['volume'])*0.000001,ndigits=2)

        aftergain14 = aftergainrdata[13]
        gainafterticker14 = aftergain14['ticker']
        gainafterchange14 = round(float(gainafterticker14['changeRatio'])*100,ndigits=2)
        gainaftersym14 = gainafterticker14['symbol']
        gainafter52low14 = gainafterticker14['fiftyTwoWkLow']
        gainafter52high14 = gainafterticker14['fiftyTwoWkHigh']
        gainafterprice14 = gainafterticker14['close']
        gainaftervol14 = round(float(gainafterticker14['volume'])*0.000001,ndigits=2)

        aftergain15 = aftergainrdata[14]
        gainafterticker15 = aftergain15['ticker']
        gainafterchange15 = round(float(gainafterticker15['changeRatio'])*100,ndigits=2)
        gainaftersym15 = gainafterticker15['symbol']
        gainafter52low15 = gainafterticker15['fiftyTwoWkLow']
        gainafter52high15 = gainafterticker15['fiftyTwoWkHigh']
        gainafterprice15 = gainafterticker15['close']
        gainaftervol15 = round(float(gainafterticker15['volume'])*0.000001,ndigits=2)


        aftergain16 = aftergainrdata[15]
        gainafterticker16 = aftergain16['ticker']
        gainafterchange16 = round(float(gainafterticker16['changeRatio'])*100,ndigits=2)
        gainaftersym16 = gainafterticker16['symbol']
        gainafter52low16 = gainafterticker16['fiftyTwoWkLow']
        gainafter52high16 = gainafterticker16['fiftyTwoWkHigh']
        gainafterprice16 = gainafterticker16['close']
        gainaftervol16 = round(float(gainafterticker16['volume'])*0.000001,ndigits=2)


        aftergain17 = aftergainrdata[16]
        gainafterticker17 = aftergain17['ticker']
        gainafterchange17 = round(float(gainafterticker17['changeRatio'])*100,ndigits=2)
        gainaftersym17 = gainafterticker17['symbol']
        gainafter52low17 = gainafterticker17['fiftyTwoWkLow']
        gainafter52high17 = gainafterticker17['fiftyTwoWkHigh']
        gainafterprice17 = gainafterticker17['close']
        gainaftervol17 = round(float(gainafterticker17['volume'])*0.000001,ndigits=2)


        aftergain18 = aftergainrdata[17]
        gainafterticker18 = aftergain18['ticker']
        gainafterchange18 = round(float(gainafterticker18['changeRatio'])*100,ndigits=2)
        gainaftersym18 = gainafterticker18['symbol']
        gainafter52low18 = gainafterticker18['fiftyTwoWkLow']
        gainafter52high18 = gainafterticker18['fiftyTwoWkHigh']
        gainafterprice18 = gainafterticker18['close']
        gainaftervol18 = round(float(gainafterticker18['volume'])*0.000001,ndigits=2)


        aftergain19 = aftergainrdata[18]
        gainafterticker19 = aftergain19['ticker']
        gainafterchange19 = round(float(gainafterticker19['changeRatio'])*100,ndigits=2)
        gainaftersym19 = gainafterticker19['symbol']
        gainafterprice19 = gainafterticker19['close']
        gainafter52low19 = gainafterticker19['fiftyTwoWkLow']
        gainafter52high19 = gainafterticker19['fiftyTwoWkHigh']
        gainaftervol19 = round(float(gainafterticker19['volume'])*0.000001,ndigits=2)


        aftergain20 = aftergainrdata[19]
        gainafterticker20 = aftergain20['ticker']
        gainafterchange20 = round(float(gainafterticker20['changeRatio'])*100,ndigits=2)
        gainaftersym20 = gainafterticker20['symbol']
        gainafterprice20 = gainafterticker20['close']
        gainafter52low20 = gainafterticker20['fiftyTwoWkLow']
        gainafter52high20 = gainafterticker20['fiftyTwoWkHigh']
        gainaftervol20 = round(float(gainafterticker20['volume'])*0.000001,ndigits=2)


        aftergain21 = aftergainrdata[20]
        gainafterticker21 = aftergain21['ticker']
        gainafterchange21 = round(float(gainafterticker21['changeRatio'])*100,ndigits=2)
        gainaftersym21 = gainafterticker21['symbol']
        gainafter52low21 = gainafterticker21['fiftyTwoWkLow']
        gainafter52high21 = gainafterticker21['fiftyTwoWkHigh']
        gainafterprice21 = gainafterticker21['close']
        gainaftervol21 = round(float(gainafterticker21['volume'])*0.000001,ndigits=2)


        aftergain22 = aftergainrdata[21]
        gainafterticker22 = aftergain22['ticker']
        gainafterchange22 = round(float(gainafterticker22['changeRatio'])*100,ndigits=2)
        gainaftersym22 = gainafterticker22['symbol']
        gainafter52low22 = gainafterticker22['fiftyTwoWkLow']
        gainafterprice22= gainafterticker22['close']
        gainafter52high22 = gainafterticker22['fiftyTwoWkHigh']
        gainaftervol22 = round(float(gainafterticker22['volume'])*0.000001,ndigits=2)


        aftergain23 = aftergainrdata[22]
        gainafterticker23 = aftergain23['ticker']
        gainafterchange23 = round(float(gainafterticker23['changeRatio'])*100,ndigits=2)
        gainaftersym23 = gainafterticker23['symbol']
        gainafter52low23 = gainafterticker23['fiftyTwoWkLow']
        gainafter52high23 = gainafterticker23['fiftyTwoWkHigh']
        gainafterprice23 = gainafterticker23['close']
        gainaftervol23 = round(float(gainafterticker23['volume'])*0.000001,ndigits=2)


        aftergain24 = aftergainrdata[23]
        gainafterticker24 = aftergain24['ticker']
        gainafterchange24 = round(float(gainafterticker24['changeRatio'])*100,ndigits=2)
        gainaftersym24 = gainafterticker24['symbol']
        gainafter52low24 = gainafterticker24['fiftyTwoWkLow']
        gainafter52high24 = gainafterticker24['fiftyTwoWkHigh']
        gainafterprice24 = gainafterticker24['close']
        gainaftervol24 = round(float(gainafterticker24['volume'])*0.000001,ndigits=2)



        super().__init__(
            placeholder="🇬 🇦 🇮 🇳 🇪 🇷 🇸  - 🇦 🇫 🇹 🇪 🇷 🇭 🇴 🇺 🇷 🇸",
           min_values=1,
           max_values=1,
            custom_id="gainah",
            options=[ 
                disnake.SelectOption(label=f"1️⃣{gainaftersym1} ${gainafterprice1} Performance: {gainafterchange1}", description=f"Vol:{gainaftervol1}m 52 low:{gainafter52low1} 52 high:{gainafter52high1}"),
                disnake.SelectOption(label=f"2️⃣{gainaftersym2} ${gainafterprice2} Performance: {gainafterchange2}", description=f"Vol:{gainaftervol2}m 52 low:{gainafter52low2} 52 high:{gainafter52high2}"),
                disnake.SelectOption(label=f"3️⃣{gainaftersym3} ${gainafterprice3} Performance: {gainafterchange3}", description=f"Vol:{gainaftervol3}m 52 low:{gainafter52low3} 52 high:{gainafter52high3}"),
                disnake.SelectOption(label=f"4️⃣{gainaftersym4} ${gainafterprice4} Performance: {gainafterchange4}", description=f"Vol:{gainaftervol4}m 52 low:{gainafter52low4} 52 high:{gainafter52high4}"),
                disnake.SelectOption(label=f"5️⃣{gainaftersym5} ${gainafterprice5} Performance: {gainafterchange5}", description=f"Vol:{gainaftervol5}m52 low:{gainafter52low5} 52 high:{gainafter52high5}"),
                disnake.SelectOption(label=f"6️⃣{gainaftersym6} ${gainafterprice6} Performance: {gainafterchange6}", description=f"Vol:{gainaftervol6}m 52 low:{gainafter52low6} 52 high:{gainafter52high6}"),
                disnake.SelectOption(label=f"7️⃣{gainaftersym7} ${gainafterprice7} Performance: {gainafterchange7}",description=f"Vol:{gainaftervol7}m 52 low:{gainafter52low7} 52 high:{gainafter52high7}"),
                disnake.SelectOption(label=f"8️⃣{gainaftersym8} ${gainafterprice8} Performance: {gainafterchange8}",description=f"Vol:{gainaftervol8}m 52 low:{gainafter52low8} 52 high:{gainafter52high8}"),
                disnake.SelectOption(label=f"9️⃣{gainaftersym9} ${gainafterprice9} Performance: {gainafterchange9}",description=f"Vol:{gainaftervol9}m 52 low:{gainafter52low9} 52 high:{gainafter52high9}"),
                disnake.SelectOption(label=f"🔟{gainaftersym10} ${gainafterprice10} Performance: {gainafterchange10}",description=f"Vol:{gainaftervol10}m 52 low:{gainafter52low10} 52 high:{gainafter52high10}"),
                disnake.SelectOption(label=f"1️⃣1️⃣{gainaftersym11} ${gainafterprice11} Performance: {gainafterchange11}",description=f"Vol:{gainaftervol11}m 52 low:{gainafter52low11} 52 high:{gainafter52high11}"),
                disnake.SelectOption(label=f"1️⃣2️⃣{gainaftersym12} ${gainafterprice12} Performance: {gainafterchange12}",description=f"Vol:{gainaftervol12}m 52 low:{gainafter52low12} 52 high:{gainafter52high12}"),
                disnake.SelectOption(label=f"1️⃣3️⃣{gainaftersym13} ${gainafterprice13} Performance: {gainafterchange13}",description=f"Vol:{gainaftervol13}m 52 low:{gainafter52low13} 52 high:{gainafter52high13}"),
                disnake.SelectOption(label=f"1️⃣4️⃣{gainaftersym14} ${gainafterprice14} Performance: {gainafterchange14}",description=f"Vol:{gainaftervol14}m 52 low:{gainafter52low14} 52 high:{gainafter52high14}"),
                disnake.SelectOption(label=f"1️⃣5️⃣{gainaftersym15} ${gainafterprice15} Performance: {gainafterchange15}", description=f"Vol:{gainaftervol15}m 52 low:{gainafter52low15} 52 high:{gainafter52high15}"),
                disnake.SelectOption(label=f"1️⃣6️⃣{gainaftersym16} ${gainafterprice16} Performance: {gainafterchange16}", description=f"Vol:{gainaftervol16}m 52 low:{gainafter52low16} 52 high:{gainafter52high16}"),
                disnake.SelectOption(label=f"1️⃣7️⃣{gainaftersym17} ${gainafterprice17} Performance: {gainafterchange17}", description=f"Vol:{gainaftervol17}m 52 low:{gainafter52low17} 52 high:{gainafter52high17}"),
                disnake.SelectOption(label=f"1️⃣8️⃣{gainaftersym18} ${gainafterprice18} Performance: {gainafterchange18}", description=f"Vol:{gainaftervol18}m 52 low:{gainafter52low18} 52 high:{gainafter52high18}"),
                disnake.SelectOption(label=f"1️⃣9️⃣{gainaftersym19} ${gainafterprice19} Performance: {gainafterchange19}", description=f"Vol:{gainaftervol19}m 52 low:{gainafter52low19} 52 high:{gainafter52high19}"),
                disnake.SelectOption(label=f"2️⃣0️⃣{gainaftersym20} ${gainafterprice20} Performance: {gainafterchange20}", description=f"Vol:{gainaftervol20}m 52 low:{gainafter52low20} 52 high:{gainafter52high20}"),
                disnake.SelectOption(label=f"2️⃣1️⃣{gainaftersym21} ${gainafterprice21} Performance: {gainafterchange21}", description=f"Vol:{gainaftervol21}m 52 low:{gainafter52low21} 52 high:{gainafter52high21}"),
                disnake.SelectOption(label=f"2️⃣2️⃣{gainaftersym22} ${gainafterprice22} Performance: {gainafterchange22}", description=f"Vol:{gainaftervol22}m 52 low:{gainafter52low22} 52 high:{gainafter52high22}"),
                disnake.SelectOption(label=f"2️⃣3️⃣{gainaftersym23} ${gainafterprice23} Performance: {gainafterchange23}", description=f"Vol:{gainaftervol23}m 52 low:{gainafter52low23} 52 high:{gainafter52high23}"),
                disnake.SelectOption(label=f"2️⃣4️⃣{gainaftersym24} ${gainafterprice24} Performance: {gainafterchange24}", description=f"Vol:{gainaftervol24}m 52 low:{gainafter52low24} 52 high:{gainafter52high24}"),



            ]
        )

    async def callback(self, interaction:disnake.ApplicationCommandInteraction):
        if self.values[0] == self.values[0]:
            await interaction.send("```py\nSoon dad ormom, soon! For now - quick display for reference~!``")           


class TopMoversView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(PremarketGainer())
        self.add_item(FiveMinuteGainer())
        self.add_item(Day1Gainer())
        self.add_item(AfterHoursGainer())



    @disnake.ui.button(label="Top 🟩 Gainers", style=disnake.ButtonStyle.grey)
    async def topmovers(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        em=disnake.Embed(title="Top 🟩 Gainers", description="```py\nChoose between top movers on the 5min timeframe, one day, pre-market, and after-hours. Can toggle between top movers and top gainers using the '🪩' button.```", color=disnake.Colour.green(), url="https://www.fudstop.io")
        view = disnake.ui.View()
        try:
            view.clear_items()
            view.add_item(Day1Gainer())
            view.add_item(FiveMinuteGainer())
            view.add_item(AfterHoursGainer())
            view.add_item(PremarketGainer())

        except ValueError:
            view.clear_items()
            view.add_item(Day1Gainer())
            view.add_item(FiveMinuteGainer())
            view.add_item(AfterHoursGainer())
            view.add_item(PremarketGainer())

        Day1Gainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        FiveMinuteGainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        AfterHoursGainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        PremarketGainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())

        await inter.response.edit_message(embed=em,view=view)



    @disnake.ui.button(label="FTDs 🗓️ With T+35 Dates", style=disnake.ButtonStyle.grey)
    async def t35(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        em=disnake.Embed(title="FTDs 🗓️ With T+35 Dates", description="```py\nCurrently displaying the top 24 tickers with the highest amount of FTDs and with their respective T+35 settlement dates posted. These tickers can be great opportunities for share play rebounds just like the high short interest menu.\n\nThis data updates every time the command is called.```", color=disnake.Colour.red(), url="https://www.fudstop.io")
        view = disnake.ui.View()
        try:
            view.add_item(FTDStocksDropdown())
        except ValueError:
            view.clear_items()
            view.add_item(FTDStocksDropdown())


        FTDStocksDropdown().callback =lambda inter: inter.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view,embed=em)


    @disnake.ui.button(label="High 🩳 Shorts", style=disnake.ButtonStyle.grey)
    async def highshort(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        em=disnake.Embed(title="High 🩳 Shorts", description="```py\nThis dropdown displays the ```", color=disnake.Colour.red(), url="https://www.fudstop.io")
        view = disnake.ui.View()
        try:
            view.add_item(ShortInt())
        except ValueError:
            view.clear_items()
            view.add_item(ShortInt())


        ShortInt().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view, embed=em)



class Day1Loser(disnake.ui.Select):
    def __init__(self):

        day1gainr = requests.get(url="https://quotes-gw.webullfintech.com/api/bgw/market/dropGainers?regionId=6&rankType=1d&pageIndex=1&pageSize=24").json()
        day1gainrdata = day1gainr['data']

        day1gain1 = day1gainrdata[0]
        gaind1ticker1 = day1gain1['ticker']
        gaind1change1 = round(float(gaind1ticker1['changeRatio'])*100,ndigits=2)
        gain1dsym1 = gaind1ticker1['symbol']
        gain1d52low1 = gaind1ticker1['fiftyTwoWkLow']
        gain1d52high1 = gaind1ticker1['fiftyTwoWkHigh']
        gain1dprice1 = gaind1ticker1['close']
        gain1dvol1 = round(float(gaind1ticker1['volume'])*0.000001,ndigits=2)



        day1gain2 = day1gainrdata[1]
        gaind1ticker2 = day1gain2['ticker']
        gaind1change2 = round(float(gaind1ticker2['changeRatio'])*100,ndigits=2)
        gain1dsym2 = gaind1ticker2['symbol']
        gain1d52low2 = gaind1ticker2['fiftyTwoWkLow']
        gain1d52high2 = gaind1ticker2['fiftyTwoWkHigh']
        gain1dprice2 = gaind1ticker2['close']
        gain1dvol2 = round(float(gaind1ticker2['volume'])*0.000001,ndigits=2)



        day1gain3 = day1gainrdata[2]
        gaind1ticker3 = day1gain3['ticker']
        gaind1change3 = round(float(gaind1ticker3['changeRatio'])*100,ndigits=2)
        gain1dsym3 = gaind1ticker3['symbol']
        gain1d52low3 = gaind1ticker3['fiftyTwoWkLow']
        gain1d52high3 = gaind1ticker3['fiftyTwoWkHigh']
        gain1dprice3 = gaind1ticker3['close']
        gain1dvol3 = round(float(gaind1ticker3['volume'])*0.000001,ndigits=2)



        day1gain4 = day1gainrdata[3]
        gaind1ticker4 = day1gain4['ticker']
        gaind1change4 = round(float(gaind1ticker4['changeRatio'])*100,ndigits=2)
        gain1dsym4 = gaind1ticker4['symbol']
        gain1d52low4 = gaind1ticker4['fiftyTwoWkLow']
        gain1d52high4 = gaind1ticker4['fiftyTwoWkHigh']
        gain1dprice4 = gaind1ticker4['close']
        gain1dvol4 = round(float(gaind1ticker4['volume'])*0.000001,ndigits=2)

        day1gain5 = day1gainrdata[4]
        gaind1ticker5 = day1gain5['ticker']
        gaind1change5 = round(float(gaind1ticker5['changeRatio'])*100,ndigits=2)
        gain1dsym5 = gaind1ticker5['symbol']
        gain1d52low5 = gaind1ticker5['fiftyTwoWkLow']
        gain1d52high5 = gaind1ticker5['fiftyTwoWkHigh']
        gain1dprice5 = gaind1ticker5['close']
        gain1dvol5 = round(float(gaind1ticker5['volume'])*0.000001,ndigits=2)


        day1gain6 = day1gainrdata[5]
        gaind1ticker6 = day1gain6['ticker']
        gaind1change6 = round(float(gaind1ticker6['changeRatio'])*100,ndigits=2)
        gain1dsym6 = gaind1ticker6['symbol']
        gain1d52low6 = gaind1ticker6['fiftyTwoWkLow']
        gain1d52high6 = gaind1ticker6['fiftyTwoWkHigh']
        gain1dprice6 = gaind1ticker6['close']
        gain1dvol6 = round(float(gaind1ticker6['volume'])*0.000001,ndigits=2)


        day1gain7 = day1gainrdata[6]
        gaind1ticker7 = day1gain7['ticker']
        gaind1change7 = round(float(gaind1ticker7['changeRatio'])*100,ndigits=2)
        gain1dsym7 = gaind1ticker7['symbol']
        gain1d52low7 = gaind1ticker7['fiftyTwoWkLow']
        gain1d52high7 = gaind1ticker7['fiftyTwoWkHigh']
        gain1dprice7 = gaind1ticker7['close']
        gain1dvol7 = round(float(gaind1ticker7['volume'])*0.000001,ndigits=2)


        day1gain8 = day1gainrdata[7]
        gaind1ticker8 = day1gain8['ticker']
        gaind1change8 = round(float(gaind1ticker8['changeRatio'])*100,ndigits=2)
        gain1dsym8 = gaind1ticker8['symbol']
        gain1d52low8 = gaind1ticker8['fiftyTwoWkLow']
        gain1d52high8 = gaind1ticker8['fiftyTwoWkHigh']
        gain1dprice8 = gaind1ticker8['close']
        gain1dvol8 = round(float(gaind1ticker8['volume'])*0.000001,ndigits=2)


        day1gain9 = day1gainrdata[8]
        gaind1ticker9 = day1gain9['ticker']
        gaind1change9 = round(float(gaind1ticker9['changeRatio'])*100,ndigits=2)
        gain1dsym9 = gaind1ticker9['symbol']
        gain1d52low9 = gaind1ticker9['fiftyTwoWkLow']
        gain1d52high9 = gaind1ticker9['fiftyTwoWkHigh']
        gain1dprice9 = gaind1ticker9['close']
        gain1dvol9 = round(float(gaind1ticker9['volume'])*0.000001,ndigits=2)


        day1gain10 = day1gainrdata[9]
        gaind1ticker10 = day1gain10['ticker']
        gaind1change10 = round(float(gaind1ticker10['changeRatio'])*100,ndigits=2)
        gain1dsym10 = gaind1ticker10['symbol']
        gain1d52low10 = gaind1ticker10['fiftyTwoWkLow']
        gain1d52high10 = gaind1ticker10['fiftyTwoWkHigh']
        gain1dprice10 = gaind1ticker10['close']
        gain1dvol10 = round(float(gaind1ticker10['volume'])*0.000001,ndigits=2)


        day1gain11 = day1gainrdata[10]
        gaind1ticker11 = day1gain11['ticker']
        gaind1change11 = round(float(gaind1ticker11['changeRatio'])*100,ndigits=2)
        gain1dsym11 = gaind1ticker11['symbol']
        gain1d52low11 = gaind1ticker11['fiftyTwoWkLow']
        gain1d52high11 = gaind1ticker11['fiftyTwoWkHigh']
        gain1dprice11 = gaind1ticker11['close']
        gain1dvol11 = round(float(gaind1ticker11['volume'])*0.000001,ndigits=2)


        day1gain12 = day1gainrdata[11]
        gaind1ticker12 = day1gain12['ticker']
        gaind1change12 = round(float(gaind1ticker12['changeRatio'])*100,ndigits=2)
        gain1dsym12 = gaind1ticker12['symbol']
        gain1d52low12 = gaind1ticker12['fiftyTwoWkLow']
        gain1d52high12 = gaind1ticker12['fiftyTwoWkHigh']
        gain1dprice12 = gaind1ticker12['close']
        gain1dvol12 = round(float(gaind1ticker12['volume'])*0.000001,ndigits=2)


        day1gain13 = day1gainrdata[12]
        gaind1ticker13 = day1gain13['ticker']
        gaind1change13 = round(float(gaind1ticker13['changeRatio'])*100,ndigits=2)
        gain1dsym13 = gaind1ticker13['symbol']
        gain1d52low13 = gaind1ticker13['fiftyTwoWkLow']
        gain1d52high13 = gaind1ticker13['fiftyTwoWkHigh']
        gain1dprice13 = gaind1ticker13['close']
        gain1dvol13 = round(float(gaind1ticker13['volume'])*0.000001,ndigits=2)

        day1gain14 = day1gainrdata[13]
        gaind1ticker14 = day1gain14['ticker']
        gaind1change14 = round(float(gaind1ticker14['changeRatio'])*100,ndigits=2)
        gain1dsym14 = gaind1ticker14['symbol']
        gain1d52low14 = gaind1ticker14['fiftyTwoWkLow']
        gain1d52high14 = gaind1ticker14['fiftyTwoWkHigh']
        gain1dprice14 = gaind1ticker14['close']
        gain1dvol14 = round(float(gaind1ticker14['volume'])*0.000001,ndigits=2)

        day1gain15 = day1gainrdata[14]
        gaind1ticker15 = day1gain15['ticker']
        gaind1change15 = round(float(gaind1ticker15['changeRatio'])*100,ndigits=2)
        gain1dsym15 = gaind1ticker15['symbol']
        gain1d52low15 = gaind1ticker15['fiftyTwoWkLow']
        gain1d52high15 = gaind1ticker15['fiftyTwoWkHigh']
        gain1dprice15 = gaind1ticker15['close']
        gain1dvol15 = round(float(gaind1ticker15['volume'])*0.000001,ndigits=2)


        day1gain16 = day1gainrdata[15]
        gaind1ticker16 = day1gain16['ticker']
        gaind1change16 = round(float(gaind1ticker16['changeRatio'])*100,ndigits=2)
        gain1dsym16 = gaind1ticker16['symbol']
        gain1d52low16 = gaind1ticker16['fiftyTwoWkLow']
        gain1d52high16 = gaind1ticker16['fiftyTwoWkHigh']
        gain1dprice16 = gaind1ticker16['close']
        gain1dvol16 = round(float(gaind1ticker16['volume'])*0.000001,ndigits=2)


        day1gain17 = day1gainrdata[16]
        gaind1ticker17 = day1gain17['ticker']
        gaind1change17 = round(float(gaind1ticker17['changeRatio'])*100,ndigits=2)
        gain1dsym17 = gaind1ticker17['symbol']
        gain1d52low17 = gaind1ticker17['fiftyTwoWkLow']
        gain1d52high17 = gaind1ticker17['fiftyTwoWkHigh']
        gain1dprice17 = gaind1ticker17['close']
        gain1dvol17 = round(float(gaind1ticker17['volume'])*0.000001,ndigits=2)


        day1gain18 = day1gainrdata[17]
        gaind1ticker18 = day1gain18['ticker']
        gaind1change18 = round(float(gaind1ticker18['changeRatio'])*100,ndigits=2)
        gain1dsym18 = gaind1ticker18['symbol']
        gain1d52low18 = gaind1ticker18['fiftyTwoWkLow']
        gain1d52high18 = gaind1ticker18['fiftyTwoWkHigh']
        gain1dprice18 = gaind1ticker18['close']
        gain1dvol18 = round(float(gaind1ticker18['volume'])*0.000001,ndigits=2)


        day1gain19 = day1gainrdata[18]
        gaind1ticker19 = day1gain19['ticker']
        gaind1change19 = round(float(gaind1ticker19['changeRatio'])*100,ndigits=2)
        gain1dsym19 = gaind1ticker19['symbol']
        gain1dprice19 = gaind1ticker19['close']
        gain1d52low19 = gaind1ticker19['fiftyTwoWkLow']
        gain1d52high19 = gaind1ticker19['fiftyTwoWkHigh']
        gain1dvol19 = round(float(gaind1ticker19['volume'])*0.000001,ndigits=2)


        day1gain20 = day1gainrdata[19]
        gaind1ticker20 = day1gain20['ticker']
        gaind1change20 = round(float(gaind1ticker20['changeRatio'])*100,ndigits=2)
        gain1dsym20 = gaind1ticker20['symbol']
        gain1dprice20 = gaind1ticker20['close']
        gain1d52low20 = gaind1ticker20['fiftyTwoWkLow']
        gain1d52high20 = gaind1ticker20['fiftyTwoWkHigh']
        gain1dvol20 = round(float(gaind1ticker20['volume'])*0.000001,ndigits=2)


        day1gain21 = day1gainrdata[20]
        gaind1ticker21 = day1gain21['ticker']
        gaind1change21 = round(float(gaind1ticker21['changeRatio'])*100,ndigits=2)
        gain1dsym21 = gaind1ticker21['symbol']
        gain1d52low21 = gaind1ticker21['fiftyTwoWkLow']
        gain1d52high21 = gaind1ticker21['fiftyTwoWkHigh']
        gain1dprice21 = gaind1ticker21['close']
        gain1dvol21 = round(float(gaind1ticker21['volume'])*0.000001,ndigits=2)


        day1gain22 = day1gainrdata[21]
        gaind1ticker22 = day1gain22['ticker']
        gaind1change22 = round(float(gaind1ticker22['changeRatio'])*100,ndigits=2)
        gain1dsym22 = gaind1ticker22['symbol']
        gain1d52low22 = gaind1ticker22['fiftyTwoWkLow']
        gain1dprice22= gaind1ticker22['close']
        gain1d52high22 = gaind1ticker22['fiftyTwoWkHigh']
        gain1dvol22 = round(float(gaind1ticker22['volume'])*0.000001,ndigits=2)


        day1gain23 = day1gainrdata[22]
        gaind1ticker23 = day1gain23['ticker']
        gaind1change23 = round(float(gaind1ticker23['changeRatio'])*100,ndigits=2)
        gain1dsym23 = gaind1ticker23['symbol']
        gain1d52low23 = gaind1ticker23['fiftyTwoWkLow']
        gain1d52high23 = gaind1ticker23['fiftyTwoWkHigh']
        gain1dprice23 = gaind1ticker23['close']
        gain1dvol23 = round(float(gaind1ticker23['volume'])*0.000001,ndigits=2)


        day1gain24 = day1gainrdata[23]
        gaind1ticker24 = day1gain24['ticker']
        gaind1change24 = round(float(gaind1ticker24['changeRatio'])*100,ndigits=2)
        gain1dsym24 = gaind1ticker24['symbol']
        gain1d52low24 = gaind1ticker24['fiftyTwoWkLow']
        gain1d52high24 = gaind1ticker24['fiftyTwoWkHigh']
        gain1dprice24 = gaind1ticker24['close']
        gain1dvol24 = round(float(gaind1ticker24['volume'])*0.000001,ndigits=2)



        super().__init__(
            placeholder="🇱 🇴 🇸 🇪 🇷 🇸  - 1️⃣ 🇩 🇦 🇾",
           min_values=1,
           max_values=1,
            custom_id="lose1dsel",
            options=[ 
                disnake.SelectOption(label=f"1️⃣{gain1dsym1} ${gain1dprice1}", description=f"Vol:{gain1dvol1}m 52 low:{gain1d52low1} 52 high:{gain1d52high1}"),
                disnake.SelectOption(label=f"2️⃣{gain1dsym2} ${gain1dprice2}", description=f"Vol:{gain1dvol2}m 52 low:{gain1d52low2} 52 high:{gain1d52high2}"),
                disnake.SelectOption(label=f"3️⃣{gain1dsym3} ${gain1dprice3}", description=f"Vol:{gain1dvol3}m 52 low:{gain1d52low3} 52 high:{gain1d52high3}"),
                disnake.SelectOption(label=f"4️⃣{gain1dsym4} ${gain1dprice4}", description=f"Vol:{gain1dvol4}m 52 low:{gain1d52low4} 52 high:{gain1d52high4}"),
                disnake.SelectOption(label=f"5️⃣{gain1dsym5} ${gain1dprice5}", description=f"Vol:{gain1dvol5}m 52 low:{gain1d52low5} 52 high:{gain1d52high5}"),
                disnake.SelectOption(label=f"6️⃣{gain1dsym6} ${gain1dprice6}", description=f"Vol:{gain1dvol6}m 52 low:{gain1d52low6} 52 high:{gain1d52high6}"),
                disnake.SelectOption(label=f"7️⃣{gain1dsym7} ${gain1dprice7}", description=f"Vol:{gain1dvol7}m 52 low:{gain1d52low7} 52 high:{gain1d52high7}"),
                disnake.SelectOption(label=f"8️⃣{gain1dsym8} ${gain1dprice8}", description=f"Vol:{gain1dvol8}m 52 low:{gain1d52low8} 52 high:{gain1d52high8}"),
                disnake.SelectOption(label=f"9️⃣{gain1dsym9} ${gain1dprice9}", description=f"Vol:{gain1dvol9}m 52 low:{gain1d52low9} 52 high:{gain1d52high9}"),
                disnake.SelectOption(label=f"🔟{gain1dsym10} ${gain1dprice10}", description=f"Vol:{gain1dvol10}m 52 low:{gain1d52low10} 52 high:{gain1d52high10}"),
                disnake.SelectOption(label=f"1️⃣1️⃣{gain1dsym11} ${gain1dprice11}", description=f"Vol:{gain1dvol11}m 52 low:{gain1d52low11} 52 high:{gain1d52high11}"),
                disnake.SelectOption(label=f"1️⃣2️⃣{gain1dsym12} ${gain1dprice12}", description=f"Vol:{gain1dvol12}m 52 low:{gain1d52low12} 52 high:{gain1d52high12}"),
                disnake.SelectOption(label=f"1️⃣3️⃣{gain1dsym13} ${gain1dprice13}", description=f"Vol:{gain1dvol13}m 52 low:{gain1d52low13} 52 high:{gain1d52high13}"),
                disnake.SelectOption(label=f"1️⃣4️⃣{gain1dsym14} ${gain1dprice14}", description=f"Vol:{gain1dvol14}m 52 low:{gain1d52low14} 52 high:{gain1d52high14}"),
                disnake.SelectOption(label=f"1️⃣5️⃣{gain1dsym15} ${gain1dprice15}", description=f"Vol:{gain1dvol15}m 52 low:{gain1d52low15} 52 high:{gain1d52high15}"),
                disnake.SelectOption(label=f"1️⃣6️⃣{gain1dsym16} ${gain1dprice16}", description=f"Vol:{gain1dvol16}m 52 low:{gain1d52low16} 52 high:{gain1d52high16}"),
                disnake.SelectOption(label=f"1️⃣7️⃣{gain1dsym17} ${gain1dprice17}", description=f"Vol:{gain1dvol17}m 52 low:{gain1d52low17} 52 high:{gain1d52high17}"),
                disnake.SelectOption(label=f"1️⃣8️⃣{gain1dsym18} ${gain1dprice18}", description=f"Vol:{gain1dvol18}m 52 low:{gain1d52low18} 52 high:{gain1d52high18}"),
                disnake.SelectOption(label=f"1️⃣9️⃣{gain1dsym19} ${gain1dprice19}", description=f"Vol:{gain1dvol19}m 52 low:{gain1d52low19} 52 high:{gain1d52high19}"),
                disnake.SelectOption(label=f"2️⃣0️⃣{gain1dsym20} ${gain1dprice20}", description=f"Vol:{gain1dvol20}m 52 low:{gain1d52low20} 52 high:{gain1d52high20}"),
                disnake.SelectOption(label=f"2️⃣1️⃣{gain1dsym21} ${gain1dprice21}", description=f"Vol:{gain1dvol21}m 52 low:{gain1d52low21} 52 high:{gain1d52high21}"),
                disnake.SelectOption(label=f"2️⃣2️⃣{gain1dsym22} ${gain1dprice22}", description=f"Vol:{gain1dvol22}m 52 low:{gain1d52low22} 52 high:{gain1d52high22}"),
                disnake.SelectOption(label=f"2️⃣3️⃣{gain1dsym23} ${gain1dprice23}", description=f"Vol:{gain1dvol23}m 52 low:{gain1d52low23} 52 high:{gain1d52high23}"),
                disnake.SelectOption(label=f"2️⃣4️⃣{gain1dsym24} ${gain1dprice24}", description=f"Vol:{gain1dvol24}m 52 low:{gain1d52low24} 52 high:{gain1d52high24}"),



            ]
        )

    async def callback(self, interaction:disnake.ApplicationCommandInteraction):
        if self.values[0] == self.values[0]:
            await interaction.send("```py\nSoon dad ormom, soon! For now - quick display for reference~!``")


class FiveMinuteLoser(disnake.ui.Select):
    def __init__(self):

        fivemingainr = requests.get(url="https://quotes-gw.webullfintech.com/api/bgw/market/dropGainers?regionId=6&rankType=5min&pageIndex=1&pageSize=50").json()
        fivemingainrdata = fivemingainr['data']

        fivemingain1 = fivemingainrdata[0]
        gain5minticker1 = fivemingain1['ticker']
        gain5minchange1 = round(float(gain5minticker1['changeRatio'])*100,ndigits=2)
        gain5minsym1 = gain5minticker1['symbol']
        gain5min52low1 = gain5minticker1['fiftyTwoWkLow']
        gain5min52high1 = gain5minticker1['fiftyTwoWkHigh']
        gain5minprice1 = gain5minticker1['close']
        gain5minvol1 = round(float(gain5minticker1['volume'])*0.000001,ndigits=2)



        fivemingain2 = fivemingainrdata[1]
        gain5minticker2 = fivemingain2['ticker']
        gain5minchange2 = round(float(gain5minticker2['changeRatio'])*100,ndigits=2)
        gain5minsym2 = gain5minticker2['symbol']
        gain5min52low2 = gain5minticker2['fiftyTwoWkLow']
        gain5min52high2 = gain5minticker2['fiftyTwoWkHigh']
        gain5minprice2 = gain5minticker2['close']
        gain5minvol2 = round(float(gain5minticker2['volume'])*0.000001,ndigits=2)



        fivemingain3 = fivemingainrdata[2]
        gain5minticker3 = fivemingain3['ticker']
        gain5minchange3 = round(float(gain5minticker3['changeRatio'])*100,ndigits=2)
        gain5minsym3 = gain5minticker3['symbol']
        gain5min52low3 = gain5minticker3['fiftyTwoWkLow']
        gain5min52high3 = gain5minticker3['fiftyTwoWkHigh']
        gain5minprice3 = gain5minticker3['close']
        gain5minvol3 = round(float(gain5minticker3['volume'])*0.000001,ndigits=2)



        fivemingain4 = fivemingainrdata[3]
        gain5minticker4 = fivemingain4['ticker']
        gain5minchange4 = round(float(gain5minticker4['changeRatio'])*100,ndigits=2)
        gain5minsym4 = gain5minticker4['symbol']
        gain5min52low4 = gain5minticker4['fiftyTwoWkLow']
        gain5min52high4 = gain5minticker4['fiftyTwoWkHigh']
        gain5minprice4 = gain5minticker4['close']
        gain5minvol4 = round(float(gain5minticker4['volume'])*0.000001,ndigits=2)

        fivemingain5 = fivemingainrdata[4]
        gain5minticker5 = fivemingain5['ticker']
        gain5minchange5 = round(float(gain5minticker5['changeRatio'])*100,ndigits=2)
        gain5minsym5 = gain5minticker5['symbol']
        gain5min52low5 = gain5minticker5['fiftyTwoWkLow']
        gain5min52high5 = gain5minticker5['fiftyTwoWkHigh']
        gain5minprice5 = gain5minticker5['close']
        gain5minvol5 = round(float(gain5minticker5['volume'])*0.000001,ndigits=2)


        fivemingain6 = fivemingainrdata[5]
        gain5minticker6 = fivemingain6['ticker']
        gain5minchange6 = round(float(gain5minticker6['changeRatio'])*100,ndigits=2)
        gain5minsym6 = gain5minticker6['symbol']
        gain5min52low6 = gain5minticker6['fiftyTwoWkLow']
        gain5min52high6 = gain5minticker6['fiftyTwoWkHigh']
        gain5minprice6 = gain5minticker6['close']
        gain5minvol6 = round(float(gain5minticker6['volume'])*0.000001,ndigits=2)


        fivemingain7 = fivemingainrdata[6]
        gain5minticker7 = fivemingain7['ticker']
        gain5minchange7 = round(float(gain5minticker7['changeRatio'])*100,ndigits=2)
        gain5minsym7 = gain5minticker7['symbol']
        gain5min52low7 = gain5minticker7['fiftyTwoWkLow']
        gain5min52high7 = gain5minticker7['fiftyTwoWkHigh']
        gain5minprice7 = gain5minticker7['close']
        gain5minvol7 = round(float(gain5minticker7['volume'])*0.000001,ndigits=2)


        fivemingain8 = fivemingainrdata[7]
        gain5minticker8 = fivemingain8['ticker']
        gain5minchange8 = round(float(gain5minticker8['changeRatio'])*100,ndigits=2)
        gain5minsym8 = gain5minticker8['symbol']
        gain5min52low8 = gain5minticker8['fiftyTwoWkLow']
        gain5min52high8 = gain5minticker8['fiftyTwoWkHigh']
        gain5minprice8 = gain5minticker8['close']
        gain5minvol8 = round(float(gain5minticker8['volume'])*0.000001,ndigits=2)


        fivemingain9 = fivemingainrdata[8]
        gain5minticker9 = fivemingain9['ticker']
        gain5minchange9 = round(float(gain5minticker9['changeRatio'])*100,ndigits=2)
        gain5minsym9 = gain5minticker9['symbol']
        gain5min52low9 = gain5minticker9['fiftyTwoWkLow']
        gain5min52high9 = gain5minticker9['fiftyTwoWkHigh']
        gain5minprice9 = gain5minticker9['close']
        gain5minvol9 = round(float(gain5minticker9['volume'])*0.000001,ndigits=2)


        fivemingain10 = fivemingainrdata[9]
        gain5minticker10 = fivemingain10['ticker']
        gain5minchange10 = round(float(gain5minticker10['changeRatio'])*100,ndigits=2)
        gain5minsym10 = gain5minticker10['symbol']
        gain5min52low10 = gain5minticker10['fiftyTwoWkLow']
        gain5min52high10 = gain5minticker10['fiftyTwoWkHigh']
        gain5minprice10 = gain5minticker10['close']
        gain5minvol10 = round(float(gain5minticker10['volume'])*0.000001,ndigits=2)


        fivemingain11 = fivemingainrdata[10]
        gain5minticker11 = fivemingain11['ticker']
        gain5minchange11 = round(float(gain5minticker11['changeRatio'])*100,ndigits=2)
        gain5minsym11 = gain5minticker11['symbol']
        gain5min52low11 = gain5minticker11['fiftyTwoWkLow']
        gain5min52high11 = gain5minticker11['fiftyTwoWkHigh']
        gain5minprice11 = gain5minticker11['close']
        gain5minvol11 = round(float(gain5minticker11['volume'])*0.000001,ndigits=2)


        fivemingain12 = fivemingainrdata[11]
        gain5minticker12 = fivemingain12['ticker']
        gain5minchange12 = round(float(gain5minticker12['changeRatio'])*100,ndigits=2)
        gain5minsym12 = gain5minticker12['symbol']
        gain5min52low12 = gain5minticker12['fiftyTwoWkLow']
        gain5min52high12 = gain5minticker12['fiftyTwoWkHigh']
        gain5minprice12 = gain5minticker12['close']
        gain5minvol12 = round(float(gain5minticker12['volume'])*0.000001,ndigits=2)


        fivemingain13 = fivemingainrdata[12]
        gain5minticker13 = fivemingain13['ticker']
        gain5minchange13 = round(float(gain5minticker13['changeRatio'])*100,ndigits=2)
        gain5minsym13 = gain5minticker13['symbol']
        gain5min52low13 = gain5minticker13['fiftyTwoWkLow']
        gain5min52high13 = gain5minticker13['fiftyTwoWkHigh']
        gain5minprice13 = gain5minticker13['close']
        gain5minvol13 = round(float(gain5minticker13['volume'])*0.000001,ndigits=2)

        fivemingain14 = fivemingainrdata[13]
        gain5minticker14 = fivemingain14['ticker']
        gain5minchange14 = round(float(gain5minticker14['changeRatio'])*100,ndigits=2)
        gain5minsym14 = gain5minticker14['symbol']
        gain5min52low14 = gain5minticker14['fiftyTwoWkLow']
        gain5min52high14 = gain5minticker14['fiftyTwoWkHigh']
        gain5minprice14 = gain5minticker14['close']
        gain5minvol14 = round(float(gain5minticker14['volume'])*0.000001,ndigits=2)

        fivemingain15 = fivemingainrdata[14]
        gain5minticker15 = fivemingain15['ticker']
        gain5minchange15 = round(float(gain5minticker15['changeRatio'])*100,ndigits=2)
        gain5minsym15 = gain5minticker15['symbol']
        gain5min52low15 = gain5minticker15['fiftyTwoWkLow']
        gain5min52high15 = gain5minticker15['fiftyTwoWkHigh']
        gain5minprice15 = gain5minticker15['close']
        gain5minvol15 = round(float(gain5minticker15['volume'])*0.000001,ndigits=2)


        fivemingain16 = fivemingainrdata[15]
        gain5minticker16 = fivemingain16['ticker']
        gain5minchange16 = round(float(gain5minticker16['changeRatio'])*100,ndigits=2)
        gain5minsym16 = gain5minticker16['symbol']
        gain5min52low16 = gain5minticker16['fiftyTwoWkLow']
        gain5min52high16 = gain5minticker16['fiftyTwoWkHigh']
        gain5minprice16 = gain5minticker16['close']
        gain5minvol16 = round(float(gain5minticker16['volume'])*0.000001,ndigits=2)


        fivemingain17 = fivemingainrdata[16]
        gain5minticker17 = fivemingain17['ticker']
        gain5minchange17 = round(float(gain5minticker17['changeRatio'])*100,ndigits=2)
        gain5minsym17 = gain5minticker17['symbol']
        gain5min52low17 = gain5minticker17['fiftyTwoWkLow']
        gain5min52high17 = gain5minticker17['fiftyTwoWkHigh']
        gain5minprice17 = gain5minticker17['close']
        gain5minvol17 = round(float(gain5minticker17['volume'])*0.000001,ndigits=2)


        fivemingain18 = fivemingainrdata[17]
        gain5minticker18 = fivemingain18['ticker']
        gain5minchange18 = round(float(gain5minticker18['changeRatio'])*100,ndigits=2)
        gain5minsym18 = gain5minticker18['symbol']
        gain5min52low18 = gain5minticker18['fiftyTwoWkLow']
        gain5min52high18 = gain5minticker18['fiftyTwoWkHigh']
        gain5minprice18 = gain5minticker18['close']
        gain5minvol18 = round(float(gain5minticker18['volume'])*0.000001,ndigits=2)


        fivemingain19 = fivemingainrdata[18]
        gain5minticker19 = fivemingain19['ticker']
        gain5minchange19 = round(float(gain5minticker19['changeRatio'])*100,ndigits=2)
        gain5minsym19 = gain5minticker19['symbol']
        gain5minprice19 = gain5minticker19['close']
        gain5min52low19 = gain5minticker19['fiftyTwoWkLow']
        gain5min52high19 = gain5minticker19['fiftyTwoWkHigh']
        gain5minvol19 = round(float(gain5minticker19['volume'])*0.000001,ndigits=2)


        fivemingain20 = fivemingainrdata[19]
        gain5minticker20 = fivemingain20['ticker']
        gain5minchange20 = round(float(gain5minticker20['changeRatio'])*100,ndigits=2)
        gain5minsym20 = gain5minticker20['symbol']
        gain5minprice20 = gain5minticker20['close']
        gain5min52low20 = gain5minticker20['fiftyTwoWkLow']
        gain5min52high20 = gain5minticker20['fiftyTwoWkHigh']
        gain5minvol20 = round(float(gain5minticker20['volume'])*0.000001,ndigits=2)


        fivemingain21 = fivemingainrdata[20]
        gain5minticker21 = fivemingain21['ticker']
        gain5minchange21 = round(float(gain5minticker21['changeRatio'])*100,ndigits=2)
        gain5minsym21 = gain5minticker21['symbol']
        gain5min52low21 = gain5minticker21['fiftyTwoWkLow']
        gain5min52high21 = gain5minticker21['fiftyTwoWkHigh']
        gain5minprice21 = gain5minticker21['close']
        gain5minvol21 = round(float(gain5minticker21['volume'])*0.000001,ndigits=2)


        fivemingain22 = fivemingainrdata[21]
        gain5minticker22 = fivemingain22['ticker']
        gain5minchange22 = round(float(gain5minticker22['changeRatio'])*100,ndigits=2)
        gain5minsym22 = gain5minticker22['symbol']
        gain5min52low22 = gain5minticker22['fiftyTwoWkLow']
        gain5minprice22= gain5minticker22['close']
        gain5min52high22 = gain5minticker22['fiftyTwoWkHigh']
        gain5minvol22 = round(float(gain5minticker22['volume'])*0.000001,ndigits=2)


        fivemingain23 = fivemingainrdata[22]
        gain5minticker23 = fivemingain23['ticker']
        gain5minchange23 = round(float(gain5minticker23['changeRatio'])*100,ndigits=2)
        gain5minsym23 = gain5minticker23['symbol']
        gain5min52low23 = gain5minticker23['fiftyTwoWkLow']
        gain5min52high23 = gain5minticker23['fiftyTwoWkHigh']
        gain5minprice23 = gain5minticker23['close']
        gain5minvol23 = round(float(gain5minticker23['volume'])*0.000001,ndigits=2)


        fivemingain24 = fivemingainrdata[23]
        gain5minticker24 = fivemingain24['ticker']
        gain5minchange24 = round(float(gain5minticker24['changeRatio'])*100,ndigits=2)
        gain5minsym24 = gain5minticker24['symbol']
        gain5min52low24 = gain5minticker24['fiftyTwoWkLow']
        gain5min52high24 = gain5minticker24['fiftyTwoWkHigh']
        gain5minprice24 = gain5minticker24['close']
        gain5minvol24 = round(float(gain5minticker24['volume'])*0.000001,ndigits=2)



        super().__init__(
            placeholder="🇱 🇴 🇸 🇪 🇷 🇸  - 5️⃣ 🇲 🇮 🇳",
           min_values=1,
           max_values=1,
            custom_id="lose1dselsc",
            options=[ 
                disnake.SelectOption(label=f"1️⃣{gain5minsym1} ${gain5minprice1}", description=f"Vol:{gain5minvol1}m 52 low:{gain5min52low1} 52 high:{gain5min52high1}"),
                disnake.SelectOption(label=f"2️⃣{gain5minsym2} ${gain5minprice2}", description=f"Vol:{gain5minvol2}m 52 low:{gain5min52low2} 52 high:{gain5min52high2}"),
                disnake.SelectOption(label=f"3️⃣{gain5minsym3} ${gain5minprice3}", description=f"Vol:{gain5minvol3}m 52 low:{gain5min52low3} 52 high:{gain5min52high3}"),
                disnake.SelectOption(label=f"4️⃣{gain5minsym4} ${gain5minprice4}", description=f"Vol:{gain5minvol4}m 52 low:{gain5min52low4} 52 high:{gain5min52high4}"),
                disnake.SelectOption(label=f"5️⃣{gain5minsym5} ${gain5minprice5}", description=f"Vol:{gain5minvol5}m52 low:{gain5min52low5} 52 high:{gain5min52high5}"),
                disnake.SelectOption(label=f"6️⃣{gain5minsym6} ${gain5minprice6}", description=f"Vol:{gain5minvol6}m 52 low:{gain5min52low6} 52 high:{gain5min52high6}"),
                disnake.SelectOption(label=f"7️⃣{gain5minsym7} ${gain5minprice7}",description=f"Vol:{gain5minvol7}m 52 low:{gain5min52low7} 52 high:{gain5min52high7}"),
                disnake.SelectOption(label=f"8️⃣{gain5minsym8} ${gain5minprice8}",description=f"Vol:{gain5minvol8}m 52 low:{gain5min52low8} 52 high:{gain5min52high8}"),
                disnake.SelectOption(label=f"9️⃣{gain5minsym9} ${gain5minprice9}",description=f"Vol:{gain5minvol9}m 52 low:{gain5min52low9} 52 high:{gain5min52high9}"),
                disnake.SelectOption(label=f"🔟{gain5minsym10} ${gain5minprice10}",description=f"Vol:{gain5minvol10}m 52 low:{gain5min52low10} 52 high:{gain5min52high10}"),
                disnake.SelectOption(label=f"1️⃣1️⃣{gain5minsym11} ${gain5minprice11}",description=f"Vol:{gain5minvol11}m 52 low:{gain5min52low11} 52 high:{gain5min52high11}"),
                disnake.SelectOption(label=f"1️⃣2️⃣{gain5minsym12} ${gain5minprice12}",description=f"Vol:{gain5minvol12}m 52 low:{gain5min52low12} 52 high:{gain5min52high12}"),
                disnake.SelectOption(label=f"1️⃣3️⃣{gain5minsym13} ${gain5minprice13}",description=f"Vol:{gain5minvol13}m 52 low:{gain5min52low13} 52 high:{gain5min52high13}"),
                disnake.SelectOption(label=f"1️⃣4️⃣{gain5minsym14} ${gain5minprice14}",description=f"Vol:{gain5minvol14}m 52 low:{gain5min52low14} 52 high:{gain5min52high14}"),
                disnake.SelectOption(label=f"1️⃣5️⃣{gain5minsym15} ${gain5minprice15}", description=f"Vol:{gain5minvol15}m 52 low:{gain5min52low15} 52 high:{gain5min52high15}"),
                disnake.SelectOption(label=f"1️⃣6️⃣{gain5minsym16} ${gain5minprice16}", description=f"Vol:{gain5minvol16}m 52 low:{gain5min52low16} 52 high:{gain5min52high16}"),
                disnake.SelectOption(label=f"1️⃣7️⃣{gain5minsym17} ${gain5minprice17}", description=f"Vol:{gain5minvol17}m 52 low:{gain5min52low17} 52 high:{gain5min52high17}"),
                disnake.SelectOption(label=f"1️⃣8️⃣{gain5minsym18} ${gain5minprice18}", description=f"Vol:{gain5minvol18}m 52 low:{gain5min52low18} 52 high:{gain5min52high18}"),
                disnake.SelectOption(label=f"1️⃣9️⃣{gain5minsym19} ${gain5minprice19}", description=f"Vol:{gain5minvol19}m 52 low:{gain5min52low19} 52 high:{gain5min52high19}"),
                disnake.SelectOption(label=f"2️⃣0️⃣{gain5minsym20} ${gain5minprice20}", description=f"Vol:{gain5minvol20}m 52 low:{gain5min52low20} 52 high:{gain5min52high20}"),
                disnake.SelectOption(label=f"2️⃣1️⃣{gain5minsym21} ${gain5minprice21}", description=f"Vol:{gain5minvol21}m 52 low:{gain5min52low21} 52 high:{gain5min52high21}"),
                disnake.SelectOption(label=f"2️⃣2️⃣{gain5minsym22} ${gain5minprice22}", description=f"Vol:{gain5minvol22}m 52 low:{gain5min52low22} 52 high:{gain5min52high22}"),
                disnake.SelectOption(label=f"2️⃣3️⃣{gain5minsym23} ${gain5minprice23}", description=f"Vol:{gain5minvol23}m 52 low:{gain5min52low23} 52 high:{gain5min52high23}"),
                disnake.SelectOption(label=f"2️⃣4️⃣{gain5minsym24} ${gain5minprice24}", description=f"Vol:{gain5minvol24}m 52 low:{gain5min52low24} 52 high:{gain5min52high24}"),



            ]
        )

    async def callback(self, interaction:disnake.ApplicationCommandInteraction):
        if self.values[0] == self.values[0]:
            await interaction.send("```py\nSoon dad ormom, soon! For now - quick display for reference~!``")



class PremarketLoser(disnake.ui.Select):
    def __init__(self):

        pregainr = requests.get(url="https://quotes-gw.webullfintech.com/api/bgw/market/dropGainers?regionId=6&rankType=preMarket&pageIndex=1&pageSize=50").json()
        pregainrdata = pregainr['data']

        pregain1 = pregainrdata[0]
        gainpreticker1 = pregain1['ticker']
        gainprechange1 = round(float(gainpreticker1['changeRatio'])*100,ndigits=2)
        gainpresym1 = gainpreticker1['symbol']
        gainpre52low1 = gainpreticker1['fiftyTwoWkLow']
        gainpre52high1 = gainpreticker1['fiftyTwoWkHigh']
        gainpreprice1 = gainpreticker1['close']
        gainprevol1 = round(float(gainpreticker1['volume'])*0.000001,ndigits=2)



        pregain2 = pregainrdata[1]
        gainpreticker2 = pregain2['ticker']
        gainprechange2 = round(float(gainpreticker2['changeRatio'])*100,ndigits=2)
        gainpresym2 = gainpreticker2['symbol']
        gainpre52low2 = gainpreticker2['fiftyTwoWkLow']
        gainpre52high2 = gainpreticker2['fiftyTwoWkHigh']
        gainpreprice2 = gainpreticker2['close']
        gainprevol2 = round(float(gainpreticker2['volume'])*0.000001,ndigits=2)



        pregain3 = pregainrdata[2]
        gainpreticker3 = pregain3['ticker']
        gainprechange3 = round(float(gainpreticker3['changeRatio'])*100,ndigits=2)
        gainpresym3 = gainpreticker3['symbol']
        gainpre52low3 = gainpreticker3['fiftyTwoWkLow']
        gainpre52high3 = gainpreticker3['fiftyTwoWkHigh']
        gainpreprice3 = gainpreticker3['close']
        gainprevol3 = round(float(gainpreticker3['volume'])*0.000001,ndigits=2)



        pregain4 = pregainrdata[3]
        gainpreticker4 = pregain4['ticker']
        gainprechange4 = round(float(gainpreticker4['changeRatio'])*100,ndigits=2)
        gainpresym4 = gainpreticker4['symbol']
        gainpre52low4 = gainpreticker4['fiftyTwoWkLow']
        gainpre52high4 = gainpreticker4['fiftyTwoWkHigh']
        gainpreprice4 = gainpreticker4['close']
        gainprevol4 = round(float(gainpreticker4['volume'])*0.000001,ndigits=2)

        pregain5 = pregainrdata[4]
        gainpreticker5 = pregain5['ticker']
        gainprechange5 = round(float(gainpreticker5['changeRatio'])*100,ndigits=2)
        gainpresym5 = gainpreticker5['symbol']
        gainpre52low5 = gainpreticker5['fiftyTwoWkLow']
        gainpre52high5 = gainpreticker5['fiftyTwoWkHigh']
        gainpreprice5 = gainpreticker5['close']
        gainprevol5 = round(float(gainpreticker5['volume'])*0.000001,ndigits=2)


        pregain6 = pregainrdata[5]
        gainpreticker6 = pregain6['ticker']
        gainprechange6 = round(float(gainpreticker6['changeRatio'])*100,ndigits=2)
        gainpresym6 = gainpreticker6['symbol']
        gainpre52low6 = gainpreticker6['fiftyTwoWkLow']
        gainpre52high6 = gainpreticker6['fiftyTwoWkHigh']
        gainpreprice6 = gainpreticker6['close']
        gainprevol6 = round(float(gainpreticker6['volume'])*0.000001,ndigits=2)


        pregain7 = pregainrdata[6]
        gainpreticker7 = pregain7['ticker']
        gainprechange7 = round(float(gainpreticker7['changeRatio'])*100,ndigits=2)
        gainpresym7 = gainpreticker7['symbol']
        gainpre52low7 = gainpreticker7['fiftyTwoWkLow']
        gainpre52high7 = gainpreticker7['fiftyTwoWkHigh']
        gainpreprice7 = gainpreticker7['close']
        gainprevol7 = round(float(gainpreticker7['volume'])*0.000001,ndigits=2)


        pregain8 = pregainrdata[7]
        gainpreticker8 = pregain8['ticker']
        gainprechange8 = round(float(gainpreticker8['changeRatio'])*100,ndigits=2)
        gainpresym8 = gainpreticker8['symbol']
        gainpre52low8 = gainpreticker8['fiftyTwoWkLow']
        gainpre52high8 = gainpreticker8['fiftyTwoWkHigh']
        gainpreprice8 = gainpreticker8['close']
        gainprevol8 = round(float(gainpreticker8['volume'])*0.000001,ndigits=2)


        pregain9 = pregainrdata[8]
        gainpreticker9 = pregain9['ticker']
        gainprechange9 = round(float(gainpreticker9['changeRatio'])*100,ndigits=2)
        gainpresym9 = gainpreticker9['symbol']
        gainpre52low9 = gainpreticker9['fiftyTwoWkLow']
        gainpre52high9 = gainpreticker9['fiftyTwoWkHigh']
        gainpreprice9 = gainpreticker9['close']
        gainprevol9 = round(float(gainpreticker9['volume'])*0.000001,ndigits=2)


        pregain10 = pregainrdata[9]
        gainpreticker10 = pregain10['ticker']
        gainprechange10 = round(float(gainpreticker10['changeRatio'])*100,ndigits=2)
        gainpresym10 = gainpreticker10['symbol']
        gainpre52low10 = gainpreticker10['fiftyTwoWkLow']
        gainpre52high10 = gainpreticker10['fiftyTwoWkHigh']
        gainpreprice10 = gainpreticker10['close']
        gainprevol10 = round(float(gainpreticker10['volume'])*0.000001,ndigits=2)


        pregain11 = pregainrdata[10]
        gainpreticker11 = pregain11['ticker']
        gainprechange11 = round(float(gainpreticker11['changeRatio'])*100,ndigits=2)
        gainpresym11 = gainpreticker11['symbol']
        gainpre52low11 = gainpreticker11['fiftyTwoWkLow']
        gainpre52high11 = gainpreticker11['fiftyTwoWkHigh']
        gainpreprice11 = gainpreticker11['close']
        gainprevol11 = round(float(gainpreticker11['volume'])*0.000001,ndigits=2)


        pregain12 = pregainrdata[11]
        gainpreticker12 = pregain12['ticker']
        gainprechange12 = round(float(gainpreticker12['changeRatio'])*100,ndigits=2)
        gainpresym12 = gainpreticker12['symbol']
        gainpre52low12 = gainpreticker12['fiftyTwoWkLow']
        gainpre52high12 = gainpreticker12['fiftyTwoWkHigh']
        gainpreprice12 = gainpreticker12['close']
        gainprevol12 = round(float(gainpreticker12['volume'])*0.000001,ndigits=2)


        pregain13 = pregainrdata[12]
        gainpreticker13 = pregain13['ticker']
        gainprechange13 = round(float(gainpreticker13['changeRatio'])*100,ndigits=2)
        gainpresym13 = gainpreticker13['symbol']
        gainpre52low13 = gainpreticker13['fiftyTwoWkLow']
        gainpre52high13 = gainpreticker13['fiftyTwoWkHigh']
        gainpreprice13 = gainpreticker13['close']
        gainprevol13 = round(float(gainpreticker13['volume'])*0.000001,ndigits=2)

        pregain14 = pregainrdata[13]
        gainpreticker14 = pregain14['ticker']
        gainprechange14 = round(float(gainpreticker14['changeRatio'])*100,ndigits=2)
        gainpresym14 = gainpreticker14['symbol']
        gainpre52low14 = gainpreticker14['fiftyTwoWkLow']
        gainpre52high14 = gainpreticker14['fiftyTwoWkHigh']
        gainpreprice14 = gainpreticker14['close']
        gainprevol14 = round(float(gainpreticker14['volume'])*0.000001,ndigits=2)

        pregain15 = pregainrdata[14]
        gainpreticker15 = pregain15['ticker']
        gainprechange15 = round(float(gainpreticker15['changeRatio'])*100,ndigits=2)
        gainpresym15 = gainpreticker15['symbol']
        gainpre52low15 = gainpreticker15['fiftyTwoWkLow']
        gainpre52high15 = gainpreticker15['fiftyTwoWkHigh']
        gainpreprice15 = gainpreticker15['close']
        gainprevol15 = round(float(gainpreticker15['volume'])*0.000001,ndigits=2)


        pregain16 = pregainrdata[15]
        gainpreticker16 = pregain16['ticker']
        gainprechange16 = round(float(gainpreticker16['changeRatio'])*100,ndigits=2)
        gainpresym16 = gainpreticker16['symbol']
        gainpre52low16 = gainpreticker16['fiftyTwoWkLow']
        gainpre52high16 = gainpreticker16['fiftyTwoWkHigh']
        gainpreprice16 = gainpreticker16['close']
        gainprevol16 = round(float(gainpreticker16['volume'])*0.000001,ndigits=2)


        pregain17 = pregainrdata[16]
        gainpreticker17 = pregain17['ticker']
        gainprechange17 = round(float(gainpreticker17['changeRatio'])*100,ndigits=2)
        gainpresym17 = gainpreticker17['symbol']
        gainpre52low17 = gainpreticker17['fiftyTwoWkLow']
        gainpre52high17 = gainpreticker17['fiftyTwoWkHigh']
        gainpreprice17 = gainpreticker17['close']
        gainprevol17 = round(float(gainpreticker17['volume'])*0.000001,ndigits=2)


        pregain18 = pregainrdata[17]
        gainpreticker18 = pregain18['ticker']
        gainprechange18 = round(float(gainpreticker18['changeRatio'])*100,ndigits=2)
        gainpresym18 = gainpreticker18['symbol']
        gainpre52low18 = gainpreticker18['fiftyTwoWkLow']
        gainpre52high18 = gainpreticker18['fiftyTwoWkHigh']
        gainpreprice18 = gainpreticker18['close']
        gainprevol18 = round(float(gainpreticker18['volume'])*0.000001,ndigits=2)


        pregain19 = pregainrdata[18]
        gainpreticker19 = pregain19['ticker']
        gainprechange19 = round(float(gainpreticker19['changeRatio'])*100,ndigits=2)
        gainpresym19 = gainpreticker19['symbol']
        gainpreprice19 = gainpreticker19['close']
        gainpre52low19 = gainpreticker19['fiftyTwoWkLow']
        gainpre52high19 = gainpreticker19['fiftyTwoWkHigh']
        gainprevol19 = round(float(gainpreticker19['volume'])*0.000001,ndigits=2)


        pregain20 = pregainrdata[19]
        gainpreticker20 = pregain20['ticker']
        gainprechange20 = round(float(gainpreticker20['changeRatio'])*100,ndigits=2)
        gainpresym20 = gainpreticker20['symbol']
        gainpreprice20 = gainpreticker20['close']
        gainpre52low20 = gainpreticker20['fiftyTwoWkLow']
        gainpre52high20 = gainpreticker20['fiftyTwoWkHigh']
        gainprevol20 = round(float(gainpreticker20['volume'])*0.000001,ndigits=2)


        pregain21 = pregainrdata[20]
        gainpreticker21 = pregain21['ticker']
        gainprechange21 = round(float(gainpreticker21['changeRatio'])*100,ndigits=2)
        gainpresym21 = gainpreticker21['symbol']
        gainpre52low21 = gainpreticker21['fiftyTwoWkLow']
        gainpre52high21 = gainpreticker21['fiftyTwoWkHigh']
        gainpreprice21 = gainpreticker21['close']
        gainprevol21 = round(float(gainpreticker21['volume'])*0.000001,ndigits=2)


        pregain22 = pregainrdata[21]
        gainpreticker22 = pregain22['ticker']
        gainprechange22 = round(float(gainpreticker22['changeRatio'])*100,ndigits=2)
        gainpresym22 = gainpreticker22['symbol']
        gainpre52low22 = gainpreticker22['fiftyTwoWkLow']
        gainpreprice22= gainpreticker22['close']
        gainpre52high22 = gainpreticker22['fiftyTwoWkHigh']
        gainprevol22 = round(float(gainpreticker22['volume'])*0.000001,ndigits=2)


        pregain23 = pregainrdata[22]
        gainpreticker23 = pregain23['ticker']
        gainprechange23 = round(float(gainpreticker23['changeRatio'])*100,ndigits=2)
        gainpresym23 = gainpreticker23['symbol']
        gainpre52low23 = gainpreticker23['fiftyTwoWkLow']
        gainpre52high23 = gainpreticker23['fiftyTwoWkHigh']
        gainpreprice23 = gainpreticker23['close']
        gainprevol23 = round(float(gainpreticker23['volume'])*0.000001,ndigits=2)


        pregain24 = pregainrdata[23]
        gainpreticker24 = pregain24['ticker']
        gainprechange24 = round(float(gainpreticker24['changeRatio'])*100,ndigits=2)
        gainpresym24 = gainpreticker24['symbol']
        gainpre52low24 = gainpreticker24['fiftyTwoWkLow']
        gainpre52high24 = gainpreticker24['fiftyTwoWkHigh']
        gainpreprice24 = gainpreticker24['close']
        gainprevol24 = round(float(gainpreticker24['volume'])*0.000001,ndigits=2)



        super().__init__(
            placeholder="🇱 🇴 🇸 🇪 🇷 🇸 - 🇵 🇷 🇪 🇲 🇦 🇷 🇰 🇪 🇹",
           min_values=1,
           max_values=1,
            custom_id="losepremarket",
            options=[ 
                disnake.SelectOption(label=f"1️⃣{gainpresym1} ${gainpreprice1}", description=f"Vol:{gainprevol1}m 52 low:{gainpre52low1} 52 high:{gainpre52high1}"),
                disnake.SelectOption(label=f"2️⃣{gainpresym2} ${gainpreprice2}", description=f"Vol:{gainprevol2}m 52 low:{gainpre52low2} 52 high:{gainpre52high2}"),
                disnake.SelectOption(label=f"3️⃣{gainpresym3} ${gainpreprice3}", description=f"Vol:{gainprevol3}m 52 low:{gainpre52low3} 52 high:{gainpre52high3}"),
                disnake.SelectOption(label=f"4️⃣{gainpresym4} ${gainpreprice4}", description=f"Vol:{gainprevol4}m 52 low:{gainpre52low4} 52 high:{gainpre52high4}"),
                disnake.SelectOption(label=f"5️⃣{gainpresym5} ${gainpreprice5}", description=f"Vol:{gainprevol5}m52 low:{gainpre52low5} 52 high:{gainpre52high5}"),
                disnake.SelectOption(label=f"6️⃣{gainpresym6} ${gainpreprice6}", description=f"Vol:{gainprevol6}m 52 low:{gainpre52low6} 52 high:{gainpre52high6}"),
                disnake.SelectOption(label=f"7️⃣{gainpresym7} ${gainpreprice7}",description=f"Vol:{gainprevol7}m 52 low:{gainpre52low7} 52 high:{gainpre52high7}"),
                disnake.SelectOption(label=f"8️⃣{gainpresym8} ${gainpreprice8}",description=f"Vol:{gainprevol8}m 52 low:{gainpre52low8} 52 high:{gainpre52high8}"),
                disnake.SelectOption(label=f"9️⃣{gainpresym9} ${gainpreprice9}",description=f"Vol:{gainprevol9}m 52 low:{gainpre52low9} 52 high:{gainpre52high9}"),
                disnake.SelectOption(label=f"🔟{gainpresym10} ${gainpreprice10}",description=f"Vol:{gainprevol10}m 52 low:{gainpre52low10} 52 high:{gainpre52high10}"),
                disnake.SelectOption(label=f"1️⃣1️⃣{gainpresym11} ${gainpreprice11}",description=f"Vol:{gainprevol11}m 52 low:{gainpre52low11} 52 high:{gainpre52high11}"),
                disnake.SelectOption(label=f"1️⃣2️⃣{gainpresym12} ${gainpreprice12}",description=f"Vol:{gainprevol12}m 52 low:{gainpre52low12} 52 high:{gainpre52high12}"),
                disnake.SelectOption(label=f"1️⃣3️⃣{gainpresym13} ${gainpreprice13}",description=f"Vol:{gainprevol13}m 52 low:{gainpre52low13} 52 high:{gainpre52high13}"),
                disnake.SelectOption(label=f"1️⃣4️⃣{gainpresym14} ${gainpreprice14}",description=f"Vol:{gainprevol14}m 52 low:{gainpre52low14} 52 high:{gainpre52high14}"),
                disnake.SelectOption(label=f"1️⃣5️⃣{gainpresym15} ${gainpreprice15}", description=f"Vol:{gainprevol15}m 52 low:{gainpre52low15} 52 high:{gainpre52high15}"),
                disnake.SelectOption(label=f"1️⃣6️⃣{gainpresym16} ${gainpreprice16}", description=f"Vol:{gainprevol16}m 52 low:{gainpre52low16} 52 high:{gainpre52high16}"),
                disnake.SelectOption(label=f"1️⃣7️⃣{gainpresym17} ${gainpreprice17}", description=f"Vol:{gainprevol17}m 52 low:{gainpre52low17} 52 high:{gainpre52high17}"),
                disnake.SelectOption(label=f"1️⃣8️⃣{gainpresym18} ${gainpreprice18}", description=f"Vol:{gainprevol18}m 52 low:{gainpre52low18} 52 high:{gainpre52high18}"),
                disnake.SelectOption(label=f"1️⃣9️⃣{gainpresym19} ${gainpreprice19}", description=f"Vol:{gainprevol19}m 52 low:{gainpre52low19} 52 high:{gainpre52high19}"),
                disnake.SelectOption(label=f"2️⃣0️⃣{gainpresym20} ${gainpreprice20}", description=f"Vol:{gainprevol20}m 52 low:{gainpre52low20} 52 high:{gainpre52high20}"),
                disnake.SelectOption(label=f"2️⃣1️⃣{gainpresym21} ${gainpreprice21}", description=f"Vol:{gainprevol21}m 52 low:{gainpre52low21} 52 high:{gainpre52high21}"),
                disnake.SelectOption(label=f"2️⃣2️⃣{gainpresym22} ${gainpreprice22}", description=f"Vol:{gainprevol22}m 52 low:{gainpre52low22} 52 high:{gainpre52high22}"),
                disnake.SelectOption(label=f"2️⃣3️⃣{gainpresym23} ${gainpreprice23}", description=f"Vol:{gainprevol23}m 52 low:{gainpre52low23} 52 high:{gainpre52high23}"),
                disnake.SelectOption(label=f"2️⃣4️⃣{gainpresym24} ${gainpreprice24}", description=f"Vol:{gainprevol24}m 52 low:{gainpre52low24} 52 high:{gainpre52high24}"),



            ]
        )

    async def callback(self, interaction:disnake.ApplicationCommandInteraction):
        if self.values[0] == self.values[0]:
            await interaction.send("```py\nSoon dad ormom, soon! For now - quick display for reference~!``")




class AfterHoursLoser(disnake.ui.Select):
    def __init__(self):

        aftergainr = requests.get(url="https://quotes-gw.webullfintech.com/api/bgw/market/dropGainers?regionId=6&rankType=afterHours&pageIndex=1&pageSize=50").json()
        aftergainrdata = aftergainr['data']

        aftergain1 = aftergainrdata[0]
        gainafterticker1 = aftergain1['ticker']
        gainafterchange1 = round(float(gainafterticker1['changeRatio'])*100,ndigits=2)
        gainaftersym1 = gainafterticker1['symbol']
        gainafter52low1 = gainafterticker1['fiftyTwoWkLow']
        gainafter52high1 = gainafterticker1['fiftyTwoWkHigh']
        gainafterprice1 = gainafterticker1['close']
        gainaftervol1 = round(float(gainafterticker1['volume'])*0.000001,ndigits=2)



        aftergain2 = aftergainrdata[1]
        gainafterticker2 = aftergain2['ticker']
        gainafterchange2 = round(float(gainafterticker2['changeRatio'])*100,ndigits=2)
        gainaftersym2 = gainafterticker2['symbol']
        gainafter52low2 = gainafterticker2['fiftyTwoWkLow']
        gainafter52high2 = gainafterticker2['fiftyTwoWkHigh']
        gainafterprice2 = gainafterticker2['close']
        gainaftervol2 = round(float(gainafterticker2['volume'])*0.000001,ndigits=2)



        aftergain3 = aftergainrdata[2]
        gainafterticker3 = aftergain3['ticker']
        gainafterchange3 = round(float(gainafterticker3['changeRatio'])*100,ndigits=2)
        gainaftersym3 = gainafterticker3['symbol']
        gainafter52low3 = gainafterticker3['fiftyTwoWkLow']
        gainafter52high3 = gainafterticker3['fiftyTwoWkHigh']
        gainafterprice3 = gainafterticker3['close']
        gainaftervol3 = round(float(gainafterticker3['volume'])*0.000001,ndigits=2)



        aftergain4 = aftergainrdata[3]
        gainafterticker4 = aftergain4['ticker']
        gainafterchange4 = round(float(gainafterticker4['changeRatio'])*100,ndigits=2)
        gainaftersym4 = gainafterticker4['symbol']
        gainafter52low4 = gainafterticker4['fiftyTwoWkLow']
        gainafter52high4 = gainafterticker4['fiftyTwoWkHigh']
        gainafterprice4 = gainafterticker4['close']
        gainaftervol4 = round(float(gainafterticker4['volume'])*0.000001,ndigits=2)

        aftergain5 = aftergainrdata[4]
        gainafterticker5 = aftergain5['ticker']
        gainafterchange5 = round(float(gainafterticker5['changeRatio'])*100,ndigits=2)
        gainaftersym5 = gainafterticker5['symbol']
        gainafter52low5 = gainafterticker5['fiftyTwoWkLow']
        gainafter52high5 = gainafterticker5['fiftyTwoWkHigh']
        gainafterprice5 = gainafterticker5['close']
        gainaftervol5 = round(float(gainafterticker5['volume'])*0.000001,ndigits=2)


        aftergain6 = aftergainrdata[5]
        gainafterticker6 = aftergain6['ticker']
        gainafterchange6 = round(float(gainafterticker6['changeRatio'])*100,ndigits=2)
        gainaftersym6 = gainafterticker6['symbol']
        gainafter52low6 = gainafterticker6['fiftyTwoWkLow']
        gainafter52high6 = gainafterticker6['fiftyTwoWkHigh']
        gainafterprice6 = gainafterticker6['close']
        gainaftervol6 = round(float(gainafterticker6['volume'])*0.000001,ndigits=2)


        aftergain7 = aftergainrdata[6]
        gainafterticker7 = aftergain7['ticker']
        gainafterchange7 = round(float(gainafterticker7['changeRatio'])*100,ndigits=2)
        gainaftersym7 = gainafterticker7['symbol']
        gainafter52low7 = gainafterticker7['fiftyTwoWkLow']
        gainafter52high7 = gainafterticker7['fiftyTwoWkHigh']
        gainafterprice7 = gainafterticker7['close']
        gainaftervol7 = round(float(gainafterticker7['volume'])*0.000001,ndigits=2)


        aftergain8 = aftergainrdata[7]
        gainafterticker8 = aftergain8['ticker']
        gainafterchange8 = round(float(gainafterticker8['changeRatio'])*100,ndigits=2)
        gainaftersym8 = gainafterticker8['symbol']
        gainafter52low8 = gainafterticker8['fiftyTwoWkLow']
        gainafter52high8 = gainafterticker8['fiftyTwoWkHigh']
        gainafterprice8 = gainafterticker8['close']
        gainaftervol8 = round(float(gainafterticker8['volume'])*0.000001,ndigits=2)


        aftergain9 = aftergainrdata[8]
        gainafterticker9 = aftergain9['ticker']
        gainafterchange9 = round(float(gainafterticker9['changeRatio'])*100,ndigits=2)
        gainaftersym9 = gainafterticker9['symbol']
        gainafter52low9 = gainafterticker9['fiftyTwoWkLow']
        gainafter52high9 = gainafterticker9['fiftyTwoWkHigh']
        gainafterprice9 = gainafterticker9['close']
        gainaftervol9 = round(float(gainafterticker9['volume'])*0.000001,ndigits=2)


        aftergain10 = aftergainrdata[9]
        gainafterticker10 = aftergain10['ticker']
        gainafterchange10 = round(float(gainafterticker10['changeRatio'])*100,ndigits=2)
        gainaftersym10 = gainafterticker10['symbol']
        gainafter52low10 = gainafterticker10['fiftyTwoWkLow']
        gainafter52high10 = gainafterticker10['fiftyTwoWkHigh']
        gainafterprice10 = gainafterticker10['close']
        gainaftervol10 = round(float(gainafterticker10['volume'])*0.000001,ndigits=2)


        aftergain11 = aftergainrdata[10]
        gainafterticker11 = aftergain11['ticker']
        gainafterchange11 = round(float(gainafterticker11['changeRatio'])*100,ndigits=2)
        gainaftersym11 = gainafterticker11['symbol']
        gainafter52low11 = gainafterticker11['fiftyTwoWkLow']
        gainafter52high11 = gainafterticker11['fiftyTwoWkHigh']
        gainafterprice11 = gainafterticker11['close']
        gainaftervol11 = round(float(gainafterticker11['volume'])*0.000001,ndigits=2)


        aftergain12 = aftergainrdata[11]
        gainafterticker12 = aftergain12['ticker']
        gainafterchange12 = round(float(gainafterticker12['changeRatio'])*100,ndigits=2)
        gainaftersym12 = gainafterticker12['symbol']
        gainafter52low12 = gainafterticker12['fiftyTwoWkLow']
        gainafter52high12 = gainafterticker12['fiftyTwoWkHigh']
        gainafterprice12 = gainafterticker12['close']
        gainaftervol12 = round(float(gainafterticker12['volume'])*0.000001,ndigits=2)


        aftergain13 = aftergainrdata[12]
        gainafterticker13 = aftergain13['ticker']
        gainafterchange13 = round(float(gainafterticker13['changeRatio'])*100,ndigits=2)
        gainaftersym13 = gainafterticker13['symbol']
        gainafter52low13 = gainafterticker13['fiftyTwoWkLow']
        gainafter52high13 = gainafterticker13['fiftyTwoWkHigh']
        gainafterprice13 = gainafterticker13['close']
        gainaftervol13 = round(float(gainafterticker13['volume'])*0.000001,ndigits=2)

        aftergain14 = aftergainrdata[13]
        gainafterticker14 = aftergain14['ticker']
        gainafterchange14 = round(float(gainafterticker14['changeRatio'])*100,ndigits=2)
        gainaftersym14 = gainafterticker14['symbol']
        gainafter52low14 = gainafterticker14['fiftyTwoWkLow']
        gainafter52high14 = gainafterticker14['fiftyTwoWkHigh']
        gainafterprice14 = gainafterticker14['close']
        gainaftervol14 = round(float(gainafterticker14['volume'])*0.000001,ndigits=2)

        aftergain15 = aftergainrdata[14]
        gainafterticker15 = aftergain15['ticker']
        gainafterchange15 = round(float(gainafterticker15['changeRatio'])*100,ndigits=2)
        gainaftersym15 = gainafterticker15['symbol']
        gainafter52low15 = gainafterticker15['fiftyTwoWkLow']
        gainafter52high15 = gainafterticker15['fiftyTwoWkHigh']
        gainafterprice15 = gainafterticker15['close']
        gainaftervol15 = round(float(gainafterticker15['volume'])*0.000001,ndigits=2)


        aftergain16 = aftergainrdata[15]
        gainafterticker16 = aftergain16['ticker']
        gainafterchange16 = round(float(gainafterticker16['changeRatio'])*100,ndigits=2)
        gainaftersym16 = gainafterticker16['symbol']
        gainafter52low16 = gainafterticker16['fiftyTwoWkLow']
        gainafter52high16 = gainafterticker16['fiftyTwoWkHigh']
        gainafterprice16 = gainafterticker16['close']
        gainaftervol16 = round(float(gainafterticker16['volume'])*0.000001,ndigits=2)


        aftergain17 = aftergainrdata[16]
        gainafterticker17 = aftergain17['ticker']
        gainafterchange17 = round(float(gainafterticker17['changeRatio'])*100,ndigits=2)
        gainaftersym17 = gainafterticker17['symbol']
        gainafter52low17 = gainafterticker17['fiftyTwoWkLow']
        gainafter52high17 = gainafterticker17['fiftyTwoWkHigh']
        gainafterprice17 = gainafterticker17['close']
        gainaftervol17 = round(float(gainafterticker17['volume'])*0.000001,ndigits=2)


        aftergain18 = aftergainrdata[17]
        gainafterticker18 = aftergain18['ticker']
        gainafterchange18 = round(float(gainafterticker18['changeRatio'])*100,ndigits=2)
        gainaftersym18 = gainafterticker18['symbol']
        gainafter52low18 = gainafterticker18['fiftyTwoWkLow']
        gainafter52high18 = gainafterticker18['fiftyTwoWkHigh']
        gainafterprice18 = gainafterticker18['close']
        gainaftervol18 = round(float(gainafterticker18['volume'])*0.000001,ndigits=2)


        aftergain19 = aftergainrdata[18]
        gainafterticker19 = aftergain19['ticker']
        gainafterchange19 = round(float(gainafterticker19['changeRatio'])*100,ndigits=2)
        gainaftersym19 = gainafterticker19['symbol']
        gainafterprice19 = gainafterticker19['close']
        gainafter52low19 = gainafterticker19['fiftyTwoWkLow']
        gainafter52high19 = gainafterticker19['fiftyTwoWkHigh']
        gainaftervol19 = round(float(gainafterticker19['volume'])*0.000001,ndigits=2)


        aftergain20 = aftergainrdata[19]
        gainafterticker20 = aftergain20['ticker']
        gainafterchange20 = round(float(gainafterticker20['changeRatio'])*100,ndigits=2)
        gainaftersym20 = gainafterticker20['symbol']
        gainafterprice20 = gainafterticker20['close']
        gainafter52low20 = gainafterticker20['fiftyTwoWkLow']
        gainafter52high20 = gainafterticker20['fiftyTwoWkHigh']
        gainaftervol20 = round(float(gainafterticker20['volume'])*0.000001,ndigits=2)


        aftergain21 = aftergainrdata[20]
        gainafterticker21 = aftergain21['ticker']
        gainafterchange21 = round(float(gainafterticker21['changeRatio'])*100,ndigits=2)
        gainaftersym21 = gainafterticker21['symbol']
        gainafter52low21 = gainafterticker21['fiftyTwoWkLow']
        gainafter52high21 = gainafterticker21['fiftyTwoWkHigh']
        gainafterprice21 = gainafterticker21['close']
        gainaftervol21 = round(float(gainafterticker21['volume'])*0.000001,ndigits=2)


        aftergain22 = aftergainrdata[21]
        gainafterticker22 = aftergain22['ticker']
        gainafterchange22 = round(float(gainafterticker22['changeRatio'])*100,ndigits=2)
        gainaftersym22 = gainafterticker22['symbol']
        gainafter52low22 = gainafterticker22['fiftyTwoWkLow']
        gainafterprice22= gainafterticker22['close']
        gainafter52high22 = gainafterticker22['fiftyTwoWkHigh']
        gainaftervol22 = round(float(gainafterticker22['volume'])*0.000001,ndigits=2)


        aftergain23 = aftergainrdata[22]
        gainafterticker23 = aftergain23['ticker']
        gainafterchange23 = round(float(gainafterticker23['changeRatio'])*100,ndigits=2)
        gainaftersym23 = gainafterticker23['symbol']
        gainafter52low23 = gainafterticker23['fiftyTwoWkLow']
        gainafter52high23 = gainafterticker23['fiftyTwoWkHigh']
        gainafterprice23 = gainafterticker23['close']
        gainaftervol23 = round(float(gainafterticker23['volume'])*0.000001,ndigits=2)


        aftergain24 = aftergainrdata[23]
        gainafterticker24 = aftergain24['ticker']
        gainafterchange24 = round(float(gainafterticker24['changeRatio'])*100,ndigits=2)
        gainaftersym24 = gainafterticker24['symbol']
        gainafter52low24 = gainafterticker24['fiftyTwoWkLow']
        gainafter52high24 = gainafterticker24['fiftyTwoWkHigh']
        gainafterprice24 = gainafterticker24['close']
        gainaftervol24 = round(float(gainafterticker24['volume'])*0.000001,ndigits=2)



        super().__init__(
            placeholder="🇱 🇴 🇸 🇪 🇷 🇸  - 🇦 🇫 🇹 🇪 🇷 🇭 🇴 🇺 🇷 🇸",
           min_values=1,
           max_values=1,
            custom_id="loseah",
            options=[ 
                disnake.SelectOption(label=f"1️⃣{gainaftersym1} ${gainafterprice1}", description=f"Vol:{gainaftervol1}m 52 low:{gainafter52low1} 52 high:{gainafter52high1}"),
                disnake.SelectOption(label=f"2️⃣{gainaftersym2} ${gainafterprice2}", description=f"Vol:{gainaftervol2}m 52 low:{gainafter52low2} 52 high:{gainafter52high2}"),
                disnake.SelectOption(label=f"3️⃣{gainaftersym3} ${gainafterprice3}", description=f"Vol:{gainaftervol3}m 52 low:{gainafter52low3} 52 high:{gainafter52high3}"),
                disnake.SelectOption(label=f"4️⃣{gainaftersym4} ${gainafterprice4}", description=f"Vol:{gainaftervol4}m 52 low:{gainafter52low4} 52 high:{gainafter52high4}"),
                disnake.SelectOption(label=f"5️⃣{gainaftersym5} ${gainafterprice5}", description=f"Vol:{gainaftervol5}m52 low:{gainafter52low5} 52 high:{gainafter52high5}"),
                disnake.SelectOption(label=f"6️⃣{gainaftersym6} ${gainafterprice6}", description=f"Vol:{gainaftervol6}m 52 low:{gainafter52low6} 52 high:{gainafter52high6}"),
                disnake.SelectOption(label=f"7️⃣{gainaftersym7} ${gainafterprice7}",description=f"Vol:{gainaftervol7}m 52 low:{gainafter52low7} 52 high:{gainafter52high7}"),
                disnake.SelectOption(label=f"8️⃣{gainaftersym8} ${gainafterprice8}",description=f"Vol:{gainaftervol8}m 52 low:{gainafter52low8} 52 high:{gainafter52high8}"),
                disnake.SelectOption(label=f"9️⃣{gainaftersym9} ${gainafterprice9}",description=f"Vol:{gainaftervol9}m 52 low:{gainafter52low9} 52 high:{gainafter52high9}"),
                disnake.SelectOption(label=f"🔟{gainaftersym10} ${gainafterprice10}",description=f"Vol:{gainaftervol10}m 52 low:{gainafter52low10} 52 high:{gainafter52high10}"),
                disnake.SelectOption(label=f"1️⃣1️⃣{gainaftersym11} ${gainafterprice11}",description=f"Vol:{gainaftervol11}m 52 low:{gainafter52low11} 52 high:{gainafter52high11}"),
                disnake.SelectOption(label=f"1️⃣2️⃣{gainaftersym12} ${gainafterprice12}",description=f"Vol:{gainaftervol12}m 52 low:{gainafter52low12} 52 high:{gainafter52high12}"),
                disnake.SelectOption(label=f"1️⃣3️⃣{gainaftersym13} ${gainafterprice13}",description=f"Vol:{gainaftervol13}m 52 low:{gainafter52low13} 52 high:{gainafter52high13}"),
                disnake.SelectOption(label=f"1️⃣4️⃣{gainaftersym14} ${gainafterprice14}",description=f"Vol:{gainaftervol14}m 52 low:{gainafter52low14} 52 high:{gainafter52high14}"),
                disnake.SelectOption(label=f"1️⃣5️⃣{gainaftersym15} ${gainafterprice15}", description=f"Vol:{gainaftervol15}m 52 low:{gainafter52low15} 52 high:{gainafter52high15}"),
                disnake.SelectOption(label=f"1️⃣6️⃣{gainaftersym16} ${gainafterprice16}", description=f"Vol:{gainaftervol16}m 52 low:{gainafter52low16} 52 high:{gainafter52high16}"),
                disnake.SelectOption(label=f"1️⃣7️⃣{gainaftersym17} ${gainafterprice17}", description=f"Vol:{gainaftervol17}m 52 low:{gainafter52low17} 52 high:{gainafter52high17}"),
                disnake.SelectOption(label=f"1️⃣8️⃣{gainaftersym18} ${gainafterprice18}", description=f"Vol:{gainaftervol18}m 52 low:{gainafter52low18} 52 high:{gainafter52high18}"),
                disnake.SelectOption(label=f"1️⃣9️⃣{gainaftersym19} ${gainafterprice19}", description=f"Vol:{gainaftervol19}m 52 low:{gainafter52low19} 52 high:{gainafter52high19}"),
                disnake.SelectOption(label=f"2️⃣0️⃣{gainaftersym20} ${gainafterprice20}", description=f"Vol:{gainaftervol20}m 52 low:{gainafter52low20} 52 high:{gainafter52high20}"),
                disnake.SelectOption(label=f"2️⃣1️⃣{gainaftersym21} ${gainafterprice21}", description=f"Vol:{gainaftervol21}m 52 low:{gainafter52low21} 52 high:{gainafter52high21}"),
                disnake.SelectOption(label=f"2️⃣2️⃣{gainaftersym22} ${gainafterprice22}", description=f"Vol:{gainaftervol22}m 52 low:{gainafter52low22} 52 high:{gainafter52high22}"),
                disnake.SelectOption(label=f"2️⃣3️⃣{gainaftersym23} ${gainafterprice23}", description=f"Vol:{gainaftervol23}m 52 low:{gainafter52low23} 52 high:{gainafter52high23}"),
                disnake.SelectOption(label=f"2️⃣4️⃣{gainaftersym24} ${gainafterprice24}", description=f"Vol:{gainaftervol24}m 52 low:{gainafter52low24} 52 high:{gainafter52high24}"),



            ]
        )

    async def callback(self, interaction:disnake.ApplicationCommandInteraction):
        if self.values[0] == self.values[0]:
            await interaction.send("```py\nSoon dad ormom, soon! For now - quick display for reference~!``")    

class TopGainersView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(PremarketGainer())
        self.add_item(FiveMinuteGainer())
        self.add_item(Day1Gainer())
        self.add_item(AfterHoursGainer())



class TopLosersView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(PremarketLoser())
        self.add_item(FiveMinuteLoser())
        self.add_item(Day1Loser())
        self.add_item(AfterHoursLoser())


    
    @disnake.ui.button(label="Top 🟩 Gainers", style=disnake.ButtonStyle.grey)
    async def topmovers(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        em=disnake.Embed(title="Top 🟩 Gainers", description="```py\nChoose between top movers on the 5min timeframe, one day, pre-market, and after-hours. Can toggle between top movers and top gainers using the '🪩' button.", color=disnake.Colour.green(), url="https://www.fudstop.io")
        view = disnake.ui.View()
        try:
            view.clear_items()
            view.add_item(Day1Loser())
            view.add_item(FiveMinuteLoser())
            view.add_item(AfterHoursLoser())
            view.add_item(PremarketLoser())

        except ValueError:
            view.clear_items()
            view.add_item(Day1Loser())
            view.add_item(FiveMinuteLoser())
            view.add_item(AfterHoursLoser())
            view.add_item(PremarketLoser())

        Day1Loser.callback = lambda interaction: inter.response.edit_message(view=MarketMainView())
        FiveMinuteLoser.callback = lambda interaction: inter.response.edit_message(view=MarketMainView())
        AfterHoursLoser.callback = lambda interaction: inter.response.edit_message(view=MarketMainView())
        PremarketLoser.callback = lambda interaction: inter.response.edit_message(view=MarketMainView())

        await inter.response.edit_message(embed=em,view=view)





    @disnake.ui.button(label="High 🩸 Short Interest", style=disnake.ButtonStyle.grey)
    async def shortint(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        em=disnake.Embed(title="High 🩸 Short Interest", description="```py\nCurrently displaying the top 24 tickers with the highest amount of short interest relative to float size. These tickers can be great opportunities for share play rebounds.\n\nThis data updates every time the command is called.```", color=disnake.Colour.red(), url="https://www.fudstop.io")
        view = disnake.ui.View()
        try:
            view.clear_items()
            view.add_item(ShortInt())

        except ValueError:
            view.clear_items()
            view.add_item(ShortInt())

        ShortInt.callback = lambda interaction: inter.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view,embed=em)



    @disnake.ui.button(label="FTDs 🗓️ With T+35 Dates", style=disnake.ButtonStyle.grey)
    async def t35(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        em=disnake.Embed(title="FTDs 🗓️ With T+35 Dates", description="```py\nCurrently displaying the top 24 tickers with the highest amount of FTDs and with their respective T+35 settlement dates posted. These tickers can be great opportunities for share play rebounds just like the high short interest menu.\n\nThis data updates every time the command is called.```", color=disnake.Colour.red(), url="https://www.fudstop.io")
        view = disnake.ui.View()
        try:
            view.add_item(FTDStocksDropdown())
        except ValueError:
            view.clear_items()

            view.add_item(FTDStocksDropdown())
        FTDStocksDropdown.callback = lambda interaction: inter.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view,embed=em)




class FTDStocksDropdown(disnake.ui.Select):
    def __init__(self):
        data = client.ftd()
        self.index0 = data[0]
        self.index1 = data[1]
        self.index2 = data[2]
        self.index3 = data[3]
        self.index4 = data[4]
        self.index5 = data[5]
        self.index6 = data[6]
        self.index7 = data[7]
        self.index8 = data[8]
        self.index9 = data[9]
        self.index10 = data[10]
        self.index11 = data[11]
        self.index12 = data[12]
        self.index13 = data[13]
        self.index14 = data[14]
        self.t350 = self.index0['T+35 Date']
        self.t351 = self.index1['T+35 Date']
        self.t352 = self.index2['T+35 Date']
        self.t353 = self.index3['T+35 Date']
        self.t354 = self.index4['T+35 Date']
        self.t355 = self.index5['T+35 Date']
        self.t356 = self.index6['T+35 Date']
        self.t357 = self.index7['T+35 Date']
        self.t358 = self.index8['T+35 Date']
        self.t359 = self.index9['T+35 Date']
        self.t3510 = self.index10['T+35 Date']
        self.t3511 = self.index11['T+35 Date']
        self.t3512 = self.index12['T+35 Date']
        self.t3513 = self.index13['T+35 Date']
        self.t3514 = self.index14['T+35 Date']
        self.symbol0 = self.index0['Ticker']
        self.symbol1 = self.index1['Ticker']
        self.symbol2 = self.index2['Ticker']
        self.symbol3 = self.index3['Ticker']
        self.symbol4 = self.index4['Ticker']
        self.symbol5 = self.index5['Ticker']
        self.symbol6 = self.index6['Ticker']
        self.symbol7 = self.index7['Ticker']
        self.symbol8 = self.index8['Ticker']
        self.symbol9 = self.index9['Ticker']
        self.symbol10 = self.index10['Ticker']
        self.symbol11 = self.index11['Ticker']
        self.symbol12 = self.index12['Ticker']
        self.symbol13 = self.index13['Ticker']
        self.symbol14 = self.index14['Ticker']

        options = [
            disnake.SelectOption(label=f"{self.symbol0} | T35 🗓️ Date: {self.t350}"),
            disnake.SelectOption(label=f"{self.symbol1} | t35 🗓️ Date: {self.t351}"),
            disnake.SelectOption(label=f"{self.symbol2} | t35 🗓️ Date: {self.t352}"),
            disnake.SelectOption(label=f"{self.symbol3} | t35 🗓️ Date: {self.t353}"),
            disnake.SelectOption(label=f"{self.symbol4} | t35 🗓️ Date: {self.t354}"),
            disnake.SelectOption(label=f"{self.symbol5} | t35 🗓️ Date: {self.t355}"),
            disnake.SelectOption(label=f"{self.symbol6} | t35 🗓️ Date: {self.t356}"),
            disnake.SelectOption(label=f"{self.symbol7} | t35 🗓️ Date: {self.t357}"),
            disnake.SelectOption(label=f"{self.symbol8} | t35 🗓️ Date: {self.t358}"),
            disnake.SelectOption(label=f"{self.symbol9} | t35 🗓️ Date: {self.t359}"),
            disnake.SelectOption(label=f"{self.symbol10} | t35 🗓️ Date: {self.t3510}"),
            disnake.SelectOption(label=f"{self.symbol11} | t35 🗓️ Date: {self.t3511}"),
            disnake.SelectOption(label=f"{self.symbol12} | t35 🗓️ Date: {self.t3512}"),
            disnake.SelectOption(label=f"{self.symbol13} | t35 🗓️ Date: {self.t3513}"),
            disnake.SelectOption(label=f"{self.symbol14} | t35 🗓️ Date: {self.t3514}"),

        ]
        super().__init__(
            placeholder = "🇫 🇹 🇩 🇸",
            min_values = 1,
            max_values = 1,
            options = options
        )
    async def callback(self, interaction:disnake.MessageCommandInteraction):
        await interaction.response.defer(with_message=True)
        if self.values[0] == self.values[0]:
            em = disnake.Embed(title="🗓️ Tickers with High FTDs", description="```py\nThe tickers shown here have the most FTDs in the market - and their respective T+35 settlement dates are displayed as well. These can be lucrative profit opportunities.```", color=disnake.Colour.dark_green())
            em.add_field(name="1",value=f"```py\n{FTDStocksDropdown().symbol0} | T35 🗓️ Date: {FTDStocksDropdown().t350}```")
            em.add_field(name="2",value=f"```py\n{FTDStocksDropdown().symbol1} | T35 🗓️ Date: {FTDStocksDropdown().t351}```")
            em.add_field(name="3",value=f"```py\n{FTDStocksDropdown().symbol2} | T35 🗓️ Date: {FTDStocksDropdown().t352}```")
            em.add_field(name="4",value=f"```py\n{FTDStocksDropdown().symbol3} | T35 🗓️ Date: {FTDStocksDropdown().t353}```")
            em.add_field(name="5",value=f"```py\n{FTDStocksDropdown().symbol4} | T35 🗓️ Date: {FTDStocksDropdown().t354}```")
            em.add_field(name="6",value=f"```py\n{FTDStocksDropdown().symbol5} | T35 🗓️ Date: {FTDStocksDropdown().t355}```")
            em.add_field(name="7",value=f"```py\n{FTDStocksDropdown().symbol6} | T35 🗓️ Date: {FTDStocksDropdown().t356}```")
            em.add_field(name="8",value=f"```py\n{FTDStocksDropdown().symbol7} | T35 🗓️ Date: {FTDStocksDropdown().t357}```")
            em.add_field(name="9",value=f"```py\n{FTDStocksDropdown().symbol8} | T35 🗓️ Date: {FTDStocksDropdown().t358}```")
            em.add_field(name="10",value=f"```py\n{FTDStocksDropdown().symbol9} | T35 🗓️ Date: {FTDStocksDropdown().t359}```")
            em.add_field(name="11",value=f"```py\n{FTDStocksDropdown().symbol10} | T35 🗓️ Date: {FTDStocksDropdown().t3510}```")
            em.add_field(name="12",value=f"```py\n{FTDStocksDropdown().symbol11} | T35 🗓️ Date: {FTDStocksDropdown().t3511}```")
            em.add_field(name="13",value=f"```py\n{FTDStocksDropdown().symbol12} | T35 🗓️ Date: {FTDStocksDropdown().t3512}```")
            em.add_field(name="14",value=f"```py\n{FTDStocksDropdown().symbol13} | T35 🗓️ Date: {FTDStocksDropdown().t3513}```")
            em.add_field(name="15",value=f"```py\n{FTDStocksDropdown().symbol14} | T35 🗓️ Date: {FTDStocksDropdown().t3514}```")
            await interaction.edit_original_response(embed=em,view=MarketMainView())





class FTDStocks(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(FTDStocksDropdown())
        
    @disnake.ui.button(style=disnake.ButtonStyle.red, label="🟥Top Losers🟥")
    async def viewtswitch(self,button: disnake.ui.Button, inter: disnake.AppCmdInter):
        em = disnake.Embed(title="🟥Top Losers🟥", description=f"```py\nMarket Losers\n\nChoose between '5minute' '1day' 'premarket' and 'afterhours'\n\nData updates every time the command is called.```", color=disnake.Colour.dark_red(),url="https://www.fudstop.io")
        view = disnake.ui.View()
        try:
            view.clear_items()
            view.add_item(Day1Loser())
            view.add_item(FiveMinuteLoser())
            view.add_item(AfterHoursLoser())
            view.add_item(PremarketLoser())

        except ValueError:
            view.clear_items()
            view.add_item(Day1Loser())
            view.add_item(FiveMinuteLoser())
            view.add_item(AfterHoursLoser())
            view.add_item(PremarketLoser())

        Day1Loser().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        FiveMinuteLoser().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        AfterHoursLoser().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        PremarketLoser().callback = lambda inter: inter.response.edit_message(view=MarketMainView())

        await inter.response.edit_message(embed=em, view=view)



    @disnake.ui.button(label="Top 🟩 Gainers", style=disnake.ButtonStyle.grey)
    async def topmovers(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        em=disnake.Embed(title="Top 🟩 Gainers", description="```py\nChoose between top movers on the 5min timeframe, one day, pre-market, and after-hours. Can toggle between top movers and top gainers using the '🪩' button.```", color=disnake.Colour.green(), url="https://www.fudstop.io")
        view = disnake.ui.View()
        try:
            view.clear_items()
            view.add_item(Day1Gainer())
            view.add_item(FiveMinuteGainer())
            view.add_item(AfterHoursGainer())
            view.add_item(PremarketGainer())

        except ValueError:
            view.clear_items()
            view.add_item(Day1Gainer())
            view.add_item(FiveMinuteGainer())
            view.add_item(AfterHoursGainer())
            view.add_item(PremarketGainer())

        Day1Gainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        FiveMinuteGainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        AfterHoursGainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        PremarketGainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())

        await inter.response.edit_message(embed=em,view=view)



    @disnake.ui.button(label="High 🩸 Short Interest", style=disnake.ButtonStyle.grey)
    async def shortint(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        em=disnake.Embed(title="High 🩸 Short Interest", description="```py\nCurrently displaying the top 24 tickers with the highest amount of short interest relative to float size. These tickers can be great opportunities for share play rebounds.\n\nThis data updates every time the command is called.```", color=disnake.Colour.dark_gold(), url="https://www.fudstop.io")
        view = disnake.ui.View()
        try:
            view.add_item(ShortInt())
        except ValueError:
            view.clear_items()
            view.add_item(ShortInt())

        ShortInt().callback = lambda inter: inter.response.edit_message(view=MarketMainView())


        await inter.response.edit_message(view=view)


    @disnake.ui.button(label="FTDs 🗓️ With T+35 Dates", style=disnake.ButtonStyle.grey)
    async def t35(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        em=disnake.Embed(title="FTDs 🗓️ With T+35 Dates", description="```py\nCurrently displaying the top 24 tickers with the highest amount of FTDs and with their respective T+35 settlement dates posted. These tickers can be great opportunities for share play rebounds just like the high short interest menu.\n\nThis data updates every time the command is called.```", color=disnake.Colour.yellow(), url="https://www.fudstop.io")
        view = disnake.ui.View()
        try:
            view.add_item(FTDStocksDropdown())
        except ValueError:
            view.clear_items()
            view.add_item(FTDStocksDropdown)


        FTDStocksDropdown().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        
        await inter.response.edit_message(view=view)



class ShortIntView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(ShortInt())


    @disnake.ui.button(style=disnake.ButtonStyle.red, label="🟥Top Losers🟥")
    async def viewtswitch(self,button: disnake.ui.Button, inter: disnake.AppCmdInter):
        em = disnake.Embed(title="🟥Top Losers🟥", description=f"```py\nMarket Losers\n\nChoose between '5minute' '1day' 'premarket' and 'afterhours'\n\nData updates every time the command is called.```", color=disnake.Colour.dark_red(),url="https://www.fudstop.io")
        view = disnake.ui.View()
        try:
            view.clear_items()
            view.add_item(Day1Loser())
            view.add_item(FiveMinuteLoser())
            view.add_item(AfterHoursLoser())
            view.add_item(PremarketLoser())

        except ValueError:
            view.clear_items()
            view.add_item(Day1Gainer())
            view.add_item(FiveMinuteGainer())
            view.add_item(AfterHoursGainer())
            view.add_item(PremarketGainer())

        Day1Gainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        FiveMinuteGainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        AfterHoursGainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        PremarketGainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())

        await inter.response.edit_message(embed=em, view=view)



    @disnake.ui.button(label="Top 🟩 Gainers", style=disnake.ButtonStyle.grey)
    async def topmovers(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        em=disnake.Embed(title="Top 🟩 Gainers", description="```py\nChoose between top movers on the 5min timeframe, one day, pre-market, and after-hours. Can toggle between top movers and top gainers using the '🪩' button.", color=disnake.Colour.green(), url="https://www.fudstop.io")
        view = disnake.ui.View()
        try:
            view.clear_items()
            view.add_item(Day1Gainer())
            view.add_item(FiveMinuteGainer())
            view.add_item(AfterHoursGainer())
            view.add_item(PremarketGainer())

        except ValueError:
            view.clear_items()
            view.add_item(Day1Gainer())
            view.add_item(FiveMinuteGainer())
            view.add_item(AfterHoursGainer())
            view.add_item(PremarketGainer())

        Day1Gainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        FiveMinuteGainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        AfterHoursGainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        PremarketGainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())

        await inter.response.edit_message(embed=em,view=view)



    @disnake.ui.button(label="FTDs 🗓️ With T+35 Dates", style=disnake.ButtonStyle.grey)
    async def t35(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        em=disnake.Embed(title="FTDs 🗓️ With T+35 Dates", description="```py\nCurrently displaying the top 24 tickers with the highest amount of FTDs and with their respective T+35 settlement dates posted. These tickers can be great opportunities for share play rebounds just like the high short interest menu.\n\nThis data updates every time the command is called.```", color=disnake.Colour.red(), url="https://www.fudstop.io")
        view = disnake.ui.View()
        try:
            view.add_item(FTDStocksDropdown())
        except ValueError:
            view.clear_items()
            view.add_item(FTDStocksDropdown())



        FTDStocksDropdown().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view,embed=em)


    @disnake.ui.button(label="High 🩳 Shorts", style=disnake.ButtonStyle.grey)
    async def t35(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        em=disnake.Embed(title="High 🩳 Shorts", description="```py\nThis dropdown displays the ```", color=disnake.Colour.red(), url="https://www.fudstop.io")
        view = disnake.ui.View()
        try:
            view.add_item(ShortInt())
        except ValueError:
            view.clear_items()
            view.add_item(ShortInt())


        ShortInt().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view, embed=em)




    @disnake.ui.button(label="Top 🏃‍♀️ Movers", style=disnake.ButtonStyle.grey)
    async def toplosers(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        em=disnake.Embed(title="Top 🏃‍♀️ Movers", description="```py\nChoose between top movers on the 5min timeframe, one day, pre-market, and after-hours. Can toggle between top movers and top gainers using the '🪩' button.```", color=disnake.Colour.red(), url="https://www.fudstop.io")
        view = disnake.ui.View()
        try:
            view.add_item(Day1Gainer())
            view.add_item(PremarketGainer())
            view.add_item(AfterHoursGainer())
            view.add_item(FiveMinuteGainer())

        except ValueError:
            view.clear_items()
            view.add_item(Day1Gainer())
            view.add_item(PremarketGainer())
            view.add_item(AfterHoursGainer())
            view.add_item(FiveMinuteGainer())

        Day1Gainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        FiveMinuteGainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        AfterHoursGainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        PremarketGainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view, embed=em)


    @disnake.ui.button(style=disnake.ButtonStyle.grey, label="⛓️Top Bonds")
    async def topbonds(self,button: disnake.ui.Button, inter: disnake.AppCmdInter):
        em = disnake.Embed(title="⛓️Top Bonds", description=f"```py\nDisplays the top 15 bonds on the day.```", color=disnake.Colour.dark_teal(),url="https://www.fudstop.io")
        view = disnake.ui.View()
        try:
            view.add_item(TopBonds())
        except ValueError:
            view.clear_items()
            view.add_item(TopBonds())

        TopBonds().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(embed=em, view=view)


class TopBondsView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(TopBonds())




    @disnake.ui.button(style=disnake.ButtonStyle.red, label="🟥Top Losers🟥")
    async def viewtswitch(self,button: disnake.ui.Button, inter: disnake.AppCmdInter):
        em = disnake.Embed(title="🟥Top Losers🟥", description=f"```py\nMarket Losers\n\nChoose between '5minute' '1day' 'premarket' and 'afterhours'\n\nData updates every time the command is called.```", color=disnake.Colour.dark_red(),url="https://www.fudstop.io")
        view = disnake.ui.View()
        try:
            view.clear_items()
            view.add_item(Day1Loser())
            view.add_item(FiveMinuteLoser())
            view.add_item(AfterHoursLoser())
            view.add_item(PremarketLoser())

        except ValueError:
            view.clear_items()
            view.add_item(Day1Loser())
            view.add_item(FiveMinuteLoser())
            view.add_item(AfterHoursLoser())
            view.add_item(PremarketLoser())

        Day1Loser().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        FiveMinuteLoser().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        AfterHoursLoser().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        PremarketLoser().callback = lambda inter: inter.response.edit_message(view=MarketMainView())

        await inter.response.edit_message(embed=em, view=view)

    @disnake.ui.button(label="Top 🏃‍♀️ Movers", style=disnake.ButtonStyle.grey)
    async def toplosers(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        em=disnake.Embed(title="Top 🏃‍♀️ Movers", description="```py\nChoose between top movers on the 5min timeframe, one day, pre-market, and after-hours. Can toggle between top movers and top gainers using the '🪩' button.```", color=disnake.Colour.red(), url="https://www.fudstop.io")
        view = disnake.ui.View()
        try:
            view.add_item(Day1Gainer())
            view.add_item(PremarketGainer())
            view.add_item(AfterHoursGainer())
            view.add_item(FiveMinuteGainer())

        except ValueError:
            self.clear_items()
            view.add_item(Day1Gainer())
            view.add_item(PremarketGainer())
            view.add_item(AfterHoursGainer())
            view.add_item(FiveMinuteGainer())

        Day1Gainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        FiveMinuteGainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        AfterHoursGainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        PremarketGainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view)

    @disnake.ui.button(label="Top 🟩 Gainers", style=disnake.ButtonStyle.grey)
    async def topmovers(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        em=disnake.Embed(title="Top 🟩 Gainers", description="```py\nChoose between top movers on the 5min timeframe, one day, pre-market, and after-hours. Can toggle between top movers and top gainers using the '🪩' button.```", color=disnake.Colour.green(), url="https://www.fudstop.io")
        view = disnake.ui.View()
        try:
            view.clear_items()
            view.add_item(Day1Gainer())
            view.add_item(FiveMinuteGainer())
            view.add_item(AfterHoursGainer())
            view.add_item(PremarketGainer())

        except ValueError:
            view.clear_items()
            view.add_item(Day1Gainer())
            view.add_item(FiveMinuteGainer())
            view.add_item(AfterHoursGainer())
            view.add_item(PremarketGainer())

        Day1Gainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        FiveMinuteGainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        AfterHoursGainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        PremarketGainer().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(embed=em,view=view)



    @disnake.ui.button(label="FTDs 🗓️ With T+35 Dates", style=disnake.ButtonStyle.grey)
    async def t35(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        em=disnake.Embed(title="FTDs 🗓️ With T+35 Dates", description="```py\nCurrently displaying the top 24 tickers with the highest amount of FTDs and with their respective T+35 settlement dates posted. These tickers can be great opportunities for share play rebounds just like the high short interest menu.\n\nThis data updates every time the command is called.```", color=disnake.Colour.red(), url="https://www.fudstop.io")
        view = disnake.ui.View()
        try:
            view.clear_items()
            view.add_item(FTDStocksDropdown())
        except ValueError:
            view.clear_items()
            view.add_item(FTDStocksDropdown())


        FTDStocksDropdown().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view,embed=em)


    @disnake.ui.button(label="High 🩳 Shorts", style=disnake.ButtonStyle.grey)
    async def highshort(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        em=disnake.Embed(title="High 🩳 Shorts", description="```py\nThis dropdown displays the ```", color=disnake.Colour.red(), url="https://www.fudstop.io")
        view = disnake.ui.View()
        try:
            view.clear_items()
            view.add_item(ShortInt())
        except ValueError:
            view.clear_items()
            view.add_item(ShortInt())


        ShortInt().callback = lambda inter: inter.response.edit_message(view=MarketMainView())
        await inter.response.edit_message(view=view, embed=em)




class ShortInt(disnake.ui.Select):
    def __init__(self):
        d = client.short_interest()
        shortint1 = d[0]
        sirank1 = shortint1['Rank']
        siticker1 = shortint1['Ticker']
        sidate1 = round(float(shortint1['Short Interest'])*0.000001,ndigits=2)
        siavgvol1 = round(float(shortint1['Average Volume'])*0.000001,ndigits=2)
        sidtc1 = shortint1['Days To Cover']
        sipshort1 = round(shortint1['%Float Short'],ndigits=2)

        shortint2 = d[1]
        sirank2 = shortint2['Rank']
        siticker2 = shortint2['Ticker']
        sidate2 = round(float(shortint2['Short Interest'])*0.000001,ndigits=2)
        siavgvol2 = round(float(shortint2['Average Volume'])*0.000001,ndigits=2)
        sidtc2 = shortint2['Days To Cover']
        sipshort2 = round(shortint2['%Float Short'],ndigits=2)



        shortint3 = d[2]
        sirank3 = shortint3['Rank']
        siticker3 = shortint3['Ticker']
        sidate3 = round(float(shortint3['Short Interest'])*0.000001,ndigits=2)
        siavgvol3 = round(float(shortint3['Average Volume'])*0.000001,ndigits=2)
        sidtc3 = shortint3['Days To Cover']
        sipshort3 = round(shortint3['%Float Short'],ndigits=2)



        shortint4 = d[3]
        sirank4 = shortint4['Rank']
        siticker4 = shortint4['Ticker']
        sidate4 = round(float(shortint4['Short Interest'])*0.000001,ndigits=2)
        siavgvol4 = round(float(shortint4['Average Volume'])*0.000001,ndigits=2)
        sidtc4 = shortint4['Days To Cover']
        sipshort4 = round(shortint4['%Float Short'],ndigits=2)




        shortint5 = d[4]
        sirank5 = shortint5['Rank']
        siticker5 = shortint5['Ticker']
        sidate5 = round(float(shortint5['Short Interest'])*0.000001,ndigits=2)
        siavgvol5 = round(float(shortint5['Average Volume'])*0.000001,ndigits=2)
        sidtc5 = shortint5['Days To Cover']
        sipshort5 = round(shortint5['%Float Short'],ndigits=2)



        shortint6 = d[5]
        sirank6 = shortint6['Rank']
        siticker6 = shortint6['Ticker']
        sidate6 = round(float(shortint6['Short Interest'])*0.000001,ndigits=2)
        siavgvol6 = round(float(shortint6['Average Volume'])*0.000001,ndigits=2)
        sidtc6 = shortint6['Days To Cover']
        sipshort6 = round(shortint6['%Float Short'],ndigits=2)




        shortint7 = d[6]
        sirank7 = shortint7['Rank']
        siticker7 = shortint7['Ticker']
        sidate7 = round(float(shortint7['Short Interest'])*0.000001,ndigits=2)
        siavgvol7 = round(float(shortint7['Average Volume'])*0.000001,ndigits=2)
        sidtc7 = shortint7['Days To Cover']
        sipshort7 = round(shortint7['%Float Short'],ndigits=2)




        shortint8 = d[7]
        sirank8 = shortint8['Rank']
        siticker8 = shortint8['Ticker']
        sidate8 = round(float(shortint8['Short Interest'])*0.000001,ndigits=2)
        siavgvol8 = round(float(shortint8['Average Volume'])*0.000001,ndigits=2)
        sidtc8 = shortint8['Days To Cover']
        sipshort8 = round(shortint8['%Float Short'],ndigits=2)


        shortint9 = d[8]
        sirank9 = shortint9['Rank']
        siticker9 = shortint9['Ticker']
        sidate9 = round(float(shortint9['Short Interest'])*0.000001,ndigits=2)
        siavgvol9 = round(float(shortint9['Average Volume'])*0.000001,ndigits=2)
        sidtc9 = shortint9['Days To Cover']
        sipshort9 = round(shortint9['%Float Short'],ndigits=2)


        shortint10 = d[9]
        sirank10 = shortint10['Rank']
        siticker10 = shortint10['Ticker']
        sidate10 = round(float(shortint10['Short Interest'])*0.000001,ndigits=2)
        siavgvol10 = round(float(shortint10['Average Volume'])*0.000001,ndigits=2)
        sidtc10 = shortint10['Days To Cover']
        sipshort10 = round(shortint10['%Float Short'],ndigits=2)


        shortint11 = d[10]
        sirank11 = shortint11['Rank']
        siticker11 = shortint11['Ticker']
        sidate11 = round(float(shortint11['Short Interest'])*0.000001,ndigits=2)
        siavgvol11 = round(float(shortint11['Average Volume'])*0.000001,ndigits=2)
        sidtc11 = shortint11['Days To Cover']
        sipshort11 = round(shortint11['%Float Short'],ndigits=2)


        shortint12 = d[11]
        sirank12 = shortint12['Rank']
        siticker12 = shortint12['Ticker']
        sidate12 = round(float(shortint12['Short Interest'])*0.000001,ndigits=2)
        siavgvol12 = round(float(shortint12['Average Volume'])*0.000001,ndigits=2)
        sidtc12 = shortint12['Days To Cover']
        sipshort12 = round(shortint12['%Float Short'],ndigits=2)


        shortint13 = d[12]
        sirank13 = shortint13['Rank']
        siticker13 = shortint13['Ticker']
        sidate13 = round(float(shortint13['Short Interest'])*0.000001,ndigits=2)
        siavgvol13 = round(float(shortint13['Average Volume'])*0.000001,ndigits=2)
        sidtc13 = shortint13['Days To Cover']
        sipshort13 = round(shortint13['%Float Short'],ndigits=2)


        shortint14 = d[13]
        sirank14 = shortint14['Rank']
        siticker14 = shortint14['Ticker']
        sidate14 = round(float(shortint14['Short Interest'])*0.000001,ndigits=2)
        siavgvol14 = round(float(shortint14['Average Volume'])*0.000001,ndigits=2)
        sidtc14 = shortint14['Days To Cover']
        sipshort14 = round(shortint14['%Float Short'],ndigits=2)


        shortint15 = d[14]
        sirank15 = shortint15['Rank']
        siticker15 = shortint15['Ticker']
        sidate15 = round(float(shortint15['Short Interest'])*0.000001,ndigits=2)
        siavgvol15 = round(float(shortint15['Average Volume'])*0.000001,ndigits=2)
        sidtc15 = shortint15['Days To Cover']
        sipshort15 = round(shortint15['%Float Short'],ndigits=2)


        shortint16 = d[15]
        sirank16 = shortint16['Rank']
        siticker16 = shortint16['Ticker']
        sidate16 = round(float(shortint16['Short Interest'])*0.000001,ndigits=2)
        siavgvol16 = round(float(shortint16['Average Volume'])*0.000001,ndigits=2)
        sidtc16 = shortint16['Days To Cover']
        sipshort16 = round(shortint16['%Float Short'],ndigits=2)


        shortint17 = d[16]
        sirank17 = shortint17['Rank']
        siticker17 = shortint17['Ticker']
        sidate17 = round(float(shortint17['Short Interest'])*0.000001,ndigits=2)
        siavgvol17 = round(float(shortint17['Average Volume'])*0.000001,ndigits=2)
        sidtc17 = shortint17['Days To Cover']
        sipshort17 = round(shortint17['%Float Short'],ndigits=2)


        shortint18 = d[17]
        sirank18 = shortint18['Rank']
        siticker18 = shortint18['Ticker']
        sidate18 = round(float(shortint18['Short Interest'])*0.000001,ndigits=2)
        siavgvol18 = round(float(shortint18['Average Volume'])*0.000001,ndigits=2)
        sidtc18 = shortint18['Days To Cover']
        sipshort18 = round(shortint18['%Float Short'],ndigits=2)


        shortint19 = d[18]
        sirank19 = shortint19['Rank']
        siticker19 = shortint19['Ticker']
        sidate19 = round(float(shortint19['Short Interest'])*0.000001,ndigits=2)
        siavgvol19 = round(float(shortint19['Average Volume'])*0.000001,ndigits=2)
        sidtc19 = shortint19['Days To Cover']
        sipshort19 = round(shortint19['%Float Short'],ndigits=2)


        shortint20 = d[19]
        sirank20 = shortint20['Rank']
        siticker20 = shortint20['Ticker']
        sidate20 = round(float(shortint20['Short Interest'])*0.000001,ndigits=2)
        siavgvol20 = round(float(shortint20['Average Volume'])*0.000001,ndigits=2)
        sidtc20 = shortint20['Days To Cover']
        sipshort20 = round(shortint20['%Float Short'],ndigits=2)


        shortint21 = d[20]
        sirank21 = shortint21['Rank']
        siticker21 = shortint21['Ticker']
        sidate21 = round(float(shortint21['Short Interest'])*0.000001,ndigits=2)
        siavgvol21 = round(float(shortint21['Average Volume'])*0.000001,ndigits=2)
        sidtc21 = shortint21['Days To Cover']
        sipshort21 = round(shortint21['%Float Short'], ndigits=2)



        shortint22 = d[21]
        sirank22 = shortint22['Rank']
        siticker22 = shortint22['Ticker']
        sidate22 = round(float(shortint22['Short Interest'])*0.000001,ndigits=2)
        siavgvol22 = round(float(shortint22['Average Volume'])*0.000001,ndigits=2)
        sidtc22 = shortint22['Days To Cover']
        sipshort22 = round(shortint22['%Float Short'],ndigits=2)


        shortint23 = d[22]
        sirank23 = shortint23['Rank']
        siticker23 = shortint23['Ticker']
        sidate23 = round(float(shortint23['Short Interest'])*0.000001,ndigits=2)
        siavgvol23 = round(float(shortint23['Average Volume'])*0.000001,ndigits=2)
        sidtc23 = shortint23['Days To Cover']
        sipshort23 = round(shortint23['%Float Short'],ndigits=2)


        shortint24 = d[23]
        sirank24 = shortint24['Rank']
        siticker24 = shortint24['Ticker']
        sidate24 = round(float(shortint24['Short Interest'])*0.000001,ndigits=2)
        siavgvol24 = round(float(shortint24['Average Volume'])*0.000001,ndigits=2)
        sidtc24 = shortint24['Days To Cover']
        sipshort24 = round(shortint24['%Float Short'],ndigits=2)



        super().__init__(
            placeholder="🇭 🇮 🇬 🇭 🩳  🇸 🇭 🇴 🇷 🇹 🇸",
            min_values=1,
            max_values=1,
            custom_id="shortintsel",
            options=[ 
                disnake.SelectOption(label=f"{sirank1}| {siticker1} | {sipshort1}% short", description=f"Days to Dover: {sidtc1} | Short Interest: {sidate1} million"),
                disnake.SelectOption(label=f"{sirank2}| {siticker2} | {sipshort2}% short", description=f"Days to Dover: {sidtc2} | Short Interest: {sidate2} million"),
                disnake.SelectOption(label=f"{sirank3}| {siticker3} | {sipshort3}% short", description=f"Days to Dover: {sidtc3} | Short Interest: {sidate3} million"),
                disnake.SelectOption(label=f"{sirank4}| {siticker4} | {sipshort4}% short", description=f"Days to Dover: {sidtc4} | Short Interest: {sidate4} million"),
                disnake.SelectOption(label=f"{sirank5}| {siticker5} | {sipshort5}% short", description=f"Days to Dover: {sidtc5} | Short Interest: {sidate5} million"),
                disnake.SelectOption(label=f"{sirank6}| {siticker6} | {sipshort6}% short", description=f"Days to Dover: {sidtc6} | Short Interest: {sidate6} million"),
                disnake.SelectOption(label=f"{sirank7}| {siticker7} | {sipshort7}% short", description=f"Days to Dover: {sidtc7} | Short Interest: {sidate7} million"),
                disnake.SelectOption(label=f"{sirank8}| {siticker8} | {sipshort8}% short", description=f"Days to Dover: {sidtc8} | Short Interest: {sidate8} million"),
                disnake.SelectOption(label=f"{sirank9}| {siticker9} | {sipshort9}% short", description=f"Days to Dover: {sidtc9} | Short Interest: {sidate9} million"),
                disnake.SelectOption(label=f"{sirank10}| {siticker10} | {sipshort10}% short", description=f"Days to Dover: {sidtc10} | Short Interest: {sidate10} million"),
                disnake.SelectOption(label=f"{sirank11}| {siticker11} | {sipshort11}% short", description=f"Days to Dover: {sidtc11} | Short Interest: {sidate11} million"),
                disnake.SelectOption(label=f"{sirank12}| {siticker12} | {sipshort12}% short", description=f"Days to Dover: {sidtc12} | Short Interest: {sidate12} million"),
                disnake.SelectOption(label=f"{sirank13}| {siticker13} | {sipshort13}% short", description=f"Days to Dover: {sidtc13} | Short Interest: {sidate13} million"),
                disnake.SelectOption(label=f"{sirank14}| {siticker14} | {sipshort14}% short", description=f"Days to Dover: {sidtc14} | Short Interest: {sidate14} million"),
                disnake.SelectOption(label=f"{sirank15}| {siticker15} | {sipshort15}% short", description=f"Days to Dover: {sidtc15} | Short Interest: {sidate15} million"),
                disnake.SelectOption(label=f"{sirank16}| {siticker16} | {sipshort16}% short", description=f"Days to Dover: {sidtc16} | Short Interest: {sidate16} million"),
                disnake.SelectOption(label=f"{sirank17}| {siticker17} | {sipshort17}% short", description=f"Days to Dover: {sidtc17} | Short Interest: {sidate17} million"),
                disnake.SelectOption(label=f"{sirank18}| {siticker18} | {sipshort18}% short", description=f"Days to Dover: {sidtc18} | Short Interest: {sidate18} million"),
                disnake.SelectOption(label=f"{sirank19}| {siticker19} | {sipshort19}% short", description=f"Days to Dover: {sidtc19} | Short Interest: {sidate19} million"),
                disnake.SelectOption(label=f"{sirank20}| {siticker20} | {sipshort20}% short", description=f"Days to Dover: {sidtc20} | Short Interest: {sidate20} million"),
                disnake.SelectOption(label=f"{sirank21}| {siticker21} | {sipshort21}% short", description=f"Days to Dover: {sidtc21} | Short Interest: {sidate21} million"),
                disnake.SelectOption(label=f"{sirank22}| {siticker22} | {sipshort22}% short", description=f"Days to Dover: {sidtc22} | Short Interest: {sidate22} million"),
                disnake.SelectOption(label=f"{sirank23}| {siticker23} | {sipshort23}% short", description=f"Days to Dover: {sidtc23} | Short Interest: {sidate23} million"),
                disnake.SelectOption(label=f"{sirank24}| {siticker24} | {sipshort24}% short", description=f"Days to Dover: {sidtc24} | Short Interest: {sidate24} million"),

            ]
        )

    async def callback(self, interaction: disnake.MessageCommandInteraction):
        await interaction.response.send_message("Soon daddy !! or mom!!")



class TopBonds(disnake.ui.Select):
    def __init__(self):


        r = requests.get(url="https://quotes-gw.webullfintech.com/api/wlas/etfinder/pcFinder?topNum=15&finderId=wlas.etfinder.other&nbboLevel=false").json()
        name = r['name']
        comment = r['comment']
        tab=r['tabs']
        bonds = tab[0]
        upnum = bonds['upNum']
        down = bonds['dowoNum']
        flat = bonds['flatNum']
        print(upnum, down, flat)
        ticklist = bonds['tickerTupleList']
        ticker1 = ticklist[0]
        symbol1 = ticker1['disSymbol']
        change1 = round(float(ticker1['changeRatio'])*100,ndigits=2)
        name1 = ticker1['name']
        fiftylow1 = ticker1['fiftyTwoWkLow']
        fiftyhigh1 = ticker1['fiftyTwoWkHigh']


        ticker2 = ticklist[1]
        symbol2 = ticker2['disSymbol']
        change2 = round(float(ticker2['changeRatio'])*100,ndigits=2)
        name2 = ticker2['name']
        fiftylow2 = ticker2['fiftyTwoWkLow']
        fiftyhigh2 = ticker2['fiftyTwoWkHigh']




        ticker3 = ticklist[2]
        symbol3 = ticker3['disSymbol']
        change3 = round(float(ticker3['changeRatio'])*100,ndigits=2)
        name3 = ticker3['name']
        fiftylow3 = ticker3['fiftyTwoWkLow']
        fiftyhigh3 = ticker3['fiftyTwoWkHigh']

        ticker4 = ticklist[3]
        symbol4 = ticker4['disSymbol']
        change4 = round(float(ticker4['changeRatio'])*100,ndigits=2)
        name4 = ticker4['name']
        fiftylow4 = ticker4['fiftyTwoWkLow']
        fiftyhigh4 = ticker4['fiftyTwoWkHigh']

        ticker5 = ticklist[4]
        symbol5 = ticker5['disSymbol']
        change5 = round(float(ticker5['changeRatio'])*100,ndigits=2)
        name5 = ticker5['name']
        fiftylow5 = ticker5['fiftyTwoWkLow']
        fiftyhigh5 = ticker5['fiftyTwoWkHigh']

        ticker6 = ticklist[5]
        symbol6 = ticker6['disSymbol']
        change6 = round(float(ticker6['changeRatio'])*100,ndigits=2)
        name6 = ticker6['name']
        fiftylow6 = ticker6['fiftyTwoWkLow']
        fiftyhigh6 = ticker6['fiftyTwoWkHigh']

        ticker7 = ticklist[6]
        symbol7 = ticker7['disSymbol']
        change7 = round(float(ticker7['changeRatio'])*100,ndigits=2)
        name7 = ticker7['name']
        fiftylow7 = ticker7['fiftyTwoWkLow']
        fiftyhigh7 = ticker7['fiftyTwoWkHigh']

        ticker8 = ticklist[7]
        symbol8 = ticker8['disSymbol']
        change8 = round(float(ticker8['changeRatio'])*100,ndigits=2)
        name8 = ticker8['name']
        fiftylow8 = ticker8['fiftyTwoWkLow']
        fiftyhigh8 = ticker8['fiftyTwoWkHigh']

        ticker9 = ticklist[8]
        symbol9 = ticker9['disSymbol']
        change9 = round(float(ticker9['changeRatio'])*100,ndigits=2)
        name9 = ticker9['name']
        fiftylow9 = ticker9['fiftyTwoWkLow']
        fiftyhigh9 = ticker9['fiftyTwoWkHigh']

        ticker10 = ticklist[9]
        symbol10 = ticker10['disSymbol']
        change10 = round(float(ticker10['changeRatio'])*100,ndigits=2)
        name10 = ticker10['name']
        fiftylow10 = ticker10['fiftyTwoWkLow']
        fiftyhigh10 = ticker10['fiftyTwoWkHigh']

        ticker11 = ticklist[10]
        symbol11 = ticker11['disSymbol']
        change11 = round(float(ticker11['changeRatio'])*100,ndigits=2)
        name11 = ticker11['name']
        fiftylow11 = ticker11['fiftyTwoWkLow']
        fiftyhigh11 = ticker11['fiftyTwoWkHigh']

        ticker12 = ticklist[11]
        symbol12 = ticker12['disSymbol']
        change12 = round(float(ticker12['changeRatio'])*100,ndigits=2)
        name12 = ticker12['name']
        fiftylow12 = ticker12['fiftyTwoWkLow']
        fiftyhigh12 = ticker12['fiftyTwoWkHigh']

        ticker13 = ticklist[12]
        symbol13 = ticker13['disSymbol']
        change13 = round(float(ticker13['changeRatio'])*100,ndigits=2)
        name13 = ticker13['name']
        fiftylow13 = ticker13['fiftyTwoWkLow']
        fiftyhigh13 = ticker13['fiftyTwoWkHigh']

        ticker14 = ticklist[13]
        symbol14 = ticker14['disSymbol']
        change14 = round(float(ticker14['changeRatio'])*100,ndigits=2)
        name14 = ticker14['name']
        fiftylow14 = ticker14['fiftyTwoWkLow']
        fiftyhigh14 = ticker14['fiftyTwoWkHigh']

        ticker15 = ticklist[14]
        symbol15 = ticker15['disSymbol']
        change15 = round(float(ticker15['changeRatio'])*100,ndigits=2)
        name15 = ticker15['name']
        fiftylow15 = ticker15['fiftyTwoWkLow']
        fiftyhigh15 = ticker15['fiftyTwoWkHigh']



        ticker16 = ticklist[15]
        symbol16 = ticker16['disSymbol']
        change16 = round(float(ticker16['changeRatio'])*100,ndigits=2)
        name16 = ticker16['name']
        fiftylow16 = ticker16['fiftyTwoWkLow']
        fiftyhigh16 = ticker16['fiftyTwoWkHigh']

        ticker17 = ticklist[16]
        symbol17 = ticker17['disSymbol']
        change17 = round(float(ticker17['changeRatio'])*100,ndigits=2)
        name17 = ticker17['name']
        fiftylow17 = ticker17['fiftyTwoWkLow']
        fiftyhigh17 = ticker17['fiftyTwoWkHigh']

        ticker18 = ticklist[17]
        symbol18 = ticker18['disSymbol']
        change18 = round(float(ticker18['changeRatio'])*100,ndigits=2)
        name18 = ticker18['name']
        fiftylow18 = ticker18['fiftyTwoWkLow']
        fiftyhigh18 = ticker18['fiftyTwoWkHigh']

        ticker19 = ticklist[18]
        symbol19 = ticker19['disSymbol']
        change19 = round(float(ticker19['changeRatio'])*100,ndigits=2)
        name19 = ticker19['name']
        fiftylow19 = ticker19['fiftyTwoWkLow']
        fiftyhigh19 = ticker19['fiftyTwoWkHigh']

        ticker20 = ticklist[19]
        symbol20 = ticker20['disSymbol']
        change20 = round(float(ticker20['changeRatio'])*100,ndigits=2)
        name20 = ticker20['name']
        fiftylow20 = ticker20['fiftyTwoWkLow']
        fiftyhigh20 = ticker20['fiftyTwoWkHigh']


    

        super().__init__(
            placeholder="🇹 🇴 🅿️ ⛓️  🅱️ 🇴 🇳 🇩 🇸",
            min_values=1,
            max_values=1,
            custom_id="bondsdrop",
            options=[ 
                disnake.SelectOption(label=f"{symbol1} | Today's gain: {change1}%", description=f"Name: {name1} | 52weekLow: {fiftylow1} | 52weekHigh: {fiftyhigh1}"),
                disnake.SelectOption(label=f"{symbol2} | Today's gain: {change2}%", description=f"Name: {name2} | 52weekLow: {fiftylow2} | 52weekHigh: {fiftyhigh2}"),
                disnake.SelectOption(label=f"{symbol3} | Today's gain: {change3}%", description=f"Name: {name3} | 52weekLow: {fiftylow3} | 52weekHigh: {fiftyhigh3}"),
                disnake.SelectOption(label=f"{symbol4} | Today's gain: {change4}%", description=f"Name: {name4} | 52weekLow: {fiftylow4} | 52weekHigh: {fiftyhigh4}"),
                disnake.SelectOption(label=f"{symbol5} | Today's gain: {change5}%", description=f"Name: {name5} | 52weekLow: {fiftylow5} | 52weekHigh: {fiftyhigh5}"),
                disnake.SelectOption(label=f"{symbol6} | Today's gain: {change6}%", description=f"Name: {name6} | 52weekLow: {fiftylow6} | 52weekHigh: {fiftyhigh6}"),
                disnake.SelectOption(label=f"{symbol7} | Today's gain: {change7}%", description=f"Name: {name7} | 52weekLow: {fiftylow7} | 52weekHigh: {fiftyhigh7}"),

                disnake.SelectOption(label=f"{symbol8} | Today's gain: {change8}%", description=f"Name: {name8} | 52weekLow: {fiftylow8} | 52weekHigh: {fiftyhigh8}"),
                disnake.SelectOption(label=f"{symbol9} | Today's gain: {change9}%", description=f"Name: {name9} | 52weekLow: {fiftylow9} | 52weekHigh: {fiftyhigh9}"),
                disnake.SelectOption(label=f"{symbol10} | Today's gain: {change10}%", description=f"Name: {name10} | 52weekLow: {fiftylow10} | 52weekHigh: {fiftyhigh10}"),
                disnake.SelectOption(label=f"{symbol11} | Today's gain: {change11}%", description=f"Name: {name11} | 52weekLow: {fiftylow11} | 52weekHigh: {fiftyhigh11}"),
                disnake.SelectOption(label=f"{symbol12} | Today's gain: {change12}%", description=f"Name: {name12} | 52weekLow: {fiftylow12} | 52weekHigh: {fiftyhigh12}"),
                disnake.SelectOption(label=f"{symbol13} | Today's gain: {change13}%", description=f"Name: {name13} | 52weekLow: {fiftylow13} | 52weekHigh: {fiftyhigh13}"),
                disnake.SelectOption(label=f"{symbol14} | Today's gain: {change14}%", description=f"Name: {name14} | 52weekLow: {fiftylow14} | 52weekHigh: {fiftyhigh14}"),
                disnake.SelectOption(label=f"{symbol15} | Today's gain: {change15}%", description=f"Name: {name15} | 52weekLow: {fiftylow15} | 52weekHigh: {fiftyhigh15}"),
                disnake.SelectOption(label=f"{symbol16} | Today's gain: {change16}%", description=f"Name: {name16} | 52weekLow: {fiftylow16} | 52weekHigh: {fiftyhigh16}"),
                disnake.SelectOption(label=f"{symbol17} | Today's gain: {change17}%", description=f"Name: {name17} | 52weekLow: {fiftylow17} | 52weekHigh: {fiftyhigh17}"),
                disnake.SelectOption(label=f"{symbol18} | Today's gain: {change18}%", description=f"Name: {name18} | 52weekLow: {fiftylow18} | 52weekHigh: {fiftyhigh18}"),
                disnake.SelectOption(label=f"{symbol19} | Today's gain: {change19}%", description=f"Name: {name19} | 52weekLow: {fiftylow19} | 52weekHigh: {fiftyhigh19}"),
                disnake.SelectOption(label=f"{symbol20} | Today's gain: {change20}%", description=f"Name: {name20} | 52weekLow: {fiftylow20} | 52weekHigh: {fiftyhigh20}"),


            ]
        )


    async def callback(self, interaction: disnake.MessageCommandInteraction):
        if self.values[0] == self.values[0]:
            await interaction.send("```py\nNo functionality here yet. Stay tuned!```")



class TurnoverDrop(disnake.ui.Select):
    def __init__(self):

        topactturnover = requests.get(url="https://quotes-gw.webullfintech.com/api/wlas/ranking/topActive?regionId=6&rankType=turnover&pageIndex=1&pageSize=24").json()
        topactdata = topactturnover['data']
        topturn1 = topactdata[0]
        topturnticker1 = topturn1['ticker']
        topturnchange1 = round(float(topturn1['changeRatio'])*100,ndigits=2)
        topturnvol1 = round(float(topturnticker1['volume'])*0.000001,ndigits=2)
        topturnsym1 = topturnticker1['disSymbol']
        topturn52low1 = topturnticker1['fiftyTwoWkLow']
        topturn52high1 = topturnticker1['fiftyTwoWkHigh']
        try:
            topturnturn1 = topturnticker1['turnoverRate']
        except ValueError:
            topturnturn1 = "N/A"
        topturnprice1 = topturnturn1['close']




        topturn2 = topactdata[1]
        topturnticker2 = topturn2['ticker']
        topturnchange2 = round(float(topturn2['changeRatio'])*100,ndigits=2)
        topturnvol2 = round(float(topturnticker2['volume'])*0.000001,ndigits=2)
        topturnsym2 = topturnticker2['disSymbol']
        topturn52low2 = topturnticker2['fiftyTwoWkLow']
        topturn52high2 = topturnticker2['fiftyTwoWkHigh']
        try:
            topturnturn2 = topturnticker2['turnoverRate']
        except ValueError:
            topturnturn2 = "N/A"
        topturnprice2 = topturnturn2['close']



        topturn3 = topactdata[2]
        topturnticker3 = topturn3['ticker']
        topturnchange3 = round(float(topturn3['changeRatio'])*100,ndigits=2)
        topturnvol3 = round(float(topturnticker1['volume'])*0.000001,ndigits=2)
        topturnsym3 = topturnticker3['disSymbol']
        topturn52low3 = topturnticker3['fiftyTwoWkLow']
        topturn52high3 = topturnticker3['fiftyTwoWkHigh']
        try:
            topturnturn3 = topturnticker3['turnoverRate']
        except ValueError:
            topturnturn3 = "N/A"
        topturnprice3 = topturnturn3['close']




        topturn4 = topactdata[3]
        topturnticker4 = topturn4['ticker']
        topturnchange4 = round(float(topturn4['changeRatio'])*100,ndigits=2)
        topturnvol4 = round(float(topturnticker1['volume'])*0.000001,ndigits=2)
        topturnsym4 = topturnticker4['disSymbol']
        topturn52low4 = topturnticker4['fiftyTwoWkLow']
        topturn52high4 = topturnticker4['fiftyTwoWkHigh']
        try:
            topturnturn4 = topturnticker4['turnoverRate']
        except ValueError:
            topturnturn4 = "N/A"
        topturnprice4 = topturnturn4['close']






        topturn5 = topactdata[4]
        topturnticker5 = topturn5['ticker']
        topturnchange5 = round(float(topturn5['changeRatio'])*100,ndigits=2)
        topturnvol5 = round(float(topturnticker1['volume'])*0.000001,ndigits=2)
        topturnsym5 = topturnticker5['disSymbol']
        topturn52low5 = topturnticker5['fiftyTwoWkLow']
        topturn52high5 = topturnticker5['fiftyTwoWkHigh']
        try:
            topturnturn5 = topturnticker5['turnoverRate']
        except ValueError:
            topturnturn5 = "N/A"
        topturnprice5 = topturnturn5['close']





        topturn6 = topactdata[5]
        topturnticker6 = topturn6['ticker']
        topturnchange6 = round(float(topturn6['changeRatio'])*100,ndigits=2)
        topturnvol6 = round(float(topturnticker1['volume'])*0.000001,ndigits=2)
        topturnsym6 = topturnticker6['disSymbol']
        topturn52low6 = topturnticker6['fiftyTwoWkLow']
        topturn52high6 = topturnticker6['fiftyTwoWkHigh']
        try:
            topturnturn6 = topturnticker6['turnoverRate']
        except ValueError:
            topturnturn6 = "N/A"
        topturnprice6 = topturnturn6['close']






        topturn7 = topactdata[6]
        topturnticker7 = topturn7['ticker']
        topturnchange7 = round(float(topturn7['changeRatio'])*100,ndigits=2)
        topturnvol7 = round(float(topturnticker1['volume'])*0.000001,ndigits=2)
        topturnsym7 = topturnticker7['disSymbol']
        topturn52low7 = topturnticker7['fiftyTwoWkLow']
        topturn52high7 = topturnticker7['fiftyTwoWkHigh']
        try:
            topturnturn7 = topturnticker7['turnoverRate']
        except ValueError:
            topturnturn7 = "N/A"
        topturnprice7 = topturnturn7['close']






        topturn8 = topactdata[7]
        topturnticker8 = topturn8['ticker']
        topturnchange8 = round(float(topturn8['changeRatio'])*100,ndigits=2)
        topturnvol8 = round(float(topturnticker1['volume'])*0.000001,ndigits=2)
        topturnsym8 = topturnticker8['disSymbol']
        topturn52low8 = topturnticker8['fiftyTwoWkLow']
        topturn52high8 = topturnticker8['fiftyTwoWkHigh']
        try:
            topturnturn8 = topturnticker8['turnoverRate']
        except ValueError:
            topturnturn8 = "N/A"
        topturnprice8 = topturnturn8['close']






        topturn9 = topactdata[8]
        topturnticker9 = topturn9['ticker']
        topturnchange9 = round(float(topturn9['changeRatio'])*100,ndigits=2)
        topturnvol9 = round(float(topturnticker1['volume'])*0.000001,ndigits=2)
        topturnsym9 = topturnticker9['disSymbol']
        topturn52low9 = topturnticker9['fiftyTwoWkLow']
        topturn52high9 = topturnticker9['fiftyTwoWkHigh']
        try:
            topturnturn9 = topturnticker9['turnoverRate']
        except ValueError:
            topturnturn9 = "N/A"
        topturnprice9 = topturnturn9['close']






        topturn10 = topactdata[9]
        topturnticker10 = topturn10['ticker']
        topturnchange10 = round(float(topturn10['changeRatio'])*100,ndigits=2)
        topturnvol10 = round(float(topturnticker1['volume'])*0.000001,ndigits=2)
        topturnsym10 = topturnticker10['disSymbol']
        topturn52low10 = topturnticker10['fiftyTwoWkLow']
        topturn52high10 = topturnticker10['fiftyTwoWkHigh']
        try:
            topturnturn10 = topturnticker10['turnoverRate']
        except ValueError:
            topturnturn10 = "N/A"
        topturnprice10 = topturnturn10['close']






        topturn11 = topactdata[10]
        topturnticker11 = topturn11['ticker']
        topturnchange11 = round(float(topturn11['changeRatio'])*100,ndigits=2)
        topturnvol11 = round(float(topturnticker1['volume'])*0.000001,ndigits=2)
        topturnsym11 = topturnticker11['disSymbol']
        topturn52low11 = topturnticker11['fiftyTwoWkLow']
        topturn52high11 = topturnticker11['fiftyTwoWkHigh']
        try:
            topturnturn11 = topturnticker11['turnoverRate']
        except ValueError:
            topturnturn11 = "N/A"
        topturnprice11 = topturnturn11['close']






        topturn12 = topactdata[11]
        topturnticker12 = topturn12['ticker']
        topturnchange12 = round(float(topturn12['changeRatio'])*100,ndigits=2)
        topturnvol12 = round(float(topturnticker1['volume'])*0.000001,ndigits=2)
        topturnsym12 = topturnticker12['disSymbol']
        topturn52low12 = topturnticker12['fiftyTwoWkLow']
        topturn52high12 = topturnticker12['fiftyTwoWkHigh']
        try:
            topturnturn12 = topturnticker12['turnoverRate']
        except ValueError:
            topturnturn12 = "N/A"
        topturnprice12 = topturnturn12['close']






        topturn13 = topactdata[12]
        topturnticker13 = topturn13['ticker']
        topturnchange13 = round(float(topturn13['changeRatio'])*100,ndigits=2)
        topturnvol13 = round(float(topturnticker1['volume'])*0.000001,ndigits=2)
        topturnsym13 = topturnticker13['disSymbol']
        topturn52low13 = topturnticker13['fiftyTwoWkLow']
        topturn52high13 = topturnticker13['fiftyTwoWkHigh']
        try:
            topturnturn13 = topturnticker13['turnoverRate']
        except ValueError:
            topturnturn13 = "N/A"
        topturnprice13 = topturnturn13['close']





        topturn14 = topactdata[13]
        topturnticker14 = topturn14['ticker']
        topturnchange14 = round(float(topturn14['changeRatio'])*100,ndigits=2)
        topturnvol14 = round(float(topturnticker1['volume'])*0.000001,ndigits=2)
        topturnsym14 = topturnticker14['disSymbol']
        topturn52low14 = topturnticker14['fiftyTwoWkLow']
        topturn52high14 = topturnticker14['fiftyTwoWkHigh']
        try:
            topturnturn14 = topturnticker14['turnoverRate']
        except ValueError:
            topturnturn14 = "N/A"
        topturnprice14 = topturnturn14['close']





        topturn15 = topactdata[14]
        topturnticker15 = topturn15['ticker']
        topturnchange15 = round(float(topturn15['changeRatio'])*100,ndigits=2)
        topturnvol15 = round(float(topturnticker1['volume'])*0.000001,ndigits=2)
        topturnsym15 = topturnticker15['disSymbol']
        topturn52low15 = topturnticker15['fiftyTwoWkLow']
        topturn52high15 = topturnticker15['fiftyTwoWkHigh']
        try:
            topturnturn15 = topturnticker15['turnoverRate']
        except ValueError:
            topturnturn15 = "N/A"
        topturnprice15 = topturnturn15['close']






        topturn16 = topactdata[15]
        topturnticker16 = topturn16['ticker']
        topturnchange16 = round(float(topturn16['changeRatio'])*100,ndigits=2)
        topturnvol16 = round(float(topturnticker1['volume'])*0.000001,ndigits=2)
        topturnsym16 = topturnticker16['disSymbol']
        topturn52low16 = topturnticker16['fiftyTwoWkLow']
        topturn52high16 = topturnticker16['fiftyTwoWkHigh']
        try:
            topturnturn16 = topturnticker16['turnoverRate']
        except ValueError:
            topturnturn16 = "N/A"
        topturnprice16 = topturnturn16['close']





        topturn17 = topactdata[16]
        topturnticker17 = topturn17['ticker']
        topturnchange17 = round(float(topturn17['changeRatio'])*100,ndigits=2)
        topturnvol17 = round(float(topturnticker1['volume'])*0.000001,ndigits=2)
        topturnsym17 = topturnticker17['disSymbol']
        topturn52low17 = topturnticker17['fiftyTwoWkLow']
        topturn52high17 = topturnticker17['fiftyTwoWkHigh']
        try:
            topturnturn17 = topturnticker17['turnoverRate']
        except ValueError:
            topturnturn17 = "N/A"
        topturnprice17 = topturnturn17['close']






        topturn18 = topactdata[17]
        topturnticker18 = topturn18['ticker']
        topturnchange18 = round(float(topturn18['changeRatio'])*100,ndigits=2)
        topturnvol18 = round(float(topturnticker1['volume'])*0.000001,ndigits=2)
        topturnsym18 = topturnticker18['disSymbol']
        topturn52low18 = topturnticker18['fiftyTwoWkLow']
        topturn52high18 = topturnticker18['fiftyTwoWkHigh']
        try:
            topturnturn18 = topturnticker18['turnoverRate']
        except ValueError:
            topturnturn18 = "N/A"
        topturnprice18 = topturnturn18['close']





        topturn19 = topactdata[18]
        topturnticker19 = topturn19['ticker']
        topturnchange19 = round(float(topturn19['changeRatio'])*100,ndigits=2)
        topturnvol19 = round(float(topturnticker1['volume'])*0.000001,ndigits=2)
        topturnsym19 = topturnticker19['disSymbol']
        topturn52low19 = topturnticker19['fiftyTwoWkLow']
        topturn52high19 = topturnticker19['fiftyTwoWkHigh']
        try:
            topturnturn19 = topturnticker19['turnoverRate']
        except ValueError:
            topturnturn19 = "N/A"
        topturnprice19 = topturnturn19['close']





        topturn20 = topactdata[19]
        topturnticker20 = topturn20['ticker']
        topturnchange20 = round(float(topturn20['changeRatio'])*100,ndigits=2)
        topturnvol20 = round(float(topturnticker1['volume'])*0.000001,ndigits=2)
        topturnsym20 = topturnticker20['disSymbol']
        topturn52low20 = topturnticker20['fiftyTwoWkLow']
        topturn52high20 = topturnticker20['fiftyTwoWkHigh']
        try:
            topturnturn20 = topturnticker20['turnoverRate']
        except ValueError:
            topturnturn20 = "N/A"
        topturnprice20 = topturnturn20['close']





        topturn21 = topactdata[20]
        topturnticker21 = topturn21['ticker']
        topturnchange21 = round(float(topturn21['changeRatio'])*100,ndigits=2)
        topturnvol21 = round(float(topturnticker1['volume'])*0.000001,ndigits=2)
        topturnsym21 = topturnticker21['disSymbol']
        topturn52low21 = topturnticker21['fiftyTwoWkLow']
        topturn52high21 = topturnticker21['fiftyTwoWkHigh']
        try:
            topturnturn21 = topturnticker21['turnoverRate']
        except ValueError:
            topturnturn21 = "N/A"
        topturnprice21 = topturnturn21['close']





        topturn22 = topactdata[21]
        topturnticker22 = topturn22['ticker']
        topturnchange22 = round(float(topturn22['changeRatio'])*100,ndigits=2)
        topturnvol22 = round(float(topturnticker1['volume'])*0.000001,ndigits=2)
        topturnsym22 = topturnticker22['disSymbol']
        topturn52low22 = topturnticker22['fiftyTwoWkLow']
        topturn52high22 = topturnticker22['fiftyTwoWkHigh']
        try:
            topturnturn22 = topturnticker22['turnoverRate']
        except ValueError:
            topturnturn22 = "N/A"
        topturnprice22 = topturnturn22['close']





        topturn23 = topactdata[22]
        topturnticker23 = topturn23['ticker']
        topturnchange23 = round(float(topturn23['changeRatio'])*100,ndigits=2)
        topturnvol23 = round(float(topturnticker1['volume'])*0.000001,ndigits=2)
        topturnsym23 = topturnticker23['disSymbol']
        topturn52low23 = topturnticker23['fiftyTwoWkLow']
        topturn52high23 = topturnticker23['fiftyTwoWkHigh']
        try:
            topturnturn23 = topturnticker23['turnoverRate']
        except ValueError:
            topturnturn23 = "N/A"
        topturnprice23 = topturnturn23['close']



        topturn24 = topactdata[23]
        topturnticker24 = topturn24['ticker']
        topturnchange24 = round(float(topturn24['changeRatio'])*100,ndigits=2)
        topturnvol24 = round(float(topturnticker1['volume'])*0.000001,ndigits=2)
        topturnsym24 = topturnticker24['disSymbol']
        topturn52low24 = topturnticker24['fiftyTwoWkLow']
        topturn52high24 = topturnticker24['fiftyTwoWkHigh']
        try:
            topturnturn24 = topturnticker24['turnoverRate']
        except ValueError:
            topturnturn24 = "N/A"
        topturnprice24 = topturnturn24['close']



        super().__init__(
            placeholder = "🇹 🇴 🇵 🛞 🇹 🇺 🇷 🇳 🇴 🇻 🇪 🇷",
            min_values=1,
            max_values=1,
            custom_id="turnoverdrop",
            options=[ 
                disnake.SelectOption(label=f"{topturnsym1} | Price: {topturnprice1} | Vol: {topturnvol1}", description=f"Turnover: {topturnturn1} | 52wk Low: {topturn52low1} | 52wk High: {topturn52high1}"),
                disnake.SelectOption(label=f"{topturnsym2} | Price: {topturnprice2} | Vol: {topturnvol2}", description=f"Turnover: {topturnturn2} | 52wk Low: {topturn52low2} | 52wk High: {topturn52high2}"),
                disnake.SelectOption(label=f"{topturnsym3} | Price: {topturnprice3} | Vol: {topturnvol3}", description=f"Turnover: {topturnturn3} | 52wk Low: {topturn52low3} | 52wk High: {topturn52high3}"),
                disnake.SelectOption(label=f"{topturnsym4} | Price: {topturnprice4} | Vol: {topturnvol4}", description=f"Turnover: {topturnturn4} | 52wk Low: {topturn52low4} | 52wk High: {topturn52high4}"),
                disnake.SelectOption(label=f"{topturnsym5} | Price: {topturnprice5} | Vol: {topturnvol5}", description=f"Turnover: {topturnturn5} | 52wk Low: {topturn52low5} | 52wk High: {topturn52high5}"),
                disnake.SelectOption(label=f"{topturnsym6} | Price: {topturnprice6} | Vol: {topturnvol6}", description=f"Turnover: {topturnturn6} | 52wk Low: {topturn52low6} | 52wk High: {topturn52high6}"),
                disnake.SelectOption(label=f"{topturnsym7} | Price: {topturnprice7} | Vol: {topturnvol7}", description=f"Turnover: {topturnturn7} | 52wk Low: {topturn52low7} | 52wk High: {topturn52high7}"),
                disnake.SelectOption(label=f"{topturnsym8} | Price: {topturnprice8} | Vol: {topturnvol8}", description=f"Turnover: {topturnturn8} | 52wk Low: {topturn52low8} | 52wk High: {topturn52high8}"),
                disnake.SelectOption(label=f"{topturnsym9} | Price: {topturnprice9} | Vol: {topturnvol9}", description=f"Turnover: {topturnturn9} | 52wk Low: {topturn52low9} | 52wk High: {topturn52high9}"),
                disnake.SelectOption(label=f"{topturnsym10} | Price: {topturnprice10} | Vol: {topturnvol10}", description=f"Turnover: {topturnturn10} | 52wk Low: {topturn52low10} | 52wk High: {topturn52high10}"),
                disnake.SelectOption(label=f"{topturnsym11} | Price: {topturnprice11} | Vol: {topturnvol11}", description=f"Turnover: {topturnturn11} | 52wk Low: {topturn52low11} | 52wk High: {topturn52high11}"),
                disnake.SelectOption(label=f"{topturnsym12} | Price: {topturnprice12} | Vol: {topturnvol12}", description=f"Turnover: {topturnturn12} | 52wk Low: {topturn52low12} | 52wk High: {topturn52high12}"),
                disnake.SelectOption(label=f"{topturnsym13} | Price: {topturnprice13} | Vol: {topturnvol13}", description=f"Turnover: {topturnturn13} | 52wk Low: {topturn52low13} | 52wk High: {topturn52high13}"),
                disnake.SelectOption(label=f"{topturnsym14} | Price: {topturnprice14} | Vol: {topturnvol14}", description=f"Turnover: {topturnturn14} | 52wk Low: {topturn52low14} | 52wk High: {topturn52high14}"),
                disnake.SelectOption(label=f"{topturnsym15} | Price: {topturnprice15} | Vol: {topturnvol15}", description=f"Turnover: {topturnturn15} | 52wk Low: {topturn52low15} | 52wk High: {topturn52high15}"),
                disnake.SelectOption(label=f"{topturnsym16} | Price: {topturnprice16} | Vol: {topturnvol16}", description=f"Turnover: {topturnturn16} | 52wk Low: {topturn52low16} | 52wk High: {topturn52high16}"),
                disnake.SelectOption(label=f"{topturnsym17} | Price: {topturnprice17} | Vol: {topturnvol17}", description=f"Turnover: {topturnturn17} | 52wk Low: {topturn52low17} | 52wk High: {topturn52high17}"),
                disnake.SelectOption(label=f"{topturnsym18} | Price: {topturnprice18} | Vol: {topturnvol18}", description=f"Turnover: {topturnturn18} | 52wk Low: {topturn52low18} | 52wk High: {topturn52high18}"),
                disnake.SelectOption(label=f"{topturnsym19} | Price: {topturnprice19} | Vol: {topturnvol19}", description=f"Turnover: {topturnturn19} | 52wk Low: {topturn52low19} | 52wk High: {topturn52high19}"),
                disnake.SelectOption(label=f"{topturnsym20} | Price: {topturnprice20} | Vol: {topturnvol20}", description=f"Turnover: {topturnturn20} | 52wk Low: {topturn52low20} | 52wk High: {topturn52high20}"),
                disnake.SelectOption(label=f"{topturnsym21} | Price: {topturnprice21} | Vol: {topturnvol21}", description=f"Turnover: {topturnturn21} | 52wk Low: {topturn52low21} | 52wk High: {topturn52high21}"),
                disnake.SelectOption(label=f"{topturnsym22} | Price: {topturnprice22} | Vol: {topturnvol22}", description=f"Turnover: {topturnturn22} | 52wk Low: {topturn52low22} | 52wk High: {topturn52high22}"),
                disnake.SelectOption(label=f"{topturnsym23} | Price: {topturnprice23} | Vol: {topturnvol23}", description=f"Turnover: {topturnturn23} | 52wk Low: {topturn52low23} | 52wk High: {topturn52high23}"),
                disnake.SelectOption(label=f"{topturnsym24} | Price: {topturnprice24} | Vol: {topturnvol24}", description=f"Turnover: {topturnturn24} | 52wk Low: {topturn52low24} | 52wk High: {topturn52high24}"),
            ]
        )
    async def callback(self, interaction: disnake.MessageCommandInteraction):
        if self.values[0] == self.values[0]:
            await interaction.response.edit_message(view=MarketMainView())


class TopTurnView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(TurnoverDrop())



    @disnake.ui.button(label="🔙",style=disnake.ButtonStyle.red)
    async def back(self, inter: disnake.AppCommandInteraction):
        await inter.response.edit_message(view=MarketMainView())

class TopVolumeView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(TopVolume())


    @disnake.ui.button(label="🔙",style=disnake.ButtonStyle.red)
    async def back(self, inter: disnake.AppCommandInteraction):
        await inter.response.edit_message(view=MarketMainView())


class TopVolume(disnake.ui.Select):
    def __init__(self):

        topactvol = requests.get(url="https://quotes-gw.webullfintech.com/api/wlas/ranking/topActive?regionId=6&rankType=volume&pageIndex=1&pageSize=24").json()
        topactvoldata = topactvol['data']
        topvol1 = topactvoldata[0]
        topvolticker1 = topvol1['ticker']
        try:
            topvolchange1 = round(float(topvol1['changeRatio'])*100,ndigits=2)
        except KeyError:
            topvolchange1 = "N/A"
        topvolvol1 = round(float(topvolticker1['volume'])*0.000001,ndigits=2)
        topvolsym1 = topvolticker1['disSymbol']
        topvol52low1 = topvolticker1['fiftyTwoWkLow']
        topvol52high1 = topvolticker1['fiftyTwoWkHigh']
        try:
            topvolturn1 = topvolticker1['turnoverRate']
        except ValueError:
            topvolturn1 = "N/A"
        topvolprice1 = topvolturn1['close']




        topvol2 = topactvoldata[1]
        topvolticker2 = topvol2['ticker']
        topvolchange2 = round(float(topvol2['changeRatio'])*100,ndigits=2)
        topvolvol2 = round(float(topvolticker2['volume'])*0.000001,ndigits=2)
        topvolsym2 = topvolticker2['disSymbol']
        topvol52low2 = topvolticker2['fiftyTwoWkLow']
        topvol52high2 = topvolticker2['fiftyTwoWkHigh']
        try:
            topvolturn2 = topvolticker2['turnoverRate']
        except ValueError:
            topvolturn2 = "N/A"
        topvolprice2 = topvolturn2['close']



        topvol3 = topactvoldata[2]
        topvolticker3 = topvol3['ticker']
        topvolchange3 = round(float(topvol3['changeRatio'])*100,ndigits=2)
        topvolvol3 = round(float(topvolticker1['volume'])*0.000001,ndigits=2)
        topvolsym3 = topvolticker3['disSymbol']
        topvol52low3 = topvolticker3['fiftyTwoWkLow']
        topvol52high3 = topvolticker3['fiftyTwoWkHigh']
        try:
            topvolturn3 = topvolticker3['turnoverRate']
        except ValueError:
            topvolturn3 = "N/A"
        topvolprice3 = topvolturn3['close']




        topvol4 = topactvoldata[3]
        topvolticker4 = topvol4['ticker']
        topvolchange4 = round(float(topvol4['changeRatio'])*100,ndigits=2)
        topvolvol4 = round(float(topvolticker1['volume'])*0.000001,ndigits=2)
        topvolsym4 = topvolticker4['disSymbol']
        topvol52low4 = topvolticker4['fiftyTwoWkLow']
        topvol52high4 = topvolticker4['fiftyTwoWkHigh']
        try:
            topvolturn4 = topvolticker4['turnoverRate']
        except ValueError:
            topvolturn4 = "N/A"
        topvolprice4 = topvolturn4['close']






        topvol5 = topactvoldata[4]
        topvolticker5 = topvol5['ticker']
        topvolchange5 = round(float(topvol5['changeRatio'])*100,ndigits=2)
        topvolvol5 = round(float(topvolticker1['volume'])*0.000001,ndigits=2)
        topvolsym5 = topvolticker5['disSymbol']
        topvol52low5 = topvolticker5['fiftyTwoWkLow']
        topvol52high5 = topvolticker5['fiftyTwoWkHigh']
        try:
            topvolturn5 = topvolticker5['turnoverRate']
        except ValueError:
            topvolturn5 = "N/A"
        topvolprice5 = topvolturn5['close']





        topvol6 = topactvoldata[5]
        topvolticker6 = topvol6['ticker']
        topvolchange6 = round(float(topvol6['changeRatio'])*100,ndigits=2)
        topvolvol6 = round(float(topvolticker1['volume'])*0.000001,ndigits=2)
        topvolsym6 = topvolticker6['disSymbol']
        topvol52low6 = topvolticker6['fiftyTwoWkLow']
        topvol52high6 = topvolticker6['fiftyTwoWkHigh']
        try:
            topvolturn6 = topvolticker6['turnoverRate']
        except ValueError:
            topvolturn6 = "N/A"
        topvolprice6 = topvolturn6['close']






        topvol7 = topactvoldata[6]
        topvolticker7 = topvol7['ticker']
        topvolchange7 = round(float(topvol7['changeRatio'])*100,ndigits=2)
        topvolvol7 = round(float(topvolticker1['volume'])*0.000001,ndigits=2)
        topvolsym7 = topvolticker7['disSymbol']
        topvol52low7 = topvolticker7['fiftyTwoWkLow']
        topvol52high7 = topvolticker7['fiftyTwoWkHigh']
        try:
            topvolturn7 = topvolticker7['turnoverRate']
        except ValueError:
            topvolturn7 = "N/A"
        topvolprice7 = topvolturn7['close']






        topvol8 = topactvoldata[7]
        topvolticker8 = topvol8['ticker']
        topvolchange8 = round(float(topvol8['changeRatio'])*100,ndigits=2)
        topvolvol8 = round(float(topvolticker1['volume'])*0.000001,ndigits=2)
        topvolsym8 = topvolticker8['disSymbol']
        topvol52low8 = topvolticker8['fiftyTwoWkLow']
        topvol52high8 = topvolticker8['fiftyTwoWkHigh']
        try:
            topvolturn8 = topvolticker8['turnoverRate']
        except ValueError:
            topvolturn8 = "N/A"
        topvolprice8 = topvolturn8['close']






        topvol9 = topactvoldata[8]
        topvolticker9 = topvol9['ticker']
        topvolchange9 = round(float(topvol9['changeRatio'])*100,ndigits=2)
        topvolvol9 = round(float(topvolticker1['volume'])*0.000001,ndigits=2)
        topvolsym9 = topvolticker9['disSymbol']
        topvol52low9 = topvolticker9['fiftyTwoWkLow']
        topvol52high9 = topvolticker9['fiftyTwoWkHigh']
        try:
            topvolturn9 = topvolticker9['turnoverRate']
        except ValueError:
            topvolturn9 = "N/A"
        topvolprice9 = topvolturn9['close']






        topvol10 = topactvoldata[9]
        topvolticker10 = topvol10['ticker']
        topvolchange10 = round(float(topvol10['changeRatio'])*100,ndigits=2)
        topvolvol10 = round(float(topvolticker1['volume'])*0.000001,ndigits=2)
        topvolsym10 = topvolticker10['disSymbol']
        topvol52low10 = topvolticker10['fiftyTwoWkLow']
        topvol52high10 = topvolticker10['fiftyTwoWkHigh']
        try:
            topvolturn10 = topvolticker10['turnoverRate']
        except ValueError:
            topvolturn10 = "N/A"
        topvolprice10 = topvolturn10['close']






        topvol11 = topactvoldata[10]
        topvolticker11 = topvol11['ticker']
        topvolchange11 = round(float(topvol11['changeRatio'])*100,ndigits=2)
        topvolvol11 = round(float(topvolticker1['volume'])*0.000001,ndigits=2)
        topvolsym11 = topvolticker11['disSymbol']
        topvol52low11 = topvolticker11['fiftyTwoWkLow']
        topvol52high11 = topvolticker11['fiftyTwoWkHigh']
        try:
            topvolturn11 = topvolticker11['turnoverRate']
        except ValueError:
            topvolturn11 = "N/A"
        topvolprice11 = topvolturn11['close']






        topvol12 = topactvoldata[11]
        topvolticker12 = topvol12['ticker']
        topvolchange12 = round(float(topvol12['changeRatio'])*100,ndigits=2)
        topvolvol12 = round(float(topvolticker1['volume'])*0.000001,ndigits=2)
        topvolsym12 = topvolticker12['disSymbol']
        topvol52low12 = topvolticker12['fiftyTwoWkLow']
        topvol52high12 = topvolticker12['fiftyTwoWkHigh']
        try:
            topvolturn12 = topvolticker12['turnoverRate']
        except ValueError:
            topvolturn12 = "N/A"
        topvolprice12 = topvolturn12['close']






        topvol13 = topactvoldata[12]
        topvolticker13 = topvol13['ticker']
        topvolchange13 = round(float(topvol13['changeRatio'])*100,ndigits=2)
        topvolvol13 = round(float(topvolticker1['volume'])*0.000001,ndigits=2)
        topvolsym13 = topvolticker13['disSymbol']
        topvol52low13 = topvolticker13['fiftyTwoWkLow']
        topvol52high13 = topvolticker13['fiftyTwoWkHigh']
        try:
            topvolturn13 = topvolticker13['turnoverRate']
        except ValueError:
            topvolturn13 = "N/A"
        topvolprice13 = topvolturn13['close']





        topvol14 = topactvoldata[13]
        topvolticker14 = topvol14['ticker']
        topvolchange14 = round(float(topvol14['changeRatio'])*100,ndigits=2)
        topvolvol14 = round(float(topvolticker1['volume'])*0.000001,ndigits=2)
        topvolsym14 = topvolticker14['disSymbol']
        topvol52low14 = topvolticker14['fiftyTwoWkLow']
        topvol52high14 = topvolticker14['fiftyTwoWkHigh']
        try:
            topvolturn14 = topvolticker14['turnoverRate']
        except ValueError:
            topvolturn14 = "N/A"
        topvolprice14 = topvolturn14['close']





        topvol15 = topactvoldata[14]
        topvolticker15 = topvol15['ticker']
        topvolchange15 = round(float(topvol15['changeRatio'])*100,ndigits=2)
        topvolvol15 = round(float(topvolticker1['volume'])*0.000001,ndigits=2)
        topvolsym15 = topvolticker15['disSymbol']
        topvol52low15 = topvolticker15['fiftyTwoWkLow']
        topvol52high15 = topvolticker15['fiftyTwoWkHigh']
        try:
            topvolturn15 = topvolticker15['turnoverRate']
        except ValueError:
            topvolturn15 = "N/A"
        topvolprice15 = topvolturn15['close']






        topvol16 = topactvoldata[15]
        topvolticker16 = topvol16['ticker']
        topvolchange16 = round(float(topvol16['changeRatio'])*100,ndigits=2)
        topvolvol16 = round(float(topvolticker1['volume'])*0.000001,ndigits=2)
        topvolsym16 = topvolticker16['disSymbol']
        topvol52low16 = topvolticker16['fiftyTwoWkLow']
        topvol52high16 = topvolticker16['fiftyTwoWkHigh']
        try:
            topvolturn16 = topvolticker16['turnoverRate']
        except ValueError:
            topvolturn16 = "N/A"
        topvolprice16 = topvolturn16['close']





        topvol17 = topactvoldata[16]
        topvolticker17 = topvol17['ticker']
        topvolchange17 = round(float(topvol17['changeRatio'])*100,ndigits=2)
        topvolvol17 = round(float(topvolticker1['volume'])*0.000001,ndigits=2)
        topvolsym17 = topvolticker17['disSymbol']
        topvol52low17 = topvolticker17['fiftyTwoWkLow']
        topvol52high17 = topvolticker17['fiftyTwoWkHigh']
        try:
            topvolturn17 = topvolticker17['turnoverRate']
        except ValueError:
            topvolturn17 = "N/A"
        topvolprice17 = topvolturn17['close']






        topvol18 = topactvoldata[17]
        topvolticker18 = topvol18['ticker']
        topvolchange18 = round(float(topvol18['changeRatio'])*100,ndigits=2)
        topvolvol18 = round(float(topvolticker1['volume'])*0.000001,ndigits=2)
        topvolsym18 = topvolticker18['disSymbol']
        topvol52low18 = topvolticker18['fiftyTwoWkLow']
        topvol52high18 = topvolticker18['fiftyTwoWkHigh']
        try:
            topvolturn18 = topvolticker18['turnoverRate']
        except ValueError:
            topvolturn18 = "N/A"
        topvolprice18 = topvolturn18['close']





        topvol19 = topactvoldata[18]
        topvolticker19 = topvol19['ticker']
        topvolchange19 = round(float(topvol19['changeRatio'])*100,ndigits=2)
        topvolvol19 = round(float(topvolticker1['volume'])*0.000001,ndigits=2)
        topvolsym19 = topvolticker19['disSymbol']
        topvol52low19 = topvolticker19['fiftyTwoWkLow']
        topvol52high19 = topvolticker19['fiftyTwoWkHigh']
        try:
            topvolturn19 = topvolticker19['turnoverRate']
        except ValueError:
            topvolturn19 = "N/A"
        topvolprice19 = topvolturn19['close']





        topvol20 = topactvoldata[19]
        topvolticker20 = topvol20['ticker']
        topvolchange20 = round(float(topvol20['changeRatio'])*100,ndigits=2)
        topvolvol20 = round(float(topvolticker1['volume'])*0.000001,ndigits=2)
        topvolsym20 = topvolticker20['disSymbol']
        topvol52low20 = topvolticker20['fiftyTwoWkLow']
        topvol52high20 = topvolticker20['fiftyTwoWkHigh']
        try:
            topvolturn20 = topvolticker20['turnoverRate']
        except ValueError:
            topvolturn20 = "N/A"
        topvolprice20 = topvolturn20['close']





        topvol21 = topactvoldata[20]
        topvolticker21 = topvol21['ticker']
        topvolchange21 = round(float(topvol21['changeRatio'])*100,ndigits=2)
        topvolvol21 = round(float(topvolticker1['volume'])*0.000001,ndigits=2)
        topvolsym21 = topvolticker21['disSymbol']
        topvol52low21 = topvolticker21['fiftyTwoWkLow']
        topvol52high21 = topvolticker21['fiftyTwoWkHigh']
        try:
            topvolturn21 = topvolticker21['turnoverRate']
        except ValueError:
            topvolturn21 = "N/A"
        topvolprice21 = topvolturn21['close']





        topvol22 = topactvoldata[21]
        topvolticker22 = topvol22['ticker']
        topvolchange22 = round(float(topvol22['changeRatio'])*100,ndigits=2)
        topvolvol22 = round(float(topvolticker1['volume'])*0.000001,ndigits=2)
        topvolsym22 = topvolticker22['disSymbol']
        topvol52low22 = topvolticker22['fiftyTwoWkLow']
        topvol52high22 = topvolticker22['fiftyTwoWkHigh']
        try:
            topvolturn22 = topvolticker22['turnoverRate']
        except ValueError:
            topvolturn22 = "N/A"
        topvolprice22 = topvolturn22['close']





        topvol23 = topactvoldata[22]
        topvolticker23 = topvol23['ticker']
        topvolchange23 = round(float(topvol23['changeRatio'])*100,ndigits=2)
        topvolvol23 = round(float(topvolticker1['volume'])*0.000001,ndigits=2)
        topvolsym23 = topvolticker23['disSymbol']
        topvol52low23 = topvolticker23['fiftyTwoWkLow']
        topvol52high23 = topvolticker23['fiftyTwoWkHigh']
        try:
            topvolturn23 = topvolticker23['turnoverRate']
        except ValueError:
            topvolturn23 = "N/A"
        topvolprice23 = topvolturn23['close']



        topvol24 = topactvoldata[23]
        topvolticker24 = topvol24['ticker']
        topvolchange24 = round(float(topvol24['changeRatio'])*100,ndigits=2)
        topvolvol24 = round(float(topvolticker1['volume'])*0.000001,ndigits=2)
        topvolsym24 = topvolticker24['disSymbol']
        topvol52low24 = topvolticker24['fiftyTwoWkLow']
        topvol52high24 = topvolticker24['fiftyTwoWkHigh']
        try:
            topvolturn24 = topvolticker24['turnoverRate']
        except ValueError:
            topvolturn24 = "N/A"
        topvolprice24 = topvolturn24['close']



        super().__init__(
            placeholder = "🇹 🇴 🇵 🛞 🇻 🇴 🇱 🇺 🇲 🇪",
            min_values=1,
            max_values=1,
            custom_id="topvolumedrop",
            options=[ 
                disnake.SelectOption(label=f"{topvolsym1} | Price: {topvolprice1} | Vol: {topvolvol1} mill.", description=f"Turnover: {topvolturn1} | 52wk Low: {topvol52low1} | 52wk High: {topvol52high1}"),
                disnake.SelectOption(label=f"{topvolsym2} | Price: {topvolprice2} | Vol: {topvolvol2} mill.", description=f"Turnover: {topvolturn2} | 52wk Low: {topvol52low2} | 52wk High: {topvol52high2}"),
                disnake.SelectOption(label=f"{topvolsym3} | Price: {topvolprice3} | Vol: {topvolvol3} mill.", description=f"Turnover: {topvolturn3} | 52wk Low: {topvol52low3} | 52wk High: {topvol52high3}"),
                disnake.SelectOption(label=f"{topvolsym4} | Price: {topvolprice4} | Vol: {topvolvol4} mill.", description=f"Turnover: {topvolturn4} | 52wk Low: {topvol52low4} | 52wk High: {topvol52high4}"),
                disnake.SelectOption(label=f"{topvolsym5} | Price: {topvolprice5} | Vol: {topvolvol5} mill.", description=f"Turnover: {topvolturn5} | 52wk Low: {topvol52low5} | 52wk High: {topvol52high5}"),
                disnake.SelectOption(label=f"{topvolsym6} | Price: {topvolprice6} | Vol: {topvolvol6} mill.", description=f"Turnover: {topvolturn6} | 52wk Low: {topvol52low6} | 52wk High: {topvol52high6}"),
                disnake.SelectOption(label=f"{topvolsym7} | Price: {topvolprice7} | Vol: {topvolvol7} mill.", description=f"Turnover: {topvolturn7} | 52wk Low: {topvol52low7} | 52wk High: {topvol52high7}"),
                disnake.SelectOption(label=f"{topvolsym8} | Price: {topvolprice8} | Vol: {topvolvol8} mill.", description=f"Turnover: {topvolturn8} | 52wk Low: {topvol52low8} | 52wk High: {topvol52high8}"),
                disnake.SelectOption(label=f"{topvolsym9} | Price: {topvolprice9} | Vol: {topvolvol9} mill.", description=f"Turnover: {topvolturn9} | 52wk Low: {topvol52low9} | 52wk High: {topvol52high9}"),
                disnake.SelectOption(label=f"{topvolsym10} | Price: {topvolprice10} | Vol: {topvolvol10} mill.", description=f"Turnover: {topvolturn10} | 52wk Low: {topvol52low10} | 52wk High: {topvol52high10}"),
                disnake.SelectOption(label=f"{topvolsym11} | Price: {topvolprice11} | Vol: {topvolvol11} mill.", description=f"Turnover: {topvolturn11} | 52wk Low: {topvol52low11} | 52wk High: {topvol52high11}"),
                disnake.SelectOption(label=f"{topvolsym12} | Price: {topvolprice12} | Vol: {topvolvol12} mill.", description=f"Turnover: {topvolturn12} | 52wk Low: {topvol52low12} | 52wk High: {topvol52high12}"),
                disnake.SelectOption(label=f"{topvolsym13} | Price: {topvolprice13} | Vol: {topvolvol13} mill.", description=f"Turnover: {topvolturn13} | 52wk Low: {topvol52low13} | 52wk High: {topvol52high13}"),
                disnake.SelectOption(label=f"{topvolsym14} | Price: {topvolprice14} | Vol: {topvolvol14} mill.", description=f"Turnover: {topvolturn14} | 52wk Low: {topvol52low14} | 52wk High: {topvol52high14}"),
                disnake.SelectOption(label=f"{topvolsym15} | Price: {topvolprice15} | Vol: {topvolvol15} mill.", description=f"Turnover: {topvolturn15} | 52wk Low: {topvol52low15} | 52wk High: {topvol52high15}"),
                disnake.SelectOption(label=f"{topvolsym16} | Price: {topvolprice16} | Vol: {topvolvol16} mill.", description=f"Turnover: {topvolturn16} | 52wk Low: {topvol52low16} | 52wk High: {topvol52high16}"),
                disnake.SelectOption(label=f"{topvolsym17} | Price: {topvolprice17} | Vol: {topvolvol17} mill.", description=f"Turnover: {topvolturn17} | 52wk Low: {topvol52low17} | 52wk High: {topvol52high17}"),
                disnake.SelectOption(label=f"{topvolsym18} | Price: {topvolprice18} | Vol: {topvolvol18} mill.", description=f"Turnover: {topvolturn18} | 52wk Low: {topvol52low18} | 52wk High: {topvol52high18}"),
                disnake.SelectOption(label=f"{topvolsym19} | Price: {topvolprice19} | Vol: {topvolvol19} mill.", description=f"Turnover: {topvolturn19} | 52wk Low: {topvol52low19} | 52wk High: {topvol52high19}"),
                disnake.SelectOption(label=f"{topvolsym20} | Price: {topvolprice20} | Vol: {topvolvol20} mill.", description=f"Turnover: {topvolturn20} | 52wk Low: {topvol52low20} | 52wk High: {topvol52high20}"),
                disnake.SelectOption(label=f"{topvolsym21} | Price: {topvolprice21} | Vol: {topvolvol21} mill.", description=f"Turnover: {topvolturn21} | 52wk Low: {topvol52low21} | 52wk High: {topvol52high21}"),
                disnake.SelectOption(label=f"{topvolsym22} | Price: {topvolprice22} | Vol: {topvolvol22} mill.", description=f"Turnover: {topvolturn22} | 52wk Low: {topvol52low22} | 52wk High: {topvol52high22}"),
                disnake.SelectOption(label=f"{topvolsym23} | Price: {topvolprice23} | Vol: {topvolvol23} mill.", description=f"Turnover: {topvolturn23} | 52wk Low: {topvol52low23} | 52wk High: {topvol52high23}"),
                disnake.SelectOption(label=f"{topvolsym24} | Price: {topvolprice24} | Vol: {topvolvol24} mill.", description=f"Turnover: {topvolturn24} | 52wk Low: {topvol52low24} | 52wk High: {topvol52high24}"),
            ]
        )
    async def callback(self, interaction: disnake.MessageCommandInteraction):
        if self.values[0] == self.values[0]:
            await interaction.response.edit_message(view=MarketMainView())

class ForexView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

        self.add_item(Forex())

class Forex(disnake.ui.Select):
    def __init__(self):
        
        forex = requests.get(url="https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids=913348845,913349000,913344317,913344337,913349155,913344262,913344331,913344246,913344269,913328210,913328365,913328351,913339131,913348741,913349051,913342231,913348896&includeSecu=1&more=1").json()
        forex1 = forex[0]
        forexsym1 = forex1['disSymbol']
        forexchange1 = round(float(forex1['changeRatio'])*100,ndigits=2)
        forexprice1 = forex1['close']
        forexvol1 = forex1['volume']
        forexmaker1 = forex1['quoteMaker']
        forexname1 = forex1['name']
        type1 = forex1['type']
        forex52l1 = forex1['fiftyTwoWkLow']
        forex52h1 = forex1['fiftyTwoWkHigh']


        forex2 = forex[1]
        forexsym2 = forex2['disSymbol']
        forexchange2 = round(float(forex2['changeRatio'])*100,ndigits=2)
        forexprice2 = forex2['close']
        forexvol2 = forex2['volume']
        forexmaker2 = forex2['quoteMaker']
        forexname2 = forex2['name']
        type2 = forex2['type']
        forex52l2 = forex2['fiftyTwoWkLow']
        forex52h2 = forex2['fiftyTwoWkHigh']



        forex3 = forex[2]
        forexsym3 = forex3['disSymbol']
        forexchange3 = round(float(forex3['changeRatio'])*100,ndigits=2)
        forexprice3 = forex3['close']
        forexvol3 = forex3['volume']
        forexmaker3 = forex3['quoteMaker']
        forexname3 = forex3['name']
        type3 = forex3['type']
        forex52l3 = forex3['fiftyTwoWkLow']
        forex52h3 = forex3['fiftyTwoWkHigh']


        forex4 = forex[3]
        forexsym4 = forex4['disSymbol']
        forexchange4 = round(float(forex4['changeRatio'])*100,ndigits=2)
        forexprice4 = forex4['close']
        forexvol4 = forex4['volume']
        forexmaker4 = forex4['quoteMaker']
        forexname4 = forex4['name']
        type4 = forex4['type']
        forex52l4 = forex4['fiftyTwoWkLow']
        forex52h4 = forex4['fiftyTwoWkHigh']



        forex5 = forex[4]
        forexsym5 = forex5['disSymbol']
        forexchange5 = round(float(forex5['changeRatio'])*100,ndigits=2)
        forexprice5 = forex5['close']
        forexvol5 = forex5['volume']
        forexmaker5 = forex5['quoteMaker']
        forexname5 = forex5['name']
        type5 = forex5['type']
        forex52l5 = forex5['fiftyTwoWkLow']
        forex52h5 = forex5['fiftyTwoWkHigh']


        forex6 = forex[5]
        forexsym6 = forex6['disSymbol']
        forexchange6 = round(float(forex6['changeRatio'])*100,ndigits=2)
        forexprice6 = forex6['close']
        forexvol6 = forex6['volume']
        forexmaker6 = forex6['quoteMaker']
        forexname6 = forex6['name']
        type6 = forex6['type']
        forex52l6 = forex6['fiftyTwoWkLow']
        forex52h6 = forex6['fiftyTwoWkHigh']



        forex7 = forex[6]
        forexsym7 = forex7['disSymbol']
        forexchange7 = round(float(forex7['changeRatio'])*100,ndigits=2)
        forexprice7 = forex7['close']
        forexvol7 = forex7['volume']
        forexmaker7 = forex7['quoteMaker']
        forexname7 = forex7['name']
        type7 = forex7['type']
        forex52l7 = forex7['fiftyTwoWkLow']
        forex52h7 = forex7['fiftyTwoWkHigh']



        forex8 = forex[7]
        forexsym8 = forex8['disSymbol']
        forexchange8 = round(float(forex8['changeRatio'])*100,ndigits=2)
        forexprice8 = forex8['close']
        forexvol8 = forex8['volume']
        forexmaker8 = forex8['quoteMaker']
        forexname8 = forex8['name']
        type8 = forex8['type']
        forex52l8 = forex8['fiftyTwoWkLow']
        forex52h8 = forex8['fiftyTwoWkHigh']



        forex9 = forex[8]
        forexsym9 = forex9['disSymbol']
        forexchange9 = round(float(forex9['changeRatio'])*100,ndigits=2)
        forexprice9 = forex9['close']
        forexvol9 = forex9['volume']
        forexmaker9 = forex9['quoteMaker']
        forexname9 = forex9['name']
        type9 = forex9['type']
        forex52l9 = forex9['fiftyTwoWkLow']
        forex52h9 = forex9['fiftyTwoWkHigh']



        forex10 = forex[9]
        forexsym10 = forex10['disSymbol']
        forexchange10 = round(float(forex10['changeRatio'])*100,ndigits=2)
        forexprice10 = forex10['close']
        forexvol10 = forex10['volume']
        forexmaker10 = forex10['quoteMaker']
        forexname10 = forex10['name']
        type10 = forex10['type']
        forex52l10 = forex10['fiftyTwoWkLow']
        forex52h10 = forex10['fiftyTwoWkHigh']

        forex11 = forex[10]
        forexsym11 = forex11['disSymbol']
        forexchange11 = round(float(forex11['changeRatio'])*100,ndigits=2)
        forexprice11 = forex11['close']
        forexvol11 = forex11['volume']
        forexmaker11 = forex11['quoteMaker']
        forexname11 = forex11['name']
        type11 = forex11['type']
        forex52l11 = forex11['fiftyTwoWkLow']
        forex52h11 = forex11['fiftyTwoWkHigh']

        forex12 = forex[11]
        forexsym12 = forex12['disSymbol']
        forexchange12 = round(float(forex12['changeRatio'])*100,ndigits=2)
        forexprice12 = forex12['close']
        forexvol12 = forex12['volume']
        forexmaker12 = forex12['quoteMaker']
        forexname12 = forex12['name']
        type12 = forex12['type']
        forex52l12 = forex12['fiftyTwoWkLow']
        forex52h12 = forex12['fiftyTwoWkHigh']

        forex13 = forex[12]
        forexsym13 = forex13['disSymbol']
        forexchange13 = round(float(forex13['changeRatio'])*100,ndigits=2)
        forexprice13 = forex13['close']
        forexvol13 = forex13['volume']
        forexmaker13 = forex13['quoteMaker']
        forexname13 = forex13['name']
        type13 = forex13['type']
        forex52l13 = forex13['fiftyTwoWkLow']
        forex52h13 = forex13['fiftyTwoWkHigh']

        forex14 = forex[13]
        forexsym14 = forex14['disSymbol']
        forexchange14 = round(float(forex14['changeRatio'])*100,ndigits=2)
        forexprice14 = forex14['close']
        forexvol14 = forex14['volume']
        forexmaker14 = forex14['quoteMaker']
        forexname14 = forex14['name']
        type14 = forex14['type']
        forex52l14 = forex14['fiftyTwoWkLow']
        forex52h14 = forex14['fiftyTwoWkHigh']

        forex15 = forex[14]
        forexsym15 = forex15['disSymbol']
        forexchange15 = round(float(forex15['changeRatio'])*100,ndigits=2)
        forexprice15 = forex15['close']
        forexvol15 = forex15['volume']
        forexmaker15 = forex15['quoteMaker']
        forexname15 = forex15['name']
        type15 = forex15['type']
        forex52l15 = forex15['fiftyTwoWkLow']
        forex52h15 = forex15['fiftyTwoWkHigh']

        forex16 = forex[15]
        forexsym16 = forex16['disSymbol']
        forexchange16 = round(float(forex16['changeRatio'])*100,ndigits=2)
        forexprice16 = forex16['close']
        forexvol16 = forex16['volume']
        forexmaker16 = forex16['quoteMaker']
        forexname16 = forex16['name']
        type16 = forex16['type']
        forex52l16 = forex16['fiftyTwoWkLow']
        forex52h16 = forex16['fiftyTwoWkHigh']



        forex17 = forex[16]
        forexsym17 = forex17['disSymbol']
        forexchange17 = round(float(forex17['changeRatio'])*100,ndigits=2)
        forexprice17 = forex17['close']
        forexvol17 = forex17['volume']
        forexmaker17 = forex17['quoteMaker']
        forexname17 = forex17['name']
        type17 = forex17['type']
        forex52l17 = forex17['fiftyTwoWkLow']
        forex52h17 = forex17['fiftyTwoWkHigh']


        super().__init__(
            placeholder="🇫 🇴 🇷 🇪 🇽 👛",
            min_values=1,
            max_values=1,
            custom_id="forexdrop",
            options= [ 
                disnake.SelectOption(label=f"{forexname1} ${forexprice1} | Change: {forexchange1}", description=f"Volume: {forexvol1} | MarketMaker: {forexmaker1} | 52wLow: {forex52l1} | 52wHigh: {forex52h1}"),
                disnake.SelectOption(label=f"{forexname2} ${forexprice2} | Change: {forexchange2}", description=f"Volume: {forexvol2} | MarketMaker: {forexmaker2} | 52wLow: {forex52l2} | 52wHigh: {forex52h2}"),
                disnake.SelectOption(label=f"{forexname3} ${forexprice3} | Change: {forexchange3}", description=f"Volume: {forexvol3} | MarketMaker: {forexmaker3} | 52wLow: {forex52l3} | 52wHigh: {forex52h3}"),
                disnake.SelectOption(label=f"{forexname4} ${forexprice4} | Change: {forexchange4}", description=f"Volume: {forexvol4} | MarketMaker: {forexmaker4} | 52wLow: {forex52l4} | 52wHigh: {forex52h4}"),
                disnake.SelectOption(label=f"{forexname5} ${forexprice5} | Change: {forexchange5}", description=f"Volume: {forexvol5} | MarketMaker: {forexmaker5} | 52wLow: {forex52l5} | 52wHigh: {forex52h5}"),
                disnake.SelectOption(label=f"{forexname6} ${forexprice6} | Change: {forexchange6}", description=f"Volume: {forexvol6} | MarketMaker: {forexmaker6} | 52wLow: {forex52l6} | 52wHigh: {forex52h6}"),
                disnake.SelectOption(label=f"{forexname7} ${forexprice7} | Change: {forexchange7}", description=f"Volume: {forexvol7} | MarketMaker: {forexmaker7} | 52wLow: {forex52l7} | 52wHigh: {forex52h7}"),
                disnake.SelectOption(label=f"{forexname8} ${forexprice8} | Change: {forexchange8}", description=f"Volume: {forexvol8} | MarketMaker: {forexmaker8} | 52wLow: {forex52l8} | 52wHigh: {forex52h8}"),
                disnake.SelectOption(label=f"{forexname9} ${forexprice9} | Change: {forexchange9}", description=f"Volume: {forexvol9} | MarketMaker: {forexmaker9} | 52wLow: {forex52l9} | 52wHigh: {forex52h9}"),
                disnake.SelectOption(label=f"{forexname10} ${forexprice10} | Change: {forexchange10}", description=f"Volume: {forexvol10} | MarketMaker: {forexmaker10} | 52wLow: {forex52l10} | 52wHigh: {forex52h10}"),
                disnake.SelectOption(label=f"{forexname11} ${forexprice11} | Change: {forexchange11}", description=f"Volume: {forexvol11} | MarketMaker: {forexmaker11} | 52wLow: {forex52l11} | 52wHigh: {forex52h11}"),
                disnake.SelectOption(label=f"{forexname12} ${forexprice12} | Change: {forexchange12}", description=f"Volume: {forexvol12} | MarketMaker: {forexmaker12} | 52wLow: {forex52l12} | 52wHigh: {forex52h12}"),
                disnake.SelectOption(label=f"{forexname13} ${forexprice13} | Change: {forexchange13}", description=f"Volume: {forexvol13} | MarketMaker: {forexmaker13} | 52wLow: {forex52l13} | 52wHigh: {forex52h13}"),
                disnake.SelectOption(label=f"{forexname14} ${forexprice14} | Change: {forexchange14}", description=f"Volume: {forexvol14} | MarketMaker: {forexmaker14} | 52wLow: {forex52l14} | 52wHigh: {forex52h14}"),
                disnake.SelectOption(label=f"{forexname15} ${forexprice15} | Change: {forexchange15}", description=f"Volume: {forexvol15} | MarketMaker: {forexmaker15} | 52wLow: {forex52l15} | 52wHigh: {forex52h15}"),
                disnake.SelectOption(label=f"{forexname16} ${forexprice16} | Change: {forexchange16}", description=f"Volume: {forexvol16} | MarketMaker: {forexmaker16} | 52wLow: {forex52l16} | 52wHigh: {forex52h16}"),
                disnake.SelectOption(label=f"{forexname17} ${forexprice17} | Change: {forexchange17}", description=f"Volume: {forexvol17} | MarketMaker: {forexmaker17} | 52wLow: {forex52l17} | 52wHigh: {forex52h17}"),
            ]
        )

    async def callback(self, interaction:disnake.MessageCommandInteraction):
        if self.values[0] == self.values[0]:
            forex = requests.get(url="https://quotes-gw.webullfintech.com/api/bgw/quote/realtime?ids=913348845,913349000,913344317,913344337,913349155,913344262,913344331,913344246,913344269,913328210,913328365,913328351,913339131,913348741,913349051,913342231,913348896&includeSecu=1&more=1").json()
            forex1 = forex[0]
            forexsym1 = forex1['disSymbol']
            forexchange1 = round(float(forex1['changeRatio'])*100,ndigits=2)
            forexprice1 = forex1['close']
            forexvol1 = forex1['volume']
            forexmaker1 = forex1['quoteMaker']
            forexname1 = forex1['name']
            type1 = forex1['type']
            forex52l1 = forex1['fiftyTwoWkLow']
            forex52h1 = forex1['fiftyTwoWkHigh']


            forex2 = forex[1]
            forexsym2 = forex2['disSymbol']
            forexchange2 = round(float(forex2['changeRatio'])*100,ndigits=2)
            forexprice2 = forex2['close']
            forexvol2 = forex2['volume']
            forexmaker2 = forex2['quoteMaker']
            forexname2 = forex2['name']
            type2 = forex2['type']
            forex52l2 = forex2['fiftyTwoWkLow']
            forex52h2 = forex2['fiftyTwoWkHigh']



            forex3 = forex[2]
            forexsym3 = forex3['disSymbol']
            forexchange3 = round(float(forex3['changeRatio'])*100,ndigits=2)
            forexprice3 = forex3['close']
            forexvol3 = forex3['volume']
            forexmaker3 = forex3['quoteMaker']
            forexname3 = forex3['name']
            type3 = forex3['type']
            forex52l3 = forex3['fiftyTwoWkLow']
            forex52h3 = forex3['fiftyTwoWkHigh']


            forex4 = forex[3]
            forexsym4 = forex4['disSymbol']
            forexchange4 = round(float(forex4['changeRatio'])*100,ndigits=2)
            forexprice4 = forex4['close']
            forexvol4 = forex4['volume']
            forexmaker4 = forex4['quoteMaker']
            forexname4 = forex4['name']
            type4 = forex4['type']
            forex52l4 = forex4['fiftyTwoWkLow']
            forex52h4 = forex4['fiftyTwoWkHigh']



            forex5 = forex[4]
            forexsym5 = forex5['disSymbol']
            forexchange5 = round(float(forex5['changeRatio'])*100,ndigits=2)
            forexprice5 = forex5['close']
            forexvol5 = forex5['volume']
            forexmaker5 = forex5['quoteMaker']
            forexname5 = forex5['name']
            type5 = forex5['type']
            forex52l5 = forex5['fiftyTwoWkLow']
            forex52h5 = forex5['fiftyTwoWkHigh']


            forex6 = forex[5]
            forexsym6 = forex6['disSymbol']
            forexchange6 = round(float(forex6['changeRatio'])*100,ndigits=2)
            forexprice6 = forex6['close']
            forexvol6 = forex6['volume']
            forexmaker6 = forex6['quoteMaker']
            forexname6 = forex6['name']
            type6 = forex6['type']
            forex52l6 = forex6['fiftyTwoWkLow']
            forex52h6 = forex6['fiftyTwoWkHigh']



            forex7 = forex[6]
            forexsym7 = forex7['disSymbol']
            forexchange7 = round(float(forex7['changeRatio'])*100,ndigits=2)
            forexprice7 = forex7['close']
            forexvol7 = forex7['volume']
            forexmaker7 = forex7['quoteMaker']
            forexname7 = forex7['name']
            type7 = forex7['type']
            forex52l7 = forex7['fiftyTwoWkLow']
            forex52h7 = forex7['fiftyTwoWkHigh']



            forex8 = forex[7]
            forexsym8 = forex8['disSymbol']
            forexchange8 = round(float(forex8['changeRatio'])*100,ndigits=2)
            forexprice8 = forex8['close']
            forexvol8 = forex8['volume']
            forexmaker8 = forex8['quoteMaker']
            forexname8 = forex8['name']
            type8 = forex8['type']
            forex52l8 = forex8['fiftyTwoWkLow']
            forex52h8 = forex8['fiftyTwoWkHigh']



            forex9 = forex[8]
            forexsym9 = forex9['disSymbol']
            forexchange9 = round(float(forex9['changeRatio'])*100,ndigits=2)
            forexprice9 = forex9['close']
            forexvol9 = forex9['volume']
            forexmaker9 = forex9['quoteMaker']
            forexname9 = forex9['name']
            type9 = forex9['type']
            forex52l9 = forex9['fiftyTwoWkLow']
            forex52h9 = forex9['fiftyTwoWkHigh']



            forex10 = forex[9]
            forexsym10 = forex10['disSymbol']
            forexchange10 = round(float(forex10['changeRatio'])*100,ndigits=2)
            forexprice10 = forex10['close']
            forexvol10 = forex10['volume']
            forexmaker10 = forex10['quoteMaker']
            forexname10 = forex10['name']
            type10 = forex10['type']
            forex52l10 = forex10['fiftyTwoWkLow']
            forex52h10 = forex10['fiftyTwoWkHigh']

            forex11 = forex[10]
            forexsym11 = forex11['disSymbol']
            forexchange11 = round(float(forex11['changeRatio'])*100,ndigits=2)
            forexprice11 = forex11['close']
            forexvol11 = forex11['volume']
            forexmaker11 = forex11['quoteMaker']
            forexname11 = forex11['name']
            type11 = forex11['type']
            forex52l11 = forex11['fiftyTwoWkLow']
            forex52h11 = forex11['fiftyTwoWkHigh']

            forex12 = forex[11]
            forexsym12 = forex12['disSymbol']
            forexchange12 = round(float(forex12['changeRatio'])*100,ndigits=2)
            forexprice12 = forex12['close']
            forexvol12 = forex12['volume']
            forexmaker12 = forex12['quoteMaker']
            forexname12 = forex12['name']
            type12 = forex12['type']
            forex52l12 = forex12['fiftyTwoWkLow']
            forex52h12 = forex12['fiftyTwoWkHigh']

            forex13 = forex[12]
            forexsym13 = forex13['disSymbol']
            forexchange13 = round(float(forex13['changeRatio'])*100,ndigits=2)
            forexprice13 = forex13['close']
            forexvol13 = forex13['volume']
            forexmaker13 = forex13['quoteMaker']
            forexname13 = forex13['name']
            type13 = forex13['type']
            forex52l13 = forex13['fiftyTwoWkLow']
            forex52h13 = forex13['fiftyTwoWkHigh']

            forex14 = forex[13]
            forexsym14 = forex14['disSymbol']
            forexchange14 = round(float(forex14['changeRatio'])*100,ndigits=2)
            forexprice14 = forex14['close']
            forexvol14 = forex14['volume']
            forexmaker14 = forex14['quoteMaker']
            forexname14 = forex14['name']
            type14 = forex14['type']
            forex52l14 = forex14['fiftyTwoWkLow']
            forex52h14 = forex14['fiftyTwoWkHigh']

            forex15 = forex[14]
            forexsym15 = forex15['disSymbol']
            forexchange15 = round(float(forex15['changeRatio'])*100,ndigits=2)
            forexprice15 = forex15['close']
            forexvol15 = forex15['volume']
            forexmaker15 = forex15['quoteMaker']
            forexname15 = forex15['name']
            type15 = forex15['type']
            forex52l15 = forex15['fiftyTwoWkLow']
            forex52h15 = forex15['fiftyTwoWkHigh']

            forex16 = forex[15]
            forexsym16 = forex16['disSymbol']
            forexchange16 = round(float(forex16['changeRatio'])*100,ndigits=2)
            forexprice16 = forex16['close']
            forexvol16 = forex16['volume']
            forexmaker16 = forex16['quoteMaker']
            forexname16 = forex16['name']
            type16 = forex16['type']
            forex52l16 = forex16['fiftyTwoWkLow']
            forex52h16 = forex16['fiftyTwoWkHigh']



            forex17 = forex[16]
            forexsym17 = forex17['disSymbol']
            forexchange17 = round(float(forex17['changeRatio'])*100,ndigits=2)
            forexprice17 = forex17['close']
            forexvol17 = forex17['volume']
            forexmaker17 = forex17['quoteMaker']
            forexname17 = forex17['name']
            type17 = forex17['type']
            forex52l17 = forex17['fiftyTwoWkLow']
            forex52h17 = forex17['fiftyTwoWkHigh']
            await interaction.response.defer(with_message=True)
            counter = 1
            while True:
                counter = counter+1
                embed = disnake.Embed(title="Realtime Forex", color=disnake.Colour.random(), url="https://www.fudstop.io")
                view = disnake.ui.View()
                forexb1 = disnake.ui.Button(style=disnake.ButtonStyle.grey, label=f"{forexname1} ${forexprice1}")
                forexb2 = disnake.ui.Button(style=disnake.ButtonStyle.grey, label=f"{forexname2} ${forexprice2}")
                forexb3 = disnake.ui.Button(style=disnake.ButtonStyle.grey, label=f"{forexname3} ${forexprice3}")
                forexb4 = disnake.ui.Button(style=disnake.ButtonStyle.grey, label=f"{forexname4} ${forexprice4}")
                forexb5 = disnake.ui.Button(style=disnake.ButtonStyle.grey, label=f"{forexname5} ${forexprice5}")
                forexb6 = disnake.ui.Button(style=disnake.ButtonStyle.grey, label=f"{forexname6} ${forexprice6}")
                forexb7 = disnake.ui.Button(style=disnake.ButtonStyle.grey, label=f"{forexname7} ${forexprice7}")
                forexb8 = disnake.ui.Button(style=disnake.ButtonStyle.grey, label=f"{forexname8} ${forexprice8}")
                forexb9 = disnake.ui.Button(style=disnake.ButtonStyle.grey, label=f"{forexname9} ${forexprice9}")
                forexb10 = disnake.ui.Button(style=disnake.ButtonStyle.grey, label=f"{forexname10} ${forexprice10}")
                forexb11 = disnake.ui.Button(style=disnake.ButtonStyle.grey, label=f"{forexname11} ${forexprice11}")
                forexb12 = disnake.ui.Button(style=disnake.ButtonStyle.grey, label=f"{forexname12} ${forexprice12}")
                forexb13 = disnake.ui.Button(style=disnake.ButtonStyle.grey, label=f"{forexname13} ${forexprice13}")
                forexb14 = disnake.ui.Button(style=disnake.ButtonStyle.grey, label=f"{forexname14} ${forexprice14}")
                forexb15 = disnake.ui.Button(style=disnake.ButtonStyle.grey, label=f"{forexname15} ${forexprice15}")
                forexb16 = disnake.ui.Button(style=disnake.ButtonStyle.grey, label=f"{forexname16} ${forexprice16}")
                forexb17 = disnake.ui.Button(style=disnake.ButtonStyle.grey, label=f"{forexname17} ${forexprice17}")
                view.add_item(forexb1)
                view.add_item(forexb2)
                view.add_item(forexb3)
                view.add_item(forexb4)
                view.add_item(forexb5)
                view.add_item(forexb6)
                view.add_item(forexb7)
                view.add_item(forexb8)
                view.add_item(forexb9)
                view.add_item(forexb10)
                view.add_item(forexb11)
                view.add_item(forexb12)
                view.add_item(forexb13)
                view.add_item(forexb14)
                view.add_item(forexb15)
                view.add_item(forexb16)
                view.add_item(forexb17)
                await interaction.edit_original_response(view=view,embed=embed)

class TopETFView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

class CommodityETF(disnake.ui.Select):
    def __init__(self):

        commod = requests.get(url="https://quotes-gw.webullfintech.com/api/wlas/etfinder/pcFinder?topNum=5&finderId=wlas.etfinder.commodity&nbboLevel=false").json()
        tabs = commod['tabs']
        cmdty1 = tabs[0]
        cmdtyup1 = cmdty1['upNum']
        cmdtydown1 = cmdty1['dowoNum']
        cmdtyflat1 = cmdty1['flatNum']
        cmdtytickers = cmdty1['tickerTupleList']
        for i in cmdtytickers:
            name = i.get('name')
            print(name)

        cmdtyticker1 = cmdtytickers[0]
        cmdtyname1 = cmdtyticker1['name']
        cmdtysym1 = cmdtyticker1['disSymbol']
        cmdtychange1 = round(float(cmdtyticker1['changeRatio'])*100,ndigits=2)
        cmdtyprice1 = cmdtyticker1['close']
        cmdtyvol1 = round(float(cmdtyticker1['volume'])*0.000001,ndigits=2)
        try:    
            cmdtyasset1 = round(float(cmdtyticker1['totalAsset'])*0.000001,ndigits=2)
        except KeyError:
            cmdtyasset1 = "N/A"


        cmdtyticker2 = cmdtytickers[1]
        cmdtyname2 = cmdtyticker2['name']
        cmdtysym2 = cmdtyticker2['disSymbol']
        cmdtychange2 = round(float(cmdtyticker2['changeRatio'])*100,ndigits=2)
        cmdtyprice2 = cmdtyticker2['close']
        cmdtyvol2 = round(float(cmdtyticker1['volume'])*0.000001,ndigits=2)
        try:
            cmdtyasset2 = round(float(cmdtyticker2['totalAsset'])*0.000001,ndigits=2)
        except KeyError:
            cmdtyasset2 = "N/A"



        cmdtyticker3 = cmdtytickers[2]
        cmdtyname3 = cmdtyticker3['name']
        cmdtysym3 = cmdtyticker3['disSymbol']
        cmdtychange3 = round(float(cmdtyticker3['changeRatio'])*100,ndigits=2)
        cmdtyprice3 = cmdtyticker3['close']
        cmdtyvol3 = round(float(cmdtyticker1['volume'])*0.000001,ndigits=2)
        try:
            cmdtyasset3 = round(float(cmdtyticker3['totalAsset'])*0.000001,ndigits=2)
        except KeyError:
            cmdtyasset3 = "N/A"


        cmdtyticker4 = cmdtytickers[3]
        cmdtyname4 = cmdtyticker4['name']
        cmdtysym4 = cmdtyticker4['disSymbol']
        cmdtychange4 = round(float(cmdtyticker4['changeRatio'])*100,ndigits=2)
        cmdtyprice4 = cmdtyticker4['close']
        cmdtyvol4 = round(float(cmdtyticker1['volume'])*0.000001,ndigits=2)
        try:
            cmdtyasset4 = round(float(cmdtyticker4['totalAsset'])*0.000001,ndigits=2)
        except KeyError:
            cmdtyasset4 = "N/A"



        cmdtyticker5 = cmdtytickers[4]
        cmdtyname5 = cmdtyticker5['name']
        cmdtysym5 = cmdtyticker5['disSymbol']
        cmdtychange5 = round(float(cmdtyticker5['changeRatio'])*100,ndigits=2)
        cmdtyprice5 = cmdtyticker5['close']
        cmdtyvol5 = round(float(cmdtyticker1['volume'])*0.000001,ndigits=2)
        try:
            cmdtyasset5 = round(float(cmdtyticker5['totalAsset'])*0.000001,ndigits=2)
        except KeyError:
            cmdtyasset5 = "N/A"




        cmdtyticker6 = cmdtytickers[5]
        cmdtyname6 = cmdtyticker6['name']
        cmdtysym6 = cmdtyticker6['disSymbol']
        cmdtychange6 = round(float(cmdtyticker6['changeRatio'])*100,ndigits=2)
        cmdtyprice6 = cmdtyticker6['close']
        cmdtyvol6 = round(float(cmdtyticker1['volume'])*0.000001,ndigits=2)
        try:
            cmdtyasset6 = round(float(cmdtyticker6['totalAsset'])*0.000001,ndigits=2)
        except KeyError:
            cmdtyasset6 = "N/A"




        cmdtyticker7 = cmdtytickers[6]
        cmdtyname7 = cmdtyticker7['name']
        cmdtysym7 = cmdtyticker7['disSymbol']
        cmdtychange7 = round(float(cmdtyticker7['changeRatio'])*100,ndigits=2)
        cmdtyprice7 = cmdtyticker7['close']
        cmdtyvol7 = round(float(cmdtyticker1['volume'])*0.000001,ndigits=2)
        try:
            cmdtyasset7 = round(float(cmdtyticker7['totalAsset'])*0.000001,ndigits=2)
        except KeyError:
            cmdtyasset7 = "N/A"




        cmdtyticker8 = cmdtytickers[7]
        cmdtyname8 = cmdtyticker8['name']
        cmdtysym8 = cmdtyticker8['disSymbol']
        cmdtychange8 = round(float(cmdtyticker8['changeRatio'])*100,ndigits=2)
        cmdtyprice8 = cmdtyticker8['close']
        cmdtyvol8 = round(float(cmdtyticker1['volume'])*0.000001,ndigits=2)
        try:
            cmdtyasset8 = round(float(cmdtyticker8['totalAsset'])*0.000001,ndigits=2)
        except KeyError:
            cmdtyasset8 = "N/A"




        cmdtyticker9 = cmdtytickers[8]
        cmdtyname9 = cmdtyticker9['name']
        cmdtysym9 = cmdtyticker9['disSymbol']
        cmdtychange9 = round(float(cmdtyticker9['changeRatio'])*100,ndigits=2)
        cmdtyprice9 = cmdtyticker9['close']
        cmdtyvol9 = round(float(cmdtyticker1['volume'])*0.000001,ndigits=2)
        try:
            cmdtyasset9 = round(float(cmdtyticker9['totalAsset'])*0.000001,ndigits=2)
        except KeyError:
            cmdtyasset9 = "N/A"




        cmdtyticker10 = cmdtytickers[9]
        cmdtyname10 = cmdtyticker10['name']
        cmdtysym10 = cmdtyticker10['disSymbol']
        cmdtychange10 = round(float(cmdtyticker10['changeRatio'])*100,ndigits=2)
        cmdtyprice10 = cmdtyticker10['close']
        cmdtyvol10 = round(float(cmdtyticker1['volume'])*0.000001,ndigits=2)
        try:
            cmdtyasset10 = round(float(cmdtyticker10['totalAsset'])*0.000001,ndigits=2)
        except KeyError:
            cmdtyasset10 = "N/A"


        super().__init__(
            placeholder="🇨 🇴 🇲 🇲 🇴 🇩 🇮 🇹 🇾🔮🇪 🇹 🇫 🇸",
            min_values=1,
            max_values=1,
            custom_id="commodityetfdrop",
            options= [ 
                disnake.SelectOption(label=f"{cmdtysym1} | ${cmdtyprice1} | Change: {cmdtychange1}%", description=f"Vol: {cmdtyvol1} million | Assets: {cmdtyasset1} million."),
                disnake.SelectOption(label=f"{cmdtysym2} | ${cmdtyprice2} | Change: {cmdtychange2}%", description=f"Vol: {cmdtyvol2} million | Assets: {cmdtyasset2} million."),
                disnake.SelectOption(label=f"{cmdtysym3} | ${cmdtyprice3} | Change: {cmdtychange3}%", description=f"Vol: {cmdtyvol3} million | Assets: {cmdtyasset3} million."),
                disnake.SelectOption(label=f"{cmdtysym4} | ${cmdtyprice4} | Change: {cmdtychange4}%", description=f"Vol: {cmdtyvol4} million | Assets: {cmdtyasset4} million."),
                disnake.SelectOption(label=f"{cmdtysym5} | ${cmdtyprice5} | Change: {cmdtychange5}%", description=f"Vol: {cmdtyvol5} million | Assets: {cmdtyasset5} million."),
                disnake.SelectOption(label=f"{cmdtysym6} | ${cmdtyprice6} | Change: {cmdtychange6}%", description=f"Vol: {cmdtyvol6} million | Assets: {cmdtyasset6} million."),
                disnake.SelectOption(label=f"{cmdtysym7} | ${cmdtyprice7} | Change: {cmdtychange7}%", description=f"Vol: {cmdtyvol7} million | Assets: {cmdtyasset7} million."),
                disnake.SelectOption(label=f"{cmdtysym8} | ${cmdtyprice8} | Change: {cmdtychange8}%", description=f"Vol: {cmdtyvol8} million | Assets: {cmdtyasset8} million."),
                disnake.SelectOption(label=f"{cmdtysym9} | ${cmdtyprice9} | Change: {cmdtychange9}%", description=f"Vol: {cmdtyvol9} million | Assets: {cmdtyasset9} million."),
                disnake.SelectOption(label=f"{cmdtysym10} | ${cmdtyprice10} | Change: {cmdtychange10}%", description=f"Vol: {cmdtyvol10} million | Assets: {cmdtyasset10} million."),
            ]
        )
    async def callback(self, interaction: disnake.MessageCommandInteraction):
        if self.values[0] == self.values[0]:
            await interaction.response.edit_message(self.values[0])



class TopOiDrop(disnake.ui.Select):
    def __init__(self):
        topoi= requests.get(url="https://quotes-gw.webullfintech.com/api/wlas/option/rank/list?regionId=6&rankType=totalPosition&pageIndex=1&pageSize=50").json()
        topoidata = topoi['data']

        topoi1 = topoidata[0]
        topoiticker1 = topoi1['ticker']
        topoisym1 = topoiticker1['symbol']
        topoiprice1 = topoiticker1['close']
        topoichange1 = round(float(topoiticker1['changeRatio'])*100,ndigits=2)

        topoivalues1 = topoi1['values']
        topoivol1 = round(float(topoivalues1['volume'])*0.000001,ndigits=2)
        topoioi1 = round(float(topoivalues1['position'])*0.000001,ndigits=2)
        topoivolpcr1 = topoivalues1['volumeCallPutRatio']
        topoipospcr1 = topoivalues1['positionCallPutRatio']




        topoi2 = topoidata[1]
        topoiticker2 = topoi2['ticker']
        topoisym2 = topoiticker2['symbol']
        topoiprice2 = topoiticker2['close']
        topoichange2 = round(float(topoiticker2['changeRatio'])*100,ndigits=2)

        topoivalues2 = topoi2['values']
        topoivol2 = round(float(topoivalues2['volume'])*0.000001,ndigits=2)
        topoioi2 = round(float(topoivalues2['position'])*0.000001,ndigits=2)
        topoivolpcr2 = topoivalues2['volumeCallPutRatio']
        topoipospcr2 = topoivalues2['positionCallPutRatio']


        topoi3 = topoidata[2]
        topoiticker3 = topoi3['ticker']
        topoisym3 = topoiticker3['symbol']
        topoiprice3 = topoiticker3['close']
        topoichange3 = round(float(topoiticker3['changeRatio'])*100,ndigits=2)

        topoivalues3 = topoi3['values']
        topoivol3 = round(float(topoivalues3['volume'])*0.000001,ndigits=2)
        topoioi3 = round(float(topoivalues3['position'])*0.000001,ndigits=2)
        topoivolpcr3 = topoivalues3['volumeCallPutRatio']
        topoipospcr3 = topoivalues3['positionCallPutRatio']



        topoi4 = topoidata[3]
        topoiticker4 = topoi4['ticker']
        topoisym4 = topoiticker4['symbol']
        topoiprice4 = topoiticker4['close']
        topoichange4 = round(float(topoiticker4['changeRatio'])*100,ndigits=2)

        topoivalues4 = topoi4['values']
        topoivol4 = round(float(topoivalues4['volume'])*0.000001,ndigits=2)
        topoioi4 = round(float(topoivalues4['position'])*0.000001,ndigits=2)
        topoivolpcr4 = topoivalues4['volumeCallPutRatio']
        topoipospcr4 = topoivalues4['positionCallPutRatio']



        topoi5 = topoidata[4]
        topoiticker5 = topoi5['ticker']
        topoisym5 = topoiticker5['symbol']
        topoiprice5 = topoiticker5['close']
        topoichange5 = round(float(topoiticker5['changeRatio'])*100,ndigits=2)

        topoivalues5 = topoi5['values']
        topoivol5 = round(float(topoivalues5['volume'])*0.000001,ndigits=2)
        topoioi5 = round(float(topoivalues5['position'])*0.000001,ndigits=2)
        topoivolpcr5 = topoivalues5['volumeCallPutRatio']
        topoipospcr5 = topoivalues5['positionCallPutRatio']



        topoi6 = topoidata[5]
        topoiticker6 = topoi6['ticker']
        topoisym6 = topoiticker6['symbol']
        topoiprice6 = topoiticker6['close']
        topoichange6 = round(float(topoiticker6['changeRatio'])*100,ndigits=2)

        topoivalues6 = topoi6['values']
        topoivol6 = round(float(topoivalues6['volume'])*0.000001,ndigits=2)
        topoioi6 = round(float(topoivalues6['position'])*0.000001,ndigits=2)
        topoivolpcr6 = topoivalues6['volumeCallPutRatio']
        topoipospcr6 = topoivalues6['positionCallPutRatio']



        topoi7 = topoidata[6]
        topoiticker7 = topoi7['ticker']
        topoisym7 = topoiticker7['symbol']
        topoiprice7 = topoiticker7['close']
        topoichange7 = round(float(topoiticker7['changeRatio'])*100,ndigits=2)

        topoivalues7 = topoi7['values']
        topoivol7 = round(float(topoivalues7['volume'])*0.000001,ndigits=2)
        topoioi7 = round(float(topoivalues7['position'])*0.000001,ndigits=2)
        topoivolpcr7 = topoivalues7['volumeCallPutRatio']
        topoipospcr7 = topoivalues7['positionCallPutRatio']



        topoi8 = topoidata[7]
        topoiticker8 = topoi8['ticker']
        topoisym8 = topoiticker8['symbol']
        topoiprice8 = topoiticker8['close']
        topoichange8 = round(float(topoiticker8['changeRatio'])*100,ndigits=2)

        topoivalues8 = topoi8['values']
        topoivol8 = round(float(topoivalues8['volume'])*0.000001,ndigits=2)
        topoioi8 = round(float(topoivalues8['position'])*0.000001,ndigits=2)
        topoivolpcr8 = topoivalues8['volumeCallPutRatio']
        topoipospcr8 = topoivalues8['positionCallPutRatio']



        topoi9 = topoidata[8]
        topoiticker9 = topoi9['ticker']
        topoisym9 = topoiticker9['symbol']
        topoiprice9 = topoiticker9['close']
        topoichange9 = round(float(topoiticker9['changeRatio'])*100,ndigits=2)

        topoivalues9 = topoi9['values']
        topoivol9 = round(float(topoivalues9['volume'])*0.000001,ndigits=2)
        topoioi9 = round(float(topoivalues9['position'])*0.000001,ndigits=2)
        topoivolpcr9 = topoivalues9['volumeCallPutRatio']
        topoipospcr9 = topoivalues9['positionCallPutRatio']



        topoi10 = topoidata[9]
        topoiticker10 = topoi10['ticker']
        topoisym10 = topoiticker10['symbol']
        topoiprice10 = topoiticker10['close']
        topoichange10 = round(float(topoiticker10['changeRatio'])*100,ndigits=2)

        topoivalues10 = topoi10['values']
        topoivol10 = round(float(topoivalues10['volume'])*0.000001,ndigits=2)
        topoioi10 = round(float(topoivalues10['position'])*0.000001,ndigits=2)
        topoivolpcr10 = topoivalues10['volumeCallPutRatio']
        topoipospcr10 = topoivalues10['positionCallPutRatio']


        super().__init__(
            placeholder="🇹 🇴 🇵 🎯 🇴 🇵 🇪 🇳 🇮 🇳 🇹",
            min_values=1,
            max_values=1,
            custom_id="topoidrop",
            options = [ 
                disnake.SelectOption(label=f"{topoiticker1} | Vol: {topoivol1} million | OI: {topoioi1} million",description=f"Volume PCR: {topoivolpcr1} | OI PCR: {topoipospcr1}"),
                disnake.SelectOption(label=f"{topoiticker2} | Vol: {topoivol2} million | OI: {topoioi2} million",description=f"Volume PCR: {topoivolpcr2} | OI PCR: {topoipospcr2}"),
                disnake.SelectOption(label=f"{topoiticker3} | Vol: {topoivol3} million | OI: {topoioi3} million",description=f"Volume PCR: {topoivolpcr3} | OI PCR: {topoipospcr3}"),
                disnake.SelectOption(label=f"{topoiticker4} | Vol: {topoivol4} million | OI: {topoioi4} million",description=f"Volume PCR: {topoivolpcr4} | OI PCR: {topoipospcr4}"),
                disnake.SelectOption(label=f"{topoiticker5} | Vol: {topoivol5} million | OI: {topoioi5} million",description=f"Volume PCR: {topoivolpcr5} | OI PCR: {topoipospcr5}"),
                disnake.SelectOption(label=f"{topoiticker6} | Vol: {topoivol6} million | OI: {topoioi6} million",description=f"Volume PCR: {topoivolpcr6} | OI PCR: {topoipospcr6}"),
                disnake.SelectOption(label=f"{topoiticker7} | Vol: {topoivol7} million | OI: {topoioi7} million",description=f"Volume PCR: {topoivolpcr7} | OI PCR: {topoipospcr7}"),
                disnake.SelectOption(label=f"{topoiticker8} | Vol: {topoivol8} million |  OI: {topoioi8} million",description=f"Volume PCR: {topoivolpcr8} | OI PCR: {topoipospcr8}"),
                disnake.SelectOption(label=f"{topoiticker9} | Vol: {topoivol9} million | OI: {topoioi9} million",description=f"Volume PCR: {topoivolpcr9} | OI PCR: {topoipospcr9}"),
                disnake.SelectOption(label=f"{topoiticker10} | Vol: {topoivol10} million | OI: {topoioi10} million",description=f"Volume PCR: {topoivolpcr10} | OI PCR: {topoipospcr10}"),

            ]
        )
    async def callback(self, interaction: disnake.MessageCommandInteraction):
        if self.values[0] == self.values[0]:
            await interaction.response.edit_message(view = MarketMainView())





class TopVolDrop(disnake.ui.Select):
    def __init__(self):
        topvol = requests.get(url="https://quotes-gw.webullfintech.com/api/wlas/option/rank/list?regionId=6&rankType=volume&pageIndex=1&pageSize=50").json()
        topvoldata = topvol['data']
        topvol1 = topvoldata[0]
        topvolderiv1 = topvol1['derivative']
        topvolvalues1 = topvol1['values']

        topvoldir1 = topvolderiv1['direction']
        topvolexp1 = topvolderiv1['expireDate']
        topvolstrike1 = topvolderiv1['strikePrice']
        topvolprice1 = topvolderiv1['price']
        topvolchange1 = round(float(topvolderiv1['changeRatio'])*100,ndigits=2)

        topvoliv1 = topvolvalues1['implVol']
        topvoloichange1 = topvolvalues1['positionChange']
        topvolmid1 = topvolvalues1['middlePrice']
        topvolsym1 = topvolderiv1['unSymbol']
        topvolvol1 = topvolvalues1['volume']
        topvoloi1 = topvolvalues1['position']





        topvol2 = topvoldata[1]
        topvolderiv2 = topvol2['derivative']
        topvolvalues2 = topvol2['values']

        topvoldir2 = topvolderiv2['direction']
        topvolexp2 = topvolderiv2['expireDate']
        topvolstrike2 = topvolderiv2['strikePrice']
        topvolsym2 = topvolderiv2['unSymbol']
        topvolprice2 = topvolderiv2['price']
        topvolchange2 = round(float(topvolderiv2['changeRatio'])*100,ndigits=2)

        topvoliv2 = topvolvalues2['implVol']
        topvoloichange2 = topvolvalues2['positionChange']
        topvolmid2 = topvolvalues2['middlePrice']
        topvolvol2 = topvolvalues2['volume']
        topvoloi2 = topvolvalues2['position']





        topvol3 = topvoldata[2]
        topvolderiv3 = topvol3['derivative']
        topvolvalues3 = topvol3['values']

        topvoldir3 = topvolderiv3['direction']
        topvolexp3 = topvolderiv3['expireDate']
        topvolstrike3 = topvolderiv3['strikePrice']
        topvolsym3 = topvolderiv3['unSymbol']
        topvolprice3 = topvolderiv3['price']
        topvolchange3 = round(float(topvolderiv3['changeRatio'])*100,ndigits=2)

        topvoliv3 = topvolvalues3['implVol']
        topvoloichange3 = topvolvalues3['positionChange']
        topvolmid3 = topvolvalues3['middlePrice']
        topvolvol3 = topvolvalues3['volume']
        topvoloi3 = topvolvalues3['position']


        topvol4 = topvoldata[3]
        topvolderiv4 = topvol4['derivative']
        topvolvalues4 = topvol4['values']

        topvoldir4 = topvolderiv4['direction']
        topvolexp4 = topvolderiv4['expireDate']
        topvolstrike4 = topvolderiv4['strikePrice']
        topvolsym4 = topvolderiv4['unSymbol']
        topvolprice4 = topvolderiv4['price']
        topvolchange4 = round(float(topvolderiv4['changeRatio'])*100,ndigits=2)

        topvoliv4 = topvolvalues4['implVol']
        topvoloichange4 = topvolvalues4['positionChange']
        topvolmid4 = topvolvalues4['middlePrice']
        topvolvol4 = topvolvalues4['volume']
        topvoloi4 = topvolvalues4['position']



        topvol5 = topvoldata[4]
        topvolderiv5 = topvol5['derivative']
        topvolvalues5 = topvol5['values']

        topvoldir5 = topvolderiv5['direction']
        topvolexp5 = topvolderiv5['expireDate']
        topvolstrike5 = topvolderiv5['strikePrice']
        topvolsym5 = topvolderiv5['unSymbol']
        topvolprice5 = topvolderiv5['price']
        topvolchange5 = round(float(topvolderiv5['changeRatio'])*100,ndigits=2)

        topvoliv5 = topvolvalues5['implVol']
        topvoloichange5 = topvolvalues5['positionChange']
        topvolmid5 = topvolvalues5['middlePrice']
        topvolvol5 = topvolvalues5['volume']
        topvoloi5 = topvolvalues5['position']



        topvol6 = topvoldata[5]
        topvolderiv6 = topvol6['derivative']
        topvolvalues6 = topvol6['values']

        topvoldir6 = topvolderiv6['direction']
        topvolexp6 = topvolderiv6['expireDate']
        topvolstrike6 = topvolderiv6['strikePrice']
        topvolsym6 = topvolderiv6['unSymbol']
        topvolprice6 = topvolderiv6['price']
        topvolchange6 = round(float(topvolderiv6['changeRatio'])*100,ndigits=2)

        topvoliv6 = topvolvalues6['implVol']
        topvoloichange6 = topvolvalues6['positionChange']
        topvolmid6 = topvolvalues6['middlePrice']
        topvolvol6 = topvolvalues6['volume']
        topvoloi6 = topvolvalues6['position']



        topvol7 = topvoldata[6]
        topvolderiv7 = topvol7['derivative']
        topvolvalues7 = topvol7['values']

        topvoldir7 = topvolderiv7['direction']
        topvolexp7 = topvolderiv7['expireDate']
        topvolstrike7 = topvolderiv7['strikePrice']
        topvolsym7 = topvolderiv7['unSymbol']
        topvolprice7 = topvolderiv7['price']
        topvolchange7 = round(float(topvolderiv7['changeRatio'])*100,ndigits=2)

        topvoliv7 = topvolvalues7['implVol']
        topvoloichange7 = topvolvalues7['positionChange']
        topvolmid7 = topvolvalues7['middlePrice']
        topvolvol7 = topvolvalues7['volume']
        topvoloi7 = topvolvalues7['position']


        topvol8 = topvoldata[7]
        topvolderiv8 = topvol8['derivative']
        topvolvalues8 = topvol8['values']

        topvoldir8 = topvolderiv8['direction']
        topvolexp8 = topvolderiv8['expireDate']
        topvolstrike8 = topvolderiv8['strikePrice']
        topvolsym8 = topvolderiv8['unSymbol']
        topvolprice8 = topvolderiv8['price']
        topvolchange8 = round(float(topvolderiv8['changeRatio'])*100,ndigits=2)

        topvoliv8 = topvolvalues8['implVol']
        topvoloichange8 = topvolvalues8['positionChange']
        topvolmid8 = topvolvalues8['middlePrice']
        topvolvol8 = topvolvalues8['volume']
        topvoloi8 = topvolvalues8['position']



        topvol9 = topvoldata[8]
        topvolderiv9 = topvol9['derivative']
        topvolvalues9 = topvol9['values']

        topvoldir9 = topvolderiv9['direction']
        topvolexp9 = topvolderiv9['expireDate']
        topvolsym9 = topvolderiv9['unSymbol']
        topvolstrike9 = topvolderiv9['strikePrice']
        topvolprice9 = topvolderiv9['price']
        topvolchange9 = round(float(topvolderiv9['changeRatio'])*100,ndigits=2)

        topvoliv9 = topvolvalues9['implVol']
        topvoloichange9 = topvolvalues9['positionChange']
        topvolmid9 = topvolvalues9['middlePrice']
        topvolvol9 = topvolvalues9['volume']
        topvoloi9 = topvolvalues9['position']


        topvol10 = topvoldata[9]
        topvolderiv10 = topvol10['derivative']
        topvolvalues10 = topvol10['values']

        topvoldir10 = topvolderiv10['direction']
        topvolexp10 = topvolderiv10['expireDate']
        topvolsym10 = topvolderiv10['unSymbol']
        topvolstrike10 = topvolderiv10['strikePrice']
        topvolprice10 = topvolderiv10['price']
        topvolchange10 = round(float(topvolderiv10['changeRatio'])*100,ndigits=2)

        topvoliv10 = topvolvalues10['implVol']
        topvoloichange10 = topvolvalues10['positionChange']
        topvolmid10 = topvolvalues10['middlePrice']
        topvolvol10 = topvolvalues10['volume']
        topvoloi10 = topvolvalues10['position']


        super().__init__(
            placeholder="🇹 🇴 🇵 🎯 🇻 🇴 🇱 🇺 🇲 🇪",
            min_values=1,
            max_values=1,
            custom_id="topvoldrop",
            options = [ 
                disnake.SelectOption(label=f"{topvolsym1} ${topvolstrike1} {topvoldir1} Exp: {topvolexp1} IV: {topvoliv1}% Price: ${topvolprice1}",description=f"Vol: {topvolvol1} million | OI: {topvoloi1} million | OI Change: {topvoloichange1}"),
                disnake.SelectOption(label=f"{topvolsym2} ${topvolstrike2} {topvoldir2} Exp: {topvolexp2} IV: {topvoliv2}% Price: ${topvolprice2}",description=f"Vol: {topvolvol2} million | OI: {topvoloi2} million | OI Change: {topvoloichange2}"),
                disnake.SelectOption(label=f"{topvolsym3} ${topvolstrike3} {topvoldir3} Exp: {topvolexp3} IV: {topvoliv3}% Price: ${topvolprice3}",description=f"Vol: {topvolvol3} million | OI: {topvoloi3} million | OI Change: {topvoloichange3}"),
                disnake.SelectOption(label=f"{topvolsym4} ${topvolstrike4} {topvoldir4} Exp: {topvolexp4} IV: {topvoliv4}% Price: ${topvolprice4}",description=f"Vol: {topvolvol4} million | OI: {topvoloi4} million | OI Change: {topvoloichange4}"),
                disnake.SelectOption(label=f"{topvolsym5} ${topvolstrike5} {topvoldir5} Exp: {topvolexp5} IV: {topvoliv5}% Price: ${topvolprice5}",description=f"Vol: {topvolvol5} million | OI: {topvoloi5} million | OI Change: {topvoloichange5}"),
                disnake.SelectOption(label=f"{topvolsym6} ${topvolstrike6} {topvoldir6} Exp: {topvolexp6} IV: {topvoliv6}% Price: ${topvolprice6}",description=f"Vol: {topvolvol6} million | OI: {topvoloi6} million | OI Change: {topvoloichange6}"),
                disnake.SelectOption(label=f"{topvolsym7} ${topvolstrike7} {topvoldir7} Exp: {topvolexp7} IV: {topvoliv7}% Price: ${topvolprice7}",description=f"Vol: {topvolvol7} million | OI: {topvoloi7} million | OI Change: {topvoloichange7}"),
                disnake.SelectOption(label=f"{topvolsym8} ${topvolstrike8} {topvoldir8} Exp: {topvolexp8} IV: {topvoliv8}% Price: ${topvolprice8}",description=f"Vol: {topvolvol8} million | OI: {topvoloi8} million | OI Change: {topvoloichange8}"),
                disnake.SelectOption(label=f"{topvolsym9} ${topvolstrike9} {topvoldir9} Exp: {topvolexp9} IV: {topvoliv9}% Price: ${topvolprice9}",description=f"Vol: {topvolvol9} million | OI: {topvoloi9} million | OI Change: {topvoloichange9}"),
                disnake.SelectOption(label=f"{topvolsym10} ${topvolstrike10} {topvoldir10} Exp: {topvolexp10} IV: {topvoliv10}% Price: ${topvolprice10}",description=f"Vol: {topvolvol10} million | OI: {topvoloi10} million | OI Change: {topvoloichange10}"),



            ]
        )
    async def callback(self, interaction: disnake.MessageCommandInteraction):
        if self.values[0] == self.values[0]:
            await interaction.response.edit_message(view = MarketMainView())




class TopOIUp(disnake.ui.Select):
    def __init__(self):
        topoiup= requests.get(url="https://quotes-gw.webullfintech.com/api/wlas/option/rank/list?regionId=6&rankType=posIncrease&pageIndex=1&pageSize=50").json()
        topoiupdata = topoiup['data']
        topvol1 = topoiupdata[0]
        self.topvolderiv1 = topvol1['derivative']
        self.topvolvalues1 = topvol1['values']

        self.topvoldir1 = self.topvolderiv1['direction']
        self.topvolexp1 = self.topvolderiv1['expireDate']
        self.topvolstrike1 = self.topvolderiv1['strikePrice']
        self.topvolprice1 = self.topvolderiv1['price']
        self.topvolchange1 = round(float(self.topvolderiv1['changeRatio'])*100,ndigits=2)

        self.topvoliv1 = self.topvolvalues1['implVol']
        self.topvoloichange1 = self.topvolvalues1['positionChange']
        self.topvolmid1 = self.topvolvalues1['middlePrice']
        self.topvolsym1 = self.topvolderiv1['unSymbol']
        self.topvolvol1 = self.topvolvalues1['volume']
        self.topvoloi1 = self.topvolvalues1['position']





        topvol2 = topoiupdata[1]
        self.topvolderiv2 = topvol2['derivative']
        self.topvolvalues2 = topvol2['values']

        self.topvoldir2 = self.topvolderiv2['direction']
        self.topvolexp2 = self.topvolderiv2['expireDate']
        self.topvolstrike2 = self.topvolderiv2['strikePrice']
        self.topvolsym2 = self.topvolderiv2['unSymbol']
        self.topvolprice2 = self.topvolderiv2['price']
        self.topvolchange2 = round(float(self.topvolderiv2['changeRatio'])*100,ndigits=2)

        self.topvoliv2 = self.topvolvalues2['implVol']
        self.topvoloichange2 = self.topvolvalues2['positionChange']
        self.topvolmid2 = self.topvolvalues2['middlePrice']
        self.topvolvol2 = self.topvolvalues2['volume']
        self.topvoloi2 = self.topvolvalues2['position']





        self.topvol3 = topoiupdata[2]
        self.topvolderiv3 = self.topvol3['derivative']
        self.topvolvalues3 = self.topvol3['values']

        self.topvoldir3 = self.topvolderiv3['direction']
        self.topvolexp3 = self.topvolderiv3['expireDate']
        self.topvolstrike3 = self.topvolderiv3['strikePrice']
        self.topvolsym3 = self.topvolderiv3['unSymbol']
        self.topvolprice3 = self.topvolderiv3['price']
        self.topvolchange3 = round(float(self.topvolderiv3['changeRatio'])*100,ndigits=2)

        self.topvoliv3 = self.topvolvalues3['implVol']
        self.topvoloichange3 = self.topvolvalues3['positionChange']
        self.topvolmid3 = self.topvolvalues3['middlePrice']
        self.topvolvol3 = self.topvolvalues3['volume']
        self.topvoloi3 = self.topvolvalues3['position']


        self.topvol4 = topoiupdata[3]
        self.topvolderiv4 = self.topvol4['derivative']
        self.topvolvalues4 = self.topvol4['values']

        self.topvoldir4 = self.topvolderiv4['direction']
        self.topvolexp4 = self.topvolderiv4['expireDate']
        self.topvolstrike4 = self.topvolderiv4['strikePrice']
        self.topvolsym4 = self.topvolderiv4['unSymbol']
        self.topvolprice4 = self.topvolderiv4['price']
        self.topvolchange4 = round(float(self.topvolderiv4['changeRatio'])*100,ndigits=2)

        self.topvoliv4 = self.topvolvalues4['implVol']
        self.topvoloichange4 = self.topvolvalues4['positionChange']
        self.topvolmid4 = self.topvolvalues4['middlePrice']
        self.topvolvol4 = self.topvolvalues4['volume']
        self.topvoloi4 = self.topvolvalues4['position']



        self.topvol5 = topoiupdata[4]
        self.topvolderiv5 = self.topvol5['derivative']
        self.topvolvalues5 = self.topvol5['values']

        self.topvoldir5 = self.topvolderiv5['direction']
        self.topvolexp5 = self.topvolderiv5['expireDate']
        self.topvolstrike5 = self.topvolderiv5['strikePrice']
        self.topvolsym5 = self.topvolderiv5['unSymbol']
        self.topvolprice5 = self.topvolderiv5['price']
        self.topvolchange5 = round(float(self.topvolderiv5['changeRatio'])*100,ndigits=2)

        self.topvoliv5 = self.topvolvalues5['implVol']
        self.topvoloichange5 = self.topvolvalues5['positionChange']
        self.topvolmid5 = self.topvolvalues5['middlePrice']
        self.topvolvol5 = self.topvolvalues5['volume']
        self.topvoloi5 = self.topvolvalues5['position']



        self.topvol6 = topoiupdata[5]
        self.topvolderiv6 = self.topvol6['derivative']
        self.topvolvalues6 = self.topvol6['values']

        self.topvoldir6 = self.topvolderiv6['direction']
        self.topvolexp6 = self.topvolderiv6['expireDate']
        self.topvolstrike6 = self.topvolderiv6['strikePrice']
        self.topvolsym6 = self.topvolderiv6['unSymbol']
        self.topvolprice6 = self.topvolderiv6['price']
        self.topvolchange6 = round(float(self.topvolderiv6['changeRatio'])*100,ndigits=2)

        self.topvoliv6 = self.topvolvalues6['implVol']
        self.topvoloichange6 = self.topvolvalues6['positionChange']
        self.topvolmid6 = self.topvolvalues6['middlePrice']
        self.topvolvol6 = self.topvolvalues6['volume']
        self.topvoloi6 = self.topvolvalues6['position']



        self.topvol7 = topoiupdata[6]
        self.topvolderiv7 = self.topvol7['derivative']
        self.topvolvalues7 = self.topvol7['values']

        self.topvoldir7 = self.topvolderiv7['direction']
        self.topvolexp7 = self.topvolderiv7['expireDate']
        self.topvolstrike7 = self.topvolderiv7['strikePrice']
        self.topvolsym7 = self.topvolderiv7['unSymbol']
        self.topvolprice7 = self.topvolderiv7['price']
        self.topvolchange7 = round(float(self.topvolderiv7['changeRatio'])*100,ndigits=2)

        self.topvoliv7 = self.topvolvalues7['implVol']
        self.topvoloichange7 = self.topvolvalues7['positionChange']
        self.topvolmid7 = self.topvolvalues7['middlePrice']
        self.topvolvol7 = self.topvolvalues7['volume']
        self.topvoloi7 = self.topvolvalues7['position']


        self.topvol8 = topoiupdata[7]
        self.topvolderiv8 = self.topvol8['derivative']
        self.topvolvalues8 = self.topvol8['values']

        self.topvoldir8 = self.topvolderiv8['direction']
        self.topvolexp8 = self.topvolderiv8['expireDate']
        self.topvolstrike8 = self.topvolderiv8['strikePrice']
        self.topvolsym8 = self.topvolderiv8['unSymbol']
        self.topvolprice8 = self.topvolderiv8['price']
        self.topvolchange8 = round(float(self.topvolderiv8['changeRatio'])*100,ndigits=2)

        self.topvoliv8 = self.topvolvalues8['implVol']
        self.topvoloichange8 = self.topvolvalues8['positionChange']
        self.topvolmid8 = self.topvolvalues8['middlePrice']
        self.topvolvol8 = self.topvolvalues8['volume']
        self.topvoloi8 = self.topvolvalues8['position']



        self.topvol9 = topoiupdata[8]
        self.topvolderiv9 = self.topvol9['derivative']
        self.topvolvalues9 = self.topvol9['values']

        self.topvoldir9 = self.topvolderiv9['direction']
        self.topvolexp9 = self.topvolderiv9['expireDate']
        self.topvolsym9 = self.topvolderiv9['unSymbol']
        self.topvolstrike9 = self.topvolderiv9['strikePrice']
        self.topvolprice9 = self.topvolderiv9['price']
        self.topvolchange9 = round(float(self.topvolderiv9['changeRatio'])*100,ndigits=2)

        self.topvoliv9 = self.topvolvalues9['implVol']
        self.topvoloichange9 = self.topvolvalues9['positionChange']
        self.topvolmid9 = self.topvolvalues9['middlePrice']
        self.topvolvol9 = self.topvolvalues9['volume']
        self.topvoloi9 = self.topvolvalues9['position']


        self.topvol10 = topoiupdata[9]
        self.topvolderiv10 = self.topvol10['derivative']
        self.topvolvalues10 = self.topvol10['values']

        self.topvoldir10 = self.topvolderiv10['direction']
        self.topvolexp10 = self.topvolderiv10['expireDate']
        self.topvolsym10 = self.topvolderiv10['unSymbol']
        self.topvolstrike10 = self.topvolderiv10['strikePrice']
        self.topvolprice10 = self.topvolderiv10['price']
        self.topvolchange10 = round(float(self.topvolderiv10['changeRatio'])*100,ndigits=2)

        self.topvoliv10 = self.topvolvalues10['implVol']
        self.topvoloichange10 = self.topvolvalues10['positionChange']
        self.topvolmid10 = self.topvolvalues10['middlePrice']
        self.topvolvol10 = self.topvolvalues10['volume']
        self.topvoloi10 = self.topvolvalues10['position']
        super().__init__(
            placeholder="🇹 🇴 🇵 🎯 🇴 🇮 | 🇮 🇳 🇨 🇷 🇪 🇦 🇸 🇪",
            min_values=1,
            max_values=1,
            custom_id="topoiincreasedrop",
            options = [ 
                disnake.SelectOption(label=f"{self.topvolsym1} ${self.topvolstrike1} {self.topvoldir1} {self.topvolexp1} OI Change: {self.topvoloichange1}| Price: {self.topvolprice1}",description=f"Change On Day: {self.topvolchange1}% | Vol: {self.topvolvol1} | OI: {self.topvoloi1}"),
                disnake.SelectOption(label=f"{self.topvolsym2} ${self.topvolstrike2} {self.topvoldir2} {self.topvolexp2} OI Change: {self.topvoloichange2}| Price: {self.topvolprice2}",description=f"Change On Day: {self.topvolchange2}% | Vol: {self.topvolvol2} | OI: {self.topvoloi2}"),
                disnake.SelectOption(label=f"{self.topvolsym3} ${self.topvolstrike3} {self.topvoldir3} {self.topvolexp3} OI Change: {self.topvoloichange3}| Price: {self.topvolprice3}",description=f"Change On Day: {self.topvolchange3}% | Vol: {self.topvolvol3} | OI: {self.topvoloi3}"),
                disnake.SelectOption(label=f"{self.topvolsym4} ${self.topvolstrike4} {self.topvoldir4} {self.topvolexp4} OI Change: {self.topvoloichange4}| Price: {self.topvolprice4}",description=f"Change On Day: {self.topvolchange4}% | Vol: {self.topvolvol4} | OI: {self.topvoloi4}"),
                disnake.SelectOption(label=f"{self.topvolsym5} ${self.topvolstrike5} {self.topvoldir5} {self.topvolexp5} OI Change: {self.topvoloichange5}| Price: {self.topvolprice5}",description=f"Change On Day: {self.topvolchange5}% | Vol: {self.topvolvol5} | OI: {self.topvoloi5}"),
                disnake.SelectOption(label=f"{self.topvolsym6} ${self.topvolstrike6} {self.topvoldir6} {self.topvolexp6} OI Change: {self.topvoloichange6}| Price: {self.topvolprice6}",description=f"Change On Day: {self.topvolchange6}% | Vol: {self.topvolvol6} | OI: {self.topvoloi6}"),
                disnake.SelectOption(label=f"{self.topvolsym7} ${self.topvolstrike7} {self.topvoldir7} {self.topvolexp7} OI Change: {self.topvoloichange7}| Price: {self.topvolprice7}",description=f"Change On Day: {self.topvolchange7}% | Vol: {self.topvolvol7} | OI: {self.topvoloi7}"),
                disnake.SelectOption(label=f"{self.topvolsym8} ${self.topvolstrike8} {self.topvoldir8} {self.topvolexp8} OI Change: {self.topvoloichange8}| Price: {self.topvolprice8}",description=f"Change On Day: {self.topvolchange8}% | Vol: {self.topvolvol8} | OI: {self.topvoloi8}"),
                disnake.SelectOption(label=f"{self.topvolsym9} ${self.topvolstrike9} {self.topvoldir9} {self.topvolexp9} OI Change: {self.topvoloichange9}| Price: {self.topvolprice9}",description=f"Change On Day: {self.topvolchange9}% | Vol: {self.topvolvol9} | OI: {self.topvoloi9}"),
                disnake.SelectOption(label=f"{self.topvolsym10} ${self.topvolstrike10} {self.topvoldir10} {self.topvolexp10} OI Change: {self.topvoloichange10}| Price: {self.topvolprice10}",description=f"Change On Day: {self.topvolchange10}% | Vol: {self.topvolvol10} | OI: {self.topvoloi10}"),
            ]
        )
    async def callback(self, interaction: disnake.MessageCommandInteraction):
        if self.values[0] == self.values[0]:
            await interaction.response.defer(with_message=True)
            em = disnake.Embed(title="Top OI Increase Contracts",color=disnake.Colour.dark_gold())
            em.add_field(name=f"{TopOIUp().topvolsym1} ${TopOIUp().topvolstrike1} {TopOIUp().topvoldir1} {TopOIUp().topvolexp1}",value=f"```py\nContract Stats:\nOI Change: {TopOIUp().topvoloichange1}\nPrice: {TopOIUp().topvolprice1}\nChange On Day: {TopOIUp().topvolchange1}% \nVol: {TopOIUp().topvolvol1} \nOI: {TopOIUp().topvoloi1}")
            em.add_field(name=f"{TopOIUp().topvolsym2} ${TopOIUp().topvolstrike2} {TopOIUp().topvoldir2} {TopOIUp().topvolexp2}",value=f"```py\nContract Stats:\nOI Change: {TopOIUp().topvoloichange2}\nPrice: {TopOIUp().topvolprice2}\nChange On Day: {TopOIUp().topvolchange2}% \nVol: {TopOIUp().topvolvol2} \nOI: {TopOIUp().topvoloi2}```")
            em.add_field(name=f"{TopOIUp().topvolsym3} ${TopOIUp().topvolstrike3} {TopOIUp().topvoldir3} {TopOIUp().topvolexp3}",value=f"```py\nContract Stats:\nOI Change: {TopOIUp().topvoloichange3}\nPrice: {TopOIUp().topvolprice3}\nChange On Day: {TopOIUp().topvolchange3}% \nVol: {TopOIUp().topvolvol3} \nOI: {TopOIUp().topvoloi3}```")
            em.add_field(name=f"{TopOIUp().topvolsym4} ${TopOIUp().topvolstrike4} {TopOIUp().topvoldir4} {TopOIUp().topvolexp4}",value=f"```py\nContract Stats:\nOI Change: {TopOIUp().topvoloichange4}\nPrice: {TopOIUp().topvolprice4}\nChange On Day: {TopOIUp().topvolchange4}% \nVol: {TopOIUp().topvolvol4} \nOI: {TopOIUp().topvoloi4}```")
            em.add_field(name=f"{TopOIUp().topvolsym5} ${TopOIUp().topvolstrike5} {TopOIUp().topvoldir5} {TopOIUp().topvolexp5}",value=f"```py\nContract Stats:\nOI Change: {TopOIUp().topvoloichange5}\nPrice: {TopOIUp().topvolprice5}\nChange On Day: {TopOIUp().topvolchange5}% \nVol: {TopOIUp().topvolvol5} \nOI: {TopOIUp().topvoloi5}```")
            em.add_field(name=f"{TopOIUp().topvolsym6} ${TopOIUp().topvolstrike6} {TopOIUp().topvoldir6} {TopOIUp().topvolexp6}",value=f"```py\nContract Stats:\nOI Change: {TopOIUp().topvoloichange6}\nPrice: {TopOIUp().topvolprice6}\nChange On Day: {TopOIUp().topvolchange6}% \nVol: {TopOIUp().topvolvol6} \nOI: {TopOIUp().topvoloi6}```")
            em.add_field(name=f"{TopOIUp().topvolsym7} ${TopOIUp().topvolstrike7} {TopOIUp().topvoldir7} {TopOIUp().topvolexp7}",value=f"```py\nContract Stats:\nOI Change: {TopOIUp().topvoloichange7}\nPrice: {TopOIUp().topvolprice7}\nChange On Day: {TopOIUp().topvolchange7}% \nVol: {TopOIUp().topvolvol7} \nOI: {TopOIUp().topvoloi7}```")
            em.add_field(name=f"{TopOIUp().topvolsym8} ${TopOIUp().topvolstrike8} {TopOIUp().topvoldir8} {TopOIUp().topvolexp8}",value=f"```py\nContract Stats:\nOI Change: {TopOIUp().topvoloichange8}\nPrice: {TopOIUp().topvolprice8}\nChange On Day: {TopOIUp().topvolchange8}% \nVol: {TopOIUp().topvolvol8} \nOI: {TopOIUp().topvoloi8}```")
            em.add_field(name=f"{TopOIUp().topvolsym9} ${TopOIUp().topvolstrike9} {TopOIUp().topvoldir9} {TopOIUp().topvolexp9}",value=f"```py\nContract Stats:\nOI Change: {TopOIUp().topvoloichange9}\nPrice: {TopOIUp().topvolprice9}\nChange On Day: {TopOIUp().topvolchange9}% \nVol: {TopOIUp().topvolvol9} \nOI: {TopOIUp().topvoloi9}```")
            em.add_field(name=f"{TopOIUp().topvolsym10} ${TopOIUp().topvolstrike10} {TopOIUp().topvoldir10} {TopOIUp().topvolexp10}",value=f"```py\nContract Stats:\nOI Change: {TopOIUp().topvoloichange10}\nPrice: {TopOIUp().topvolprice10}\nChange On Day: {TopOIUp().topvolchange10}% \nVol: {TopOIUp().topvolvol10} \nOI: {TopOIUp().topvoloi10}```")
            await interaction.edit_original_response(embed=em, view = MarketMainView())




class TopOIDown(disnake.ui.Select):
    def __init__(self):
        topoidown= requests.get(url="https://quotes-gw.webullfintech.com/api/wlas/option/rank/list?regionId=6&rankType=posDecrease&pageIndex=1&pageSize=50").json()
        topoiupdata = topoidown['data']
        topvol1 = topoiupdata[0]
        topvolderiv1 = topvol1['derivative']
        topvolvalues1 = topvol1['values']

        topvoldir1 = topvolderiv1['direction']
        topvolexp1 = topvolderiv1['expireDate']
        topvolstrike1 = topvolderiv1['strikePrice']
        topvolprice1 = topvolderiv1['price']
        topvolchange1 = round(float(topvolderiv1['changeRatio'])*100,ndigits=2)

        topvoliv1 = topvolvalues1['implVol']
        topvoloichange1 = topvolvalues1['positionChange']
        topvolmid1 = topvolvalues1['middlePrice']
        topvolsym1 = topvolderiv1['unSymbol']
        topvolvol1 = topvolvalues1['volume']
        topvoloi1 = topvolvalues1['position']





        topvol2 = topoiupdata[1]
        topvolderiv2 = topvol2['derivative']
        topvolvalues2 = topvol2['values']

        topvoldir2 = topvolderiv2['direction']
        topvolexp2 = topvolderiv2['expireDate']
        topvolstrike2 = topvolderiv2['strikePrice']
        topvolsym2 = topvolderiv2['unSymbol']
        topvolprice2 = topvolderiv2['price']
        topvolchange2 = round(float(topvolderiv2['changeRatio'])*100,ndigits=2)

        topvoliv2 = topvolvalues2['implVol']
        topvoloichange2 = topvolvalues2['positionChange']
        topvolmid2 = topvolvalues2['middlePrice']
        topvolvol2 = topvolvalues2['volume']
        topvoloi2 = topvolvalues2['position']





        topvol3 = topoiupdata[2]
        topvolderiv3 = topvol3['derivative']
        topvolvalues3 = topvol3['values']

        topvoldir3 = topvolderiv3['direction']
        topvolexp3 = topvolderiv3['expireDate']
        topvolstrike3 = topvolderiv3['strikePrice']
        topvolsym3 = topvolderiv3['unSymbol']
        topvolprice3 = topvolderiv3['price']
        topvolchange3 = round(float(topvolderiv3['changeRatio'])*100,ndigits=2)

        topvoliv3 = topvolvalues3['implVol']
        topvoloichange3 = topvolvalues3['positionChange']
        topvolmid3 = topvolvalues3['middlePrice']
        topvolvol3 = topvolvalues3['volume']
        topvoloi3 = topvolvalues3['position']


        topvol4 = topoiupdata[3]
        topvolderiv4 = topvol4['derivative']
        topvolvalues4 = topvol4['values']

        topvoldir4 = topvolderiv4['direction']
        topvolexp4 = topvolderiv4['expireDate']
        topvolstrike4 = topvolderiv4['strikePrice']
        topvolsym4 = topvolderiv4['unSymbol']
        topvolprice4 = topvolderiv4['price']
        topvolchange4 = round(float(topvolderiv4['changeRatio'])*100,ndigits=2)

        topvoliv4 = topvolvalues4['implVol']
        topvoloichange4 = topvolvalues4['positionChange']
        topvolmid4 = topvolvalues4['middlePrice']
        topvolvol4 = topvolvalues4['volume']
        topvoloi4 = topvolvalues4['position']



        topvol5 = topoiupdata[4]
        topvolderiv5 = topvol5['derivative']
        topvolvalues5 = topvol5['values']

        topvoldir5 = topvolderiv5['direction']
        topvolexp5 = topvolderiv5['expireDate']
        topvolstrike5 = topvolderiv5['strikePrice']
        topvolsym5 = topvolderiv5['unSymbol']
        topvolprice5 = topvolderiv5['price']
        topvolchange5 = round(float(topvolderiv5['changeRatio'])*100,ndigits=2)

        topvoliv5 = topvolvalues5['implVol']
        topvoloichange5 = topvolvalues5['positionChange']
        topvolmid5 = topvolvalues5['middlePrice']
        topvolvol5 = topvolvalues5['volume']
        topvoloi5 = topvolvalues5['position']



        topvol6 = topoiupdata[5]
        topvolderiv6 = topvol6['derivative']
        topvolvalues6 = topvol6['values']

        topvoldir6 = topvolderiv6['direction']
        topvolexp6 = topvolderiv6['expireDate']
        topvolstrike6 = topvolderiv6['strikePrice']
        topvolsym6 = topvolderiv6['unSymbol']
        topvolprice6 = topvolderiv6['price']
        topvolchange6 = round(float(topvolderiv6['changeRatio'])*100,ndigits=2)

        topvoliv6 = topvolvalues6['implVol']
        topvoloichange6 = topvolvalues6['positionChange']
        topvolmid6 = topvolvalues6['middlePrice']
        topvolvol6 = topvolvalues6['volume']
        topvoloi6 = topvolvalues6['position']



        topvol7 = topoiupdata[6]
        topvolderiv7 = topvol7['derivative']
        topvolvalues7 = topvol7['values']

        topvoldir7 = topvolderiv7['direction']
        topvolexp7 = topvolderiv7['expireDate']
        topvolstrike7 = topvolderiv7['strikePrice']
        topvolsym7 = topvolderiv7['unSymbol']
        topvolprice7 = topvolderiv7['price']
        topvolchange7 = round(float(topvolderiv7['changeRatio'])*100,ndigits=2)

        topvoliv7 = topvolvalues7['implVol']
        topvoloichange7 = topvolvalues7['positionChange']
        topvolmid7 = topvolvalues7['middlePrice']
        topvolvol7 = topvolvalues7['volume']
        topvoloi7 = topvolvalues7['position']


        topvol8 = topoiupdata[7]
        topvolderiv8 = topvol8['derivative']
        topvolvalues8 = topvol8['values']

        topvoldir8 = topvolderiv8['direction']
        topvolexp8 = topvolderiv8['expireDate']
        topvolstrike8 = topvolderiv8['strikePrice']
        topvolsym8 = topvolderiv8['unSymbol']
        topvolprice8 = topvolderiv8['price']
        topvolchange8 = round(float(topvolderiv8['changeRatio'])*100,ndigits=2)

        topvoliv8 = topvolvalues8['implVol']
        topvoloichange8 = topvolvalues8['positionChange']
        topvolmid8 = topvolvalues8['middlePrice']
        topvolvol8 = topvolvalues8['volume']
        topvoloi8 = topvolvalues8['position']



        topvol9 = topoiupdata[8]
        topvolderiv9 = topvol9['derivative']
        topvolvalues9 = topvol9['values']

        topvoldir9 = topvolderiv9['direction']
        topvolexp9 = topvolderiv9['expireDate']
        topvolsym9 = topvolderiv9['unSymbol']
        topvolstrike9 = topvolderiv9['strikePrice']
        topvolprice9 = topvolderiv9['price']
        topvolchange9 = round(float(topvolderiv9['changeRatio'])*100,ndigits=2)

        topvoliv9 = topvolvalues9['implVol']
        topvoloichange9 = topvolvalues9['positionChange']
        topvolmid9 = topvolvalues9['middlePrice']
        topvolvol9 = topvolvalues9['volume']
        topvoloi9 = topvolvalues9['position']


        topvol10 = topoiupdata[9]
        topvolderiv10 = topvol10['derivative']
        topvolvalues10 = topvol10['values']

        topvoldir10 = topvolderiv10['direction']
        topvolexp10 = topvolderiv10['expireDate']
        topvolsym10 = topvolderiv10['unSymbol']
        topvolstrike10 = topvolderiv10['strikePrice']
        topvolprice10 = topvolderiv10['price']
        topvolchange10 = round(float(topvolderiv10['changeRatio'])*100,ndigits=2)

        topvoliv10 = topvolvalues10['implVol']
        topvoloichange10 = topvolvalues10['positionChange']
        topvolmid10 = topvolvalues10['middlePrice']
        topvolvol10 = topvolvalues10['volume']
        topvoloi10 = topvolvalues10['position']

        super().__init__(
            placeholder="🇹 🇴 🇵 🎯 🇴 🇮 | 🇩 🇪 🇨 🇷 🇪 🇦 🇸 🇪",
            min_values=1,
            max_values=1,
            custom_id="topoiincreasedrop",
            options = [ 
                disnake.SelectOption(label=f"{topvolsym1} ${topvolstrike1} {topvoldir1} {topvolexp1} OI Change: {topvoloichange1}| Price: {topvolprice1}",description=f"Change On Day: {topvolchange1}% | Vol: {topvolvol1} | OI: {topvoloi1}"),
                disnake.SelectOption(label=f"{topvolsym2} ${topvolstrike2} {topvoldir2} {topvolexp2} OI Change: {topvoloichange2}| Price: {topvolprice2}",description=f"Change On Day: {topvolchange2}% | Vol: {topvolvol2} | OI: {topvoloi2}"),
                disnake.SelectOption(label=f"{topvolsym3} ${topvolstrike3} {topvoldir3} {topvolexp3} OI Change: {topvoloichange3}| Price: {topvolprice3}",description=f"Change On Day: {topvolchange3}% | Vol: {topvolvol3} | OI: {topvoloi3}"),
                disnake.SelectOption(label=f"{topvolsym4} ${topvolstrike4} {topvoldir4} {topvolexp4} OI Change: {topvoloichange4}| Price: {topvolprice4}",description=f"Change On Day: {topvolchange4}% | Vol: {topvolvol4} | OI: {topvoloi4}"),
                disnake.SelectOption(label=f"{topvolsym5} ${topvolstrike5} {topvoldir5} {topvolexp5} OI Change: {topvoloichange5}| Price: {topvolprice5}",description=f"Change On Day: {topvolchange5}% | Vol: {topvolvol5} | OI: {topvoloi5}"),
                disnake.SelectOption(label=f"{topvolsym6} ${topvolstrike6} {topvoldir6} {topvolexp6} OI Change: {topvoloichange6}| Price: {topvolprice6}",description=f"Change On Day: {topvolchange6}% | Vol: {topvolvol6} | OI: {topvoloi6}"),
                disnake.SelectOption(label=f"{topvolsym7} ${topvolstrike7} {topvoldir7} {topvolexp7} OI Change: {topvoloichange7}| Price: {topvolprice7}",description=f"Change On Day: {topvolchange7}% | Vol: {topvolvol7} | OI: {topvoloi7}"),
                disnake.SelectOption(label=f"{topvolsym8} ${topvolstrike8} {topvoldir8} {topvolexp8} OI Change: {topvoloichange8}| Price: {topvolprice8}",description=f"Change On Day: {topvolchange8}% | Vol: {topvolvol8} | OI: {topvoloi8}"),
                disnake.SelectOption(label=f"{topvolsym9} ${topvolstrike9} {topvoldir9} {topvolexp9} OI Change: {topvoloichange9}| Price: {topvolprice9}",description=f"Change On Day: {topvolchange9}% | Vol: {topvolvol9} | OI: {topvoloi9}"),
                disnake.SelectOption(label=f"{topvolsym10} ${topvolstrike10} {topvoldir10} {topvolexp10} OI Change: {topvoloichange10}| Price: {topvolprice10}",description=f"Change On Day: {topvolchange10}% | Vol: {topvolvol10} | OI: {topvoloi10}"),
            ]
        )
    async def callback(self, interaction: disnake.MessageCommandInteraction):
        if self.values[0] == self.values[0]:
            await interaction.response.edit_message(view = MarketMainView())