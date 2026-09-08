# ==============================
# World War - Start Menu
# ==============================

import database
import keyboards


# ارسال پیام از bot.py
send_message = None
edit_message = None


def setup(send_message_function, edit_message_function):
    global send_message
    global edit_message

    send_message = send_message_function
    edit_message = edit_message_function


# =========================
# صفحه انتخاب کشور
# =========================

def show_country_selection(chat_id):
    if send_message is None:
        return

    send_message(
        chat_id,
        "🌍 فرمانده، ابتدا کشور خود را انتخاب کن:",
        keyboards.country_keyboard()
    )


# =========================
# منوی اصلی
# =========================

def show_main_menu(chat_id, user, message_id=None):
    if send_message is None:
        return

    text = (
        "سلام فرمانده! 👋\n"
        "خوش برگشتی.\n\n"
        f"🌍 کشور: {user['country']}\n"
        f"💰 بودجه: {user['budget']:,}\n"
        f"❤️ HP: {user['hp']}%\n\n"
        "فرمانده، دستور بعدی را انتخاب کن:"
    )

    if message_id is not None and edit_message is not None:
        edit_message(
            chat_id,
            message_id,
            text,
            keyboards.main_menu_keyboard()
        )
    else:
        send_message(
            chat_id,
            text,
            keyboards.main_menu_keyboard()
        )


# =========================
# مدیریت آپدیت‌ها
# =========================

def handle_update(update):

    # =========================
    # دریافت پیام
    # =========================

    message = update.get("message")

    if message:
        chat = message.get("chat", {})
        chat_id = chat.get("id")
        text = message.get("text", "")

        if not chat_id:
            return

        # =========================
        # دستور /start
        # =========================

        if text == "/start":

            # گرفتن یا ساخت کاربر
            user = database.get_or_create_user(chat_id)

            # اگر کشور ندارد
            if user["country"] is None:
                show_country_selection(chat_id)

            # اگر کشور دارد
            else:
                show_main_menu(
                    chat_id,
                    user
                )

    # =========================
    # کلیک روی دکمه‌ها
    # =========================

    callback_query = update.get("callback_query")

    if callback_query:

        data = callback_query.get("data")

        message = callback_query.get("message", {})
        chat = message.get("chat", {})

        chat_id = chat.get("id")
        message_id = message.get("message_id")

        if not chat_id:
            return

        # =========================
        # لیست کشورها
        # =========================

        countries = {
            "country_iran": "ایران",
            "country_usa": "آمریکا",
            "country_israel": "اسرائیل",
            "country_russia": "روسیه",
            "country_japan": "ژاپن",
            "country_china": "چین",
            "country_uk": "انگلیس",
            "country_france": "فرانسه",
            "country_germany": "آلمان",
            "country_turkey": "ترکیه",
            "country_india": "هند",
            "country_south_korea": "کره جنوبی",
            "country_north_korea": "کره شمالی",
            "country_saudi_arabia": "عربستان",
            "country_uae": "امارات",
            "country_egypt": "مصر",
            "country_pakistan": "پاکستان",
            "country_ukraine": "اوکراین",
            "country_italy": "ایتالیا",
            "country_spain": "اسپانیا",
            "country_canada": "کانادا",
            "country_australia": "استرالیا",
            "country_brazil": "برزیل",
            "country_mexico": "مکزیک",
            "country_indonesia": "اندونزی",
            "country_vietnam": "ویتنام",
            "country_poland": "لهستان",
            "country_greece": "یونان",
            "country_iraq": "عراق",
            "country_qatar": "قطر"
        }

        # =========================
        # انتخاب کشور
        # =========================

        if data in countries:

            country = countries[data]

            # مطمئن می‌شویم کاربر وجود دارد
            database.get_or_create_user(chat_id)

            # ذخیره کشور
            database.set_country(
                chat_id,
                country
            )

            # گرفتن اطلاعات جدید
            user = database.get_user(chat_id)

            # ویرایش همان پیام
            show_main_menu(
                chat_id,
                user,
                message_id
            )
