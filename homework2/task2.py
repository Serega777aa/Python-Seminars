N = int(input('Введите целое число: '))
prod = 1
col = []
for i in range(1, N + 1):
    prod *= i
    col.append(prod)
print(col)
