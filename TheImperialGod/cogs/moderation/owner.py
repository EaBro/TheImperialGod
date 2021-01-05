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
        print("Owner commands are loaded!")

    @commands.command()
    @commands.is_owner()
    async def leaveguild(self, ctx, guild_id : int):
        guild = self.client.get_guild(guild_id)
        await guild.leave()
        # send an embed
        embed = discord.Embed(title = "Imperial God leaves a guild", color = ctx.author.color)
        embed.add_field(name = f"Guild:", value = f"`{guild.name}`")
        embed.add_field(name = "New Usercount:", value = f"`{len(self.client.users)}`")
        embed.add_field(name = "New Servercount:", value = f'`{len(self.client.guilds)}`')
        await ctx.send(embed = embed)

    @commands.command()
    @commands.is_owner()
    async def osay(self, ctx, *, arg):
        """Says what you tell it to
        Uses: `imp osay <message>`"""
        await ctx.message.delete()
        await ctx.send(arg)

    @commands.command(aliases=["enable"])
    @commands.is_owner()
    async def load(self, ctx, *, extension):
        if extension not in ["cogs.moderation.owner", "cogs.moderation.admin"]:
            await self.client.load_extension(extension)
            await ctx.send(f"Loaded {extension}!")
        else:
            await ctx.send("Admin or owner commands cannot be enabled or disabled!")
            return

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, *, extension):
        if extension not in ["cogs.moderation.owner", "cogs.moderation.admin"]:
            await self.client.unload_extension(extension)
            await ctx.send(f"Unloaded {extension}!")
        else:
            await ctx.send("Admin or owner commands cannot be disabled!")
            return

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, *, extension):
        await self.client.reload_extension(extension)
        await ctx.send(f"Reloaded {extension}!")

    @commands.command()
    @commands.is_owner()
    async def embed(self, ctx, *, content):
        try:
            title, desc = content.split("|")
        except:
            await ctx.send("Type an embed in this format: `imp embed {title} | {description}`")
            return
        else:
            em = discord.Embed(title = title, color = ctx.author.color, description= desc)
            em.set_footer(text='Bot Made by NightZan999#0194')
            await ctx.send(embed = em)



def setup(client):
    client.add_cog(Owner(client))
