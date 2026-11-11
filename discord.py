import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def ship(ctx, nombre1:str, nombre2:str):
    import random
    porcentaje = random.randint(0, 100)
    await ctx.send(nombre1 + " ❤️ " + nombre2 + " = " + str(porcentaje) + "% de compatibilidad")

bot.run("")
