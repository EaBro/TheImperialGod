import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import random
import json

class Automod(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Automod ready!")
    
    @commands.command()
    @has_permissions(administrator = True)
    async def enableautomod(self, ctx, *, reason = None):
        with open("./data/automod.json", "r") as f:
            guilds = json.load(f)
        
        with open("./data/emojis.json", "r") as f:
            emojis = json.load(f)

        if str(ctx.guild.id) in guilds:
            guilds[str(ctx.guild.id)]["automod"] = "true"
        else:
            guilds[str(ctx.guild.id)] = {}
            guilds[str(ctx.guild.id)]["automod"] = "true"

        embed = discord.Embed(title = f"<:success:761297849475399710> change in server settings!", color = ctx.author.color,
        description = "An awesome moderator, enabled automod. Beware no more **bad words!**"
        )
        embed.add_field(name = "Automod Status:", value = f"`Automod = True`")
        embed.add_field(name = "Reason:", value = f"`{reason}`")
        embed.add_field(name = "Moderator:", value = f"`{ctx.author.name}`", inline = False)
        await ctx.send(embed = embed)

        with open("./data/automod.json", "w") as f:
            json.dump(guilds, f)

    @enableautomod.error
    async def enableautomod_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Bruh you really think you can use that?")
    
    @commands.command()
    @has_permissions(administrator = True)
    async def disableautomod(self, ctx, *, reason = None):
        with open("./data/automod.json", "r") as f:
            guilds = json.load(f)

        with open("./data/emojis.json","r") as f:
            emojis = json.load(f)

        if str(ctx.guild.id) in guilds:
            guilds[str(ctx.guild.id)]["automod"] = "false"
        else:
            guilds[str(ctx.guild.id)] = {}
            guilds[str(ctx.guild.id)]["automod"] = "false"

        embed = discord.Embed(title = f'<:success:761297849475399710> Change in Server Settings', color = ctx.author.color)
        embed.add_field(name = 'Automod:', value = "`Automod = False`")
        embed.add_field(name = "Reason:", value = f"`{reason}`")
        embed.add_field(name = "Moderator:", value = f"`{ctx.author.name}`", inline = False)
        await ctx.send(embed = embed)

        with open("data/automod.json", "w") as f:
            json.dump(guilds, f)

    @disableautomod.error
    async def disableautomod_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("Bruh you really think you can use that?")

    @commands.command()
    async def checkautomod(self,ctx):
        with open("./data/automod.json", "r") as f:
            guilds = json.load(f)
        
        embed = discord.Embed(title = f"Automoderation status of {ctx.guild.name}", color = ctx.author.color)

        if str(ctx.guild.id) in guilds:
            if guilds[str(ctx.guild.id)]["automod"] == "true":
                embed.add_field(name = "Automod Status:", value = f"`True`")
            elif guilds[str(ctx.guild.id)]["automod"] == "false":
                embed.add_field(name = "Automod Status:", value = f"`False`")
            await ctx.send(embed = embed)
        else:
            embed.add_field(name = "Automod Status:", value = f"`<:fail:761292267360485378> Not set up!`")
            embed.add_field(name = "What to do?", value = "Ask a mod to set this up!")
            await ctx.send(embed = embed)
    

def setup(client):  
    client.add_cog(Automod(client))