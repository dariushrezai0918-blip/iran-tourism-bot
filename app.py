import time
import schedule

from world_places import WORLD_PLACES
from wikipedia_source import get_summary
from formatter import format_post


def publish_post():

    place = WORLD_PLACES[0]

    data = get_summary(place["title"])

    if data:

        post = format_post(
            data["title"],
            place["country"],
            data["description"]
        )

        print("=" * 40)
        print(post)

        if data["image"]:
            print("\n📷 تصویر:")
            print(data["image"])

        print("=" * 40)

    else:
        print("دریافت اطلاعات ناموفق بود.")


# اجرای آزمایشی هنگام شروع
publish_post()

# زمان‌بندی (فعلاً هر 1 دقیقه برای تست)
schedule.every(1).minutes.do(publish_post)

print("🤖 ربات آماده است...")

while True:
    schedule.run_pending()
    time.sleep(1)
