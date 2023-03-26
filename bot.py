import discord
from dotenv import load_dotenv
import os

#create intents
intents = discord.Intents.default()
intents.message_content = True

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
    if message.content.startswitch

# log in
client.run(token)



