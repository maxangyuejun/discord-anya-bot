from pydoc import cli
import discord
import os
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()
token = os.getenv("TOKEN")
# print(token)

@client.event
async def on_ready():
    print(f"{client.user} has connected to discord!")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Spy X Family"))

@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    content = msg.content.lower()

    if "hello" in content:
        # await msg.add_reaction("<:elbobo:777884601615777803>")
        await msg.channel.send("Hello!")
        

    elif "ferrari" in content:
        await msg.channel.send("10-place grid penalty")
        

client.run(token)

