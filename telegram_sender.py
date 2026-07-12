import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")

def publish(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHANNEL_USERNAME,
        "text": text
    }

    response = requests.post(url, data=data)

    print("Telegram:", response.status_code)
    print(response.text)
