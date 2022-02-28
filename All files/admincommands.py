import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

#in this class are commands that requiere cetain permissions

class admincommands(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['KICK'])
  @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
  async def kick(self, ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.reply(f'User {member.mention} has been kicked!')
    print(f'User {member} has been kicked and logged on console!')


  @commands.command(aliases=['BAN'])
  @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
  async def ban(self, ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.reply(f'User {member.mention} has been banned!')
    print(f'User {member} has been banend and logged on console!')

  @commands.command(aliases=['UNBAN'])
  @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
  async def unban(self, ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
      user = ban_entry.user

      if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.reply(f'{user.mention} has been unbanned!')
        return

  @commands.command(aliases=['MUTE'])
  @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
  async def mute(self, ctx, member: discord.Member, *, reason=None):
    roles = discord.utils.get(ctx.guild.roles, name=['Stille Treppe / Silent Stair', 'Bonus+ / Discord Nitro', 'Stille Treppe / Silent Stair'])
    await member.remove_roles(roles)
    await ctx.reply(f'User {member.mention} has been muted!')
    print(f'User {member} has been muted and logged on console!')

  @commands.command(aliases=['UNMUTE'])
  @has_permissions(administrator=True, manage_messages=True, manage_roles=True)
  async def unmute(self, ctx, member: discord.Member, *, reason=None):
    role1 = discord.utils.get(ctx.guild.roles, name=['Stille Treppe / Silent Stair', 'Bonus+ / Discord Nitro', 'Stille Treppe / Silent Stair'])
    await member.add_roles(role1)
    await ctx.reply(f'User {member.mention} has been unmuted!')
    print(f'User {member} has been unmuted and logged on console!')

  @commands.command(aliases=['CLEAR'])
  @has_permissions(manage_messages=True)
  async def clear(self, ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    print(str(amount) + ' messages have been cleared')

  

#for the cogs in the main.py 
def setup(client):
  client.add_cog(admincommands(client))