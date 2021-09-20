import discord
from dotenv import load_dotenv
import os

# Credentials
load_dotenv('.env')

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$feedstan'):
        await message.channel.send('{0.user} is feeding <@!321526735579381762>!')
        await message.channel.send('<@!321526735579381762>')
        await message.channel.send('https://shadow.s-ul.eu/jkrnJnLt')
        await message.channel.send("Don't forget to look up <@!321526735579381762>!")
        await message.channel.send("Dinner time for <@!321526735579381762> has been completed. Please rate <@!321526735579381762>'s dinner time in the chat below by sending '$1', '$2', '$3', '$4' or '$5'")

    if message.content.startswith('$1'):
        await message.channel.send("Thank you for voting on the bot that feeds <@!321526735579381762>.")
    if message.content.startswith('$2'):
        await message.channel.send("Thank you for voting on the bot that feeds <@!321526735579381762>.")
    if message.content.startswith('$3'):
        await message.channel.send("Thank you for voting on the bot that feeds <@!321526735579381762>.")
    if message.content.startswith('$4'):
        await message.channel.send("Thank you for voting on the bot that feeds <@!321526735579381762>.")
    if message.content.startswith('$5'):
        await message.channel.send("Thank you for voting on the bot that feeds <@!321526735579381762>.")


    if message.content.startswith('$fuckyou'):
        await message.channel.send("https://cdn.discordapp.com/attachments/756894822643793944/889609333380382780/video0_73.mp4")

client.run(os.getenv('TOKEN'))