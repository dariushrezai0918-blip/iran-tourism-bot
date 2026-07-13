from wikipedia_source import get_random_place
from formatter import format_post


def generate_post():

    place = get_random_place()

    print("Wikipedia result:", place)

    if not place:
        print("❌ هیچ مکانی از ویکی‌پدیا دریافت نشد")
        return None

    info = {
        "title": place["title"],
        "description": place["description"],
        "image": place.get("image", ""),
        "wiki": place.get("wiki", "")
    }

    post = format_post(info)

    print("Generated post:", post)

    return post
