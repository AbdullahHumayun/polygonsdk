import disnake
from disnake.ext import commands
from views.learnviews import MainView
from views.learnviews import SectorViewDropdown

class FUDSTOP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.slash_command()
    async def fudstop(self,inter):
        pass


    @fudstop.sub_command()
    async def application(self, inter:disnake.AppCmdInter):
        """⚙️The FUDSTOP Application designed to help you learn discord and markets."""
        await inter.response.defer(with_message=True, ephemeral=True)
        
        emb = disnake.Embed(title="Welcome to FUDSTOP", description="```py\nThis is the FUDSTOP Application. It's an interactive tool that contains a plethora of tools. See /fud command for short-cuts to specific areas of this application.```", color=disnake.Color.fuchsia())
        emb.add_field(name="Navigating the APP", value="```py\nTo navigate - simply click the buttons to change the Embed display, or choose from the dropdown to switch content categories. Each time a button is clicked - a new Embed will display with fresh content.```", inline=False)
        emb.add_field(name="To get started -->", value="```py\nSelect between 'Trade' - which contains several data series to use for easy market plays - \n\n **Learn** which contains a plethora of information to better equip you with the necessary information needed to trade.``` **or** ```py\nSetup Server Notifications with **Settings** Note: DON'T FORGET ABOUT PAPER TRADING.```", inline=False)
        emb.add_field(name="LIFETIME MEMBERSHIP", value="```py\nFinding success? Here for the long haul? Consider a lifetime membership. One payment of $750 nets you as a member for life - and with it you'll recieve your own personal portfolio and webhook integration as well as the lifetime member flair for the discord server.```", inline=True)
        emb.set_footer(text="``AQuery Credentials can be found at the bottom of the Menu Dropdown``")
        await inter.edit_original_response(embed = emb, view=MainView())


    @fudstop.sub_command()
    async def notifications(inter:disnake.AppCmdInter):
        """⚙️Creates a dropdown of the Discord Sectors to setup notifications."""
        await inter.response.defer(with_message=True,ephemeral=True)
        emb = disnake.Embed(title="Notifications Setup",description="```py\nThis is the setup-menu for notifications regarding sector feeds.``` ```py\n Each selection below will create an Embed listing each channel and different ways to navigate to them within Discord.``` ```py\n You can select the industries you wish to recieve notifications to - and set them via your user settings by clicking the bell at the top of each industry channel.``` ```py\n By enabling notifications, and ensuring that they are enabled in your user settings, you will recieve:``` ```py\n 'Dark Pool Notifications' for each ticker within each industry you choose. \n\n 'Golden Sweep Notifications' that will give you an idea of market sentiment revolving a particular security, or the industry as a whole. \n\n 'Quant Alerts' which are now 'realtime' bullish/bearish signals alerting for a potential move. \n\n 'Unusual Options Notifications' which are perhaps the most useful and can provide some insights as to where the industry is placing their current bets within each industry.``` The discord is massive. Make sure to take advantage of our unique set-up and truly streamline the information you want via notifications.", color=disnake.Colour.dark_gold())
        view = disnake.ui.View()
        view.add_item(SectorViewDropdown())
        await inter.edit_original_response(embed=emb, view=view)


    @notifications.error
    async def notificationserror(inter: disnake.AppCmdInter, error):
        if isinstance(error, commands.CheckAnyFailure):
            await inter.send(f"```py\n Sorry, something went wrong: error code: {error}```")    

def setup(bot):
    bot.add_cog(FUDSTOP(bot))
    print(f"> Extension {__name__} is ready\n")