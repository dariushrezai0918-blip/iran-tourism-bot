import random

from places import PLACES
from history import exists, add_place
from wikipedia_source import get_summary
from formatter import format_post


def generate_post():

    random.shuffle(PLACES)

    for title in PLACES:

        if exists(title):
            continue

        place = get_summary(title)

        if place:

            add_place(title)

            return format_post(place)

    return None
