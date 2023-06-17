import disnake
import stocksera
from cfg import YOUR_STOCKSERA_KEY
from utils.webull_tickers import ticker_list
client = stocksera.Client(api_key=YOUR_STOCKSERA_KEY)
class LowFloatDropdown(disnake.ui.Select):
    def __init__(self):
        data = client.low_float()
        index0 = data[0]
        index1 = data[1]
        index2 = data[2]
        index3 = data[3]
        index4 = data[4]
        index5 = data[5]
        index6 = data[6]
        index7 = data[7]
        index8 = data[8]
        index9 = data[9]
        index10 = data[10]
        index11 = data[11]
        index12 = data[12]
        index13 = data[13]
        index14 = data[14]
        index15 = data[15]
        index16 = data[16]
        index17 = data[17]
        index18 = data[18]
        index19 = data[19]
        index20 = data[20]
        index21 = data[21]
        index22 = data[22]
        index23 = data[23]
        index24 = data[24]
        ticker0 = index0['ticker']
        ticker1 = index1['ticker']
        ticker2 = index2['ticker']
        ticker3 = index3['ticker']
        ticker4 = index4['ticker']
        ticker5 = index5['ticker']
        ticker6 = index6['ticker']
        ticker7 = index7['ticker']
        ticker8 = index8['ticker']
        ticker9 = index9['ticker']
        ticker10 = index10['ticker']
        ticker11 = index11['ticker']
        ticker12 = index12['ticker']
        ticker13 = index13['ticker']
        ticker14 = index14['ticker']
        ticker15 = index15['ticker']
        ticker16 = index16['ticker']
        ticker17 = index17['ticker']
        ticker18 = index18['ticker']
        ticker19 = index19['ticker']
        ticker20 = index20['ticker']
        ticker21 = index21['ticker']
        ticker22 = index22['ticker']
        ticker23 = index23['ticker']
        ticker24 = index24['ticker']
        floating_shares0 = index0['floating_shares']
        floating_shares1 = index1['floating_shares']
        floating_shares2 = index2['floating_shares']
        floating_shares3 = index3['floating_shares']
        floating_shares4 = index4['floating_shares']
        floating_shares5 = index5['floating_shares']
        floating_shares6 = index6['floating_shares']
        floating_shares7 = index7['floating_shares']
        floating_shares8 = index8['floating_shares']
        floating_shares9 = index9['floating_shares']
        floating_shares10 = index10['floating_shares']
        floating_shares11 = index11['floating_shares']
        floating_shares12 = index12['floating_shares']
        floating_shares13 = index13['floating_shares']
        floating_shares14 = index14['floating_shares']
        floating_shares15 = index15['floating_shares']
        floating_shares16 = index16['floating_shares']
        floating_shares17 = index17['floating_shares']
        floating_shares18 = index18['floating_shares']
        floating_shares19 = index19['floating_shares']
        floating_shares20 = index20['floating_shares']
        floating_shares21 = index21['floating_shares']
        floating_shares22 = index22['floating_shares']
        floating_shares23 = index23['floating_shares']
        floating_shares24 = index24['floating_shares']
        options = [
            disnake.SelectOption(label=f"{ticker0}", description=f"{floating_shares0}"),
            disnake.SelectOption(label=f"{ticker1}", description=f"{floating_shares1}"),
            disnake.SelectOption(label=f"{ticker2}", description=f"{floating_shares2}"),
            disnake.SelectOption(label=f"{ticker3}", description=f"{floating_shares3}"),
            disnake.SelectOption(label=f"{ticker4}", description=f"{floating_shares4}"),
            disnake.SelectOption(label=f"{ticker5}", description=f"{floating_shares5}"),
            disnake.SelectOption(label=f"{ticker6}", description=f"{floating_shares6}"),
            disnake.SelectOption(label=f"{ticker7}", description=f"{floating_shares7}"),
            disnake.SelectOption(label=f"{ticker8}", description=f"{floating_shares8}"),
            disnake.SelectOption(label=f"{ticker9}", description=f"{floating_shares9}"),
            disnake.SelectOption(label=f"{ticker10}", description=f"{floating_shares10}"),
            disnake.SelectOption(label=f"{ticker11}", description=f"{floating_shares11}"),
            disnake.SelectOption(label=f"{ticker12}", description=f"{floating_shares12}"),
            disnake.SelectOption(label=f"{ticker13}", description=f"{floating_shares13}"),
            disnake.SelectOption(label=f"{ticker14}", description=f"{floating_shares14}"),
            disnake.SelectOption(label=f"{ticker15}", description=f"{floating_shares15}"),
            disnake.SelectOption(label=f"{ticker16}", description=f"{floating_shares16}"),
            disnake.SelectOption(label=f"{ticker17}", description=f"{floating_shares17}"),
            disnake.SelectOption(label=f"{ticker18}", description=f"{floating_shares18}"),
            disnake.SelectOption(label=f"{ticker19}", description=f"{floating_shares19}"),
            disnake.SelectOption(label=f"{ticker20}", description=f"{floating_shares20}"),
            disnake.SelectOption(label=f"{ticker21}", description=f"{floating_shares21}"),
            disnake.SelectOption(label=f"{ticker22}", description=f"{floating_shares22}"),
            disnake.SelectOption(label=f"{ticker23}", description=f"{floating_shares23}"),
            disnake.SelectOption(label=f"{ticker24}", description=f"{floating_shares24}"),]

        super().__init__(
            placeholder = "🇱 🇴 🇼  🇫 🇱 🇴 🇦 🇹",
            min_values = 1,
            max_values = 1,
            options = options
        )
    async def callback(self, interaction: disnake.MessageCommandInteraction):
        data = client.low_float()
        index0 = data[0]
        index1 = data[1]
        index2 = data[2]
        index3 = data[3]
        index4 = data[4]
        index5 = data[5]
        index6 = data[6]
        index7 = data[7]
        index8 = data[8]
        index9 = data[9]
        index10 = data[10]
        index11 = data[11]
        index12 = data[12]
        index13 = data[13]
        index14 = data[14]
        index15 = data[15]
        index16 = data[16]
        index17 = data[17]
        index18 = data[18]
        index19 = data[19]
        index20 = data[20]
        index21 = data[21]
        index22 = data[22]
        index23 = data[23]
        index24 = data[24]
        ticker0 = index0['ticker']
        ticker1 = index1['ticker']
        ticker2 = index2['ticker']
        ticker3 = index3['ticker']
        ticker4 = index4['ticker']
        ticker5 = index5['ticker']
        ticker6 = index6['ticker']
        ticker7 = index7['ticker']
        ticker8 = index8['ticker']
        ticker9 = index9['ticker']
        ticker10 = index10['ticker']
        ticker11 = index11['ticker']
        ticker12 = index12['ticker']
        ticker13 = index13['ticker']
        ticker14 = index14['ticker']
        ticker15 = index15['ticker']
        ticker16 = index16['ticker']
        ticker17 = index17['ticker']
        ticker18 = index18['ticker']
        ticker19 = index19['ticker']
        ticker20 = index20['ticker']
        ticker21 = index21['ticker']
        ticker22 = index22['ticker']
        ticker23 = index23['ticker']
        ticker24 = index24['ticker']
        await interaction.response.defer(with_message=True)
        if self.values[0] == self.values[0]:
            await interaction.send("```py\nFor dispaly only! Use as a quick reference!```")

