from DiscordMiddleMan import client


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