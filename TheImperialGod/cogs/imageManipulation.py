import discord
from discord.ext import commands
import random
#image manipulation
from PIL import Image
from io import BytesIO

class ImageManipulation(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Image Manipulation - Done")
    
    @commands.command()
    async def wanted(self, ctx, user : discord.Member = None):
        if user == None:
            user = ctx.author
        
        wanted = Image.open("./assets/wanted.jpg")
        asset = user.avatar_url_as(size = 128)

        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((88, 88))
        wanted.paste(pfp, (47, 84))

        wanted.save("./assets/profile.jpg")
        await ctx.send(file = discord.File("./assets/profile.jpg"))
    

def setup(client):
    client.add_cog(ImageManipulation(client))