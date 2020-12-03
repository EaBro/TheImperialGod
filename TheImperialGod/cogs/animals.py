import discord
from discord.ext import commands
import praw
import random

class Animals(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.reddit = praw.Reddit(
            client_id = 'NY_kPmfmJV1VAg',
            client_secret = "GNKjyvMHErF9yYqZGrhx6MxG55WtVw",
            username = "NightZan999",
            password = "python123_praw",
            user_agent = "python_praw"
        )

    @commands.Cog.listener()
    async def on_ready(self):
        print("Animal module loaded!")

    @commands.command()
    async def dog(self, ctx):
        subreddit = self.reddit.subreddit("dog")
        top = subreddit.top(limit = 100)

        all_subs = []
        for submission in top:
            all_subs.append(submission)

        sub = random.choice(all_subs)
        embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
        embed.set_image(url = sub.url)
        await ctx.send(embed = embed)

    @commands.command()
    async def cat(self, ctx):
        subreddit = self.reddit.subreddit("cat")
        top = subreddit.top(limit = 100)

        all_subs = []
        for submission in top:
            all_subs.append(submission)

        sub = random.choice(all_subs)
        embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
        embed.set_image(url = sub.url)
        await ctx.send(embed = embed)

    @commands.command()
    async def duck(self, ctx):
        subreddit = self.reddit.subreddit("duck")
        top = subreddit.top(limit = 100)

        all_subs = []
        for submission in top:
            all_subs.append(submission)

        sub = random.choice(all_subs)
        embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
        embed.set_image(url = sub.url)
        await ctx.send(embed = embed)

    @commands.command()
    async def fox(self, ctx):
        subreddit = self.reddit.subreddit("fox")
        top = subreddit.top(limit = 100)

        all_subs = []
        for submission in top:
            all_subs.append(submission)

        sub = random.choice(all_subs)
        embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
        embed.set_image(url = sub.url)
        await ctx.send(embed = embed)

    @commands.command()
    async def panda(self, ctx):
        subreddit = self.reddit.subreddit("panda")
        top = subreddit.top(limit = 10)

        all_subs = []
        for submission in top:
            all_subs.append(submission)

        sub = random.choice(all_subs)
        embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
        embed.set_image(url = sub.url)
        await ctx.send(embed = embed)

    @commands.command()
    async def koala(self, ctx):
        subreddit = self.reddit.subreddit("koala")
        top = subreddit.top(limit = 10)

        all_subs = []
        for submission in top:
            all_subs.append(submission)

        sub = random.choice(all_subs)
        embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
        embed.set_image(url = sub.url)
        await ctx.send(embed = embed)

    @commands.command()
    async def tiger(self, ctx):
        subreddit = self.reddit.subreddit("tiger")
        top = subreddit.top(limit = 10)

        all_subs = []
        for submission in top:
            all_subs.append(submission)

        sub = random.choice(all_subs)
        embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
        embed.set_image(url = sub.url)
        await ctx.send(embed = embed)

    @commands.command()
    async def lion(self, ctx):
        subreddit = self.reddit.subreddit("lion")
        top = subreddit.top(limit = 10)

        all_subs = []
        for submission in top:
            all_subs.append(submission)

        sub = random.choice(all_subs)
        embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
        embed.set_image(url = sub.url)
        await ctx.send(embed = embed)

    @commands.command(aliases = ["snek"])
    async def snake(self, ctx):
        subreddit = self.reddit.subreddit("snake")
        top = subreddit.top(limit = 10)

        all_subs = []
        for submission in top:
            all_subs.append(submission)

        sub = random.choice(all_subs)
        embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
        embed.set_image(url = sub.url)
        await ctx.send(embed = embed)

    @commands.command()
    async def owl(self, ctx):
        subreddit = self.reddit.subreddit("owl")
        top = subreddit.top(limit = 10)

        all_subs = []
        for submission in top:
            all_subs.append(submission)

        sub = random.choice(all_subs)
        embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
        embed.set_image(url = sub.url)
        await ctx.send(embed = embed)
    
    @commands.command(aliases = ["pandared", "rpanda", "pandr"])
    async def redpanda(self, ctx):
        subreddit = self.reddit.subreddit("redpanda")
        top = subreddit.top(limit = 10)

        all_subs = []
        for submission in top:
            all_subs.append(submission)

        sub = random.choice(all_subs)
        embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
        embed.set_image(url = sub.url)
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Animals(client))