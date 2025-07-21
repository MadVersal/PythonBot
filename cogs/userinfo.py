# Zuriel V. Alejandro
# All rigths reserved
# Whit love ♥️.
from discord.ext import commands
import discord
import datetime

class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def userinfo(self, ctx, usuario: discord.Member = None):
        usuario = usuario or ctx.author
        embed = discord.Embed(title=f"👤 Información de {usuario.display_name}", color=discord.Color.purple())
        embed.set_thumbnail(url=usuario.avatar.url if usuario.avatar else usuario.default_avatar.url)
        embed.add_field(name="ID", value=usuario.id, inline=False)
        embed.add_field(name="Nombre de usuario", value=str(usuario), inline=False)
        embed.add_field(name="Rol más alto", value=usuario.top_role.mention if hasattr(usuario, 'top_role') else 'N/A', inline=False)
        embed.add_field(name="Cuenta creada", value=usuario.created_at.strftime('%d/%m/%Y %H:%M:%S'), inline=False)
        if hasattr(usuario, 'joined_at') and usuario.joined_at:
            embed.add_field(name="Entró al servidor", value=usuario.joined_at.strftime('%d/%m/%Y %H:%M:%S'), inline=False)
        embed.set_footer(text="@MadVersal 2025")
        await ctx.send(embed=embed)

async def setup(bot):
    cog = UserInfo(bot)
    await bot.add_cog(cog)
    print("[DEBUG] Cog UserInfo cargado y comando !userinfo registrado.")
