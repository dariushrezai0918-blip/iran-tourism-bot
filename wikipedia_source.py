import requests
import random


KEYWORDS = [
    "برج تاریخی",
    "قلعه تاریخی",
    "کاخ تاریخی",
    "معبد تاریخی",
    "آبشار معروف",
    "جزیره گردشگری",
    "پارک ملی",
    "میراث جهانی یونسکو",
    "مکان گردشگری",
    "جاذبه طبیعی",
    "مکان گردشی",
    "جاذبه های دیدنی"
    
]


BLOCK_WORDS = [
    "فهرست",
    "رده:",
    "دسته:",
    "تمدن",
    "تاریخچه",
    "انواع",
    "تعریف",
    "مقاله",
    "لیست"
]


def is_valid_place(title, description):

    text = title + " " + description

    for word in BLOCK_WORDS:
        if word in text:
            return False

    if len(description) < 150:
        return False

    return True



def get_random_place():

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
            headers={
                "User-Agent": "TourismBot"
            },
            timeout=10
        )


        data = response.json()

        results = data["query"]["search"]


        random.shuffle(results)


        for item in results:

            title = item["title"]

            place = get_summary(title)


            if place:

                if is_valid_place(
                    place["title"],
                    place["description"]
                ):
                    print("✅ انتخاب شد:", place["title"])
                    return place



        return None



    except Exception as e:

        print("Wiki error:", e)
        return None




def get_summary(title):

    url = f"https://fa.wikipedia.org/api/rest_v1/page/summary/{title}"


    try:

        r = requests.get(
            url,
            headers={
                "User-Agent": "TourismBot"
            },
            timeout=10
        )


        if r.status_code != 200:
            return None


        data = r.json()


        return {

            "title": data.get("title",""),

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

        print("Summary error:", e)

        return None
