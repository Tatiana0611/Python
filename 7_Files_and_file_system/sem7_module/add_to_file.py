# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform


def add_to_file(num_str, file_name):
    with open(f'../{file_name}.txt', 'a', encoding='utf-8') as f:
        for _ in range(num_str):
            print(f'{randint(-1000, 1000)}|{uniform(-1000, 1000):.2f}', file=f)


if __name__ == '__main__':
    add_to_file(10, 'file_1')