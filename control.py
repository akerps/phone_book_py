import view, model

def start ():
    choice = 1
    while choice != 9:
        choice = view.show_menu()
        match(choice):
            case 0:
                phone_book = model.get_phone_book()
                view.show_phone_book(phone_book)
            case 1:
                path = view.input_path()
                model.set_path(path)
                model.open_file()  
            case 2:
                path = view.input_path()
                model.set_path(path)
                model.write_file()
            case 3:
                contact = view.input_contact()
                model.new_contact(contact)
            case 4:
                contact = view.input_change_contact()
                model.change_contact(*contact)
            case 5:
                index = view.delete_contact()
                model.delete_info(index)
            case 6:
                choice, value = view.search_contacts()
                search_list = model.searching(choice, value)
                view.print_search_result(search_list)                     
