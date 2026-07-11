from config import HASHTAGS

def format_post(title, country, text):

    hashtags = "\n".join(HASHTAGS)

    post = f"""
🌍 {title}

📍 کشور: {country}

📝 {text}

━━━━━━━━━━━━━━

🤔 آیا می‌دانستید؟

این مکان یکی از معروف‌ترین جاذبه‌های گردشگری جهان است و هر سال میلیون‌ها نفر از آن بازدید می‌کنند.

━━━━━━━━━━━━━━

{hashtags}
"""

    return post
