import discord
import json
from discord.ext import commands

class Points(commands.Cog):
    def __init__(self, client):
        self.client = client 
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Points are ready!")
    
    @commands.command()
    async def points(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author
        
        with open("./data/points.json", "r") as f:
            points = json.load(f)
        
        if str(ctx.guild.id) not in points:
            points[str(ctx.guild.id)] = {}
        
        if str(member.id) not in points[str(ctx.guild.id)]:
            points[str(ctx.guild.id)][str(member.id)] = 0  
            member_points = points[str(ctx.guild.id)][str(member.id)]        
        else:
            member_points = points[str(ctx.guild.id)][str(member.id)]

        em = discord.Embed(title = f"<:success:761297849475399710> {member.name}'s Points", color = member.color, description = f"This embed shows how many points {member.mention} has!")
        em.set_thumbnail(url = member.avatar_url)
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        em.add_field(name = "Points:", value = f"`{member_points}`")
        if member_points > 5000:
            em.set_footer(text = f"Oi {member.name} rich as hell boi", icon_url = member.avatar_url)
        await ctx.send(embed = em)
    
        with open("./data/points.json", "w") as f:
            json.dump(points, f)
    
    @commands.command()
    async def givepoints(self, ctx, member: discord.Member = None, points: int = None, *, reason: str = None):
        if member is None:
            await ctx.send("Give me a member to give points to!")
            return
        elif points is None:
            await ctx.send("Give some valid points!")
            return 
        
        with open("./data/points.json", "r") as f:
            points = json.load(f)
        
        if str(ctx.guild.id) not in points:
            points[str(ctx.guild.id)] = {} 
        
        if str(ctx.author.id) not in points[str(ctx.guild.id)]:
            points[str(ctx.guild.id)][str(ctx.author.id)] = 0
            member_points = points[str(ctx.guild.id)][str(ctx.author.id)]
        else:
            member_points = int(points[str(ctx.guild.id)][str(ctx.author.id)])
        if member_points < points:
            await ctx.send("You don't even have {} points".format(points))
            return
        
        if points <= 0:
            await ctx.send("Points have to be greater than 0!")
            return 

        em = discord.Embed(title = f"{member.name}'s Points", color = ctx.author.color)
        em.add_field(name = "From:", value = f"{ctx.author.mention}")
        em.add_field(name = "To:", value = f"{member.mention}")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        em.description = f"Successfully transferred `**{points}**` points to {member.mention}"
        
        points[str(ctx.guild.id)][str(ctx.author.id)] -= points
        if str(member.id) not in points[str(ctx.guild.id)]:
            points[str(ctx.guild.id)][str(member.id)] = points
            em.add_field(name = "Points:", value = f"`0` => `{points}`", inline = True)
        else:
            old_points = points[str(ctx.guild.id)][str(member.id)]
            em.add_field(name = "Points:", value = f"`{old_points}` => `{old_points + points}`", inline = True)
            points[str(ctx.guild.id)][str(member.id)] += points
        
        with open("./data/points.json", "w") as f:
            json.dump(points, f)    

        await ctx.send(embed = em)

def setup(client):
    client.add_cog(Points(client))