def get_image(page_data):
    """
    آدرس تصویر را از اطلاعات ویکی‌پدیا برمی‌گرداند.
    """

    if not page_data:
        return ""

    return page_data.get("image", "")
