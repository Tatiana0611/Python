# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.

from creating_files import create_files


def diff_extensions(extensions: list, num_extensions: list):
    for i, item in enumerate(extensions):
        create_files(extension=item, num=num_extensions[i])


if __name__ == '__main__':
    diff_extensions(['txt', 'md'], [2, 3])

