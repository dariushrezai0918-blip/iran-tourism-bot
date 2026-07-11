from config import HASHTAGS

def format_post(info):
    hashtags = "\n".join(HASHTAGS)

    post = f"""🌍 {info['title']}

📍 کشور: {info['country']}

📝 {info['description']}

━━━━━━━━━━━━━━

🤔 آیا می‌دانستید؟

این مکان یکی از معروف‌ترین جاذبه‌های گردشگری جهان است و هر سال میلیون‌ها نفر از آن بازدید می‌کنند.

📚 مطالعه بیشتر:
{info['wiki']}

━━━━━━━━━━━━━━

{hashtags}
"""

    return post
