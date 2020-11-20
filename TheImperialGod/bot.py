"""
MIT LICENCE 2020 - 2021
All the code and the full bot is nothing but TheImperialGod
All the code is made by NightZan999, check him out at https://github.com/NightZan999
The deposit and withdraw command have been added on to by Makiyu-py, he used it in a fork

The repository the code has been taken from is at https://github.com/NightZan999/TheImperialGod
"""
import discord #discord object
import discord.ext #external
from discord.ext import commands #commands from external
from discord.ext.commands import has_role #has a role
from discord.ext.commands import has_permissions #permissions
from discord.ext.commands import MissingPermissions #the missing perms
from discord.ext.commands import BadArgument #incorrect arguments
from discord.ext.commands import CheckFailure #failure
import discord.utils
from discord.ext.commands.errors import MissingPermissions
from discord.ext.commands.errors import BadArgument
from discord.ext.commands.errors import CheckFailure
from discord.ext.commands import cooldown, BucketType
import random #random
#FOR GAWS
import datetime #date and time
import asyncio #asyncio needed!
from asyncio import sleep
#General Imports
import os
import math
import json
import traceback
#image manipulation
from PIL import Image
from io import BytesIO
# reddit
import praw

#constants
CLIENT_ID = 768695035092271124
BOT_TOKEN = ""
CLIENT_SECRET = "dOT7giQx_zJKPPbk3QLRQkl0QrGdSMgH"
INVITE_LINK = "https://discordapp.com/oauth2/authorize?&client_id=768695035092271124&scope=bot&permissions=21474836398"
PUBLIC_KEY = "cb1c82b5894134285d3313d67742d62d75e72149b9a7bab0bec4f29bd0b90292"
LINES_OF_CODE = 500
DATABASES = 'data/mainbank.json'
PACKAGING_DATA = "package.json"
BOT_PREFIX = "imp "
ZAN_ID = 575706831192719370

client = commands.Bot(command_prefix = "imp ", case_insensitive = True) #making a client object
reddit = praw.Reddit(
    client_id = 'NY_kPmfmJV1VAg',
    client_secret = "GNKjyvMHErF9yYqZGrhx6MxG55WtVw",
    username = "NightZan999",
    password = "python123_praw",
    user_agent = "python_praw"
)

@client.command()
async def ping(ctx):
    embed = discord.Embed(title = 'Pong', color = ctx.author.color)
    embed.add_field(name = "Ping:", value = f"`{random.randint(175, 300)} ms`")
    await ctx.send(embed = embed)

#when the bot gets ready
@client.event
async def on_ready():
    print("Ready!")
    print("Username: ", client.user.name)
    print("User ID: ", client.user.id)

#when an error occurs
@client.command()
async def invite(ctx):
    embed = discord.Embed(title = "Invite Link:", color = ctx.author.color)
    embed.add_field(name = "Here:", value = f"[Click me]({INVITE_LINK})")
    await ctx.send(embed = embed)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found!")
    if isinstance(error, commands.NoPrivateMessage):
        await ctx.author.send('This command cannot be used in private messages.')
    elif isinstance(error, commands.DisabledCommand):
        await ctx.author.send('Sorry. This command is disabled and cannot be used.')
    elif isinstance(error, commands.CommandInvokeError):
        pass

filtered_words = ['idiot', 'Idiots', "DIE", "ass", "butt", "Fool", "shit", "bitch"]

@client.event
async def on_message(msg):
    with open("data/automod.json", "r") as f:
        guilds = json.load(f)

    ctx = await client.get_context(msg)

    try:
        if guilds[str(ctx.guild.id)]["automod"] == "true":
            for word in filtered_words:
                if word in msg.content.lower():
                    warns = await read_json("data/warns.json")
                    await msg.delete()
    except:
        pass

    try:
        if msg.mentions[0] == client.user:
            await msg.channel.send(f"My prefix for this server is `imp`\nCheck out `imp help` for more information")
        elif client.user in msg.mentions:
            for i in range(0, len(msg.mentions)):
                if msg.mentions[i] == client.user:
                    await msg.channel.send(f"My prefix for this server is `imp`\nCheck out `imp help` for more information")
                    break
        else:
            pass
    except:
        pass


    await client.process_commands(msg)

@client.event
async def on_guild_join(guild):
    ctx = await client.get_context(guild)
    with open("data/guilds.json", "r") as f:
        guilds = json.load(f)

    if guild.name in guilds:
        print("Joined old server!")
    else:
        guilds[str(guild.name)] = {}
        guilds[str(guild.name)]["guild_id"] = guild.id
        print("Joined a new SERVER!")

    with open("data/guilds.json", "w") as f:
        json.dump(guilds, f)

#moderation commands
@client.command()
@commands.has_permissions(manage_roles = True)
async def addrole(ctx, member : discord.Member, role : int = None, *, reason = None):
    if role == None:
        await ctx.send("Sorry but you have to give a valid role id")
        return

    try:
        rol = ctx.guild.get_role(role)
    except:
        await ctx.send("Wrong role id!")
    else:
        await member.add_roles(rol)
        embed = discord.Embed(title = "Addrole!", color = ctx.author.color)
        embed.add_field(name = f'Moderator:', value = f"`{ctx.author.name}``")
        embed.add_field(name = "Reason:", value = f"`{reason}`")
        await ctx.send(embed = embed)

@addrole.error
async def addrole_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Bruh you really think you can use that!")
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(title = "Addrole Error", color = ctx.author.color, description = "An error occured")
        embed.add_field(name = "Correct Usage:", value = f"`imp addrole {ctx.author.mention} [role_id]`")
        await ctx.send(embed = embed)

@client.command()
@commands.has_permissions(manage_roles = True)
async def removerole(ctx, member : discord.Member, role : int, *, reason = None):
    try:
        rol = ctx.guild.get_role(role)
    except:
        await ctx.send("Wrong role id!")
    else:
        await member.remove_roles(rol)
        embed = discord.Embed(title = "Removerole!", color = ctx.author.color)
        embed.add_field(name = f'Moderator:', value = f"{ctx.author.name}")
        embed.add_field(name = "Reason:", value = reason)
        await ctx.send(embed = embed)

