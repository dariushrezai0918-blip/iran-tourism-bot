import requests
import json
import time

URL = "https://www.wikidata.org/w/api.php"

PLACES = []

seen = set()

offset = 0

while len(PLACES) < 10000:

    params = {
        "action": "wbsearchentities",
        "search": "tourist attraction",
        "language": "en",
        "format": "json",
        "limit": 50,
        "continue": offset
    }

    r = requests.get(URL, params=params, timeout=20)

    if r.status_code != 200:
        break

    data = r.json()

    if "search" not in data:
        break

    if len(data["search"]) == 0:
        break

    for item in data["search"]:

        title = item.get("label", "").strip()

        if not title:
            continue

        if title in seen:
            continue

        seen.add(title)

        PLACES.append({
            "title": title
        })

        print(len(PLACES), title)

        if len(PLACES) >= 10000:
            break

    offset += 50

    time.sleep(1)

with open("places.py", "w", encoding="utf-8") as f:

    f.write("PLACES = ")

    f.write(json.dumps(PLACES, ensure_ascii=False, indent=4))

print("DONE :", len(PLACES))
