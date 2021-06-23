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
    content = message.content

    replacedict = {
        "a": "∀",
        "e": "∃"
    }

    if message.author == client.user:
        if "I totally agree! He's super dumb." in content:
            await message.channel.send("But Giselle's even dumber!")
        return

    if content.startswith('!hello'):
        await message.channel.send('Hello!')

    if content.startswith('!q'):
        msg = ''
        for e in content:
            if e.lower() in replacedict.values():
                msg += dict.get(e.lower())
            else:
                msg += e
        await message.channel.send(msg)
    
    if "Conner is dumb" in content:
        await message.channel.send("I totally agree! He's super dumb.")


token = os.getenv('TOKEN')
client.run(token)