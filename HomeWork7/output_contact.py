import view

def read_contact():
    data = ''
    with open('phonebook.txt', 'r', encoding='utf8') as file:
        data += file.read()
    with open('phonebook.csv', 'r', encoding='utf8') as file:
        data += file.read()
        return data


def find_contact(data):
    lst = ([i for i in read_contact().split('\n')])
    count = 0
    for i in lst:
        if data.lower() in i.lower():
            view.show_info(i)
            count += 1
    if count == 0:
        view.show_info('Нет такого контакта')