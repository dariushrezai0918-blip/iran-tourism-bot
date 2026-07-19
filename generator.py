import random

from places import PLACES
from wikipedia_source import get_summary
from formatter import format_post


def generate_post():

    title = random.choice(PLACES)

    print("📍 مکان انتخاب شده:", title)

    place = get_summary(title)

    if place is None:
        print("❌ اطلاعات این مکان پیدا نشد")
        return None

    info = {
        "title": place["title"],
        "description": place["description"],
        "image": place["image"],
        "wiki": place["wiki"]
    }

    post = format_post(info)

    return post
