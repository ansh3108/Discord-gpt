


import discord
import os

token = os.getenv("YOUR_TOKEN")

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        channel = message.channel
        await channel.send("hello world!")
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run("YOUR_TOKEN")


