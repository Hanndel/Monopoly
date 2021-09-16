from DiscordMiddleMan import client
import re

games = {}


class CreateGame:
    propertiesPlayers = {}

    def __init__(self, players, owner, channel, debug):
        self.MaxPlayers = players
        self.CurrentPlayers = 0
        self.owner = owner
        self.id = owner
        self.playersId = [owner]
        self.propertiesPlayers[owner] = 0

    async def Create(idPlayer, players, channel, debug):
        if(len([x for x in games.values() if idPlayer in x.playersId]) == 0):
            games[idPlayer] = (CreateGame(players=int(
                players), owner=idPlayer, channel=channel, debug=debug))
            await games[idPlayer].Announcement(channel, debug)
        else:
            if debug:
                return
            await channel.send("You are in a game already")

    async def Announcement(self, channel, debug):
        print("{0} made a game".format(self.owner))
        if debug:
            return
        await channel.send(
            "Next {0} persons that type !Join <@{1}> will join the game!".format(self.MaxPlayers, self.owner))

    async def Join(content, idPlayer,guild, channel, debug):
        if(len([x for x in games.values() if idPlayer in x.playersId]) == 0):
            _regexForId = re.search("(<@!+[0-9])\w+", content)[0]
            idGame = int(re.search("([0-9])\w+", _regexForId)[0])
            if idGame in games:
                game = games[idGame]
                await game.Joining(idPlayer=idPlayer, guild=guild, channel=channel, idGame=idGame, debug=debug)
            else:
                if debug:
                    return
                await channel.send("That person is not making a game right now")
        else:
            if debug:
                return
            await channel.send("{}, you are in a game already")

    async def Joining(self, idPlayer, idGame, guild, channel, debug):
        self.playersId.append(idPlayer)
        self.propertiesPlayers[idPlayer] = 0
        if (len(self.playersId)) > self.MaxPlayers:  # Añadir un +1 cuando terminen los tests
            if debug:
                return
            await channel.send(
                "{0.display_name}´s game is full already".format(client.fetch_user(idPlayer)))
        else:
            if len(self.playersId) == self.MaxPlayers:
                # await message.channel.send("{0.author}´s game is full and starting".format(
                # message, str(self.MaxPlayers-self.CurrentPlayers)))
                # Crear canal y asignar permisos para verlo/interactuar con el
                print("{0}'s game has started".format(self.owner))
                _VarForChannel = await guild.create_text_channel(idGame)
                for k in self.playersId:
                    _VarForMember = await guild.fetch_member(k)
                    await _VarForChannel.set_permissions(_VarForMember, read_messages=True, send_messages=True, view_channel=True)
            else:
                if debug:
                    return
                await channel.send("<@{0}> just joined! {1} to go!".format(
                    idPlayer, str(self.MaxPlayers-self.CurrentPlayers)))
                self.CurrentPlayers = len(self.playersId)
