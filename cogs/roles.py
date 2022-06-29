import discord 
from discord.ext import commands
from discord.utils import get

class Roles(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is ready")

    # adds role to user, !addrole (role name) (username)
    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def addrole(self, ctx, role_str, member: discord.Member=None):
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
    @commands.command(name="removerole")
    @commands.has_permissions(manage_roles = True)
    async def removerole(self, ctx, role_str, member: discord.Member=None):
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

def setup(client):
    client.add_cog(Roles(client))