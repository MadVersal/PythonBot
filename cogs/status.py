# Zuriel V. Alejandro
# All rigths reserved
# Whit love ♥️.
from discord.ext import commands
import discord
import requests

class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot 

    @commands.command()
    async def status(self, ctx, ip: str = "play.legacymc.lat", port: int = 19132):
        """Estado del servidor"""
        url = f'https://api.mcsrvstat.us/bedrock/2/{ip}:{port}'
        try:
            response = requests.get(url, timeout=10)
            data = response.json()
                    
            if data.get('online', False):
                motd = data.get('motd', {}).get('raw', ['Sin descripción'])[0]
                players = data.get('players', {})
                online = players.get('online', 0)
                max_players = players.get('max', 0)
                version = data.get('version', 'Bedrock')
                embed = discord.Embed(title="Server Status", color=discord.Color.green())
                embed.add_field(name="IP", value=f"`{ip}:{port}`", inline=False)
                embed.add_field(name="MOTD", value=motd, inline=False)
                embed.add_field(name="Jugadores", value=f"{online}/{max_players}", inline=True)
                embed.add_field(name="Versión", value=version, inline=True)
                
                if players.get('list'):
                    players_list = ", ".join(players['list'])
                    if len(players_list) > 1024:
                        players_list = players_list[:1021] + "..."
                    embed.add_field(name="Jugadores Online", value=players_list, inline=False)
                
                embed.set_footer(text="@MadVersal 2025")
                await ctx.send(embed=embed)
            else:
                error_msg = "El servidor está offline"
                if data.get('error'):
                    error_msg += f"\nRazón: {data['error']}"
                    
                embed = discord.Embed(title="Server Status", 
                                    description=f'`{ip}:{port}`\n{error_msg}',
                                    color=discord.Color.red())
                embed.set_footer(text="@MadVersal 2025")
                await ctx.send(embed=embed)
        except Exception as e:
            embed = discord.Embed(description=f'Error', 
                                color=discord.Color.purple())
            embed.set_footer(text="@MadVersal 2025")
            await ctx.send(embed=embed)

async def setup(bot):
    cog = Status(bot)
    await bot.add_cog(cog)
    print("[DEBUG] Cog Status cargado y comando !status registrado.")
