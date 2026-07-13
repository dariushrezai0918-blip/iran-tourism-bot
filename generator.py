from wikipedia_source import get_random_place
from formatter import format_post


def generate_post():

    place = get_random_place()

    if not place:
        return None

    info = {
        "title": place["title"],
        "description": place["description"],
        "image": place["image"],
        "wiki": place["wiki"]
    }

    post = format_post(info)

    return post
