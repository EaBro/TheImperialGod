import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
import math as m

class Mathematics(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Mathematics commands are ready!")
        
    def get_out(_type, num1, num2=None):
        try:
            num1 = float(num1)
            num2 = float(num2) if num2 is not None and _type in ["a", "s", "m", "d"] else None
        except ValueError:
            return False
        
        if _type == "a":
            return num1 + num2
        elif _type == "s":
            return num1 - num2
        elif _type == "m":
            return num1 * num2
        elif _type == "d":
            return num1 / num2
        elif _type == "sq":
            return num1 * num1
        
    @commands.command()
    @cooldown(1, 5, BucketType.user)
    async def add(self, ctx, num1, num2):
        output = get_out("a", num1, num2)
        if output == False:
            await ctx.send("Both your input must be numbers! Next time add numbers!")
            return

        em = discord.Embed(title = "<:success:761297849475399710> Adding Successful", color = ctx.author.color)
        em.add_field(name = "Number 1:", value = f"`{num1}`")
        em.add_field(name=  "Number 2:", value = f"`{num2}`")
        em.add_field(name = "Answer", value = f"`{output}`", inline = False)
        return await ctx.send(embed = em)

    @add.error
    async def add_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            em = discord.Embed(title = "<:fail:761292267360485378> Adding Failed", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "You didn't provide all 2 numbers to add!")
            em.add_field(name = "Usage:", value = f"```\nimp add <num1> <num2>\n```")
            await ctx.send(embed = em)
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = "<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "Did you go to middle school? Stop constantly adding!")
            em.add_field(name = "Try again in:", value = "{:.2f}".format(error.retry_after))
            await ctx.send(embed = em)
    
    @commands.command(aliases=["sub"])
    @cooldown(1, 5, BucketType.user)
    async def subtract(self, ctx, num1, num2):
        output = get_out("s", num1, num2)
        if output == False:
            await ctx.send("Both your input must be numbers! Next time subtract numbers!")
            return

        em = discord.Embed(title = "<:success:761297849475399710> Subtracting Successful", color = ctx.author.color)
        em.add_field(name = "Number 1:", value = f"`{num1}`")
        em.add_field(name=  "Number 2:", value = f"`{num2}`")
        em.add_field(name = "Answer", value = f"`{output}`", inline = False)
        return await ctx.send(embed = em)

    @subtract.error
    async def subtract_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            em = discord.Embed(title = "<:fail:761292267360485378> Subtracting Failed", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "You didn't provide all 2 numbers to subtract!")
            em.add_field(name = "Usage:", value = f"```\nimp sub <num1> <num2>\n```")
            await ctx.send(embed = em)
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = "<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "Did you go to middle school? Stop constantly subtracting!")
            em.add_field(name = "Try again in:", value = "{:.2f}".format(error.retry_after))
            await ctx.send(embed = em)

    @commands.command(aliases=["mul"])
    @cooldown(1, 5, BucketType.user)
    async def multiply(self, ctx, num1, num2):
        output = get_out("m", num1, num2)
        if output == False:
            await ctx.send("Both your input must be numbers! Next time multiply numbers!")
            return

        em = discord.Embed(title = "<:success:761297849475399710> Multiplication Successful", color = ctx.author.color)
        em.add_field(name = "Number 1:", value = f"`{num1}`")
        em.add_field(name=  "Number 2:", value = f"`{num2}`")
        em.add_field(name = "Answer", value = f"`{output}`", inline = False)
        return await ctx.send(embed = em)

    @multiply.error
    async def multiply_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            em = discord.Embed(title = "<:fail:761292267360485378> Multiplication Failed", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "You didn't provide all 2 numbers to multiply!")
            em.add_field(name = "Usage:", value = f"```\nimp mul <num1> <num2>\n```")
            await ctx.send(embed = em)
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = "<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "Did you go to middle school? Stop constantly multiplying!")
            em.add_field(name = "Try again in:", value = "{:.2f}".format(error.retry_after))
            await ctx.send(embed = em)

    @commands.command(aliases=["div"])
    @cooldown(1, 5, BucketType.user)
    async def divide(self, ctx, num1, num2):
        output = get_out("d", num1, num2)
        if output == False:
            await ctx.send("Both your input must be numbers! Next time divide numbers!")
            return

        em = discord.Embed(title = "<:success:761297849475399710> Division Successful", color = ctx.author.color)
        em.add_field(name = "Number 1:", value = f"`{num1}`")
        em.add_field(name=  "Number 2:", value = f"`{num2}`")
        em.add_field(name = "Answer", value = f"`{output}`", inline = False)
        return await ctx.send(embed = em)

    @divide.error
    async def divide_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            em = discord.Embed(title = "<:fail:761292267360485378> Division Failed", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "You didn't provide all 2 numbers to divide!")
            em.add_field(name = "Usage:", value = f"```\nimp div <num1> <num2>\n```")
            await ctx.send(embed = em)
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = "<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "Did you go to middle school? Stop constantly dividing!")
            em.add_field(name = "Try again in:", value = "{:.2f}".format(error.retry_after))
            await ctx.send(embed = em)

    @commands.command(aliases=["sq"])
    @cooldown(1, 30, BucketType.user)
    async def square(self, ctx, num):
        output = get_out("sq", num)
        if output == False:
            return await ctx.channel.send("Your input has to be an number")
        else:
            em = discord.Embed(title = "<:success:761297849475399710> Getting Squared Successful", color = ctx.author.color)
            em.add_field(name = "Number", value = f"`{num}`")
            em.add_field(name = "Answer", value = f"`{output}`", inline = False)
            return await ctx.send(embed = em)

    @square.error
    async def square_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            em = discord.Embed(title = "<:fail:761292267360485378> Getting Squared Failed", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "You didn't provide 1 number to square!")
            em.add_field(name = "Usage:", value = f"```\nimp sq <num>\n```")
            await ctx.send(embed = em)
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = "<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "Did you go to high school? Stop constantly getting a square of a number!")
            em.add_field(name = "Try again in:", value = "{:.2f}".format(error.retry_after))
            await ctx.send(embed = em)

    @commands.command(aliases=["sqrt"])
    @cooldown(1, 30, BucketType.user)
    async def squareroot(self, ctx, num):
        try:
            num1 = float(num)
        except:
            return await ctx.channel.send("Your input has to be a number")
        else:
            em = discord.Embed(title = f"<:success:761297849475399710> Getting Square Root of {num} is Successful", color = ctx.author.color)
            em.add_field(name = "Number", value = f"`{num}`")
            em.add_field(name = "Answer", value = f"`{m.sqrt(num)}`", inline = False)
            return await ctx.send(embed = em)

    @squareroot.error
    async def squareroot_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            em = discord.Embed(title = "<:fail:761292267360485378> Getting Square Root Failed", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "You didn't provide 1 number to get the square root of!")
            em.add_field(name = "Usage:", value = f"```\nimp sqrt <num>\n```")
            await ctx.send(embed = em)
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = "<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "Did you go to high school? Stop constantly getting a square root of a number!")
            em.add_field(name = "Try again in:", value = "{:.2f}".format(error.retry_after))
            await ctx.send(embed = em)

def setup(client):
    client.add_cog(Mathematics(client))
