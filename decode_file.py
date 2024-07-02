import sqlite3

def for_mp3 ():
    def retrieve_mp3_from_database():
        conn = sqlite3.connect('./DataBase/dataBase.sqlite')
        cursor = conn.cursor()

        # Предположим, что mp3 файл хранится в поле с именем mp3_data в таблице mp3_table
        cursor.execute("SELECT demo_podcast_file FROM podcasts WHERE id=?", (6,))
        mp3_data = cursor.fetchone()[0]  # Предположим, что данные возвращаются в виде байтов

        conn.close()
        return mp3_data

    def save_mp3_to_file(mp3_data, output_file):
        try:
            with open(output_file, 'wb') as f:
                f.write(mp3_data)
            print(f"MP3 файл успешно сохранен как {output_file}")
        except Exception as e:
            print(f"Ошибка при сохранении MP3 файла: {e}")

    # Пример использования:
    mp3_data_from_db = retrieve_mp3_from_database()
    output_file = 'decoded_audio.mp3'  # Имя файла для сохранения декодированного аудио
    save_mp3_to_file(mp3_data_from_db, output_file)

def for_preset ():
    def retrieve_mp3_from_database():
        conn = sqlite3.connect('./DataBase/dataBase.sqlite')
        cursor = conn.cursor()

        # Предположим, что mp3 файл хранится в поле с именем mp3_data в таблице mp3_table
        cursor.execute("SELECT preset_file FROM podcasts WHERE id=?", (6,))
        mp3_data = cursor.fetchone()[0]  # Предположим, что данные возвращаются в виде байтов

        conn.close()
        return mp3_data

    def save_mp3_to_file(mp3_data, output_file):
        try:
            with open(output_file, 'wb') as f:
                f.write(mp3_data)
            print(f"FST файл успешно сохранен как {output_file}")
        except Exception as e:
            print(f"Ошибка при сохранении FST файла: {e}")

    # Пример использования:
    mp3_data_from_db = retrieve_mp3_from_database()
    output_file = 'decoded_preset.fst'  # Имя файла для сохранения декодированного аудио
    save_mp3_to_file(mp3_data_from_db, output_file)


for_preset()