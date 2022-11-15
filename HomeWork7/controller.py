import view
import input_contact 
import output_contact

def start():   
    n = view.input_info('Выберите действие: \n1 - Записать контакт \n2 - Показать все контакты \n3 - Найти контакт \n')
    if n == '1':
        data = input('Введите фамилию имя телефон: ')
        input_contact.add_contact(data)
    elif n == '2':
        view.show_info(output_contact.read_contact())
    elif n == '3':
        data =  view.input_info('Введите фамилию, имя или номер: ')
        lst = ([i for i in output_contact.read_contact().split('\n')])
        count = 0
        for i in lst:
            if data.lower() in i.lower():
                view.show_info(i)
                count += 1
        if count == 0:
                view.show_info('Нет такого контакта')

            
    else: 
        view.show_info('Ввели неверно')
