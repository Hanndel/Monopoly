from logging import exception
import time
import os
import discord
import asyncio
client = discord.Client()
# Al formatear se jode, hay que ponerlo debajo del cliente si o si
from CreateGame import *
from Game import GameData


debug = True
DelayThread = None


async def CallADelay(delay, func):
    await asyncio.sleep(delay)
    return await func()

async def FetchMessagesFromConsole():
    while True:
        message = input()
        _VarForChannel = await client.fetch_channel(864644094343905294)
        await _VarForChannel.send(message)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    #Multithreading in asyncio

    # Tests
    _VarForGuild = client.guilds[0]
    for k in client.get_all_channels():
        if k.name in ["hanndels-game", "revivers-game"]:
            await k.delete()
    _VarForChannel = await client.fetch_channel(864644094343905294)
    try:
        #await CreateGame.Create(509718122488659979, 2, _VarForChannel, debug)
        pass
        #await CreateGame.Join("<@!509718122488659979", 371776838491701258, _VarForGuild, _VarForChannel, True)
    except:
        await _VarForChannel.send("Something went wrong while creating the game, please , try again")
    Embed = discord.Embed()
    Color = discord.Color.teal()
    Embed.title = "test"
    Embed.type = "rich"
    Embed.description = "this is a test"
    Embed.set_author(name="Hanndel", url="https://github.com/Hanndel/Monopoly")
    Embed.colour = Color
    Embed.add_field(name="ak", value="asd")
    ak = Embed.to_dict()
    print(ak)
    #await _VarForChannel.send(embed = Embed)
    loop = asyncio.get_event_loop()
    asyncio.run_coroutine_threadsafe(FetchMessagesFromConsole(), loop)

@client.event
async def on_message(message):
    # Making sure author is not a bot
    if message.author.bot: return
    print("message recieved",message.content, "From, {0}".format(message.author.name))

    # Start a new game
    if message.content.startswith("!Create"):
        try:
            await CreateGame.Create(
                message.author.id, message.content.split()[1], message.channel, debug)

        except:
            await message.channel.send(
                "Something went wrong while creating the game, please , try again")

    # Join an existing game
    if message.content.startswith("!Join"):
        await CreateGame.Join(
            message.content, message.author.id, message.guild, message.channel, True)

    # Roll once you are inside a game
    if message.content.startswith("!Roll"):
        try:
            GameData[message.channel.id][message.author.id].Roll()
        except KeyError:
            await message.delete()
            _aware_message_to_delete = await message.channel.send("Wrong channel, or you are not in a game")
            #Multithreading in asyncio
            loop = asyncio.get_event_loop()
            asyncio.run_coroutine_threadsafe(CallADelay(
                2, _aware_message_to_delete.delete), loop)


route = os.getcwdb()
token = open(route+b"/Monopoly/token.txt", "r")
client.run(token.read())
