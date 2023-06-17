"""MENUS"""
from typing import List
import disnake
from disnake.ext import commands
intents = disnake.Intents.all()
bot = commands.Bot( command_prefix="!", intents=intents)


class Menu(disnake.ui.View):
    """MENU"""
    def __init__(self, embeds: List[disnake.Embed]):
        super().__init__(timeout=None)

  # Sets the embed list variable.
        self.embeds = embeds
        # Current embed number.
        self.embed_count = 0

    # Disables previous page button by default.

    # Sets the footer of the embeds with their respective page numbers.
        self.count = 0
        self.set_link_button()

        for i, embed in enumerate(self.embeds):
            embed.set_footer(
            text=f"Page {i + 1} of {len(self.embeds)}",
        )

    def set_link_button(self) -> None:
        """LINK BUTTON"""
        if not hasattr(self, "link_button"):
            self.link_button: disnake.ui.Button = disnake.ui.Button(
            style=disnake.ButtonStyle.url,
            url="https://www.fudstop.io",
            label="FUDSTOP",
            row=0,
        )
        self.add_item(self.link_button)
        self.link_button.label = "Site"
        self.count += 1


    @disnake.ui.button(
    label="Previous page",
    emoji="<a:leftarrow:929686892339937371>",
    style=disnake.ButtonStyle.red,
    custom_id=f"persistent_view:prevpage_{str(disnake.Member)}",
        )

    async def prev_page(  # pylint: disable=W0613
    self,
    button: disnake.ui.Button,
    interaction: disnake.MessageInteraction,
        ):
        """PREVIOUS PAGE"""
    # Increments the embed count.
        self.embed_count += -1

    # Gets the embed object.
        embed = self.embeds[self.embed_count]

        await interaction.response.edit_message(embed=embed, view=self)

    @disnake.ui.button(
    label="Next page",
    emoji="<a:rightarrow:929686891891155006>",
    style=disnake.ButtonStyle.red,
    custom_id=f"persistent_view:nextpage_{str(disnake.Member)}",
        )
    async def next_page(  # pylint: disable=W0613
    self,
    button: disnake.ui.Button,
    interaction: disnake.MessageInteraction,
        ):
        """next page"""
    # Increments the embed count.
        self.embed_count += 1

        # Gets the embed object.
        embed = self.embeds[self.embed_count]

    # Enables the previous page button and disables the next page button if we're on the last embed.
        self.prev_page.disabled = False
        if self.embed_count == len(self.embeds) - 1:
            self.next_page.disabled = False
            await interaction.response.edit_message(embed=embed, view=self)
