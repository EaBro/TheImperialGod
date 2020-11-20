import discord
from discord.ext import commands
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

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Help command ready!")
    
    @commands.command()
    async def helpowner(self, ctx):
        if ctx.author.id != ZAN_ID:
            await ctx.send("Not for server owners, but for the Emperor\nBehold my creator: NightZan999")
            return
        embed = discord.Embed(title = "Help Bot Dev", color = discord.Color.purple())
        embed.add_field(name = "The Special Powers of the Sith!", value = "`Guilds`, `Leaveguild`, `load`, `unload`")
        await ctx.send(embed = embed)

    @commands.command()
    async def help(self, ctx, command = None):
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
            embed.add_field(name = f":dollar: Economy Commands: [{len(economy_commands)}]", value = "`Balance`, `Beg`, `Serve`, `Withdraw`, `Deposit`, `Slots`, `Rob`, `Dice`, `Leaderboard`, `Daily`, `Weekly` ")
            embed.add_field(name = f"<:moderation:761292265049686057> Moderation Commands: [15]", value = "`Kick`, `Ban`, `Softban`, `Purge`, `Lock`, `Unlock`, `Mute`, `Unmute`, `Unban`, `Addrole`, `Delrole`, `Announce`, `Warn`, `Checkwarns`, `setbanwarns`, `nick`")
            embed.add_field(name = f":tools: Utilities: [{len(utils_commands)}]", value = "`Coinflip`, `Random_Number`, `code`, `guess`, `respect`, `poll`, `thank`, `reverse`, `eightball`, `fight`, `wanted`, `quote`, `whois`, `osay`, `nick`")
            embed.add_field(name = f':video_game: Animals: [7]', value = f"`dog`, `cat`, `duck`, `fox`, `panda`, `koala`")
            embed.add_field(name = f":gift: Giveaways: [{len(gaws_commands)}]", value = "`gstart`, `reroll`")
            embed.add_field(name = f":question: Misc: [{len(misc_commands)}]", value = "`invite`, `show_toprole`, `botinfo`, `serverinfo`, `userinfo`, `channelinfo`, `avatar`, `candy`, `hypesquad`")
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

def setup(client):
    client.add_cog(Help(client))