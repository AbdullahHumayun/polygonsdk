from discord_webhook import DiscordEmbed, AsyncDiscordWebhook


async def make_news_embed(webhook_url, image_url, title, description, name, icon_url, article_url, tickers, home_url, keywords, author):
    webhook = AsyncDiscordWebhook(webhook_url, content="YOUR CONTENT")
    embed = DiscordEmbed(title=title, description=f"```py\n{description}```", url=article_url)
    embed.add_embed_field(name="Relevant tickers:", value=f"```py\n{tickers}```", inline=False)
    embed.add_embed_field(name="News Keywords:", value=f"```py\n{keywords}```", inline=True)
    embed.add_embed_field(name="Publisher:", value=f"```py\n{name}```")
    embed.add_embed_field(name=f"Author:", value=f"> **{author}**")
    embed.set_image(image_url)
    embed.set_footer(text="Data provided by Polygon.io", icon_url=icon_url)
    embed.set_author(name=author)
    embed.set_timestamp()
    webhook.add_embed(embed)
    await webhook.execute()