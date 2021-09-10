import discord
import os


client = discord.Client()
import CreateGame as CG


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith("!Create"):
        await CG.Create(message.author.id, message.content.split()[1], message)
        ###ToDo
        ###Arreglar create null
        ###Arreglar confirmar int
    if message.content.startswith("!Join"):
        await CG.Join(message, message.author.id)
    if message.content.startswith("!Interactuate"):
        await CG.Interactuate(message, message.author.id)
route = os.getcwdb()
token = open(route+b"/Monopoly/token.txt", "r")
client.run(token.read())
