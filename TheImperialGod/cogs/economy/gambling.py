import discord
from discord.ext import commands
import random

class Gambling(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Gambling commands are loaded!")

    @commands.command()
    async def bet(self, ctx, amount = None):
        if amount is None:
            em = discord.Embed(title = "<:fail:761292267360485378> Bet failed!", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "You didn't provide an amount. Or go to school!")
            em.add_field(name = "Next Steps:", value = "Next time try to type an amount too!")
            em.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = em)
            return

        if amount != 'all':
            amount = int(amount)
    
        async with aiosqlite.connect("./data/economy.db") as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("SELECT bank, wallet FROM users WHERE userid = ?", (ctx.author.id))
                rows = await cursor.fetchone()

                if not rows:
                    await ctx.send("bruh you haven't even played-")
                    return
                
                if rows[1] < amount:
                    em = discord.Embed(title = "<:fail:761292267360485378> Bet failed!", color = ctx.author.color)
                    em.add_field(name = "Reason:", value = "You don't even have that much money!")
                    em.add_field(name = "Next Steps:", value = "Get richer next time!")
                    em.set_thumbnail(url = ctx.author.avatar_url)
                    await ctx.send(embed = em)
                    return
                
                if amount == 0 or amount < 0:
                    em = discord.Embed(title = "<:fail:761292267360485378> Bet failed!", color = ctx.author.color)
                    em.add_field(name = "Reason:", value = "Amount was too low!")
                    em.add_field(name = "Next Steps:", value = "Type a positive integer next time!")
                    em.set_thumbnail(url = ctx.author.avatar_url)
                    await ctx.send(embed = em)
                    return

                res = random.choice(["Won", "Lost"])
                if res == "Won":
                    em = discord.Embed(title= "<:success:761297849475399710> Bet Won!", color = ctx.author.color)
                    em.add_field(name = "Money Earned:", value = f"{amount}")
                elif res == "Lost":
                    em = discord.Embed(title= "<:fail:761292267360485378> Bet Lost!", color = ctx.author.color)
                    em.add_field(name = "Money Lost:", value = f"{amount}")
                em.add_field(name = "Result:", value =f"{res}")

                if res == "Won":
                    await cursor.execute("UPDATE users SET wallet = ?, bank = ? WHERE userid = ?", (rows[1] + amount, rows[0], ctx.author.id))
                elif res == "Lost":
                    await cursor.execute("UPDATE users SET wallet = ?, bank = ? WHERE userid = ?", (rows[1] - amount, rows[0], ctx.author.id))


def setup(client):
    client.add_cog(Gambling(client))