import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'hey! welcome to shross')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='shross'))
    print('Ready') 


@client.event
async def on_message(message):
    if message.content == '!shross':
        await client.send_message(message.channel,'hey shross!')
    if message.content == '':
        em = discord.Embed(description='#shross the master')
        em.set_image(url='https://cdn.discordapp.com/attachments/543920568110546948/544117286756155392/IMG_20180916_210906_670.jpg')
        await client.send_message(message.channel, embed=em)
    if ('sex') in message.content:
       await client.delete_message(message)
    if message.content.startswith('shross tm'):
        randomlist = ["hey","goodlife",]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('wsf'):
        await client.send_message(message.channel,'hello, <@%s>'  %(message.author.id))
    if message.content == 'fuck':
        await client.send_message(message.channel,'talk nice! דבר יפה!')
    if message.content == 'bitch':
        await client.send_message(message.channel,'talk nice! דבר יפה!')
    if message.content == 'זין':
        await client.send_message(message.channel,'talk nice! דבר יפה!')
    if message.content == 'תזדיין':
        await client.send_message(message.channel,'talk nice! דבר יפה!')
    if message.content == 'כוסעמק':
        await client.send_message(message.channel,'talk nice! דבר יפה!')
    if message.content == 'זונה':
        await client.send_message(message.channel,'talk nice! דבר יפה!')
    if message.content == 'שיט':
        await client.send_message(message.channel,'talk nice! דבר יפה!')
    if message.content == 'shit':
        await client.send_message(message.channel,'talk nice! דבר יפה!')
    if message.content == 'מנייאק':
        await client.send_message(message.channel,'talk nice! דבר יפה!')
    if message.content == 'join':
        await client.send_message(message.channel,'hey! welcome to shross')
client.run('NTQ0MDk0NDEzMTA2NzA4NDgx.D0GyYg.dw_2hZD6frunsPW1hTi4GRb3rG0')
