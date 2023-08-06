import discord
from discord.ext import commands

# Set your bot's token here
TOKEN = 'MTA2Mzk5ODEzMTIxNTI5MDM4OA.GMWaRY.2-E2fDoOOL5JjdxLcRoVnb4L_SjT0bI-uSfKks'

# Set the command prefix
bot = commands.Bot(command_prefix='!')

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Command: Ping
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Command: Hello
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello, {ctx.author.mention}!')

# Run the bot
bot.run(TOKEN)
