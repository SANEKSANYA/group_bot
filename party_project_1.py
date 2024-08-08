import discord
from discord.ext import commands
import os
from random import choice


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f'ГОТОВ УЖЕ КАК {bot.user}')




@bot.command()
async def trash(ctx):

    random_image = choice(os.listdir('imgs'))

    with open(f"imgs/{random_image}", "rb") as image:
       picture =  discord.File(image)

    await ctx.send(file = picture)


@bot.command("help_me")
async def help_me(ctx):
    await ctx.send("Привет! Я бот созданный для того, чтобы вы смогли понять, я чего начать перестать загрязнять природу. Команда /trash расскажет интересные факты, которые я знаю.")



bot.run("")

