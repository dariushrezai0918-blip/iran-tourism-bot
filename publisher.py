from telegram_sender import publish as telegram_publish
from rubika_sender import publish as rubika_publish


def publish(post):
    # ارسال به تلگرام
    try:
        telegram_publish(post)
        print("✅ ارسال تلگرام موفق بود")
    except Exception as e:
        print("❌ خطای تلگرام:", e)

    # ارسال به روبیکا
    try:
        rubika_publish(post)
        print("✅ ارسال روبیکا موفق بود")
    except Exception as e:
        print("❌ خطای روبیکا:", e)
