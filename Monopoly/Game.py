from DiscordMiddleMan import client

Data = {}

GameBoard = {
    "0": {
        "Name": "Something",
        "Owner": 0,
        "Cost": 5000,
        "HouseCost": 6000,
        "Houses": 0,
        "Hotel": False,
        "Fee": 3000,
    },
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


}

class Game():
    def __init__(self, players, channelid):
        self.Gameid = 0
        self.Players = players
        self.channelid = channelid
        self.AddChannel()

    def AddChannel(self):
        Data[self.channelid] = {}
        Data[self.channelid][0] = Board(self.channelid, GameBoard)
        for player in self.Players:
            Data[self.channelid][player] = Player(player, self.channelid)

    
        



class Player():
    def __init__(self, playerid, channelid):
        self.Playerid = playerid
        self.Channelid = channelid
        self.Money = 0
        self.Position = 0

    def Roll(self):
        pass
    def GiveMoney(self, player, money):
        if (self.Money - money) > 0:
            Data[self.Channelid][player].GetMoney(self.Playerid, money)
            self.Money -= money
        else:
            self.SendMessage("You dont have enough money")

    def GetMoney(self, player, money):
        self.Money += money
    def BuyPropertie(self, player):
        pass
    def SellPropertie(self, player):
        pass
    async def SendMessage(self,message):
        _VarForChannel = await client.fetch_channel(self.Channelid)
        _VarForMember = await client.fetch_user(self.Playerid)
        _VarForChannel.send("{1.name}, {0}".format(message, _VarForMember))



class Board():
    def __init__(self, channelid, gameboard):
        self.channelid = channelid
        self.gameboard = gameboard.copy()
        self.money = 9999999
        self.jail  = {}

    def DisplayCell(self, cell):
        pass
    def GetMoney(self, player):
        pass
    def GiveMoney(self, player):
        pass
    async def SendMessage(self,message):
        _VarForChannel = await client.fetch_channel(self.Channelid)
        _VarForChannel.send("Bank, {message}".format(message))



