import requests
import json
import time

URL = "https://www.wikidata.org/w/api.php"

places = []

for offset in range(0, 5000, 50):

    params = {
        "action": "query",
        "list": "search",
        "srsearch": "haswbstatement:P31=Q839954",
        "format": "json",
        "srlimit": 50,
        "sroffset": offset
    }

    try:

        r = requests.get(URL, params=params, timeout=20)

        data = r.json()

        if "query" not in data:
            continue

        for item in data["query"]["search"]:

            places.append({
                "title": item["title"]
            })

        print(len(places))

        time.sleep(1)

    except Exception as e:
        print(e)

with open("places.json", "w", encoding="utf8") as f:
    json.dump(places, f, ensure_ascii=False, indent=2)

print("Done")
