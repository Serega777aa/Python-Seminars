import view
import input_contact 
import output_contact
import delete


def start(n = view.select_option()):   
    
    if n == '1':
        k = view.select_format()
        if k == '1':
            input_contact.add_contact_txt(view.input_info('Введите контакт: '))
        if k == '2':
            input_contact.add_contact_csv(view.input_info('Введите контакт: '))
    elif n == '2':
        view.show_info(output_contact.read_contact())
    elif n == '3':
        output_contact.find_contact(view.input_info('Введите фамилию, имя или номер: '))
    elif n == '4':
        delete.del_contact(view.input_info('Введите фамилию, имя или номер: '))
    elif n == '5':
        k = view.select_del()
        if k == '1':
            delete.del_all_contact()
        else:
            start(n = view.select_option())
        

            
    else: 
        view.show_info('Ввели неверно')
