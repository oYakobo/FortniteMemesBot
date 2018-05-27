import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from datetime import datetime


BOT_PREFIX=('-', '<@447201699971596298> ')
client = Bot(command_prefix=BOT_PREFIX)
startup_extensions = ['DeveloperCommands', 'AdminCommands', 'InfoCommands', 'Moderation', 'WebRequests', 'MoneySystem', 'FunCommands']
client.remove_command('help')
Admins = ['285521611887607809']
colors = [int(0xe6194b), int(0x3cb44b), int(0xffe119), int(0x0082c8), int(0xf58231), int(0x911eb4), int(0x46f0f0), int(0xf032e6), int(0xd2f53c), int(0xfabebe), int(0x008080), int(0xe6beff), int(0xaa6e28), int(0xfffac8), int(0x000000)]
Blacklist = ['fuck', 'shit', 'arse', 'ass', 'asshole', 'bastard', 'bitch', 'bollocks', 'child-fucker', 'christ on a bike', 'christ on a cracker', 'crap', 'cunt', 'damn', 'swear word', 'frigger', 'fuck', 'goddamn', 'godsdamn', 'hell', 'holy shit', 'jesus', 'jesus Christ', 'jesus h. christ', 'jesus harold christ', 'jesus wept', 'jesus', 'mary and joseph', 'judas priest', 'motherfucker', 'nigga', 'nigger', 'shit', 'shit ass', 'shitass', 'son of a bitch', 'son of a motherless goat', 'son of a whoresweet jesus', 'twat']

@client.event
async def on_ready():
    print('''#     #    #    #    # ####### ######     ######  ####### ####### 
 #   #    # #   #   #  #     # #     #    #     # #     #    #    
  # #    #   #  #  #   #     # #     #    #     # #     #    #    
   #    #     # ###    #     # ######     ######  #     #    #    
   #    ####### #  #   #     # #     #    #     # #     #    #    
   #    #     # #   #  #     # #     #    #     # #     #    #    
   #    #     # #    # ####### ######     ######  #######    #    
                                                                  
####### #     # #       ### #     # ####### 
#     # ##    # #        #  ##    # #       
#     # # #   # #        #  # #   # #       
#     # #  #  # #        #  #  #  # #####   
#     # #   # # #        #  #   # # #       
#     # #    ## #        #  #    ## #       
####### #     # ####### ### #     # ####### 
''')
    print('\n\nLogged in as: {} - {}\nDiscord Version: {}\n'.format(client.user.name, client.user.id, discord.__version__))
    embed = discord.Embed(title='Bot Online!', description='Launched @ {}'.format(str(time.asctime( time.localtime(time.time()) ))))
    #await client.send_message(discord.Object('440304039968899072'), embed=embed)

@client.event
async def on_message(message):
    if message.content.lower() in Blacklist:
        await client.delete_message(message)
        await client.send_message(message.author, 'Please Do Not Use Inappropriate Language In My Chrsitian Server')
    await client.process_commands(message)

@client.command(pass_context=True)
async def Lockdown(ctx):
    if ctx.message.author.id in Admins:
        global Lockdown
        try:
            await client.say('Lockdown Enabled.')
            Lockdown = True
        except Exception as e:
            await client.say('Error! {}'.format(e))
    else:
        await client.say('That Is An Owner Command!')

@client.command(pass_context=True)
async def DisableLockdown(ctx):
    if ctx.message.author.id in Admins:
        global Lockdown
        if Lockdown == False:
            await client.say('This Server Is Not In Lockdown.')
        if Lockdown == True:
            try:
                await client.say('Lockdown Disabled.')
                Lockdown = False
            except Exception as e:
                await client.say('Error! {}'.format(e))
    else:
        await client.say('That Is An Owner Command!')

@client.event
async def on_member_join(member):
        await client.send_message(discord.Object('450126176548028416'), 'Welcome {} Please Read The Rules And Have Fun.'.format(member.mention))

@client.event
async def on_command_error(message, ctx):
    try:
        embed = discord.Embed(title = 'Error!', description = '`{}:` {}'.format(type(message).__name__, message), color = 0x8B0000)
        embed.set_footer(text='-help for a full list of commands')
        await client.send_message(ctx.message.channel, embed=embed)
    except Exception as e:
        if 'CommandNotFound' in str(e):
            embed = discord.Embed(title = 'Error!', description = '`{}:` {}'.format(type(message).__name__, message), color = 0x8B0000)
            embed.set_footer(text='-help for a full list of commands')
            await client.send_message(ctx.message.channel, embed=embed)
        else:
            embed = discord.Embed(title = 'Error!', description = '`{}:` {}'.format(type(message).__name__, message), color = 0x8B0000)
            embed.set_footer(text='-help for a full list of commands')
            await client.send_message(ctx.message.channel, embed=embed)

