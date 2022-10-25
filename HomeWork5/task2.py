from random import randint

def input_count(total_count):
    count = int(input('Возьмите от 1 до 28 конфет: '))
    while count < 1 or count > 28 or count > total_count:
        count = int(input('Взяли неверное количество конфет, повторите попытку :'))
    return count
    
input('Нажмите Enter для начала игры')
rnd = randint(0, 1)
count = 2021
while count > 0:
    if rnd == True:
        print(f'Ход 1 игрока, на столе {count} конфет')
        count_1 = input_count(count)
        count -= count_1
        if count < 1:
            print('Победил игрок 1')
        rnd = False
    else:
        print(f'Ход 2 игрока, на столе {count} конфет')
        count_2 = input_count(count)
        count -= count_2
        if count < 1:
            print('Победил игрок 2')
        rnd = True

