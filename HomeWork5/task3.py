board = list(range(1, 10))

def draw_board():
    print('-' * 13)
    for i in range(3):
        print('|', board[0 + i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
    print('-' * 13)

def input_mark():
    mark = int(input(f'Ходит "{player}" введите цифру: '))
    while (mark < 1 or mark > 9) or str(board[mark - 1]).isalpha():
         mark = int(input('Ввели неверную цифру, повторите попытку: '))
    return mark

def check_win():
    wins_comb =[(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
    (2, 5, 8), (3, 6, 9), (2, 5, 9), (3, 5, 7)]
    for i in wins_comb:
        if board[i[0] - 1] == board[i[1] - 1] == board[i[2] - 1]:
            return True
        

draw_board()
counter = 1
player = 'X'
while True:
    if player == 'X':
        move_x = input_mark()
        board[move_x - 1] = 'X'
        draw_board()
        if counter > 4: 
            check_win()
            if check_win():
                print(f'Игра окончена победил "{player}"')
                break
        player = 'O'
        counter += 1
    else:
        if counter > 8:
            print('Игра окончена: ничья')
            break
        move_o = input_mark()
        board[move_o - 1] = 'O'
        draw_board()
        if counter > 5: 
            if check_win():
                print(f'Игра окончена победил "{player}"')
                break
        player = 'X'
        counter += 1

    
