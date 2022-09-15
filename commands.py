import discord
from util import meme_getter


async def multiple_memes(interaction: discord.Interaction, amount: int):
    if amount > 50:
        amount = 50
    elif amount < 1:
        amount = 10

    urls = meme_getter.meme_urls(amount)

    await interaction.response.send_message(urls.pop(0))

    for url in urls:
        await interaction.channel.send(url)
