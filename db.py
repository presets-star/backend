import sqlite3

def create_db_users():
    conn = sqlite3.connect("DataBase/dataBase.sqlite")

    cursor = conn.cursor()
    sql_query = """ CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_user TEXT NOT NULL,
        surname_user TEXT NOT NULL,
        email_user TEXT NOT NULL,
        password_user TEXT NOT NULL,
        profile_picture BLOB,
        spend_user INTEGER NOT NULL,
        buyer_user INTEGER NOT NULL,
        wallet_user INTEGER NOT NULL,
        sold_user INTEGER NOT NULL,
        gender_user TEXT NOT NULL,
        birthday_user TEXT NOT NULL,
        phone_user INTEGER NOT NULL
    );"""

    cursor.execute(sql_query)

def create_db_podcasts():
    conn = sqlite3.connect("DataBase/dataBase.sqlite")

    cursor = conn.cursor()
    sql_query = """CREATE TABLE IF NOT EXISTS podcasts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name_podcast TEXT NOT NULL,
    name_auth_podcast TEXT NOT NULL,
    name_coauth_podcast TEXT NOT NULL,
    date_podcast TEXT NOT NULL,
    price_podcast INTEGER NOT NULL,
    duration_podcast INTEGER NOT NULL,
    programm_os_podcast TEXT NOT NULL,
    tags_podcast TEXT NOT NULL,
    rate_podcast INTEGER NOT NULL,
    avatar_podcast BLOB,
    demo_podcast_file BLOB,
    preset_file BLOB
    );"""

    cursor.execute(sql_query)