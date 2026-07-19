import requests


def get_summary(title):

    url = f"https://fa.wikipedia.org/api/rest_v1/page/summary/{title}"

    try:

        r = requests.get(
            url,
            headers={
                "User-Agent": "WorldTourismBot/1.0"
            },
            timeout=15
        )

        if r.status_code != 200:
            print("❌ پیدا نشد:", title)
            return None

        data = r.json()

        image = ""

        if "thumbnail" in data:
            image = data["thumbnail"].get("source", "")

        wiki = ""

        if "content_urls" in data:
            wiki = (
                data["content_urls"]
                .get("desktop", {})
                .get("page", "")
            )

        return {

            "title": data.get("title", title),

            "description": data.get("extract", ""),

            "image": image,

            "wiki": wiki

        }

    except Exception as e:

        print("Wikipedia Error:", e)

        return None
