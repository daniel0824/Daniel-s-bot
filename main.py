import os
import discord

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#client = discord.Client()
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

# !!!!!`
# you have to change 'MESSAGE CONNTEN INTENT" to True
# @ dicord deceloper page
# !!!!!
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'hi':
        await message.channel.send('hello')
    elif message.content == 'i miss you':
        await message.channel.send("me too, I miss you too")
    elif message.content == 'give me money':
        await message.channel.send('about the deal')
    elif message.content == 'how are you':
        await message.channel.send('good thank you')
    elif message.content == 'anything new':
        await message.channel.send('buy my game')
    elif message.content == 'put ur hands up':
        await message.channel.send('yo man chiil out')
    elif message.content == 'whats ur super power':
        await message.channel.send('i can fly')
    elif message.content == 'whats your favorite game':
        await message.channel.send('Ghost Recon wildlands')
    elif message.content == 'whats the season':
        await message.channel.send('autumn')
    elif message.content == 'what game do you hate':
        await message.channel.send('Valorant!!!!!')
    elif message.content == 'whats your favorite show':
        await message.channel.send('I dont have one')
    




client.run(TOKEN)
