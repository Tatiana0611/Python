# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

"""Game with users.

The user has to guess the number in a certain number of attempts."""

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
ATTEMPTS = 5


def game(lower_limit, upper_limit, attempts):
    num_rand = randint(lower_limit, upper_limit)
    print('Рандомное число', num_rand)
    count = 1
    while count <= attempts:
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
    print(game(LOWER_LIMIT, UPPER_LIMIT, ATTEMPTS))