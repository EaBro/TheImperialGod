import discord
from discord.ext import commands
import aiosqlite
import random
from discord.ext.commands import cooldown, BucketType

class Economy(commands.Cog):
    """Economy commands!"""

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Economy commands are ready!')
        async with aiosqlite.connect("./data/economy.db") as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("CREATE TABLE IF NOT EXISTS users (userid INTEGER, bank INTEGER, wallet INTEGER);")
                await connection.commit()

    @commands.command(aliases=['bal'])
    @cooldown(1, 5, BucketType.channel)
    async def balance(self, ctx, member : discord.Member= None):
        if member == None:
            member = ctx.author
        async with aiosqlite.connect("./data/economy.db") as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("SELECT * FROM users WHERE userid = ?",(member.id,))
                rows = await cursor.fetchone()
                if not rows:
                    await cursor.execute("INSERT INTO users (userid, bank, wallet) VALUES (?,?,?)",(member.id,0,0))
                    await cursor.execute("SELECT * FROM users WHERE userid = ?",(member.id,))
                    rows = await cursor.fetchone()
                await connection.commit()
                em = discord.Embed(title = f"{member.name}'s Balance", color = ctx.author.color)
                em.add_field(name = "Wallet Balance:", value = f"{rows[2]} :coin:")
                em.add_field(name = "Bank Balance:", value = f"{rows[1]} :coin:")
                await ctx.send(embed=em)

    @commands.command(aliases=['dep'])
    @commands.cooldown(1,5,commands.BucketType.user)
    async def deposit(self,ctx,amount = None):
        if amount == None:
            await ctx.send("Type an amount you idiot!")
            return

        if amount != "all":
            amount = int(amount)

        async with aiosqlite.connect("./data/economy.db") as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("SELECT bank, wallet FROM users WHERE userid = ?",(ctx.author.id,))
                rows = await cursor.fetchone()
                if not rows:
                    await cursor.execute("INSERT INTO users (userid, bank, wallet) VALUES (?,?,?)",(ctx.author.id,0,0,''))
                else:
                    if amount != 'all':
                        if amount > rows[1]:
                            await ctx.send("You dont have that much money, get richer!")
                            return
                        elif amount <= 0:
                            await ctx.send("Bruh, don't try to break me!")
                            return
                        else:
                            await cursor.execute("UPDATE users SET wallet = ?, bank = ? WHERE userid = ?",(rows[1] - amount,rows[0] + amount,ctx.author.id,))
                            await ctx.send(f"Wow you deposited {amount} coins into your bank!")
                    else:
                        await cursor.execute("UPDATE users SET wallet = ?, bank = ? WHERE userid = ?",(0,rows[0] + rows[1],ctx.author.id,))
                        await ctx.send(f"Successfully deposited {rows[1]} into your bank")
                    await connection.commit()

    @commands.command(aliases=['with'])
    @commands.cooldown(1,5,commands.BucketType.user)
    async def withdraw(self,ctx,amount = None):
        if amount == None:
            await ctx.send("Type an amount!")
            return

        if not amount == 'all':
            amount = int(amount)
        async with aiosqlite.connect("./data/economy.db") as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("SELECT bank, wallet FROM users WHERE userid = ?",(ctx.author.id,))
                rows = await cursor.fetchone()
                if not rows:
                    await cursor.execute("INSERT INTO users (userid, bank, wallet) VALUES (?,?,?)",(ctx.author.id,0,0,))
                else:
                    if not amount == 'all':
                        if amount > rows[0]:
                            await ctx.send("You dont have that much")
                        elif amount <= 0:
                            await ctx.send("That is too low")
                        else:
                            await cursor.execute("UPDATE users SET wallet = ?, bank = ? WHERE userid = ?",(rows[1] + amount,rows[0] - amount,ctx.author.id,))
                            await ctx.send(f"Successfully withdrew {amount} from your bank")
                    else:
                        await cursor.execute("UPDATE users SET wallet = ?, bank = ? WHERE userid = ?",(rows[1] + rows[0],0,ctx.author.id,))
                        await ctx.send(f"Successfully withdrew {rows[0]} from your bank")
                await connection.commit()

def setup(client):
    client.add_cog(Economy(client))
