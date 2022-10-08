from math import sqrt


xa = float(input('Введите координату x для точки A '))
ya = float(input('Введите координату y для точки A '))
xb = float(input('Введите координату x для точки B '))
yb = float(input('Введите координату y для точки B '))
ab = round(sqrt((xb - xa) ** 2 + (yb - ya) ** 2), 2)
print(f'Расстояние между точками АВ = {ab}')