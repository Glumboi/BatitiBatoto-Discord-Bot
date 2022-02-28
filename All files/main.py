import discord
import random
from discord.ext import commands
from webserver import keep_alive
import os
import embeds
import admincommands
import memecommands
from datetime import datetime
from discord.ext.commands import has_permissions



#List of very strong words with the intention to ban these words in
#discord channels
badWords = []

#List of discord nitro scams to delete them
Scamlinks = [
    'https://gifs-discord.com/helof', 'https://discrod.us/nitro',
    'https://dicsordgifting.xyz/gift/r0mwdFjqL3', 'dicsordgifting.com',
    'discord-nitrogift.com', 'steamcommunutiy.com', 'app-discord.com',
    'freenitrol.ru', 'nitro-drop.com', 'disrcod.gifts', 'discord-gifts.com',
    'come-nitro.com', 'discord-promo.com', 'discord-gifts.org',
    'steamgivenitro.com', 'discord-airdrop.com', 'discord-nltro.com',
    'dlscord.wiki', 'discod.info', 'steamcommunrlity.com',
    'nitro-discord.store', 'dlscord.in', 'giveawayd.shop', 'dlscord.org',
    'discordgift.org', 'discord-nitro.info', 'discordnitro.live',
    'injectbox.com', 'discordnitro.link', 'injectx.co', 'psp-haxors.com',
    'stearncommunity.com', 'steamcomminuty.com', 'steamnitro.com',
    'steamnitros.com', 'stearncomminytu.com', 'freenitro.ru', 'giveawey.com',
    'gave-nitro.com', 'discord-app.ru', 'discord-app.net', 'discorclsteam.com',
    'steamdlscord.com', 'discrod-app.ru', 'discord-app.net', 'discord-give.com'
]

#sum cringe stuff here (the bot will react with a meme called "Oh no cringe")
cringewords = []

#sus words here (bot will respond with a meme called "the rock sus")
suswords = []

#the rock gifs
the_rock_memes = [
    'https://c.tenor.com/GjQ3YL3zCVsAAAAC/wwe-the-rock.gif',
    'https://c.tenor.com/k4TgrD7WDaUAAAAC/the-rock-face.gif',
    'https://c.tenor.com/9swGRuA4tNYAAAAC/sussy-the-rock.gif',
    'https://c.tenor.com/VmxCjy966YwAAAAd/the-wok-the-rock.gif'
]

#list of pictures used in a secret command (sum meme stuff)
driplist = [
    'Pics/Drip.png', 'Pics/Drip2.png', 'Pics/Drip3.png', 'Pics/Drip4.png',
    'Pics/Drip5.png', 'Pics/Drip6.png', 'Pics/Drip7.png', 'Pics/Drip8.png',
    'Pics/Drip9.png'
]

#list of pictures used in a secret command (sum meme stuff)
floppalist = [
    'Pics/floppa1.png', 'Pics/floppa2.png', 'Pics/floppa3.png',
    'Pics/floppa4.png', 'Pics/floppa5.png'
]

#list of words to say when a very strong word was texted
StopWords = [
    'Stop using such bad words!', 'Stop that!!', 'Please dont say that!',
    'We dont want such bad words in the chat!',
    'Dont say that! Be nice to everybody.'
]


#list of pictures used in a secret command (this is a little insider from my friend and me so you can delete it if you want)
box = ['Pics/box.png', 'Pics/box2.png']
#cogs
cogs = [embeds, admincommands, memecommands]
#client and prefix
client = commands.Bot(command_prefix='!',
                      intents=discord.Intents.all(),
                      help_command=None)

for i in range(len(cogs)):
    cogs[i].setup(client)


#explains itself
@client.event
async def on_ready():
    print('Bot is ready to use!')
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Game('Type !info or !help for help/info abt me!'))
@client.command()
async def roles(ctx):
    embed = discord.Embed(
        title="Reaction Roles",
        description="React with an emoji to get a role",
        color=discord.Color.random(),
        timestamp=datetime.now())
    embed.set_author(name="BatitiBatoto role reaction",
                     icon_url=ctx.guild.icon_url)
    embed.add_field(name="💻", value="PC", inline=True)
    embed.add_field(name="🟦", value="Playstation", inline=True)
    embed.add_field(name="🎮", value="XBOX", inline=True)
    embed.add_field(name="🐐", value="Gamer", inline=True)
    embed.add_field(name="⌨️", value="Programmer", inline=True)
    embed.add_field(name="🥶", value="Active Person", inline=True)
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('💻')
    await msg.add_reaction('🟦')
    await msg.add_reaction('🎮')
    await msg.add_reaction('🐐')
    await msg.add_reaction('⌨️')
    await msg.add_reaction('🥶')


