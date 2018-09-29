import discord
import requests
from discord.ext import commands

import aiohttp
import asyncio

BOT_PREFIX = ("?", "!")
#TOKEN = "NDU0NTA4MTUyMjYwNjU3MTUy.Df0JXw.bZbcfhQ4d9Oeb6X6uwrvi7MSiZk"
TOKEN = "NDU0NTA4MTUyMjYwNjU3MTUy.Dg90oQ.03JCJQWIjLa_98t33Y80FgluuGc"

client = commands.Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    #await client.change_presence(game=Game(name="with humans"))
    #await client.say(client.user.name)
    print("Ready")

# @client.command()
# async def bitcoin():
#     url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
#     response = requests.get(url)
#     value = response.json()['bpi']['USD']['rate']
#     print("Getting BTC price")
#     await client.say("Bitcoin (BTC) : $" + value)

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await client.send_message(channel, content)

@client.event
async def on_message(message):
    if message.content.upper().startswith('!UPVOTE'):

        auth = message.author
        content = message.content
        #print(content)

        # Parse memo
        memo = content.split("://")
        print("Memo: " + memo[1])

        # send message to steemybot
        await httpSend(memo[1])
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Your post has been upvoted " % (userID))

    elif message.content.upper().startswith('!DOWNVOTE'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Your post has been down voted, sorry " % (userID))

async def httpSend(message):
    requests.get('http://142.93.203.25:5000/freevote/' + message, auth=('user', 'pass'))
    return True

async def list_servers():
    await client.wait_until_ready() # no actions performed until connections are established
    while not client.is_closed:
        print("Current Services:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)

client.loop.create_task(list_servers())
client.run(TOKEN)