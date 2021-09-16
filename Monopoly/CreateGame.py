from DiscordMiddleMan import client
import re

games = {}

class CreateGame:
    propertiesPlayers= {}
    
    def __init__(self, players, owner, message, debug):
        self.MaxPlayers = players
        self.CurrentPlayers = 0
        self.owner = owner
        self.id = owner
        self.playersId = [owner]
        self.propertiesPlayers[owner] = 0

    async def Create(idPlayer, players, message, debug):
        if(len([x for x in games.values() if idPlayer in x.playersId])==0):
            games[idPlayer] = (CreateGame(players=int(players), owner=idPlayer, message=message, debug = debug))
            await games[idPlayer].Announcement(message, debug)
        else:
            if debug: return
            await message.channel.send("You are in a game already")

    async def Announcement(self, message, debug):
        print("{0} made a game".format(self.owner))
        if debug: return
        await message.channel.send(
            "Next {0} persons that type !Join <@{1}> will join the game!".format(self.MaxPlayers, self.owner))

    async def Join(message, idPlayer, debug):
        if(len([x for x in games.values() if idPlayer in x.playersId])==0):
            _regexForId = re.search("(<@!+[0-9])\w+",message)[0]
            idGame = int(re.search("([0-9])\w+",_regexForId)[0])
            if idGame in games:
                game = games[idGame]
                await game.Joining(message,idPlayer, debug)
            else:
                if debug: return
                await message.channel.send("That person is not making a game right now")
        else:
            if debug: return
            await message.channel.send("{}, you are in a game already")

    async def Joining(self, message,idPlayer, debug):
        self.playersId.append(idPlayer)
        self.propertiesPlayers[idPlayer] = 0
        self.CurrentPlayers += 1
        if self.CurrentPlayers >= self.MaxPlayers:
            if debug: return 
            await message.channel.send(
                "{0.author}´s game is full already".format(message))
        else:
            print("{0}'s game has started".format(self.owner))
            if debug: return 
            await message.channel.send("<@{0.author.id}> just joined! {1} to go!".format(
                message, str(self.MaxPlayers-self.CurrentPlayers)))
            if self.CurrentPlayers == self.MaxPlayers:
                await message.channel.send("{0.author}´s game is full and starting".format(
                message, str(self.MaxPlayers-self.CurrentPlayers)))
                ###Crear dm grupal o canal 















































