# Zuriel V. Alejandro
# All rigths reserved
# Whit love ♥️.
from discord.ext import commands
import discord
import datetime

class Uptime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.start_time = datetime.datetime.utcnow()

    @commands.command()
    async def uptime(self, ctx):
        now = datetime.datetime.utcnow()
        delta = now - self.start_time
        hours, remainder = divmod(int(delta.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        embed = discord.Embed(title="Uptime", description=f"El bot ha estado en línea por {hours}h {minutes}m {seconds}s", color=discord.Color.purple())
        embed.set_footer(text="@MadVersal 2025")
        await ctx.send(embed=embed)

async def setup(bot):
    cog = Uptime(bot)
    await bot.add_cog(cog)
    print("[DEBUG] Cog Uptime cargado y comando !uptime registrado.")
