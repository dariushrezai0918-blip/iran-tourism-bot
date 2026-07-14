from flask import Flask
from threading import Thread
from generator import generate_post
from publisher import publish
import schedule
import time
import os

app = Flask(__name__)


@app.route("/")
def home():
    return "Bot is running!"


def job():
    print("🚀 شروع تولید پست...")

    try:
        post = generate_post()

        print("📄 نتیجه generate_post:", post)

        if post:
            publish(post)
            print("✅ پست با موفقیت ارسال شد")
        else:
            print("❌ پست تولید نشد")

    except Exception as e:
        print("🔥 خطا در job:", e)


def scheduler():
    print("⏰ Scheduler Started")

    # اجرای اولیه
    job()

    # برای تست هر یک دقیقه
    schedule.every(1).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(5)


Thread(target=scheduler, daemon=True).start()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
