import discord
from discord.ext import commands
from discord.ext import tasks
import random
import os
from itertools import cycle
import wikia

client = commands.Bot(command_prefix = 'i+')

@client.event
async def on_ready():
    print('bloons index ready')

@client.command()
async def red(ctx):
    await ctx.send('**red bloon**\nRbe = 1 \nchildren = none')

@client.command()
async def blue(ctx):
    await ctx.send('**blue bloon**\nRbe = 1 \nchildren = red bloon')

@client.command()
async def green(ctx):
    await ctx.send('**green bloon**\nRbe = 3 \nchildren = blue bloon')

@client.command()
async def pink(ctx):
    await ctx.send('**pink bloon**\nRbe = 5 \nchildren = yellow bloon')

@client.command()
async def yellow(ctx):
    await ctx.send('**yellow bloon**\nRbe = 4 \nchildren = green bloon')

@client.command()
async def black(ctx):
    await ctx.send('**black bloon**\nRbe = 11\n children = 2x pink bloon')

@client.command()
async def white(ctx):
    await ctx.send('**white bloon**\nRbe = 11\nchildren = 2x pink bloon')

@client.command()
async def lead(ctx):
    await ctx.send('**lead bloon**\nRbe = 19(BTD2-BTD3)/23 (BTD4-BTD6)\nchldren = 2x black bloon')

@client.command()
async def zebra(ctx):
    await ctx.send('**zebra bloon**\nRbe = 23 \nchildren = black bloon, white bloon')

@client.command()
async def raibow(ctx):
    await ctx.send('**rainbow bloon**\nRbe = 37(BTD2 -BTD3)/47(BTD4-BTD6)\nchildren = 2x black bloon, 2x white bloon (BTD2-BTD3)\n2x zebra bloon (BTD4-BTD6)\nyellow bloon (Bloons-Supermonkey)')

@client.command()
async def ceramic(ctx):
    await ctx.send('**ceramic bloon**\nRbe = 84 (BTD3), 104 (BTD4-BTD5),146 (BTD5 freeplay), 104(BTD6)\children = 2x rainbow bloon')

@client.command()
async def purple(ctx):
    await ctx.send('**purple bloon**\nRbe = 11\nchildren = 2x pink bloon')

@client.command()
async def moab(ctx):
    await ctx.send('**M.O.A.B.**\nRbe = 536(BTD3)/ 623(BTD4)/ 616(BTD5-BTD6)/ 1800(Bloons Supermonkey 2 Boss)/ 700(Bloons Supermonkey)/ 856(Fortified)\nchildren = 4x ceramic bloons (BTD)\nMany Red Bloons (Bloons Supermonkey)\nMany red bloons, 8x mini moabs (Bloons Supermonkey 2)')

@client.command()
async def bfb(ctx):
    await ctx.send('**B.F.B.**\nRbe = 2,884 in BTD4(400 HP)/ 3,164 in BTD5(750 HP)/ 3,214 in BTD6(800 HP)/ 4,824 in BD6(1600 HP) (Fortified)8,500 in BSM217,500 in BSM2 (as a Boss in 2-5)')

@client.command()
async def zomg(ctx):
    await ctx.send('**Z.O.M.G.**\nRbe = 16,656(4000hp)/ fortiefied: 27,296(8000hp)\nchildren: 4x B.F.B.')

@client.command()
async def bad(ctx):
    await ctx.send('**B.A.D.**\nRbe = 55,760 (20,000 HP)/ fortified: 98,360(40,000 HP)\nchildren: 2x Z.O.M.G, 3x D.D.T.')

@client.command()
async def ddt(ctx):
    await ctx.send('**D.D.T.**\nRbe = BTD6: 816(400 HP)/ fortiefied: 1256(800 HP)/ Bloons Monkey City: 924(300 HP)\nchildren: 4x Camo Regen Ceramic Bloons (BTD6)/ 6x Camo Regen Ceramic Bloons (Bloons Monkey City)')

client.run('Token')
