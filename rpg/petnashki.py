import random

Pleyer = 'X'
MOVES = {'w': -4,'s': 4,'a': -1,'d': 1,}


def create_field(): #создание поля
   
    field = list(range(1, 17))
    field[-1] = Pleyer
    random.shuffle(field)

    
    return field


def print_field(field): #отрисовка
   
    for i in range(0, 16, 4):
        print(field[i:i + 4])
    print('\n')


def is_game_finished(field): #услония завершения,если созданное поле == эталону
   
    ideal = list(range(1, 16))
    ideal.append(Pleyer)

    return ideal == field


def perform_move(field, key):           #я сломал свой мозг,ход игрока
  
    my_position = field.index(Pleyer)

    if key == 's' and my_position >= 12:
        raise IndexError('Cant move down')

    if key == 'd' and my_position % 4 == 3:
        raise IndexError('Cant move right')

    if key == 'w' and my_position < 4:
        raise IndexError('Cant move up')

    if key == 'a' and my_position % 4 == 0:
        raise IndexError('Cant move left')

    delta = MOVES[key]
    field[my_position], field[my_position + delta] = field[my_position + delta], field[my_position]
    return field


def handle_user_input(): #ввод игрока
  
    while True:
        user_move = input('Please, input your move: ')
        if user_move in MOVES.keys():
            return user_move


def main():     #сборка игры
  
    field = create_field()
  

    while not is_game_finished(field):
        try:
            print_field(field)
            move = handle_user_input()
            field = perform_move(field, move)
        except IndexError as e:
            print(e)

    print('Game is finished!!!')


if __name__ == '__main__':


    main()
