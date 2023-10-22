# Задание №1
# Создайте класс Моя Строка, где будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания (time.time)

import time


class MyStr(str):
    """Class for extension class str(object)"""

    def __new__(cls, value, name):
        """Added parameters: name, value, time"""
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time = time.ctime()
        return instance


ex = MyStr(name='john', value='Hello')
print(f'{ex.name = }, {ex.time = }')
print(ex.upper())


# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку. При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков архивов list-архивы также являются свойствами экземпляра


class Archive:
    list_num = []
    list_str = []

    def __init__(self, number, string):
        self.number = number
        self.string = string

        Archive.list_num.append(number)
        Archive.list_str.append(string)

# Задание №4
# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста и для пользователя.

    def __str__(self):
        return f'Экземпляр класса Archive, имеющий число {self.number} и строку {self.string}'

    def __repr__(self):
        return f'Archive({self.number}, {self.string})'


a = Archive(4, 'dfd')
b = Archive(6, 'dfd')
print(a)
print(f'{a}')
print(repr(a))
print(f'{a=}')
print(b.list_num)
c = Archive(8, 'dfd')
print(a.number)
print(a.string)
print(a.list_num)
print(Archive.list_num)


# Задание №5
# Дорабатываем класс прямоугольник из прошлого семинара. Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину. При вычитании не допускайте отрицательных значений.

# Задание №6
# Доработайте прошлую задачу. Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения


class Rectangle:
    def __init__(self, name, length, width=None):
        self.name = name
        self.length = length
        if width is None:
            self.width = length
        else:
            self.width = width

    def perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter

    def area(self):
        area = self.length * self.width
        return area

    def __str__(self):
        return f'Экземпляр класса Rectangle с именем {self.name} и сторонами {self.length} и {self.width}'

    def __add__(self, other):
        name = f'{self.name}{other.name}'
        p = self.perimeter() + other.perimeter()
        lenght = self.length
        width = int(p / 2 - lenght)
        return Rectangle(name, lenght, width)

    def __sub__(self, other):
        if self.perimeter() > other.perimeter():
            name = f'{self.name}{other.name}'
            p = self.perimeter() - other.perimeter()
            lenght = self.length
            width = int(p / 2 - lenght)
            return Rectangle(name, lenght, width)
        else:
            raise ValueError(f'{self.name} меньше {other.name}')

    def __eq__(self, other):
        return self.area() == other.area()
    #
    # def __ne__(self, other):
    #     return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __le__(self, other):
        return self.area() <= other.area()


r = Rectangle('rec1', 2, 6)
r1 = Rectangle('rec2', 3, 4)

print(r.perimeter(), r.area())
print(r1.perimeter(), r1.area())
print(r+r1)
print(r-r1)
print(r>r1)
print(r<r1)
print(r>=r1)
print(r<=r1)
print(r!=r1) # срабатывает not __eq__
print(r==r1)