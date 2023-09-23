# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

from sys import argv


def _leap_year(year: int):

    if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return True


def check_date():
    date = input('Введите дату в формате DD.MM.YYYY: ')
    day, month, year = map(int, date.split('.'))

    case_1 = month in [1, 3, 5, 7, 8, 10, 12] and day in range(1, 32)
    case_2 = month in [4, 6, 9, 11] and day in range(1, 31)
    case_3 = _leap_year(year) and month == 2 and day in range(1, 30)
    case_4 = not(_leap_year(year)) and month == 2 and day in range(1, 29)

    if year in range(1, 10000):
        if case_1 or case_2 or case_3 or case_4:
            return True
        else:
            return False
    else:
        return False


# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.


def check_cmd_date():
    day, month, year = map(int, argv[1].split('.'))

    case_1 = month in [1, 3, 5, 7, 8, 10, 12] and day in range(1, 32)
    case_2 = month in [4, 6, 9, 11] and day in range(1, 31)
    case_3 = _leap_year(year) and month == 2 and day in range(1, 30)
    case_4 = not (_leap_year(year)) and month == 2 and day in range(1, 29)

    if year in range(1, 10000):
        if case_1 or case_2 or case_3 or case_4:
            return True
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    # print(_leap_year(2100))
    # print(check_date())
    print(check_cmd_date())