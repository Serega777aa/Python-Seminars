from random import randint

N = int(input('Введите число N: '))
col = []
for i in range(N):
    col.append(randint(-N, N))
print(col)

x = int(input('Введите позицию 1 элемента: '))
y = int(input('Введите позицию 2 элемента: '))
prod = col[x] * col[y]
print(f'Произведение {x} и {y} позиции равно {prod}')