@removerole.error
async def removerole_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Bruh you really think you can use that!")
    if isinstance(error, commands.BadArgument):
        embed = discord.Embed(title = "Removerole Error", color = ctx.author.color, description = "An error occured")
        embed.add_field(name = "Correct Usage:", value = f"`imp removerole {ctx.author.mention} [role_id]`")
        await ctx.send(embed = embed)

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    embed = discord.Embed(title = f"{member.name} got kicked!", color = ctx.author.color)
    embed.add_field(name = f"Moderator:", value = f"`{ctx.author.name}`")
    embed.add_field(name = 'Reason', value = f"`{reason}`")
    await ctx.send(embed = embed)
    try:
        await member.send(f'You were kicked in {ctx.message.guild.name}\nBy: {ctx.author.name}')
    except:
        pass

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Bruh you really think you can use that!")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You have to provide a valid person to kick!")
        await ctx.send(f"Good usage:\n`imp kick `{ctx.author.mention}")
    if isinstance(error, commands.BadArgument):
        await ctx.send("You have to provide a valid person to kick!")
        await ctx.send(f"Good usage:\n`imp kick `{ctx.author.mention}")

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    embed = discord.Embed(title = f"{member.name} got banned!", color = ctx.author.color)
    embed.add_field(name = f"Moderator:", value = f"`{ctx.author.name}`")
    embed.add_field(name = 'Reason', value = f"`{reason}`")
    await ctx.send(embed = embed)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Bruh you really think you can use that!")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You have to provide a valid person to ban!")
        await ctx.send(f"Good usage:\n`imp ban `{ctx.author.mention}")

@client.command()
@commands.has_permissions(kick_members = True)
async def softban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await member.unban(reason = reason)
    embed = discord.Embed(title = f"{member.name} got softbanned!", color = ctx.author.color)
    embed.add_field(name = f"Moderator:", value = f"`{ctx.author.name}``")
    embed.add_field(name = 'Reason', value = f"`{reason}`")
    await ctx.send(embed = embed)
    try:
        await member.send(f"You got softbanned in {ctx.guild.name}\nReason: {reason}\nModerator: {ctx.author.name}")
    except:
        print("DMs off")

@softban.error
async def softban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Bruh you really think you can use that!")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You have to provide a valid person to softban!")
        await ctx.send(f"Good usage:\n`imp softban `{ctx.author.mention}")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You have to provide a valid person to kick!")
        await ctx.send(f"Good usage:\n`imp kick `{ctx.author.mention}")

@client.command(aliases = ["ub"])
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

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You have to provide a valid person to unban!")
        await ctx.send(f"Good usage:\n`imp unban `{ctx.author.mention}")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You really think you can use that?")
    if isinstance(error, commands.BadArgument):
        await ctx.send("You have to provide a valid person to kick!")
        await ctx.send(f"Good usage:\n`imp unban `{ctx.author.mention}")

@client.command(aliases = ["warn"])
@has_permissions(kick_members = True)
async def addwarn(ctx, member : discord.Member, *, reason = None):
    warns = await read_json("data/warns.json")

    if str(ctx.guild.id) not in warns:
        warns[str(ctx.guild.id)] = {}
    if str(member.id) not in warns[str(ctx.guild.id)]:
        warns[str(ctx.guild.id)][str(member.id)] = {}
        warns[str(ctx.guild.id)][str(member.id)]["warns"] = 1
    else:
        warns[str(ctx.guild.id)][str(member.id)]["warns"] += 1

    res = warns[str(ctx.guild.id)][str(member.id)]["warns"]

    embed = discord.Embed(title = f"{member.name} was warned!", color = ctx.author.color)
    embed.add_field(name = "Reason:", value = f"`{reason}`")
    embed.add_field(name = "Moderator:", value = f"`{ctx.author.name}`")
    embed.add_field(name = "Number of Warns:", value = f"`{res}`")
    await ctx.send(embed = embed)
    try:
        await member.send(f"You were warned in {ctx.guild.name}\nBy {ctx.author.name}\nFor {reason}")
    except:
        pass

@client.command()
async def checkwarns(ctx, member : discord.Member):
    warns = await read_json("data/warns.json")
    if str(ctx.guild.id) not in warns:
        res = 0
    if str(member.id) not in warns[str(ctx.guild.id)]:
        res = 0
    else:
        res = warns[str(ctx.guild.id)][str(member.id)]["warns"]

    embed = discord.Embed(title=  f"{member.name} has {res} warnings", color = ctx.author.color)
    await ctx.send(embed = embed)

@addwarn.error
async def warn_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Permissions missing!")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("You have to provide a valid person to warn!")
        await ctx.send(f"Good usage:\n`imp warn `{ctx.author.mention}")
    if isinstance(error, commands.BadArgument):
        await ctx.send("You have to provide a valid person to kick!")
        await ctx.send(f"Good usage:\n`imp warn `{ctx.author.mention}")


 #`Mute`, `Unmute`, `Hardmute`, `setmuterole`,
@client.command()
@commands.has_permissions(manage_channels = True)
async def lock(ctx,*, reason = None):
    await ctx.message.channel.set_permissions(ctx.guild.default_role, send_messages = False)
    embed = discord.Embed(title = "Channel Was Locked!", color = ctx.author.color)
    embed.add_field(name = "Moderator:", inline = True, value = f"`{ctx.author.name}`")
    embed.add_field(name = "Reason:", inline = True, value = f"`{reason}`")
    await ctx.send(embed = embed)

@lock.error
async def lock_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You really think you can use that?")

@client.command()
@commands.has_permissions(manage_channels = True)
async def unlock(ctx, *, reason = None):
    await ctx.message.channel.set_permissions(ctx.guild.default_role, send_messages = True)
    embed = discord.Embed(title = "Channel Was Unlocked!", color = ctx.author.color)
    embed.add_field(name = "Moderator:", inline = True, value = f"`{ctx.author.name}`")
    embed.add_field(name = "Reason:", inline = True, value = f"`{reason}`")
    await ctx.send(embed = embed)

@unlock.error
async def unlock_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You really think you can use that?")

