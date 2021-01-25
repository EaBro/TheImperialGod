import discord
from discord.ext import commands
from random import choice

class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Server Utilties are ready to be used!")

    @commands.command()
    async def coinflip(self, ctx):
        em = discord.Embed(title = "Coinflip", color = ctx.author.color)
        choices = ["Heads", "Tails"]
        em.add_field(name = "Roll:", value = f"`{choice(choices)}` :coin:")
        return await ctx.send(embed = em)

    @commands.command(aliases=["rn"])
    async def random_number(self, ctx, range1, range2):
        try:
            range1 = int(range1)
            range2 = int(range2)
        except TypeError:
            return await ctx.send("The ranges are both integers! You have not typed integers!")
        
        else:
            if (range1 > range2):
                return ctx.channel.send("the first range must be smaller than the second, idiot!")
            elif range1 == range2:
                return ctx.channel.send("the first range must be smaller than the second, not the same idiot!")
            num = randint(range1, range2)

            await ctx.send("Random number is `{}`".format(num))
    
    @random_number.error
    async def random_number_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            em  = discord.Embed(title = "<:fail:761292267360485378> Random Number Error", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "Missing Required Arguments!")
            em.add_field(name = "Args:", value = "```\nimp random_number <first_range> <second_range>\n```")
            await ctx.send(embed = em)

def setup(client):
    client.add_cog(Utils(client))