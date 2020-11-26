import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext.commands import MissingPermissions, BadArgument
from asyncio import sleep
from discord.ext.commands import cooldown, BucketType
import random
import json

class Mod(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # Creating Helperfunctions
    async def open_muterole(self, role):
        roles = self.get_muterole()
        if str(role.id) in roles:
            return False
        else:
            roles[str(role.id)] = "none"

        with open('./data/muterole.json', 'w') as f:
            json.dump(roles, f)
        return True

    async def get_muterole(self):
        with open("./data/muterole.json", "r") as f:
            dict = json.load(f)
        return dict

    @commands.Cog.listener()
    async def on_ready(self):
        print("Mod commands Loaded!")

    @commands.command()
    @has_permissions(manage_roles = True)
    async def addrole(self, ctx, member : discord.Member = None,role : discord.Role = None, *, reason = None):
        if member == None:
            await ctx.send("You need to provide someone to add them the role")
            return
        if reason == None:
            reason = "No reason provided"
            pass
        if role == None:
            await ctx.send("Ping a role next time!")
            return
        
        await member.add_roles(role)
        embed = discord.Embed(title=  f"{member.name} has got a new role!!", color = ctx.author.color)
        embed.add_field(name = "Reason:", value = f"`{reason}`")
        embed.add_field(name = f"Member getting {role.name}:", value = f"{member.mention}")
        embed.add_field(name = "Role:", value = f"`{role.name}`")
        embed.add_field(name = "Moderator:", value = f"`{ctx.author.name}`", inline = False)
        await ctx.send(embed=  embed)

        try:
            await member.send(f"You were added {role.name} role in {ctx.guild.name}\nReason: `{reason}`\nModerator: `{ctx.author.name}`")       
        except:
            pass
    
    @addrole.error
    async def addrole_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(title = "Addrole Failed!", color = ctx.author.color)
            embed.add_field(name = "Reason:", value = f"Manage Roles Permissions Missing!")
            await ctx.send(embed = embed)
        if isinstance(error, BadArgument):
            embed = discord.Embed(title = "Addrole Failed!", color = ctx.author.color)
            embed.add_field(name = "Reason:", value = f"Tag a user and a role!")
            await ctx.send(embed = embed)

    @commands.command()
    @has_permissions(manage_roles = True)
    async def removerole(self, ctx, member : discord.Member = None,role : discord.Role = None, *, reason = None):
        if member == None:
            await ctx.send("You need to provide someone to add them the role")
            return
        if reason == None:
            reason = "No reason provided"
            pass
        if role == None:
            await ctx.send("Ping a role next time!")
            return
        
        await member.remove_roles(role)
        embed = discord.Embed(title=  f"{member.name} was softbanned!", color = ctx.author.color)
        embed.add_field(name = "Reason:", value = f"`{reason}`")
        embed.add_field(name = f"Member losing {role.name}:", value = f"{member.mention}")
        embed.add_field(name = "Role:", value = f"`{role.mention}`")
        embed.add_field(name = "Moderator:", value = f"`{ctx.author.name}`", inline = False)
        await ctx.send(embed=  embed)

        try:
            await member.send(f"You lost {role.name} role in {ctx.guild.name}\nReason: `{reason}`\nModerator: `{ctx.author.name}`")
        except:
            pass

    @removerole.error
    async def removerole_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(title = "Removerole Failed!", color = ctx.author.color)
            embed.add_field(name = "Reason:", value = f"Manage Roles Permissions Missing!")
            await ctx.send(embed = embed)
        if isinstance(error, BadArgument):
            embed = discord.Embed(title = "Removerole Failed!", color = ctx.author.color)
            embed.add_field(name = "Reason:", value = f"Tag a user and a role!")
            await ctx.send(embed = embed)

    @commands.command(aliases = ["purge", "massdelete", "bulkdel"])
    @has_permissions(manage_messages = True)
    async def clear(self, ctx, amount = 1):
        await ctx.channel.purge(limit = amount)
        await ctx.send("Done purging, deleting this in 5 seconds", delete_in = 5)
    
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(title = "Purge Failed!", color = ctx.author.color)
            embed.add_field(name = "Reason:", value = f"Manage Messages Permissions Missing!")
            await ctx.send(embed = embed)

    @commands.command()
    @has_permissions(manage_channels = True)
    async def lock(self, ctx, channel = None):
        if channel == None:
            channel = ctx.channel
        
        await channel.set_permissions(ctx.guild.default_role, send_messages = False, read_messages = True)
        embed = discord.Embed(title = "Channel Was Locked!", color = ctx.author.color)
        embed.add_field(name = "Moderator:", inline = True, value = f"`{ctx.author.name}`")
        embed.add_field(name = "Reason:", inline = True, value = f"`Spam`")
        embed.add_field(name = "Channel:", value = f"`{channel.mention}`")
        await channel.send(embed = embed)

    @lock.error
    async def lock_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(title = "Lock Failed!", color = ctx.author.color)
            embed.add_field(name = "Reason:", value = f"Manage Channels Permissions Missing!")
            await ctx.send(embed = embed)


    @commands.command()
    @has_permissions(manage_channels = True)
    async def unlock(self, ctx, channel = None):
        if channel == None:
            channel = ctx.channel
        
        await channel.set_permissions(ctx.guild.default_role, send_messages = True, read_messages = True)
        embed = discord.Embed(title = "Channel Was Unlocked!", color = ctx.author.color)
        embed.add_field(name = "Moderator:", inline = True, value = f"`{ctx.author.name}`")
        embed.add_field(name = "Reason:", inline = True, value = f"`Spam`")
        embed.add_field(name = "Channel:", value = f"`{channel.mention}`")
        await ctx.send(embed = embed)

    @unlock.error
    async def unlock_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(title = "Unlock Failed!", color = ctx.author.color)
            embed.add_field(name = "Reason:", value = f"Manage Channels Permissions Missing!")
            await ctx.send(embed = embed)

    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def setdelay(self, ctx, amount = 5, *, reason = None):
        if amount > 6000:
            await ctx.channel.send("Amount needs to be less than 6000!")
            return

        await ctx.channel.edit(slowmode_delay=amount)
        embed = discord.Embed(title = "Change in Channel Settings", color = ctx.author.color)
        embed.add_field(name = "New slowmode:", value = f"`{amount} seconds`")
        embed.add_field(name = "Moderator:", value = f"`{ctx.author.name}`")
        embed.add_field(name = "Reason:", value = f"`{reason}`")
        await ctx.send(embed = embed)

    @setdelay.error
    async def setdelay_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(title = "Setdelay Failed!", color = ctx.author.color)
            embed.add_field(name = "Reason:", value = f"Manage Channels Permissions Missing!")
            await ctx.send(embed = embed)

    @commands.command()
    @has_permissions(ban_members = True)
    async def unban(ctx, member : str, *, reason = None):
        banned_users = await ctx.guild.bans()
        member_name, member_disc = member.split("#")

        for banned_entry in banned_users:
            user = banned_entry.user

            if (user.name, user.discriminator) == (member_name, member_disc):
                await ctx.guild.unban(user)
                embed = discord.Embed(title = f"{member_name} was unbanned!", color = ctx.author.color)
                embed.add_field(name = "Reason:", value = f"`{reason}`")
                embed.add_field(name = "Moderator:", value = f"`{ctx.author.name}`")
                await ctx.send(embed = embed)
                return

        await ctx.send("Not a valid user, try it like this:\`imp unban name#disc`")

    #normal function
    def convert(self, time):
        pos = ["s","m","h","d"]

        time_dict = {"s" : 1, "m" : 60, "h" : 3600 , "d" : 3600*24}

        unit = time[-1]

        if unit not in pos:
            return -1
        try:
            val = int(time[:-1])
        except:
            return -2

        return val * time_dict[unit]


    @commands.command(aliases = ["muterole"])
    @has_permissions(manage_guild = True)
    async def setmuterole(self, ctx, *, role : discord.Role = None):
        await self.open_muterole(ctx.guild)
        roles = await self.get_muterole()
        embed = discord.Embed(title = "Muterole has been setup", color = ctx.author.color)
        embed.add_field(name = "Moderator:", value = f"`{ctx.author.name}`")
        embed.add_field(name = "New muterole:", value = f"{role.mention}")
        try:
            old_role = ctx.guild.get_role(roles[str(ctx.guild.id)])
            embed.add_field(name = "Old Muterole:", value = f"{old_role.mention}")
        except:
            pass
        finally:
            await ctx.send(embed = embed)
        
        roles[str(ctx.guild.id)] = role.id
    
    @setmuterole.error
    async def setmuterole_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            embed = discord.Embed(title = "Mute setup Failed!", color = ctx.author.color)
            embed.add_field(name = "Reason:", value = f"Manage Server Permissions Missing!")
            await ctx.send(embed = embed)
        if isinstance(error, BadArgument):
            embed = discord.Embed(title = "Setmuterole Failed!", color = ctx.author.color)
            embed.add_field(name = "Reason:", value = f"Tag a role!")
            await ctx.send(embed = embed)

    @commands.command()
    @has_permissions(kick_members = True, manage_channels = True)
    async def mute(self, ctx, member: discord.Member = None, *, reason = None):
        await self.open_muterole(ctx.guild)
        if member == None:
            await ctx.send("Wow, define a member to get muted. Your an idiot!")
        
        with open("./data/muterole.json", "r") as f:
            roles = json.load(f)

        if roles[str(ctx.guild.id)] == "none":
            await ctx.send("Muting for this server has not been set up. Do set it up, type `imp setmuterole <role>`")
            return
        
        muterole = roles[str(ctx.guild.id)]
        await member.add_roles(muterole)

        embed = discord.Embed(title = f"{member.name} was muted!", color = member.color)
        embed.add_field(name = "Reason:", value = f"`{reason}`")
        embed.add_field(name = "Moderator:", value = f"`{ctx.author.name}`")
        await ctx.send(embed = embed)

    @commands.command()
    @has_permissions(manage_channels = True)
    async def count(ctx, channel: discord.TextChannel = None):
        channel = channel or ctx.channel #or since sometimes people have it locked!
        messages = await channel.history(limit = None).flatten()
        count = len(messages)

        embed = discord.Embed(
        title="Total Messages",
        colour=ctx.author.color,
        description=f"There were {count} messages in {channel.mention}")

        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @cooldown(1, 3, BucketType.user)
    async def unban(self, ctx, member=None, *, reason='No Reason Was Provided'):
        if member == None:
            await ctx.send(f"You can't unban yourself, {ctx.author.mention}\nNext time provide a user.")
        banned_users = await ctx.guild.bans()
        member_name, member_disc = member.split('#')

        for banned_entry in banned_users:
            user = banned_entry.user

            if (user.name, user.discriminator) == (member_name, member_disc):
                em = discord.Embed(title = f"{member} has been unbanned!", description = f"**Responsible Moderator:** {ctx.author.mention}\n**Reason:** {reason}", color = ctx.author.color, timestamp = ctx.message.created_at)
    
                await ctx.send(embed=em)

                await member.send(f"You were unbanned from **{ctx.guild}** by **{ctx.author}** because **{reason}**")

                return

        await ctx.send(member + ' was not found. Make sure you gave a valid format (For eg. The Imperial God#9642)')

    @commands.command()
    @has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        await member.kick(reason = reason)
        em = discord.Embed(title = f"<:success:761297849475399710> Kick was successful!", color = ctx.author.color)
        em.add_field(name = f"Victim:", value = f"`{member.name}`")
        em.add_field(name = "Reason: ", value = f"`{reason}`")
        em.add_field(name = "Moderator:", value = f"`{ctx.author.name}`")
        await ctx.send(embed = em)
        try:
            await member.send(f"You were kicked in {ctx.guild.name}\nReason: `{reason}`\nModerator: `{ctx.author.name}`")
        except:
            pass

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em = discord.Embed(title = "<:fail:761292267360485378> Kick Failed!", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "`Kick members Permission Missing!`")
            await ctx.send(embed = embed)

    @commands.command()
    @has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, *,reason = None):
        await member.ban(reason = reason)
        em = discord.Embed(title = f"<:success:761297849475399710> Ban was successful!", color = ctx.author.color)
        em.add_field(name = f"Victim:", value = f"`{member.name}`")
        em.add_field(name = "Reason: ", value = f"`{reason}`")
        em.add_field(name = "**Moderator**:", value = f"`{ctx.author.name}`")
        await ctx.send(embed = em)
        try:
            await member.send(f"You were banned in {ctx.guild.name}\nReason: `{reason}`\nModerator: `{ctx.author.name}`")
        except:
            pass
    
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em = discord.Embed(title = "<:fail:761292267360485378> Ban Failed!", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "`Ban members Permission Missing!`")
            await ctx.send(embed = embed)

    async def get_warns(self):
        with open("./data/warns.json", "r") as f:
            warns = json.load(f)
        return warns
    
    async def open_guild(self, guild):
        warns = await self.get_warns()
        if str(guild.id) not in warns:
            warns[str(guild.id)] = {}
            return True
        else:
            return False

        with open("warns.json", "w") as f:
            json.dump(warns, f)

    async def addwarns(self, guild, user, number : int):
        warns = await self.get_warns()
        await self.open_guild(guild)

        if str(user.id) not in warns[str(guild.id)]:
            warns[str(guild.id)][str(user.id)] = number
        else:
            warns[str(guild.id)][str(user.id)] += number

        with open("warns.json", "w") as f:
            json.dump(warns, f)
    
    async def removewarns(self, guild, user, number : int):
        warns = await self.get_warns()
        await self.open_guild(guild)

        if str(user.id) not in warns[str(guild.id)]:
            return [False, 1]
        else:
            if warns[str(guild.id)][str(user.id)] < number:
                return [False, 2]
            warns[str(guild.id)][str(user.id)] -= number

        with open("warns.json", "w") as f:
            json.dump(warns, f)
    
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


def setup(client):
    client.add_cog(Mod(client))