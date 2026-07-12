from generator import generate_post
from publisher import publish
import schedule
import time

print("🌍 ربات گردشگری جهان شروع شد...")

def job():
    print("در حال تولید پست جدید...")

    post = generate_post()

    if post:
        publish(post)
    else:
        print("❌ خطا در تولید محتوا")

# یک بار هنگام شروع اجرا شود
job()

# هر ۶ ساعت یک بار اجرا شود
schedule.every(6).hours.do(job)

# همیشه روشن بماند
while True:
    schedule.run_pending()
    time.sleep(30)
