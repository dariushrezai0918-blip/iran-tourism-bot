import requests


def get_location(title):

    url = "https://www.wikidata.org/w/api.php"

    params = {

        "action": "wbsearchentities",
        "search": title,
        "language": "fa",
        "format": "json",
        "limit": 1

    }

    try:

        r = requests.get(
            url,
            params=params,
            headers={
                "User-Agent": "TourismBot"
            },
            timeout=15
        )

        data = r.json()

        results = data.get("search", [])

        if not results:
            return None


        entity_id = results[0]["id"]


        # دریافت اطلاعات موجودیت

        url2 = "https://www.wikidata.org/w/api.php"

        params2 = {

            "action": "wbgetentities",
            "ids": entity_id,
            "languages": "fa",
            "format": "json"

        }


        r2 = requests.get(
            url2,
            params=params2,
            headers={
                "User-Agent": "TourismBot"
            },
            timeout=15
        )


        entity = r2.json()["entities"][entity_id]


        result = {}


        claims = entity.get("claims", {})


        # کشور (P17)

        if "P17" in claims:

            country_id = claims["P17"][0]["mainsnak"] \
                ["datavalue"]["value"]["id"]

            result["country"] = get_label(country_id)


        # شهر یا مکان قرارگیری (P131)

        if "P131" in claims:

            city_id = claims["P131"][0]["mainsnak"] \
                ["datavalue"]["value"]["id"]

            result["city"] = get_label(city_id)


        return result


    except Exception as e:

        print("Wikidata error:", e)

        return None



def get_label(entity_id):

    url = "https://www.wikidata.org/w/api.php"


    params = {

        "action": "wbgetentities",
        "ids": entity_id,
        "languages": "fa|en",
        "format": "json"

    }


    try:

        r = requests.get(
            url,
            params=params,
            headers={
                "User-Agent": "TourismBot"
            },
            timeout=10
        )


        data = r.json()

        entity = data["entities"][entity_id]


        labels = entity.get("labels", {})


        if "fa" in labels:
            return labels["fa"]["value"]

        if "en" in labels:
            return labels["en"]["value"]


    except:

        pass


    return ""
