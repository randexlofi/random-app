import discord
from discord.ext import commands

#Self made
import settings

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# Create an instance of the bot with a command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    print(f'Message from {message.author} on {message.channel}:\n{message.content}')

    await bot.process_commands(message)

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

def RunBot():
    bot.run(settings.BOT_TOKEN)