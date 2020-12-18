import discord
from discord import Embed
from discord.ext import commands
import json
from discord.ext.commands import cooldown
from discord.ext.commands import BucketType
import random

class Economy(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    async def get_bank_data(self):
        with open("./data/mainbank.json", "r") as f:
            users = json.load(f)
        return users
    
    async def open_account(self, user):
        users = await self.get_bank_data()
        if str(user.id) in users:
            return False
        else:
            users[str(user.id)] = {}
            users[str(user.id)]["wallet"] = 0
            users[str(user.id)]["bank"] = 0
            return True

        with open("./data/mainbank.json", "w") as f:
            json.dump(users,f)

    async def update_bank(self, user, change = 0, mode = 'wallet'):
        users = await self.get_bank_data()
        await self.open_account(user)

        users[str(user.id)][mode] += change

        with open("./data/mainbank.json", "w") as f:
            json.dump(users,f)
    
    @commands.command(aliases=["bal"])
    @cooldown(1, 5, BucketType.user)
    async def balance(self, ctx, user : discord.Member = None):
        if user == None:
            user = ctx.author
        users = await self.get_bank_data()
        await self.open_account(user)

        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]

        em = discord.Embed(title = f"{user.name}'s Balance",color = ctx.author.color)
        em.add_field(name = "Wallet Balance:", value = f"{wallet_amt} :coin:")
        em.add_field(name = "Bank Balance:", value = f"{bank_amt} :coin:")
        await ctx.send(embed = em)
    
    @commands.command()
    @cooldown(1, 15, BucketType.user)
    async def beg(self, ctx):
        users = await self.get_bank_data()
        await self.open_account(ctx.author)
        earnings = random.randint(1, 100)
        await self.update_bank(ctx.author, earnings)

        wallet_amt = users[str(ctx.author.id)]["wallet"]
        bank_amt = users[str(ctx.author.id)]["bank"]

        em = discord.Embed(title = f"{ctx.author.name} begs",color = ctx.author.color)
        em.add_field(name = "Wallet Balance:", value = f"{wallet_amt} :coin:")
        em.add_field(name = "Bank Balance:", value = f"{bank_amt} :coin:")
        em.add_field(name = f"Amount Earned:", value = f"{earnings} :coin:", inline = False)
        await ctx.send(embed = em)
    
    @beg.error
    async def beg_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = Embed(title = "<:fail:761292267360485378> Beg Error", color = ctx.author.color)
            em.add_field(name = 'Reason:', value = 'Stop begging so much, makes you look poor!')
            em.add_field(name = "Try again in:", value = "{:.2}s".format(error.retry_after))
            await ctx.send(embed = em)

    @commands.command(aliases=["with"])
    @cooldown(1,3, BucketType.user)
    async def withdraw(self, ctx, amount = None):
        if amount == None:
            await ctx.send("Type an amount!")
            return
        
        users = await self.get_bank_data()
        await self.open_account(ctx.author)
        if amount == 0 or amount < 0:
            await ctx.send("Amount must be positive!")
            return

        if amount > users[str(ctx.author.id)]["bank"]:
            await ctx.send("You don't even have that much money!")
            return

        await self.update_bank(ctx.author, amount)
        await self.update_bank(ctx.author, -1*amount, "bank")

        wallet_amt = users[str(ctx.author.id)]["wallet"]
        bank_amt = users[str(ctx.author.id)]["bank"]
        em = discord.Embed(title = f"{ctx.author.name} withdraws!",color = ctx.author.color)
        em.add_field(name = "Wallet Balance:", value = f"{wallet_amt} :coin:")
        em.add_field(name = "Bank Balance:", value = f"{bank_amt} :coin:")
        em.add_field(name = f"Amount Withdrawn:", value = f"{amount} :coin:", inline = False)
        await ctx.send(embed = em)

    @withdraw.error
    async def withdraw_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = Embed(title = "<:fail:761292267360485378> Withdraw Error", color = ctx.author.color)
            em.add_field(name = 'Reason:', value = 'Stop withdrawing so much, makes you look like a tax accountant!')
            em.add_field(name = "Try again in:", value = "{:.2}s".format(error.retry_after))
            await ctx.send(embed = em)

    @commands.command(aliases=["dep"])
    @cooldown(1, 3, BucketType.user)
    async def deposit(self, ctx, amount = None):
        if amount == None:
            await ctx.send("Type an amount!")
            return
        
        users = await self.get_bank_data()
        await self.open_account(ctx.author)
        if amount == 0 or amount < 0:
            await ctx.send("Amount must be positive!")
            return

        if amount > users[str(ctx.author.id)]["wallet"]:
            await ctx.send("You don't even have that much money!")
            return

        await self.update_bank(ctx.author, -1*amount)
        await self.update_bank(ctx.author, amount, "bank")

        wallet_amt = users[str(ctx.author.id)]["wallet"]
        bank_amt = users[str(ctx.author.id)]["bank"]
        em = discord.Embed(title = f"{ctx.author.name} deposits!",color = ctx.author.color)
        em.add_field(name = "Wallet Balance:", value = f"{wallet_amt} :coin:")
        em.add_field(name = "Bank Balance:", value = f"{bank_amt} :coin:")
        em.add_field(name = f"Amount Deposited:", value = f"{amount} :coin:", inline = False)
        await ctx.send(embed = em)
    
    @deposit.error
    async def deposit_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = Embed(title = "<:fail:761292267360485378> Deposit Error", color = ctx.author.color)
            em.add_field(name = 'Reason:', value = 'Stop depositing so much, makes you look like a tax accountant!')
            em.add_field(name = "Try again in:", value = "{:.2}s".format(error.retry_after))
            await ctx.send(embed = em)
    
    @commands.command()
    @cooldown(1, 30, BucketType.user)
    async def slots(self, ctx, amount = None):
        if amount == None:
            await ctx.send("Type an amount!")
            return
        
        users = await self.get_bank_data()
        await self.open_account(ctx.author)
        if amount == 0 or amount < 0:
            await ctx.send("Amount must be positive!")
            return

        if amount > users[str(ctx.author.id)]["wallet"]:
            await ctx.send("You don't even have that much money!")
            return

        final = []
        for i in range(0, 3):
            a = random.choice(["👻", "👾", "🔱"])
            final.append(a)
        
        if final[0] == final[1] or final[1] == final[2] or final[0] == final[2]:
            winTrue = True
            await self.update_bank(ctx.author, amount)
        else:
            winTrue = False
            await self.update_bank(ctx.author, -1*amount)
        
        wallet_amt = users[str(ctx.author.id)]["wallet"]
        bank_amt = users[str(ctx.author.id)]["bank"]
        em = discord.Embed(title = f"{ctx.author.name} bets!",color = ctx.author.color)
        em.add_field(name = "Wallet Balance:", value = f"{wallet_amt} :coin:")
        em.add_field(name = "Bank Balance:", value = f"{bank_amt} :coin:")
        em.add_field(name = f"Amount bet:", value = f"{amount} :coin:", inline = False)
        em.add_field(name = "Result:", value = str(final))
        if winTrue:
            em.add_field(name = "Profit:", value = f"{amount} :coin:")
        else:
            em.add_field(name = "Loss", value = f"{amount} :coin:")
        await ctx.send(embed = em)
    
    @slots.error
    async def slots_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = Embed(title = "<:fail:761292267360485378> Slots Error", color = ctx.author.color)
            em.add_field(name = 'Reason:', value = 'If you would then you would lose all your money!')
            em.add_field(name = "Try again in:", value = "{:.2}s".format(error.retry_after))
            await ctx.send(embed = em)

    @commands.command(aliases=["share", "send"])
    @cooldown(1, 10, BucketType.user)
    async def give(self, ctx, member : discord.Member = None,amount = None):
        if amount == None:
            await ctx.send("Type an amount!")
            return
        if member == None:
            await ctx.send("Type a person to send money to!")
            return
        
        users = await self.get_bank_data()
        await self.open_account(ctx.author)
        await self.open_account(member)
        if amount == 0 or amount < 0:
            await ctx.send("Amount must be positive!")
            return

        if amount > users[str(ctx.author.id)]["wallet"]:
            await ctx.send("You don't even have that much money!")
            return

        await self.update_bank(ctx.author, -1*amount)
        await self.update_bank(member, amount)

    @give.error
    async def give_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = Embed(title = "<:fail:761292267360485378> Give Error", color = ctx.author.color)
            em.add_field(name = 'Reason:', value = 'If you give all your money, you would become poor!')
            em.add_field(name = "Try again in:", value = "{:.2}s".format(error.retry_after))
            await ctx.send(embed = em)

    @commands.command(aliases=["steal", "walletrob"])
    @cooldown(1, 60, BucketType.user)
    async def rob(self, ctx, member : discord.Member = None):
        if member == None:
            await ctx.send("Type a person to rob!")
            return
        
        users = await self.get_bank_data()
        await self.open_account(ctx.author)
        await self.open_account(member)

        if users[str(ctx.author.id)]["wallet"] < 500:
            await ctx.send("You don't even 500 coins!")
            return
        if users[str(member.id)]["wallet"] < 500:
            await ctx.send("Victim doesn't have 500 coins not worth it!")
            return
        if member.bot:
            await ctx.send("You can't rob a bot back of my kind!")
            return
        
        wallet_amt = users[str(member.id)]["wallet"]
        amount = random.randint(1, wallet_amt)

        await self.update_bank(ctx.author, amount)
        await self.update_bank(member, -1*amount)

        await ctx.send("You gained `{}` :coin: from that!".format(amount))

    @rob.error
    async def rob_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = Embed(title = "<:fail:761292267360485378> Rob Error", color = ctx.author.color)
            em.add_field(name = 'Reason:', value = 'Pesky robber! You need time to plan your next attack!')
            em.add_field(name = "Try again in:", value = "{:.2}s".format(error.retry_after))
            await ctx.send(embed = em)

def setup(client):
    client.add_cog(Economy(client))