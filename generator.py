from wikipedia_source import get_random_place
from formatter import format_post


def generate_post():

    print("🔎 شروع دریافت از ویکی‌پدیا")

    place = get_random_place()

    print("📌 نتیجه ویکی‌پدیا:", place)

    if not place:
        print("❌ اطلاعات دریافت نشد")
        return None

    info = {
        "title": place.get("title", ""),
        "description": place.get("description", ""),
        "image": place.get("image", ""),
        "wiki": place.get("wiki", "")
    }

    post = format_post(info)

    print("✅ پست ساخته شد")

    return post
