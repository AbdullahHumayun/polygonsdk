import disnake
from disnake.ext import commands


class Navigate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def navigate(inter: disnake.CommandInteraction, channel: disnake.TextChannel):
        """>>> Command category for discord-navigation commands."""
        pass


    @navigate.sub_command()
    async def channels(self, inter: disnake.CommandInteraction, channel: disnake.TextChannel):
        """Returns the channel to navigate to."""

        await inter.response.defer(with_message=True, ephemeral=True)
        embed = disnake.Embed(title="You just navigated!", color=disnake.Colour.dark_magenta())
        embed.set_footer(text="Data provided by Financial Modeling Prep. Implemented by FUDSTOP Trading.", icon_url="https://uploads-ssl.webflow.com/62661f74776abb77ef7621a8/6272ac0a541297826e1a5209_963244979063517184.gif")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1009552305869303828/1009555505699639366/ezgif-2-f4a5623248.gif")
        await inter.edit_original_message(channel.mention)
    
    @navigate.sub_command()
    async def threads(self, inter: disnake.CommandInteraction, channel: disnake.Thread,):
        """Returns the thread to navigate to."""
        await inter.response.defer(with_message=True, ephemeral=True)
        embed = disnake.Embed(title="You just navigated!",color=disnake.Colour.dark_magenta())
        embed.set_footer(text="Data provided by Financial Modeling Prep. Implemented by FUDSTOP Trading.", icon_url="https://uploads-ssl.webflow.com/62661f74776abb77ef7621a8/6272ac0a541297826e1a5209_963244979063517184.gif")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/1009552305869303828/1009555505699639366/ezgif-2-f4a5623248.gif")
        await inter.edit_original_message(channel.mention)

    @navigate.sub_command()
    async def forums(self, inter:disnake.CommandInteraction, channel: disnake.ForumChannel):
        """Returns the forum to navigate to."""

        await inter.send(channel.mention)

def setup(bot: commands.Bot):
    bot.add_cog(Navigate(bot))
    print(f"> Extension {__name__} is ready\n")