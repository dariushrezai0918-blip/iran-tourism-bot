def get_category(title, description):

    text = (title + " " + description).lower()


    # مکان های تاریخی
    historical = [
        "قلعه",
        "کاخ",
        "برج",
        "پل",
        "کاروانسرا",
        "باستان",
        "تاریخی",
        "آرامگاه",
        "محوطه"
    ]


    # مکان های طبیعی
    natural = [
        "آبشار",
        "کوه",
        "دریاچه",
        "جزیره",
        "غار",
        "جنگل",
        "دره",
        "ساحل",
        "پارک ملی"
    ]


    # مکان های فرهنگی
    cultural = [
        "موزه",
        "مسجد",
        "کلیسا",
        "معبد",
        "باغ",
        "بازار"
    ]


    for item in historical:
        if item in text:
            return "تاریخی"


    for item in natural:
        if item in text:
            return "طبیعی"


    for item in cultural:
        if item in text:
            return "فرهنگی"


    return "گردشگری"
