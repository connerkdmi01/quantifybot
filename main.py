import discord
import os
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
    if message.content.startswith("Conner is dumb"):
        await message.channel.send("I agree, Conner is dumb!")

client.run(os.getenv('TOKEN'))