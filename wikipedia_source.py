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
        print("📖 دریافت اطلاعات:", title)

        response = requests.get(url, timeout=10)

        print("Status:", response.status_code)

        if response.status_code != 200:
            return None

        data = response.json()

        return {
            "title": data.get("title", ""),
            "description": data.get("extract", ""),
            "image": data.get("thumbnail", {}).get("source", ""),
            "wiki": data.get("content_urls", {}).get("desktop", {}).get("page", "")
        }

    except Exception as e:
        print("Summary Error:", e)
        return None



def get_random_place():

    keyword = random.choice(KEYWORDS)

    print("🔍 جستجو:", keyword)

    url = "https://fa.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "list": "search",
        "srsearch": keyword,
        "format": "json",
        "srlimit": 10
    }

    try:
    response = requests.get(
        url,
        params=params,
        headers={
            "User-Agent": "TourismBot/1.0"
        },
        timeout=10
    )

    print("📡 پاسخ ویکی‌پدیا دریافت شد")

    data = response.json()

        print("Search status:", response.status_code)

        data = response.json()

        results = data.get("query", {}).get("search", [])

        if not results:
            print("❌ نتیجه‌ای پیدا نشد")
            return None

        title = random.choice(results)["title"]

        print("✅ انتخاب شد:", title)

        return get_summary(title)

    except Exception as e:
        print("Random place Error:", e)
        return None
