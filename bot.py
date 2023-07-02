import discord

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
  await channel.send(f"{member.name} has joined")


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')


client.run('')
