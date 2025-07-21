# Zuriel V. Alejandro
# All rigths reserved
# Whit love ♥️.
from discord.ext import commands
import discord

class Despedidas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.goodbye_channels = {} 

    @commands.group(invoke_without_command=True)
    @commands.has_permissions(administrator=True)
    async def despedida(self, ctx):
        """Gestiona el sistema de despedidas"""
        embed = discord.Embed(
            title="Sistema de Despedidas",
            description="**Comandos disponibles:**\n"
                       "`!despedida canal #canal` - Establece el canal de despedidas\n"
                       "`!despedida test` - Prueba el mensaje de despedida\n"
                       "`!despedida disable` - Desactiva las despedidas",
            color=discord.Color.orange()
        )
        await ctx.send(embed=embed)

    @despedida.command(name="canal")
    @commands.has_permissions(administrator=True)
    async def goodbye_channel(self, ctx, channel: discord.TextChannel):
        """Establece el canal de despedidas"""
        self.goodbye_channels[ctx.guild.id] = channel.id
        embed = discord.Embed(
            description=f"Canal de despedidas establecido en {channel.mention}",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

    @despedida.command(name="test")
    @commands.has_permissions(administrator=True)
    async def goodbye_test(self, ctx):
        """Prueba el mensaje de despedida"""
        await self.send_goodbye_message(ctx.author, ctx.guild)

    @despedida.command(name="disable")
    @commands.has_permissions(administrator=True)
    async def goodbye_disable(self, ctx):
        """Desactiva las despedidas"""
        if ctx.guild.id in self.goodbye_channels:
            del self.goodbye_channels[ctx.guild.id]
            embed = discord.Embed(
                description="Sistema de despedidas desactivado",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send("El sistema de despedidas ya está desactivado.")

    async def send_goodbye_message(self, member, guild):
        """Envía el mensaje de despedida"""
        if guild.id not in self.goodbye_channels:
            return
            
        channel = self.bot.get_channel(self.goodbye_channels[guild.id])
        if not channel:
            return

        embed = discord.Embed(
            title="¡Hasta luego!",
            description=f"**{member.name}** ha abandonado el servidor.",
            color=discord.Color.orange()
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.add_field(name="Miembros restantes", value=str(len(guild.members)), inline=True)
        embed.set_footer(text=f"ID: {member.id}")

        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        """Evento cuando un miembro abandona el servidor"""
        await self.send_goodbye_message(member, member.guild)

async def setup(bot):
    cog = Despedidas(bot)
    await bot.add_cog(cog)
    print("[DEBUG] Sistema de Despedidas cargado.")
# Zuriel V. Alejandro
# All rigths reserved
# Whit love ♥️.
