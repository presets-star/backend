from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3
import base64
import db




app = Flask(__name__)


db.create_db_users()
db.create_db_podcasts()

def db_conn():
    conn = None
    try:
        conn = sqlite3.connect('DataBase/dataBase.sqlite')
        conn.row_factory = sqlite3.Row
    except sqlite3.error as e:
        print(e)
    return conn

########################           CRUD для ПОЛЬЗОВАТЕЛЕЙ          #############################


@app.route("/users", methods=["GET", "POST"])
def users_crud():
    conn = db_conn()
    cursor = conn.cursor()
    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM users")
        users = [
            dict(id=row[0], name=row[1], surname=row[2], email=row[3], password=row[4],
                 profile_picture=base64.b64encode(row[5]).decode('utf-8') if row[5] else None, spend_user=row[6],
                 buyer_user=row[7], wallet_user=row[8], sold_user=row[9], gender_user=row[10], birthday_user=row[11],
                 phone_user=row[12])
            for row in cursor.fetchall()
        ]
        if users is not None:
            return jsonify(users)
    if request.method == "POST":
        new_name = request.form["name_user"]
        new_surname = request.form["surname_user"]
        new_email = request.form["email_user"]
        new_password = request.form["password_user"]
        profile_picture = request.files["profile_picture"].read() if "profile_picture" in request.files else None
        spend_user = request.form["spend_user"]
        buyer_user = request.form["buyer_user"]
        wallet_user = request.form["wallet_user"]
        sold_user = request.form["sold_user"]
        gender_user = request.form["gender_user"]
        birthday_user = request.form["password_user"]
        phone_user = request.form["password_user"]
        sql = """INSERT INTO users (name_user, surname_user, email_user, password_user, profile_picture, spend_user, buyer_user, wallet_user, sold_user, gender_user, birthday_user, phone_user)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        cursor = cursor.execute(sql, (new_name, new_surname, new_email, new_password, profile_picture, spend_user, buyer_user, wallet_user, sold_user, gender_user, birthday_user, phone_user))
        conn.commit()
        return f"Пользователь с айди {cursor.lastrowid} успешно добавлен", 201

@app.route("/user/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_user(id):
    conn = db_conn()
    cursor = conn.cursor()
    user = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM users WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            user = {
                "id": r[0],
                "name_user": r[1],
                "surname_user": r[2],
                "email_user": r[3],
                "password_user": r[4],
                "profile_picture": base64.b64encode(r[5]).decode('utf-8') if r[5] else None,
                "spend_user": r[4],
                "buyer_user": r[6],
                "wallet_user": r[7],
                "sold_user": r[8],
                "gender_user": r[9],
                "birthday_user": r[10],
                "phone_user": r[11]
            }
        if user is not None:
            return jsonify(user), 200
        else:
            return "Пользователь не найден", 404
    if request.method == "PUT":
        sql = """UPDATE users 
                 SET name_user=?, surname_user=?, email_user=?, password_user=?, profile_picture=?, spend_user=?, buyer_user=?, wallet_user=?, sold_user=?, gender_user=?, birthday_user=?, phone_user=?
                 WHERE id=?"""
        name_user = request.form["name_user"]
        surname_user = request.form["surname_user"]
        email_user = request.form["email_user"]
        password_user = request.form["password_user"]
        profile_picture = request.files["profile_picture"].read() if "profile_picture" in request.files else None
        spend_user = request.form["spend_user"]
        buyer_user = request.form["buyer_user"]
        wallet_user = request.form["wallet_user"]
        sold_user = request.form["sold_user"]
        gender_user = request.form["gender_user"]
        birthday_user = request.form["birthday_user"]
        phone_user = request.form["phone_user"]
        update_user = {
            "id": id,
            "name_user": name_user,
            "surname_user": surname_user,
            "email_user": email_user,
            "password_user": password_user,
            "profile_picture": base64.b64encode(profile_picture).decode('utf-8') if profile_picture else None,
            "spend_user": spend_user,
            "buyer_user": buyer_user,
            "wallet_user": wallet_user,
            "sold_user": sold_user,
            "gender_user": gender_user,
            "birthday_user": birthday_user,
            "phone_user": phone_user,
        }
        conn.execute(sql, (name_user, surname_user, email_user, password_user, profile_picture,
                           spend_user, buyer_user, wallet_user, sold_user, gender_user,
                           birthday_user, phone_user, id))
        conn.commit()
        return jsonify(update_user), 200
    if request.method == "DELETE":
        sql = """DELETE FROM users WHERE id=?"""
        conn.execute(sql, (id,))
        conn.commit()
        return f"Пользователь с айди {id} был удален", 200




########################           CRUD для ПОДКАСТОВ          #############################





@app.route('/podcasts', methods=["GET", "POST"])
def podcasts_crud():
    now = datetime.now()
    date_str = f"{now.day:02d}-{now.month:02d}-{now.year}"

    conn = db_conn()
    cursor = conn.cursor()
    if request.method == "GET":
        try:
            cursor.execute("SELECT * FROM podcasts")
            podcasts = [
                dict(id=row['id'], name_podcast=row['name_podcast'], name_auth_podcast=row['name_auth_podcast'],
                     name_coauth_podcast=row['name_coauth_podcast'], date_podcast=row['date_podcast'],
                     avatar_podcast=base64.b64encode(row['avatar_podcast']).decode('utf-8') if row['avatar_podcast'] else None,
                     price_podcast=row['price_podcast'], duration_podcast=row['duration_podcast'],
                     programm_os_podcast=row['programm_os_podcast'], tags_podcast=row['tags_podcast'],
                     rate_podcast=row['rate_podcast'], demo_podcast_file=base64.b64encode(row['demo_podcast_file']).decode('utf-8') if row['demo_podcast_file'] else None,
                     preset_file=base64.b64encode(row['preset_file']).decode('utf-8') if row['preset_file'] else None)
                for row in cursor.fetchall()
            ]
            return jsonify(podcasts)
        except Exception as e:
            print(f"Ошибка при выполнении GET-запроса: {e}")
            return "Произошла ошибка на сервере", 500

    if request.method == "POST":
        try:
            name_podcast = request.form["name_podcast"]
            name_auth_podcast = request.form["name_auth_podcast"]
            name_coauth_podcast = request.form["name_coauth_podcast"]
            date_podcast = date_str
            avatar_podcast = request.files["avatar_podcast"].read() if "avatar_podcast" in request.files else None
            demo_podcast_file = request.files["demo_podcast_file"].read() if "demo_podcast_file" in request.files else None
            preset_file = request.files["preset_file"].read() if "preset_file" in request.files else None
            price_podcast = request.form["price_podcast"]
            duration_podcast = request.form["duration_podcast"]
            programm_os_podcast = request.form["programm_os_podcast"]
            tags_podcast = request.form["tags_podcast"]
            rate_podcast = request.form["rate_podcast"]

            sql = """INSERT INTO podcasts (name_podcast, name_auth_podcast, name_coauth_podcast, date_podcast, price_podcast, duration_podcast, programm_os_podcast, tags_podcast, rate_podcast, avatar_podcast, demo_podcast_file, preset_file)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
            cursor.execute(sql, (name_podcast, name_auth_podcast, name_coauth_podcast, date_podcast,
                                 price_podcast, duration_podcast, programm_os_podcast, tags_podcast,
                                 rate_podcast, avatar_podcast, demo_podcast_file, preset_file))
            conn.commit()
            return f"Подкаст с айди {cursor.lastrowid} успешно добавлен", 201
        except Exception as e:
            print(f"Ошибка при выполнении POST-запроса: {e}")
            return "Произошла ошибка на сервере", 500

