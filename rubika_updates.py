import os
import requests

token = os.getenv("RUBIKA_TOKEN")

url = f"https://botapi.rubika.ir/v3/{token}/getUpdates"

response = requests.post(
    url,
    json={}
)

print(response.text)
