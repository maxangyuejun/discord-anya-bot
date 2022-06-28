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



# adds role to user, !addrole (role name) (username)
@bot.command(name="addrole")
@commands.has_permissions(manage_roles = True)
async def addrole(ctx, role_str, member: discord.Member=None):
    role = get(ctx.guild.roles, name=role_str)
    if role == None:
        await ctx.send("Role does not exist. Please create the role first")
        return
    member = member or ctx.message.author
    if role in member.roles:
        await ctx.send(f"User {member} already has role \'{role}\'")
    else:
        await member.add_roles(role)
        await ctx.send(f"Role \'{role}\' has been added to user {member}")
@addrole.error
async def addrole_error(ctx, error):
    print(error)
    await ctx.send("Something went wrong or you do not have permission to use this command.")
    await ctx.send("Try !addrole \"<insert role here>\" <username> if role contains more than 1 word")


# removes role from user, !removerole (role name) (username)
@bot.command(name="removerole")
@commands.has_permissions(manage_roles = True)
async def removerole(ctx, role_str, member: discord.Member=None):
    role = get(ctx.guild.roles, name=role_str)
    if role == None:
        await ctx.send("Role does not even exist, how to remove? You airhead, Anya does not like you. Anya likes peanuts.")
        return
    member = member or ctx.message.author
    if role not in member.roles:
        await ctx.send(f"User {member} does not have role \'{role}\'")
    else:
        await member.remove_roles(role)
        await ctx.send(f"Role \'{role}\' has been removed from user {member}")
@removerole.error
async def add_role_error(ctx, error):
    print(error)
    await ctx.send("Something went wrong or you do not have permission to use this command.")
    await ctx.send("Try !removerole \"<insert role here>\" <username> if role contains more than 1 word")


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

