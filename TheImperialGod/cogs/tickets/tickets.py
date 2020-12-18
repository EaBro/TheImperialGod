import discord
from discord.ext import commands
import asyncio
from discord.ext.commands import cooldown, BucketType

class Tickets(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Tickets are ready!")

    @commands.command()
    @cooldown(1, 60, BucketType.user)
    async def new(self, ctx, *, reason = None):
        tickets = await self.get_tickets()
        # Logic
        if str(ctx.guild.id) not in tickets:
            await ctx.send("Ask a moderator to set this up with: `imp addticketrole @role`")
            return
        # Getting the role made!
        ticketrole = tickets[str(ctx.guild.id)]["ticketrole"]
        role_id = int(ticketrole)
        helper_role = ctx.guild.get_role(role_id)
        # Creating the embed
        em = discord.Embed(title = f"<:success:761297849475399710> New ticket", color = ctx.author.color)
        em.add_field(name = "Ticket Channel:", value= f"{channel.mention}")
        em.add_field(name = "Description:", value = "Staff will be with your shortly")
        em.add_field(name = "Member:", value = f"{ctx.author.mention}")
        em.add_field(name = "Reason:", value = f"`{reason}`")
        # Setting up the channel
        channel = await guild.create_text_channel(f'ticket-{ctx.author.name}')
        await channel.set_permissions(ctx.author, read_messages = True, send_messages = True)
        await channel.set_permissions(helper_role, read_messages = True, send_messages = True)
        # Sending the embed
        await channel.send(embed = em)

    @commands.command()
    @commands.has_permissions(manage_guild = True)
    async def addticketrole(self, ctx, role : discord.Role):
        return

    async def get_tickets(self):
        with open("./data/tickets.json", "r") as f:
            tickets = json.load(f)
        return tickets

def setup(client):
    client.add_cog(Tickets(client))
