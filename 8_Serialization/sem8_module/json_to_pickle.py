# Задание №5
# Напишите функцию, которая ищет json файлы в указанной
# директории и сохраняет их содержимое в виде одноимённых pickle файлов.

import os
import json
import pickle


def pickle_from_json():
    os.chdir('..')

    for i in os.listdir():
        if i.split('.')[-1] == 'json':

            with open(f'{i}', 'r', encoding='utf-8') as f_read:
                json_dict = json.load(f_read)

            with open(f'{i.split(".")[0]}.pickle', 'wb') as f_write:
                pickle.dump(json_dict, f_write)


if __name__ == '__main__':
    pickle_from_json()