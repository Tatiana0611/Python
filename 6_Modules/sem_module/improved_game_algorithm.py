# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

"""Game with users.

The user has to guess the number in a certain number of attempts."""

from sys import argv
from random import randint


def game(lower_limit, upper_limit, attempts_quantity):
    num_rand = randint(lower_limit, upper_limit-1)
    print('Рандомное число', num_rand)
    count = 1
    while count <= attempts_quantity:
        num = int(input(f'Попытка {count}. Введите целое число от 0 до 1000: '))
        if num not in range(lower_limit, upper_limit):
            print('Введенное число вне заданного диапазона!')
        elif num > num_rand:
            print('Введенное число больше, чем загаданное!')
        elif num < num_rand:
            print('Введенное число меньше, чем загаданное!')
        else:
            return True
        count += 1
    else:
        return False


if __name__ == '__main__':
    print(game(*(int(i) for i in argv[1:4])))