import discord 
from discord.ext import commands
import music

cogs = [music]
client = commands.Bot(command_prefix='?',intents=discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)



client.run("ODczNDI0NTkyNTQxMjE2Nzg4.YQ4OCg.Db2IiVl4gFyU48fFupO-WCO1Suo")