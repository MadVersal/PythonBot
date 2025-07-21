from discord.ext import commands
import discord

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def avatar(self, ctx, usuario: discord.User = None):
        usuario = usuario or ctx.author
        embed = discord.Embed(title=f"Avatar de {usuario.display_name}", color=discord.Color.purple())
        embed.set_image(url=usuario.avatar.url if usuario.avatar else usuario.default_avatar.url)
        embed.set_footer(text="@MadVersal 2025")
        await ctx.send(embed=embed)

async def setup(bot):
    cog = Avatar(bot)
    await bot.add_cog(cog)
    print("[DEBUG] Cog Avatar cargado y comando !avatar registrado.")
