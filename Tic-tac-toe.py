"""
Игра крестики-нолики.
Размер игрового поля 3х3.
Игроки делают свой ход через консольный ввод. Игрок 1 играет крестиками, Игрок 2 - ноликами.
На каждом ходу игроки вводят пару чисел. Первое число соотвуствует номеру строки, второе - номеру столбца.
Нумерация столбцов и строк с 1 до 3.
"""
print ("Добро пожаловать в новую игру!")
# список переменных: каждая переменная может быть крестиком, ноликом или прочерком. В первоначальном положении
# все переменные равны "-"
def field_print():
    for field in play_field:
        print(' '.join(field))
def player_num(turn):
    if turn%2 == 0:
        return "нолики"
    else:
        return "крестики"
def correct_move(index):
    row = int(index[0])
    col = int(index[1])
    if row and col in range (1,4):
        return True
    else:
        print ("Номера строк и столбцов должны быть в диапазоне от 1 до 3!")

def move_check(index):
    while (not correct_move(index)) or (index in moves_log):
        if index in moves_log:
            print("Такой ход уже был!")
            index = input('Введите номер строки и номер столбца без пробела и нажмите Enter')

        else:
            index = input('Введите номер строки и номер столбца без пробела и нажмите Enter')

    moves_log.append(index)
    return index


def make_a_move (index):
    row = int(index[0])
    col = int(index[1])
    if player_num(turn) == "нолики":
        play_field[row][col] = "0"
    else:
        play_field[row][col] = "X"
def win_check(index):
    row = int(index[0])
    col = int(index[1])
    if (play_field[row][1]==play_field[row][2]==play_field[row][3]!="-" or
    play_field[1][col]==play_field[2][col]==play_field[3][col]!="-" or
    play_field[1][1]==play_field[2][2]==play_field[3][3]!="-" or
    play_field[1][3]==play_field[2][2]==play_field[3][1]!="-"):
        return True


play_field = [[" ",'1','2','3'],
         ['1','-','-','-'],
         ['2','-','-','-'],
         ['3','-','-','-']]
moves_log=[]

for turn in range (1,10):
    player = player_num (turn) # определяем, чей сейчас ход
    print("Ходят ",player) # выводим информацию на экран
    field_print() # распечатываем игровое поле
    index =  input ('Введите номер строки и номер столбца без пробела и нажмите Enter') # игрок делает ход,
    # столбец и строка записываются в переменную
    index = move_check(index) # проверяем, что такого хода еще не было
    make_a_move(index) # Делаем ход
    if win_check(index):
        field_print()
        print("Победили ",player," игра окончена!")
        break



