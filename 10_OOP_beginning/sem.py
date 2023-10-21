# Задание №1
# Создайте класс окружность. Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def len(self):
        return 2 * self.radius * math.pi

    def area(self):
        return self.radius**2 * math.pi


c = Circle(5)
print(c.len(), c.area())


# Задание №2
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.


class Rectangle:

    def __init__(self, length, width=None):
        self.length = length
        if width is None:
            self.width = length
        else:
            self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width


r = Rectangle(5, 10)
r1 = Rectangle(5)

print(r.perimeter(), r.area())
print(r1.perimeter(), r1.area())


# Задание №3
# Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.


class Person:
    def __init__(self, first_name, second_name, age):
        self.first_name = first_name
        self.second_name = second_name
        self.__age = age

    def full_name(self):
        return f'{self.first_name} {self.second_name}'

    def birthday(self):
        self.__age += 1

    def get_age(self):
        return self.__age


p1 = Person('John', 'Smith', 20)
print(p1.full_name(), p1.get_age())

p1.__age = 30
print(p1.full_name(), p1.get_age())

p1.birthday()
print(p1.full_name(), p1.get_age())

#
# Задание №4
# Создайте класс Сотрудник. Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь


class Employee(Person):
    def __init__(self, id_num, *args, **kwargs):
        self.id = id_num
        self.access_level = sum(int(i) for i in str(id_num)) % 7
        super().__init__(*args, **kwargs)


e1 = Employee(123457, 'George', 'Duck', 10)
print(e1.full_name())
e1.birthday()
print(e1.full_name(), e1.get_age(), e1.id, e1.access_level)


# Задание №5
# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
#
# Задание №6
# Доработайте задачу 5. Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него. Убедитесь, что в созданные ранее классы внесены правки.


class Animal:
    def __init__(self, name, sound, age):
        self.name = name
        self.sound = sound
        self.age = age

    def get_attr(self):
        return f'{self.name}, {self.sound}, {self.age}'


class Fish(Animal):
    def __init__(self, fins_num, name, age, sound=None):
        self.fins_num = fins_num
        super().__init__(name, sound, age)

    def get_attr(self):
        return f'{super().get_attr()} {self.fins_num}'


class Bird(Animal):
    def __init__(self, wings_color, *args, **kwargs):
        self.wings_color = wings_color
        super().__init__(*args, **kwargs)

    def get_wings_color(self):
        print(self.wings_color)


class Insects(Animal):
    def __init__(self, paws_num, *args, **kwargs):
        self.paws_num = paws_num
        super().__init__(*args, **kwargs)

    def get_paws_num(self):
        print(self.paws_num)


f = Fish(4, 'fish', 100)
print(f.get_attr())
