# Zuriel V. Alejandro
# All rigths reserved
# Whit love ♥️.
from discord.ext import commands
import discord
import requests

class Players(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command()
    async def players(self, ctx, ip: str = "play.legacymc.lat", port: int = 19132):
        """Muestra la lista de jugadores"""
        url = f'https://api.mcsrvstat.us/bedrock/2/{ip}:{port}'
        try:
            response = requests.get(url, timeout=10)
            data = response.json()
                    
            if data.get('online', False):
                players = data.get('players', {})
                online = players.get('online', 0)
                max_players = players.get('max', 0)
                
                embed = discord.Embed(title="Jugadores Online", color=discord.Color.blue())
                embed.add_field(name="Servidor", value=f"`{ip}:{port}`", inline=False)
                embed.add_field(name="Cantidad", value=f"{online}/{max_players} jugadores", inline=False)
                
                if players.get('list'):
                    players_list = players['list']
                    formatted_list = ""
                    
                    for i, player in enumerate(players_list, 1):
                        formatted_list += f"{i}. {player}\n"
                    
                    if len(formatted_list) > 1024: 
                        formatted_list = formatted_list[:1021] + "..."
                    
                    embed.add_field(name="Lista de Jugadores", value=formatted_list or "No hay jugadores conectados", inline=False)
                else:
                    if online > 0:
                        embed.add_field(name="Lista de Jugadores", value="Hay jugadores conectados pero no se pueden mostrar sus nombres", inline=False)
                    else:
                        embed.add_field(name="Lista de Jugadores", value="No hay jugadores conectados", inline=False)
                
                embed.set_footer(text="@MadVersal 2025")
            else:
                embed = discord.Embed(title="Estado del Servidor",
                                    description=f'El servidor `{ip}:{port}` está offline.',
                                    color=discord.Color.red())
                embed.set_footer(text="@MadVersal 2025")
            
            await ctx.send(embed=embed)
            
        except Exception as e:
            embed = discord.Embed(description=f'Error al consultar el servidor: No se pudo conectar',
                                color=discord.Color.purple())
            embed.set_footer(text="@MadVersal 2025")
            await ctx.send(embed=embed)

async def setup(bot):
    cog = Players(bot)
    await bot.add_cog(cog)
    print("[DEBUG] Cog Players cargado y comando !players registrado.")
# Zuriel V. Alejandro
# All rigths reserved
# Whit love ♥️.
