from DiscordMiddleMan import client
import random   
#Games that are running 
GameData = {}
#Board
GameBoard = {
    "1": {
        "Name": "Something",
        "Owner": 0,
        "Cost": 5000,
        "HouseCost": 6000,
        "Houses": 0,
        "Hotel": False,
        "Fee": 3000,
    },
    "2": {
        "Name": "Something",
        "Owner": 0,
        "Cost": 5000,
        "HouseCost": 6000,
        "Houses": 0,
        "Hotel": False,
        "Fee": 3000,
    },
    "3": {
        "Name": "Something",
        "Owner": 0,
        "Cost": 5000,
        "HouseCost": 6000,
        "Houses": 0,
        "Hotel": False,
        "Fee": 3000,
    },
    "4": {
        "Name": "Something",
        "Owner": 0,
        "Cost": 5000,
        "HouseCost": 6000,
        "Houses": 0,
        "Hotel": False,
        "Fee": 3000,
    },
    "5": {
        "Name": "Something",
        "Owner": 0,
        "Cost": 5000,
        "HouseCost": 6000,
        "Houses": 0,
        "Hotel": False,
        "Fee": 3000,
    },
    "6": {
        "Name": "Something",
        "Owner": 0,
        "Cost": 5000,
        "HouseCost": 6000,
        "Houses": 0,
        "Hotel": False,
        "Fee": 3000,
    },
    "7": {
        "Name": "Something",
        "Owner": 0,
        "Cost": 5000,
        "HouseCost": 6000,
        "Houses": 0,
        "Hotel": False,
        "Fee": 3000,
    },
    "8": {
        "Name": "Something",
        "Owner": 0,
        "Cost": 5000,
        "HouseCost": 6000,
        "Houses": 0,
        "Hotel": False,
        "Fee": 3000,
    },
    "9": {
        "Name": "Something",
        "Owner": 0,
        "Cost": 5000,
        "HouseCost": 6000,
        "Houses": 0,
        "Hotel": False,
        "Fee": 3000,
    },
    "10": {
        "Name": "Something",
        "Owner": 0,
        "Cost": 5000,
        "HouseCost": 6000,
        "Houses": 0,
        "Hotel": False,
        "Fee": 3000,
    },
    "11": {
        "Name": "Something",
        "Owner": 0,
        "Cost": 5000,
        "HouseCost": 6000,
        "Houses": 0,
        "Hotel": False,
        "Fee": 3000,
    },
    "12": {
        "Name": "Something",
        "Owner": 0,
        "Cost": 5000,
        "HouseCost": 6000,
        "Houses": 0,
        "Hotel": False,
        "Fee": 3000,
    },
    


}
#Class to
class Game():
    def __init__(self, players, channelid):
        self.Gameid = 0
        self.Players = players
        self.channelid = channelid
        self.AddChannel()

    def AddChannel(self):
        GameData[self.channelid] = {}
        GameData[self.channelid][self.channelid] = Board(self.channelid, GameBoard)
        for player in self.Players:
            GameData[self.channelid][player] = Player(player, self.channelid)

    
        



class Player():
    def __init__(self, playerid, channelid):
        self.Playerid = playerid
        self.Channelid = channelid
        self.Money = 500000
        self.Position = 0
        self.Jail = False
        self.Properties = {}

    def Roll(self):
        rolled = random.randint(1, 6)
        GameData[self.Channelid][self.Channelid].MovePlayer(self.Playerid, rolled)

    def GiveMoney(self, player, money):
        if (self.Money - money) > 0:
            GameData[self.Channelid][player].GetMoney(money)
            self.Money -= money
        else:
            self.SendMessage("You dont have enough money")

    def GetMoney(self, money):
        self.Money += money

    def BuyPropertie(self, player):
        pass

    def SellPropertie(self, player):
        pass

    def GoToJail(self):
        self.Jail = True
        GameData[self.Channelid][self.Channelid].WentToJail(self.Playerid)

    def OutOfJail(self):
        self.Jail = False
        GameData[self.Channelid][self.Channelid].KickFromJail(self.Playerid)

    async def SendMessage(self,message):
        _VarForChannel = await client.fetch_channel(self.Channelid)
        _VarForMember = await client.fetch_user(self.Playerid)
        _VarForChannel.send("{1.name}, {0}".format(message, _VarForMember))



class Board():
    def __init__(self, channelid, gameboard):
        self.channelid = channelid
        self.Playerid = channelid
        self.gameboard = gameboard.copy()
        self.BoardApropiation()
        self.money = 9999999
        self.jail  = {}
        self.playersPos = {}

    def DisplayCell(self, cell):
        pass

    def GetMoney(self, money):
        self.money += money

    def GiveMoney(self,player, money):
        GameData[self.channelid][player].GetMoney(money)

    def WentToJail(self, player):
        self.jail[player] = True

    def KickFromJail(self, player):
        self.jail[player] = False

    def Moveplayer(self, player, roll):
        x = 25
        if (self.playersPos[player]+roll) > x:
            self.playersPos[player] = x-self.playersPos[player]
            self.GiveMoney(player, 50000)
        else:
            self.playersPos[player] += roll
        pass

    async def SendMessage(self,message):
        _VarForChannel = await client.fetch_channel(self.Channelid)
        _VarForChannel.send("Bank, {message}".format(message))

    def BoardApropiation(self):
        for cell in self.gameboard:
            self.gameboard[cell]["Owner"] = self.channelid
        for player in GameData[self.Channelid]:
            self.playersPos[player] = 1

    def MakeEmbed(self, reason):
        embed = {
            'author': {
                'name': 'Hanndel',
                'url': 'https://github.com/Hanndel/Monopoly'
            }, 
            'color': 1752220, 
            'type': 'rich', 
            'description': '{0}'.format(reason), 
            'title': 'Monopoly!'
        },


        pass



