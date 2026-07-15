from wikipedia_source import get_random_place
from formatter import format_post


def generate_post():

    print("🔎 شروع دریافت از ویکی‌پدیا")

    place = get_random_place()

if place is None:
    return None

info = {
    "title": place["title"],
    "description": place["description"],
    "image": place["image"],
    "wiki": place["wiki"]
}

    post = format_post(info)

    print("✅ پست ساخته شد")

    return post
