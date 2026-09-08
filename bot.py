import requests
import time

from config import BOT_TOKEN, API_URL


# =========================
# تنظیمات اصلی ربات
# =========================

BASE_URL = API_URL


def api_request(method, data=None):
    """
    ارسال درخواست به API بله
    """
    url = f"{BASE_URL}/{method}"

    try:
        response = requests.post(
            url,
            json=data or {},
            timeout=30
        )

        return response.json()

    except requests.RequestException as error:
        print(f"API Error: {error}")
        return None

    except ValueError:
        print("API پاسخ معتبر JSON برنگرداند.")
        return None


# =========================
# دریافت آپدیت‌ها
# =========================

def get_updates(offset=None):
    data = {
        "timeout": 25
    }

    if offset is not None:
        data["offset"] = offset

    return api_request("getUpdates", data)


# =========================
# ارسال پیام
# =========================

def send_message(chat_id, text, reply_markup=None):
    data = {
        "chat_id": chat_id,
        "text": text
    }

    if reply_markup is not None:
        data["reply_markup"] = reply_markup

    return api_request("sendMessage", data)


# =========================
# سیستم اتصال فایل‌ها
# =========================

modules = []


def register_module(module):
    """
    ثبت یک فایل قابلیت در bot.py
    """
    if module not in modules:
        modules.append(module)

    print(f"Module loaded: {module.__name__}")


# =========================
# اتصال ماژول Start
# =========================

import start

start.setup(send_message)
register_module(start)


# =========================
# اجرای ربات
# =========================

def run_bot():
    print("================================")
    print("World War Bot")
    print("Bot is starting...")
    print("================================")

    offset = None

    while True:
        try:
            result = get_updates(offset)

            if not result:
                time.sleep(2)
                continue

            if not result.get("ok"):
                print("API Error:", result)
                time.sleep(3)
                continue

            updates = result.get("result", [])

            for update in updates:
                offset = update["update_id"] + 1

                for module in modules:
                    try:
                        module.handle_update(update)
                    except Exception as error:
                        print(
                            f"Error in {module.__name__}: {error}"
                        )

        except KeyboardInterrupt:
            print("\nBot stopped.")
            break

        except Exception as error:
            print(f"Main Error: {error}")
            time.sleep(5)
