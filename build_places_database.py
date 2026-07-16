import requests
import json
import time

places = []

URL = "https://fa.wikipedia.org/w/api.php"

KEYWORDS = [
    "میراث جهانی یونسکو",
    "جاذبه گردشگری",
    "بنای تاریخی",
    "پارک ملی",
    "کاخ",
    "قلعه",
    "موزه",
    "آبشار",
    "جزیره",
    "غار",
    "کوه",
    "دریاچه"
]

for keyword in KEYWORDS:

    print("جستجو:", keyword)

    offset = 0

    while offset <= 500:

        params = {
            "action": "query",
            "list": "search",
            "srsearch": keyword,
            "format": "json",
            "srlimit": 50,
            "sroffset": offset
        }

        r = requests.get(URL, params=params)

        data = r.json()

        if "query" not in data:
            break

        results = data["query"]["search"]

        if len(results) == 0:
            break

        for item in results:

            places.append({
                "title": item["title"]
            })

        offset += 50

        time.sleep(1)

print("تعداد کل:", len(places))

with open("places.json", "w", encoding="utf8") as f:

    json.dump(places, f, ensure_ascii=False, indent=2)

print("ذخیره شد.")
