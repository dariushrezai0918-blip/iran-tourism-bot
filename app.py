from generator import generate_post
from publisher import publish

print("ربات گردشگری ایران شروع شد...")

post = generate_post()

if post:
    publish(post)
else:
    print("خطا در تولید محتوا")
