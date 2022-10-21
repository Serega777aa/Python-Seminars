import math

d = input('Задайте точность: ')
pi = str(math.pi)
pi = pi[: len(d)]
p = 0
i = 1
while str(p)[: len(d)] != pi:
    p += 4 * ((-1) ** (i + 1)) / (2 * i - 1)
    i += 1
print(f'при d = {d}, π = {round(p, len(d))}')
print(pi)