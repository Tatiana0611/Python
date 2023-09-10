# Задание №7
# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.


def profitable_companies(data_dict):
    company_profits = []
    for value in data_dict.values():
        company_profits.append(sum(value))
    # print(company_profits)
    return all(map(lambda x: x > 0, company_profits))


data_dict = {'company A': [1, 2, 4, 5],
             'company B': [1, 2, 4, 5],
             'company C': [1, 2, 4, 5],
             'company D': [1, 2, 4, 5],
             'company I': [1, 2, -4, -5],
             }

print(profitable_companies(data_dict))


# Напишите функцию для транспонирования матрицы


def transpose_matrix(matrix):
    trans_matrix = [[None for i in range(len(matrix))] for j in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            trans_matrix[j][i] = matrix[i][j]
    return trans_matrix


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [7, 8, 9],
          ]

for i in transpose_matrix(matrix):
    print(i)


# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.


def hash_dict(**kwargs):
    new_dict = {}
    for key, value in kwargs.items():
        try:
            hash(value)
        except TypeError:
            new_dict[str(value)] = key
        else:
            new_dict[value] = key
    return new_dict


print(hash_dict(a=3, b='4', c=(5, 6), d=[7, 8]))


# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


MULTIPLE_NUM = 50
WEALTH_LIMIT = 5_000_000
WEALTH_TAX = 0.1
MIN_WITHDRAWAL_FEE = 30
MAX_WITHDRAWAL_FEE = 600
WITHDRAWAL_FEE = 0.015
COUNT_OPERATIONS = 3
COUNT_OPERATIONS_BONUS = 0.03


def main():
    balance = 0
    count_operations = 0


    def deposit():
        """Функция внесения наличных"""
        nonlocal count_operations
        nonlocal balance
        cash = int(input(f'Сумма пополнения должна быть кратна {MULTIPLE_NUM}. \nВведите значение: '))

        if balance > WEALTH_LIMIT:
            balance -= WEALTH_TAX * cash
            print(f'Вычтен налог на богатство {WEALTH_TAX * cash}.')

        if cash % MULTIPLE_NUM == 0:
            balance += cash
            count_operations += 1

            if count_operations % COUNT_OPERATIONS == 0:
                balance += COUNT_OPERATIONS_BONUS * cash
                print(f'Начислен процент {COUNT_OPERATIONS_BONUS * cash} за количество совершенных операций {count_operations}.')

            print(f'Текущий баланс: {balance}.')
        else:
            print(f'Сумма пополнения должна быть кратна {MULTIPLE_NUM}.')



    def withdrawal():
        """Функция снятия наличных."""
        nonlocal count_operations
        nonlocal balance

        cash = int(input(f'Сумма снятия должна быть кратна {MULTIPLE_NUM}. \nВведите значение: '))

        if balance > WEALTH_LIMIT:
            balance -= WEALTH_TAX * cash
            print(f'Вычтен налог на богатство {WEALTH_TAX * cash}.')

        if cash % MULTIPLE_NUM == 0:

            if WITHDRAWAL_FEE * cash < MIN_WITHDRAWAL_FEE:
                fee = MIN_WITHDRAWAL_FEE
            elif WITHDRAWAL_FEE * cash > MAX_WITHDRAWAL_FEE:
                fee = MAX_WITHDRAWAL_FEE
            else:
                fee = WITHDRAWAL_FEE * cash

            if balance > cash + fee:
                balance -= (cash + fee)
                count_operations += 1

                if count_operations % COUNT_OPERATIONS == 0:
                    balance += COUNT_OPERATIONS_BONUS * cash
                    print(f'Начислен процент {COUNT_OPERATIONS_BONUS * cash} за количество совершенных операций {count_operations}.')

                print(f'Комиссия за снятие составляет {fee}.\nТекущий баланс: {balance}. ')
            else:
                print(f'Недостаточно средств. \nТекущий баланс: {balance}')

        else:
            print(f'Сумма снятия должна быть кратна. {MULTIPLE_NUM}!')


    while True:
        operation = int(input('\nВыберите тип операции:\n1 - Узнать баланс\n2 - Внести наличные\
        \n3 - Снять наличные\n4 - Выйти'))

        if operation == 1:
            print(f'Текущий баланс: {balance}')
        elif operation == 2:
            deposit()
        elif operation == 3:
            withdrawal()
        else:
            break

main()