# Задание №2
# Дорабатываем задачу 1. Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами из диапазонов.

from random import randint as rnd


def main(func):
    def wrapper(*args):
        num, count = args
        if num not in range(1, 101):
            num = rnd(1, 100)
            print('The entered desired number is out of the range. Desired number =', num)

        if count not in range(1, 11):
            count = rnd(1, 10)
            print('The entered number of attempts is out of the range. Number of attempts =', count)
        return func(num, count)

    return wrapper


@main
def guess(num, count):
    result = ''
    for _ in range(count):
        num_check = int(input('Enter a number '))
        if num_check == num:
            result = 'You guessed'
            break
        else:
            result = "You didn't guess"
    return result


if __name__ == '__main__':
    num1 = int(input('Enter desired number in range [1, 100]: '))
    count1 = int(input('Enter number of attempts in range [1, 10]: '))
    print(guess(num1, count1))
