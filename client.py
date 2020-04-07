import discord
import pyninegag
from discord.ext import commands
import json
import simplejson
from urllib import request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re
import requests
from googlesearch import search

# AIzaSyAPfd60CrXhRTUPonnPBKrsuWI2aTOBjfA

Client = discord.Client()

client=commands.Bot(command_prefix="!")

channel = Client.get_guild(696739378826969228)

Token="Njk2NzMwNDAyMDgxMDc5Mzg2.XotAnQ.J7qCX3e3BGgJ2Ua5k4CrNom4Pfo"

WEBHOOK_URL = "https://discordapp.com/api/webhooks/696746111679070259/r2rUADf_EVOMGvoJvO5biEIzfhiuE0NTgrlQ9QjCBzcXbEcZtVo3KGkH-bAPbpzFFuCv"

# Les paramètres d'en-tête de la requête
headers = {
    'Content-Type': 'application/json',
    'user-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
}
         
@client.event
async def on_ready():
    print("Op is ready")

@client.event
async def on_message(message):

    if message.content.startswith('!commands'):
        await message.channel.send("**Commandes du bot :**\n\n"
                                   "- Recherches google : **'!google: [recherche]'**\n"
                                   "- ")

    if message.content.startswith('!google'):

        query = message.content.split(': ')

        for i in search(query[1],  # The query you want to run
                        tld='com',  # The top level domain
                        lang='fr',  # The language
                        num=3,  # Number of results per page
                        start=0,  # First result to retrieve
                        stop=3,  # Last result to retrieve
                        pause=2.0,  # Lapse between HTTP requests
                        ):
            await message.channel.send(i)

client.run(Token)

