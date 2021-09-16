from DiscordMiddleMan import client
from CreateGame import games
        
async def Interactuate(message,idPlayer):
    gamesList = [x for x in games.values() if idPlayer in x.playersId]
    if(len(gamesList)>0):
        game = gamesList[0]
        ##comprobar accion aqui o pasar id accion y comprobar cual es en Game.py
        game.ComprarPropiedad(idPlayer)
    else:
        await message.channel.send("You are not in a game currently")

def ComprarPropiedad(self,idPlayer):
    self.propertiesPlayers[idPlayer]+=1
    print(self.propertiesPlayers)
    return