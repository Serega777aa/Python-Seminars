def read_contact():
    with open('phonebook.txt', 'r', encoding='utf8') as file:
        data = file.read()
        return data