import requests

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
            "image": data.get("thumbnail", {}).get("source", "")
        }

    except Exception as e:
        print("Wikipedia Exception:", e)
        return None
