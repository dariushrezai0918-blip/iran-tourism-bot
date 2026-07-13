import random
from world_places import WORLD_PLACES
from formatter import format_post

def generate_post():
    place = get_random_place()

    info = {
        "title": place["title"],
        "country": place["country"],
        "description": place["description"],
        "image": place["image"],
        "wiki": place["wiki"]
    }

    post = format_post(info)

    return post
