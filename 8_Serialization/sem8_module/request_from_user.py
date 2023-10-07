# Задание №2
# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо от уровня доступа.
# При перезапуске функции уже записанные в файл данные должны сохраняться.


import json


def add_to_json():
    while True:
        with open('../task_2.json', 'r', encoding='utf-8') as f_j:
            access_level_dict = json.load(f_j)

        name, id_num, access_level = input().split(' ')

        if int(access_level) not in range(1, 8):
            continue

        id_num_list = []
        for value in access_level_dict.values():
            for key in value.keys():
                id_num_list.append(key)

        if id_num in id_num_list:
            continue

        if access_level not in access_level_dict.keys():
            access_level_dict[access_level] = {id_num: name}
        else:
            access_level_dict[access_level].update({id_num: name})

        with open('../task_2.json', 'w') as f_j:
            json.dump(access_level_dict, f_j, indent=2, sort_keys=True)


if __name__ == '__main__':
    add_to_json()