# Задание №1
# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл. Например отлавливаем ошибку деления на ноль.

# import logging
#
# logging.basicConfig(filename='div_by_zero.log', encoding='utf-8', level=logging.ERROR)
#
#
# def div_by_zero(num_1, num_2):
#     try:
#         result = num_1 / num_2
#     except ZeroDivisionError as e:
#         logging.error(f'{e}')
#         result = None
#     return result
#
#
# div_by_zero(5, 0)


# Задание №2
# На семинаре про декораторы был создан логирующий декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте модуль logging.

# import json
# import logging
#
#
# def main(func):
#     def wrapper(*args, **kwargs):
#         with open(f'{func.__name__}.json', 'r', encoding='utf-8') as f:
#             json_dict = json.load(f)
#
#         new_dict = {'args': list(args)}
#
#         for i, item in kwargs.items():
#             new_dict[i] = item
#
#         new_dict['result'] = func(*args, **kwargs)
#
#         json_dict[max(map(int, json_dict.keys()))+1] = new_dict
#
#         logging.info(json_dict)
#
#         return json_dict
#     return wrapper
#
#
# @main
# def profit(*args, **kwargs):
#     n_dict = {'mean': round(sum(args) / len(args), 2)}
#     for i, item in kwargs.items():
#         n_dict.update({i: item})
#     return n_dict
#
#
# if __name__ == '__main__':
#     logging.basicConfig(filename='task_2.log', encoding='utf-8', level=logging.INFO)
#     profit(1, 2, k=6, l=6)


# Задание №3
# Доработаем задачу 2. Сохраняйте в лог файл раздельно:
# ○ уровень логирования, ○ дату события, ○ имя функции (не декоратора),
# ○ аргументы вызова, ○ результат.

# import json
# import logging
#
#
# def main(func):
#     def wrapper(*args, **kwargs):
#         with open(f'{func.__name__}.json', 'r', encoding='utf-8') as f:
#             json_dict = json.load(f)
#
#         new_dict = {'args': list(args)}
#
#         for i, item in kwargs.items():
#             new_dict[i] = item
#
#         new_dict['result'] = func(*args, **kwargs)
#
#         json_dict[max(map(int, json_dict.keys()))+1] = new_dict
#
#         logger.info(json_dict)
#
#         return json_dict
#     return wrapper
#
#
# @main
# def profit(*args, **kwargs):
#     n_dict = {'mean': round(sum(args) / len(args), 2)}
#     for i, item in kwargs.items():
#         n_dict.update({i: item})
#     return n_dict
#
#
# if __name__ == '__main__':
#     FORMAT = '{levelname:<8} - {asctime} {funcName}(): {msg}'
#     logging.basicConfig(format=FORMAT, style='{', filename='task_3.log', encoding='utf-8', level=logging.INFO)
#     logger = logging.getLogger(__name__)
#     profit(1, 2, k=3, l=5)

