import discord
from discord.ext import commands
#import keep_alive
TOKEN = ''  #Discord bot's Token
bot = commands.Bot(command_prefix='')

@bot.event
async def on_ready():
    print("Hi")




#keep_alive.keep_alive()
bot.run(TOKEN) 
