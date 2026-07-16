BAD_WORDS = [

    "فیلم",
    "سریال",
    "بازی",
    "رمان",
    "کتاب",
    "آلبوم",
    "ترانه",
    "خواننده",
    "بازیگر",
    "شخصیت",
    "فوتبال",
    "باشگاه",
    "بازیکن",
    "سیاستمدار",
    "نماینده",
    "یوسف پیامبر",
    "فصل",
    "قسمت"

]

GOOD_WORDS = [

    "کاخ",
    "قلعه",
    "موزه",
    "جزیره",
    "پارک",
    "غار",
    "آبشار",
    "دریاچه",
    "برج",
    "کوه",
    "مسجد",
    "کلیسا",
    "معبد",
    "شهر",
    "روستا",
    "پل",
    "بازار",
    "میراث",
    "تاریخی",
    "گردشگری"

]


def is_place(title):

    title = title.lower()

    for word in BAD_WORDS:

        if word in title:
            return False

    for word in GOOD_WORDS:

        if word in title:
            return True

    return False
