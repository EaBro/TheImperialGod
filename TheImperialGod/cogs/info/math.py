import discord
from discord.ext import commands
import math

class Math(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Mathematics command are loaded")

    @commands.command()
    async def add(self, ctx, num1, num2):
        num1 = int(num1)
        num2 = int(num2)
        res = num1 + num2
        embed = discord.Embed(title = "Sum:", color = ctx.author.color)
        embed.add_field(name = "Result:", value = f"`{res}`")
        embed.set_footer(text='Bot Made by NightZan999#0194')
        await ctx.send(embed = embed)

    @commands.command()
    async def subtract(self, ctx, num1, num2):
        num1 = int(num1)
        num2 = int(num2)
        res = num1 - num2
        embed = discord.Embed(title = "Difference:", color = ctx.author.color)
        embed.add_field(name = "Result:", value = f"`{res}`")
        embed.set_footer(text='Bot Made by NightZan999#0194')
        await ctx.send(embed = embed)

    @commands.command()
    async def multiply(self, ctx, num1, num2):
        num1 = int(num1)
        num2 = int(num2)
        res = num1 * num2
        embed = discord.Embed(title = "Product:", color = ctx.author.color)
        embed.add_field(name = "Result:", value = f"`{res}`")
        embed.set_footer(text='Bot Made by NightZan999#0194')
        await ctx.send(embed = embed)

    @commands.command()
    async def divide(self, ctx, num1, num2):
        num1 = int(num1)
        num2 = int(num2)
        res = num1 / num2
        embed = discord.Embed(title = "Quotient:", color = ctx.author.color)
        embed.add_field(name = "Result:", value = f"`{res}`")
        embed.set_footer(text='Bot Made by NightZan999#0194')
        await ctx.send(embed = embed)

    @commands.command()
    async def square(self, ctx, num1):
        num1 = int(num1)
        res = num1 * num1
        embed = discord.Embed(title = "Square:", color = ctx.author.color)
        embed.add_field(name = "Result:", value = f"`{res}`")
        embed.set_footer(text='Bot Made by NightZan999#0194')
        await ctx.send(embed = embed)

    @commands.command()
    async def sqrt(self, ctx, num1):
        num1 = int(num1)
        res = math.sqrt(num1)

        embed = discord.Embed(title = "Sum:", color = ctx.author.color)
        embed.add_field(name = "Result:", value = f"`{res}`")
        embed.set_footer(text='Bot Made by NightZan999#0194')
        await ctx.send(embed = embed)

    @commands.command()
    async def pow(self, ctx, num1, num2):
        num1 = int(num1)
        num2 = int(num2)
        res = math.pow(num1, num2)

        embed = discord.Embed(title = "Sum:", color = ctx.author.color)
        embed.add_field(name = "Result:", value = f"`{res}`")
        embed.set_footer(text='Bot Made by NightZan999#0194')
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Math(client))
