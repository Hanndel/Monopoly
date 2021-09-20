from DiscordMiddleMan import client

Data = {}

GameBoard = {
    "0": {
        "owner": "Bank",
        "Cost": 5000,
        "HouseCost": 6000,
        "Houses": 0,
        "Hotel": False,
        "Fee": 3000,
    }
}

Recipes = {
    "CopperWire": {
        "Requires": {
            "CopperBar": 1
        }
    },
    "Circuit": {
        "Requires":{
            "CopperWire": 5,
            "IronBar": 2,
            "SiliconBar": 2
        }
    }
}

class Game():
    def __init__(self, players, channelid):
        self.Gameid = 0
        self.Players = players
        self.channelid = channelid
        self.AddChannel()

    def AddChannel(self):
        Data[self.channelid] = {}
        Data[self.channelid][self.channelid] = Board(self.channelid)
        for player in self.Players:
            Data[self.channelid][player] = Player(player, self.channelid)

    
        



class Player():
    def __init__(self, playerid, channelid):
        self.playerid = playerid
        self.channelid = channelid
        pass

    def Roll(self):
        print("RolledHEHE")


class Board():
    def __init__(self, channelid):
        pass



        







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