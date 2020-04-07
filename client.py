import discord
from discord.ext import commands
from googlesearch import search
import os
from dotenv import load_dotenv

load_dotenv()

SERVER_TOKEN = os.getenv("SERVER_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

load_dotenv()

Client = discord.Client()

client=commands.Bot(command_prefix="!")

channel = Client.get_guild(CHANNEL_ID)

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
                                   "- Faire une __recherche google :__ (3 premiers résultats) **'!google: [recherche]'**\n"
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

client.run(SERVER_TOKEN)

