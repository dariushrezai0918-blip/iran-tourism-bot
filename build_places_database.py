from wikidata_source import get_location
from place_filter import is_place
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
            "image": data.get("thumbnail", {}).get("source", ""),
            "wiki": data.get("content_urls", {})
                        .get("desktop", {})
                        .get("page", "")

        }

    except Exception as e:

        print(e)
        return None


places = []

URL = "https://fa.wikipedia.org/w/api.php"

KEYWORDS = [

    "میراث جهانی یونسکو",
    "جاذبه گردشگری",
    "بنای تاریخی",
    "کاخ",
    "قلعه",
    "آرامگاه",
    "مسجد تاریخی",
    "کلیسا",
    "معبد",
    "موزه",
    "برج",
    "پل تاریخی",
    "باغ تاریخی",
    "کاروانسرا",
    "شهر تاریخی",
    "محوطه باستانی",

    "پارک ملی",
    "پارک طبیعی",
    "جنگل",
    "دریاچه",
    "رودخانه",
    "آبشار",
    "غار",
    "جزیره",
    "کوه",
    "دره",
    "بیابان",
    "ساحل",

    "گردشگری ایران",
    "گردشگری جهان",
    "جاذبه طبیعی",
    "جاذبه فرهنگی",
    "اثر باستانی",
    "اثر تاریخی",
    "میراث فرهنگی"

]

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

        r = requests.get(URL, params=params)

        data = r.json()

        if "query" not in data:
            break

        results = data["query"]["search"]

        if len(results) == 0:
            break

        for item in results:

            title = item["title"]

            if is_place(title):

                info = get_summary(title)
                if info:

    if len(info["description"]) < 250:
        continue

    places.append(info)

    print(info["title"])
if info:

    location = get_location(title)

    if location:

        info.update(location)

    places.append(info)

    print(info["title"])

        offset += 50

        time.sleep(1)

print("تعداد کل:", len(places))

with open("places.json", "w", encoding="utf8") as f:

    json.dump(places, f, ensure_ascii=False, indent=2)

print("ذخیره شد.")
unique_places = []

seen = set()

for place in places:

    if place["title"] not in seen:

        seen.add(place["title"])

        unique_places.append(place)

places = unique_places

print("بعد از حذف موارد تکراری:", len(places))
