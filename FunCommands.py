import discord
from discord.ext import commands
import random
import requests
import aiohttp
import pynite
from bs4 import BeautifulSoup


colors = [int(0xe6194b), int(0x3cb44b), int(0xffe119), int(0x0082c8), int(0xf58231), int(0x911eb4), int(0x46f0f0), int(0xf032e6), int(0xd2f53c), int(0xfabebe), int(0x008080), int(0xe6beff), int(0xaa6e28), int(0xfffac8), int(0x000000)]
Admins = ['285521611887607809', '168167351580098561']
dice=['http://www.clker.com/cliparts/X/w/P/Y/q/H/dice-1-hi.png', 'http://www.clker.com/cliparts/X/V/S/C/I/x/dice-2-hi.png', 'http://www.clker.com/cliparts/n/O/d/R/Y/c/dice-3-hi.png', 'http://www.clker.com/cliparts/D/j/Z/R/5/P/dice-4-hi.png', 'http://www.clker.com/cliparts/U/N/J/F/T/x/dice-5-hi.png', 'https://wpclipart.com/recreation/games/dice/die_face_6.png']


class FunCommands():
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def clap(self, *, word:str):
        try:
            if len(word) <= int(35):
                x = word.replace('', ':clap:')
                await self.client.say(x)
            if len(word) > int(35):
                x = word.replace(' ', ':clap:')
                await self.client.say(x)
        except Exception as e:
            await self.client.say('Error! {}'.format(e))

    @commands.command(pass_context=True)
    async def pfp(self, ctx, user:discord.Member=None):
        if user is None:
            embed=discord.Embed()
            embed.set_image(url=ctx.message.author.avatar_url)
            await self.client.say(embed=embed)
        else:
            embed=discord.Embed()
            embed.set_image(url=user.avatar_url)
            await self.client.say(embed=embed)

    @commands.command(pass_context=True)
    async def rolldice(self):
        embed = discord.Embed(title=':accept:', color=random.choice(colors))
        embed.set_image(url=random.choice(dice))
        await self.client.say(embed=embed)

    @commands.command(pass_context = True)
    async def fuck(self, ctx):
        try:
            for member in ctx.message.server.members:
                if member is not ctx.message.server.owner:
                    if member.nick is not None:
                        name = member.nick
                        await self.client.change_nickname(member, "NORMIE {}".format(name))
                    else:
                        name = member.name
                        await self.client.change_nickname(member, "NORMIE {}".format(name))
            await self.client.say("This server has been FUCKED!")
        except Exception as e:
            if 'Privilege is too low' in str(e):
                return await self.client.say("Permissions too low!")
            
    @commands.command(pass_context = True)
    async def clearnicks(self, ctx):
        try:
            for member in ctx.message.server.members:
                if member is not ctx.message.server.owner:
                    name = member.name
                    await self.client.change_nickname(member, name)
            await self.client.say("Nicknames Cleared!")
        except Exception as e:
            if 'Privilege is too low' in str(e):
                return await self.client.say("Permissions too low!")

    @commands.command(pass_context=True)
    async def format(self, ctx, *, code:str):
        await self.client.delete_message(ctx.message)
        await self.client.say('```' + code + '```')

    @commands.command(pass_context=True)
    async def Server(self, ctx, args):
        ServerNames = [x.name for x in self.client.servers]
        ServerIDs=[x.id for x in self.client.servers]
        try:
            if args == 'ID':
                await self.client.say(ServerIDs)
            if args == 'Name':
                await self.client.say(ServerNames)
        except Exception as e:
            await self.client.say('`Error!` {}'.format(e))

    @commands.command(pass_context=True)
    async def add(self, ctx, *args):
        try:
            first=int(args[0])
            second=int(args[1])
            await self.client.say(first + second)
            await self.client.say('Quik Maths')
        except Exception as e:
            await self.client.say('`Error!` {}'.format(e))
            await self.client.say('Correct Usage: `-add 2 2`')

    @commands.command(pass_context=True)
    async def gayrate(self, ctx, user:discord.Member=None):
        if user is None:
            embed=discord.Embed(title='GayRate Machine!', description='{}%'.format(random.randint(1,100), color=random.choice(colors)))
            embed.set_footer(text=ctx.message.author)
            await self.client.say(embed=embed)
        if user is not None:
            if user.id == '285521611887607809':
                embed=discord.Embed(title='GayRate Machine!', description='{} is 0% Gay'.format(user.name, color=random.choice(colors)))
                embed.set_footer(text=user)
                await self.client.say(embed=embed)
            elif user.id == '220662601082863616':
                embed=discord.Embed(title='GayRate Machine!', description='{} is {}% Gay'.format(user.name, random.randint(95,100), color=random.choice(colors)))
                embed.set_footer(text=user)
                await self.client.say(embed=embed)
            else:
                embed=discord.Embed(title='GayRate Machine!', description='{} is {}% Gay'.format(user.name, random.randint(1,100), color=random.choice(colors)))
                embed.set_footer(text=user)
                await self.client.say(embed=embed)

    @commands.command(pass_context=True)
    async def NSFWgif(self, ctx):
        if ctx.message.author.id in Admins:
            channel = ctx.message.channel
            await self.client.send_typing(channel)
            number = random.randint(1600,1999)
            link = f"https://cdn.boob.bot/Gifs/{number}.gif"
            embed=discord.Embed(title='Dont Get Too Excited', color=random.choice(colors))
            embed.set_image(url=link)
            await self.client.say(embed=embed)
        else:
            await client.say('You Do Not Have Permission To Use This Command')

    @commands.command(pass_context=True)
    async def urban(self, ctx, *, args):
        r = requests.get("http://www.urbandictionary.com/define.php?term={}".format(args))
        soup = BeautifulSoup(r.content)
        x = (soup.find("div",attrs={"class":"meaning"}).text)
        embed = discord.Embed(title='Term: {}'.format(args), description='Description:\n{}'.format(x), color=random.choice(colors))
        await self.client.say(embed=embed)


    @commands.command(pass_context=True)
    async def dog(self, ctx):
        if ctx.message.author.id in Admins:
            api = "https://api.thedogapi.co.uk/v2/dog.php"
            async with aiohttp.ClientSession() as session:
                async with session.get(api) as r:
                    if r.status == 200:
                        response = await r.json()
                        embed = discord.Embed(description=None, color = random.choice(colors))
                        embed.set_author(name = "{} here is your random dog".format(ctx.message.author.name))
                        embed.set_image(url = response['data'][0]["url"])
                        await self.client.say(embed = embed)
        else:
            await client.say('You Do Not Have Permission To Use This Command')

    @commands.command(pass_context=True)
    async def announce(self, ctx, *, strn:str):
        embed = discord.Embed(title = '{} Would Like To Announce The Following: '.format(ctx.message.author.name), description = '`{}`'.format(strn), color = random.choice(colors))
        embed.set_footer(text=ctx.message.author)
        await self.client.say(embed=embed)
        await self.client.add_reaction(ctx.message, '<:thumbsup:447835156120862720>')
        await self.client.add_reaction(ctx.message, '<:neutral_face:447834905129517075>')
        await self.client.add_reaction(ctx.message, '<:thumbsdown:447834993364828162>')

    @commands.command(pass_context=True)
    async def stats(self, ctx, platform, name):
        client = pynite.Client('6a336fec-4732-475e-909c-f1b697f01129', timeout=5)
        player = await client.get_player(platform, name)
        solos = await player.get_solos()
        duos = await player.get_duos()
        squads = await player.get_squads()
        lifetime = await player.get_lifetime_stats()
        embed = discord.Embed(title = '{}\'s Fortnite Stats'.format(name.capitalize()), description = 'Score:{}\nGames Played:{}\nTotal Wins: {}(≈{})'.format(lifetime[6].value, lifetime[7].value, lifetime[8].value, lifetime[9].value), color=random.choice(colors))
        embed.add_field(name = '__Solos:__', value = 'Wins- {}\nKills- {}\nK/D- {}'.format(solos.top1.value, solos.kills.value, solos.kd.value))
        embed.add_field(name = '__Duos:__', value = 'Wins- {}\nKills- {}\nK/D- {}'.format(duos.top1.value, duos.kills.value, duos.kd.value))
        embed.add_field(name = '__Squads:__', value = 'Wins- {}\nKills- {}\nK/D- {}'.format(squads.top1.value, squads.kills.value, squads.kd.value))
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/435971749054513176/450123603585794048/fortnite-battle-royale-Fortnite2Fhome2Ffn_battle_logo-1159x974-8edd8b02d505b78febe3baacec47a83c2d521.png')
        embed.set_footer(text='Requested By {}'.format(ctx.message.author))
        await self.client.say(embed=embed)

    @commands.command(pass_context=True)
    async def mobile(self, ctx):
        Mobile_Role = discord.utils.get(ctx.message.server.roles, name='Mobile')
        if Mobile_Role in ctx.message.author.roles:
            await self.client.say('You Already Have That Role.')
        else:
            await self.client.add_roles(ctx.message.author, Mobile_Role)
            await self.client.say(':white_check_mark:{} You Have Been Assigned The Role `Mobile`'.format(ctx.message.author.mention))
        
        
def setup(client):
    client.add_cog(FunCommands(client))