@client.command(aliases = ["setslowmode", "slowmode", "setmsgdelay"])
@has_permissions(manage_messages = True)
async def setdelay(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")

@setdelay.error
async def setdelay_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the permissions to use this command!")

@client.command(aliases = ['clear', 'delete'])
@has_permissions(manage_messages = True)
async def purge(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)
    await ctx.send(f'Done purging {amount} messages')

@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Looks like you don't have the perms.")

@client.command()
async def guilds(ctx):
    if ctx.author.id != 575706831192719370:
        await ctx.send("Only for bot devs, sorry no sorry")
        return
    else:
        a = 0
        for guild in client.guilds:
            a += 1
            await ctx.author.send(f"{guild.name} : {guild.id}")

#balance command
@client.command(aliases = ["balance"])
async def bal(ctx, member : discord.Member = None):
    if member == None: #if they didnt mention a member
        member = ctx.author #make themselves the member

    await open_account(member) #see if the person has an account
    user = member
    users = await get_bank_data() #seeing the full data

    #in the open_account function everyone who doesn't have an account gets one!
    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    #creating an embed and showing the balance!
    embed = discord.Embed(title = f"{member.name}'s Balance", color = ctx.author.color)
    embed.add_field(name = "Wallet Balance", value = f"`{wallet_amt}`", inline = False)
    embed.add_field(name = "Bank Balance", value = f"`{bank_amt}`", inline = False)
    embed.add_field(name = "Total Balance", value = f"`{bank_amt + wallet_amt}`")
    await ctx.send(embed = embed)

@client.command()
@commands.cooldown(1, 15, commands.BucketType.user) #has a cooldown
async def beg(ctx):

    #same as last time!
    await open_account(ctx.author)
    users = await get_bank_data()
    user = ctx.author

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    #I deleted the halloween event
    list = ['money']
    reward_type = random.choice(list)
    if reward_type == "money":
        earnings = random.randint(0, 100)
        users[str(user.id)]["wallet"] += earnings

        #making sure the balance is saved
        with open("data/mainbank.json", "w") as f:
            json.dump(users, f)

        await ctx.send(f"Well you earned {earnings} coins")
@beg.error
async def beg_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title = "Slow it down C'mon!", color = ctx.author.color)
        embed.add_field(name = "Bruh", value = "Stop begging so much! It makes you look poor!")
        embed.add_field(name = "Try again in:", value = f"`{error.retry_after}`")
        await ctx.send(embed = embed)



@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
    await ctx.send("Great you claimed 20k coins")
    users = await get_bank_data()
    user = ctx.author
    await open_account(user)

    users[str(user.id)]["wallet"] += 20000

    with open("data/mainbank.json", "w") as f:
        json.dump(users, f)

@daily.error
async def daily_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title = "Slow it down C'mon!", color = ctx.author.color)
        embed.add_field(name = "Bruh", value = "Stop moneying so much! It makes you look poor!")
        embed.add_field(name = "Try again in:", value = f"`{error.retry_after}`")
        await ctx.send(embed = embed)

@client.command()
@commands.cooldown(1, 604800, commands.BucketType.user)
async def weekly(ctx):
    await ctx.send("Great you claimed 50k coins")
    users = await get_bank_data()
    user = ctx.author
    await open_account(user)

    users[str(user.id)]["wallet"] += 50000

    with open("data/mainbank.json", "w") as f:
        json.dump(users, f)

@client.command(aliases = ["with"])
async def withdraw(ctx, amount = None):
    #BTW for dep im not doing comments :-(
    await open_account(ctx.author) #opening their account
    if amount == None: #making sure they are withdrawing something!
        await ctx.send("Type an amount")

    amount = int(amount)
    bal = await update_bank(ctx.author)

    if amount == 'all':
        amount = bal[1]

    if amount > bal[1]:
        await ctx.send("You can't withdraw more than you have in your bank!")
        return
    if amount <= 0:
        await ctx.send("Amount must be positive!")

    await update_bank(ctx.author, amount)
    await update_bank(ctx.author, -1*amount, "bank")
    await ctx.send(f"You withdrew {amount} coins from your bank")

@client.command(aliases = ["dep"])
async def deposit(ctx, amount = None):
    await open_account(ctx.author)
    if amount == None:
        await ctx.send("Type an amount")

    amount = int(amount)
    bal = await update_bank(ctx.author)

    if amount == 'all':
        amount = bal[0]

    if amount > bal[0]:
        await ctx.send("You can't deposit more than you have in your wallet!")
        return
    if amount <= 0:
        await ctx.send("Amount must be positive!")

    await update_bank(ctx.author, -1*amount)
    await update_bank(ctx.author,amount, "bank")
    await ctx.send(f"You deposited {amount} coins from your wallet into your bank")

@client.command()
@commands.cooldown(1, 20, commands.BucketType.user) #I dont want alt spams
async def give(ctx, member : discord.Member, amount = None):
    await open_account(ctx.author) #open the givers account
    await open_account(member) #and the receivers
    if amount == None: #making sure hes giving something
        await ctx.send("Type an amount")

    amount = int(amount)
    bal = await update_bank(ctx.author)
    if amount > bal[0]:
        await ctx.send("You don't even have that much money, lol")
        return
    if amount <= 0:
        await ctx.send("Amount must be positive!")

    await update_bank(ctx.author, -1*amount, "wallet") #making sure they lose the coins they gave
    await update_bank(member,amount, "wallet") #making sure the other one receives
    await ctx.send(f"You give {amount} coins from your wallet to {member.name}'s wallet")

@give.error
async def give_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title = "Slow it down C'mon", color = ctx.author.color)
        embed.add_field(name = 'Stop giving', value = "Wanna make a company, try `imp createbiz`")
        embed.add_field(name = "Try again in:", value = f"`{error.retry_after}`")
        await ctx.send(embed)

