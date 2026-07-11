import requests
from urllib.parse import quote

def get_summary(title):
    """
    دریافت خلاصه مقاله از ویکی‌پدیای فارسی
    """

    url = f"https://fa.wikipedia.org/api/rest_v1/page/summary/{title}"

    try:
        response = requests.get(url, timeout=15)

        if response.status_code != 200:
            return None

        data = response.json()

        return {
            "title": data.get("title", ""),
            "description": data.get("extract", ""),
            "image": data.get("thumbnail", {}).get("source", "")
        }

    except Exception as e:
        print(e)
        return None
