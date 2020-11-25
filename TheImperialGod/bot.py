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
# reddit
import praw

banned_userids = [
    758169063871741984
]

def load_cogs(): #loading all our cogs
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            client.load_extension(f"cogs.{filename[:-3]}")

with open("config.json", "r") as f:
    config = json.load(f)

BOT_TOKEN = config["token"]
#constants
CLIENT_ID = 768695035092271124
CLIENT_SECRET = "dOT7giQx_zJKPPbk3QLRQkl0QrGdSMgH"
INVITE_LINK = "https://discordapp.com/oauth2/authorize?&client_id=768695035092271124&scope=bot&permissions=21474836398"
PUBLIC_KEY = "cb1c82b5894134285d3313d67742d62d75e72149b9a7bab0bec4f29bd0b90292"
LINES_OF_CODE = 500
DATABASES = 'data/mainbank.json'
PACKAGING_DATA = "package.json"
BOT_PREFIX = config["prefix"]
ZAN_ID = 575706831192719370

client = commands.Bot(command_prefix = BOT_PREFIX, case_insensitive = True) #making a client object
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

@client.remove_command("help")
@client.command()
async def help(ctx, command = None):
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
        'wanted',
        "quote",
        "osay"
        ]
    gaws_commands = [
            'gstart',
            'reroll'
            ]
    misc_commands = [
            'invite',
            'show_toprole',
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
    info_commands = [
        "channelinfo",
        "botinfo",
        "serverinfo",
        "userinfo"
    ]
    async with ctx.typing():
        await asyncio.sleep(2)
        if command == None:
            embed = discord.Embed(title = "Help", color = ctx.author.color, description = "Type `imp help` and then a command or category for more information for even more information!")
            embed.add_field(name = f":dollar: Economy Commands: [{len(economy_commands)}]", value = "`Balance`, `Beg`, `Serve`, `Withdraw`, `Deposit`, `Slots`, `Rob`, `Dice`, `Leaderboard`, `Daily`, `Weekly` ")
            embed.add_field(name = f"<:moderation:761292265049686057> Moderation Commands: [15]", value = "`Kick`, `Ban`, `Softban`, `Purge`, `Lock`, `Unlock`, `Mute`, `Unmute`, `Unban`, `Addrole`, `Delrole`, `Announce`, `Warn`, `nick`, `setmuterole`")
            embed.add_field(name = f"<:info:761298826907746386> Information Commands: [{len(info_commands)}]", value = f"`userinfo`, `avatar`, `serverinfo`, `whois`, `channelinfo`, `botinfo`")
            embed.add_field(name = f":tools: Utilities: [{len(utils_commands)}]", value = "`Coinflip`, `Random_Number`, `code`, `guess`, `respect`, `poll`, `thank`, `reverse`, `eightball`, `fight`, `quote`, `osay`, `nick`")
            embed.add_field(name = f"<:pepethink:779232211336822804> Math Commands [7]:", value = f"`add`, `subtract`, `multiply`, `divide`, `square`, `sqrt`, `pow`")
            embed.add_field(name = f"Image Module [2]: ", value = f"`wanted`, `crown`")
            embed.add_field(name = f':video_game: Animals: [7]', value = f"`dog`, `cat`, `duck`, `fox`, `panda`, `koala`")
            embed.add_field(name = f":gift: Giveaways: [{len(gaws_commands)}]", value = "`gstart`, `reroll`")
            embed.add_field(name = f":question: Misc: [{len(misc_commands)}]", value = "`invite`, `show_toprole`, `avatar`, `candy`, `hypesquad`")
            embed.add_field(name = f"<:owner:761302143331205131> Owner: [{len(owner_commands)}]", value = "`enableautomod`, `disableautomod`, `checkautomod`, `addwinnerrole`")
            embed.add_field(name = "Invite Link:", value = f"[Invite Link]({INVITE_LINK})", inline = False)
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
                em.add_field(name = "Purge", value = "Deletes plenty of messages")
                em.add_field(name = "Lock", value = "Makes sure no-one other than mods can type in a channel!")
                em.add_field(name = "Unlock", value = "Unlocks a locked channel")
                em.add_field(name = "Addrole", value = "Simply gives a role to someone, uses role id!")
                em.add_field(name = "Removerole", value = "Removes a role from someone, uses role id!")
                em.add_field(name = "Announce", value = "Make an announcement with the bot! Uses channel id")
                em.add_field(name = "Addwarnpoints", value = "Add warn points to a user")
                em.add_field(name = 'Removewarnpoints', value = "Remove warn points")
                em.add_field(name = "Setwarnbanpoints", value = "Set a number of points, in which a user gets banned")
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
                em.add_field(name=  "Whois", value = "Show information about people")
                em.add_field(name=  "Osay:", value = "Make the bot say something in a channel")
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
                embed.add_field(name = "Correct usage", value = f"`imp lock [reason]`")
                await ctx.send(embed = embed)

            elif command == "unlock":
                embed = discord.Embed(title = "Help on Unlock", color = ctx.author.color)
                embed.add_field(name = "Requirements - Permissions:", value = f"`Manage Channels`")
                embed.add_field(name = "Correct usage", value = f"`imp unlock [reason]`")
                await ctx.send(embed = embed)

            elif command == "setdelay":
                embed = discord.Embed(title = "Help on Setdelay", color = ctx.author.color)
                embed.add_field(name = "Requirements - Permissions:", value = f"`Manage Messages`")
                embed.add_field(name = "Correct usage", value = f"`imp setdelay <secs>`")
                await ctx.send(embed = embed)

            elif command == "unban":
                embed = discord.Embed(title = "Help on Unban", color = ctx.author.color)
                embed.add_field(name = "Requirements - Permissions:", value = f"`Ban Members`")
                embed.add_field(name = "Correct usage", value = f"`imp unban {ctx.author.mention}`")
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

            elif command == "dog":
                embed = discord.Embed(title = "Help Dog", color = ctx.author.color)
                embed.add_field(name = "Description:", value = "Shows you any random dog from reddit!")
                embed.add_field(name = "Correct Usuage:", value = f'`imp {command}`')
                await ctx.send(embed = embed)

            elif command == "osay":
                await ctx.send("Make the bot say something!")

            elif command == "nick":
                embed = discord.Embed(title = "Help Nick", color = ctx.author.color)
                embed.add_field(name = "Description:", value = "Change your nickname boi!")
                await ctx.send(embed = embed)


#when an error occurs
@client.command()
async def invite(ctx):
    embed = discord.Embed(title = "Invite Link:", color = ctx.author.color)
    embed.add_field(name = "Here:", value = f"[Click me]({INVITE_LINK})")
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

    if user.id in banned_userids:
        return False

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
    
    if user.id in banned_userids:
        return

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


@client.command()
async def support(ctx):
    await ctx.send("Please vote for the bot on top.gg\nLink: ")

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
async def load(ctx, extension):
    if ZAN_ID != ctx.author.id:
        await ctx.send("Only for bot devs")
        return
    client.load_extension(f"cogs.{extension}")
    await ctx.send("loaded the cog...")

@client.command()
async def unload(ctx, extension):
    if ZAN_ID != ctx.author.id:
        await ctx.send("Only for bot devs")
        return
    client.unload_extension(f"cogs.{extension}")
    await ctx.send('unloaded the cog...')


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
load_cogs() #finally loading all our files, since I dont want to type:
#imp load [cog_name] for all my cogs, its better automated!
client.loop.create_task(ch_pr())
client.run(BOT_TOKEN)