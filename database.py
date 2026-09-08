# ==============================
# World War - Database
# ==============================

import sqlite3

from config import DATABASE_NAME


# =========================
# اتصال به دیتابیس
# =========================

def get_connection():
    return sqlite3.connect(DATABASE_NAME)


# =========================
# ساخت جداول
# =========================

def init_db():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            country TEXT,
            budget INTEGER DEFAULT 100000,
            hp INTEGER DEFAULT 100
        )
    """)

    connection.commit()
    connection.close()


# =========================
# ساخت کاربر
# =========================

def create_user(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO users
        (user_id, country, budget, hp)
        VALUES (?, ?, ?, ?)
    """, (
        user_id,
        None,
        100000,
        100
    ))

    connection.commit()
    connection.close()


# =========================
# گرفتن اطلاعات کاربر
# =========================

def get_user(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT user_id, country, budget, hp
        FROM users
        WHERE user_id = ?
    """, (user_id,))

    user = cursor.fetchone()

    connection.close()

    if user is None:
        return None

    return {
        "user_id": user[0],
        "country": user[1],
        "budget": user[2],
        "hp": user[3]
    }


# =========================
# گرفتن یا ساخت کاربر
# =========================

def get_or_create_user(user_id):
    user = get_user(user_id)

    if user is None:
        create_user(user_id)
        user = get_user(user_id)

    return user


# =========================
# انتخاب کشور
# =========================

def set_country(user_id, country):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE users
        SET country = ?
        WHERE user_id = ?
    """, (country, user_id))

    connection.commit()
    connection.close()


# =========================
# تغییر بودجه
# =========================

def update_budget(user_id, budget):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE users
        SET budget = ?
        WHERE user_id = ?
    """, (budget, user_id))

    connection.commit()
    connection.close()


# =========================
# تغییر HP
# =========================

def update_hp(user_id, hp):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE users
        SET hp = ?
        WHERE user_id = ?
    """, (hp, user_id))

    connection.commit()
    connection.close()
