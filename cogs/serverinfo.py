# Zuriel V. Alejandro
# All rigths reserved
# Whit love ♥️.
from discord.ext import commands
import discord

class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def serverinfo(self, ctx):
        guild = ctx.guild
        if guild:
            embed = discord.Embed(title="Información del Servidor", color=discord.Color.purple())
            embed.add_field(name="Nombre", value=guild.name, inline=False)
            embed.add_field(name="ID", value=guild.id, inline=False)
            embed.add_field(name="Miembros", value=guild.member_count, inline=False)
            embed.add_field(name="Dueño", value=guild.owner.mention if guild.owner else "Desconocido", inline=False)
            embed.set_thumbnail(url=guild.icon.url if guild.icon else discord.Embed.Empty)
            embed.set_footer(text="@MadVersal 2025")
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(description="Este comando solo puede usarse en un servidor.", color=discord.Color.purple())
            embed.set_footer(text="@MadVersal 2025")
            await ctx.send(embed=embed)

async def setup(bot):
    cog = ServerInfo(bot)
    await bot.add_cog(cog)
    print("[DEBUG] Cog ServerInfo cargado y comando !serverinfo registrado.")
