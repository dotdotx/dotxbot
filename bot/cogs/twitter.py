import discord
import tweepy
import asyncio
import config
from discord import app_commands
from discord.ext import tasks, commands


class Twitter(commands.Cog):

    def __init__(self, dotxbot: commands.Bot):
        self.dotxbot = dotxbot


    @commands.Cog.listener()
    async def on_ready(self):
        print('Twitter cog loaded!')
    
    @commands.command()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync(guild=ctx.guild) # sync for specifi guild
        # fmt = await ctx.bot.tree.sync() # sync globally 
        await ctx.send(f'Synced {len(fmt)} commands!')
        return
    

    @app_commands.command(name='follow', description='follow twitter posts from specified twitter handle')
    # @tasks.loop(seconds=10)
    async def follow(self, interaction: discord.Interaction, twitter_username: str):#, channel: str, inclutde_retweets: bool):
        compare_id = 0
        prefix_post_url ='https://twitter.com/'

        tweets = twitter_api.api.user_timeline(
            screen_name=twitter_username, 
            count=1, 
            tweet_mode='extended', 
            exclude_replies=True, 
            include_rts=False
            )
        for tweet in tweets:
            if compare_id < tweet.id:
                compare_id = tweet.id
                embed = discord.Embed(color=discord.Color.green())
                embed.set_author(name=tweet.user.name, url=f'{prefix_post_url}{tweet.user.screen_name}')
                embed.description = tweet.full_text
                embed.set_image(url=tweet.entities['media'][0]['media_url_https'])
                embed.set_thumbnail(url=tweet.user.profile_image_url_https)
                embed.set_footer(text='Powered by dotX BOT', 
                icon_url='https://pbs.twimg.com/media/FnuqBzaXoAI1nVX?format=png&name=240x240')
                embed.timestamp = tweet.created_at
                await interaction.response.send_message(f'{prefix_post_url}{tweet.user.screen_name}/status/{tweet.id}', embed=embed)
            else:
                print('Waiting for a new post!')


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
    await dotxbot.add_cog(Twitter(dotxbot), guilds=[discord.Object(id=931121706070839336)]) # specific guild
    # await dotxbot.add_cog(Twitter(dotxbot)) # global