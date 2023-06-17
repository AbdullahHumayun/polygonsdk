import disnake
from webull import webull
wbb = webull()
    
class PressRelease(disnake.ui.Select):
    def __init__(self, ticker: str):
        self.ticker = ticker
        
        prelease = wbb.get_press_releases(stock=f"{ticker}")
        try:
            prannouncements = prelease['announcements']
            self.filingtitle1 = prannouncements[0]['title']
        except KeyError:
            prelease = "None Found"
            prannouncements = "None Found"
            filingtitle1 = "None Found"
        try:
            self.filingpubdate1 = prannouncements[0]['publishDate']
            self.filinghtmlurl1 = prannouncements[0]['htmlUrl']
            self.filingtypename1 = prannouncements[0]['typeName']
            self.filingtitle2 = prannouncements[1]['title']
            self.filingpubdate2 = prannouncements[1]['publishDate']
            self.filinghtmlurl2 = prannouncements[1]['htmlUrl']
            self.filingtypename2 = prannouncements[1]['typeName']
            self.filingtitle3 = prannouncements[2]['title']
            self.filingpubdate3 = prannouncements[2]['publishDate']
            self.filinghtmlurl3 = prannouncements[2]['htmlUrl']
            self.filingtypename3 = prannouncements[2]['typeName']
            self.filingtitle4 = prannouncements[3]['title']
            self.filingpubdate4 = prannouncements[3]['publishDate']
            self.filinghtmlurl4 = prannouncements[3]['htmlUrl']
            self.filingtypename4 = prannouncements[3]['typeName']
            self.filingtitle5 = prannouncements[4]['title']
            self.filingpubdate5 = prannouncements[4]['publishDate']
            self.filinghtmlurl5 = prannouncements[4]['htmlUrl']
            self.filingtypename5 = prannouncements[4]['typeName']
            self.filingtitle6 = prannouncements[5]['title']
            self.filingpubdate6 = prannouncements[5]['publishDate']
            self.filinghtmlurl6 = prannouncements[5]['htmlUrl']
            self.filingtypename6 = prannouncements[5]['typeName']
            self.filingtitle7 = prannouncements[6]['title']
            self.filingpubdate7 = prannouncements[6]['publishDate']
            self.filinghtmlurl7 = prannouncements[6]['htmlUrl']
            self.filingtypename7 = prannouncements[6]['typeName']
            self.filingtitle8 = prannouncements[7]['title']
            self.filingpubdate8 = prannouncements[7]['publishDate']
            self.filinghtmlurl8 = prannouncements[7]['htmlUrl']
            self.filingtypename8 = prannouncements[7]['typeName']
            self.filingtitle9 = prannouncements[8]['title']
            self.filingpubdate9 = prannouncements[8]['publishDate']
            self.filinghtmlurl9 = prannouncements[8]['htmlUrl']
            self.filingtypename9 = prannouncements[8]['typeName']
            self.filingtitle10 = prannouncements[9]['title']
            self.filingpubdate10 = prannouncements[9]['publishDate']
            self.filinghtmlurl10 = prannouncements[9]['htmlUrl']
            self.filingtypename10 = prannouncements[9]['typeName']
        except KeyError:
           return ("Doesn't work on ETFs.")


        super().__init__(
            placeholder ="🇫 ℹ️ 🇱 ℹ️ 🇳 🇬 🇸",
            min_values=1,
            max_values=2,
            options=[
            disnake.SelectOption(label=f"{self.filingtitle1}",values="1",description=f"{self.filingpubdate1} | {self.filingtypename1}"),
            disnake.SelectOption(label=f"{self.filingtitle2}",values="2",description=f"{self.filingpubdate2} | {self.filingtypename2}"),
            disnake.SelectOption(label=f"{self.filingtitle3}",description=f"{self.filingpubdate3} | {self.filingtypename3}"),
            disnake.SelectOption(label=f"{self.filingtitle4}",description=f"{self.filingpubdate4} | {self.filingtypename4}"),
            disnake.SelectOption(label=f"{self.filingtitle5}",description=f"{self.filingpubdate5} | {self.filingtypename5}"),
            disnake.SelectOption(label=f"{self.filingtitle6}",description=f"{self.filingpubdate6} | {self.filingtypename6}"),
            disnake.SelectOption(label=f"{self.filingtitle7}",description=f"{self.filingpubdate7} | {self.filingtypename7}"),
            disnake.SelectOption(label=f"{self.filingtitle8}",description=f"{self.filingpubdate8} | {self.filingtypename8}"),
            disnake.SelectOption(label=f"{self.filingtitle9}",description=f"{self.filingpubdate9} | {self.filingtypename9}"),
            disnake.SelectOption(label=f"{self.filingtitle10}",description=f"{self.filingpubdate10} | {self.filingtypename10}"),]
        )


    async def callback(self, interaction:disnake.MessageCommandInteraction):
        
        if self.values[0] == "1":
            await interaction.send(f"```py\nHere is a link to the filing you chose:``` {PressRelease.filinghtmlurl1}")
        elif self.values[0] == f"{PressRelease.filinghtmlurl2}":
            await interaction.send(f"```py\nHere is a link to the filing you chose:``` {PressRelease.filinghtmlurl2}")
        elif self.values[0] == f"{PressRelease.filinghtmlurl3}":
            await interaction.send(f"```py\nHere is a link to the filing you chose:``` {PressRelease.filinghtmlurl3}")
        elif self.values[0] == f"{PressRelease.filinghtmlurl4}":
            await interaction.send(f"```py\nHere is a link to the filing you chose:``` {PressRelease.filinghtmlurl4}")
        elif self.values[0] == f"{PressRelease.filinghtmlurl5}":
            await interaction.send(f"```py\nHere is a link to the filing you chose:``` {PressRelease.filinghtmlurl5}")
        elif self.values[0] == f"{PressRelease.filinghtmlurl6}":
            await interaction.send(f"```py\nHere is a link to the filing you chose:``` {PressRelease.filinghtmlurl6}")
        elif self.values[0] == f"{PressRelease.filinghtmlurl7}":
            await interaction.send(f"```py\nHere is a link to the filing you chose:``` {PressRelease.filinghtmlurl7}")
        elif self.values[0] == f"{PressRelease.filinghtmlurl8}":
            await interaction.send(f"```py\nHere is a link to the filing you chose:``` {PressRelease.filinghtmlurl8}")
        elif self.values[0] == f"{PressRelease.filinghtmlurl9}":
            await interaction.send(f"```py\nHere is a link to the filing you chose:``` {PressRelease.filinghtmlurl9}")
        elif self.values[0] == f"{PressRelease.filinghtmlurl10}":
            await interaction.send(f"```py\nHere is a link to the filing you chose:``` {PressRelease.filinghtmlurl10}")
