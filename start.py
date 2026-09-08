# ==============================
# World War - Start Menu
# ==============================

# ارسال پیام از bot.py بعداً به این فایل وصل می‌شود
send_message = None
edit_message = None

# کشور انتخاب‌شده کاربران
# فعلاً موقت است؛ بعداً به database.py وصل می‌شود
user_countries = {}


def setup(send_message_function, edit_message_function):
    global send_message
    global edit_message

    send_message = send_message_function
    edit_message = edit_message_function


def country_keyboard():
    return {
        "inline_keyboard": [
            [
                {"text": "🇮🇷 ایران", "callback_data": "country_iran"},
                {"text": "🇺🇸 آمریکا", "callback_data": "country_usa"},
                {"text": "🇮🇱 اسرائیل", "callback_data": "country_israel"}
            ],
            [
                {"text": "🇷🇺 روسیه", "callback_data": "country_russia"},
                {"text": "🇯🇵 ژاپن", "callback_data": "country_japan"},
                {"text": "🇨🇳 چین", "callback_data": "country_china"}
            ],
            [
                {"text": "🇬🇧 انگلیس", "callback_data": "country_uk"},
                {"text": "🇫🇷 فرانسه", "callback_data": "country_france"},
                {"text": "🇩🇪 آلمان", "callback_data": "country_germany"}
            ],
            [
                {"text": "🇹🇷 ترکیه", "callback_data": "country_turkey"},
                {"text": "🇮🇳 هند", "callback_data": "country_india"},
                {"text": "🇰🇷 کره جنوبی", "callback_data": "country_south_korea"}
            ],
            [
                {"text": "🇰🇵 کره شمالی", "callback_data": "country_north_korea"},
                {"text": "🇸🇦 عربستان", "callback_data": "country_saudi_arabia"},
                {"text": "🇦🇪 امارات", "callback_data": "country_uae"}
            ],
            [
                {"text": "🇪🇬 مصر", "callback_data": "country_egypt"},
                {"text": "🇵🇰 پاکستان", "callback_data": "country_pakistan"},
                {"text": "🇺🇦 اوکراین", "callback_data": "country_ukraine"}
            ],
            [
                {"text": "🇮🇹 ایتالیا", "callback_data": "country_italy"},
                {"text": "🇪🇸 اسپانیا", "callback_data": "country_spain"},
                {"text": "🇨🇦 کانادا", "callback_data": "country_canada"}
            ],
            [
                {"text": "🇦🇺 استرالیا", "callback_data": "country_australia"},
                {"text": "🇧🇷 برزیل", "callback_data": "country_brazil"},
                {"text": "🇲🇽 مکزیک", "callback_data": "country_mexico"}
            ],
            [
                {"text": "🇮🇩 اندونزی", "callback_data": "country_indonesia"},
                {"text": "🇻🇳 ویتنام", "callback_data": "country_vietnam"},
                {"text": "🇵🇱 لهستان", "callback_data": "country_poland"}
            ],
            [
                {"text": "🇬🇷 یونان", "callback_data": "country_greece"},
                {"text": "🇮🇶 عراق", "callback_data": "country_iraq"},
                {"text": "🇶🇦 قطر", "callback_data": "country_qatar"}
            ]
        ]
    }


def main_menu_keyboard():
    return {
        "inline_keyboard": [
            [
                {"text": "🌍 کشور من", "callback_data": "my_country"},
                {"text": "🔫 بازار تسلیحات", "callback_data": "arms_market"}
            ],
            [
                {"text": "🏢 شرکت‌های بین‌المللی", "callback_data": "international_companies"}
            ],
            [
                {"text": "📦 صادرات/واردات", "callback_data": "trade"}
            ],
            [
                {"text": "📢 صدور بیانیه", "callback_data": "statement"}
            ],
            [
                {"text": "⚔️ قوانین جنگ", "callback_data": "war_rules"}
            ],
            [
                {"text": "💥 حمله نظامی", "callback_data": "attack"}
            ]
        ]
    }


def show_country_selection(chat_id):
    if send_message is None:
        return

    send_message(
        chat_id,
        "🌍 فرمانده، ابتدا کشور خود را انتخاب کن:",
        country_keyboard()
    )


def show_main_menu(chat_id, country, message_id=None):
    if send_message is None:
        return

    text = (
        "سلام فرمانده! 👋\n"
        "خوش برگشتی.\n\n"
        f"🌍 کشور: {country}\n"
        "💰 بودجه: 100,000\n"
        "❤️ HP: 100%\n\n"
        "فرمانده، دستور بعدی را انتخاب کن:"
    )

    if message_id is not None and edit_message is not None:
        edit_message(
            chat_id,
            message_id,
            text,
            main_menu_keyboard()
        )
    else:
        send_message(
            chat_id,
            text,
            main_menu_keyboard()
        )


def handle_update(update):
    if send_message is None:
        return

    # دریافت پیام
    message = update.get("message")

    if message:
        chat = message.get("chat", {})
        chat_id = chat.get("id")
        text = message.get("text", "")

        if not chat_id:
            return

        # دستور /start
        if text == "/start":
            if chat_id not in user_countries:
                show_country_selection(chat_id)
            else:
                show_main_menu(chat_id, user_countries[chat_id])

    # دریافت کلیک روی دکمه‌های شیشه‌ای
    callback_query = update.get("callback_query")

    if callback_query:
        data = callback_query.get("data")
        message = callback_query.get("message", {})
        chat = message.get("chat", {})
        chat_id = chat.get("id")
        message_id = message.get("message_id")

        if not chat_id:
            return

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

        # انتخاب کشور
        if data in countries:
            country = countries[data]

            user_countries[chat_id] = country

            show_main_menu(
                chat_id,
                country,
                message_id
            )
