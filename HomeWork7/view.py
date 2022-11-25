def show_info(a):
    print(a)


def input_info(b):
    return input(b)   


def select_option():
    show_info('Выберите действие:') 
    show_info('1 - Записать контакт')
    show_info('2 - Показать все контакты')
    show_info('3 - Найти контакт')
    show_info('4 - Удалить контакт')
    show_info('5 - Удалить все контакты')
    return input_info('ваш выбор: ')


def select_format():
    show_info('Выберите формат записи:') 
    show_info('1 - .txt')
    show_info('2 - .csv')
    n = input_info('ваш выбор: ')
    while n != '1' and n != '2':
        n = input_info('ваш выбор: ')
    return n


def select_del():
    show_info('Точно хотите удалить все записи?') 
    show_info('1 - ДА')
    show_info('2 - НЕТ')
    n = input_info('ваш выбор: ')
    while n != '1' and n != '2':
        n = input_info('ваш выбор: ')
    return n
