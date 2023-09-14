# Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

import os.path


# Первый вариант
def path_func(new_str):
    a = new_str[:new_str.rfind('\\')]
    b, c = new_str.split('\\')[-1].split('.')
    return a, b, c


# Второй вариант
def path_func_os(new_str):
    a, b = os.path.split(my_str)
    b, c = os.path.splitext(b)
    return a, b, c


my_str = r'C:\Users\Tatiana\Documents\gb\Python\Iterators_and_Generators\homework.py'

print(path_func(my_str))
print(path_func_os(my_str))


# Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии

names = ['Ann', 'Boris', 'John', 'Mike']
salaries = [10_000, 15_000, 20_000, 18_000]
awards = ['10.15%', '9.85%', '11.35%', '9.25%']

dict_salary = {names: salaries * float(awards[:-1]) / 100
               for names, salaries, awards in zip(names, salaries, awards)}

print(dict_salary)


# Создайте функцию генератор чисел Фибоначчи


def fib_sequence(n):
    fib_1, fib_2 = 0, 1
    print(fib_1, fib_2, sep='\n')
    for _ in range(2, n):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        yield fib_2


N = 10

for i in fib_sequence(N):
    print(i)
