# Задание №7
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку


import pickle


def pickle_from_csv():
    with open(f'../task_6.csv', 'r', encoding='utf-8', newline='') as f_read:
        new_list = []
        next(f_read)

        for line in f_read:
            access_level, id_num, name, hash_func = line.split(',')
            new_list.append({'access_level': access_level,
                             'id': id_num,
                             'name': name[:-2],
                             'hash': hash_func[:-2]
                             })
        print(new_list)

        res = pickle.dumps(new_list, protocol=pickle.DEFAULT_PROTOCOL)
        print(f'{res = }')


if __name__ == "__main__":
    pickle_from_csv()
