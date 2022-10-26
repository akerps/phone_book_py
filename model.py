import control

phone_book = []
path = 'task\\data/'

def get_phone_book():
    global phone_book
    return phone_book

def set_path(file):
    global path
    path += file

def open_file():
    global path
    global phone_book
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for item in data:
        contact = item.replace('\n', '').split(';')
        phone_book.append(contact)

def write_file():
    global phone_book
    global path
    with open(path, 'w', encoding='UTF-8') as data:
        for id, item in enumerate(phone_book):
            phone_book[id] = ';'.join(item)
        phone_book = '\n'.join(phone_book)
        print(phone_book)
        data.write(phone_book)
    return phone_book
       

def new_contact(contact):
    global phone_book
    phone_book.append(list(contact))

def change_contact(id, choice, value):
    global phone_book
    phone_book[int(id)][int(choice)] = value

def delete_info(index):
    global phone_book
    phone_book.pop(index)

def searching(choice, value):
    global phone_book
    search_list = []
    for id, item in enumerate(phone_book):
        if value in item[int(choice)]:
            search_list.append(id)
            search_list.append(item)
    return search_list