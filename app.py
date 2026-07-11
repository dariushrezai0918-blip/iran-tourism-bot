from world_places import WORLD_PLACES
from wikipedia_source import get_summary
from formatter import format_post

place = WORLD_PLACES[0]

data = get_summary(place["title"])

if data:

    post = format_post(
        data["title"],
        place["country"],
        data["description"]
    )

    print(post)

    print("\nتصویر:\n")
    print(data["image"])

else:
    print("اطلاعات دریافت نشد.")
