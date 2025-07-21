from discord.ext import commands
import discord

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




    @commands.command()
    async def info(self, ctx):
        """Muestra información básica del bot"""
        embed = discord.Embed(title="Información", color=discord.Color.purple())
        embed.add_field(name="Sobre el Bot", value="Soy un bot de ejemplo hecho con discord.py", inline=False)
        embed.add_field(name="Servidor Minecraft", value="IP: `play.legacymc.lat:19132`", inline=False)
        embed.set_footer(text="@MadVersal 2025")
        await ctx.send(embed=embed)

async def setup(bot):
    cog = Info(bot)
    await bot.add_cog(cog)
    print("[DEBUG] Cog Info cargado y comando !info registrado.")
