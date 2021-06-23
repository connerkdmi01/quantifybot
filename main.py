import discord
import os
import dotenv
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")
client = discord.Client()

@client.event
async def on_ready():
    print('Poggers it is me, {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

token = os.getenv('DISCORD_TOKEN')
client = discord.Client()
client.run(token)