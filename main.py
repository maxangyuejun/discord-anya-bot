from discord.utils import get
from discord.ext import commands
import discord
import os
from dotenv import load_dotenv

load_dotenv()
bot = commands.Bot(command_prefix='!')
token = os.getenv("TOKEN")

@bot.event
async def on_ready():
    print(f"{bot.user} has connected to discord!")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Bondman"))

# test command, bot repeats message from user after !testing (message)
@bot.command(name="testing")
async def test(ctx, *args):
    await ctx.send(" ".join(args))

# Loads a cog file from cogs folder
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f"cogs.{extension}")

# Unloads a cog file from cogs folder
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f"cogs.{extension}")

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return

    content = msg.content.lower()

    if "hello" in content and content[0] != "!":
        await msg.channel.send("Hello!")
        
    elif "wat" in content and content[0] != "!":
        await msg.channel.send("WAT")

    elif "ferrari" in content and content[0] != "!":
        await msg.add_reaction("<:elbobo:777884601615777803>")
        await msg.channel.send("10-place grid penalty")

    await bot.process_commands(msg)
        
# Loads all .py Cog files in cogs folder
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run(token)

