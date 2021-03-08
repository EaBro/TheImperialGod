import discord
from discord.ext import commands
import traceback
import random
import datetime
import json

class Information(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.launched_at = datetime.datetime.utcnow()

    @commands.Cog.listener()
    async def on_ready(self):
        print("Information is ready")

    @commands.command(aliases = ["guild", "guildinfo", "si"])
    async def serverinfo(self, ctx):

        findbots = sum(1 for member in ctx.guild.members if member.bot)
        roles = sum(1 for role in ctx.guild.roles)

        embed = discord.Embed(title = 'Infomation about ' + ctx.guild.name + '.', colour = ctx.author.color)
        embed.set_thumbnail(url = str(ctx.guild.icon_url))
        embed.add_field(name = "Guild's name: ", value = ctx.guild.name)
        embed.add_field(name = "Guild's owner: ", value = str(ctx.guild.owner))
        embed.add_field(name = "Guild's verification level: ", value = str(ctx.guild.verification_level))
        embed.add_field(name = "Guild's id: ", value = f"`{ctx.guild.id}`")
        embed.add_field(name = "Guild's member count: ", value = f"{ctx.guild.member_count}")
        embed.add_field(name="Bots", value=f"`{findbots}`", inline=True)
        embed.add_field(name = "Guild created at: ", value = str(ctx.guild.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC")))
        embed.add_field(name = "Number of Roles:", value = f"`{roles}`")
        embed.set_footer(text='Bot Made by NightZan999#0194')
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)

        await ctx.send(embed =  embed)

    @commands.command(aliases = ["ci"])
    async def channelinfo(self, ctx, channel : discord.TextChannel = None):
        if channel == None:
            channel = ctx.channel
        
        em = discord.Embed(title = f"Info about {channel.name}", color = ctx.author.color, description = f"Here is an insight into {channel.mention}")
        em.add_field(name = "ID:", value = f"`{channel.id}`")
        em.add_field(name = "Name:", value = f"`{channel.name}`")
        em.add_field(name = "Server it belongs to:", value = f"{channel.guild.name}", inline = True)
        
        try:
            em.add_field(name = "Category ID:", value = f"`{channel.category_id}`", inline = False)
        except:
            pass
        em.add_field(name = "Topic:", value = f"`{channel.topic}`")
        em.add_field(name = "Slowmode:", value = f"`{channel.slowmode_delay}`", inline = True)

        em.add_field(name = "People who can see the channel:", value = f"`{len(channel.members)}`", inline = False)
        em.add_field(name = "Is NSFW:", value = f"`{channel.is_nsfw()}`")
        em.add_field(name = "Is News:", value = f"`{channel.is_news()}`", inline = True)
        
        em.set_footer(text = "invite me ;)", icon_url = ctx.author.avatar_url)
        em.set_thumbnail(url = str(ctx.guild.icon_url))
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        
        await ctx.send(embed = em)

    @commands.command()
    async def userinfo(self, ctx, member : discord.Member = None):
        if member == None:
            member = ctx.author
        pos = sum(m.joined_at < member.joined_at for m in ctx.guild.members if m.joined_at is not None)
        roles = [role for role in member.roles]
        embed = discord.Embed(color=member.color, timestamp=datetime.datetime.utcnow())
        embed.set_author(name=f"{member}", icon_url=member.avatar_url)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p"))
        embed.add_field(name='Registered at:', value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p'))
        embed.add_field(name='Bot?', value=f'{member.bot}')
        embed.add_field(name='Status?', value=f'{member.status}')
        embed.add_field(name='Top Role?', value=f'{member.top_role}')
        embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles[:1]]))
        embed.add_field(name='Join position', value=pos)
        embed.set_footer(icon_url=member.avatar_url, text=f'Requested By: {ctx.author.name}')
        embed.set_footer(text='Bot Made by NightZan999#0194')
        await ctx.send(embed=embed)
    
    @userinfo.error
    async def userinfo_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            em = discord.Embed(title = f"<:fail:761292267360485378> Userinfo Error", color = ctx.author.color)
            em.add_field(name = f"Reason:", value = f"Arguments were of the wrong data type!")
            em.add_field(name = "Args", value = "```\nimp userinfo [@user]\n```")
            em.set_thumbnail(url = ctx.author.avatar_url)
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)


    @commands.command()
    async def whois(self,ctx, user : discord.Member = None):
        if user == None:
            user = ctx.author
        em = discord.Embed(title = user.name, color = user.color)
        em.add_field(name = "ID:", value = user.id)
        em.set_thumbnail(url = user.avatar_url)
        em.set_footer(text='Bot Made by NightZan999#0194')
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = em)

    @whois.error
    async def whois_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            em = discord.Embed(title = f"<:fail:761292267360485378> Whois Error", color = ctx.author.color)
            em.add_field(name = f"Reason:", value = f"Arguments were of the wrong data type!")
            em.add_field(name = "Args", value = "```\nimp whois [@user]\n```")
            em.set_thumbnail(url = ctx.author.avatar_url)
            em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
            await ctx.send(embed = em)
            
    @commands.command(aliases = ["bi"])
    async def botinfo(self, ctx):
        embed = discord.Embed(title = "Botinfo", color = ctx.author.color,
        description = "TheImperialGod, is an awesome customizable discord bot with awesome features. Check some information about the bot below!"
        )
        embed.add_field(name = "First went live on:", value = "1 / 10 / 2020")
        embed.add_field(name = "Started coding on:", value = "26 / 9 / 2020")
        embed.add_field(name = f"Creator", value = f"NightZan999#0194")
        embed.add_field(name = 'Hosting', value = f"Chaotic Destiny Hosting ")
        embed.add_field(name = "Servers:", value = f'`{len(self.client.guilds)}`')
        embed.add_field(name = 'Customizable Settings:', value = f"Automoderation and utilities! ")
        embed.add_field(name = "Database:", value = "SQLite3")
        embed.add_field(name = "Website:", value = "<:VERIFIED_DEVELOPER:761297621502656512> [Web Dashboard](https://theimperialgod.ml)")
        embed.add_field(name = "Number of Commands:", value = f"`85` (including special owner commands)")
        embed.add_field(name = "**Tech:**", value = "```diff\n+ Library : discord.py\n+ Database : AIOSQLite\n+ Hosting Services : Chaotic Destiny Hosting!\n```", inline = False)
        embed.add_field(name = "Users:", value = f'`{len(self.client.users)}`')
        embed.set_footer(text='Bot Made by NightZan999#0194', icon_url = ctx.author.avatar_url)
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)

    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title = ":ping_pong: Pong!", color = ctx.author.color,
        description = "The number rlly doesn't matter. Smh!")
        embed.add_field(name=  "Client Latency", value = f"`{round(self.client.latency * 1000)}ms`")
        embed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        embed.set_footer(text='Bot Made by NightZan999#0194')
        await ctx.send(embed = embed)
    
    @commands.command()
    async def credits(self, ctx):
        em = discord.Embed(title = ":scroll: Credits of TheImperialGod", color = ctx.author.color, description = "Github link is [here](https://github.com/NightZan999/TheImperialGod)")
        em.add_field(name = "#1 NightZan999", value = f"""I have done everything on TheImperialGod, coded the entire bot, taken feedback, grown it to {len(self.client.guilds)} servers.\nI am even writing this right now!\nMy hopes are to you, if you like this bot type: `imp support`. That shows you ways to support TheImperialGod"\n\nI have written 70,000 lines of code for the bot and the website, so yeah-""")
        em.add_field(name = '#2 Github', value = "I did do all the coding, but I made TheImperialGod open source, this is why many people respond to my issues. Some people have corrected some glitches, and a full credits list is avalible on github")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        em.set_footer(text = "invite me now!")
        await ctx.send(embed = em)
    
    @commands.command()
    async def uptime(self, ctx):
        current_time = datetime.datetime.utcnow()
        uptime = (current_time - self.launched_at)
        em = discord.Embed(title = "<:zancool:809268843138646066> My Uptime", color = ctx.author.color)
        em.add_field(name = "Uptime", value = "I have been online for {}!".format(uptime))
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        em.set_footer(text = "Requested by {}".format(ctx.author.name), icon_url = ctx.author.avatar_url)
        await ctx.send(embed = em)
    
    @commands.command()
    async def roleinfo(self, ctx, *, role_: discord.Role = None):
        role = role_
        if role is None:
            await ctx.send("Please provide a valid role")
        em = discord.Embed(title = f"Info about {role.name}", color = ctx.author.color, description = f"Here is an insight into {role.mention}")
        em.add_field(name = "ID:", value = f"`{role.id}`")
        em.add_field(name = "Name:", value = f"`{role.name}`")
        em.add_field(name = "Server it belongs to:", value = f"{role.guild.name}", inline = True)

        em.add_field(name = "Hoisted:", value = f"`{role.hoist}`", inline = False)
        em.add_field(name = "Managed by extension:", value = f"`{role.managed}`")
        em.add_field(name = "Boost Role:", value = f"`{role.is_premium_subscriber()}`", inline = True)

        em.add_field(name = "Mentionable:", value = f"`{role.mentionable}`", inline = False)
        em.add_field(name = "Is Default:", value = f"`{role.is_default()}`")
        em.add_field(name = "Bot Role:", value = f"`{role.is_bot_managed()}`", inline = True)

        em.add_field(name = "Color:", value = f"{role.color}", inline = False)
        em.add_field(name = "Created At:", value = f"{role.created_at}")
        em.add_field(name = "People with it:", value =f"{len(role.members)}", inline = True)

        em.set_footer(text = "invite me ;)", icon_url = ctx.author.avatar_url)
        em.set_thumbnail(url = str(ctx.guild.icon_url))
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        
        await ctx.send(embed = em)


def setup(client):
    client.add_cog(Information(client))