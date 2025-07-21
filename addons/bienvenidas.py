# Zuriel V. Alejandro
# All rigths reserved
# Whit love ♥️.
from discord.ext import commands
import discord

class Bienvenidas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.welcome_channels = {}

    @commands.group(invoke_without_command=True)
    @commands.has_permissions(administrator=True)
    async def bienvenida(self, ctx):
        """Gestiona el sistema de bienvenidas"""
        embed = discord.Embed(
            title="Sistema de Bienvenidas",
            description="**Comandos disponibles:**\n"
                       "`!bienvenida canal #canal` - Establece el canal de bienvenidas\n"
                       "`!bienvenida test` - Prueba el mensaje de bienvenida\n"
                       "`!bienvenida disable` - Desactiva las bienvenidas",
            color=discord.Color.green()
            embed.set_footer(text="@MadVersal 2025")
        )
        await ctx.send(embed=embed)

    @bienvenida.command(name="canal")
    @commands.has_permissions(administrator=True)
    async def welcome_channel(self, ctx, channel: discord.TextChannel):
        """Establece el canal de bienvenidas"""
        self.welcome_channels[ctx.guild.id] = channel.id
        embed = discord.Embed(
            description=f"Canal de bienvenidas establecido en {channel.mention}",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)

    @bienvenida.command(name="test")
    @commands.has_permissions(administrator=True)
    async def welcome_test(self, ctx):
        """Prueba el mensaje de bienvenida"""
        await self.send_welcome_message(ctx.author, ctx.guild)

    @bienvenida.command(name="disable")
    @commands.has_permissions(administrator=True)
    async def welcome_disable(self, ctx):
        """Desactiva las bienvenidas"""
        if ctx.guild.id in self.welcome_channels:
            del self.welcome_channels[ctx.guild.id]
            embed = discord.Embed(
                description="Sistema de bienvenidas desactivado",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send("El sistema de bienvenidas ya está desactivado.")

    async def send_welcome_message(self, member, guild):
        """Envía el mensaje de bienvenida"""
        if guild.id not in self.welcome_channels:
            return
            
        channel = self.bot.get_channel(self.welcome_channels[guild.id])
        if not channel:
            return

        embed = discord.Embed(
            title="¡Bienvenido!",
            description=f"¡Hola {member.mention}, bienvenido a **{guild.name}**!",
            color=discord.Color.green()
        )
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.add_field(name="Miembro #", value=str(len(guild.members)), inline=True)
        embed.add_field(name="Cuenta creada", value=member.created_at.strftime("%d/%m/%Y"), inline=True)
        embed.set_footer(text=f"ID: {member.id}")

        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        """Evento cuando un miembro se une al servidor"""
        await self.send_welcome_message(member, member.guild)

async def setup(bot):
    cog = Bienvenidas(bot) # Borren pmmp ya xdxdxd
    await bot.add_cog(cog)
    print("[DEBUG] Sistema de Bienvenidas cargado.")
# Zuriel V. Alejandro
# All rigths reserved
# Whit love ♥️.
