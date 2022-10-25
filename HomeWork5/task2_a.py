from random import randint

def input_count(total_count):
    count = int(input('Возьмите от 1 до 28 конфет: '))
    while count < 1 or count > 28 or count > total_count:
        count = int(input('Взяли неверное количество конфет, повторите попытку :'))
    return count

def bot_move(total_count):
    count = randint(1, 28)
    while count > total_count:
        count = randint(1, 28)
    return count
    
input('Нажмите Enter для начала игры')
rnd = randint(0, 1)
count = 100
while count > 0:
    if rnd == True:
        print(f'Ваш ход, на столе {count} конфет')
        count_1 = input_count(count)
        count -= count_1
        if count < 1:
            print('Вы победили!')
        rnd = False
    else:
        count_2 = bot_move(count)
        print(f'На столе было {count} конфет, бот взял {count_2}')
        count -= count_2
        if count < 1:
            print('Победил бот')
        rnd = True

