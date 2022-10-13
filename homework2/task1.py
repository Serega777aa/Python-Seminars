n = float(input('Введите вещественное число: '))
sum_digits = 0
line = str(n)
for i in line:
    if i != '.':
        sum_digits += int(i)
print(f'Сумма цифр = {sum_digits}')