import discord
from discord.ext import commands
import json

class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client
        with open("./config.json", "r") as f:
            config = json.load(f)
        self.ownerId = config["IDs"]["ownerId"]

    @commands.Cog.listener()
    async def on_ready(self):
        print("owner commands are loaded!")
    
    @commands.command()
    async def leaveguild(self, ctx, guild_id : int):
        if ctx.author.id != self.ownerId:
            await ctx.send("Only bot devs can use this command!")
            return

        guild = self.client.get_guild(guild_id)
        await guild.leave()
        embed = discord.Embed(title = "Imperial Bot leaves a guild", color = ctx.author.color)
        embed.add_field(name = f"Guild:", value = f"`{guild.name}`")
        await ctx.send(embed = embed)

    @commands.command()
    async def devwith(self, ctx, amount = 1000000):
        with open("./data/mainbank.json", "r") as f:
            users = json.load(f)

        if ctx.author.id != self.ownerId:
            return

        # assuming the user has an account
        users[str(self.ownerId)]["wallet"] += amount

        with open("./data/mainbank.json", "w") as f:
            json.dump(users, f)

def setup(client):
    client.add_cog(Owner(client))