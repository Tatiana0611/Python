# Задание №3
# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

import json
import csv


def csv_from_json():
    with (
        open('../task_2.json', 'r', encoding='utf-8') as f_read,
        open('../task_3.csv', 'w', newline='', encoding='utf-8') as f_write
    ):

        json_dict = json.load(f_read)

        csv_write = csv.DictWriter(f_write, fieldnames=['access_level', 'id', 'name'])

        csv_write.writeheader()

        dict_row = {}

        for key, value in json_dict.items():
            for k, v in value.items():
                dict_row['access_level'] = key
                dict_row['id'] = k
                dict_row['name'] = v
                csv_write.writerow(dict_row)


if __name__ == '__main__':
    csv_from_json()