@app.route("/podcast/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_podcast(id):
    now = datetime.now()
    date_str = f"{now.day:02d}-{now.month:02d}-{now.year}"
    conn = db_conn()
    cursor = conn.cursor()

    if request.method == "GET":
        try:
            cursor.execute("SELECT * FROM podcasts WHERE id=?", (id,))
            row = cursor.fetchone()
            if row:
                podcast = {
                    "id": row['id'],
                    "name_podcast": row['name_podcast'],
                    "name_auth_podcast": row['name_auth_podcast'],
                    "name_coauth_podcast": row['name_coauth_podcast'],
                    "date_podcast": row['date_podcast'],
                    "price_podcast": row['price_podcast'],
                    "duration_podcast": row['duration_podcast'],
                    "programm_os_podcast": row['programm_os_podcast'],
                    "tags_podcast": row['tags_podcast'],
                    "rate_podcast": row['rate_podcast'],
                    "avatar_podcast": base64.b64encode(row['avatar_podcast']).decode('utf-8') if row['avatar_podcast'] else None,
                    "demo_podcast_file": base64.b64encode(row['demo_podcast_file']).decode('utf-8') if row['demo_podcast_file'] else None,
                    "preset_file": base64.b64encode(row['preset_file']).decode('utf-8') if row[
                        'preset_file'] else None
                }
                return jsonify(podcast), 200
            else:
                return "Подкаст не найден", 404
        except Exception as e:
            print(f"Ошибка при выполнении GET-запроса для одного подкаста: {e}")
            return "Произошла ошибка на сервере", 500

    if request.method == "PUT":
        try:
            name_podcast = request.form["name_podcast"]
            name_auth_podcast = request.form["name_auth_podcast"]
            name_coauth_podcast = request.form["name_coauth_podcast"]
            date_podcast = date_str
            price_podcast = request.form["price_podcast"]
            duration_podcast = request.form["duration_podcast"]
            programm_os_podcast = request.form["programm_os_podcast"]
            tags_podcast = request.form["tags_podcast"]
            rate_podcast = request.form["rate_podcast"]
            avatar_podcast = request.files["avatar_podcast"].read() if "avatar_podcast" in request.files else None
            demo_podcast_file = request.files["demo_podcast_file"].read() if "demo_podcast_file" in request.files else None,
            preset_file = request.files["preset_file"].read() if "preset_file" in request.files else None

            sql = """UPDATE podcasts 
                     SET name_podcast=?, name_auth_podcast=?, name_coauth_podcast=?, date_podcast=?, price_podcast=?, duration_podcast=?, programm_os_podcast=?, tags_podcast=?, rate_podcast=?, avatar_podcast=?, demo_podcast_file=?, preset_file=?
                     WHERE id=?"""
            cursor.execute(sql, (name_podcast, name_auth_podcast, name_coauth_podcast, date_podcast,
                                 price_podcast, duration_podcast, programm_os_podcast, tags_podcast,
                                 rate_podcast, avatar_podcast, demo_podcast_file, preset_file, id))
            conn.commit()
            update_podcast = {
                "id": id,
                "name_podcast": name_podcast,
                "name_auth_podcast": name_auth_podcast,
                "name_coauth_podcast": name_coauth_podcast,
                "date_podcast": date_podcast,
                "price_podcast": price_podcast,
                "duration_podcast": duration_podcast,
                "programm_os_podcast": programm_os_podcast,
                "tags_podcast": tags_podcast,
                "rate_podcast": rate_podcast,
                "avatar_podcast": base64.b64encode(avatar_podcast).decode('utf-8') if avatar_podcast else None,
                "demo_podcast_file": base64.b64encode(demo_podcast_file).decode('utf-8') if demo_podcast_file else None,
                "preset_file": base64.b64encode(preset_file).decode('utf-8') if preset_file else None,
            }
            return jsonify(update_podcast), 200
        except Exception as e:
            print(f"Ошибка при выполнении PUT-запроса: {e}")
            return "Произошла ошибка на сервере", 500

    if request.method == "DELETE":
        try:
            sql = """DELETE FROM podcasts WHERE id=?"""
            cursor.execute(sql, (id,))
            conn.commit()
            return f"Подкаст с айди {id} был удален", 200
        except Exception as e:
            print(f"Ошибка при выполнении DELETE-запроса: {e}")
            return "Произошла ошибка на сервере", 500

if __name__ == "__main__":
    app.run(debug=True)