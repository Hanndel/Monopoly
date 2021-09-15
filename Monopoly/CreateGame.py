from DiscordMiddleMan import client
import re

games = {}

class Game:
    propertiesPlayers= {}
    
    def __init__(self, players, owner, message):
        self.MaxPlayers = players
        self.CurrentPlayers = 0
        self.owner = owner
        self.id = owner
        self.playersId = [owner]
        self.propertiesPlayers[owner] = 0

    async def Announcement(self, message):
        await message.channel.send(
            "Next {0} persons that type !Join <@{1}> will join the game!".format(self.MaxPlayers, self.owner))

    def GameOn(self, message):
        print("debugging :)")

    async def Joining(self, message,idPlayer):
        self.playersId.append(idPlayer)
        self.propertiesPlayers[idPlayer] = 0
        self.CurrentPlayers += 1
        if self.CurrentPlayers >= self.MaxPlayers:
            await message.channel.send(
                "{0.author}´s game just started!".format(message))
            ###Crear dm grupal o canal 
        else:
            await message.channel.send("<@{0.author.id}> just joined! {1} to go!".format(
                message, str(self.MaxPlayers-self.CurrentPlayers)))

    def ComprarPropiedad(self,idPlayer):
        self.propertiesPlayers[idPlayer]+=1
        print(self.propertiesPlayers)
        return

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















































