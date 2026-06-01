# a prime number generator function

from typing import Generator

def prime_generator(end: int) -> Generator[int, None, None]:
    """
    Finds and prints all prime numbers from 2 up to the given limit (inclusive).
    A prime number is a natural number greater than 1 that is divisible only by 1 and by itself.
    :param end: The upper limit of the range. Must be an integer greater than or equal to 2.
    :type end: int
    :return: This function does not return anything; it only prints prime numbers.
    :rtype: Generator[int, None, None]
    """
    for dividend in range(2, end + 1):
        for divisor in range(2, dividend):
            if dividend % divisor == 0:
                break
        else:
            yield dividend

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')