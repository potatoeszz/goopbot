import discord
from dotenv import load_dotenv
import os
from math import *
from discord.ext import commands
import random
import openai
import time


#variables
messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "You are a middle school teacher."},
        {"role": "assistant", "content": "Sure. I would like!"},
    ]

# Goal: Reset the conversation after 5 minutes
chat_timestamp = time.time() # time of last chat message

def resetConversationIfExpired():
    global chat_timestamp
    global messages
    cur_time = time.time()
    if cur_time - chat_timestamp > 300: # reset history message
        messages = messages[:3]
        print("Resetting conversation history")
    chat_timestamp = cur_time


magic_list = ["yes ma'am", "no sir", "maybe", "dunno", "what the heck did you just say", "so so who knows", "bro your stupid no", "bruh obviously"]

#chat gpt
load_dotenv("C_TOKEN")
c_token = os.getenv("C_TOKEN")

openai.api_key = c_token

def chat(inp):
  resetConversationIfExpired()
  messages.append({"role": "user", "content": inp})
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
  )
  messages.append(response.choices[0].message)
  return (response.choices[0].message.content)

#create intents
intents = discord.Intents.default()
intents.message_content = True

# read bot token from .env file
load_dotenv("TOKEN")
token = os.environ.get("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.command(help="makes it say some stuff")
async def test(ctx):
    await ctx.send("omg slay soul sister " + " :smirk_cat:" + ":nail_care:")

@bot.command(help="repeats what you said")
async def echo(ctx, *, arg):
    await ctx.send(arg)

@bot.command(help="does math for you")
async def math(ctx, *, arg):
    await ctx.send("the answer is " + str(eval(arg)) + " you little bozo")

@bot.command(help="chat gpt for yall nerds")
async def ai(ctx, *, arg):
    await ctx.send(chat(arg))


bot.run(token)

