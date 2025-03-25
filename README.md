# Discord Spam Cleaner Bot

A Python bot to delete old spam messages (even from users who have left the server). Useful for Discord moderators who need to clean up unwanted links and messages.

## Features
- Deletes old messages from a specific user (even if they left the server).
- Deletes messages older than 14 days, even bots like MEE6, Carl-bot, etc can't do that cause of discord's policies.
- Targets messages with links to remove spam effectively.
- Works across all channels in a server.
- Uses a real bot (not a self-bot) to comply with Discord's rules.

## Setup Guide

### 1. Create a Discord Bot
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click **"New Application"** -> Give it a name.
3. Navigate to **"Bot"** -> Click **"Add Bot"**.
4. Enable **"Message Content Intent"** under "Privileged Gateway Intents".
5. Copy the **Bot Token** (you'll need it later).

### 2. Invite the Bot to Your Server
1. In the **OAuth2 > URL Generator**, check the following:
   - `bot`
   - `applications.commands` (optional, for future use)
2. Under **Bot Permissions**, check:
   - `Manage Messages`
   - `Read Message History`
   - `View Channels`
3. Copy the **generated invite link** and open it in your browser.
4. Select your **server** and click **"Authorize"**.

### 3. Install Dependencies
Make sure you have Python installed, then run:
```sh
pip install discord.py
```

### 4. Run the Script
Create a file `delete_spam.py` and paste the following code:

```python
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
```

### 5. Run the Script
```sh
python delete_spam.py
```

This will:
- Scan all channels.
- Delete messages with links from the specific user.

## Notes
- This bot **must have "Manage Messages" permission**.
- Make sure to **replace `SPAMMER_ID`** with the actual Discord ID of the spammer.
- This script **deletes only messages from the target user**, not everyone.

**Happy moderating!**
