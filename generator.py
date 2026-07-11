import random

from world_places import WORLD_PLACES
from wikipedia_source import get_summary
from formatter import format_post


def generate_post():
    place = random.choice(WORLD_PLACES)

    data = get_summary(place["title"])

    if not data:
        return None

    info = {
        "title": place["title"],
        "country": place["country"],
        "description": data["description"],
        "image": data["image"],
        "wiki": place["wiki"]
    }

    post = format_post(info)

    return post
