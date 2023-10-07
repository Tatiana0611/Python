# Задание №6
# Напишите функцию, которая преобразует pickle файл
# хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков
# столбца из переданного файла.

import pickle
import csv


def csv_from_pickle():
    with (
        open('../task_4.pickle', 'rb') as f_read,
        open('../task_6.csv', 'w', newline='', encoding='utf-8') as f_write
    ):
        pickle_dict = pickle.load(f_read)
        keys = [i for i in pickle_dict[0].keys()]

        writer = csv.DictWriter(f_write, fieldnames=keys)
        writer.writeheader()
        writer.writerows(pickle_dict)


if __name__ == '__main__':
    csv_from_pickle()