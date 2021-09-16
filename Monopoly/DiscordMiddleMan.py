import discord
import os
import time

client = discord.Client()
from CreateGame import *

debug = True

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print(client.guilds)
    await CreateGame.Create(371776838491701258, 2, "message", True) ### Mensaje de test
    time.sleep(2)
    await CreateGame.Join("<@!371776838491701258", 509718122488659979, True) ### Mensaje de test

@client.event
async def on_message(message):
    if message.content.startswith("!Create"):
        await CreateGame.Create(message.author.id, message.content.split()[1], message, debug) ###Mensaje normal
        ###ToDo
        ###Arreglar create null
        ###Arreglar confirmar int
    if message.content.startswith("!Join"):
        await CreateGame.Join(message, message.author.id, debug) ###Mensaje normal


route = os.getcwdb()
token = open(route+b"/Monopoly/token.txt", "r")
client.run(token.read())
