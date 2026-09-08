# ==============================
# World War - Keyboards
# ==============================


# =========================
# دکمه‌های انتخاب کشور
# =========================

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


# =========================
# منوی اصلی
# =========================

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
