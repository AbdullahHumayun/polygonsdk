"""Leverage Command Dropdown"""
import requests
import disnake
from utils.webull_tickers import ticker_list
from disnake.ext import commands


class LeverageDropdown(disnake.ui.Select):
    def __init__(self, ticker):
        self.ticker = ticker
        ids = ticker_list[ticker]
        r = requests.get(url=f"https://trade.webullfintech.com/api/trading/v1/global/ticker/permission?tickerId={ids}")
        d = r.json()
        permissions = d['permissions']
        tickers = d['ticker']
        self.brokerid1 = permissions[0]
        list2 = permissions[1]
        list3 = permissions[2]
        brokerid2 = list2['brokerId']
        self.shorttype = list2['shortType']
        lotsize = list2['lotSize']
        pricesteps = list2['priceSteps']
        pricesteps2 = list3['priceSteps']
        types = list2['types']
        self.canfract = list2['canFract']
        self.crypto = list2['cryptoTransferAllow']


        leverage = list2['leverage']
        self.tradetype = leverage['tradeType']#
        self.shortType = leverage['shortType']#
        self.tradepolicy = leverage['tradePolicy']#
        dtlongrate = float(leverage['dayTradeLongRate'])
        dtshortrate = float(leverage['dayTradeShortRate'])
        overnightlongrate = float(leverage['overnightLongRate'])
        overnightshortrate = float(leverage['overnightShortRate'])
        self.onlongrate = round(overnightlongrate * 100, ndigits=2)
        self.onshortrate = round(overnightshortrate * 100, ndigits=2)
        shortmaintenance = float(leverage['maintenanceForShort'])
        longmaintenance = float(leverage['maintenanceForLong'])
        lintrate = float(leverage['tradeLongInterestRate'])
        sintrate = float(leverage['tradeShortInterestRate'])
        longrate = float(leverage['longRate'])
        shortrate = float(leverage['shortRate'])


        steps1 = pricesteps[0]
        self.rangebegin = steps1['rangeBegin']#
        self.containBegin = steps1['containBegin']#
        self.rangeend = steps1['rangeEnd']#
        self.containend = steps1['containEnd']#


        steps2 = pricesteps[1]
        self.rangebegin2 = steps2['rangeBegin']#
        self.containBegin2 = steps2['containBegin']#
        self.rangeend2 = steps2['containEnd']#
        self.daytradelonglever = leverage['dayTradeLongLever']#
        self.daytradeshortlever = leverage['dayTradeShortLever']#
        self.overnightlonglever = leverage['overnightLongLever']#
        self.overnightshortlever = leverage['overnightShortLever']#
        self.dayshortrate = round(dtshortrate * 100, ndigits=2)#
        self.daylongrate = round(dtlongrate * 100, ndigits=2)#
        self.longmain = round(longmaintenance * 100, ndigits=2)#
        self.shortmain = round(shortmaintenance * 100, ndigits=2)#
        self.onlongrate = round(overnightlongrate * 100, ndigits=2)#
        self.onshortrate = round(overnightshortrate * 100, ndigits=2)#
        self.shortintrate = round(sintrate * 100, ndigits=2)#
        self.longintrate = round(lintrate * 100, ndigits=2)#
        self.lrate = round(longrate * 100, ndigits=2)#
        self.srate = round(shortrate * 100, ndigits=2)#

        super().__init__(
            placeholder="🇱  🇪  🇻  🇪  🇷  🇦  🇬  🇪",
            min_values=1,
            max_values=1,
            custom_id="🇱  🇪  🇻  🇪  🇷  🇦  🇬  🇪",
            options=[
                disnake.SelectOption(label=f"Trade Type: {self.tradetype}",description=f"Short Type: {self.shorttype} | Policy: {self.tradepolicy}"),
                disnake.SelectOption(label="Base Rates:",description=f"Long: {self.lrate} | Short: {self.srate}"),
                disnake.SelectOption(label="Interest Rates:",description=f"Long: {self.longintrate} | Short: {self.shortintrate}"),
                disnake.SelectOption(label="Daytrading Rates:",description=f"Long: {self.daylongrate} | Short: {self.dayshortrate}"),
                disnake.SelectOption(label="Daytrading Leverage:",description=f"Long: {self.daytradelonglever} | Short: {self.daytradeshortlever}"),
                disnake.SelectOption(label="Overnight Rates:",description=f"Long: {self.onlongrate} | Short: {self.onshortrate}"),
                disnake.SelectOption(label="Maintenance:",description=f"Long: {self.longmain} | Short: {self.shortmain}"),
            
            ]
        )
        async def callback(interaction: disnake.MessageCommandInteraction):
            if self.values[0] == self.values[0]:
                await interaction.send("```py\nDrop-down is for display! Use another command.```")
