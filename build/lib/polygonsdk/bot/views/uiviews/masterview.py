import disnake
from disnake.ext import commands
from views.learnviews import MarketGlossaryView,Opt101View,OptionsView,OpportunitiesView,CandleDropdownView
from views.learnviews import WebullOrderDropdown,TechDropdown,TechDropdown2
from views.learnviews import TutorialsView,WebullTutView,LearningDropdown,OStratsView,OptStratsView,OptionStratsDropdown,AlertsView,HelperView,CoreView

class UltimateView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)


    @disnake.ui.button(label="Order Types", style=disnake.ButtonStyle.grey)
    async def order_types(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        self.add_item(WebullOrderDropdown())
        await inter.response.edit_message(view=self)
    
    @disnake.ui.button(label="Options", style=disnake.ButtonStyle.grey)
    async def options(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        await inter.response.edit_message(view=OptionsView())
   
    @disnake.ui.button(label="Tech Analysis", style=disnake.ButtonStyle.grey)
    async def tech_analysis(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        self.add_item(TechDropdown2())
        self.add_item(TechDropdown())
        await inter.response.edit_message(view=self)
    
    @disnake.ui.button(label="Discord Commands", style=disnake.ButtonStyle.grey)
    async def discord_commands(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):

        await inter.response.edit_message(view=HelperView())
    
    @disnake.ui.button(label="Discord Tutorials", style=disnake.ButtonStyle.grey)
    async def discordtut(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        self.add_item(TutorialsView().botcmds)
        self.add_item(TutorialsView().slashr)
        self.add_item(TutorialsView().disctuts)
        self.add_item(TutorialsView().home)
        self.add_item(LearningDropdown())
        await inter.response.edit_message(view=self)
    
    @disnake.ui.button(label="Options Strategies", style=disnake.ButtonStyle.grey)
    async def optstrats(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        self.add_item(OStratsView().winningcall)
        self.add_item(OptStratsView().putoptions)
        self.add_item(OptStratsView().ccs)
        self.add_item(OptStratsView().calloptions)
        self.add_item(OStratsView().losingcall)
        self.add_item(OStratsView().opts)
        self.add_item(OptionStratsDropdown())
        await inter.response.edit_message(view=self)

    
    @disnake.ui.button(label="Market Glossary", style=disnake.ButtonStyle.grey)
    async def marketglossary(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        await inter.response.edit_message(view=MarketGlossaryView())
    
    @disnake.ui.button(label="Options 101", style=disnake.ButtonStyle.grey)
    async def opt101(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        await inter.response.edit_message(view=Opt101View())
    
    @disnake.ui.button(label="Candle Patterns", style=disnake.ButtonStyle.grey)
    async def candles(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        await inter.response.edit_message(view=CandleDropdownView())
    
    @disnake.ui.button(label="Webull Tutorials", style=disnake.ButtonStyle.grey)
    async def webulltutorial(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        await inter.response.edit_message(view=WebullTutView())
    
    @disnake.ui.button(label="Discord Forums", style=disnake.ButtonStyle.grey)
    async def forums(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        await inter.response.edit_message(f"Coming soon.")
    
    @disnake.ui.button(label="Play Alerts", style=disnake.ButtonStyle.grey)
    async def playalerts(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        await inter.response.edit_message(view=AlertsView())
    @disnake.ui.button(label="Core Logic", style=disnake.ButtonStyle.grey)
    async def core(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        
        await inter.response.edit_message(view=CoreView())
   
    @disnake.ui.button(label="Opportunities", style=disnake.ButtonStyle.grey)
    async def order_types(self, button: disnake.ui.Button, inter: disnake.AppCmdInter):
        await inter.response.edit_message(view=OpportunitiesView())
    

    