
import requests

token = "توکن_روبیکا"

url = f"https://botapi.rubika.ir/v3/{token}/getUpdates"

data = {
    "limit": 10
}

response = requests.post(url, json=data)

print(response.text)
