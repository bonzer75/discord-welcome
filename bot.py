import discord
from discord import File
from easy_pil import Editor, load_image_async, Font

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')


@client.event
async def on_member_join(member):
  channel = client.get_channel(849295547210137630)

  bg = Editor("nyan-cat.gif")
  profile = await load_image_async(f'{member.avatar.url}')
  pfp = Editor(profile).resize((150, 150)).circle_image()
  h1 = Font.poppins(size=50, variant="bold")

  bg.paste(pfp, (325, 90))
  #bg.eclipse((325, 90), 150, 150, outline="white", stroke_width=5)
  bg.text((400, 260), f"BIENVENIDO {member.name}", color="white", font=h1, align="center")

  await channel.send(f"Bienvenido {member.name} no olvides mirar las #reglas")
  await channel.send(file=File(fp=bg.image_bytes, filename="wecolme1.jpg"))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')


client.run('OTQ5MzIzNzQ2NDA4Mjc2MDI4.GJx_z_.Kmvf5gEf9jjbpwXD3EcNJi6uqz0wMxMMC7vEDM')