@client.command()
@commands.cooldown(1, 10, commands.BucketType.user) #I dont want alt spams
async def slots(ctx, amount = None):
    if amount == None:
        await ctx.send("Type an amount")

    amount = int(amount)
    bal = await update_bank(ctx.author)

    if amount > bal[0]:
        await ctx.send("You can't pay more than you have in your wallet!")
        return
    if amount <= 0:
        await ctx.send("Amount must be positive!")

    final = []
    for i in range(0, 3):
        a = random.choice("🐸", "👾", "👻")
        final.append(a)

    await ctx.send(str(final))
    if final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
        if final[0] == final[1] and final[1] == final[2]:
            await update_bank(ctx.author, 5 * amount)
        else:
            await update_bank(ctx.author, 2 *amount)
    else:
        await update_bank(ctx.author, -1* amount)

@slots.error
async def slots_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title = "Slow it down C'mon", color = ctx.author.color)
        embed.add_field(name = 'Stop playing!', value = "You would only be more poor if you did")
        embed.add_field(name = "Try again in:", value = f"`{error.retry_after}`")
        await ctx.send(embed)

@client.command()
@commands.cooldown(1, 60, commands.BucketType.user) #this pays a lot thus cooldown
async def serve(ctx):
    await open_account(ctx.author)
    earnings = random.randint(1, 1000)
    await update_bank(ctx.author, earnings)
    await ctx.send(f'You served {ctx.author.guild.name} and got {earnings} coins out of it')

@serve.error
async def serve_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title = "Slow it down C'mon", color = ctx.author.color)
        embed.add_field(name = 'Stop Serving', value = "The money is high, thus the cooldown")
        embed.add_field(name = "Try again in:", value = f"`{error.retry_after}`")
        await ctx.send(embed)



@client.command()
@commands.cooldown(1, 1000, commands.BucketType.user)
async def bankrob(ctx, member : discord.Member):
    await open_account(ctx.author)
    await open_account(member)
    users = await get_bank_data()
    if users[str(user.id)]["wallet"] > 10000:
        a = random.randint(1, 100)
        if a < 20:
            earnings = random.randint(100, users[str(member.id)]["bank"])
            await ctx.send(f"You stole {earnings} coins from {member.mention}!")
            update_bank(ctx.author, earnings, "wallet")
            update_bank(member, -1*earnings, "bank")
        else:
            await ctx.send("Sorry you got caught!")
            update_bank(ctx.author, -10000, "wallet")
            update_bank(member, 10000, "bank")
    else:
        await ctx.send("You need 10,000 coin in your wallet to bankrob!")

@bankrob.error
async def bankrob_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title = "Slow it down C'mon", color = ctx.author.color)
        embed.add_field(name = "You need to plan your next attack", value = "If you try once more your next robbery will be a fail")
        embed.add_field(name = "Try again in:", value = f"`{error.retry_after}`")
        await ctx.send(embed = embed)

@client.command(aliases = ["lb"])
async def leaderboard(ctx,x = 1):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total,reverse=True)

    em = discord.Embed(title = f"Top {x} Richest People" , description = "This is decided on the basis of raw money in the bank and wallet",color = discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        name = member.name
        em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
        if index == x:
            break
        else:
            index += 1

    await ctx.send(embed = em)

@client.command()
async def devwith(ctx, amount): #had to make this!
    if ctx.author.id == 575706831192719370: #if the user is me!
        amount = int(amount)
        await open_account(ctx.author)
        user = ctx.author
        users = await get_bank_data()

        users[str(user.id)]["wallet"] += amount
        with open("data/mainbank.json", "w") as f:
            json.dump(users, f)

        await ctx.send(f"Gave you {amount} coins!")
    else: #else it should not give!
        await ctx.send("Bruh, your not a bot dev!")

#Helperfunctions
async def open_account(user):
    with open("data/mainbank.json", "r") as f:
        users = json.load(f)

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0 #I want them to get 100 coins
        users[str(user.id)]["bank"]  = 0

    with open("data/mainbank.json", "w") as f:
        json.dump(users, f)


async def get_bank_data():
    with open("data/mainbank.json", "r") as f:
        users = json.load(f)
    return users

async def update_bank(user, change = 0, mode = "wallet"):
    users = await get_bank_data()
    users[str(user.id)][mode] = users[str(user.id)][mode] + change

    with open("data/mainbank.json", "w") as f:
        json.dump(users, f)

    bal = users[str(user.id)]["wallet"], users[str(user.id)]["bank"]
    return bal

async def ch_pr(): #changing the bots status every 5 secs!!!
    await client.wait_until_ready()
    statuses = [
        f"Helping {len(client.guilds)} servers",
        "Making money!",
        "Hosting Giveaways",
        "imp gstart",
        "Kicking people!",
        "Using utils!",
        "Serving 256 users"
    ]
    while not client.is_closed():
        status = random.choice(statuses)

        await client.change_presence(activity = discord.Streaming(name = status, url = "https://twitch.tv/pewdiepie"))
        await asyncio.sleep(60)

    if client.is_closed():
        print("Offline again, f in the chat for the discord devs!")


#UTILITIES
@client.command()
async def coinflip(ctx):
    list = ["Heads", "Tails"]
    embed = discord.Embed(title = "Coinflip by {}".format(ctx.author.name), color = ctx.author.color)
    res = random.choice(list)
    embed.add_field(name = "We rolled a:", value = f"`{res}`")
    if res.lower() == "heads":
        embed.set_image(url = """
        data:image/jpeg;base64,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
        """
        )
    else:
        embed.set_image(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnWL81FKwiyIak8DR8azPVHryuOFNlS5esVw&usqp=CAU")
    await ctx.send(embed = embed)

@client.command(aliases = ['rn', 'random_n', 'random_int', 'randrange', 'randint', 'r_number'])
async def random_number(ctx, start, end):
    bool = True
    start = int(start)
    end = int(end)
    try:
    #because someone will be an idiot!
        if end > 9223372036854775807:
            await ctx.send(':warning: ending number too big!')
            bool = False
        if end <= start:
            await ctx.send(':warning: ending number must be larger than starting number!')
            bool = False
    except:
        pass
    if bool == True:
        embed = discord.Embed(title = "Random Number by {}".format(ctx.author.name), color = ctx.author.color)
        embed.add_field(name = "Number:", value = random.randint(start, end))
        await ctx.send(embed = embed)
    else:
        await ctx.send("Sorry, you were an idiot! Thus its not for you!")

@random_number.error
async def random_number_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title = "Missing Required Argument", color = ctx.author.color)
        embed.add_field(name = "Error:", value = "You have missed an argument")
        embed.add_field(name = "Correct usage:", value = "`imp random_number <first_range> <last_range>`")

@client.command(pass_context = True)
async def code(ctx, *, msg):
    await ctx.send("```" + msg.replace("`", "") +("```"))

@client.command()
async def guess(ctx, start, end, guess):
    async with ctx.channel.typing():
        bool = True
        start = int(start)
        end = int(end)
        try:
            if end > 10000000000:
                await ctx.send(':warning: ending number too big!')
                bool = False
            if end <= start:
                await ctx.send(':warning: ending number must be larger than starting number!')
                bool = False
        except:
            pass
        if bool == True:
            number = random.randint(start, end)
            embed = discord.Embed(title = "Guess Game by {}".format(ctx.author.name), color = ctx.author.color)
            embed.add_field(name = "Number:", value = number)
            if guess == number:
                embed.add_field(name = "You Won!", value = "The number was {} and your guess was {}".format(number, guess))
            else:
                embed.add_field(name = "You Lost!", value = "The number was {} and your guess was {}".format(number, guess))
            await ctx.send(embed = embed)
        else:
            await ctx.send("Sorry, you were an idiot! Thus its not for you!")

@guess.error
async def guess_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title = "Missing Required Argument", color = ctx.author.color)
        embed.add_field(name = "Error:", value = "You have missed an argument")
        embed.add_field(name = "Correct usage:", value = "`imp guess <first_range> <last_range> <guess>`")


