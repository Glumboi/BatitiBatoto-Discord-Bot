import discord
import json
from requests import get
import aiohttp
import asyncio
import reddit as reddit
from discord.ext import commands

#this class is for sending memes like in the danke memer bot

class memecommands(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    #!meme will only work in a certaih channel/server but it needs to be built into the bot
    @commands.command(aliases=['MEME'])
    async def meme(self, ctx):
        icon_url = ctx.guild.icon_url
        memeAPI = "https://meme-api.herokuapp.com/gimme/dankmemes"
        content = get("https://meme-api.herokuapp.com/gimme").text
        data = json.loads(content, )
        meme = discord.Embed(
            title=f"{data['title']}",
            Color=discord.Color.random()).set_image(url=f"{data['url']}")
        meme.set_thumbnail(url=icon_url)
        if ctx.guild.id == :
            channel = self.client.get_channel(
                )
            await channel.send(embed=meme)
        if ctx.guild.id == :
            channel2 = self.client.get_channel()
            await channel2.send(embed=meme)
        if ctx.guild.id == :
            channel3 = self.client.get_channel()
            await channel3.send(embed=meme)

    #memehere is for every server and every channel 
    @commands.command(aliases=['MEMEHERE'])
    async def memehere(self, ctx):
        memeAPI = "https://meme-api.herokuapp.com/gimme/dankmemes"
        content = get("https://meme-api.herokuapp.com/gimme").text
        data = json.loads(content, )
        meme = discord.Embed(
            title=f"{data['title']}",
            Color=discord.Color.random()).set_image(url=f"{data['url']}")
        await ctx.reply(embed=meme)

#for the cogs in the main.py
def setup(client):
    client.add_cog(memecommands(client))
