import os
import asyncio
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")

async def send_message(text):
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(
        chat_id=CHANNEL_USERNAME,
        text=text
    )

def publish(post):
    asyncio.run(send_message(post))