@client.command(aliases = ['r', 'respecting', 'resp'])
async def respect(ctx, *, text = None):
    text = str(text)
    hearts = ['❤', '💛', '💚', '💙', '💜', '🧡', '🤎', '🖤']
    reason = f"for **{text}** " if text else ""
    embed = discord.Embed(title = "{} pays some respect!".format(ctx.author.name), color = ctx.author.color)
    embed.add_field(name = "Info:", value = f"**{ctx.author.name}** has paid their respect {reason}{random.choice(hearts)}")
    await ctx.send(embed = embed)

@respect.error
async def respect_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Type some text after the command!")

@client.command()
async def thank(ctx, member : discord.Member, *, reason = None):
    if reason == None:
        await ctx.send(f"{ctx.author.mention} thanked {member} for no reason at all!")
    else:
        await ctx.send(f"{ctx.author.mention} thanks {member} for {reason} reason.")
    try:
        if reason != None:
            await member.send(f"You were thanked in {ctx.guild.name} by {ctx.author.name}!\nReason: {reason}")
        else:
            await member.send(f"You were thanked in {ctx.guild.name} by {ctx.author.name}")
    except:
        pass

    user = member
    await givethanks(user)

@client.command()
async def checkthanks(ctx, member : discord.Member = None):
    if member == None:
        member = ctx.author

    with open("thanks.json", "r") as f:
        ty = json.load(f)

    if member.id in ty:
        thanks_user = ty[str(user.id)]["thanks"]
        await ctx.send(f"{member.mention} has {thanks_user} thanks!")
    else:
        await ctx.send("That user has never gotten any thanks!")

@client.command()
async def reverse(ctx,*,msg):
    try:
        msg = list(msg)
        msg.reverse()
        print(msg)
        send = ''.join(msg)
        await ctx.send(send)
    except Exception:
        traceback.print_exc()

@client.command()
async def eightball(ctx, *, question):
    responses = [
    'That is certain',
    'Of course',
    'My sources say yes',
    'Try again',
    'Bad internet try again',
    'No',
    'Never',
    'Always true',
    'My sources say no!'
    ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.command()
async def poll(ctx, *, message):
    embed = discord.Embed(title = f"{ctx.author.name}'s Poll", color = ctx.author.color)
    embed.add_field(name = f"{message}", value = "Share your thoughts about this topic")

    my_msg = await ctx.send(embed = embed)
    await my_msg.add_reaction("✅")
    await my_msg.add_reaction("❌")

@client.command(aliases = ['str', 'show_tp', 's_toprole'])
async def show_toprole(ctx, *, member: discord.Member=None):
    if member is None:
        member = ctx.author
        await ctx.send(f'The top role for {member.display_name} is {member.top_role.name}')
    else:
        await ctx.send(f'The top role for {member.display_name} is {member.top_role.name}')

@client.command(aliases = ['generator','password','passwordgenerator', 'passwordgen'])
async def _pass(ctx,amt : int = 8):
    try:
        nwpss = []
        lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z','!','@',
        '#','$','%','^','&','*','(',')','-','_','+','=','{',",",'}',']',
        '[',';',':','<','>','?','/','1','2','3','4','5','6','7','8','9','0'
        ,'`','~','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'
        ,'Q','R','S','T','U','V','W','X','Y','Z'] #all char
        for x in range(amt):
            newpass = random.choice(lst)
            nwpss.append(newpass)

        fnpss = ''.join(nwpss)
        await ctx.send(f'{ctx.author} attempting to send you the genereated password in dms.')
        await ctx.author.send(f'Password Generated: {fnpss}')
    except Exception as e:
        print(e)

@client.command()
@commands.has_permissions(manage_channels = True)
async def count(ctx, channel: discord.TextChannel = None):
    channel = channel or ctx.channel #or since sometimes people have it locked!
    messages = await channel.history(limit = None).flatten()
    count = len(messages)

    embed = discord.Embed(
    title="Total Messages",
    colour=ctx.author.color,
    description=f"There were {count} messages in {channel.mention}")

    await ctx.send(embed=embed)


@client.command()
async def mute(ctx, member : discord.Member, *, reason = None):
    muted_role = ctx.guild.get_role(770124762231603211) #mute role
    await member.add_roles(muted_role)
    await ctx.send("Successfully muted!")
    try:
        await member.send(f"You have been muted in {ctx.guild.name}\nBy {ctx.author.name}\nReason is {reason}")
    except Exception as e:
        print(f"{member.name} has DMs off Lord!")

