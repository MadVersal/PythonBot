from discord.ext import commands
import discord

class BotInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def botinfo(self, ctx):
        embed = discord.Embed(title="Información del Bot", color=discord.Color.purple())
        embed.add_field(name="Nombre", value=self.bot.user.name, inline=False)
        embed.add_field(name="ID", value=self.bot.user.id, inline=False)
        embed.add_field(name="Creador", value="MadVersal", inline=False)     
        embed.add_field(name="Versión", value="1.0.0", inline=False)
        embed.add_field(name="Discord", value="oldversal / 1028453310686048318", inline=False)
        embed.set_thumbnail(url=self.bot.user.avatar.url if self.bot.user.avatar else discord.Embed.Empty)
        embed.set_footer(text="@MadVersal 2025")
        await ctx.send(embed=embed)

async def setup(bot):
    cog = BotInfo(bot)
    await bot.add_cog(cog)
    print("[DEBUG] Cog BotInfo cargado y comando !botinfo registrado.")
