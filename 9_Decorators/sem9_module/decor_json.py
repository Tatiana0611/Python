# Задание №3
# Напишите декоратор, который сохраняет в json файл параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.
import json


def main(func):
    def wrapper(*args, **kwargs):
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


@main
def profit(*args, **kwargs):
    n_dict = {'mean': round(sum(args) / len(args), 2)}
    for i, item in kwargs.items():
        n_dict.update({i: item})
    return n_dict


if __name__ == '__main__':
    profit(3, 5, k=5, l=9)
