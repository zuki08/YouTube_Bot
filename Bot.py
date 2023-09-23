import modules.ind_API as proc
from dotenv import load_dotenv
import os

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
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send(f"Hello {message.author.mention}")
    if message.content.split(" ")[0] == '$search':
        query = message.content[8:].strip()
        # print(query)
        proc.search(query)
        await message.channel.send(f"Here's what you searched: `{query}`")
    if(message.content == 'close'):
        proc.close_leConn()
        exit()
    
client.run(os.getenv('TOKEN'))