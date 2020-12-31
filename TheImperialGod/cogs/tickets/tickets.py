import discord
from discord.ext import commands
import asyncio
from discord.ext.commands import cooldown, BucketType
import json

class Tickets(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Tickets are ready!")

    @commands.command()
    @cooldown(1, 60, BucketType.user)
    async def new(self, ctx, *, reason = None):
        em = discord.Embed(title = "Confirm New Ticket", color =  ctx.author.color)
        em.add_field(name = "Reason:", value = "We don't want people to spam!")
        em.add_field(name = "Steps to do:", value = "Type `confirm` in the chat to confirm this ticket!")
        msg = await ctx.send(embed = em)

        def msg_check(m):
            return m.author == ctx.author and m.channel  == ctx.channel

        try:
            msg = await self.client.wait_for('message', timeout = 15.0, check= msg_check)
        except:
            em = discord.Embed(title = "<:fail:761292267360485378> New Ticket Failed!", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "You took too long!")
            em.add_field(name = "Cooldown", value = "1 minute more!")
            await ctx.send(embed = em)
        else:
            if msg.content != "confirm":
                em = discord.Embed(title = "<:fail:761292267360485378> New Ticket Failed!", color = ctx.author.color)
                em.add_field(name = "Reason:", value = "You did not want to create one!")
                em.add_field(name = "Cooldown", value = "1 minute more!")
                await ctx.send(embed = em)

            else:
                channelname = "ticket-{}".format(ctx.author.name)
                ticket = True
                for echannel in ctx.guild.channels:
                    if echannel.name == channelname:
                        ticket = False

                if not ticket:
                    await ctx.send("You already have a ticket! Please contact staff on your already made ticket!")
                    return  

                warning = f"""{ctx.author.mention} it is good to provide a reason for your inquires with the EMPIRE\nNext time try `imp new <reason>`
                """
                tickets = await self.get_tickets()
                guild = ctx.guild
                author = ctx.author
                # Logic
                if str(ctx.guild.id) not in tickets:
                    em = discord.Embed(title = "<:fail:761292267360485378> New Failed",color = ctx.author.color)
                    em.add_field(name = "Reason:", value = "Tickets are not setup!")
                    em.add_field(name = "Next Steps:", value = "Ask a admin to set this up, `imp addticketrole @role`")
                    await ctx.send(embed = em)
                    return
                # Getting the role made!
                ticketrole = tickets[str(ctx.guild.id)]["ticketrole"]
                role_id = int(ticketrole)
                helper_role = ctx.guild.get_role(role_id)
                # Setting up the Channel
                channel = await ctx.guild.create_text_channel(f'ticket-{ctx.author.name}')
                # Creating the embed
                em = discord.Embed(title = f"<:success:761297849475399710> New ticket", color = ctx.author.color)
                em.add_field(name = "Ticket Channel:", value= f"{channel.mention}")
                em.add_field(name = "Description:", value = "Staff will be with your shortly")
                em.add_field(name = "Member:", value = f"{ctx.author.mention}")
                em.add_field(name = "Reason:", value = f"`{reason}`")
                # Perms
                # Make sure the author can type!
                await channel.set_permissions(ctx.author, read_messages = True, send_messages = True)
                # Make sure everyone else should not be able to see anything, cause it should be private
                await channel.set_permissions(ctx.guild.default_role, read_messages = False, send_messages = False)
                # And now make sure the helper_role should see this, incase the owner is busy
                await channel.set_permissions(helper_role, read_messages = True, send_messages = True)
                """
                and before you ask, how are we gonna set our Perms
                if we can manage_channels (create a channel), then hell ye
                we can speak, we dont need to actually set perms for ourselves
                """
                # Sending the embed
                await channel.send(embed = em)
                if reason == None:
                    await channel.send(warning)
                await ctx.send(f"Created the ticket! Check {channel.mention}")

    @new.error
    async def new_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title = "<:fail:761292267360485378> New Error", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "If your trying to spam the server then get off!")
            em.add_field(name = "Try again in:", value = "{:.2f}s".format(error.retry_after))
            await ctx.send(embed = em)

    @commands.command()
    @commands.has_permissions(manage_guild = True)
    async def addticketrole(self, ctx, role : discord.Role = None):
        if role == None:
            await ctx.send("You need to provide a valid role!")
            return

        tickets = await self.get_tickets()
        em = discord.Embed(title= "<:success:761297849475399710> Added ticketrole", color = ctx.author.color)
        guild = ctx.guild
        author = ctx.author
        if str(ctx.guild.id) not in tickets:
            em.add_field(name = "Switch:", value = f"`None` => {role.mention}")
            tickets[str(guild.id)] = {}
            tickets[str(guild.id)]["ticketrole"] = int(role.id)
        else:
            role_id = tickets[str(guild.id)]["ticketrole"]
            tickets[str(guild.id)]["ticketrole"] = int(role.id)
            em.add_field(name = "Role:", value = f"{role.mention}")
        em.add_field(name = "Features:", value = "Users can now type `imp new <reason>`")
        await ctx.send(embed = em)

        # Updating the database
        with open("./data/tickets.json", "w") as f:
            json.dump(tickets, f)

    @addticketrole.error
    async def addticketrole_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em = discord.Embed(title = "<:fail:761292267360485378> Ticket Error", color = ctx.author.color)
            em.add_field(name = "Reason:", value = "You don't have the perms")
            em.add_field(name = "Perms:", value = "`Manage Server permission missing!`")
            await ctx.send(embed = em)

    async def get_tickets(self):
        with open("./data/tickets.json", "r") as f:
            tickets = json.load(f)
        return tickets

    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def close(self, ctx):
        channel = ctx.channel
        name = channel.name
        if name.startswith("ticket-"):
            await channel.delete()
        else:
            await ctx.send("Not a previous ticket channel!")
            return

def setup(client):
    client.add_cog(Tickets(client))
