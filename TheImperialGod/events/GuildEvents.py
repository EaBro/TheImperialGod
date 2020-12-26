import discord
from discord.ext import commands
import json

class GuildEvents(commands.Cog):
    def __init__(self, client):
        self.client = client
        with open("./config.json", "r") as f:
            config = json.load(f)

    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        sguild = self.client.get_guild(self.config["IDs"]["supportGuildId"])
        embed = discord.Embed(title = "I joined a new server!", color = discord.Color.red())

        embed.add_field(name = "Owner:", value = f"`{guild.owner}`")
        embed.add_field(name = "New Servercount:", value = f"`{len(client.guilds)}`")
        embed.add_field(name = "New Usercount:", value = f"`{len(client.users)}`")
        embed.add_field(name = "Name:", value = f"{str(guild.name)}")

        for channel in sguild.channels:
            if channel.id == self.config["IDs"]["channelLogId"]:
                await channel.send(embed = embed)
                break
    @commands.Cog.listener()
    async def on_guild_remove(self,guild):
        sguild = self.client.get_guild(self.config["IDs"]["supportGuildId"])
        embed = discord.Embed(title = "I left a server!", color = discord.Color.red())

        embed.add_field(name = "Owner:", value = f"`{guild.owner}`")
        embed.add_field(name = "New Servercount:", value = f"`{len(client.guilds)}`")
        embed.add_field(name = "New Usercount:", value = f"`{len(client.users)}`")
        embed.add_field(name = "Name:", value = f"{str(guild.name)}")

        for channel in sguild.channels:
            if channel.id == self.config["IDs"]["channelLogId"]:
                await channel.send(embed = embed)
                break
    @commands.Cog.listener()
    async def on_ready(self):
        print("GuildEvents are loaded!")

def setup(client):
    client.add_cog(GuildEvents(client))
