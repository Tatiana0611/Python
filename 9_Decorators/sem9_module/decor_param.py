# Задание №4
# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции.


import json


def count(num: int = 1):
    def deco(func):
        def wrapper(*args, **kwargs):

            for _ in range(num):

                with open(f'../{func.__name__}.json', 'r', encoding='utf-8') as f:
                    json_dict = json.load(f)

                new_dict = {'args': list(args)}

                for i, item in kwargs.items():
                    new_dict[i] = item

                new_dict['result'] = func(*args, **kwargs)

                json_dict[max(map(int, json_dict.keys()))+1] = new_dict

                with open(f'../{func.__name__}.json', 'w', encoding='utf-8') as f:
                    json.dump(json_dict, f, indent=4)

            return json_dict

        return wrapper

    return deco


@count(4)
def profit(*args, **kwargs):
    n_dict = {'mean': round(sum(args) / len(args), 2)}
    for i, item in kwargs.items():
        n_dict.update({i: item})
    return n_dict


if __name__ == '__main__':
    profit(1, 1, 1, 1, k=1)
