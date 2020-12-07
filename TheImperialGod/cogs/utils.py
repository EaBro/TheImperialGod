import discord
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
import random
import asyncio

class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def coinflip(self, ctx):
        list = ["Heads", "Tails"]
        embed = discord.Embed(title = "Coinflip by {}".format(ctx.author.name), color = ctx.author.color)
        res = random.choice(list)
        embed.add_field(name = "We rolled a:", value = f"`{res}`")
        embed.set_image(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnWL81FKwiyIak8DR8azPVHryuOFNlS5esVw&usqp=CAU")
        await ctx.send(embed = embed)
    
    @commands.command()
    async def random_number(self, ctx, range1: int, range2: int):
        bool = True
        try:
            #because someone will be an idiot!
            if end > 9223372036854775807:
                await ctx.send(':warning: ending number too big!')
                bool = False
            if end <= start:
                await ctx.send(':warning: ending number must be larger than starting number!')
                bool = False
        except:
            pass
        if bool == True:
            embed = discord.Embed(title = "Random Number by {}".format(ctx.author.name), color = ctx.author.color)
            embed.add_field(name = "Number:", value = random.randint(start, end))
            await ctx.send(embed = embed)
        else:
            await ctx.send("Sorry, you were an idiot! Thus its not for you!")

    @random_number.error
    async def random_number_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title = "Missing Required Argument", color = ctx.author.color)
            embed.add_field(name = "Error:", value = "You have missed an argument")
            embed.add_field(name = "Correct usage:", value = "`imp random_number <first_range> <last_range>`")

    @commands.command()
    async def code(self, ctx, *, msg = None):
        if msg == None:
            await ctx.send("You have to provide a valid message:\n `imp code hello there`")

        await ctx.send("```" + msg.replace("`", "") +("```"))
    
    @commands.command()
    async def guess(self, ctx, start, end, guess):
        async with ctx.channel.typing():
            bool = True
            start = int(start)
            end = int(end)
            try:
                if end > 10000000000:
                    await ctx.send(':warning: ending number too big!')
                    bool = False
                if end <= start:
                    await ctx.send(':warning: ending number must be larger than starting number!')
                    bool = False
            except:
                pass
            if bool == True:
                number = random.randint(start, end)
                embed = discord.Embed(title = "Guess Game by {}".format(ctx.author.name), color = ctx.author.color)
                embed.add_field(name = "Number:", value = number)
                if guess == number:
                    embed.add_field(name = "You Won!", value = "The number was {} and your guess was {}".format(number, guess))
                else:
                    embed.add_field(name = "You Lost!", value = "The number was {} and your guess was {}".format(number, guess))
                await ctx.send(embed = embed)
            else:
                await ctx.send("Sorry, you were an idiot! Thus its not for you!")

    @guess.error
    async def guess_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(title = "Missing Required Argument", color = ctx.author.color)
            embed.add_field(name = "Error:", value = "You have missed an argument")
            embed.add_field(name = "Correct usage:", value = "`imp guess <first_range> <last_range> <guess>`")
            await ctx.send(embed = embed)

    @commands.command()
    async def thank(self, ctx, member : discord.Member, *, reason = None):
        if reason == None:
            await ctx.send(f"{ctx.author.mention} thanked {member} for no reason at all!")
        else:
            await ctx.send(f"{ctx.author.mention} thanks {member} for {reason} reason.")
        try:
            if reason != None:
                await member.send(f"You were thanked in {ctx.guild.name} by {ctx.author.name}!\nReason: {reason}")
            else:
                await member.send(f"You were thanked in {ctx.guild.name} by {ctx.author.name}")
        except:
            pass

    @commands.command()
    async def reverse(self, ctx,*,msg):
        try:
            msg = list(msg)
            msg.reverse()
            print(msg)
            send = ''.join(msg)
            await ctx.send(send)
        except Exception:
            traceback.print_exc()

    @commands.command()
    async def eightball(self, ctx, *, question):
        responses = [
        'That is certain',
        'Of course',
        'My sources say yes',
        'Try again',
        'Bad internet try again',
        'No',
        'Never',
        'Always true',
        'My sources say no!'
        ]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

    @commands.command()
    async def poll(self, ctx, *, message):
        embed = discord.Embed(title = f"{ctx.author.name}'s Poll", color = ctx.author.color)
        embed.add_field(name = f"{message}", value = "Share your thoughts about this topic")

        my_msg = await ctx.send(embed = embed)
        await my_msg.add_reaction("✅")
        await my_msg.add_reaction("❌")

    @commands.command(aliases = ['str', 'show_tp', 's_toprole'])
    async def show_toprole(self, ctx, *, member: discord.Member=None):
        if member is None:
            member = ctx.author
            await ctx.send(f'The top role for {member.display_name} is {member.top_role.name}')
        else:
            await ctx.send(f'The top role for {member.display_name} is {member.top_role.name}')

    @commands.command(aliases = ['generator','password','passwordgenerator', 'passwordgen'])
    async def _pass(self, ctx,amt : int = 8):
        try:
            nwpss = []
            lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
            'n','o','p','q','r','s','t','u','v','w','x','y','z','!','@',
            '#','$','%','^','&','*','(',')','-','_','+','=','{',",",'}',']',
            '[',';',':','<','>','?','/','1','2','3','4','5','6','7','8','9','0'
            ,'`','~','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'
            ,'Q','R','S','T','U','V','W','X','Y','Z'] #all char
            for x in range(amt):
                newpass = random.choice(lst)
                nwpss.append(newpass)

            fnpss = ''.join(nwpss)
            await ctx.send(f'{ctx.author} attempting to send you the genereated password in dms.')
            await ctx.author.send(f'Password Generated: {fnpss}')
        except Exception as e:
            print(e)
    
    @commands.command(aliases = ["av"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def avatar(self, ctx, *, member: discord.Member = None):
        if member == None:
            em = discord.Embed(description=f"[**{ctx.author.name}'s Avatar**]({ctx.author.avatar_url})", colour=ctx.author.color, timestamp =ctx.message.created_at)
            em.set_image(url= ctx.author.avatar_url)
            em.set_footer(icon_url = ctx.author.avatar_url, text = f"Requested by {ctx.author}")

            await ctx.send(embed=em)

            return

        else:
            em = discord.Embed(description=f"[**{member.name}'s Avatar**]({member.avatar_url})", colour = member.color, timestamp =ctx.message.created_at)
            em.set_image(url=member.avatar_url)
            em.set_footer(icon_url = member.avatar_url, text = f"Requested by {ctx.author}")

            await ctx.send(embed=em)

            return
    
    @commands.command()
    async def treat(ctx, member:discord.Member):
        if member == ctx.author:
            await ctx.send("You can't treat youself!")
            return
        embed=discord.Embed(title = "Treats!",
            description=f'You offered {member.name} a treat! {member.mention} react to the emoji below to accept!',
            color=0x006400
        )
        timeout=int(15.0)
        message = await ctx.channel.send(embed=embed)

        await message.add_reaction('🍫')
        
        def check(reaction, user):
            return user == member and str(reaction.emoji) == '🍫'
            
        try:
            reaction, user = await client.wait_for('reaction_add', timeout=timeout, check=check)
            
        except asyncio.TimeoutError:
            msg=(f"{member.mention} didn't accept the treat in time!!")
            await ctx.channel.send(msg)

        else:
            await ctx.channel.send(f"{member.mention} You have accepted {ctx.author.name}'s offer!")
    
def setup(client):
    client.add_cog(Utils(client))