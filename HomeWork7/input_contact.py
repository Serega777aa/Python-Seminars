def add_contact_txt(data):
    with open('phonebook.txt', 'a+', encoding='utf8') as file:
        file.write(data + '\n')


def add_contact_csv(data):
    with open('phonebook.csv', 'a+', encoding='utf8') as file:
        file.write(data + '\n')

