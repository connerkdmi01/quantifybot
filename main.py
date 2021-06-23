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
        oldmsg = content[2:]
        msg = ''
        for e in oldmsg:
            lower = e.lower()
            if lower == "a":
                msg += "∀"
            elif lower == "e":
                msg += "∃"
            elif lower == "n":
                msg += "ℕ"
            elif lower == "z":
                msg += "ℤ"
            elif lower == "q":
                msg += "ℚ"
            elif lower == "r":
                msg += "ℝ"
            elif lower == "c":
                msg += "ℂ"
            elif lower == "o":
                msg += "⊖"
            else:
                msg += e
        await message.channel.send(msg)
    
    if "Conner is dumb" in content:
        await message.channel.send("I totally agree! He's super dumb.")


token = os.getenv('TOKEN')
client.run(token)