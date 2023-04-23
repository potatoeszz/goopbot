import discord
from dotenv import load_dotenv
import os
from math import * 
import random
##testing stuff
from discord.ext import commands
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")



#variable stuff
magic_list = ["yes ma'am", "no sir", "maybe", "dunno", "what the heck did you just say", "so so who knows", "bro your stupid no", "bruh obviously"]
#create intents
intents = discord.Intents.default()
intents.message_content = True

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)




#read bot token from .env file
load_dotenv("TOKEN")
token = os.environ.get("TOKEN")

# create bot client
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user.name} is ready to rock and roll!")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content.startswith("~"):
        cleanMsg = message.content[1:]
        await message.channel.send("omg slay soul sister " + " :smirk_cat:" + ":nail_care:")
    if message.content.startswith("math "):
        cleanMsg = message.content[4:]
        await message.channel.send("The answer is '" + str(eval(cleanMsg)) + "' you little bozo")
    if message.content.startswith("nails"):
        cleanMsg = message.content[5:]
        await message.channel.send("perioddttt" + " :nail_care:")
    elif message.content.startswith("8ball"):
        cleanMsg = message.content[5:]
        await message.channel.send(str(random.choice(magic_list)))
    
        
#@bot.command("/")
#async def foo(ctx, arg):
#    await ctx.send(arg)

# log in
client.run(token)



