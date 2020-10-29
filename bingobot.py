import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
from googletrans import Translator
translator = Translator()

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()
            
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')


@client.event
async def on_message(message):
    if '!translate' in message.content.lower():
        await message.channel.send(ctx.message.content)


    if 'fav that' in message.content.lower():

        await message.channel.send('Possum pic added to favorites!')
        
    if 'post fav possums' in message.content.lower():
        await message.channel.send(file=file)


        
client.run(token)

