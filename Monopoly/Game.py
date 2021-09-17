from DiscordMiddleMan import client

Data = {}
        

class Game():
    def __init__(self, players, channelid):
        self.Gameid = 0
        self.Board = []
        self.Players = players
        self.Maxplayers = len(players)
        self.channelid = channelid

    def AddPlayersToChannel(self):
        Data[self.channelid] = []
        for k in self.Players:
            Data[self.channelid].append(k)
        return


    

    

class Player(Game):
    def __init__(self,players,channelid):
        super().__init__(players,channelid)
        self.Playerid = 0







games = 0

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