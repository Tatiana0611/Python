# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.


def riddle_guessing(riddle: str, answer_list: list, attempts: int):
    count = 1
    while count <= attempts:
        print(riddle,f'\nОтвет:')
        answer = input()
        if answer in answer_list:
            return count
        count += 1
    else:
        return 0


# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.


def riddles_keeping():
    attempts = 3
    riddles_dict = {'Riddle_1': ['a', 'b', 'c'],
                    'Riddle_2': ['d', 'e', 'f'],
                    'Riddle_3': ['g', 'h', 'i'],
                    'Riddle_4': ['j', 'k', 'l'],
                    }
    for key, value in riddles_dict.items():
        print('Номер попытки', riddle_guessing(key, value, attempts))


if __name__ == '__main__':
    riddles_keeping()