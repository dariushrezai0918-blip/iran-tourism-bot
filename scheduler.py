import time
import schedule

from world_places import WORLD_PLACES
from wikipedia_source import get_summary

def job():
    place = WORLD_PLACES[0]   # فعلاً اولین مکان را تست می‌کنیم

    print(f"در حال دریافت اطلاعات: {place['title']}")

    data = get_summary(place["title"])

    if data:
        print("✅ اطلاعات دریافت شد")
        print(data["title"])
        print(data["description"][:200])
    else:
        print("❌ دریافت اطلاعات ناموفق بود")

schedule.every(1).minutes.do(job)

print("🤖 ربات آماده است...")

job()

while True:
    schedule.run_pending()
    time.sleep(1)
