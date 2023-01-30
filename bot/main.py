import discord
import config
import asyncio
import os
from discord.ext import commands


dotxbot = commands.Bot(command_prefix='.', intents=discord.Intents.all(), application_id='1064812267599831070')


@dotxbot.event
async def on_ready():
    print('Online!')
    

@dotxbot.event
async def on_message(message):
    await dotxbot.process_commands(message)
    if message[0] == '.':
        return
    if message.author == dotxbot.user:
        return
    await message.channel.send('Sup bruh?')

async def load():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await dotxbot.load_extension(f'cogs.{file[:-3]}')

async def main():
    await load()
    await dotxbot.start(config.DISCORD_BOT_TOKEN)

asyncio.run(main())