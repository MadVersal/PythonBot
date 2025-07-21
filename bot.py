# Zuriel V. Alejandro
# All rigths reserved
# Whit love ♥️.
import discord
from discord.ext import commands        

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')
    print("[DEBUG] Comandos registrados:")
    for command in bot.commands:
        print(f" - {command}")

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

import asyncio

async def main():
    
    await bot.load_extension('cogs.info')
    await bot.load_extension('cogs.ayuda')
    await bot.load_extension('cogs.status')
    await bot.load_extension('cogs.serverinfo')
    await bot.load_extension('cogs.botinfo')
    await bot.load_extension('cogs.uptime')
    await bot.load_extension('cogs.avatar')
    await bot.load_extension('cogs.userinfo')
    await bot.load_extension('cogs.players')
    await bot.load_extension('cogs.tickets')
    await bot.load_extension('cogs.ip')
    await bot.load_extension('cogs.say')
    
    await bot.load_extension('addons.bienvenidas')
    await bot.load_extension('addons.despedidas')
    await bot.start('Aqui pon tu token')

if __name__ == '__main__':
    asyncio.run(main())
# Zuriel V. Alejandro
# All rigths reserved
# Whit love ♥️.
