import os
import discord
from dotenv import load_dotenv
from functions import create_image

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_member_join(member):
    user = member.name
    user_id = member.guild.id
    avatar = client.get_user(user_id)
    channel = client.get_channel(849295547210137630)
    text = f"BIENVENIDO {user}"

    create_image(avatar, text, "out.gif")

    await channel.send(f"Bienvenido {user} no olvides mirar las #reglas")
    await channel.send(file="out.gif")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))
