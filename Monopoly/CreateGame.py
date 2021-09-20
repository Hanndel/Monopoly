from discord.abc import _Overwrites
from DiscordMiddleMan import client, discord
from Game import Game, Data
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

    async def Create(idPlayer, players, channel, debug):
        if(len([x for x in games.values() if idPlayer in x.playersId]) == 0):
            games[idPlayer] = (CreateGame(players=int(
                players), owner=idPlayer, channel=channel, debug=debug))
            await games[idPlayer].Announcement(channel, debug)
        else:
            await channel.send("You are in a game already")

    async def Announcement(self, channel, debug):
        print("{0} made a game".format(self.owner))
        await channel.send(
            "Next {0} persons that type !Join <@{1}> will join the game!".format((self.MaxPlayers-1), self.owner))

    async def Join(content, idPlayer, guild, channel, debug):
        if(len([x for x in games.values() if idPlayer in x.playersId]) == 0):
            _regexForId = re.search("(<@!+[0-9])\w+", content)[0]
            idGame = int(re.search("([0-9])\w+", _regexForId)[0])
            if idGame in games:
                game = games[idGame]
                await game.Joining(idPlayer=idPlayer, guild=guild, channel=channel, idGame=idGame, debug=debug)
            else:
                await channel.send("That person is not making a game right now")
        else:
            await channel.send("{}, you are in a game already")

    async def Joining(self, idPlayer, idGame, guild, channel, debug):
        self.playersId.append(idPlayer)
        self.propertiesPlayers[idPlayer] = 0
        self._VarForPlayer = await client.fetch_user(idPlayer)
        self._VarForOwner = await client.fetch_user(idGame)
        if (len(self.playersId)) > (self.MaxPlayers+1):
            await channel.send(
                "{0.display_name}´s game is full already".format(self._VarForPlayer))
        else:
            self.CurrentPlayers = len(self.playersId)
            if len(self.playersId) == self.MaxPlayers:
                # Crear canal y asignar permisos para verlo/interactuar con el
                overwrites = {
                    guild.default_role: discord.PermissionOverwrite(read_messages=False),
                    guild.self_role: discord.PermissionOverwrite(
                        read_messages=True, send_messages=True)
                }
                _VarForChannel = await guild.create_text_channel("{0.name}'s game".format(self._VarForOwner), overwrites=overwrites)

                for k in self.playersId:
                    _VarForMember = await guild.fetch_member(k)
                    await _VarForChannel.set_permissions(_VarForMember, read_messages=True, send_messages=True, view_channel=True)

                Game(self.playersId, _VarForChannel.id)
                Data[_VarForChannel.id][371776838491701258].Roll()

                await _VarForChannel.send("<@&864644094343905291>, game is about to start")
            else:
                await channel.send("<@{0.id}> just joined! {1} to go!".format(
                    self._VarForPlayer, str(self.MaxPlayers-self.CurrentPlayers)))
    