@client.event
async def on_raw_reaction_add(payload):
    ourMessageID = 941334810843025410

    if ourMessageID == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name
        if emoji == '💻':
            mrole = discord.utils.get(guild.roles, name='PC')
            await member.add_roles(mrole)
            print('Added a role to someone')
        if emoji == '🟦':
            mrole = discord.utils.get(guild.roles, name='Playstation')
            await member.add_roles(mrole)
            print('Added a role to someone')
        if emoji == '🎮':
            mrole = discord.utils.get(guild.roles, name='XBOX')
            await member.add_roles(mrole)
            print('Added a role to someone')
        if emoji == '🐐':
            mrole = discord.utils.get(guild.roles, name='Gamer')
            await member.add_roles(mrole)
            print('Added a role to someone')
        if emoji == '⌨️':
            mrole = discord.utils.get(guild.roles, name='Programmer')
            await member.add_roles(mrole)
            print('Added a role to someone')
        if emoji == '🥶':
            mrole = discord.utils.get(guild.roles, name='Active Person')
            await member.add_roles(mrole)
            print('Added a role to someone')

#message event (looks for content in a message such as very strong words)
@client.event
async def on_message(ctx):
    print(
        str(ctx.author) + ' said at ' + str(datetime.now()) + ': ' +
        ctx.content)
    await client.process_commands(ctx)

    if ctx.content == "floppa":
        randomPic = random.choice(floppalist)
        await ctx.reply(file=discord.File(randomPic))

    if ctx.content == "box":
        randomPic = random.choice(box)
        await ctx.reply(file=discord.File(randomPic))

    if ctx.content == "drip":
        Random = random.choice(driplist)
        await ctx.reply(file=discord.File(Random))

    if ctx.content.startswith("Hello Batiti"):
        author = str(ctx.author)
        await ctx.reply('Hello ' + author + '!')

    if ctx.content.startswith("amogus"):
        embed = discord.Embed(title='Amogus', description=' ')
        embed.set_image(
            url=
            'https://c.tenor.com/h99LQHUExJIAAAAd/19dollar-fortnite-card-among-us.gif'
        )
        await ctx.reply(embed=embed)

    if any(word.lower() in ctx.content.lower().replace(' ', '')
           for word in badWords):
        await ctx.delete()
        await ctx.channel.send(
            str(ctx.author.mention) + ' ' + random.choice(StopWords))

    if any(word.lower() in ctx.content.lower().replace(' ', '')
           for word in cringewords):
        cringeembed = discord.Embed(title='oh no cringe',
                                    description=' ',
                                    color=0xB6FF00)
        cringeembed.set_image(url='https://i.imgflip.com/5te4i0.jpg')
        await ctx.reply(embed=cringeembed)

    if any(word.lower() in ctx.content.lower().replace(' ', '')
           for word in suswords):
        susembed = discord.Embed(title='SUS',
                                 description=' ',
                                 color=discord.Color.random())
        susembed.set_image(url=random.choice(the_rock_memes))
        await ctx.reply(embed=susembed)
    if any(word.lower() in ctx.content.lower().replace(' ', '')
           for word in Scamlinks):
        scamembed = discord.Embed(title='Scam detected!',
                                  description=' ',
                                  color=discord.Color(0xFF0000))
        scamembed.set_thumbnail(
            url=
            'https://cdn.pixabay.com/photo/2012/04/12/22/25/warning-sign-30915__340.png'
        )
        await ctx.reply(embed=scamembed)
        await ctx.delete()


#Profilepic command sends the profile picture of the bot
@client.command(aliases=['PROFILEPIC'])
async def profilepic(ctx):
    await ctx.reply(file=discord.File('Pics/ProfilePic.png'))

#Keep alive is used for net stuff
keep_alive()
TOKEN = os.environ.get("TOKEN")
client.run(TOKEN)