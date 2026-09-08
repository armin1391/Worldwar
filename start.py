# ==============================
# World War - Start Menu
# ==============================

# ارسال پیام از bot.py بعداً به این فایل وصل می‌شود
send_message = None

# کشور انتخاب‌شده کاربران
# فعلاً موقت است؛ بعداً به database.py وصل می‌شود
user_countries = {}


def setup(send_message_function):
    global send_message
    send_message = send_message_function


def country_keyboard():
    return {
        "inline_keyboard": [
            [
                {"text": "🇮🇷 ایران", "callback_data": "country_iran"},
                {"text": "🇷🇺 روسیه", "callback_data": "country_russia"}
            ],
            [
                {"text": "🇺🇸 آمریکا", "callback_data": "country_usa"},
                {"text": "🇩🇪 آلمان", "callback_data": "country_germany"}
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


def show_main_menu(chat_id, country):
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

        if not chat_id:
            return

        countries = {
            "country_iran": "ایران",
            "country_russia": "روسیه",
            "country_usa": "آمریکا",
            "country_germany": "آلمان"
        }

        # انتخاب کشور
        if data in countries:
            country = countries[data]

            user_countries[chat_id] = country

            show_main_menu(chat_id, country)
