import json
import discord
from discord.ext import commands
from discord.ext import tasks
import random
import os
from itertools import cycle
import wikia

client = commands.Bot(command_prefix = '+')
status = cycle(['Dodging Quincy`s arrows! //+help//', 'Doing Bloony stuff!! //+help//', 'Going to war!! h+h//+help//'])

client.remove_command('help')

@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready')

@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def wiki(ctx, about):
    bloons = wikia.page("bloons", about)
    await ctx.send(bloons.title)
    await ctx.send(bloons.url)
    await ctx.send(bloons.content)

@client.command()
async def speed(ctx):
    await ctx.send(f'Speed: {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball', 'are'])
async def _8ball(ctx, *,question):
    responses = ['● It is certain.' ,
                '● It is decidedly so.' ,
                '● Without a doubt.' ,
                '● Yes – definitely.' ,
                '● You may rely on it.' ,
                '● As I see it, yes.' ,
                '● Most likely.' ,
                '● Outlook good.' ,
                '● Yes.',
                '● Signs point to yes.' ,
                '● Reply hazy, try again.' ,
                '● Ask again later.' ,
                '● Better not tell you now.' ,
                '● Cannot predict now.' ,
                '● Concentrate and ask again.' ,
                '● My reply is no.' ,
                '● My sources say no.' ,
                '● Outlook not so good.' ,
                '● Very doubtful',
                '● Hahaha the Bloons got the 8Ball ']
    await ctx.send(f'Question: {question}\n {random.choice(responses)}')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount+1)

@client.command()
async def easteregg(ctx):
    await ctx.send('A bot created by @zool(q), and you found the easter egg!!')

@client.command()
async def credits(ctx):
    await ctx.send('**Programing: @zool(q) and @Gas_Infinity**\n**Development Help: @epicnoob and @Juggin The Turtle and @FenixKillah and @EricOboe25**\n**Special Thanks: Bloons Wiki and the Index Server!!** ')

@client.command()
@commands.has_permissions(manage_roles=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
@commands.has_permissions(manage_roles=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def help(ctx):
    await ctx.send('**help** \nPrefix normal commands + \nPrefix index commands i+ \n**Moderation and miscellaneous commands**\nSpeed = Shows you how fats the Bot currently is\n8ball (question) = 8ball gives you an awnser\nbann @member (reason) = bann member\nkick @member (reason) = kick member\nclear (amount) = clear (amont) messages\n**Index**\n(bloon name) = information about that bloon')
    await bot.procces_commands('**help** \nPrefix normal commands + \nPrefix index commands i+ \n**Moderation and miscellaneous commands**\nSpeed = Shows you how fats the Bot currently is\n8ball (question) = 8ball gives you an awnser\nbann @member (reason) = bann member\nkick @member (reason) = kick member\nclean (amount) = clean (amont) messages\n**Index**\n(bloon name) = information about that bloon')

client.run('Token')
