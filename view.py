import control


def show_menu():
    print("0. Показать все контакты")
    print("1. Открыть файл с контактами")
    print("2. Записать файл с контактами")
    print("3. Добавить контакт")
    print("4. Изменить контакт")
    print("5. Удалить контакт")
    print("6. Поиск по контактам")
    choice = int(input("Выберите пункт меню: "))
    return choice

def show_phone_book(phone_book):
    if len(phone_book) < 1:
        print("Телефонная книга пуста!")
    else:
        for id, item in enumerate(phone_book):
            print(id, *item)

def input_path():
    path = input("Введите имя файла: ")
    return path

def input_contact():
    name_contact = input("Введите фамилию и имя контакта: ")
    phone_contact = input("Введите номер телефона контакта: ")
    comment_contact = input("Введите коментарий: ")
    return (name_contact, phone_contact, comment_contact)

def input_change_contact():
    id = int(input('Введите номер контакта: '))
    print('Что изменяем?')
    choice = input(' 0 - имя, 1 - телефон, 2 - комментарий, 3 - отмена: ')
    value = input('Введите изменения: ')
    return (id, choice, value)

def delete_contact():
    index = int(input("Введите id контакта, который нужно удалить: "))
    return index

def search_contacts():
    print("По какой информации ищем?")
    list = ['имя', 'телефон', 'комментарий']
    choice = int(input('0 - имя, 1 - телефон, 2 - комментарий: '))
    value = input(f'Введите {list[choice]}: ')
    return choice, value

def print_search_result(search_list):
    print('Результат поиска:')
    for i in range(0, len(search_list)-1, 2):
        print(search_list[i], *search_list[i+1])

