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
    print("در حال تولید پست جدید...")

    post = generate_post()

    if post:
        publish(post)
    else:
        print("خطا در تولید محتوا")

def scheduler():
    job()
   schedule.every(1).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(30)

Thread(target=scheduler, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
