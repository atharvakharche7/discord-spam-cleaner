import discord
import re
import asyncio

TOKEN = "ENTER_YOUR_BOT_TOKEN_HERE"  # Replace with your bot token that you've copied earlier 
SPAMMER_ID = 123456789012345678  # Replace with the spammer's Discord user ID (you can find it using Developer mode in discord)

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = discord.Client(intents=intents)

link_regex = re.compile(r'https?://\S+')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    
    for guild in bot.guilds:
        print(f'Scanning messages in {guild.name}')
        for channel in guild.text_channels:
            try:
                async for message in channel.history(limit=None):
                    if message.author.id == SPAMMER_ID and link_regex.search(message.content):
                        await message.delete()
                        print(f'Deleted message in #{channel.name}')
            except Exception as e:
                print(f'Could not access {channel.name}: {e}')

    print("Finished scanning.")
    await bot.close()

bot.run(TOKEN)