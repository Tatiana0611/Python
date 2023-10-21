# Создайте базовый класс Animal, который имеет атрибут name, представляющий имя животного.
# Создайте классы Bird, Fish и Mammal, которые наследуются от базового класса Animal
# и добавляют дополнительные атрибуты и методы:
# Bird имеет атрибут wingspan (размах крыльев) и метод wing_length, который возвращает длину крыла птицы.
# Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth, который возвращает категорию
# глубины рыбы (мелководная, средневодная, глубоководная) в зависимости от значения max_depth.
# Если максимальная глубина обитания рыбы (max_depth) меньше 10, то она относится к категории "Мелководная рыба".
# Если максимальная глубина обитания рыбы больше 100, то она относится к категории "Глубоководная рыба".
# В противном случае, рыба относится к категории "Средневодная рыба".
# Mammal имеет атрибут weight (вес) и метод category, который возвращает категорию млекопитающего
# (Малявка, Обычный, Гигант) в зависимости от веса. Если вес объекта меньше 1, то он относится к категории "Малявка".
# Если вес объекта больше 200, то он относится к категории "Гигант".
# В противном случае, объект относится к категории "Обычный".
# Создайте класс-фабрику AnimalFactory, который будет создавать экземпляры животных разных типов на
# основе переданного типа и параметров. Класс-фабрика должен иметь метод create_animal,
# который принимает следующие аргументы:
# animal_type (строка) - тип животного (один из: 'Bird', 'Fish', 'Mammal').
# *args - переменное количество аргументов, представляющих параметры для конкретного типа животного.
# Количество и типы аргументов могут различаться в зависимости от типа животного.
# Метод create_animal должен создавать и возвращать экземпляр животного заданного типа с переданными параметрами.


class Animal:
    def __init__(self, name):
        self.name = name


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan / 2


class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 10:
            return 'Мелководная рыба'
        elif self.max_depth > 100:
            return 'Глубоководная рыба'
        else:
            return 'Средневодная рыба'


class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight

    def category(self):
        if self.weight < 1:
            return 'Малявка'
        elif self.weight > 200:
            return 'Гигант'
        else:
            return 'Обычный'


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args):
        if animal_type == "Bird" and len(args) >= 2:
            return Bird(*args)
        elif animal_type == "Fish" and len(args) >= 2:
            return Fish(*args)
        elif animal_type == "Mammal" and len(args) >= 2:
            return Mammal(*args)
        else:
            raise ValueError("Недопустимый тип животного")


# Создание экземпляров животных
animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)

# Вывод результатов
print(animal1.wing_length())
print(animal2.depth())
print(animal3.category())


# На вход программе подаются два списка, каждый из которых содержит 10 различных целых чисел.
# Первый список ваш лотерейный билет.
# Второй список содержит список чисел, которые выпали в лотерею.
# Вам необходимо определить и вывести количество совпадающих чисел в этих двух списках.
# Напишите класс LotteryGame, который будет иметь метод compare_lists, который будет сравнивать числа
# из вашего билета из list1 со списком выпавших чисел list2
# Если совпадающих чисел нет, то выведите на экран: Совпадающих чисел нет.

class LotteryGame:

    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def compare_lists(self):
        lst = []

        for i in self.list1:
            if i in self.list2:
                lst.append(i)

        if lst:
            print(f'Совпадающие числа: {lst}\nКоличество совпадающих чисел: {len(lst)}')
        else:
            print('Совпадающих чисел нет.')

        return lst


list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

game = LotteryGame(list1, list2)
matching_numbers = game.compare_lists()
