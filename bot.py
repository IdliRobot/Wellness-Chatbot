#bot.py

import discord
from os import environ
from dotenv import load_dotenv
from discord.ext import commands
from ai import Chat, welcome



channel_id: int = int(environ.get("CHANNEL_ID"))

bot: commands.Bot = commands.Bot(command_prefix = None, intents = discord.Intents.all())

wellness: Chat = Chat()

@bot.event
async def on_ready() -> None:
    print(f"Logged in as: {bot.user.name}")
    channel: discord.TextChannel = bot.get_channel(channel_id)
    await channel.send(welcome)

@bot.event
async def on_message(message: discord.Message) -> None:
    if message.author.bot or message.channel.id != channel_id:
        return

    async with message.channel.typing():
        response: str = wellness.message(message.content)
        await string_messages(message, response)

async def string_messages(prompt: discord.Message, response: str) -> None:
    while (response != ""):
        try:
            prompt = await prompt.reply(response[0 : 2000], mention_author = True)
            response = response[2000 :]
        except:
            await prompt.reply(response, mention_author = True)

load_dotenv()
token: str = environ.get("DISCORD_TOKEN")
bot.run(token = token)
