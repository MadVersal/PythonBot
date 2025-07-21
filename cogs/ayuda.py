from discord.ext import commands
import discord

class Ayuda(commands.Cog):
    def __init__(self, bot):
        self.bot = bot




    @commands.command()
    async def ayuda(self, ctx):
        """Muestra los comandos básicos disponibles xd"""
        embed = discord.Embed(title="Ayuda", description='Comandos disponibles: !hola, !info, !ayuda, !status, !players, !ip, !avatar, !dado, !userinfo, !tickets, !serverinfo, !botinfo, !uptime, !bienvenida, !despedida', color=discord.Color.purple())
        embed.set_footer(text="@MadVersal 2025")
        await ctx.send(embed=embed)

async def setup(bot):
    cog = Ayuda(bot)
    await bot.add_cog(cog)
    print("[DEBUG] Cog Help cargado y comando !help registrado.")
