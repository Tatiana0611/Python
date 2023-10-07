# Задание №4
# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.


import json


def json_from_csv(f_csv: str, f_json: str):
    with (
        open(f'../{f_csv}', 'r', encoding='utf-8', newline='') as f_read,
        open(f'../{f_json}', 'a', encoding='utf-8') as f_write,
    ):
        json_list = []

        next(f_read)

        for line in f_read:
            access_level, id_num, name = line.split(',')

            json_list.append({'access_level': access_level,
                              'id': id_num.zfill(10),
                              'name': name[:-2].capitalize(),
                              'hash': hash(name[:-2] + id_num)
                              })
        json.dump(json_list, f_write, indent=2)


if __name__ == '__main__':
    json_from_csv('task_3.csv', 'task_4.json')