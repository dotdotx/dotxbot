import discord
import tweepy
import config
from discord import app_commands
from discord.ext import commands


class Questions(commands.Cog):

    def __init__(self, dotxbot: commands.Bot):
        self.dotxbot = dotxbot


    @commands.Cog.listener()
    async def on_ready(self):
        print('Questions cog loaded!')
    
    @commands.command()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync(guild=ctx.guild)
        await ctx.send(f'Synced {len(fmt)} commands!')

    @app_commands.command(name='questions', description='questions form')
    async def questions(self, interaction: discord.Interaction, quesiton: str):
        await interaction.response.send_message('Answered!')


class TwitterAPI:
    def __init__(self):
        self.api_key = config.TWITTER_API_KEY
        self.api_secret_key = config.TWITTER_API_SECRET_KEY
        self.access_token = config.TWITTER_ACCESS_TOKEN
        self.access_token_secret = config.TWITTER_ACCESS_TOKEN_SECRET
        self.authenticator = tweepy.OAuthHandler(self.api_key, self.api_secret_key)
        self.authenticator.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.authenticator, wait_on_rate_limit=True)


twitter_api = TwitterAPI()



async def setup(dotxbot):
    await dotxbot.add_cog(Questions(dotxbot), guilds=[discord.Object(id=931121706070839336)])