@client.command(pass_context=True)
async def help(ctx, *, args=None):
    if args == None:
        embed = discord.Embed(title='__Extension List.__', description='-help`<Extension Name>` For A List Of Commands', color=random.choice(colors))
        embed.add_field(name='`Admin Commands`', value='7 Commands')
        embed.add_field(name='`Developer Commands`', value='7 Commands')
        embed.add_field(name='`Fun Commands`', value='13 Commands')
        embed.add_field(name='`Info Commands`', value='3 Commands')
        embed.add_field(name='`Moderation`', value='4 Commands')
        embed.add_field(name='`Money`', value='2 Commands(Under Development)')
        embed.add_field(name='`No Category`', value='3 Commands')
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        embed.set_footer(text='Requested By {}'.format(ctx.message.author))
        await client.say(embed=embed)
    elif args == 'Admin Commands':
        embed = discord.Embed(title='__Admin Commands:__', description='Requires Admin On The Bot Not The Server.', color=random.choice(colors))
        embed.add_field(name='Disconnect', value='|Closes The connection To The Client|')
        embed.add_field(name='Prune', value='|Deletes messages. Min. 1, Max. 99|')
        embed.add_field(name='e', value='|Evaluates Arbitrary Py Code|')
        embed.add_field(name='leaveserver', value='|Leaves Server With SID|')
        embed.add_field(name='newnick', value='|Changes A Users Nickname|')
        embed.add_field(name='restart', value='|Restarts The Bot|')
        embed.add_field(name='test', value='|Bots Latency|')
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        embed.set_footer(text='Requested By {}'.format(ctx.message.author))
        await client.say(embed=embed)
    elif args == 'Developer Commands':
        embed = discord.Embed(title='__Developer Commands:__', color=random.choice(colors))
        embed.add_field(name='CC', value='|Creates A Text Channel. -CC <SID> <channel name>|')
        embed.add_field(name='Load', value='|Loads A Cog|')
        embed.add_field(name='Reload', value='|Reloads a cog|')
        embed.add_field(name='Unload', value='|Unloads a Cog|')
        embed.add_field(name='Set_Prefix', value='|Changes Bots Prefix|')
        embed.add_field(name='Unban', value='|Unbans A User. -Unban <UID>|')
        embed.add_field(name='giverole', value='|Assigns A Role To A User|')
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        embed.set_footer(text='Requested By {}'.format(ctx.message.author))
        await client.say(embed=embed)
    elif args == 'Fun Commands':
        embed = discord.Embed(title='__Fun Commands:__', color=random.choice(colors))
        embed.add_field(name='NSFWgif', value='|Random NSFW gif|', inline=True)
        embed.add_field(name='Server', value='|Client Server Info. Available args: \'Name\', \'ID\'|', inline=True)
        embed.add_field(name='add', value='|Adds Two Numbers. -add 2 2|', inline=True)
        embed.add_field(name='announce', value='Embeds Input')
        embed.add_field(name='clap', value='|Try it out|', inline=True)
        embed.add_field(name='clearnicks', value='|Clears NickNames Server Wide|', inline=True)
        embed.add_field(name='dog', value='|Random Dog Pic|')
        embed.add_field(name='format', value='|3 Ticks Input|', inline=True)
        embed.add_field(name='fuck', value='|Changes All Nicknames(needs permissions)|')
        embed.add_field(name='gayrate', value='|Gayrate machine. Defaults To Author If No User Provided|', inline=True)
        embed.add_field(name='pfp', value='|Sends Users Profile Pic. Defaults To Author If No User Provided|', inline=True)
        embed.add_field(name='rolldice', value='|Rolls|')
        embed.add_field(name='urban', value='|Searches Term On Urban Dict|', inline=True)
        embed.add_field(name='mobile', value='|Gives Mobile Role|')
        embed.add_field(name='pc', value='|Gives PC Role|')
        embed.add_field(name='xbox', value='|Gives Xbox Role|')
        embed.add_field(name='playstation', value='|Gives Playstation Role|')
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        embed.set_footer(text='Requested By {}'.format(ctx.message.author))
        await client.say(embed=embed)
    elif args == 'Info Commands': 
        embed = discord.Embed(title='__Info Commands:__', color=random.choice(colors))
        embed.add_field(name='botinfo', value='|Displays Client Info|')
        embed.add_field(name='info', value='|Users Info. Defaults To Author if No User Provided|')
        embed.add_field(name='serverinfo', value='|Displays Server Info|')
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        embed.set_footer(text='Requested By {}'.format(ctx.message.author))
        await client.say(embed=embed)
    elif args == 'Moderation':
        embed = discord.Embed(title='__Moderation:__', color=random.choice(colors))
        embed.add_field(name='Kick', value='|Kicks user|')
        embed.add_field(name='ban', value='|Bans User. Must Provide A Reason|')
        embed.add_field(name='invite', value='|Creates Invite|')
        embed.add_field(name='invitebot', value='|Bot Invite Link|', inline = True)
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        embed.set_footer(text='Requested By {}'.format(ctx.message.author))
        await client.say(embed=embed)
    elif args == 'Money':
        embed = discord.Embed(title='__Money:__', description='```Under Development```', color=random.choice(colors))
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        embed.set_footer(text='Requested By {}'.format(ctx.message.author))
        await client.say(embed=embed)
    elif args == 'No Category':
        embed = discord.Embed(title='__No Category:__', color=random.choice(colors))
        embed.add_field(name='help', value='|Lists Extensions|')
        embed.add_field(name='Lockdown', value='|Puts The Server On Lockdown. No One Can Join.|')
        embed.add_field(name='DisableLockdown', value='|Disables Server Lockdown|')
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        embed.set_footer(text='Requested By {}'.format(ctx.message.author))
        await client.say(embed=embed)
    else:
        await client.say('Invalid Input!')


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    
    client.run('NDQ3MjAxNjk5OTcxNTk2Mjk4.DeEImg.UVs5ZyWY9iKPtOS6R-AUFygFAf8')
