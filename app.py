from flask import Flask
from threading import Thread
from generator import generate_post
from publisher import publish
import schedule
import time
import os
from datetime import datetime


app = Flask(__name__)


@app.route("/")
def home():
    return "Tourism Bot is running!"


def job():
    print("⏰ اجرا:", datetime.now())

    try:
        post = generate_post()

        if post:
            publish(post)
            print("✅ ارسال موفق")
        else:
            print("❌ پست ساخته نشد")

    except Exception as e:
        print("🔥 خطا:", e)



def scheduler():

    print("🚀 Scheduler شروع شد")

    # اجرای اول
    job()

    # هر ۶ ساعت
    schedule.every(6).hours.do(job)


    while True:
        schedule.run_pending()
        time.sleep(30)



Thread(target=scheduler, daemon=True).start()


if __name__ == "__main__":
    port = int(os.environ.get("PORT",10000))
    app.run(
        host="0.0.0.0",
        port=port
        )
