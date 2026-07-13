import requests
import random


KEYWORDS = [
    "جاذبه گردشگری",
    "میراث جهانی یونسکو",
    "بنای تاریخی",
    "مکان دیدنی",
    "پارک ملی",
    "موزه"
]


def get_summary(title):
    url = f"https://fa.wikipedia.org/api/rest_v1/page/summary/{title}"

    try:
        response = requests.get(url, timeout=15)

        if response.status_code != 200:
            print("Wikipedia Error:", response.status_code)
            return None

        data = response.json()

        return {
            "title": data.get("title", ""),
            "description": data.get("extract", ""),
            "image": data.get("thumbnail", {}).get("source", ""),
            "wiki": data.get("content_urls", {}).get("desktop", {}).get("page", "")
        }

    except Exception as e:
        print("Wikipedia Exception:", e)
        return None



def get_random_place():

    keyword = random.choice(KEYWORDS)

    url = "https://fa.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "list": "search",
        "srsearch": keyword,
        "format": "json",
        "srlimit": 20
    }

    try:
        response = requests.get(url, params=params, timeout=15)
        data = response.json()

        results = data["query"]["search"]

        title = random.choice(results)["title"]

        return get_summary(title)

    except Exception as e:
        print("Random place error:", e)
        return None
