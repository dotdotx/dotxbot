import discord
import requests
from discord.ext import commands


class Numbers(commands.Cog):

    def __init__(self, dotxbot):
        self.dotxbot = dotxbot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Numbers cong loaded!')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def facts(self, ctx, number):
        response = requests.get(f'http://numbersapi.com/{number}')
        embed=discord.Embed(description=response.text)
        await ctx.channel.send(embed=embed)

async def setup(doxbot):
    await doxbot.add_cog(Numbers(doxbot))