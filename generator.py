from wikipedia_source import get_random_place
from formatter import format_post


def generate_post():

    import random
from places import PLACES
from wikipedia_source import get_summary

title = random.choice(PLACES)

place = get_summary(title)

    if place is None:
        print("❌ هیچ مکانی پیدا نشد")
        return None

    info = {
        "title": place["title"],
        "description": place["description"],
        "image": place["image"],
        "wiki": place["wiki"]
    }

    post = format_post(info)

    return post
