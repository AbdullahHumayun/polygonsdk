


snippets = {
    "Slash Command with Embed": """
    @bot.slash_command()
    async def slash_with_embed(inter: disnake.AppCmdInter):
        \"\"\"
        Slash Command with Embed Example.
        \"\"\"
        embed = disnake.Embed(
            title="Your Embed Title!",
            description="This is your embed description.",
            url="https://www.google.com",
            color=disnake.Colour.dark_magenta()
        )
    
        # Add fields, images, author, footer, etc. to the embed
    
        await inter.send(embed=embed)
    """,
    "Context Command with Embed": """
    @bot.command()
    async def context_command_with_embed(ctx: commands.Context):
        \"\"\"
        Context Command with an Embed Example.
        \"\"\"
        embed = disnake.Embed(
            title="Your Embed Title!",
            description="This is your embed description.",
            url="https://www.google.com",
            color=disnake.Colour.dark_magenta()
        )
    
        embed.add_field(name="Non In-line Field", value="This is a NON In-line Field.", inline=False)
        embed.add_field(name="In-Line Field", value="This is an in-line Field.")
        embed.add_field(name="In-Line Field 2", value="This is an in-line Field.")
        embed.add_field(name="In-Line Field 3", value="This is an in-line Field.")
    
        embed.set_image("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/220px-Image_created_with_a_mobile_phone.png")
        embed.set_thumbnail("https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/220px-Image_created_with_a_mobile_phone.png")
        embed.set_author(name="The Author!")
        embed.set_footer(text="This is a footer!", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/220px-Image_created_with_a_mobile_phone.png")
    
        await ctx.send(embed=embed)
    """,
    "GPT-4 Command": """
    @bot.command()
    async def gpt4(ctx: commands.Context, prompt: str):
        #... Your GPT-4 Command Code here ...
    """,
    
    "Discord Navigation Commands": 
    """
    

    class Navigate(commands.Cog):
        def __init__(self, bot):
            self.bot = bot

        @commands.slash_command()
        async def navigate(inter: disnake.CommandInteraction, channel: disnake.TextChannel):
            \"""
            >>> Command category for discord-navigation commands.
            \"""
            pass


        @navigate.sub_command()
        async def channels(self, inter: disnake.CommandInteraction, channel: disnake.TextChannel):
            \"""
            Returns the channel to navigate to.
            \"""

            await inter.response.defer(with_message=True, ephemeral=True)
            embed = disnake.Embed(title="You just navigated!", color=disnake.Colour.dark_magenta())
            embed.set_footer(text="Data provided by Financial Modeling Prep. Implemented by FUDSTOP Trading.", icon_url="https://uploads-ssl.webflow.com/62661f74776abb77ef7621a8/6272ac0a541297826e1a5209_963244979063517184.gif")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/1009552305869303828/1009555505699639366/ezgif-2-f4a5623248.gif")
            await inter.edit_original_message(channel.mention)
        
        @navigate.sub_command()
        async def threads(self, inter: disnake.CommandInteraction, channel: disnake.Thread):
            \"""
            Returns the thread to navigate to.
            \"""
            await inter.response.defer(with_message=True, ephemeral=True)
            embed = disnake.Embed(title="You just navigated!",color=disnake.Colour.dark_magenta())
            embed.set_footer(text="Data provided by Financial Modeling Prep. Implemented by FUDSTOP Trading.", icon_url="https://uploads-ssl.webflow.com/62661f74776abb77ef7621a8/6272ac0a541297826e1a5209_963244979063517184.gif")
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/1009552305869303828/1009555505699639366/ezgif-2-f4a5623248.gif")
            await inter.edit_original_message(channel.mention)

        @navigate.sub_command()
        async def forums(self, inter:disnake.CommandInteraction, channel: disnake.ForumChannel):
            \"""
            Returns the forum to navigate to.
            \"""

            await inter.send(channel.mention)

    def setup(bot):
        bot.add_cog(Navigate(bot: commands.Bot))
        print(f"> Extension {__name__} is ready\n")"""   
        
        """,





@bot.command()
async def gpt4(ctx: commands.Context, prompt: str):
    \"\"\"
    Talk with CHATGPT. Call the command once and then reply as normal.
    \"\"\"
    openai.api_key = openaikey  # get from chat.openai.com
    conversation_history = {}
    conversation_id = str(ctx.author.id)
    conversation_prompt = ctx.message.content

    # Retrieve the conversation history from the dictionary
    history = conversation_history.get(conversation_id, [])

    while True:
        # Add the new prompt to the conversation history
        history.append({"role": "user", "content": conversation_prompt})

        # Create the messages list including system message and conversation history
        messages = [
            {"role": "system", "content": "You're gonna build the most amazing program ever."},
            {"role": "user", "content": "Yes, I'm ready!"},
            {"role": "system", "content": "Great! So let's get started. What program do you want to build, and what language?"},
            {"role": "user", "content": "I want to build a program that generates beautiful stock charts for websites."},
            {"role": "system", "content": "Excellent! I'm here to help you explore your coding skills."}
        ]
        messages.extend(history)

        # Generate a response based on the full conversation history
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        message_content = completion.choices[0].message.content

        # Store the updated conversation history in the dictionary
        conversation_history[conversation_id] = history

        embed = disnake.Embed(title=f"{e.redline} GPT4 {e.redline}", description=f"{message_content}")
        embed.add_field(name=f"YOUR PROMPT:", value=f"You asked: {prompt}")

        # Send the response to the user
        await ctx.send(embed=embed)

        # Check if the user wants to stop the conversation
        if conversation_prompt.lower() == "stop":
            await ctx.send("Conversation ended.")
            break

        # Wait for the user's next message
        def check(m: disnake.Message):
            return m.author.id == ctx.author.id and m.channel.id == ctx.channel.id

        try:
            user_message = await bot.wait_for("message", check=check, timeout=60)
        except asyncio.TimeoutError:
            await ctx.send("Conversation timed out. Please start a new conversation.")
            break

        conversation_prompt = user_message.content"""
    }
