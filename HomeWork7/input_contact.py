def add_contact(data):
    with open('phonebook.txt', 'a+', encoding='utf8') as file:
        file.write(data + '\n')

