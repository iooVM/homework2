# Для глубокого копирования словаря
import copy

from view import menu, menu_record, menu_record_deleted, menu_record_edit, menu_record_input_name, \
    menu_record_view, menu_record_input_phone, menu_record_input_company, menu_callbook_find, menu_show_all, \
    menu_callbook_add, menu_add_manual

from model import callbook_show_all, callbook_clear, callbook_del, read_file_json, \
    write_file_json, callbook_find, generate_fake_user

# Файл телефонного справочника json
callbook_file_json = 'callbook.json'


def start_programm():
    choice = ''
    while choice != 'e':
        choice = menu()
        # показать все записи
        if choice == 'p':
            data = callbook_show_all(callbook_file_json)
            menu_show_all(data)
        # Добавить запись
        elif choice == 'a':
            choice6 = ''
            data = read_file_json(callbook_file_json)
            while choice6 != 'e':
                choice6 = menu_callbook_add()
                # Записать
                if choice6 == 'w':
                    write_file_json(callbook_file_json, data)
                # Сгенерировать запись
                elif choice6 == 'g':
                    record = generate_fake_user()
                    data.append(record)
                # Добавить в ручную
                elif choice6 == 'a':
                    record = menu_add_manual()
                    data.append(record)
        # Очистить все записи
        elif choice == 'c':
            callbook_clear(callbook_file_json)
        # Поиск записи
        elif choice == 'f':
            choice5, find_name = menu_callbook_find()
            find_record = callbook_find(callbook_file_json, choice5, find_name)
            choice2 = menu_record(find_record)
            if choice2 == 'd':
                callbook_del(callbook_file_json, find_record[0])
                menu_record_deleted()
            # Редактировать запись
            elif choice2 == 'm':
                choice3 = menu_record_edit()
                # Выбор поля для редактирования имя
                if choice3 == 'n':
                    new_name = menu_record_input_name()
                    rename_record = copy.deepcopy(find_record[0])
                    rename_record['name'] = new_name
                    choice4 = menu_record_view(rename_record)
                    # Редактировать имя
                    if choice4 == 'y':
                        callbook_del(callbook_file_json, find_record[0])
                        data = read_file_json(callbook_file_json)
                        data.append(rename_record)
                        write_file_json(callbook_file_json, data)
                # Выбор поля для редактирования телефон
                elif choice3 == 'pn':
                    new_name = menu_record_input_phone()
                    rename_record = copy.deepcopy(find_record[0])
                    rename_record['phone_number'] = new_name
                    choice4 = menu_record_view(rename_record)
                    # Редактировать телефон
                    if choice4 == 'y':
                        callbook_del(callbook_file_json, find_record[0])
                        data = read_file_json(callbook_file_json)
                        data.append(rename_record)
                        write_file_json(callbook_file_json, data)
                # Выбор поля для редактирования компания
                elif choice3 == 'c':
                    new_name = menu_record_input_company()
                    rename_record = copy.deepcopy(find_record[0])
                    rename_record['company'] = new_name
                    choice4 = menu_record_view(rename_record)
                    if choice4 == 'y':
                        callbook_del(callbook_file_json, find_record[0])
                        data = read_file_json(callbook_file_json)
                        data.append(rename_record)
                        write_file_json(callbook_file_json, data)
