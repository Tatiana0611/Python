# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.


import os
import json
import csv
import pickle


def dir_walk(directory: str):
    list_to_write = []

    for dir_path, dir_name, file_name in os.walk(directory):
        for i in file_name:
            list_to_write.append({
                'object_type': 'file',
                'name': i,
                'directory': dir_path.split('\\')[-1],
                'size': f'{os.path.getsize(os.path.join(dir_path, i))} bytes'
            })

        for i in dir_name:
            os.chdir(os.path.join(dir_path, i))
            size = sum(os.path.getsize(file) for file in os.listdir() if os.path.isfile(file))
            list_to_write.append({
                'object_type': 'directory',
                'name': i,
                'directory': dir_path.split('\\')[-1],
                'size': f'{size} bytes'
            })

    with (
        open('../homework.json', 'w', encoding='utf-8') as f_json,
        open('../homework.pickle', 'wb') as f_pickle,
        open('../homework.csv', 'w', newline='', encoding='utf-8') as f_csv,
    ):
        json.dump(list_to_write, f_json, indent=2)

        pickle.dump(list_to_write, f_pickle)

        keys = [i for i in list_to_write[0].keys()]
        writer = csv.DictWriter(f_csv, fieldnames=keys)
        writer.writeheader()
        writer.writerows(list_to_write)


if __name__ == '__main__':
    dir_walk(r'C:\Users\tatia\Documents\gb\2_year\Python\8_Serialization')
