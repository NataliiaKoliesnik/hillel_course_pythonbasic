# generator function for filling a list with cubes of numbers

from typing import Generator

def generate_cube_numbers(end: int) -> Generator[int, None, None]:
    """
    Generate cubes of numbers starting from 2 that are smaller than the given value.
    :param end: Upper limit for generated cube numbers
    :type end: int
    :return: Cube of the current number
    :rtype: Generator[int, None, None]
    """
    number = 2
    while True: # creating an infinite loop
        cube_of_number = number ** 3
        if cube_of_number > end: # break condition for an infinite loop
            return
        yield cube_of_number
        number += 1

from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'