# для рисования красивой таблички
import pandas as pd

# ширина окна
WINDOW_WIDTH = 180


# Блок консольного интерфейса
# -----------------------------

# Основное меню
def menu() -> str:
    choice = ''
    while choice != 'e':
        # Ввод данных от пользователя
        print('-' * WINDOW_WIDTH)
        print('e - (exit) Выход')
        print('p - (print) Показать все контакты')
        print('a - (add) Добавить новую запись')
        print('c - (clear) Очистить справочника')
        print('f - (find) Поиск по справочнику, удалить или изменить запись ')
        choice = input("Что делаем ? : ")
        print('-' * WINDOW_WIDTH)
        return choice


# Меню работы с записью
def menu_record(find_record: list) -> str:
    print('-' * WINDOW_WIDTH)
    print(f'найдено {find_record}')
    choice2 = input("d - (del) удалить, m - (modify), любая другая клавиша - оставить в покое : ")
    print('-' * WINDOW_WIDTH)
    return choice2


# Меню удалённой записи
def menu_record_deleted():
    print('-' * WINDOW_WIDTH)
    print('Запись удалена ')
    print('-' * WINDOW_WIDTH)


# Меню редактирования записи
def menu_record_edit() -> str:
    print('-' * WINDOW_WIDTH)
    print(' Что изменить ? :')
    print(" 'n' - (name) Имя")
    print(" 'pn' - (phone number) Номер телефона")
    print(" 'с' - (company) компанию")
    print(" любая другая клавиша - оставить в покое")
    choice3 = input(' :')
    print('-' * WINDOW_WIDTH)
    return choice3


# Меню ввода нового имени
def menu_record_input_name() -> str:
    print('-' * WINDOW_WIDTH)
    name = input("Введите новое имя ")
    print('-' * WINDOW_WIDTH)
    return name


# Меню ввода подтверждения
def menu_record_view(rename_record) -> str:
    print('-' * WINDOW_WIDTH)
    print(f'Выглядит так {rename_record}. перезаписать (y - yes) ')
    choice4 = input(' :')
    print('-' * WINDOW_WIDTH)
    return choice4


# Меню ввода нового имени
def menu_record_input_phone() -> str:
    print('-' * WINDOW_WIDTH)
    phone = input("введите новый номер телефона ")
    print('-' * WINDOW_WIDTH)
    return phone


# Меню ввода нового имени
def menu_record_input_company() -> str:
    print('-' * WINDOW_WIDTH)
    company = input("Введите новую компанию ")
    print('-' * WINDOW_WIDTH)
    return company


# Меню поиска контакта
def menu_callbook_find() -> str:
    print('-' * WINDOW_WIDTH)
    company = input("Введите новую компанию ")
    print('-' * WINDOW_WIDTH)
    return company


# Меню поиска контакта


def menu_callbook_find() -> tuple[str, str]:
    print("'n'   - (name) Искать по имени ")
    print("'pn'  - (phone number) Искать по номеру телефона  ")
    print("'c'   - (company) Искать по копании  ")
    choice = input("Что делаем ? :  ")
    # return callbook_find(filename, choice)
    if choice.lower() == 'n':
        find_name = input("Кого искать ? :  ")
        return choice.lower(), find_name
    elif choice.lower() == 'pn':
        find_name = input("Какой номер искать ? :  ")
        return choice.lower(), find_name
    elif choice.lower() == 'c':
        find_name = input("Какую компанию искать ? :  ")
        return choice.lower(), find_name


# Показать всю книгу
def menu_show_all(data: str):
    df = pd.DataFrame(data)
    print('-' * WINDOW_WIDTH)
    print(df.to_string(index=False, header=True, justify='center', col_space=40))
    print('-' * WINDOW_WIDTH)


# Меню добавить контакт
def menu_callbook_add():
    print('-' * WINDOW_WIDTH)

    # Ввод данных от пользователя
    print('-' * WINDOW_WIDTH)
    print("'g'  - (generate) Сгенерировать случайно")
    print("'a'  - (add) Ввести в ручную  ")
    print("'w'  - (write) Сохранить")
    # print("'we' - (write and exit) Сохранить и выйти ")
    print("'e'  - (exit) Выход без сохранения ")
    # print("'p'  - (print) Показать все контакты ")

    choice = input("Что делаем ? :  ")
    print('-' * WINDOW_WIDTH)
    return choice


# Добавление записи в ручную
def menu_add_manual() -> dict:
    print('-' * WINDOW_WIDTH)
    name = input("Введите имя  : ")
    phone_number = input("Введите номер телефона : ")
    company = input("Введите компанию: ")
    print('-' * WINDOW_WIDTH)
    record = {
        'name': name,
        'phone_number': phone_number,
        'company': company,
    }
    print(f"Новая запись: {list(map(lambda x: x, record.values()))}")
    return record
