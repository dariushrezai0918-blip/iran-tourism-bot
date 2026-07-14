import requests
import random


KEYWORDS = [
    "جاذبه گردشگری",
    "میراث جهانی یونسکو",
    "بنای تاریخی",
    "مکان دیدنی جهان"
]


def get_random_place():

    keyword=random.choice(KEYWORDS)

    url="https://fa.wikipedia.org/w/api.php"


    params={
        "action":"query",
        "list":"search",
        "srsearch":keyword,
        "format":"json",
        "srlimit":10
    }


    try:

        response=requests.get(
            url,
            params=params,
            headers={
                "User-Agent":"TourismBot"
            },
            timeout=10
        )


        data=response.json()

        results=data["query"]["search"]

        title=random.choice(results)["title"]


        return get_summary(title)


    except Exception as e:
        print("Wiki error:",e)
        return None




def get_summary(title):

    url=f"https://fa.wikipedia.org/api/rest_v1/page/summary/{title}"


    try:

        r=requests.get(
            url,
            headers={
                "User-Agent":"TourismBot"
            },
            timeout=10
        )


        data=r.json()


        return {

            "title":data.get("title"),

            "description":
            data.get("extract",""),

            "image":
            data.get("thumbnail",{}).get("source",""),

            "wiki":
            data.get("content_urls",{})
            .get("desktop",{})
            .get("page","")

        }


    except Exception as e:
        print(e)
        return None
