"""
MIT LICENCE 2020 - 2021
All the code and the full bot is nothing but TheImperialGod
All the code is made by NightZan999, check him out at https://github.com/NightZan999
The deposit and withdraw command have been added on to by Makiyu-py, he used it in a fork
The repository the code has been taken from is at https://github.com/NightZan999/TheImperialGod

Be sure to have this in your project at the beginning!
"""
import discord #discord object
import discord.ext #external
from discord.ext import commands #commands from external
import random #random
import json
import os
import asyncio

def load_cogs(client): #loading all our cogs
    for folder in os.listdir("./cogs"):
        cogCount = 0
        for filename in os.listdir(f"./cogs/{folder}"):
            if filename.endswith(".py"):
                cogCount += 1
                client.load_extension(f"cogs.{folder}.{filename[:-3]}")

        eventCount = 0
        for event in os.listdir("./events"):
            if event.endswith(".py"):
                eventCount += 1
                client.load_extension(f"events.{filename[:-3]}")

        print(f"{cogCount} cogs have been loaded!\n{eventCount} events have been loaded")

with open("config.json", "r") as f:
    config = json.load(f)

#consts
BOT_TOKEN = config["token"]
CLIENT_ID = config["clientId"]
CLIENT_SECRET = config["clientSecret"]
PUBLIC_KEY = config["publicKey"]
BOT_PREFIX = config["prefix"]
new_link ="https://discordapp.com/oauth2/authorize?&client_id=".join(str(CLIENT_ID))
new_link.join("&scope=bot&permissions=21474836398")

intents = discord.Intents.all()
client = commands.Bot(command_prefix = BOT_PREFIX, case_insensitive = True, intents = intents) #making a client object

#when the bot gets ready
@client.event
async def on_ready():
    print("Ready!")
    print("Username: ", client.user.name)
    print("User ID: ", client.user.id)
    print("----------------------------")

async def ch_pr(): #changing the bots status every 5 secs!!!
    await client.wait_until_ready()

    while not client.is_closed():
        statuses = [
            f"The Protection of {len(client.guilds)} servers",
            "Making money!",
            "Hosting Giveaways",
            "imp gstart",
            "Kicking people!",
            "Using utils!",
            f"Serving {len(client.users)} users",
            "Calculating inflation!",
            "Changing statuses!"
        ]
        status = random.choice(statuses)

        await client.change_presence(activity = discord.Streaming(name = status, url = "https://twitch.tv/pewdiepie"))
        await asyncio.sleep(15)

    if client.is_closed():
        print("Offline again, f in the chat for the discord devs!")
        
# create filtered_words and racial_slurs
@client.event
async def on_message(msg):
    with open("data/automod.json", "r") as f:
        guilds = json.load(f)

    try:
        if guilds[str(msg.guild.id)]["automod"] == "true":
            if not msg.channel.is_nsfw:
                for word in filtered_words:
                    if word in msg.content.lower():
                        await msg.delete()
                        await msg.author.send("Watch your language!")
                for slur in racial_slurs:
                    if slur in msg.content.lower():
                        await msg.delete()
                        await msg.author.ban(reason = "Used a racial slur!")
                        await msg.author.send("You were banned because you used a racial slur!")
                        return
        
        if msg.mentions[0] == self.client.user:
            em = discord.Embed(title = "Help for TheImperialGod", color = ctx.author.color,
            description = "Check some information about me!")
            em.add_field(name = "What can I do?", value = "I can make your server so charming! Whether you are a moderator or not!")
            em.add_field(name = "Commands:", value = "Check out `imp help` for a list of my commands")
            em.add_field(name = "Prefix:", value = "My prefix is `imp`")
            em.add_field(name = "Command Types", value = "Economy, Moderation, Information, Utilities, Math, Fun, Giveaways, Tickets, Miscellanous, Admin. ")
            await message.channel.send(embed = em)
    except:
        pass
    await client.process_commands(msg)

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
5000 Lines of Code = 31/01/2020
'''
load_cogs(client)
client.loop.create_task(ch_pr())
client.run(BOT_TOKEN)
