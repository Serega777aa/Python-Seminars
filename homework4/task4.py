from random import randint

k = input('Задайте степень: ')
ist = []
for i in range(int(k), -1, -1):
    ist.append(randint(-100, 100))
    if i == 0:
        continue
    if i == 1:
        ist.append('x + ')
    if i > 1:
        ist.append('x^')
        ist.append(i)
        ist.append(' + ')
ist.append(' = 0')
s = ''.join(map(str, ist))


f = open('myfile.txt', 'w')
f.write(s)
f.close()