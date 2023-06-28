"PAGINATED EMBED MENU FOR COMMANDS"


import disnake
from typing import List

class NumberSelect(disnake.ui.Select):
    def __init__(self, options: list[str]):
        super().__init__(
            custom_id="number_selector",
            placeholder="Select a command",
            min_values=1,
            max_values=1,
            options=options,
            row=1
        )

    async def callback(self, interaction: disnake.Interaction):
        selected_index = int(self.values[0])
        current_embed_target = self.view.embeds[self.view.current_page_index]

        if selected_index < len(current_embed_target.fields):
            selected_field = current_embed_target.fields[selected_index]
            await interaction.channel.send(selected_field.value)
        else:
            await interaction.channel.send("Invalid command selected.")
class PageSelect(disnake.ui.Select):
    def __init__(self, embeds):
        options = [
            disnake.SelectOption(
                label=embed.title,
                value=f"{i}"
            ) for i, embed in enumerate(embeds)
        ]

        super().__init__(
            custom_id="page_selector1",
            placeholder="Select A Category",
            min_values=1,
            max_values=1,
            options=options,
            row=0
        )
        
        self.embeds = embeds

    async def callback(self, interaction: disnake.Interaction):
        selected_value = int(self.values[0])
        embed_to_show = self.embeds[selected_value]
        
        await interaction.response.edit_message(embed=embed_to_show)

class SkewPageSelect(disnake.ui.Select):
    def __init__(self, embeds, tickers):
        self.embeds=embeds
        options = [
            disnake.SelectOption(
                label=self.shorten_label(ticker, 25),  # Use the ticker directly
                value=str(i),
            )
            for i, (embed, ticker) in enumerate(zip(embeds, tickers))
        ]

        # Debugging code
        for option in options:
            print(option.label, len(option.label))  # This should print each label and its length

        super().__init__(
            placeholder="Select A Stock ->",
            min_values=1,
            max_values=1,
            custom_id="page_selector1",
            options=options,
            row=0
        )

    def shorten_label(self, label, length):
        return label[:length] if len(label) > length else label

    async def callback(self, interaction: disnake.Interaction):
        selected_value = int(self.values[0])
        embed_to_show = self.view.embeds[selected_value]
        await interaction.response.edit_message(embed=embed_to_show)

class AlertMenus(disnake.ui.View):
    def __init__(
        self, embeds: List[disnake.Embed]
    ):
        super().__init__(timeout=None)
        self.embeds = embeds
        # Sets the embed list variable.

        #self.options2 = options2

        # Current embed number.
        self.embed_count = 0

        # Disables previous page button by default.
        self.prev_page.disabled = True


        # Sets the footer of the embeds with their respective page numbers.
        self.count = 0

        for i, embed in enumerate(self.embeds):
            embed.set_footer(
                text=f"Page {i + 1} of {len(self.embeds)}",
            )


    @disnake.ui.button(
        emoji="<a:_:1042677512284680321>",
        style=disnake.ButtonStyle.red,
        custom_id=f"persistent_view:prevqwfpage_{str(disnake.Member)}aq2wfwa",
        row=4,
        label=f"🇵 🇷 🇪 🇻"

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
        emoji="<a:_:1042677591196319765>",
        style=disnake.ButtonStyle.red,
        custom_id=f"persistent_view:nextpage_{str(disnake.Member)}awfawwa",
        label=f"🇳 🇪 🇽 🇹",
        row=4
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


class ImageMenus(disnake.ui.View):
    def __init__(
        self, embeds: List[disnake.Embed], image_files: List[str]
    ):
        super().__init__(timeout=None)
        self.embeds = embeds
        self.image_files = image_files
        self.embeds = embeds
        # Sets the embed list variable.

        #self.options2 = options2

        # Current embed number.
        self.embed_count = 0

        # Disables previous page button by default.
        self.prev_page.disabled = False


        # Sets the footer of the embeds with their respective page numbers.
        self.count = 0

        for i, embed in enumerate(self.embeds):
            embed.set_footer(
                text=f"Page {i + 1} of {len(self.embeds)}",
            )


    @disnake.ui.button(
        emoji="<a:_:1042677512284680321>",
        style=disnake.ButtonStyle.red,
        custom_id=f"persistent_view:prevqwfpage_{str(disnake.Member)}aq2wfwa",
        row=4,
        label=f"🇵 🇷 🇪 🇻"

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

        

class SkewAlertMenus(disnake.ui.View):
    def __init__(
        self, embeds: List[disnake.Embed]
    ):
        super().__init__(timeout=None)
        self.embeds = embeds
        # Sets the embed list variable.

        #self.options2 = options2

        # Current embed number.
        self.embed_count = 0

        # Disables previous page button by default.
        self.prev_page.disabled = True


        # Sets the footer of the embeds with their respective page numbers.
        self.count = 0

      #  for i, embed in enumerate(zip(self.embeds,)):
        #    embed.set_footer(
        #        text=f"Page {i + 1} of {len(self.embeds)}",
           # )


    @disnake.ui.button(
        emoji="<a:_:1042677512284680321>",
        style=disnake.ButtonStyle.red,
        custom_id=f"persistent_view:prevqwfpage_{str(disnake.Member)}aq2wfwa",
        row=4,
        label=f"🇵 🇷 🇪 🇻"

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
        emoji="<a:_:1042677591196319765>",
        style=disnake.ButtonStyle.red,
        custom_id=f"persistent_view:nextpage_{str(disnake.Member)}awfawwa",
        label=f"🇳 🇪 🇽 🇹",
        row=4
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