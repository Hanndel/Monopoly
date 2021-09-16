import time
import os
import discord
client = discord.Client()
from CreateGame import * #Al formatear se jode, hay que ponerlo debajo del cliente si o si

debug = True


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    _VarForGuild = client.guilds[0]  # Solo para tests
    await CreateGame.Create(509718122488659979, 2, 0, debug)  # Mensaje de test
    time.sleep(2)
    await CreateGame.Join("<@!509718122488659979", 371776838491701258, _VarForGuild, 0, True)


@client.event
async def on_message(message):
    if message.content.startswith("!Create"):
        # Mensaje normal
        await CreateGame.Create(message.author.id, message.content.split()[1], message.channel, debug)
        # ToDo
        # Arreglar create null
        # Arreglar confirmar int
    if message.content.startswith("!Join"):
        # Mensaje normal
        await CreateGame.Join(message.content, message.author.id, message.guild, message.channel, True)

@client.event
async def on_guild(guild):
    print("a")

@client.event
async def on_member_join(member):
    print("a")

@client.event
async def on_guild_join(guild):
    print("a")  
    

route = os.getcwdb()
token = open(route+b"/Monopoly/token.txt", "r")
client.run(token.read())
