import discord
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.filtered_words = ['idiot', 'Idiots', "DIE", "ass", "butt", "Fool", "shit", "bitch"]

    @commands.Cog.listener()
    async def on_ready(self):
        print("Misc commands are ready!")

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title = "Invite Link:", color = ctx.author.color)
        embed.add_field(name = "Here:", value = f"[Click me]({INVITE_LINK})")
        await ctx.send(embed = embed)

    @commands.command()
    async def servercount(self, ctx):
        sc = 0
        for i in self.client.guilds:
            sc += 1
        embed = discord.Embed(title = "Server Count", color = ctx.author.color)
        embed.add_field(name = "Server Count:", value = f"`{sc}`")
        embed.add_field(name = "User Count:", value = f'`{len(self.client.users)}`')
        await ctx.send(embed = embed)

    @commands.command()
    async def candy(self, ctx):
        await ctx.send("You want candy, take it!")
        await ctx.send(file = discord.File("./assets/candy.jpg"))

    @commands.command()
    async def leaveguild(self, ctx, guild_id : int)
        if ctx.author.id != ZAN_ID:
            await ctx.send("Only bot devs can use this command!")
            return

        guild = self.client.get_guild(guild_id)
        await guild.leave()
        embed = discord.Embed(title = "Imperial Bot leaves a guild", color = ctx.author.color)
        embed.add_field(name = f"Guild:", value = f"`{guild.name}`")
        await ctx.send(embed = embed)
    
    @commands.command()
    async def say(self, ctx, *, msg = None):
        if msg == None:
            await ctx.send("No message provided!")
            return

        for word in self.filtered_words:
            if word in msg.content:
                return
        
        await ctx.send(msg)

    

def setup(client):
    client.add_cog(Misc(client))