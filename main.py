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
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Spy x Family"))

@bot.command(name="testing")
async def test(ctx, *args):
    await ctx.send(" ".join(args))

@bot.command(name="createrole")
@commands.has_permissions(manage_roles = True)
async def create_role(ctx, role_name):
    if get(ctx.guild.roles, name=role_name):
        await ctx.send(f"Role {role_name} already exists")
    else:
        await ctx.guild.create_role(name=role_name, colour=discord.Colour(0x0062ff))
        await ctx.send(f"Role {role_name} created")
        print(f"role {role_name} created")


@bot.command(name="addrole")
@commands.has_permissions(manage_roles = True)
async def add_role(ctx, user: discord.Member, *, role):
    if get(ctx.guild.roles, name=role) == None:
        await ctx.guild.create_role(name=role, colour=discord.Colour(0x0062ff))
        await ctx.send(f"Role {role} created")
        print(f"role {role} created")
    target_role = get(ctx.guild.roles, name=role)
    if target_role in user.roles:
        await ctx.send(f"User {user} already has role {role}")
    else:
      await user.add_roles(target_role) #adds role if not already has it
      await ctx.send(f"Added role {role} to {user}")
@add_role.error
async def add_role_error(ctx, error):
    print(error)
    await ctx.send("Something went wrong or you do not have permission to use this command, try !addrole \"<insert nickname here>\" if nickname contains more than 1 word")


#   await user.remove_roles(role) #removes the role if user already has
#   await ctx.send(f"Removed {role} from {user.mention}")

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return

    content = msg.content.lower()

    if "hello" in content and content[0] != "!":
        await msg.channel.send("Hello!")
        

    elif "ferrari" in content and content[0] != "!":
        await msg.add_reaction("<:elbobo:777884601615777803>")
        await msg.channel.send("10-place grid penalty")

    await bot.process_commands(msg)
        



bot.run(token)

