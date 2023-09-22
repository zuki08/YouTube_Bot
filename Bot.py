from modules.ind_API import *
from dotenv import load_dotenv

load_dotenv()

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

