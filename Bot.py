import modules.ind_API as proc
from dotenv import load_dotenv
import os
import time

load_dotenv()

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    # if message.author == client.user:
    #     await message.delete(delay=330)
    #     return
    if message.content.startswith('-hello'):
        await message.channel.send(f"Hello {message.author.mention}")
    if message.content.split(" ")[0] == '-search':
        query = message.content[8:].strip()
        # print(query)
        link = proc.search(query)
        await message.channel.send(f"Here's what you searched: `{query}`")
        await message.channel.send(link)
    if message.content.split(" ")[0] == '-choose':
        query = message.content[8:].strip()
        # print(query)
        link = proc.choose(query)
        await message.channel.send(f"Here's what you chose: ")
        await message.channel.send(link)
    if(message.content == '-close'):
        proc.close_leConn()
        async for s in message.channel.history():
            if s.author == client.user:
                await s.delete()
        await message.delete()
        await client.close()
    # await message.delete()
    if message.content == "-list":
        ret = ""
        for val in proc.list():
            ret += str(val)+ "\n"
        await message.channel.send(ret)
    if message.content == "-clear":
        async for s in message.channel.history():
            await s.delete()
    if message.content.split(" ")[0] == '-select':
        query = message.content[8:].strip()
        # print(query)
        link = proc.select(query)
        await message.channel.send(f"Here you go: ")
        await message.channel.send(link)
    # await message.delete(delay=330)
client.run(os.getenv('TOKEN'))