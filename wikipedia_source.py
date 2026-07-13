import requests


def get_random_place():

    url = "https://fa.wikipedia.org/api/rest_v1/page/random/summary"

    try:
        print("🎲 دریافت صفحه تصادفی ویکی‌پدیا")

        response = requests.get(
            url,
            headers={
                "User-Agent": "TourismBot/1.0"
            },
            timeout=10
        )

        print("📡 وضعیت ویکی‌پدیا:", response.status_code)

        if response.status_code != 200:
            print("❌ خطا در دریافت اطلاعات")
            return None

        data = response.json()

        title = data.get("title", "")
        description = data.get("extract", "")

        if not title or not description:
            print("❌ اطلاعات ناقص")
            return None

        print("✅ انتخاب شد:", title)

        return {
            "title": title,
            "description": description,
            "image": data.get("thumbnail", {}).get("source", ""),
            "wiki": data.get("content_urls", {})
                         .get("desktop", {})
                         .get("page", "")
        }

    except Exception as e:
        print("❌ خطای ویکی‌پدیا:", e)
        return None
