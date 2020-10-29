import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from googletrans import Translator
from textgenrnn import textgenrnn

translator = Translator()


load_dotenv()
token = os.getenv('DISCORD_TOKEN') 

client = discord.Client()

def neuralQuote(num):
    if int(num) < 21:
        textgen_2 = textgenrnn('textgenrnn_weights.hdf5')
        value = textgen_2.generate(int(num), return_as_list=True) 
        return value
    else:
        print("in else")

    
def trans(msg):
    lang = msg.split()[0]
    text = " ".join(msg.split()[1:])
    print(text)
    print(lang)
    try:
        translated = translator.translate(text, dest=lang)
        return translated.text
    
    except ValueError as e:
        return e
    
    except:
        unknown = "unexpected error has occured."
        return unknown    


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord')


@client.event
async def on_message(message):
    if '!t' in message.content.lower():
        text = message.content
        text = text.replace("!t","")
        translated = trans(text)
        await message.channel.send(translated)

    if '!q' in message.content.lower():
        text = message.content
        text = text.replace("!q","")
        text = text.strip(" ")
        quoteRequest = neuralQuote(text)
        if len(quoteRequest) >= 1:
            for quote in quoteRequest:
                await message.channel.send(quote)
        else:
            await message.channel.send(quoteRequest)
        
client.run(token)
