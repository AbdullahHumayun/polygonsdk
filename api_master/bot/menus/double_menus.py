import disnake
import random

from typing import List



class DoubleMenus(disnake.ui.View):
    def __init__(
        self, embeds: List[disnake.Embed], options: List[disnake.SelectOption], options2: List[disnake.SelectOption]
    ):
        super().__init__(timeout=None)

        # Sets the embed list variable.
        self.embeds = embeds
        self.options = options
        self.options2 = options2
        
        # Current embed number.
        self.embed_count = 0

        # Disables previous page button by default.
        self.prev_page.disabled = True

        # Sets the footer of the embeds with their respective page numbers.
        self.count = 0
        self.set_link_button()

        for opt in options:
            self.selector.append_option(opt)  # pylint: disable=E1101
        for i, embed in enumerate(self.embeds):
            embed.set_footer(
                text=f"Page {i + 1} of {len(self.embeds)}",
                icon_url="https://static.wixstatic.com/media/3235bb_a6ebb092eaa0466792f4925f3af3d46c~mv2.gif",
            )


        for opt2 in options2:
            self.selector2.append_option(opt2)  # pylint: disable=E1101


    def set_link_button(self) -> None:
        if not hasattr(self, "link_button"):
            self.link_button: disnake.ui.Button = disnake.ui.Button(
                style=disnake.ButtonStyle.url,
                url="discord.gg/fudstop",
                label="Site",
            )
            self.add_item(self.link_button)
        self.link_button.label = "Site"
        self.count += 1

    @disnake.ui.select(
        placeholder="1️⃣  ➡️ 🪟  2️⃣  5️⃣",
        custom_id=f"select_{str(disnake.Member)}_",
 

    )
    async def selector(
        self,
        select: disnake.ui.Select,
        inter: disnake.MessageInteraction,
    ) -> None:
        self.set_link_button()
        s = ""
        str1 = s.join(select.values)
        ind = int(str1)
        self.embed_count = int(str1)
        
        self.next_page.disabled = False
        self.prev_page.disabled = False
        print(select.values)
        await inter.response.edit_message(embed=self.embeds[ind], view=self)

    @disnake.ui.select(
        placeholder="2️⃣  5️⃣ ➡️ 🪟 5️⃣  0️⃣",
        custom_id=f"select_{str(disnake.Member)}",

    )
    async def selector2(
        self,
        select: disnake.ui.Select,
        inter: disnake.MessageInteraction,
    ) -> None:
        self.set_link_button()
        s = ""
        str1 = s.join(select.values)
        ind = int(str1)
        self.embed_count = int(str1)
        self.next_page.disabled = False
        self.prev_page.disabled = False
        print(select.values)
        await inter.response.edit_message(embed=self.embeds[ind], view=self)

    @disnake.ui.button(
        label="⬅️",
        emoji="<a:_:963244979063517184>",
        style=disnake.ButtonStyle.grey,
        custom_id=f"persistent_view:prevpage_{str(disnake.Member)}_",
    )
    async def prev_page(  # pylint: disable=W0613
        self,
        button: disnake.ui.Button,
        interaction: disnake.MessageInteraction,
    ):
        # Decrements the embed count.
        self.embed_count -= 1

        # Gets the embed object.
        embed = self.embeds[self.embed_count]

        # Enables the next page button and disables the previous page button if we're on the first embed.
        self.next_page.disabled = False

        await interaction.response.edit_message(embed=embed, view=self)



    @disnake.ui.button(
        label="➡️",
        emoji="<a:_:963244979063517184>",
        style=disnake.ButtonStyle.grey,
        custom_id=f"persistent_view:nextpage_{str(disnake.Member)}_",
    )
    async def next_page(  # pylint: disable=W0613
        self,
        button: disnake.ui.Button,
        interaction: disnake.MessageInteraction,
    ):
        # Increments the embed count.
        self.embed_count += 1

        # Gets the embed object.
        embed = self.embeds[self.embed_count]

        # Enables the previous page button and disables the next page button if we're on the last embed.
        self.prev_page.disabled = False

        await interaction.response.edit_message(embed=embed, view=self)
