# для генерации телефонного справочника
from faker import Faker
# для работы с json
import json
# для проверки существует ли файл
import os


# ----------------------------------------------------------------------------------------
# 1. раздел функций работы с фалами

# Чтение из json файла
def read_file_json(filename: str) -> list:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    return []


# запись в json файла, добавление нет, только перезаписать файл
def write_file_json(filename: str, write_text: list):
    with open(filename, 'w', encoding='UTF-8') as json_file:
        # Сортируем список словарей по имени
        write_text = sorted(write_text, key=lambda x: x["name"])
        json.dump(write_text, json_file, ensure_ascii=False, indent=4)


# очистить содержимое файла
def clear_file_json(filename: str):
    with open(filename, 'w', encoding='UTF-8') as json_file:
        json.dump([], json_file, ensure_ascii=False, indent=4)


# конец раздел функций получения данных
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
# 2. функции обработки данных

# Случайная Генерация контакта
def generate_fake_user() -> dict:
    fake = Faker('ru_RU')
    return {
        'name': fake.name(),
        'phone_number': fake.phone_number(),
        'company': fake.company(),
    }


def callbook_clear(filename: str):
    clear_file_json(filename)


# найти контакт
def callbook_find(filename: str, search_area: str, find_name: str) -> list:
    data = read_file_json(filename)
    if search_area.lower() == 'p':
        callbook_show_all(filename)
    elif search_area.lower() == 'n':
        record = [person for person in data if find_name in person["name"]]
        return record
    elif search_area.lower() == 'pn':
        record = [person for person in data if find_name in person["phone_number"]]
        return record
    elif search_area.lower() == 'c':
        record = [person for person in data if find_name in person["company"]]
        return record


# удалить контакт
def callbook_del(filename: str, del_record: dict):
    data = read_file_json(filename)
    data.remove(del_record)
    write_file_json(filename, data)


# прочитать справочник
def callbook_show_all(filename: str):
    data = read_file_json(filename)
    return data
