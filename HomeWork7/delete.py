import output_contact
import view

def del_contact(data):
    lst = []
    with open('phonebook.txt', 'r', encoding='utf8') as file:
        lst = file.readlines()
        for i in lst:
            if data.lower() in i.lower():
                lst.remove(i)
            else:
                view.show_info('Нет такого контакта в phonebook.txt')
                break
    with open('phonebook.txt', 'w', encoding='utf8') as file:
        file.write(' '.join(lst))
    
    with open('phonebook.csv', 'r', encoding='utf8') as file:
        lst = file.readlines()
        for i in lst:
            if data.lower() in i.lower():
                lst.remove(i)
            else:
                view.show_info('Нет такого контакта в phonebook.csv')
                break
    with open('phonebook.csv', 'w', encoding='utf8') as file:
        file.write(' '.join(lst))
    
    
        
    


def del_all_contact():
    with open('phonebook.txt', 'w') as file:
        file.write('')

    with open('phonebook.csv', 'w') as file:
        file.write('')
