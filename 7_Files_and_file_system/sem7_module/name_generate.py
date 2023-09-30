# Напишите функцию, которая генерирует псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы, состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

import string
from random import choice


def name_gen():

    def new_name():
        new_name = ''
        for _ in range(choice(range(4, 8))):
            new_name += choice(string.ascii_lowercase)
        return new_name

    name = new_name()

    for i in name:
        if i in 'aeiou':
            with open('../file_2.txt', 'a', encoding='utf-8') as f:
                print(name.capitalize(), file=f)
            break
        else:
            new_name()


if __name__ == '__main__':
    name_gen()