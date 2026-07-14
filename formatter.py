from config import HASHTAGS

MAX_DESCRIPTION = 1200


def short_text(text, length=MAX_DESCRIPTION):
    if not text:
        return ""

    text = text.replace("\n", " ")

    if len(text) <= length:
        return text

    return text[:length] + "..."


def format_post(info):

    description = short_text(info["description"])

    hashtags = "\n".join(HASHTAGS)

    post = f"""🌍 {info['title']}

━━━━━━━━━━━━━━

🏛 معرفی

{description}

━━━━━━━━━━━━━━

📖 داستان و تاریخچه

این مکان بخشی از تاریخ و فرهنگ منطقه خود است و در طول سال‌ها اهمیت ویژه‌ای پیدا کرده است. ویژگی‌های معماری، تاریخی یا طبیعی آن باعث شده به یکی از نقاط مورد توجه گردشگران تبدیل شود.

━━━━━━━━━━━━━━

✨ نکات جالب

🔹 دارای ارزش تاریخی، فرهنگی یا طبیعی است.

🔹 یکی از مکان‌های قابل توجه برای علاقه‌مندان به گردشگری محسوب می‌شود.

🔹 بازدید از این مکان فرصتی برای آشنایی با تاریخ و فرهنگ منطقه فراهم می‌کند.

━━━━━━━━━━━━━━

📸 تجربه سفر

این مقصد می‌تواند برای علاقه‌مندان به تاریخ، معماری، طبیعت و عکاسی تجربه‌ای جذاب باشد.

━━━━━━━━━━━━━━

{hashtags}
"""

    if len(post) > 2800:
        post = post[:2700]

    return post
