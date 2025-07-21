# Zuriel V. Alejandro
# All rigths reserved
# Whit love ♥️.
from discord.ext import commands
import discord


class Ip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ip(self, ctx):
        """Responde con la IP del servidor"""
        embed = discord.Embed(title="Server IP", color=discord.Color.purple())
        embed.add_field(name="IP", value='play.legacymc.lat', inline=False)
        embed.add_field(name="Port", value='19132', inline=False)
        embed.set_footer(text="@MadVersal 2025")
        await ctx.send(embed=embed)

async def setup(bot):
    cog = Ip(bot)
    await bot.add_cog(cog)
    print("[DEBUG] Cog Ip cargado y comando !ip registrado.")
