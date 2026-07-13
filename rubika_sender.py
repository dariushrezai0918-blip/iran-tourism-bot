import os
import requests

TOKEN = os.getenv("RUBIKA_TOKEN")
CHAT_ID = os.getenv("RUBIKA_CHAT_ID")


def publish(post):

    url = f"https://botapi.rubika.ir/v3/{TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": post
    }

    response = requests.post(url, json=data)

    print("Rubika response:")
    print(response.text)
