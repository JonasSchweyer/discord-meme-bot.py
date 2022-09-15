import os
import commands as com

from discord.ext import commands
import discord


class MyBot(discord.ext.commands.Bot):
    async def on_ready(self):
        await self.tree.sync()


intents = discord.Intents.default()
bot: discord.ext.commands.Bot = MyBot(command_prefix='.', intents=intents)


@bot.tree.command(description="Send memes (default 10, max 50)")
async def memes(interaction: discord.Interaction, amount: int = 10):
    await com.multiple_memes(interaction, amount)


bot.run(os.environ.get("DISCORD_TOKEN"))
