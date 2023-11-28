# В организации есть два типа людей: сотрудники и обычные люди. Каждый человек (и сотрудник, и обычный) имеет следующие атрибуты:
# Фамилия (строка, не пустая) Имя (строка, не пустая) Отчество (строка, не пустая) Возраст (целое положительное число)
# Сотрудники имеют также уникальный идентификационный номер (ID), который должен быть шестизначным положительным целым числом.
# Ваша задача:
# Создать класс Person, который будет иметь атрибуты и методы для управления данными о людях (Фамилия, Имя, Отчество, Возраст).
# Класс должен проверять валидность входных данных и генерировать исключения InvalidNameError и InvalidAgeError, если данные неверные.
# Создать класс Employee, который будет наследовать класс Person и добавлять уникальный идентификационный номер (ID).
# Класс Employee также должен проверять валидность ID и генерировать исключение InvalidIdError, если ID неверный.
# Добавить метод birthday в класс Person, который будет увеличивать возраст человека на 1 год.
# Добавить метод get_level в класс Employee, который будет возвращать уровень сотрудника на основе суммы цифр в его ID (по остатку от деления на 7).
# Создать несколько объектов класса Person и Employee с разными данными и проверить, что исключения работают корректно при передаче неверных данных.


class InvalidNameError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class InvalidIdError(Exception):
    pass

class Person:
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        self._validate_name(last_name, "Фамилия")
        self._validate_name(first_name, "Имя")
        self._validate_name(patronymic, "Отчество")
        self._validate_age(age)
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.age = age

    def _validate_name(self, name: str, field_name: str):
        if not isinstance(name, str) or name.strip() == "":
            raise InvalidNameError(f'Invalid name: {name}. Name should be a non-empty string.')

    def _validate_age(self, age: int):
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(f'Invalid age: {age}. Age should be a positive integer.')

    def birthday(self):
        self.age += 1

    def get_age(self):
        return self.age

class Employee(Person):
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, employee_id: int):
        super().__init__(last_name, first_name, patronymic, age)
        self._validate_id(employee_id)
        self.employee_id = employee_id

    def _validate_id(self, employee_id: int):
        if not isinstance(employee_id, int) or employee_id <= 0 or employee_id > 999999:
            raise InvalidIdError("ID должен быть шестизначным положительным целым числом.")

    def get_level(self):
        return sum(int(digit) for digit in str(self.employee_id)) % 7


# Альтернативное решение!
class InvalidNameError(ValueError):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Invalid name: {self.name}. Name should be a non-empty string.'


class InvalidAgeError(ValueError):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f'Invalid age: {self.age}. Age should be a positive integer.'


class InvalidIdError(ValueError):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f'Invalid id: {self.id}. Id should be a 6-digit positive integer between 100000 and 999999.'


class Person:
    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int):
        if not isinstance(last_name, str) or len(last_name.strip()) == 0:
            raise InvalidNameError(last_name)
        if not isinstance(first_name, str) or len(first_name.strip()) == 0:
            raise InvalidNameError(first_name)
        if not isinstance(patronymic, str) or len(patronymic.strip()) == 0:
            raise InvalidNameError(patronymic)
        if not isinstance(age, int) or age <= 0:
            raise InvalidAgeError(age)

        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):
    MAX_LEVEL = 7

    def __init__(self, last_name: str, first_name: str, patronymic: str, age: int, id: int):
        super().__init__(last_name, first_name, patronymic, age)
        if not isinstance(id, int) or id < 100_000 or id > 999_999:
            raise InvalidIdError(id)

        self.id = id

    def get_level(self):
        s = sum(num for num in str(self.id))
        return s % self.MAX_LEVEL




if __name__ == "__main__":
    person = Person("", "John", "Doe", 30)

    person = Person("Alice", "Smith", "Johnson", -5)

    person = Person("Alice", "Smith", "Johnson", 25)
    print(person.get_age())