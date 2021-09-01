#Бот для просмотра курса криптовалют
import discord, requests
from discord.ext import commands
btc =requests.get('https://min-api.cryptocompare.com/data/price?fsym=btc&tsyms=USD').json()['USD']
eth =requests.get('https://api.coincap.io/v2/assets/ethereum').json()['data']['priceUsd']
xmr =requests.get('https://min-api.cryptocompare.com/data/price?fsym=xmr&tsyms=USD').json()['USD']
rvn =requests.get('https://min-api.cryptocompare.com/data/price?fsym=rvn&tsyms=USD').json()['USD']
bch=requests.get('https://min-api.cryptocompare.com/data/price?fsym=bch&tsyms=USD').json()['USD']
ltc =requests.get('https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD').json()['USD']
doge =requests.get('https://min-api.cryptocompare.com/data/price?fsym=doge&tsyms=USD').json()['USD']
client = commands.Bot(command_prefix = 'Ваш префикс')
@client.event
async def on_message(message):
    if message.content.lower() == 'btc':
        emb = discord.Embed(title='ЦЕНА BITCOIN',color=0xff0000)
        emb.add_field(name="Цена:",value=str(btc)+'$',inline=False)
        await message.channel.send(embed = emb)
    if message.content.lower() == 'eth':
        emb = discord.Embed(title='ЦЕНА ETHERIUM',color=0xff0000)
        emb.add_field(name="Цена:",value=str(eth[:-13])+'$',inline=False)
        await message.channel.send(embed = emb)
    if message.content.lower() == 'xmr':
        emb = discord.Embed(title='ЦЕНА MONERO',color=0xff0000)
        emb.add_field(name="Цена:",value=str(xmr)+'$',inline=False)
        await message.channel.send(embed = emb)
    if message.content.lower() == 'rvn':
        emb = discord.Embed(title='ЦЕНА RAVENCOIN',color=0xff0000)
        emb.add_field(name="Цена:",value=str(rvn)+'$',inline=False)
        await message.channel.send(embed = emb)
    if message.content.lower() == 'bch':
        emb = discord.Embed(title='ЦЕНА BINCOIN CASH',color=0xff0000)
        emb.add_field(name="Цена:",value=str(bch)+'$',inline=False)
        await message.channel.send(embed = emb)
    if message.content.lower() == 'ltc':
        emb = discord.Embed(title='ЦЕНА LITECOIN',color=0xff0000)
        emb.add_field(name="Цена:",value=str(ltc)+'$',inline=False)
        await message.channel.send(embed = emb)
    if message.content.lower() == 'doge':
        emb = discord.Embed(title='ЦЕНА DOGECOIN',color=0xff0000)
        emb.add_field(name="Цена:",value=str(doge)+'$',inline=False)
        await message.channel.send(embed = emb)
    await client.process_commands(message)
client.run('Ваш токен')
