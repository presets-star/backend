import sqlite3
import os

# Подготовка раскодирования
def get_unique_filename(directory, base_filename, extension):
    counter = 1
    while True:
        unique_filename = f"{base_filename}_{counter}.{extension}"
        if not os.path.exists(os.path.join(directory, unique_filename)):
            return unique_filename
        counter += 1


def retrieve_file_from_database(column_name, id_value):
    conn = sqlite3.connect('./DataBase/dataBase.sqlite')
    cursor = conn.cursor()

    cursor.execute(f"SELECT {column_name} FROM podcasts WHERE id=?", (id_value,))
    file_data = cursor.fetchone()[0]

    conn.close()
    return file_data


def save_file_to_directory(file_data, directory, base_filename, extension):
    unique_filename = get_unique_filename(directory, base_filename, extension)
    output_path = os.path.join(directory, unique_filename)

    try:
        with open(output_path, 'wb') as f:
            f.write(file_data)
        print(f"Файл успешно сохранен как {output_path}")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")



# Ракодировка аудио файлов
def for_mp3():
    mp3_data = retrieve_file_from_database('demo_podcast_file', 6)
    save_file_to_directory(mp3_data, 'decoded_files', 'decoded_audio', 'mp3')


def for_mp3():
    mp3_data = retrieve_file_from_database('demo_podcast_file', 6)
    save_file_to_directory(mp3_data, 'decoded_files', 'decoded_audio', 'wav')


# Раскодировка пресетов
def for_preset_fl_studio():
    preset_data = retrieve_file_from_database('preset_file', 6)
    save_file_to_directory(preset_data, 'decoded_files', 'decoded_preset', 'fst')

def for_preset_logic_pro():
    preset_data = retrieve_file_from_database('preset_file', 6)
    save_file_to_directory(preset_data, 'decoded_files', 'decoded_preset', 'cst')

def for_preset_studio_one():
    preset_data = retrieve_file_from_database('preset_file', 6)
    save_file_to_directory(preset_data, 'decoded_files', 'decoded_preset', 'preset')

def for_preset_pro_tools():
    preset_data = retrieve_file_from_database('preset_file', 6)
    save_file_to_directory(preset_data, 'decoded_files', 'decoded_preset', 'tfx')

def for_preset_ableton_live():
    preset_data = retrieve_file_from_database('preset_file', 6)
    save_file_to_directory(preset_data, 'decoded_files', 'decoded_preset', 'adv')

def for_preset_reaper():
    preset_data = retrieve_file_from_database('preset_file', 6)
    save_file_to_directory(preset_data, 'decoded_files', 'decoded_preset', 'rfxchain')

for_mp3()