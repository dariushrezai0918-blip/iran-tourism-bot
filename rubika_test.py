from rubika_bot_api.api import Robot

TOKEN = "توکن_جدید_ربات"

bot = Robot(token=TOKEN)

@bot.on_message()
def get_id(bot, message):
    print("CHAT ID:", message.chat_id)
    print("TEXT:", message.text)

bot.run()
