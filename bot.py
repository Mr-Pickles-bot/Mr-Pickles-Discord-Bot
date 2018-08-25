import discord
from discord.ext import commands
import aiohttp
import re
from datetime import timedelta
import traceback
import os
from random import choice, randint
from config import token

owner = ["222526329109741568", "252084047264743428"]
version = "Ver. 0.1.29.3"

bot = commands.Bot(command_prefix='p!', description=" I'm that demonic border collie from that television show.")

@bot.event
async def on_ready():
    print('Mr. Pickles Discord Bot')
    print('Version:')
    print(version)
    print('Logged in as')
    print(bot.user.name)
    print('With ID:')
    print(bot.user.id)
    print('Number of Guilds:')
    print((len(bot.servers)))
    print('------')
    print('Invite me to your server:')
    print(discord.utils.oauth_url(bot.user.id))
    await bot.change_presence(game=discord.Game(name='with my vaccum cleaner~ | p!help'))

@bot.command(pass_context=True, hidden=True)
async def setgame(ctx, *, game):
    if ctx.message.author.id not in owner:
        return
    game = game.strip()
    if game != "":
        try:
            await bot.change_presence(game=discord.Game(name=game))
        except:
            embed=discord.Embed(title="Failed", description="Couldn't change game.. Check console.", color=0xfb0006)
            await bot.say(embed=embed)
        else:
            embed=discord.Embed(title="Success!", description="Game changed.", color=0xfb0006)
            await bot.say(embed=embed)
    else:
        await bot.send_cmd_help(ctx)

@bot.command(pass_context=True, hidden=True)
async def setname(ctx, *, name):
    if ctx.message.author.id not in owner:
        return
    name = name.strip()
    if name != "":
        try:
            await bot.edit_profile(username=name)
        except:
            embed=discord.Embed(title="Failed", description="Couldn't change name. Check console.", color=0xfb0006)
            await bot.say(embed=embed)
        else:
            embed=discord.Embed(title="Success!", description="Name changed.", color=0xfb0006)
            await bot.say(embed=embed)
    else:
        await bot.send_cmd_help(ctx)

@bot.event
async def on_command_error(error, ctx):
    channel = ctx.message.channel
    if isinstance(error, commands.MissingRequiredArgument):
        await send_cmd_help(ctx)
    elif isinstance(error, commands.BadArgument):
        await send_cmd_help(ctx)
    elif isinstance(error, commands.CommandInvokeError):
        print("<:mrpickles:480552232165572608> Exception in command '{}', {}".format(ctx.command.qualified_name, error.original))
        traceback.print_tb(error.original.__traceback__)
        embed=discord.Embed(title="Error", description="It seems like something went wrong. Check console/report to my developers.", color=0xfb0006)
        await bot.say(embed=embed)

@bot.command(pass_context=True, no_pm=True)
async def avatar(ctx, member: discord.Member):
    """User Avatar"""
    await bot.reply("{}".format(member.avatar_url))

@bot.command(pass_context=True, no_pm=True)
async def guildicon(ctx):
    """Guild Icon"""
    await bot.reply("{}".format(ctx.message.server.icon_url))

@bot.command(pass_context=True)
async def guildid(ctx):
	  """Guild ID"""
	  await bot.reply("`{}`".format(ctx.message.server.id))

@bot.command(pass_context=True, hidden=True)
async def setavatar(ctx, url):
    if ctx.message.author.id not in owner:
    	return
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            data = await r.read()
    await bot.edit_profile(avatar=data)
    embed=discord.Embed(title="Success!", description="Avatar changed.", color=0xfb0006)
    await bot.say(embed=embed)

@bot.command()
async def invite():
    """Bot Invite"""
    embed = discord.Embed(title="\U0001f44d")
    embed2=discord.Embed(title="Mr. Pickles Invite", url=(discord.utils.oauth_url(bot.user.id)), description="Click the link if you want me to join your server.", color=0xfb0006)
    await bot.say(embed=embed)
    await bot.whisper(embed=embed2)

@bot.command()
async def guildcount():
    """Bot Guild Count"""
    embed=discord.Embed(title=(len(bot.servers)), color=0xfb0006)
    embed.set_author(name="Guild Count")
    await bot.say(embed=embed)

@bot.event
async def send_cmd_help(ctx):
    if ctx.invoked_subcommand:
        pages = bot.formatter.format_help_for(ctx, ctx.invoked_subcommand)
        for page in pages:
            em = discord.Embed(description=page.strip("```").replace('<', '[').replace('>', ']'),
                               color=discord.Color.blue())
            await bot.send_message(ctx.message.channel, embed=em)
    else:
        pages = bot.formatter.format_help_for(ctx, ctx.command)
        for page in pages:
            em = discord.Embed(description=page.strip("```").replace('<', '[').replace('>', ']'),
                               color=discord.Color.blue())
            await bot.send_message(ctx.message.channel, embed=em)

@bot.command(pass_context=True)
async def ping(ctx):
    embed = discord.Embed(title="Pong! :ping_pong:")
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def info():
    """Information about this bot!"""
    embed=discord.Embed(title="Mr. Pickles Discord Bot", color=0xfb0006)
    embed.add_field(name=":information_source: Version", value=(version), inline=True)
    embed.add_field(name=":busts_in_silhouette: Developers", value="**MZFX18#0069 & JoshTheGamer632#0017**", inline=True)
    embed.add_field(name="<:github:425761614441218048> GitHub", value="https://github.com/Mr-Pickles-bot/Mr.-Pickles-Discord-Bot", inline=True)
    embed.add_field(name="<:kingwumpus:425762228667416625> Need Support?", value="https://discord.gg/jqDH5wZ", inline=True)
    embed.set_footer(text="That was info about my vaccum cleaner.")
    await bot.say(embed=embed)

@bot.command(pass_context=True, hidden=True)
async def shutdown(ctx):
    if ctx.message.author.id not in owner:
        await bot.say("Naughty you...")
        return
    embed=discord.Embed(title="Back to my lair I go...", color=0xfb0006)
    await bot.say(embed=embed)
    await bot.logout()


@bot.command(hidden=True)
async def vaccum():
    await bot.say("*naughty things to Grandpa's vaccum*")

@bot.command(hidden=True)
async def secret():
    await bot.say("Stop scanning for commands. FFS.")

@bot.command(pass_context=True, hidden=True)
async def authors():
    await bot.say("<@222526329109741568> and <@252084047264743428> are my creators. ")

@bot.command(hidden=True)
async def lemmefuck():
    await bot.say("Cooters with Wings")

@bot.command()
async def vaccumgif():
    await bot.say("https://lh4.googleusercontent.com/-3PqHxlkQcXg/VE7XszJKUpI/AAAAAAAAAMg/3vOnHgjKMLQ/w500-h307/tumblr_ndsgyr7Hs51tmpaf1o1_500.gif")

@bot.command()
async def settoken():
    await bot.say("swear to fuck man.")



bot.run(token)  # Where 'TOKEN' is your bot token
