from discord.ext.commands import Bot
import json
from .utils.emojis import Emojis

class TheImperialGod(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cogs = [
            "cogs.info.help", # help command
            "cogs.fun.animals", # searching reddit
            "cogs.economy.bankcommands", # bank commands in economy
            "cogs.economy.moneymaking", # moneymaking commands in economy
            "cogs.economy.shop", # making a shop with database in economy!
            "cogs.economy.gambling", # gambling commands
            "cogs.fun.misc", # misc commands
            "cogs.fun.utils", # utilities
            "cogs.info.info", # information
            "cogs.info.math", # math commands
            "cogs.moderation.giveaways", # giveaway commands!
            "cogs.moderation.mod", # moderation commands
            "cogs.moderation.owner", # owner commands
            "cogs.tickets.tickets", # ticket commands
            "cogs.info.topgg", # has top.gg stuff bois!
            "cogs.exclusive.exclusive" # has exclusive commands
        ]

        self.events = [
            "events.GuildEvents", # when the bot leaves or joins a guild!
            "events.ReactionAdd",
            "events.ReactionRemove"
        ]

    async def on_ready(self):
        print("Ready!")
        print("Username: ", client.user.name)
        print("User ID: ", client.user.id)
        print("----------------------------")

    async def get_cogs(self):
        return self.cogs
    
    async def get_events(self):
        return self.events
    
    async def get_all_emojis(self):
        return Emojis
    
    async def read_json(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
        return data
    
    async def write_json(self, output, filename):
        with open(filename, "w") as f:
            return json.dump(output, f)