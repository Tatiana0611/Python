# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

from random import randint


def find_fighting_queens(coord_1, coord_2, coord_3, coord_4, coord_5, coord_6, coord_7, coord_8):
    queens_coord = [coord_1, coord_2, coord_3, coord_4, coord_5, coord_6, coord_7, coord_8]

    horizontal = [queens_coord[i][0] for i in range(len(queens_coord))]
    vertical = [queens_coord[i][1] for i in range(len(queens_coord))]
    ascending_diagonal = [i[0] + i[1] for i in queens_coord]
    descending_diagonal = [i[0] - i[1] for i in queens_coord]
    # print(queens_coord, horizontal, vertical, ascending_diagonal, descending_diagonal, sep='\n')

    condition_1 = len(set(horizontal)) == len(queens_coord)  # ферзи не встречаются на одной горизонтали
    condition_2 = len(set(vertical)) == len(queens_coord)  # ферзи не встречаются на одной вертикали
    condition_3 = len(set(ascending_diagonal)) == len(ascending_diagonal)  # ферзи не встречаются на одной восходящей диагонали
    condition_4 = len(set(descending_diagonal)) == len(descending_diagonal) # ферзи не встречаются на одной нисходящей диагонали

    if condition_1 and condition_2 and condition_3 and condition_4:
        return True
    else:
        return False


# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей
# в задаче выше. Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.


def successful_placement():
    count = 0
    while count < 4:
        # coordinates_list = [[randint(1, 8), randint(1, 8)] for _ in range(8)]
        coordinates_list = [[1, randint(1, 8)], [2, randint(1, 8)], [3, randint(1, 8)], [4, randint(1, 8)],
                            [5, randint(1, 8)], [6, randint(1, 8)], [7, randint(1, 8)], [8, randint(1, 8)]]
        if find_fighting_queens(*coordinates_list):
            print(coordinates_list)
            count += 1
        else:
            continue


if __name__ == '__main__':
    print(find_fighting_queens([6, 1], [2, 2], [7, 3], [1, 4],
                               [4, 5], [8, 6], [5, 7], [3, 8]))

    print(find_fighting_queens([1, 1], [2, 2], [3, 3], [4, 4],
                               [5, 5], [6, 6], [7, 7], [8, 8]))

    successful_placement()

