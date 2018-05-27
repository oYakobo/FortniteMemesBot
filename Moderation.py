import discord
from discord.ext import commands
import time
import random

Admins = ['285521611887607809']
colors = [int(0xe6194b), int(0x3cb44b), int(0xffe119), int(0x0082c8), int(0xf58231), int(0x911eb4), int(0x46f0f0), int(0xf032e6), int(0xd2f53c), int(0xfabebe), int(0x008080), int(0xe6beff), int(0xaa6e28), int(0xfffac8), int(0x000000)]

class Moderation():
    def __init__(self, client):
        self.client = client
    
    @commands.command(pass_context=True)
    async def Kick(self, ctx, user: discord.Member):
        if user.id in Admins:
            await self.client.say('You Are Not Allowed To Kick Admins! \n Action Has Been Logged!')
        else:
            await self.client.kick(user)
            await self.client.say('Kicked `{}`'.format(user.name))

    @commands.command(pass_context=True)
    async def ban(self, ctx, user:discord.Member, *, reason:str=None): 
        if ctx.message.author.id in Admins:
            if reason is None:
                await self.client.ban(user)
                await self.client.say('{} Banned {}. No Reason Provided'.format(ctx.message.author.name, user.name))
            else:
                await self.client.ban(user)
                await self.client.say('{} Banned {} Reason: `{}`'.format(ctx.message.author.mention, user.name, reason))
        else:
            await self.client.say('You Do Not Have Permission To Use This Command.')

    @commands.command(pass_context=True)
    async def bans(self, ctx, sid:str = None):
        if sid is None:
            x = await self.client.get_bans(ctx.message.server)
            embed = discord.Embed(title='__{}__ Bans:'.format(ctx.message.server.name), description=('`{}`'.format(len(x))), color=random.choice(colors))
            embed.set_footer(text=ctx.message.author)
            await self.client.say(embed=embed)
        else:
            x = await self.client.get_bans(discord.Object('{}'.format(sid)))
            embed = discord.Embed(title='__{}__ Bans:'.format(sid.name), description=('`{}`'.format(len(x))), color=random.choice(colors))
            embed.set_footer(text=ctx.message.author)
            await self.client.say(embed=embed)

    @commands.command(pass_context=True)
    async def invite(self, ctx):
        x = await self.client.create_invite(ctx.message.channel, max_age=0, max_uses=10)
        embed = discord.Embed(description = 'Invite For Server Channel: {}'.format(ctx.message.channel.name), title = ':space_invader:' , color = random.choice(colors))
        embed.add_field(name = x, value = 'Note: This Is An Invite For This Specific Channel.')
        embed.set_footer(text='Requested By: {}'.format(ctx.message.author.name))
        await self.client.say(embed=embed)

    @commands.command(pass_context=True)
    async def invitebot(self, ctx):
        embed=discord.Embed(title='Click Below To Invite Me To Your Server!', description='[Invite Link](https://discordapp.com/oauth2/authorize?client_id=447201699971596298&scope=bot&permissions=8)', color=random.choice(colors))
        await self.client.say(embed=embed)

def setup(client):
    client.add_cog(Moderation(client))
