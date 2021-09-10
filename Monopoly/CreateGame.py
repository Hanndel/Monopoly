from DiscordMiddleMan import client
from Game import Game
import re
games = {}

async def Create(idPlayer, players, message):
    if(len([x for x in games.values() if idPlayer in x.playersId])==0):
        games[idPlayer] = (Game(players=int(players), owner=idPlayer, message=message))
        await games[idPlayer].Announcement(message)
    else:
        await message.channel.send("You are in a game already")
        
async def Join(message, idPlayer):
    if(len([x for x in games.values() if idPlayer in x.playersId])==0):
        _regexForId = re.search("(<@!+[0-9])\w+",message.content)[0]
        idGame = int(re.search("([0-9])\w+",_regexForId)[0])
        if idGame in games:
            game = games[idGame]
            await game.Joining(message,idPlayer)
        else:
            await message.channel.send("That person is not making a game right now")
    else:
        await message.channel.send("{}, you are in a game already")
        
async def Interactuate(message,idPlayer):
    gamesList = [x for x in games.values() if idPlayer in x.playersId]
    if(len(gamesList)>0):
        game = gamesList[0]
        ##comprobar accion aqui o pasar id accion y comprobar cual es en Game.py
        ##comprobar accion aqui o pasar id accion y comprobar cual es en Game.py
        game.ComprarPropiedad(idPlayer)
    else:
        await message.channel.send("You are not in a game currently")















































