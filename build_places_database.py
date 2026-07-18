from category import get_category
from place_filter import is_place
from keywords import KEYWORDS
import requests
import json
import time


def get_summary(title):

    url = f"https://fa.wikipedia.org/api/rest_v1/page/summary/{title}"

    try:

        r = requests.get(
            url,
            headers={
                "User-Agent": "TourismBot"
            },
            timeout=15
        )

        if r.status_code != 200:
            return None

        data = r.json()

        return {

            "title": data.get("title", ""),

            "description": data.get("extract", ""),

            "image": data.get("thumbnail", {})
                        .get("source", ""),

            "wiki": data.get("content_urls", {})
                        .get("desktop", {})
                        .get("page", "")

        }

    except Exception as e:

        print("Wiki error:", e)

        return None



places = []

URL = "https://fa.wikipedia.org/w/api.php"

from keywords import KEYWORDS

for keyword in KEYWORDS:

    print("جستجو:", keyword)

    offset = 0


    while offset <= 5000:


        params = {

            "action": "query",
            "list": "search",
            "srsearch": keyword,
            "format": "json",
            "srlimit": 50,
            "sroffset": offset

        }


        try:

            r = requests.get(
                URL,
                params=params,
                timeout=15
            )

            data = r.json()

        except:

            break



        if "query" not in data:
            break



        results = data["query"]["search"]



        if len(results) == 0:
            break



        for item in results:


            title = item["title"]


            if not is_place(title):
                continue



            info = get_summary(title)



            if not info:
                continue



            # حذف متن های خیلی کوتاه
            if len(info["description"]) < 250:
                continue



            # اضافه کردن دسته بندی
            info["category"] = get_category(
                info["title"],
                info["description"]
            )



            places.append(info)



            print(
                info["title"],
                "=>",
                info["category"]
            )



        offset += 50


        time.sleep(1)




# حذف موارد تکراری

unique = []

seen = set()


for place in places:

    if place["title"] not in seen:

        seen.add(place["title"])

        unique.append(place)



places = unique



print("----------------")
print("تعداد کل:", len(places))
print("----------------")



with open(
    "places.json",
    "w",
    encoding="utf8"
) as f:

    json.dump(
        places,
        f,
        ensure_ascii=False,
        indent=2
    )



print("بانک مکان ها ساخته شد.")
