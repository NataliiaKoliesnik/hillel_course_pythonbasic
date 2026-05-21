# генераторна функція з використанням оператора yield, яка повертатиме
# по одному члену числової послідовності, закон якої задається за допомогою функції користувача

from typing import Callable
from collections.abc import Iterator

def my_pow(x):
    return x ** 2

def some_gen(begin: float | int, end: int, func: Callable[[int | float], int | float]) -> Iterator[int | float]:
    """
     begin: перший елемент послідовності
     end: кількість елементів у послідовності
     func: функція, яка формує значення для послідовності
    """
    new_elem = begin
    count = 1
    while count <= end:
         yield new_elem
         new_elem = func(new_elem)
         count += 1

from inspect import isgenerator

gen = some_gen(2, 4, my_pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')