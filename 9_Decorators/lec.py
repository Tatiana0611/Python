from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    def add_two_str(b: str) -> str:
        return a + ' ' + b
    return add_two_str


hello = add_one_str('Hello')
bye = add_one_str('Good bye')

print(hello('world!'))
print(hello('friend!'))
print(bye('wonderful world!'))

print(f'{type(add_one_str) = }, {add_one_str.__name__ = }, {id(add_one_str) = }')
print(f'{type(hello) = }, {hello.__name__ = }, {id(hello) = }')
print(f'{type(bye) = }, {bye.__name__ = }, {id(bye) = }')



from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    names = []

    def add_two_str(b: str) -> str:
        names.append(b)
        return a + ', ' + ', '.join(names)
    return add_two_str


hello = add_one_str('Hello')
bye = add_one_str('Good bye')

print(hello('Alex'))
print(hello('Karina'))
print(bye('Alina'))
print(hello('John'))
print(bye('Neo'))


from typing import Callable


def add_one_str(a: str) -> Callable[[str], str]:
    text = ''

    def add_two_str(b: str) -> str:
        nonlocal text
        text += ', ' + b
        return a + text
    return add_two_str


hello = add_one_str('Hello')
bye = add_one_str('Good bye')
print(hello('Alex'))
print(hello('Karina'))
print(bye('Alina'))
print(hello('John'))


from typing import Callable


def main(x: int) -> Callable[[int], dict[int, int]]:
    d = {}
    def loc(y: int) -> dict[int, int]:
        for i in range(y):
            d[i] = x ** i
        return d
    return loc


small = main(42)
big = main(73)

print(small(7))
print(big(7))
print(small(3))

def mean(*args):
    return sum(args) / len(args)
print(mean(*[1, 2, 3]))
print(mean(1, 2, 3, 5, 8))


import random
from typing import Callable


def cache(func: Callable):
    _cache_dict = {}
    def wrapper(*args):
        if args not in _cache_dict:
            _cache_dict[args] = func(*args)
        return _cache_dict[args]
    print(_cache_dict)
    return wrapper
@cache
def rnd(a: int, b: int) -> int:
    return random.randint(a, b)

print(f'{rnd(1, 10) = }')
print(f'{rnd(1, 10) = }')
print(f'{rnd(1, 10) = }')