@client.command()
async def unmute(ctx, member : discord.Member):
    muted_role = ctx.guild.get_role(768399478242803722) #put mute role id
    await member.remove_roles(muted_role)
    await ctx.send("Successfully unmuted")
    try:
        await member.send(f"You have been muted in {ctx.guild.name}\nBy {ctx.author.name}\nReason is {reason}")
    except Exception as e:
        print(f"{member.name} has DMs off Lord!")

@client.command()
async def support(ctx):
    await ctx.send("Please vote for the bot on top.gg\nLink: ")

#Hosting Giveaways
#function needed to convert time:
def convert(time):
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

#making the real command
@client.command(aliases = ['gstart', 'g_host', 'gawstart', 'giveawaystart', 'gcreate'])
@commands.has_guild_permissions(manage_channels = True, manage_roles = True, manage_messages = True)
async def giveaway(ctx):
    await ctx.send("Let's start with this giveaway! Answer these questions within 15 seconds!")

    questions = ["Which channel should it be hosted in?",
                "What should be the duration of the giveaway? (s|m|h|d)",
                "What is the prize of the giveaway?",
    ]

    answers = []

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    for i in questions:
        await ctx.send(i)

        try:
            msg = await client.wait_for('message', timeout=30.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('You didn\'t answer in time, please be quicker next time!')
            return
        else:
            answers.append(msg.content)
    try:
        c_id = int(answers[0][2:-1])
    except:
        await ctx.send(f"You didn't mention a channel properly. Do it like this {ctx.channel.mention} next time.")
        return

    channel = client.get_channel(c_id)
    time = convert(answers[1])

    if time == -1:
        await ctx.send(f"You didn't answer the time with a proper unit. Use (s|m|h|d) next time!")
        return
    elif time == -2:
        await ctx.send(f"The time must be an integer. Please enter an integer next time")
        return

    prize = answers[2]

    await ctx.send(f"The Giveaway will be in {channel.mention} and will last {answers[1]}!")


    embed = discord.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)
    embed.add_field(name = "Hosted by:", value = ctx.author.mention)
    embed.set_footer(text = f"Ends {answers[1]} from now!")

    my_msg = await channel.send(embed = embed)
    await my_msg.add_reaction("🎉")

    await asyncio.sleep(time)
    new_msg = await channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))
    try:
        winner = random.choice(users)
    except:
        await ctx.send("No-one entered the giveaway can't decide winner")
        return

    with open("data/automod.json", "r") as f:
        guilds = json.load(f)

@giveaway.error
async def giveaway_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title = "Giveaway failed!", color = ctx.author.color)
        embed.add_field(name = 'Reason:', value = "Some perms are missing")
        await ctx.send(embed = embed)

@client.command()
@commands.has_permissions(manage_channels = True)
async def announce(ctx, c_id : int, *, msg):
    channel = client.get_channel(c_id)
    embed = discord.Embed(title = "Announcement!", color = ctx.author.color)
    embed.add_field(name = "Announcement:", value = f"`{msg}`")
    embed.add_field(name = "Moderator:", value = f"`{ctx.autor.name}`")
    await channel.send(embed = embed)

@announce.error
async def announce_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title = "Announcement failed!", color = ctx.author.color)
        embed.add_field(name = 'Reason:', value = "Some perms are missing")
        await ctx.send(embed = embed)

@client.command()
@commands.has_permissions(manage_roles=  True)
async def reroll(ctx, channel : discord.TextChannel, id_ : int):
    try:
        new_msg = await channel.fetch_message(id_)
    except:
        await ctx.send("The id was entered incorrectly.")
        return

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)
    await channel.send(f"Congratulations! The new winner is {winner.mention}.!")


@reroll.error
async def reroll_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title = "Giveaway failed!", color = ctx.author.color)
        embed.add_field(name = 'Reason:', value = "Some perms are missing")
        await ctx.send(embed = embed)

@client.command(pass_context=True, aliases=['joi'])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild= ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    await voice.disconnect()

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await ctx.send(f"Joined {channel}")


