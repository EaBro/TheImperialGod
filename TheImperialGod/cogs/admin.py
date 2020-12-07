import discord
from discord.ext import commands
import json
from discord.ext.commands import has_permissions

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.filtered_words = ['idiot', 'Idiots', "DIE", "ass", "butt", "Fool", "shit", "bitch"]


    @commands.Cog.listener()
    async def on_message(self, msg):
        with open("./data/automod.json", "r") as f:
            guilds = json.load(f)

        ctx = await self.client.get_context(msg)

        try:
            if guilds[str(ctx.guild.id)]["automod"] == "true":
                for word in self.filtered_words:
                    if word in msg.content.lower():
                        await msg.delete()
        except:
            pass

        try:
            if msg.mentions[0] == self.client.user:
                await msg.channel.send(f"My prefix for this server is `imp`\nCheck out `imp help` for more information")
            elif self.client.user in msg.mentions:
                for i in range(0, len(msg.mentions)):
                    if msg.mentions[i] == self.client.user:
                        await msg.channel.send(f"My prefix for this server is `imp`\nCheck out `imp help` for more information")
                        break
            else:
                pass
        except:
            pass


        await self.client.process_commands(msg)

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

        with open("./data/automod.json", "w") as f:
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
    
    @commands.command()
    @has_permissions(manage_guild = True)
    async def addmemechannel(self, ctx, channel : discord.TextChannel, *, reason = None):
        with open("./data/automod.json", "r") as f:
            memes = json.load(f)
        
        guild = ctx.guild
        if str(guild.id) in memes:
            memes[str(guild.id)]["memechannel"] = channel.id
        else:
            memes[str(guild.id)] = {}
            memes[str(guild.id)]["memechannel"] = channel.id
        
        embed = discord.Embed(title = f"<:success:761297849475399710> Change in server settings!", color = ctx.author.color,
        description = "An awesome moderator, enabled automemes."
        )
        embed.add_field(name = "Meme Status:", value = f"`Automemes = True`")
        embed.add_field(name = "Reason:", value = f"`{reason}`")
        embed.add_field(name = "Moderator:", value = f"`{ctx.author.name}`", inline = False)
        await ctx.send(embed = embed)

        with open("./data/automod.json", "w") as f:
            json.dump(memes, f)
    
def setup(client):
    client.add_cog(Admin(client))