import discord
from discord.ext import commands
import json

class GuildEvents(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("GuildEvents are ready!")

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open("./config.json", "r") as f:
            config = json.load(f)
        serverId = int(config["IDs"]["serverLogId"])
        channelId = int(config["IDs"]["channelLogId"])

        embed = discord.Embed(title = "I joined a new server!", color = discord.Color.red())
        embed.add_field(name = "Owner:", value = f"`{guild.owner}`")
        embed.add_field(name = "New Servercount:", value = f"`{len(self.client.guilds)}`")
        embed.add_field(name = "New Usercount:", value = f"`{len(self.client.users)}`")
        embed.add_field(name = "Name:", value = f"{str(guild.name)}")


        guild = await self.client.get_guild(serverId)
        for channel in guild.channels:
            if channel.id == channelId:
                await channel.send(embed = embed)
                break

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open("./config.json", "r") as f:
            config = json.load(f)
        serverId = int(config["IDs"]["serverLogId"])
        channelId = int(config["IDs"]["channelLogId"])

        embed = discord.Embed(title = "I left a new server!", color = discord.Color.red())
        embed.add_field(name = "Owner:", value = f"`{guild.owner}`")
        embed.add_field(name = "New Servercount:", value = f"`{len(self.client.guilds)}`")
        embed.add_field(name = "New Usercount:", value = f"`{len(self.client.users)}`")
        embed.add_field(name = "Name:", value = f"{str(guild.name)}")


        guild = await self.client.get_guild(serverId)
        for channel in guild.channels:
            if channel.id == channelId:
                await channel.send(embed = embed)
                break

def setup(client):
    client.add_cog(GuildEvents(client))
