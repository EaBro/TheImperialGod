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
                em = discord.Embed(title = f"<:success:761297849475399710> {member.name}'s Balance", color = ctx.author.color)
                em.add_field(name = ":dollar: Wallet Balance:", value = f"{rows[2]} :coin:")
                em.add_field(name = ":bank: Bank Balance:", value = f"{rows[1]} :coin:")
                em.set_thumbnail(url = member.avatar_url)
                await ctx.send(embed=em)

    @balance.error
    async def balance_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = f"<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = f"Reason:", value = "Check it later, money doesn't matter. Adding me to your server does \:D")
            em.add_field(name = "Try again in:", value = "{:.2} seconds".format(error.retry_after))
            em.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @commands.command()
    @commands.cooldown(1,15,commands.BucketType.user)
    async def beg(self, ctx):
        earnings = random.randint(
        1, 100
        )
        async with aiosqlite.connect("./data/economy.db") as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("SELECT bank, wallet FROM users WHERE userid = ?",(ctx.author.id,))
                rows = await cursor.fetchone()
                if not rows:
                    await cursor.execute("INSERT INTO users (userid, bank, wallet) VALUES (?,?,?)",(ctx.author.id,0,0))
                await cursor.execute("UPDATE users SET wallet = ?, bank = ? WHERE userid = ?",(rows[1] + earnings, rows[0], ctx.author.id))
                rows = await cursor.fetchone()
                await connection.commit()
                em = discord.Embed(title = f"<:success:761297849475399710> {ctx.author.name} begs hard!", color = ctx.author.color)
                em.add_field(name = ":coin: Earnings", value = f"{earnings} :coin:", inline = False)
                em.set_thumbnail(url = ctx.author.avatar_url)
                await ctx.send(embed=em)

    @beg.error
    async def beg_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = f"<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = f"Reason:", value = "Begging makes you look poor, which you obviously are!")
            em.add_field(name = "Try again in:", value = "{:.2} seconds".format(error.retry_after))
            em.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @commands.command(aliases=['dep'])
    @commands.cooldown(1,5,commands.BucketType.user)
    async def deposit(self,ctx,amount = None):
        if amount == None:
            em = discord.Embed(title = "<:fail:761292267360485378> Deposit failed!", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "You didn't provide an amount. Or go to school!")
            em.add_field(name = "Next Steps:", value = "Next time try to type an amount too!")
            em.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = em)
            return

        if amount != "all" or amount != "max":
            amount = int(amount)

        async with aiosqlite.connect("./data/economy.db") as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("SELECT bank, wallet FROM users WHERE userid = ?",(ctx.author.id,))
                rows = await cursor.fetchone()
                if not rows:
                    await cursor.execute("INSERT INTO users (userid, bank, wallet) VALUES (?,?,?)",(ctx.author.id,0,0,''))
                else:
                    if amount != 'all' or "max":
                        if amount > rows[1]:
                            em = discord.Embed(title = "<:fail:761292267360485378> Deposit failed!", color = ctx.author.color)
                            em.add_field(name = "Reason:", value = "You don't even have that much money!")
                            em.add_field(name = "Next Steps:", value = "Get richer next time!")
                            em.set_thumbnail(url = ctx.author.avatar_url)
                            await ctx.send(embed = em)
                            return
                        elif amount <= 0:
                            em = discord.Embed(title = "<:fail:761292267360485378> Deposit failed!", color = ctx.author.color)
                            em.add_field(name = "Reason:", value = "Amount was too low!")
                            em.add_field(name = "Next Steps:", value = "Type a positive integer next time!")
                            em.set_thumbnail(url = ctx.author.avatar_url)
                            await ctx.send(embed = em)
                            return
                        else:
                            await cursor.execute("UPDATE users SET wallet = ?, bank = ? WHERE userid = ?",(rows[1] - amount,rows[0] + amount,ctx.author.id,))
                            em = discord.Embed(title = "<:success:761297849475399710> Deposit successful!", color = ctx.author.color)
                            em.add_field(name = ":bank: Amount Deposited:", value = f"{amount} :coin:")
                            em.set_thumbnail(url = ctx.author.avatar_url)
                            await ctx.send(embed = em)
                    else:
                        await cursor.execute("UPDATE users SET wallet = ?, bank = ? WHERE userid = ?",(0,rows[0] + rows[1],ctx.author.id,))
                        em = discord.Embed(title = "<:success:761297849475399710> Deposit successful!", color = ctx.author.color)
                        em.add_field(name = ":bank: Amount Deposited:", value = f"{rows[1]} :coin:")
                        em.set_thumbnail(url = ctx.author.avatar_url)
                        await ctx.send(embed = em)
                    await connection.commit()

    @deposit.error
    async def deposit_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = f"<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = f"Reason:", value = "You can always deposit later idiot!")
            em.add_field(name = "Try again in:", value = "{:.2} seconds".format(error.retry_after))
            em.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @commands.command(aliases=['with'])
    @commands.cooldown(1,5,commands.BucketType.user)
    async def withdraw(self,ctx,amount = None):
        if amount == None:
            em = discord.Embed(title = "<:fail:761292267360485378> Withdraw failed!", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "You didn't provide an amount. Or go to school!")
            em.add_field(name = "Next Steps:", value = "Next time try to type an amount too!")
            em.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = em)
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
                            em = discord.Embed(title = "<:fail:761292267360485378> Withdraw failed!", color = ctx.author.color)
                            em.add_field(name = "Reason:", value = "You don't even have that much money!")
                            em.add_field(name = "Next Steps:", value = "Get richer next time!")
                            em.set_thumbnail(url = ctx.author.avatar_url)
                            await ctx.send(embed = em)
                            return
                        elif amount <= 0:
                            em = discord.Embed(title = "<:fail:761292267360485378> Withdraw failed!", color = ctx.author.color)
                            em.add_field(name = "Reason:", value = "Amount was too low!")
                            em.add_field(name = "Next Steps:", value = "Type a positive integer next time!")
                            em.set_thumbnail(url = ctx.author.avatar_url)
                            await ctx.send(embed = em)
                            return
                        else:
                            await cursor.execute("UPDATE users SET wallet = ?, bank = ? WHERE userid = ?",(rows[1] + amount,rows[0] - amount,ctx.author.id,))
                            em = discord.Embed(title = "<:success:761297849475399710> Deposit successful!", color = ctx.author.color)
                            em.add_field(name = ":bank: Amount Deposited:", value = f"{amount} :coin:")
                            em.set_thumbnail(url = ctx.author.avatar_url)
                            await ctx.send(embed = em)
                    else:
                        await cursor.execute("UPDATE users SET wallet = ?, bank = ? WHERE userid = ?",(rows[1] + rows[0],0,ctx.author.id,))
                        em = discord.Embed(title = "<:success:761297849475399710> Deposit successful!", color = ctx.author.color)
                        em.add_field(name = ":bank: Amount Deposited:", value = f"{rows[0]} :coin:")
                        em.set_thumbnail(url = ctx.author.avatar_url)
                        await ctx.send(embed = em)
                await connection.commit()

    @withdraw.error
    async def withdraw_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = f"<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = f"Reason:", value = "You can always withdraw later idiot!")
            em.add_field(name = "Try again in:", value = "{:.2} seconds".format(error.retry_after))
            em.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = em)

    @commands.command()
    @commands.is_owner()
    @commands.cooldown(1, 300, BucketType.user)
    async def devwith(self, ctx, amount = None):
        if amount is None:
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
                        await cursor.execute("UPDATE users SET wallet = ?, bank = ? WHERE userid = ?", (rows[1] + amount, rows[0], ctx.author.id))
            await connection.commit()
        await ctx.send(f"Gave you {amount} :dollar:")

    @devwith.error
    async def devwith_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = f"<:fail:761292267360485378> Slow it down C'mon", color = ctx.author.color)
            em.add_field(name = f"Reason:", value = f"Your already too rich, Lord {ctx.author.mention}!")
            em.add_field(name = "Try again in:", value = "{:.2} seconds".format(error.retry_after))
            em.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = em)


    @commands.command(aliases=['send', "share"])
    @commands.cooldown(1,30,commands.BucketType.user)
    async def give(self,ctx,member : discord.Member = None, amount = None):
        if amount == None:
            em = discord.Embed(title = "<:fail:761292267360485378> Give failed!", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "You didn't provide an amount. Or go to school!")
            em.add_field(name = "Next Steps:", value = "Next time try to type an amount too!")
            em.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = em)
            return
        if member is None:
            em = discord.Embed(title = "<:fail:761292267360485378> Give failed!", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "You didn't provide a valid member. Get better at discord!")
            em.add_field(name = "Next Steps:", value = "Next time try to type a valid member too!")
            em.set_thumbnail(url = ctx.author.avatar_url)
            await ctx.send(embed = em)
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
                    if amount == "all":
                        amount = rows[1]

                    if amount > rows[1]:
                        em = discord.Embed(title = "<:fail:761292267360485378> Withdraw failed!", color = ctx.author.color)
                        em.add_field(name = "Reason:", value = "You don't even have that much money!")
                        em.add_field(name = "Next Steps:", value = "Get richer next time!")
                        em.set_thumbnail(url = ctx.author.avatar_url)
                        await ctx.send(embed = em)
                        return
                    elif amount <= 0:
                        em = discord.Embed(title = "<:fail:761292267360485378> Withdraw failed!", color = ctx.author.color)
                        em.add_field(name = "Reason:", value = "Amount was too low!")
                        em.add_field(name = "Next Steps:", value = "Type a positive integer next time!")
                        em.set_thumbnail(url = ctx.author.avatar_url)
                        await ctx.send(embed = em)
                        return
                    else:
                        await cursor.execute("UPDATE users SET wallet = ?, bank = ? WHERE userid = ?", (rows[1] - amount, rows[0], ctx.author.id))

                await connection.commit()

        async with aiosqlite.connect("./data/economy.db") as connection:
            async with connection.cursor() as cursor:
                await cursor.execute("SELECT bank, wallet FROM users WHERE userid = ?",(member.id,))
                membal = await cursor.fetchone()
                if not membal:
                    await cursor.execute("INSERT INTO users (userid, bank, wallet) VALUES (?,?,?)",(ctx.author.id,0,0,))
                else:
                    await cursor.execute("UPDATE users SET wallet = ?, bank = ? WHERE userid = ?", (membal[1] + amount, membal[0], member.id))
                await connection.commit()

        await ctx.send(f"{ctx.author.mention} gave {member.mention} {amount} :dollar:!\n:tada:")

def setup(client):
    client.add_cog(Economy(client))
