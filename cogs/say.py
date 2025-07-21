# Zuriel V. Alejandro
# All rigths reserved
# Whit love ♥️.
import discord
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="say", help="Repite el mensaje que escribas.")
    async def say(self, ctx: commands.Context, *, message: str = None):
        if message is None:
            await ctx.send("Debes escribir un mensaje para que lo repita")
        else:
            await ctx.send(message)

async def setup(bot: commands.Bot):
    await bot.add_cog(Say(bot))
# Zuriel V. Alejandro
# All rigths reserved
# Whit love ♥️.
