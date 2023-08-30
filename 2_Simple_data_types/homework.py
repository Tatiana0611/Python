# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

num = int(input('Введите целое число: '))

print(hex(num))

hex_digits = '0123456789ABCDEF'
result = ''

while num > 0:
    result = hex_digits[num % 16] + result
    num //= 16

print(result)


# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей. Для проверки своего
# кода используйте модуль fractions.

import math
import fractions

a1, b1 = map(int, input('Введите первую дробь: ').split('/'))
a2, b2 = map(int, input('Введите вторую дробь: ').split('/'))

f1 = fractions.Fraction(a1, b1)
f2 = fractions.Fraction(a2, b2)

def frac_reducing(x: int, y: int, s: str):
    if x % y == 0:
        print(f'{s}: {c // d}')
    else:
        print(f'{s}: {int(c / math.gcd(c, d))}/{int(d / math.gcd(c, d))}')


# Сложение дробей

c = a1*b2 + a2*b1
d = b1 * b2

frac_reducing(c, d, 'Сложение')
print(f'Сложение с использованием fractions: {f1 + f2}')

# Умножение дробей

c = a1 * a2
d = b1 * b2

frac_reducing(c, d, 'Умножение')
print(f'Умножение с использованием fractions: {f1 * f2}')


# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

balance = 0

# Функция внесения наличных
def deposit():
    global balance
    cash = int(input('Сумма пополнения должна быть кратна 50. \nВведите значение: '))
    if cash % 50 == 0:
        balance += cash
        print(f'Текущий баланс: {balance}')
    else:
        print('Сумма пополнения должна быть кратна 50!')

# Функция снятия наличных
def withdrawal():
    global balance
    cash = int(input('Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.\
    \nСумма снятия должна быть кратна 50. \nВведите значение: '))
    fee = 0.015 * cash

    if cash % 50 == 0:

        if fee < 30:
            temp = balance - (cash + 30)
        elif fee > 600:
            temp = balance - (cash + 600)
        else:
            temp = balance - (cash + fee)

        if temp > 0:
            balance = temp
            print(f'Текущий баланс: {balance}')
        else:
            print(f'Недостаточно средств. \nТекущий баланс: {balance}')

    else:
        print('Сумма снятия должна быть кратна 50!')


while True:
    operation = int(input('Выберите тип операции:\n1 - Узнать баланс\n2 - Внести наличные\
    \n3 - Снять наличные'))

    if operation == 1:
        print(f'Текущий баланс: {balance}')
    elif operation == 2:
        deposit()
    elif operation == 3:
        withdrawal()
    else:
        break