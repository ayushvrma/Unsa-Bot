import discord
import os
from discord.ext import commands
import random

client=commands.Bot(command_prefix="unsa ")

@client.event       #function denoter that denotes that func is gonna have an event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('daarubaaji'))
    print("Bot is ready")

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server')

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency *1000)}ms")

@client.command(aliases=['8ball'])
async def ques(ctx, *,question):
    answer = ['Ho sakta hai','Lund se mere','Ama chudo','Han kyu nahi']
    await ctx.send(f'{random.choice(answer)}')

@client.command()
async def clear(ctx,amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx,member: discord.Member, *,reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx,member: discord.Member, *,reason=None):
    await member.ban(reason=reason)

@client.command()
async def unban(ctx,member: discord.Member, *,reason=None):
    banned_users= ctx.guild.bans()
    member_name, member_hash= member.split('#')
    for banned_entry in banned_users:
        user= banned_entry.user

        if((user.name, user.discriminator)==(member_name, member_hash)):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {member.mention}')
            return









client.run('Nzk4NDkwOTIyNjgxNDk5NjY4.X_1ynw.uA1r3UsYLtGaLdYmLH_HYP5lySA')
