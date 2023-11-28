# Задание №1
# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или
# вещественное число.
# Обрабатывайте не числовые данные как исключения.

# def call(text: str = None) -> float:
#     while True:
#         try:
#             num = float(input('Enter number: '))
#             break
#         except ValueError as e:
#             print(f'Error {e}\nEnter a number')
#     return num


# Задание №2
# Создайте функцию аналог get для словаря. Помимо самого словаря функция принимает ключ и
# значение по умолчанию. При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение. Реализуйте работу через обработку исключений.


# def get_value(dictionary, key, value_default) -> str:
#     try:
#         return dictionary[key]
#     except KeyError as e:
#         print(f'Нет ключа {e}')
#         return value_default


# Задание №3
# Создайте класс с базовым исключением и дочерние классы исключения:
# ○ ошибка уровня,
# ○ ошибка доступа.


class MyEx(Exception):
    pass

class LevelEx(MyEx):
    def __init__(self, level, min_level):
        self.level = level
        self.min_level = min_level

    def __str__(self):
        return (f'Уровень недостаточный\nМинимальное значение уровня: {self.min_level}\n'
                f'Текущее значение: {self.level}')


class AccessEx(MyEx):
    def __init__(self, access, min_access):
        self.access = access
        self.min_access = min_access

    def __str__(self):
        return (f'Доступ запрещен\nРазрешенный доступ: {self.min_access}\n'
                f'Текущий доступ: {self.access}')



# class User:
#     MIN_LEVEL = 3
#     MIN_ACCESS = 10
#
#     def __init__(self, level, access):
#         if level > self.MIN_LEVEL:
#             self.level = level
#         else:
#             raise LevelEx(level, self.MIN_LEVEL)
#
#         if access < self.MIN_LEVEL:
#             self.access = self.MIN_ACCESS
#         else:
#             raise AccessEx(access, self.MIN_ACCESS)


# Задание №4
# Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.

import json


class Users:
    def __init__(self, name, id_num, access_level):
        self.name = name
        self.id_num = id_num
        self.access_level = access_level

    def __repr__(self):
        return f'Users({self.name}, {self.id_num}, {self.access_level})'


def generate_set_users(file):
    users = []

    with open(file, 'r', encoding='utf-8') as f:
        users_dict = json.load(f)
        for access_level, value in users_dict.items():
            for id_num, name in value.items():
                user = Users(name, id_num, access_level)
                users.append([user.name, user.id_num, user.access_level])

    return users

# Задание №5
# Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей. Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из множества пользователей.
# добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.


class Project:
    MIN_LEVEL = 3
    MIN_ACCESS = 10

    def __init__(self, file):
        self.users = self.generate_set_users(file)

    def generate_set_users(self, file):
        users_set = set()
        with open(file, 'r', encoding='utf-8') as f:
            users_dict = json.load(f)
            for access_level, value in users_dict.items():
                for id_num, name in value.items():
                    user = Users(name, id_num, access_level)
                    users_set.add(user)
        return users_set

    def login(self, new_name, new_id):
        new_user = Users(new_name, new_id, '')
        print(self.users)
        if new_user not in self.users:
            raise AccessEx(3, self.MIN_ACCESS) #не по условию задачи


if __name__ == "__main__":
    # number = call()
    # print(number)

    # d = {'one': 1, 'two': 2}
    # print(get_value(d, 'two', 'none'))

    # user = User(10, 5)

    # print(generate_set_users(r'C:\Users\tatia\Documents\gb\2_year\Python\8_Serialization\task_2.json'))

    users = Project(r'C:\Users\tatia\Documents\gb\2_year\Python\8_Serialization\task_2.json')
    # print(users.generate_set_users(r'C:\Users\tatia\Documents\gb\2_year\Python\8_Serialization\task_2.json'))
    users.login('dffd', 45)

