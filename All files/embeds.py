import discord
from discord.ext import commands

client = commands.Bot(command_prefix='!',
                      intents=discord.Intents.all(),
                      help_command=None)

#this is the class for embeds like the !help command or !info

class embeds(commands.Cog):

  def __init__(self, client):
    self.client = client

  #sends the list of commands
  @commands.command(aliases=['HELP'])
  async def help(self,ctx):
    icon_url = ctx.guild.icon_url
    helpembed = discord.Embed(title="Help", description='You can see all my commands here. Btw i also have some hidden commands that are secret and they dont use a prefix (!)', color=0x7CFC00)
    helpembed.add_field(name='!help', value='shows this window', inline=False)
    helpembed.add_field(name='!meme', value='Posts a meme in the server memechannel(only works when the developer integrated the server in the code) so if you just want memes use !memehere.', inline=False)
    helpembed.add_field(name='!info', value='Gives you info about the bot(why the bot exists)', inline=False)
    helpembed.add_field(name='!ban', value='Only server admins can use that command as it says it bans someone how to use: !ban [@member] [reasonhere]', inline=False)
    helpembed.add_field(name='!kick', value='Only server admins can use that command as it says it kicks someone how to use: !kick [@member] [reasonhere]', inline=False)
    helpembed.add_field(name='!unban', value='Only admins can use this too how to unban: \n!unban [username#1234]', inline=False)
    helpembed.add_field(name='!memehere', value='Memehere sends a meme', inline=False)
    helpembed.add_field(name='!clear', value='Clears the chat default messages that are gettin deleted are 5 how to change: \n!clear [numberhere]', inline=False) 
    helpembed.add_field(name='!join', value='Let the bot join your voice channel (is used for music playing)', inline=False)
    helpembed.add_field(name='!play', value='Plays a YouTube video as audio (bot must be in voice channel) how to use: \n!play [https://Your Youtube url here]', inline=False) 
    helpembed.add_field(name='!members', value='Shows how many people are in the server', inline=False)
    helpembed.add_field(name='!pause', value='Puases the audio', inline=False)
    helpembed.add_field(name='!resume', value='Resumes the audio', inline=False)
    helpembed.add_field(name='!disconnect', value='Disconnects the bot from the voice channel', inline=False)
    helpembed.add_field(name='!profilepic', value='Sends you the profilepicture of the bot', inline=False)
    helpembed.add_field(name='!members', value='This command shows how many people are in the server', inline=False)
    helpembed.add_field(name='!getguildpicture', value='This command send you the image of the discord server', inline=False)
    helpembed.set_thumbnail(url=icon_url)
    await ctx.reply(embed=helpembed)

  @commands.command(aliases=['INFO'])
  async def info(self, ctx):
    icon_url = ctx.guild.icon_url
    infoembed = discord.Embed(title = 'Info', description=' ' ,color=0xFF0000)
    infoembed.add_field(name = 'What the bot is', value="I'm a bot that was made for fun and learning purpose but maybe later on it will be a public bot who knows?")
    infoembed.set_thumbnail(url=icon_url)
    await ctx.reply(embed=infoembed)

  #says how many people are in the server 
  @commands.command(aliases=['MEMBERS'])
  async def members(self,ctx):
    guild_name = ctx.guild.name
    icon_url = ctx.guild.icon_url
    embed = discord.Embed(title='Member count of: ' + guild_name, description=' ', color=0x800080)
    embed.set_thumbnail(url=icon_url)
    members = ctx.guild.member_count
    embed.add_field(name='count', value=str(members) + ' people are in the server!')
    await ctx.reply(embed=embed)

  @commands.command()
  async def embed(self, ctx):
    icon_url = ctx.guild.icon_url
    embed = discord.Embed(title='Get member role ', description=' ', color=0x800080)
    embed.set_thumbnail(url=icon_url)
    embed.add_field(value='react with ✅', name='test')
    await ctx.send(embed=embed)

  #sends the picture of a guild (Discord server)
  @commands.command(aliases=['GETGUILDPICTURE'])
  async def getguildpicture(self,ctx):
    icon_url = ctx.guild.icon_url
    embed=discord.Embed(title='image', description=' ', color=0xFF0000)
    embed.set_image(url=icon_url)
    await ctx.reply(embed=embed)

  #Debug command that prints every name of a person in a server including the ids of them
  @commands.command(aliases=['MEMBERSDEBUG'])
  async def membersdebug(self,ctx):
    members = ctx.guild.members
    await ctx.reply(members)
 
#for the cogs in the main.py
def setup(client):
  client.add_cog(embeds(client))