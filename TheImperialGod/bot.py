"""
MIT LICENCE 2020 - 2021
All the code and the full bot is nothing but TheImperialGod
All the code is made by NightZan999, check him out at https://github.com/NightZan999


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
from discord.utils import get #get
from discord.ext.commands.errors import MissingPermissions
from discord.ext.commands.errors import BadArgument
from discord.ext.commands.errors import CheckFailure
import random #random
from random import randint #random number
from random import randrange #random number in range
from random import choice #random choice from a list
from random import shuffle #shuffling a list
#FOR GAWS
import datetime #date and time
import asyncio #asyncio needed!
from asyncio import sleep
#General Imports
import os
import math
from math import pow
from math import sqrt
from math import e
import json
from json import dump
from json import load
import traceback
#image manipulation
from PIL import Image
from io import BytesIO
import praw

reddit = praw.Reddit(client_id = "e9i9IueslHQ7HA",
    client_secret = "lQA_L-C19Em7h2MPR8CVNuK3gd6-Xw",
    username = "Foreign_Demand_5496",
    user_agent = "pythonpraw128982"    
)

#constants
CLIENT_ID = 768695035092271124 
BOT_TOKEN = "" #MY TOKEN IS MINE!!!
CLIENT_SECRET = "dOT7giQx_zJKPPbk3QLRQkl0QrGdSMgH"
INVITE_LINK = "https://discordapp.com/oauth2/authorize?&client_id=768695035092271124&scope=bot&permissions=21474836398"
PUBLIC_KEY = "cb1c82b5894134285d3313d67742d62d75e72149b9a7bab0bec4f29bd0b90292"
LINES_OF_CODE = 500
DATABASES = 'mainbank.json'
PACKAGING_DATA = "package.json"
BOT_PREFIX = "imp "
ZAN_ID = 575706831192719370

client = commands.Bot(command_prefix = "imp ", case_insensitive = True) #making a client object

def load_json(filename):
    with open(filename, "r") as infile:
        return json.load(infile)


def write_json(filename, contents):
    with open(filename, 'w') as outfile:
        json.dump(contents, outfile, ensure_ascii=True, indent=4)

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
    await ctx.send("The invite link:\nhttps://discordapp.com/oauth2/authorize?&client_id=768695035092271124&scope=bot&permissions=2147483383")
    await ctx.send("My other friend in botland, a moderation only bot. Invite him here:\nhttps://discordapp.com/oauth2/authorize?&client_id=774607493031657523&scope=bot&permissions=21474836398")

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
    with open("automod.json", "r") as f:
        guilds = json.load(f)

    ctx = await client.get_context(msg)
    try:
        if guilds[str(ctx.guild.id)]["automod"] == "true":
            for word in filtered_words:
                if word in msg.content:
                    await msg.delete()
        try:
            if msg.mentions[0] == client.user:
                await msg.channel.send(f"My prefix for this server is `imp`\nCheck out `imp help` for more information")
            elif client.user in msg.mentions:
                for i in range(0, len(msg.mentions)):
                    if msg.mentions[i] == client.user:
                        await ctx.send("Hello there, I think I was pinged!")
                        break   
            else:
                pass                   
        except:
            pass
    except:
        pass
    
    await client.process_commands(msg)            

@client.event
async def on_guild_join(guild):
    ctx = await client.get_context(guild)
    with open("guilds.json", "r") as f:
        guilds = json.load(f)
    
    if guild.name in guilds:
        print("Joined old server!")
    else:
        guilds[str(guild.name)] = {}
        guilds[str(guild.name)]["guild_id"] = guild.id
        print("Joined a new SERVER!")

    with open("guilds.json", "w") as f:
        json.dump(guilds, f)

@client.remove_command('help')
@client.command()
async def help(ctx, command = None):
    prefix = "imp "
    utils_commands = [
    'Coinflip',
    'Random_Number',
    'Code',
    'Guess',
    'respect',
    'Poll',
    'Thank',
    'Reverse',
    'eightball',
    'fight',
    'whois',
    'wanted'
    ]
    gaws_commands = [
        'gstart',
        'reroll'
        ]
    misc_commands = [
        'invite',
        'show_toprole',
        'botinfo',
        'serverinfo',
        'channelinfo',
        'userinfo',
        'avatar',
        'candy',
        "hypesquad"
        ]
    owner_commands = [
            'enableautomod',
            "disableautomod",
            "checkautomod",
            "addwinnerrole",
            "removewinnerrole"
    ]
    economy_commands = [
    "Withdraw",
    "Balance",
    "Deposit",
    "Slots"
    'Rob',
    'Dice',
    'Leaderboard',
    'Daily',
    'Weekly'
    ]
    if command == None:
        embed = discord.Embed(title = "Help", color = ctx.author.color, description = "Type `imp help` and then a command or category for more information for even more information!")
        embed.add_field(name = f":coin: Economy Commands: [{len(economy_commands)}]", value = "`Balance`, `Beg`, `Serve`, `Withdraw`, `Deposit`, `Slots`, `Rob`, `Dice`, `Leaderboard`, `Daily`, `Weekly` ")
        embed.add_field(name = f"<:moderation:761292265049686057> Moderation Commands: [13]", value = "`Kick`, `Ban`, `Softban`, `Warn`, `Purge`, `Lock`, `Unlock`, `Mute`, `Unmute`, `Unban`, `Addrole`, `Delrole`, `Announce`")
        embed.add_field(name = f":tools: Utilities: [{len(utils_commands)}]", value = "`Coinflip`, `Random_Number`, `code`, `guess`, `respect`, `poll`, `thank`, `reverse`, `eightball`, `fight`, `wanted`")
        embed.add_field(name = f":gift: Giveaways: [{len(gaws_commands)}]", value = "`gstart`, `reroll`")
        embed.add_field(name = f":question: Misc: [{len(misc_commands)}]", value = "`invite`, `DM`, `show_toprole`, `botinfo`, `serverinfo`, `userinfo`, `channelinfo`, `avatar`, `candy`, `hypesquad`")
        embed.add_field(name = f"<:owner:761302143331205131> Owner: [{len(owner_commands)}]", value = "`enableautomod`, `disableautomod`, `checkautomod`, `addwinnerrole`")
        embed.set_footer(text = f"My prefix is {BOT_PREFIX}")
        await ctx.send(embed = embed)

    else:
        command = command.lower()
        if command == "eco" or command == "economy":
            embed = discord.Embed(title = "Help Economy:", color = ctx.author.color)
            embed.add_field(name = "Balance", value = "Use this to check your balance")
            embed.add_field(name = "Beg", value = "Use this to beg and earn some money!")
            embed.add_field(name = "Serve", value = "Use this command to serve the  and make money!")
            embed.add_field(name = "Withdraw", value = "Use this to withdraw coins from the bank")
            embed.add_field(name = "Deposit", value = "Use this to deposit coins from the wallet")
            embed.add_field(name = "Slots", value = "Use this to play some slots")
            embed.add_field(name = "Rob", value = "Use this to rob someones wallet")
            embed.add_field(name = "Dice", value = "User this to roll a dice")
            embed.add_field(name = "Leaderboard", value = "Use this to see who is the richest in town!")
            embed.add_field(name = 'Shop', value = "Shows you what you can buy!")
            embed.add_field(name = 'Buy', value = "Buy an interesting item!")
            embed.add_field(name = 'Sell', value = "Sell any useless items you have!")
            em = await ctx.send(embed = embed)
            await em.add_reaction('💰')
        
        elif command == "mod" or command == "moderation":
            em = discord.Embed(title = "Help Moderation:", color = ctx.author.color)
            em.add_field(name = "Kick", value = "Kicks a user, with mentions")
            em.add_field(name = "Ban", value = "Bans a user, with mentions")
            em.add_field(name = "Warn", value = "Warns a user!")
            em.add_field(name = "Purge", value = "Deletes plenty of messages")
            em.add_field(name = "Lock", value = "Makes sure no-one other than mods can type in a channel!")
            em.add_field(name = "Unlock", value = "Unlocks a locked channel")
            em.add_field(name = "Addrole", value = "Simply gives a role to someone, uses role id!")
            em.add_field(name = "Removerole", value = "Removes a role from someone, uses role id!")
            em.add_field(name = "Announce", value = "Make an announcement with the bot! Uses channel id")
            msg = await ctx.send(embed = em)
            await msg.add_reaction("🗡")
            await msg.add_reaction("🛠")

        elif command == "utilities" or command == "utils":
            em = discord.Embed(title = "Help Utils:", color = ctx.author.color)
            em.add_field(name = "Coinflip", value = "Flips a coin")
            em.add_field(name = "Random Number", value = "Gives a random number in a range")
            em.add_field(name = "Code", value = "Turns a message into code")
            em.add_field(name = "Guess", value = "Selects a random number in a range and plays a guess game!")
            em.add_field(name = "Respect", value = "Shows your respect for anything")
            em.add_field(name = "Poll", value = "Creates a poll")
            em.add_field(name = "Thank", value = "Thanks someone for something")
            em.add_field(name = "Reverse", value = "Reverses a message")
            em.add_field(name = "Eightball", value = "Classic Eightball")
            em.add_field(name = "Fight", value = "Fight someone with lightsabers!")
            em.add_field(name = "Wanted", value = "Can't spoil the fun try it yourself!")
            msg = await ctx.send(embed = em)
            await msg.add_reaction("🍩") 


        elif command == "gaws" or command == "gaw" or command == "giveaways":
            em = discord.Embed(title = "Help Giveaways:", color = ctx.author.color)
            em.add_field(name = "gstart", value = "Starts a giveaway")
            em.add_field(name = "reroll", value = "Rerolls a giveaway")
            msg = await ctx.send(embed = em)
            await msg.add_reaction("🎉")
        
        elif command == "misc" or command == "miscellaneous":
            em = discord.Embed(title = "Help Misc:", color = ctx.author.color)
            em.add_field(name = "invite", value = "Get a link to invite the bot to your s")
            em.add_field(name = "show_toprole", value = "Shows the top role of a person")
            em.add_field(name = "passwordgenerator", value = "DMs you a random password, you can also specify how many letters!")
            em.add_field(name = "botinfo", value = "Shows general information about the Bot!")
            em.add_field(name = "serverinfo", value = "Shows you information about your server!")
            em.add_field(name = "userinfo", value = "Shows you information about a user")
            em.add_field(name = "channelinfo", value = "Shows you information about a channel!")
            em.add_field(name = "avatar", value = "Shows you an avatar of a person")
            em.add_field(name = "hypesquad", value = "Shows you the true story of hypesquad.")
            msg = await ctx.send(embed = em)
            await msg.add_reaction("🐬")

        elif command == "owner":
            embed = discord.Embed(title = "Help Owner:", color = ctx.author.color)
            embed.add_field(name = "enableautomod", value = "Enables automod for the server, if anyone types a bad word. It deletes")
            embed.add_field(name = "disableautomod", value = "Disable automoderation for the entire server!")
            embed.add_field(name = "checkautomod", value = "Tells you automod status")
            msg = await ctx.send(embed = embed)
            await msg.add_reaction("🐯") 
        
        elif command == "balance" or command == "bal":
            embed = discord.Embed(title = "Help on Balance", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Shows the balance of a user. You have to mention someone or if you leave it blank it shows you your balance!", inline = False)
            embed.add_field(name = "Correct usage", value = f"`imp bal {ctx.author.mention}`")
            await ctx.send(embed = embed)

        elif command == "beg":
            embed = discord.Embed(title = "Help on Beg", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Beg for money on the road, you probably will make something!", inline = False)
            embed.add_field(name = "Correct usage", value = f"`imp bal {ctx.author.mention}`")
            await ctx.send(embed = embed)
        
        elif command == "serve":
            embed = discord.Embed(title = "Help on Serve", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Serve your server and make huge counts of money!", inline = False)
            embed.add_field(name = "Correct usage", value = f"`imp bal {ctx.author.mention}`")
            await ctx.send(embed = embed)
        
        elif command == "kick":
            embed = discord.Embed(title = "Help on Kick", color = ctx.author.color)
            embed.add_field(name = "Requirements - Permissions:", value = f"`Kick Members`")
            embed.add_field(name = "Correct usage", value = f"`imp kick {ctx.author.mention} [reason]`")
            await ctx.send(embed = embed)
        
        elif command == "ban":
            embed = discord.Embed(title = "Help on Ban", color = ctx.author.color)
            embed.add_field(name = "Requirements - Permissions:", value = f"`Ban Members`")
            embed.add_field(name = "Correct usage", value = f"`imp ban {ctx.author.mention} [reason]`")
            await ctx.send(embed = embed)

        elif command == "softban":
            embed = discord.Embed(title = "Help on Softban", color = ctx.author.color)
            embed.add_field(name = "Requirements - Permissions:", value = f"`Kick Members`")
            embed.add_field(name = "Correct usage", value = f"`imp softban {ctx.author.mention} [reason]`")
            await ctx.send(embed = embed)

        elif command == "addrole":
            embed = discord.Embed(title = "Help on Addrole", color = ctx.author.color)
            embed.add_field(name = "Requirements - Permissions:", value = f"`Manage Roles`")
            embed.add_field(name = "Correct usage", value = f"`imp addrole {ctx.author.mention} <role_id>`")
            await ctx.send(embed = embed)

        elif command == "removerole":
            embed = discord.Embed(title = "Help on Removerole", color = ctx.author.color)
            embed.add_field(name = "Requirements - Permissions:", value = f"`Manage Roles`")
            embed.add_field(name = "Correct usage", value = f"`imp removerole {ctx.author.mention} <role_id>`")
            await ctx.send(embed = embed)
        
        elif command == "warn":
            embed = discord.Embed(title = "Help on Warn", color = ctx.author.color)
            embed.add_field(name = "Requirements - Permissions:", value = f"`Kick Members`")
            embed.add_field(name = "Correct usage", value = f"`imp warn {ctx.author.mention} [reason]`")
            await ctx.send(embed = embed)

        elif command == "purge":
            embed = discord.Embed(title = "Help on Purge", color = ctx.author.color)
            embed.add_field(name = "Requirements - Permissions:", value = f"`Manage Messages`")
            embed.add_field(name = "Correct usage", value = f"`imp purge <message_count>`")
            await ctx.send(embed = embed)

        elif command == "count":
            embed = discord.Embed(title = "Help on Count", color = ctx.author.color)
            embed.add_field(name = "Requirements - Permissions:", value = f"`Manage Channels`")
            embed.add_field(name = "Correct usage", value = f"`imp count {channel.mention}")
            await ctx.send(embed = embed)
        
        elif command == "lock":
            embed = discord.Embed(title = "Help on Lock", color = ctx.author.color)
            embed.add_field(name = "Requirements - Permissions:", value = f"`Manage Channels`")
            embed.add_field(name = "Correct usage", value = f"`imp lock [reason]")
            await ctx.send(embed = embed)

        elif command == "unlock":
            embed = discord.Embed(title = "Help on Unlock", color = ctx.author.color)
            embed.add_field(name = "Requirements - Permissions:", value = f"`Manage Channels`")
            embed.add_field(name = "Correct usage", value = f"`imp unlock [reason]")
            await ctx.send(embed = embed)
        
        elif command == "setdelay":
            embed = discord.Embed(title = "Help on Setdelay", color = ctx.author.color)
            embed.add_field(name = "Requirements - Permissions:", value = f"`Manage Messages`")
            embed.add_field(name = "Correct usage", value = f"`imp setdelay <secs>")
            await ctx.send(embed = embed)

        elif command == "unban":
            embed = discord.Embed(title = "Help on Unban", color = ctx.author.color)
            embed.add_field(name = "Requirements - Permissions:", value = f"`Ban Members`")
            embed.add_field(name = "Correct usage", value = f"`imp unban {ctx.author.mention}")
            await ctx.send(embed = embed)
        
        elif command == "with" or command == "withdraw":
            embed = discord.Embed(title = "Help Withdraw:", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Withdraw money from your bank!")
            embed.add_field(name = "Correct Usage:", value = "`imp with <money>`")
            await ctx.send(embed = embed)    

        elif command == "dep" or command == "deposit":
            embed = discord.Embed(title = "Help Deposit:", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Put money into your bank")
            embed.add_field(name = "Correct Usage:", value = "`imp dep <money>`")
            await ctx.send(embed = embed)

        elif command == "slots":
            embed = discord.Embed(title = "Help Slots:", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Spend your money on an arcade game")
            embed.add_field(name = "Correct Usage:", value = "`imp slots <money>`")
            await ctx.send(embed = embed)

        elif command == "steal" or command == "rob":
            embed = discord.Embed(title = "Help Rob:", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "You can try to rob someone's wallet")
            embed.add_field(name = "Correct Usage:", value = "`imp rob <user>`")
            await ctx.send(embed = embed)
        
        elif command == "dice":
            embed = discord.Embed(title = "Help Dice:", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "This time another arcade game, only simpler")
            embed.add_field(name = "Correct Usage:", value = "`imp dice <money>`")
            await ctx.send(embed = embed)
        
        elif command == "leaderboard" or command == "lb":
            embed = discord.Embed(title = "Help Leaderboard:", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "See the richest guys in town!")
            embed.add_field(name = "Correct Usage:", value = "`imp leaderboard <top_richest_people>`")
            await ctx.send(embed = embed)

        elif command == "daily":
            embed = discord.Embed(title = "Help Daily:", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Claim your daily coins!")
            embed.add_field(name = "Correct Usage:", value = "`imp daily`")
            await ctx.send(embed = embed)

        elif command == "weekly":
            embed = discord.Embed(title = "Help Weekly:", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Claim your weekly coins!")
            embed.add_field(name = "Correct Usage:", value = "`imp weekly`")
            await ctx.send(embed = embed)
        
        elif command == "buy":
            embed = discord.Embed(title = "Help Buy:", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Buy an item!")
            embed.add_field(name = "Correct Usage:", value = "`imp buy [item]`")
            await ctx.send(embed = embed)
        
        elif command == "sell":
            embed = discord.Embed(title = "Help Sell:", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Sell an item that you have for 90 percent of its cost!")
            embed.add_field(name = "Correct Usage:", value = "`imp sell [item]`")
            await ctx.send(embed = embed)
        
        elif command == "shop":
            embed = discord.Embed(title = "Help Shop:", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "See what's avalible to buy")
            embed.add_field(name = "Correct Usage:", value = "`imp shop`")
            await ctx.send(embed = embed)
        
        elif command == "coinflip":
            embed = discord.Embed(title=  "Help Coinflip", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Flip a coin!")
            embed.add_field(name = 'Correct Usage:', value = "`imp coinflip`")
            await ctx.send(embed = embed)

        elif command == "random_number" or command == "rn":
            embed = discord.Embed(title=  "Help Random Number", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Returns a random number in a range!")
            embed.add_field(name = 'Correct Usage:', value = "`imp random_number [start_range] [end_range]`")
            await ctx.send(embed = embed)

        elif command == "code":
            embed = discord.Embed(title=  "Help Code", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Shapes a message into code")
            embed.add_field(name = 'Correct Usage:', value = "`imp code [message]`")
            await ctx.send(embed = embed)

        elif command == "respect":
            embed = discord.Embed(title=  "Help Respect", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Show your respect for something")
            embed.add_field(name = 'Correct Usage:', value = "`imp respect [message]`")
            await ctx.send(embed = embed)

        elif command == "poll":
            embed = discord.Embed(title=  "Help Poll", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Creates a poll for you")
            embed.add_field(name = 'Correct Usage:', value = "`imp poll [message]`")
            await ctx.send(embed = embed)
        
        elif command == "thank":
            embed = discord.Embed(title=  "Help Thank", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Show your gratitude towards a user")
            embed.add_field(name = 'Correct Usage:', value = "`imp thank [user] [reason]`")
            await ctx.send(embed = embed)
        
        elif command == "reverse":
            embed = discord.Embed(title=  "Help Reverse", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Reverses a message!")
            embed.add_field(name = 'Correct Usage:', value = "`imp reverse [message]`")
            await ctx.send(embed = embed)
        
        elif command == "eightball":
            embed = discord.Embed(title=  "Help Eightball", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Classic eightball, predicts the future!")
            embed.add_field(name = 'Correct Usage:', value = "`imp eightball [future]`")
            await ctx.send(embed = embed)
        
        elif command == "wanted":
            embed = discord.Embed(title=  "Help Wanted", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Can't spoil the fun!")
            embed.add_field(name = 'Correct Usage:', value = "`imp wanted [user]`")
            await ctx.send(embed = embed)
        
        elif command == "guess":
            embed = discord.Embed(title=  "Help Guess", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Try to guess a number")
            embed.add_field(name = 'Correct Usage:', value = "`imp guess [start_range] [end_range] [guess]`")
            await ctx.send(embed = embed)
        
        elif command == "gstart" or command == "giveawaystart" or command == "giveaway_create":
            embed = discord.Embed(title=  "Help GSTART", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Make giveaways!")
            embed.add_field(name = 'Permissions needed:', value = "`Manage Server, Manage Roles, Manage Channels`")
            embed.add_field(name = "Correct usage:", value = '`imp gstart`')
            await ctx.send(embed = embed)
        
        elif command == "reroll":
            embed = discord.Embed(title=  "Help Reroll", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Reroll an unfair giveaway!")
            embed.add_field(name = 'Permissions needed:', value = "`Manage Server, Manage Roles, Manage Channels`")
            embed.add_field(name = "Correct usage:", value = '`imp reroll [channel] [message_id] `')
            embed.add_field(name = "Extra notes:", value = "Be sure to copy the message id of the embed and not the message")
            await ctx.send(embed = embed)

        elif command == "invite":
            embed = discord.Embed(title=  "Help Invite", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "If you would like to invite me to your server!")
            embed.add_field(name = "Correct usage:", value = '`imp invite `')
            await ctx.send(embed = embed)

        elif command == "invite":
            embed = discord.Embed(title=  "Help Invite", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "If you would like to invite me to your server!")
            embed.add_field(name = "Correct usage:", value = '`imp invite `')
            await ctx.send(embed = embed)

        elif command == "show_toprole":
            embed = discord.Embed(title=  "Help Showtoprole", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Shows the highest role of a user")
            embed.add_field(name = "Correct usage:", value = '`imp show_toprole [user] `')
            await ctx.send(embed = embed)
        
        elif command == "botinfo":
            embed = discord.Embed(title=  "Help Botinfo", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Shows you information about the bot")
            embed.add_field(name = "Correct usage:", value = '`imp botinfo `')
            await ctx.send(embed = embed)
        
        elif command == "serverinfo":
            embed = discord.Embed(title=  "Help Serverinfo", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Shows you information about the server")
            embed.add_field(name = "Correct usage:", value = '`imp serverinfo `')
            await ctx.send(embed = embed)
        
        elif command == "channelinfo":
            embed = discord.Embed(title=  "Help Channelinfo", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Shows you information about a channel")
            embed.add_field(name = "Correct usage:", value = '`imp channelinfo [channel] `')
            await ctx.send(embed = embed)
        
        elif command == "candy":
            embed = discord.Embed(title=  "Help Candy", color = ctx.author.color)
            embed.add_field(name = "Description:", value = "Gives you candy idiot")
            embed.add_field(name = "Correct usage:", value = '`imp candy `')
            await ctx.send(embed = embed)

#MODERATION COMMANDS
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

@client.command(aliases=['ub'])
@commands.has_permissions(ban_members = True)
async def unban(ctx, member : discord.Member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if (user.name, user.discriminator) == (member_name,member_disc):
            await ctx.guild.unban(user)
            await ctx.send(member_name + " has been unbanned!")
            return

    await ctx.send(member + " Was Not Found")

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

@client.command()
@commands.has_permissions(kick_members = True)
async def warn(ctx, member : discord.Member, *, reason = None):
    embed = discord.Embed(title = f"{member.name} was warned!", color = ctx.author.color)
    embed.add_field(name = "Moderator", value = f"`{ctx.author.name}`")
    embed.add_field(name = "Reason", value = f"`{reason}`")
    await ctx.send(embed = embed)

@warn.error
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
async def helpowner(ctx):
    if ctx.author.id != ZAN_ID:
        await ctx.send("Not for server owners, but for the Emperor\nBehold my creator: NightZan999")
        return 
    embed = discord.Embed(title = "Help Bot Dev", color = discord.Color.purple())
    embed.add_field(name = "The Special Powers of the Sith!", value = "`Guilds`, `Leaveguild`")
    await ctx.send(embed = embed)

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
        with open("mainbank.json", "w") as f:
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

    with open("mainbank.json", "w") as f:
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

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

@client.command(aliases = ["with"])
async def withdraw(ctx, amount = None):
    #BTW for dep im not doing comments :-(
    await open_account(ctx.author) #opening their account
    if amount == None: #making sure they are withdrawing something!
        await ctx.send("Type an amount")

    amount = int(amount)
    bal = await update_bank(ctx.author)
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
@commands.cooldown(1, 10, commands.BucketType.user)
async def slots(ctx, amount = None): 
    await open_account(ctx.author)

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
        final.append(random.choice("🎃", "👻", "👾"))

    await ctx.send(final)

    if final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
        if final[0] == final[1] and final[1] == final[2]:
            await ctx.send("GRAND PRIZE")
            await update_bank(ctx.author, amount * 3, "wallet")
        else:
            await ctx.send("PRIZE!")
            await update_bank(ctx.author, amount * 2, "wallet")
    else:
        await ctx.send("YOU LOSE!!!")
        await update_bank(ctx.author, amount * -1, "wallet")

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
        with open("mainbank.json", "w") as f:
            json.dump(users, f)

        await ctx.send(f"Gave you {amount} coins!")
    else: #else it should not give!
        await ctx.send("Bruh, your not a bot dev!")   

#Helperfunctions
async def open_account(user):
    with open("mainbank.json", "r") as f:
        users = json.load(f)

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0 #I want them to get 100 coins
        users[str(user.id)]["bank"]  = 0

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

async def get_bank_data():
    with open("mainbank.json", "r") as f:
        users = json.load(f)
    return users

async def update_bank(user, change = 0, mode = "wallet"):
    users = await get_bank_data()
    users[str(user.id)][mode] = users[str(user.id)][mode] + change

    with open("mainbank.json", "w") as f:
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
        await asyncio.sleep(10)

    if client.is_closed():
        print("Offline again, f in the chat for the discord devs!")


#UTILITIES 
@client.command()
async def coinflip(ctx):
    list = ["Heads", "Tails"]
    embed = discord.Embed(title = "Coinflip by {}".format(ctx.author.name), color = ctx.author.color)
    embed.add_field(name = "We rolled a:", value = random.choice(list))
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
    
    with open("automod.json", "r") as f:
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

@client.command()
async def avatar(ctx, *, avamember : discord.Member = None):
    userAvatarUrl = avamember.avatar_url
    embed=discord.Embed(title=f'{avamember} avatar!!')
    embed.set_image(url=userAvatarUrl)
    await ctx.send(embed=embed)

@client.command()
async def channelinfo(ctx, channel : discord.TextChannel):
    try:
        nsfw = self.bot.get_channel(channel.id).is_nsfw()
        news = self.bot.get_channel(channel.id).is_news()
        embed = discord.Embed(title = 'Channel Infromation: ' + str(channel),
        color = ctx.author.color)
        embed.add_field(name = 'Channel Name: ', value = str(channel.name))
        embed.add_field(name = "Channel's NSFW Status: ", value = str(nsfw))
        embed.add_field(name = "Channel's id: " , value = str(channel.id))
        embed.add_field(name = 'Channel Created At: ', value = str(channel.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC")))
        embed.add_field(name = 'Channel Type: ', value = str(channel.type))
        embed.add_field(name = "Channel's Announcement Status: ", value = str(news))
        await ctx.send(embed = embed) 
    except:
        await ctx.send(f"Wow, next time try to mention a channel properly! Like {ctx.channel.mention}") 

@client.command()
async def userinfo(ctx, member : discord.Member):
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
    await ctx.send(embed=embed)

@client.command()
async def serverinfo(ctx):
    findbots = sum(1 for member in ctx.guild.members if member.bot)
    embed = discord.Embed(title = 'Infomation about ' + ctx.guild.name + '.', color = ctx.author.color)
    embed.set_thumbnail(url = str(ctx.guild.icon_url))
    embed.add_field(name = "Guild's name: ", value = ctx.guild.name)
    embed.add_field(name = "Guild's owner: ", value = str(ctx.guild.owner))
    embed.add_field(name = "Guild's verification level: ", value = str(ctx.guild.verification_level))
    embed.add_field(name = "Guild's id: ", value = str(ctx.guild.id))
    embed.add_field(name = "Guild's member count: ", value = str(ctx.guild.member_count))
    embed.add_field(name="Bots", value=findbots, inline=True)
    embed.add_field(name = "Guild created at: ", value = str(ctx.guild.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC")))
    await ctx.send(embed =  embed)


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
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")

@client.command()
@commands.has_permissions(administrator = True)
async def enableautomod(ctx):
    with open("automod.json", "r") as f:
        guilds = json.load(f)

    if ctx.guild.id in guilds:
        guilds[str(ctx.guild.id)]["automod"] = "true"
    else:
        guilds[str(ctx.guild.id)] = {}
        guilds[str(ctx.guild.id)]["automod"] = "true"

    embed = discord.Embed(title = 'Change in Server Settings', color = ctx.author.color)
    embed.add_field(name = 'Automod:', value = "`Automod = True`")    
    await ctx.send(embed = embed)

    with open("automod.json", "w") as f:
        json.dump(guilds, f)

@enableautomod.error
async def enableautomod_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("Bruh you really think you can use that?")

@client.command()
@commands.has_permissions(administrator = True)
async def disableautomod(ctx):
    with open("automod.json", "r") as f:
        guilds = json.load(f)

    if ctx.guild.id in guilds:
        guilds[str(ctx.guild.id)]["automod"] = "false"
    else:
        guilds[str(ctx.guild.id)] = {}
        guilds[str(ctx.guild.id)]["automod"] = "false"

    embed = discord.Embed(title = 'Change in Server Settings', color = ctx.author.color)
    embed.add_field(name = 'Automod:', value = "`Automod = False`")    
    await ctx.send(embed = embed)

    with open("automod.json", "w") as f:
        json.dump(guilds, f)

@client.command()
@commands.has_permissions(administrator = True)
async def checkautomod(ctx):
    with open("automod.json", "r") as f:
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
    embed = discord.Embed(title = "Botinfo", color = ctx.author.color)
    embed.add_field(name = "First went live on:", value = "1 / 10 / 2020")
    embed.add_field(name = "Started coding on:", value = "26 / 9 / 2020")
    embed.add_field(name = "Creator", value = "NightZan999#0194")
    embed.add_field(name = 'Hosting', value = "DanBot Hosting, tysm", inline = False)
    await ctx.send(embed = embed)

@client.command()
async def candy(ctx):
    await ctx.send("You want candy, take it!")
    await ctx.send(file = discord.File("candy.jpg"))

@client.command()
async def bounty(ctx, user : discord.Member = None):
    if user == None:
        await ctx.send("Must provide a valid user to bounty!")
        return

    await open_account(user)
    users = await get_bank_data()
    
    if users[str(ctx.author.id)]["wallet"] < 10000:
        await ctx.send("You are supposed to have atleast 10,000 coins to bounty someone!")
        return

    wanted = Image.open("wanted.jpg")
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())

    pfp = Image.open(data)
    pfp = pfp.resize((276, 350))
    wanted.paste(pfp, (220, 300))

    wanted.save("profile.jpg")

    embed = discord.Embed(title = "New BOUNTY!", color = ctx.author.color)    
    embed.add_field(name = "Owner:", value = f"`{ctx.author.name}`")
    embed.add_field(name = "Price:", vaue = f"`10,000`")
    await ctx.send(embed = embed)

    await ctx.send(file = discord.File("profile.jpg"))
    await ctx.send("First person to type `PAY PERSON` will start a bid for the bounty!")

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
    
    wanted = Image.open("wanted.jpg")    
    asset = user.avatar_url_as(size = 128)

    data = BytesIO(await asset.read())
    pfp = Image.open(data)

    pfp = pfp.resize((88, 88))
    wanted.paste(pfp, (47, 84))

    wanted.save("profile.jpg")
    await ctx.send(file = discord.File("profile.jpg"))

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

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")
    return [True,"Worked"]

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

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost,"wallet")

    return [True,"Worked"]    

async def check_for_item(user, item_name):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            break

    if name_ == None:
        return [False, 2]
    
    users = await get_bank_data()
    bal = await update_bank(user)
    index = 0
    t = None
    for thing in users[str(user.id)]["bag"]:
        n = thing["item"]
        if n == item_name:
            return True
            t = 1

    if t == None:
        return [False, 1]

@client.command()
async def meme(ctx):

    subreddit = reddit.subreddit("memes")
    top = subreddit.new(limit = 100)
    all_subs = []

    for submission in top:
        all_subs.append(submission)
    
    current_meme = random.choice(all_subs)

    name = current_meme.title
    url = current_meme.url

    em = discord.Embed(title = f"{name}", color = ctx.author.name)
    em.set_image(url = url)
    await ctx.send(embed = embed)

'''
Some fun data about this code:
1 Line of Code = 26/09/2020
50 Lines of Code = 27/09/2020
100 Lines of Code = 29/09/2020
250 Lines of Code = 30/09/2020
500 Lines of Code = 07/10/2020
1000 Lines of Code = 19/10/2020
1500 Lines of Code = 05/11/2020
2000 Lines of Code = 
'''

client.loop.create_task(ch_pr())
client.run(BOT_TOKEN)
