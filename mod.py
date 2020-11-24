import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext.commands import MissingPermissions, BadArgument

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

def setup(client):
    client.add_cog(Mod(client))