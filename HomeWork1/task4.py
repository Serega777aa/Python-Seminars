diapason_x = [-50, 50]
diapason_y = [-50, 50]
quarter = int(input('Введите номер четверти: '))
if quarter == 1:
    print(f'диапазон возможных координат точек в {quarter} четверти для x от {0} до {diapason_x[1]}, для y от {0} до {diapason_y[1]}')
elif quarter == 2:
    print(f'диапазон возможных координат точек в {quarter} четверти для x от {diapason_x[0]} до {0}, для y от {0} до {diapason_y[1]}')
elif quarter == 3:
    print(f'диапазон возможных координат точек в {quarter} четверти для x от {diapason_x[0]} до {0}, для y от {diapason_y[0]} до {0}')
elif quarter == 4:
    print(f'диапазон возможных координат точек в {quarter} четверти для x от {0} до {diapason_x[1]}, для y от {diapason_y[0]} до {0}')
else:
    print('Ввели несуществующую четверть')