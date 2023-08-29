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