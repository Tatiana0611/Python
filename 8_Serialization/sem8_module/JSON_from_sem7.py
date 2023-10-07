# Задание №1
# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
# текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее
# файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.


import json


def json_from_txt(file_path: str):

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_dict = {}

    for i in lines:
        key, value = i.split(' ')[0].capitalize(), float(i.split(' ')[1][:-1])
        new_dict[key] = value

    with open('../task_1.json', 'w', encoding='utf-8') as f_j:
        json.dump(new_dict, f_j, indent=2, sort_keys=True)


if __name__ == '__main__':
    json_from_txt('../../7_Files_and_file_system/file_3.txt')