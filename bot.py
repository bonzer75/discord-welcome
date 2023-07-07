import os
import discord
import time
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
    user_id = 942544136098160700#member.guild.id
    avatar = client.get_user(user_id).avatar
    channel = client.get_channel(849295547210137630)
    text = f"BIENVENIDO {user}"

    create_image(str(member.avatar), text, "resources/out.gif")

    await channel.send(f"Bienvenido {user} no olvides mirar las #reglas")
    time.sleep(3)
    await channel.send(file=discord.File("resources/out.gif"))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('TOKEN'))
