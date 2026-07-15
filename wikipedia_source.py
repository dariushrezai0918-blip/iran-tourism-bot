import requests
import random

KEYWORDS = [
    "جاذبه گردشگری",
    "میراث جهانی یونسکو",
    "قلعه",
    "کاخ",
    "موزه",
    "پارک ملی",
    "آبشار",
    "دریاچه",
    "کوه",
    "جزیره",
    "معبد",
    "مسجد تاریخی",
    "کلیسا",
    "شهر تاریخی"
]

# کلماتی که اگر داخل عنوان باشند رد می‌شوند
BLACKLIST = [
    "فیلم",
    "مجموعه",
    "سریال",
    "بازیگر",
    "شخص",
    "تمدن",
    "جنگ",
    "دانشگاه",
    "شرکت",
    "باشگاه",
    "انتخابات",
    "کتاب",
    "آلبوم",
    "ترانه",
    "فوتبال",
    "روستا",
    "استان",
    "شهرستان"
]


def get_random_place():

    print("🔎 شروع دریافت از ویکی‌پدیا")

    for _ in range(15):

        keyword = random.choice(KEYWORDS)

        print("🔍 جستجو:", keyword)

        url = "https://fa.wikipedia.org/w/api.php"

        params = {
            "action": "query",
            "list": "search",
            "srsearch": keyword,
            "format": "json",
            "srlimit": 20
        }

        try:

            response = requests.get(
                url,
                params=params,
                headers={"User-Agent": "TourismBot"},
                timeout=10
            )

            data = response.json()

            results = data["query"]["search"]

            random.shuffle(results)

            for item in results:

                title = item["title"]

                if any(word in title for word in BLACKLIST):
                    continue

                place = get_summary(title)

                if not place:
                    continue

                text = (
                    place["title"] +
                    place["description"]
                ).lower()

                if any(word in text for word in BLACKLIST):
                    continue

                if len(place["description"]) < 250:
                    continue

                print("✅ انتخاب شد:", place["title"])

                return place

        except Exception as e:
            print(e)

    return None


def get_summary(title):

    url = f"https://fa.wikipedia.org/api/rest_v1/page/summary/{title}"

    try:

        r = requests.get(
            url,
            headers={"User-Agent": "TourismBot"},
            timeout=10
        )

        data = r.json()

        return {
            "title": data.get("title", ""),
            "description": data.get("extract", ""),
            "image": data.get("thumbnail", {}).get("source", ""),
            "wiki": data.get("content_urls", {}).get("desktop", {}).get("page", "")
        }

    except Exception as e:
        print(e)
        return None
