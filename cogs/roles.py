import discord 
from discord.ext import commands
from discord.utils import get

class Roles(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.name = "Roles cog"

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.name} is loaded")

    # adds role to user, !addrole (role name) (username)
    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def addrole(self, ctx, role_str, member: discord.Member=None):
        # Checks if role is mentioned using @role instead of simply typed out
        if role_str[0] == "<" and role_str[-1] == ">":
                await ctx.send("Do not tag the role. If role contains more than 1 word, wrap role in \"\" (case sensitive), for eg `\"example role\"`. Anya says try again!")
                return
        role = get(ctx.guild.roles, name=role_str)
        # Checks if role is present in server roles
        if role == None:
            await ctx.send("Role does not exist. Please create the role first")
            return
        
        anya = ctx.guild.get_member(self.client.user.id)
        # Checks if role is higher than highest Anya role in role hierarchy
        if role >= anya.top_role:
            await ctx.send("Role being added is higher than Anya's highest role, unable to be added by Anya. Please do so manually or give Anya more power owo")
            return

        # Checks if target member already has role
        if role in member.roles:
            await ctx.send(f"User {member} already has role \'{role}\'")
        else:
            await member.add_roles(role)
            await ctx.send(f"Role \'{role}\' has been added to user {member}")
    @addrole.error
    async def addrole_error(self, ctx, error):
        print(type(error))
        print(f"error is {error}")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(error)
            return
        elif isinstance(error, commands.MemberNotFound):
            await ctx.send(error)
            await ctx.send("Try wrapping username in \"\" (case sensitive) if it contains more than 1 word, for eg `\"Anya Bot\"` OR use entire user discord tag, eg. `Anya Bot#9754`")
            await ctx.send("Alternatively, try wrapping role in \"\" (case sensitive) if role contains more than 1 word, for eg `\"example role\"`. Anya says try again!")
            return
        elif isinstance(error, commands.CommandInvokeError):
            await ctx.send("Command failed to activate, missing some arguments. Make sure command is in format: \n`!addrole <role> <user>`")
            return
        await ctx.send("Something went wrong")
        await ctx.send(f"Error message is {error}")

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
    async def add_role_error(self, ctx, error):
        print(error)
        await ctx.send("Something went wrong or you do not have permission to use this command.")
        await ctx.send("Try !removerole \"<insert role here>\" <username> if role contains more than 1 word")

def setup(client):
    client.add_cog(Roles(client))