@client.command(pass_context=True, aliases=['lea'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send(f"Left {channel}")
    else:
        await ctx.send("Don't think I am in a voice channel")

@client.command()
@commands.has_permissions(administrator = True)
async def enableautomod(ctx):
    with open("data/automod.json", "r") as f:
        guilds = json.load(f)

    if ctx.guild.id in guilds:
        guilds[str(ctx.guild.id)]["automod"] = "true"
    else:
        guilds[str(ctx.guild.id)] = {}
        guilds[str(ctx.guild.id)]["automod"] = "true"

    embed = discord.Embed(title = 'Change in Server Settings', color = ctx.author.color)
    embed.add_field(name = 'Automod:', value = "`Automod = True`")
    await ctx.send(embed = embed)

    with open("data/automod.json", "w") as f:
        json.dump(guilds, f)

@enableautomod.error
async def enableautomod_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Bruh you really think you can use that?")

@client.command()
@commands.has_permissions(administrator = True)
async def disableautomod(ctx):
    with open("data/automod.json", "r") as f:
        guilds = json.load(f)

    if ctx.guild.id in guilds:
        guilds[str(ctx.guild.id)]["automod"] = "false"
    else:
        guilds[str(ctx.guild.id)] = {}
        guilds[str(ctx.guild.id)]["automod"] = "false"

    embed = discord.Embed(title = 'Change in Server Settings', color = ctx.author.color)
    embed.add_field(name = 'Automod:', value = "`Automod = False`")
    await ctx.send(embed = embed)

    with open("data/automod.json", "w") as f:
        json.dump(guilds, f)

@client.command()
@commands.has_permissions(administrator = True)
async def checkautomod(ctx):
    with open("data/automod.json", "r") as f:
        guilds = json.load(f)

    if ctx.guild.id in guilds:
        if guilds[str(ctx.guild.id)]["automod"] == "true":
            embed = discord.Embed(title = "Automod Status", color = ctx.author.color)
            embed.add_field(name = "Status:", value = "`True`")

        if guilds[str(ctx.guild.id)]["automod"] == "false":
            embed = discord.Embed(title = "Automod Status", color = ctx.author.color)
            embed.add_field(name = "Status:", value = "`False`")

        await ctx.send(embed = embed)

@checkautomod.error
async def checkautomod_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You really think you can use that?")


@disableautomod.error
async def disableautomod_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Bruh you really think you can use that?")

@client.command()
async def dice(ctx, amount : int):
    user = ctx.author
    await open_account(ctx.author)

    if amount <= 499:
        await ctx.send("You can't bet less than 500 bucks!")
        return

    if amount > users[str(user.id)]["wallet"]:
        await ctx.send("Far out you do not have that much money!")
        return

    users = await get_bank_data()
    user_roll = random.randint(1, 6)
    comp_roll = random.randint(1, 6)

    await ctx.send(f"You rolled a {user_roll}\nI rolled a {comp_roll}")
    if user_roll > comp_roll:
        await ctx.send("You won! Congrats")
        await update_bank(ctx.author, amount, "wallet")
    elif user_roll < comp_roll:
        await ctx.send("Sorry but you lost!")
        await update_bank(ctx.author, -1*amount, "wallet")
    elif user_roll == comp_roll:
        await ctx.send("A tie! Not bad so you get your money back!")

@client.command()
async def botinfo(ctx):
    embed = discord.Embed(title = "Botinfo", color = ctx.author.color,
    description = "TheImperialGod, is an awesome customizable discord bot with awesome features. Check some information about the bot below!"
    )
    embed.add_field(name = "First went live on:", value = "1 / 10 / 2020")
    embed.add_field(name = "Started coding on:", value = "26 / 9 / 2020")
    embed.add_field(name = "Creator", value = "NightZan999#0194")
    embed.add_field(name = 'Hosting', value = "DanBot Hosting")
    embed.add_field(name = "Servers:", value = f'`{len(client.guilds)}`')
    embed.add_field(name = 'Customizable Settings:', value = "Automoderation and utilities!")
    try:
        embed.add_field(name = "Users:", value = f'`{len(client.users)}`')
    except:
        pass
    finally:
        embed.add_field(name = "Website:", value = "https://theimperialgod.herokuapp.com\nNOTE: not hosted yet!")
        embed.add_field(name = "Number of Commands:", value = f"`62` (including special owner commands)")
        embed.add_field(name = "**Tech:**", value = "```+ Library : discord.py\n+ Database : JSON\n+ Hosting Services : DanBot Hosting!\n```", inline = False)
        await ctx.send(embed = embed)

@client.command()
async def candy(ctx):
    await ctx.send("You want candy, take it!")
    await ctx.send(file = discord.File("assets/candy.jpg"))

@client.command()
async def leaveguild(ctx, guild_id : int):
    if ctx.author.id != ZAN_ID:
        await ctx.send("Only bot devs can use this command!")
        return

    guild = client.get_guild(guild_id)
    await guild.leave()
    embed = discord.Embed(title = "Imperial Bot leaves a guild", color = ctx.author.color)
    embed.add_field(name = f"Guild:", value = f"`{guild.name}`")
    await ctx.send(embed = embed)


#advanced ecenomy
mainshop = [{"name":"Watch","price":100,"description":"Time"},
            {"name":"Laptop","price":1000,"description":"Work"},
            {"name":"PC","price":10000,"description":"Gaming"}]


@client.command()
async def shop(ctx):
    em = discord.Embed(title = "Shop", color = ctx.author.color)

    for item in mainshop:
        name = item["name"]
        price = item["price"]
        desc = item["description"]
        em.add_field(name = name, value = f"${price} | {desc}", inline = False)

    await ctx.send(embed = em)

@client.command()
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
            return


    await ctx.send(f"You just bought {amount} {item}")

@client.command()
async def wanted(ctx, user : discord.Member = None):
    if user == None:
        user = ctx.author

    wanted = Image.open("assets/wanted.jpg")
    asset = user.avatar_url_as(size = 128)

    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((88, 88))
    wanted.paste(pfp, (47, 84))

    wanted.save("assets/profile.jpg")
    await ctx.send(file = discord.File("assets/profile.jpg"))

@client.command(aliases = ['inv', 'inventory'])
async def bag(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []


    em = discord.Embed(title = "Inventory", color = ctx.author.color)
    for item in bag:
        name = item["item"]
        amount = item["amount"]

        em.add_field(name = name, value = amount)

    await ctx.send(embed = em)

async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False, 1]

    cost = price*amount
    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break

            index += 1

        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]

    with open("data/mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")
    return [True,"Worked"]


@client.command(aliases = ["postvid"])
@cooldown(1, 30, BucketType.user)
async def postvideo(ctx):
    users = await get_bank_data()
    a = await check_for_item(ctx.author, "pc")

    if not a:
        await ctx.send("You don't have a PC to post a video!")
        return
    
    views = random.randint(500, 2000)
    earnings = views * random.randint(1, 5)

    await ctx.send(f"The video got {views} views\nAs a result with the ads you made {earnings} coins!")
    await update_bank(ctx.author, earnings)

async def check_for_item(user, item_name):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            break

    if name_ == None:
        return False
    users = await get_bank_data()
    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                return True
                break

        if t == None:
            return False
    except:
        return False


@client.command()
async def sell(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await sell_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            await ctx.send("That Object isn't there!")
            return
        if res[1]==2:
            await ctx.send(f"You don't have {amount} {item} in your bag.")
            return
        if res[1]==3:
            await ctx.send(f"You don't have {item} in your bag.")
            return

    await ctx.send(f"You just sold {amount} {item}.")

async def sell_this(user,item_name,amount,price = None):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            if price==None:
                price = 0.9 * item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt - amount
                if new_amt < 0:
                    return [False,2]
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1
        if t == None:
            return [False,3]
    except:
        return [False,3]

    with open("data/mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]

#Math Commands
@client.command()
async def add(ctx, num1 : int, num2 : int):
    await ctx.send(f"Sum of the numbers is: `{num1 + num2}`")

#Math Commands
@client.command()
async def subtract(ctx, num1 : int, num2 : int):
    await ctx.send(f"Difference of the numbers is: `{num1 - num2}`")

@client.command()
async def multiply(ctx, num1 : int, num2 : int):
    await ctx.send(f"Product of the numbers is: `{num1 * num2}`")

@client.command()
async def divide(ctx, num1 : int, num2 : int):
    await ctx.send(f"Quotient is: `{num1 / num2}`")

@client.command()
async def sqrt(ctx, num : int):
    for i in range(0, num, 0.0001):
        if i * i == num:
            await ctx.send(f"The square root of {num} is {i}")

@client.command()
async def square(ctx, num : int):
    await ctx.send(f"`{num * num}`")

@client.command()
async def power(ctx, num1 : int, num2 : int):
    await ctx.send(f"The power of that I think is {math.pow(num1, num2)}")

@client.command()
async def dog(ctx):
    subreddit = reddit.subreddit("dog")
    top = subreddit.top(limit = 100)

    all_subs = []
    for submission in top:
        all_subs.append(submission)

    sub = random.choice(all_subs)
    embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
    embed.set_image(url = sub.url)
    await ctx.send(embed = embed)

@client.command()
async def cat(ctx):
    subreddit = reddit.subreddit("cat")
    top = subreddit.top(limit = 100)

    all_subs = []
    for submission in top:
        all_subs.append(submission)

    sub = random.choice(all_subs)
    embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
    embed.set_image(url = sub.url)
    await ctx.send(embed = embed)

@client.command()
async def duck(ctx):
    subreddit = reddit.subreddit("duck")
    top = subreddit.top(limit = 100)

    all_subs = []
    for submission in top:
        all_subs.append(submission)

    sub = random.choice(all_subs)
    embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
    embed.set_image(url = sub.url)
    await ctx.send(embed = embed)

@client.command()
async def fox(ctx):
    subreddit = reddit.subreddit("fox")
    top = subreddit.top(limit = 100)

    all_subs = []
    for submission in top:
        all_subs.append(submission)

    sub = random.choice(all_subs)
    embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
    embed.set_image(url = sub.url)
    await ctx.send(embed = embed)

@client.command()
async def panda(ctx):
    subreddit = reddit.subreddit("panda")
    top = subreddit.top(limit = 100)

    all_subs = []
    for submission in top:
        all_subs.append(submission)

    sub = random.choice(all_subs)
    embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
    embed.set_image(url = sub.url)
    await ctx.send(embed = embed)

@client.command()
async def koala(ctx):
    subreddit = reddit.subreddit("koala")
    top = subreddit.top(limit = 100)

    all_subs = []
    for submission in top:
        all_subs.append(submission)

    sub = random.choice(all_subs)
    embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
    embed.set_image(url = sub.url)
    await ctx.send(embed = embed)

menu = ['pizza', "pasta", "fries", "chips", "nachos", "hotdogs", "burgers",
"steak", "cheese", "Salad", "Chicken", "pancakes", "waffles"
]

@client.command()
@cooldown(1, 3, BucketType.user)
async def order(ctx, food = None):
    if food == None:
        await ctx.send("You have to mention some food!")
        return

    foodExists = False
    for item in menu:
        if item.lower() == food.lower():
            foodExists = True

    if foodExists == False:
        await ctx.send("Not valid food!")
        return

    users = await get_bank_data()
    await open_account(ctx.author)
    bal = await update_bank(ctx.author)

    if users[str(user.id)]["wallet"] < 500:
        await ctx.send("You need 500 coins to eat")
        return

    await ctx.send("The order has been sent to the kitchen")
    await update_bank(ctx.author, -500, "wallet")

    #searching for the food on reddit
    subreddit = reddit.subreddit(food)
    top = subreddit.top(limit = 10)

    all_subs = []
    for submission in top:
        all_subs.append(submission)

    sub = random.choice(all_subs)
    embed = discord.Embed(title = f"{sub.title}", color = ctx.author.color)
    embed.set_image(url = sub.url)

    await asyncio.sleep(5)
    await ctx.send(embed = embed)

@client.command()
async def whois(ctx, member : discord.Member = None):
    if member == None:
        member = ctx.author
    em = discord.Embed(title = member.name, color = member.color)
    em.add_field(name = "ID:", value = member.id)
    em.set_thumbnail(url = member.avatar_url)
    await ctx.send(embed = em)


async def read_json(filename):
    with open(filename, "r") as f:
        res = json.load(f)

    return res

@client.command()
async def osay(ctx, *, args : str):
    embed = discord.Embed(title=  f"Osay by {ctx.author.name}", color = ctx.author.color)
    embed.add_field(name = "Message:", value = f"`{args}`")
    await ctx.send(embed = embed)


@client.command()
@commands.cooldown(1, 180, commands.BucketType.user) #I dont want alt spams
async def rob(ctx, member : discord.Member):
    await open_account(ctx.author) #open the givers account
    await open_account(member) #and the receivers

    bal = await update_bank(member)

    if bal[0] < 500:
        await ctx.send("Not worth it, the victim has less than 500 coins")
        return

    if users[str(ctx.author.id)]["wallet"] < 1000:
        await ctx.send("You need 1000 coins to rob someone")
        return

    a = random.randint(0, bal[0])

    await ctx.send(f"You robbed {member.mention} and stole {a} coins from them!")
    await update_bank(ctx.author, a)
    await update_bank(member, -1*a)
    
@rob.error
async def rob_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed(title = "Slow it down C'mon", color = ctx.author.color)
        embed.add_field(name = 'Stop robbing', value = "Bruh, your a Tusken Raider. Stop robbing so much")
        embed.add_field(name = "Try again in:", value = f"`{error.retry_after}`")
        await ctx.send(embed)


@client.command()
async def load(ctx, extension):
    if ZAN_ID != ctx.author.id:
        await ctx.send("Only for bot devs")
        return
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    if ZAN_ID != ctx.author.id:
        await ctx.send("Only for bot devs")
        return
    client.unload_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

'''
Some fun data about this code:
1 Line of Code = 26/09/2020
50 Lines of Code = 27/09/2020
100 Lines of Code = 29/09/2020
250 Lines of Code = 30/09/2020
500 Lines of Code = 07/10/2020
1000 Lines of Code = 19/10/2020
1500 Lines of Code = 05/11/2020
2000 Lines of Code = 11/11/2020
5000 Lines of Code =
'''

client.loop.create_task(ch_pr())
client.run(BOT_TOKEN)
