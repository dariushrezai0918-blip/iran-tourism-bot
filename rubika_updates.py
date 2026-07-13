import requests
import os

token = os.getenv("RUBIKA_TOKEN")

url = f"https://botapi.rubika.ir/v3/{token}/getUpdates"

response = requests.post(
    url,
    json={"limit": 10}
)

print(response.text)
