# Задание №1
# Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

from random import randint as rnd


def param():
    result = ''

    num = int(input('Enter desired number in range [1, 100]: '))
    if num not in range(1, 101):
        num = rnd(1, 100)
        print('The entered desired number is out of the range. Desired number =', num)

    count = int(input('Enter number of attempts in range [1, 10]: '))
    if count not in range(1, 11):
        count = rnd(1, 10)
        print('The entered number of attempts is out of the range. Number of attempts =', count)

    def guess():
        nonlocal result
        for _ in range(count):
            num_check = int(input('Enter a number '))
            if num_check == num:
                result = 'You guessed'
                break
            else:
                result = "You didn't guess"
        return result

    return guess


number = param()

if __name__ == '__main__':
    print(number())
