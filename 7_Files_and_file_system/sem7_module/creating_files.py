# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.

import string
from random import choices, randint


def create_files(extension: str, min_name_length=6, max_name_length=30, min_size=256, max_size=4096, num=42):
    for _ in range(num):
        name_length = randint(min_name_length, max_name_length)
        size = randint(min_size, max_size)

        name = ''.join(choices(string.ascii_letters, k=name_length))
        filling = ''.join(choices(string.ascii_letters, k=size))

        with open(f'../{name}.{extension}', 'a', encoding='utf-8') as f:
            print(filling, file=f)
            # print(name, name_length, size)


if __name__ == '__main__':
    create_files('htm', 3, 5, 4, 10, 2)