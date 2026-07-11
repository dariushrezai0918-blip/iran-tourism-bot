import random
from world_places import WORLD_PLACES
from wiki import get_summary

def generate_post():
    place = random.choice(WORLD_PLACES)

    data = get_summary(place["title"])

    if data:
        text = data["description"][:700]
        image = data["image"]
    else:
        text = f"{place['title']} یکی از مشهورترین جاذبه‌های گردشگری {place['country']} است."
        image = None

    hashtags = [
        f"#{place['title'].replace(' ', '_')}",
        f"#{place['country'].replace(' ', '_')}",
        "#گردشگری",
        "#سفر",
        "#جهانگردی",
        "#ایرانگردی",
        "#جاذبه_گردشگری",
        "#توریسم"
    ]

    post = f"""🌍 {place['title']}

{text}

📚 مطالعه بیشتر:
{place['wiki']}

{" ".join(hashtags)}
"""

    return post, image
