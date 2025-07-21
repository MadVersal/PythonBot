# Zuriel V. Alejandro
# All rigths reserved
# Whit love ♥️.
from discord.ext import commands
import discord
import random

class Dado(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dado(self, ctx, caras: int = 6):
        if caras < 2 or caras > 1000:
            embed = discord.Embed(description="El número de caras debe estar entre 2 y 1000.", color=discord.Color.purple())
            embed.set_footer(text="Bot de MadVersal")
            await ctx.send(embed=embed)
            return
        resultado = random.randint(1, caras)
        embed = discord.Embed(title="Lanzamiento de Dado", description=f"Has lanzado un dado de {caras} caras y salió: **{resultado}**", color=discord.Color.purple())
        embed.set_footer(text="Bot de MadVersal")
        await ctx.send(embed=embed)

async def setup(bot):
    cog = Dado(bot)
    await bot.add_cog(cog)
    print("[DEBUG] Cog Dado cargado y comando !dado registrado.")
