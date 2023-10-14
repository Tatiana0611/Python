# Задание №5
# Объедините функции из прошлых задач. Функцию угадайку задекорируйте:
# ○ декораторами для сохранения параметров,
# ○ декоратором контроля значений и
# ○ декоратором для многократного запуска.
# Выберите верный порядок декораторов.

from random import randint as rnd
import json
from functools import wraps


def counter(numb: int = 1):
    def deco(func):
        @wraps(func)
        def wrapper(*args):
            for _ in range(numb):

                num, count = args

                if num not in range(1, 101):
                    num = rnd(1, 100)
                    print('The entered desired number is out of the range. Desired number =', num)

                if count not in range(1, 11):
                    count = rnd(1, 10)
                    print('The entered number of attempts is out of the range. Number of attempts =', count)

                new_dct = {'number': num, 'attempt': count, 'result': func(num, count)}

                with open('../guess_play.json', 'r', encoding='utf-8') as f_read:
                    dct = json.load(f_read)

                dct[max(map(int, dct.keys()))+1] = new_dct

                with open('../guess_play.json', 'w', encoding='utf-8') as f_write:
                    json.dump(dct, f_write, indent=2)

            return dct

        return wrapper

    return deco


@counter(3)
def guess(num, count):
    """Number guessing game"""
    attempt_dict = {}
    for _ in range(count):
        num_check = int(input('Enter a number '))
        if num_check == num:
            result = 'You guessed'
        else:
            result = "You didn't guess"
        attempt_dict.update({num_check: result})
    return attempt_dict


if __name__ == '__main__':
    num1 = int(input('Enter desired number in range [1, 100]: '))
    count1 = int(input('Enter number of attempts in range [1, 10]: '))
    print(guess(num1, count1))
    help(guess)