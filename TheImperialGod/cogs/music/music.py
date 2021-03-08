import discord
from discord.ext import commands
import youtube_dl

youtube_dl.utils.bug_reports_message = lambda: ''
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.Cog.listener()
    async def on_ready(self):
        print("Moosik is ready, time to jam to some beats!")
    
    @commands.command()
    async def join(self, ctx, *, reason = None):
        channel = ctx.message.author.voice.channel
        await channel.connect()

        em = discord.Embed(title = "<:success:761297849475399710> Join Successful", color = ctx.author.color)
        em.description = "I have successfully joined {}!".format(channel.name)
        em.add_field(name = "Reason:", value = f"`{reason}`")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        em.set_footer(text = "invite me ;)", icon_url = ctx.author.avatar_url)
        await ctx.send(embed = em)

    @commands.command(aliases=["leab", "leav", "getoff", "disconnect"])
    async def leave(self, ctx, *, reason= None):
        em = discord.Embed(title = "<:success:761297849475399710> Leave Successful", color = ctx.author.color)
        em.description = "I have successfully left all voice channels!"
        em.add_field(name = "Reason:", value = f"`{reason}`")
        em.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        em.set_footer(text = "invite me ;)", icon_url = ctx.author.avatar_url)
        await ctx.send(embed = em)

        voice_client = ctx.message.guild.voice_client
        await voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, url):
        failEmbed = discord.Embed(title = "<:fail:761292267360485378> Join Failed!", color = ctx.author.color)
        failEmbed.description = "You are not connected to a voice channel!"
        failEmbed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        failEmbed.set_footer(text = "get gud, bot", icon_url = ctx.author.avatar_url)

        exceptionEmbed = discord.Embed(title = "<:fail:761292267360485378> Join Failed!", color = ctx.author.color)
        exceptionEmbed.description = "You must provide a valid URL for this to work! We don't support plain search until now!"
        exceptionEmbed.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)
        exceptionEmbed.set_footer(text = "get gud, bot", icon_url = ctx.author.avatar_url)

        if not ctx.author.voice:
            return await ctx.send(embed = failEmbed)

        server = ctx.message.guild
        voice_channel = server.voice_client

        async with ctx.typing():
            try:
                player = await YTDLSource.from_url(url, loop=self.client.loop)
                voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
            except:
                await ctx.send(embed = exceptionEmbed)
                return
        await ctx.send('**Now playing:** {}'.format(player.title))
    
    @commands.command()
    async def pause(self, ctx):
        server = ctx.message.guild
        voice_channel = server.voice_client

        voice_channel.pause()

    @client.command()
    async def resume(self, ctx):
        server = ctx.message.guild
        voice_channel = server.voice_client

        voice_channel.resume()


def setup(client):
    client.add_cog(Music(client))