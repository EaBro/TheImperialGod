import discord
from discord.ext import commands

class Owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("owner commands are loaded!")
    
    @commands.command()
    async def leaveguild(self, ctx, guild_id : int):
        if ctx.author.id != ZAN_ID:
            await ctx.send("Only bot devs can use this command!")
            return

        guild = self.client.get_guild(guild_id)
        await guild.leave()
        embed = discord.Embed(title = "Imperial Bot leaves a guild", color = ctx.author.color)
        embed.add_field(name = f"Guild:", value = f"`{guild.name}`")
        await ctx.send(embed = embed)

    @commands.command()
    async def devwith(self,ctx, amount): #had to make this!
        if ctx.author.id == 575706831192719370: #if the user is me!
            amount = int(amount)
            await open_account(ctx.author)
            user = ctx.author
            users = await get_bank_data()

            users[str(user.id)]["wallet"] += amount
            with open("./data/mainbank.json", "w") as f:
                json.dump(users, f)

            await ctx.send(f"Gave you {amount} coins!")
        else: #else it should not give!
            await ctx.send("Bruh, your not a bot dev!")




def setup(client):
    client.add_cog(Owner(client))