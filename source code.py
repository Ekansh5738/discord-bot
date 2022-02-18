import discord
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
import youtube_dl
import asyncio
from random import choice
from webserver import keep_alive







"""



import pyttsx3

engine = pyttsx3.init('espeaks')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


"""






import wikipedia
"""import speech_recognition as sr

def takeCommand():
    # it takes microphone input and string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognistion...")
        query = r.recognize_google(audio, language='en-In')
        print(f"User said : {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again Please...")
        return "not able to understand"
    return query  
"""

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


client = commands.Bot(command_prefix='?')

status = ['Jamming out to music!', 'Eating!', 'Sleeping!']

@client.event
async def on_ready():
    change_status.start()
    print('Bot is online!')

@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f'Welcome {member.mention}!  Ready to jam out? See `?help` command for details!')

@client.command(name='ping', help='This command returns the latency')
async def ping(ctx):
    await ctx.send(f'**Pong!** Latency: {round(client.latency * 1000)}ms')

@client.command(name='hello', help='This command returns a random welcome message')
async def hello(ctx):
    responses = ['***grumble*** Why did you wake me up?', 'Top of the morning to you lad!', 'Hello, how are you?', 'Hi', '**Wasssuup!**']
    await ctx.send(choice(responses))

@client.command(name='die', help='This command returns a random last words')
async def die(ctx):
    responses = ['why have you brought my short life to an end', 'i could have done so much more', 'i have a family, kill them instead']
    await ctx.send(choice(responses))

@client.command(name='bye', help='This command returns a random last bye statement.')
async def bye(ctx):
    responses = ['Bye Bro','Chl nikal server se','yogi ko maaro','see you later','Bye','party to abhi baaki hai bhai kaha ja raha hai','Notes dekar chala ja bhai']
    await ctx.send(choice(responses))

@client.command(name='credits', help='This command returns the credits')
async def credits(ctx):
    await ctx.send('Made by Ekansh')
    await ctx.send('Thanks to Srishti for coming up with the idea')
    await ctx.send('Thanks to `Love` for helping ')

@client.command(name='creditz', help='This command returns the TRUE credits')
async def creditz(ctx):
    await ctx.send('**No one but me, lozer!**')

@client.command(name='join', help='This command joins the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return

    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()

@client.command(name='leave', help='This command makes the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()

@client.command(name='play', help='This command plays music')
async def play(ctx, url):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return

    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()

    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing():
        player = await YTDLSource.from_url(url, loop=client.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('**Now playing:** {}'.format(player.title))

@client.command(name='stop', help='This command stops the music and makes the bot leave the voice channel')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()

@client.command(name='love', help='This command stops the music and makes the bot leave the voice channel')
async def love(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()


"""
@client.command(name='listen', help='This command take command as VI')
async def listen(ctx):
    await ctx.send('listening')
    
    query = takeCommand().lower() 
    await ctx.send(query)
            #speak('Searching wikipedia')

    query = query.replace("wikipedia","")
    results = wikipedia.summary(query,sentences = 2)
    await ctx.send(results)"""

@client.command(name='take', help='This command take word and search for it')
async def take(ctx,word):
    
    query = word
    await ctx.send(query)
            #speak('Searching wikipedia')

    query = query.replace("wikipedia","")
    results = wikipedia.summary(query,sentences = 2)
    await ctx.send(results)

@client.command(name='bol', help='Work in Progress')
async def bol(ctx):
      if not ctx.message.author.voice:
          await ctx.send("You are not connected to a voice channel")
          return

      else:
          channel = ctx.message.author.voice.channel

      await channel.connect()

      server = ctx.message.guild
      voice_channel = server.voice_client

      async with ctx.typing():
          player = ''
          voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

      await ctx.send('can you here me ????')


@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))
keep_alive()
client.run("ODg1OTI0MDM5MTQ1Njg5MTA4.YTuHDg.tWtf7GGkBcRGv5swGbIm0Vj8bXs")
