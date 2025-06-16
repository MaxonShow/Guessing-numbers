from random import *

def is_valid_border(right_border):
    if right_border.isdigit() and int(right_border) > 1:
        return True
    else:
        return False

def is_valid(number_str, right_border):
    if number_str.isdigit() and 1 <= int(number_str) <= int(right_border):
        return True
    else:
        return False

def get_random_number(right_border):
    return randrange(1, right_border + 1)

def input_num(right_border):
    while True:
        str_num = input(f'Введите число от 1 до {right_border}: ')
        if is_valid(str_num, right_border):
            return int(str_num)
        else:
            print(f'А может быть все-таки введем целое число от 1 до {right_border}?')

def continue_game():
    answer = input('Хотите продолжить ("д"/"н")?\n')
    while True:
        if answer not in ('д', 'н'):
            answer = input('Введите "д" или "н":\n')
        elif answer in ('н'):
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            return False
        else:
            return True

def play_game():
    print('Добро пожаловать в числовую угадайку')
    while True:
        while True:
            right_border = input('Введите правую границу диапазона чисел: ')
            if is_valid_border(right_border):
                right_border = int(right_border)
                break
            else:
                print('Правая граница должна быть целым числом больше 1!')
        random_num = get_random_number(right_border)
        attempts = 1
        while True:
            user_num = input_num(right_border)
            if user_num == random_num:
                print('Вы угадали, поздравляем!')
                print(f'Использовано попыток: {attempts}')
                if not continue_game():
                    return
                else:
                    break
            elif user_num < random_num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            else:
                print('Ваше число больше загаданного, попробуйте еще разок')
            attempts += 1


play_game()